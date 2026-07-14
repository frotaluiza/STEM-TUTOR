"""
watch-opencode-db.py
====================
Continuous watcher for opencode SQLite database.
Polls the session table every N seconds, detects new/updated sessions,
and triggers the extraction + project state pipeline.

Usage:
    python scripts/kb/watch-opencode-db.py [--interval 30] [--settle 120]

Options:
    --interval N    Polling interval in seconds (default: 30)
    --settle N      Seconds of stability before considering session "done" (default: 120)
    --once          Run a single check and exit (for cron/task scheduler)
"""

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import time

# --- Paths ---
OPCODE_DB = os.path.expanduser(r'~\.local\share\opencode\opencode.db')
AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = AI_TUTOR_DIR / 'scripts' / 'kb'
STATE_DIR = AI_TUTOR_DIR / 'project-state'
SESSOES_DIR = AI_TUTOR_DIR / 'kb' / 'sessoes'
WATCHER_STATE = AI_TUTOR_DIR / 'scripts' / 'kb' / '.watcher_state.json'
LOG_FILE = AI_TUTOR_DIR / 'scripts' / 'kb' / 'watcher.log'

# --- Pipeline scripts ---
EXTRACT_SCRIPT = SCRIPTS_DIR / 'extract-live-docs.py'
CLASSIFY_SCRIPT = SCRIPTS_DIR / 'classify-sessions.py'
BUILD_SPACES_SCRIPT = SCRIPTS_DIR / 'build-project-spaces.py'
UPDATE_STATE_SCRIPT = SCRIPTS_DIR / 'update-project-state.py'

os.makedirs(SCRIPTS_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def log(msg, level='INFO'):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{ts}] [{level}] {msg}'
    print(line)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line + '\n')


# ---------------------------------------------------------------------------
# Watcher state persistence
# ---------------------------------------------------------------------------

def load_watcher_state():
    """Load last-known session timestamps."""
    if os.path.exists(WATCHER_STATE):
        try:
            with open(WATCHER_STATE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {'last_updated_map': {}, 'processed_sessions': []}


def save_watcher_state(state):
    with open(WATCHER_STATE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# SQLite polling
# ---------------------------------------------------------------------------

def get_sessions(cur):
    """Get all sessions with their metadata."""
    cur.execute('''
        SELECT slug, id, title, agent, time_created, time_updated, cost,
               tokens_input, tokens_output
        FROM session
        ORDER BY time_updated DESC
    ''')
    return {
        r[0]: {
            'id': r[1], 'title': r[2], 'agent': r[3],
            'time_created': r[4], 'time_updated': r[5],
            'cost': r[6] or 0, 'tokens_input': r[7] or 0,
            'tokens_output': r[8] or 0
        }
        for r in cur.fetchall()
    }


def detect_changes(state, current_sessions, settle_seconds):
    """
    Compare current state with last-known state.
    Returns: (new_sessions, updated_sessions_ready)
    """
    last_map = state.get('last_updated_map', {})
    processed = set(state.get('processed_sessions', []))
    now_ms = int(time.time() * 1000)

    new_sessions = []
    updated_ready = []

    for slug, info in current_sessions.items():
        last_ts = last_map.get(slug, 0)
        current_ts = info['time_updated']

        if not current_ts:
            continue

        if slug not in last_map:
            # New session — check if it has settled
            age_seconds = (now_ms - current_ts) / 1000
            if age_seconds >= settle_seconds and slug not in processed:
                new_sessions.append(slug)
        elif current_ts > last_ts and slug not in processed:
            # Updated session — check if it has settled
            time_since_update = (now_ms - current_ts) / 1000
            if time_since_update >= settle_seconds:
                updated_ready.append(slug)

    return new_sessions, updated_ready


# ---------------------------------------------------------------------------
# Pipeline execution
# ---------------------------------------------------------------------------

def run_pipeline(slug):
    """Run the full pipeline for a single session slug."""
    log(f'Pipeline triggered for: {slug}')
    success = True

    # Step 1: Extract live doc
    log('  Step 1: Extract live doc...')
    result = subprocess.run(
        [sys.executable, str(EXTRACT_SCRIPT), '--slug', slug],
        capture_output=True, text=True, timeout=120
    )
    if result.returncode != 0:
        log(f'  Step 1 FAILED: {result.stderr[:500]}', 'ERROR')
        success = False
    else:
        log('  Step 1 OK')

    # Step 2: Classification (runs for all but we need to pick up new one)
    log('  Step 2: Classify session...')
    result = subprocess.run(
        [sys.executable, str(CLASSIFY_SCRIPT)],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        log(f'  Step 2 FAILED: {result.stderr[:500]}', 'ERROR')
        success = False
    else:
        log('  Step 2 OK')

    # Step 3: Build project spaces
    log('  Step 3: Build project spaces...')
    result = subprocess.run(
        [sys.executable, str(BUILD_SPACES_SCRIPT)],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        log(f'  Step 3 FAILED: {result.stderr[:500]}', 'ERROR')
        success = False
    else:
        log('  Step 3 OK')

    # Step 4: Update project state (for stem tutor)
    log('  Step 4: Update project state...')
    result = subprocess.run(
        [sys.executable, str(UPDATE_STATE_SCRIPT)],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        log(f'  Step 4 FAILED: {result.stderr[:500]}', 'ERROR')
        # Non-fatal
    else:
        log('  Step 4 OK')

    # Step 5: Git commit + push to personal fork
    log('  Step 5: Git commit and push...')
    try:
        git_result = subprocess.run(
            ['git', 'add', '-f', 'kb/', 'scripts/kb/', 'project-state/'],
            capture_output=True, text=True, timeout=30, cwd=AI_TUTOR_DIR
        )
        if git_result.returncode == 0:
            git_result = subprocess.run(
                ['git', 'commit', '-m', f'auto: KB update from session {slug}', '--allow-empty'],
                capture_output=True, text=True, timeout=30, cwd=AI_TUTOR_DIR
            )
            if git_result.returncode == 0:
                push_result = subprocess.run(
                    ['git', 'push', 'personal', 'feature/mind-map-module'],
                    capture_output=True, text=True, timeout=60, cwd=AI_TUTOR_DIR
                )
                if push_result.returncode == 0:
                    log('  Step 5 OK — pushed to personal remote')
                else:
                    log(f'  Step 5 push stderr: {push_result.stderr[:300]}', 'WARN')
            else:
                log(f'  Step 5 commit: {git_result.stdout.strip()[:200]}', 'WARN')
        else:
            log(f'  Step 5 add FAILED: {git_result.stderr[:200]}', 'ERROR')
    except subprocess.TimeoutExpired:
        log('  Step 5 timed out', 'WARN')
    except Exception as e:
        log(f'  Step 5 error: {e}', 'WARN')

    if success:
        log(f'Pipeline completed for: {slug}')
    else:
        log(f'Pipeline completed with errors for: {slug}', 'WARN')

    return success


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def run_once(settle_seconds=120):
    """Single check cycle. Returns number of sessions processed."""
    try:
        conn = sqlite3.connect(OPCODE_DB)
        cur = conn.cursor()
        current_sessions = get_sessions(cur)
        conn.close()
    except sqlite3.Error as e:
        log(f'DB connection error: {e}', 'ERROR')
        return 0

    state = load_watcher_state()
    new_sessions, updated_ready = detect_changes(state, current_sessions, settle_seconds)

    processed_count = 0
    for slug in new_sessions + updated_ready:
        log(f'New/updated session detected: {slug}')
        if run_pipeline(slug):
            state.setdefault('processed_sessions', []).append(slug)
            processed_count += 1

    # Update the last-known timestamps
    state['last_updated_map'] = {
        slug: info['time_updated']
        for slug, info in current_sessions.items()
    }
    save_watcher_state(state)

    return processed_count


def run_forever(interval=30, settle=120):
    """Continuous polling loop."""
    log(f'Watcher started — polling every {interval}s, settle time {settle}s')
    log(f'  DB: {OPCODE_DB}')
    log(f'  Output: {SESSOES_DIR}')
    log('')

    while True:
        try:
            count = run_once(settle)
            if count:
                log(f'Cycle complete: {count} sessions processed')
        except KeyboardInterrupt:
            log('Watcher stopped by user')
            break
        except Exception as e:
            log(f'Cycle error: {e}', 'ERROR')

        time.sleep(interval)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Continuous watcher for opencode DB')
    parser.add_argument('--interval', type=int, default=30, help='Polling interval in seconds')
    parser.add_argument('--settle', type=int, default=120, help='Settle time in seconds before processing')
    parser.add_argument('--once', action='store_true', help='Run a single check and exit')
    parser.add_argument('--watchdog', action='store_true', help='Run with watchdog file for health checks')

    args = parser.parse_args()

    if args.watchdog:
        watchdog_path = AI_TUTOR_DIR / 'scripts' / 'kb' / '.watcher_healthy'
        log('Watchdog mode enabled')
        while True:
            try:
                run_once(args.settle)
                with open(watchdog_path, 'w') as f:
                    f.write(datetime.now().isoformat())
            except Exception as e:
                log(f'Watchdog cycle error: {e}', 'ERROR')
            time.sleep(args.interval)
    elif args.once:
        count = run_once(args.settle)
        log(f'One-shot check: {count} sessions processed')
    else:
        run_forever(args.interval, args.settle)


if __name__ == '__main__':
    main()
