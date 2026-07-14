"""
extract-live-docs.py — MAX DETAIL VERSION
========================================
Extract sessions from opencode.db → kb/sessoes/{slug}.md
Includes all 8 part types (text, reasoning, tool, file, step-start,
step-finish, compaction, agent) with minimal truncation.

Usage:
    python scripts/kb/extract-live-docs.py [--all] [--slug SLUG]

By default, only processes sessions tagged as 'AI STEM Tutor' in registry.
Use --all to process ALL 266 sessions, or --slug to process a single one.
"""

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sqlite3

# --- Constants ---
OPCODE_DB = os.path.expanduser(r'~\.local\share\opencode\opencode.db')
REGISTRY = os.path.expanduser(r'~\.local\share\opencode\session-registry\active.json')
AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
SESSOES_DIR = AI_TUTOR_DIR / 'kb' / 'sessoes'
PROJECT_NAME = 'AI STEM Tutor'
MAX_CMD_LEN = 10000
MAX_OUT_LEN = 15000

os.makedirs(SESSOES_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_registry():
    with open(REGISTRY, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_registry_map():
    return {e['slug']: e for e in load_registry()}


def parse_model_id(raw):
    if isinstance(raw, str):
        try:
            obj = json.loads(raw)
            return obj.get('id', obj.get('modelID', raw))
        except json.JSONDecodeError:
            return raw
    if isinstance(raw, dict):
        return raw.get('id', raw.get('modelID', 'unknown'))
    return 'unknown'


def fmt_ts(ms):
    if not ms:
        return ''
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def fmt_duration(start_ms, end_ms):
    if not start_ms or not end_ms:
        return ''
    s = (end_ms - start_ms) / 1000
    h, r = divmod(s, 3600)
    m, s = divmod(r, 60)
    return f'{int(h)}h{int(m):02d}m{int(s):02d}s'


def plural(n, s):
    return f'{n} {s}' if n == 1 else f'{n} {s}s'


# ---------------------------------------------------------------------------
# SQLite data access
# ---------------------------------------------------------------------------

def get_session_map(cur):
    cur.execute('''
        SELECT slug, id, title, project_id, agent, model,
               time_created, time_updated, cost,
               tokens_input, tokens_output, tokens_reasoning,
               tokens_cache_read, tokens_cache_write
        FROM session
    ''')
    m = {}
    for r in cur.fetchall():
        m[r[0]] = dict(zip(
            ['id', 'title', 'project_id', 'agent', 'model',
             'time_created', 'time_updated', 'cost',
             'tokens_input', 'tokens_output', 'tokens_reasoning',
             'tokens_cache_read', 'tokens_cache_write'],
            [r[1], r[2], r[3], r[4], r[5],
             r[6], r[7], r[8],
             r[9], r[10], r[11], r[12], r[13]]
        ))
    return m


def get_switches(cur, session_id):
    """Get agent/model switches from session_message table."""
    cur.execute('''
        SELECT type, data, time_created
        FROM session_message
        WHERE session_id = ?
        ORDER BY time_created ASC
    ''', (session_id,))
    switches = []
    for r in cur.fetchall():
        typ = r[0]
        try:
            data = json.loads(r[1])
        except json.JSONDecodeError:
            data = {}
        ts = r[2]
        if typ == 'agent-switched':
            switches.append({'type': 'agent', 'value': data.get('agent', '?'), 'time': ts})
        elif typ == 'model-switched':
            switches.append({'type': 'model', 'value': data.get('model', data.get('modelID', '?')), 'time': ts})
    return switches


def extract_messages(cur, session_id):
    """All messages + parts, ordered."""
    cur.execute('SELECT id, time_created, data FROM message WHERE session_id=? ORDER BY time_created ASC', (session_id,))
    messages = []
    for m_row in cur.fetchall():
        mid, mtime, mraw = m_row
        try:
            mdata = json.loads(mraw)
        except json.JSONDecodeError:
            mdata = {'role': 'unknown', 'raw': mraw[:300]}

        cur.execute('SELECT time_created, data FROM part WHERE message_id=? ORDER BY time_created ASC', (mid,))
        parts = []
        for p_row in cur.fetchall():
            try:
                parts.append(json.loads(p_row[1]))
            except json.JSONDecodeError:
                parts.append({'type': 'unknown', 'raw': p_row[1][:300]})

        messages.append({'id': mid, 'time': mtime, 'data': mdata, 'parts': parts})

    return messages


# ---------------------------------------------------------------------------
# Per-part-type renderers
# ---------------------------------------------------------------------------

def render_text(part):
    return part.get('text', '')


def render_reasoning(part, idx):
    text = part.get('text', '')
    if not text:
        return ''
    out = []
    out.append('<details open>')
    out.append(f'<summary>🧠 Raciocínio #{idx+1}</summary>')
    out.append('')
    out.append(text)
    out.append('')
    out.append('</details>')
    return '\n'.join(out)


def render_tool(part):
    tool_name = part.get('tool', 'unknown')
    state = part.get('state', {})
    inp = state.get('input', {}) if isinstance(state, dict) else {}
    cmd = inp.get('command', '') if isinstance(inp, dict) else ''
    status = state.get('status', '')
    meta = state.get('metadata', {}) if isinstance(state.get('metadata'), dict) else {}
    output = meta.get('output', '') if isinstance(meta, dict) else ''
    if not output and isinstance(state, dict):
        output = state.get('output', '')
    error = meta.get('error', '') if isinstance(meta, dict) else ''
    duration = ''
    if isinstance(state, dict) and 'time' in state:
        st = state['time'].get('start')
        en = state['time'].get('end')
        if st and en:
            duration = fmt_duration(st, en)

    out = []
    status_icon = '✅' if status == 'completed' else '❌' if status == 'error' else '⏳'
    info = f'{status_icon} **{tool_name}** ({status})'
    if duration:
        info += f' — {duration}'
    out.append(info)

    if cmd:
        cmd_text = cmd[:MAX_CMD_LEN]
        truncated = len(cmd) > MAX_CMD_LEN
        out.append('```bash')
        out.append(cmd_text)
        out.append('```')
        if truncated:
            out.append(f'*[Comando truncado: {len(cmd)} chars, exibindo {MAX_CMD_LEN}]*')

    if error:
        out.append(f'**Erro:** {error[:2000]}')
        if len(error) > 2000:
            out.append(f'*[Erro truncado: {len(error)} chars]*')

    if output:
        out_text = output[:MAX_OUT_LEN]
        truncated = len(output) > MAX_OUT_LEN
        out.append('**Output:**')
        out.append('```')
        out.append(out_text)
        out.append('```')
        if truncated:
            out.append(f'*[Output truncado: {len(output)} chars, exibindo {MAX_OUT_LEN}]*')

    return '\n'.join(out)


def render_file(part):
    fname = part.get('filename', part.get('path', 'unknown'))
    mime = part.get('mime', '')
    action = part.get('action', 'anexado')
    url = part.get('url', '')
    info = f'{action}: {fname}'
    if mime:
        info += f' ({mime})'
    if url and not url.startswith('data:'):
        info += f' — {url}'
    return info


def render_step(part, is_start):
    prefix = '▶️' if is_start else '⏹️'
    return f'{prefix} **{"Início" if is_start else "Fim"} do passo**'


def render_compaction(part):
    tail = part.get('tail_start_id', '')
    auto = part.get('auto', False)
    note = 'automática' if auto else 'manual'
    out = f'🔄 **Compactação de contexto ({note})**'
    if tail:
        out += f' — a partir de {tail[:20]}...'
    return out


def render_agent_delegation(part):
    agent_name = part.get('agent', part.get('name', 'subagente'))
    return f'🤖 **Subagente: {agent_name}**'


# ---------------------------------------------------------------------------
# Cross-message analysis
# ---------------------------------------------------------------------------

def find_decisions(all_text):
    decisions = set()
    patterns = [
        (r'(?:Decisão|Decisao)\s*(?:Arquitetural|arquitetural)?\s*:?\s*(.+?)(?=\n|$)', False),
        (r'[-*]\s*\*{0,2}(?:Contexto)\*{0,2}\s*:?\s*(.+?)(?=\s*[-*]\s*\*{0,2}(?:Escolha|Decisão|Decisao))', True),
        (r'(?:Escolha|Escolhi|Optamos|Vamos usar|Stack|Abordagem)\s*:?\s*(.+?)(?=\n[-*]|\n\n|\Z)', False),
    ]
    for pat, is_context in patterns:
        for m in re.finditer(pat, all_text, re.DOTALL | re.IGNORECASE):
            t = m.group(1).strip().strip('`').strip()
            if len(t) > 15:
                decisions.add(t)
    return list(decisions)[:20]


def count_parts(messages):
    return sum(len(m['parts']) for m in messages)


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

def build_frontmatter(slug, session_sql, registry_entry, msgs, switches):
    model_id = parse_model_id(session_sql.get('model'))

    tc = session_sql.get('time_created', 0)
    tu = session_sql.get('time_updated', 0)

    fm = {
        'slug': slug,
        'title': registry_entry.get('title', session_sql.get('title', '')),
        'date': fmt_ts(tc).split(' ')[0] if tc else '',
        'agent': registry_entry.get('agent', session_sql.get('agent', '')),
        'model': model_id,
        'project': registry_entry.get('project', PROJECT_NAME),
        'branch': registry_entry.get('branch', ''),
        'duration': fmt_duration(tc, tu),
        'messages': len(msgs),
        'parts': count_parts(msgs),
        'cost': session_sql.get('cost', 0) or 0,
        'tokens_input': session_sql.get('tokens_input', 0) or 0,
        'tokens_output': session_sql.get('tokens_output', 0) or 0,
        'tokens_reasoning': session_sql.get('tokens_reasoning', 0) or 0,
        'tokens_cache_read': session_sql.get('tokens_cache_read', 0) or 0,
        'tokens_cache_write': session_sql.get('tokens_cache_write', 0) or 0,
        'created': fmt_ts(tc) if tc else '',
        'updated': fmt_ts(tu) if tu else '',
    }
    return fm


# ---------------------------------------------------------------------------
# Main generation
# ---------------------------------------------------------------------------

def generate_live_doc(slug):
    print(f'  Processing: {slug}')

    conn = sqlite3.connect(OPCODE_DB)
    cur = conn.cursor()
    session_map = get_session_map(cur)
    registry_map = load_registry_map()

    if slug not in session_map:
        print('    SKIP: slug not found in SQLite')
        conn.close()
        return False

    session_sql = session_map[slug]
    registry_entry = registry_map.get(slug, {})
    session_id = session_sql['id']
    msgs = extract_messages(cur, session_id)
    switches = get_switches(cur, session_id)
    conn.close()

    if not msgs:
        print('    SKIP: no messages found')
        return False

    fm = build_frontmatter(slug, session_sql, registry_entry, msgs, switches)

    # Timeline of switches for inline annotation
    switch_times = {s['time']: s for s in switches}

    content = []
    # --- YAML frontmatter ---
    content.append('---')
    for k, v in fm.items():
        if isinstance(v, str):
            if ':' in v or v == '' or ' ' in v:
                content.append(f'{k}: "{v}"')
            else:
                content.append(f'{k}: {v}')
        elif isinstance(v, float):
            content.append(f'{k}: {v:.6f}')
        else:
            content.append(f'{k}: {v}')
    content.append('---')
    content.append('')

    # --- Session header ---
    part_count = count_parts(msgs)
    cost_str = f' | 💰 ${float(fm["cost"]):.4f}' if float(fm['cost']) > 0 else ''
    cache_str = ''
    if int(fm['tokens_cache_read']):
        cache_str = f' | 💾 cache read: {fmt_tokens(int(fm["tokens_cache_read"]))}'

    header = (
        f'Sessão com **{plural(len(msgs), "message")}**, '
        f'**{plural(part_count, "part")}**, '
        f'agente **{fm["agent"]}**, modelo **{fm["model"]}**'
        f'{cost_str}{cache_str}'
    )
    if fm.get('duration'):
        header += f' | ⏱️ {fm["duration"]}'
    content.append(header)
    content.append('')

    files_changed = {}
    commands_run = []
    all_text = ''
    # Track if this is first user message (for summary)
    first_user_encountered = False

    for msg in msgs:
        role = msg['data'].get('role', 'unknown')
        created = msg['data'].get('time', {}).get('created', msg['time'])
        completed = msg['data'].get('time', {}).get('completed', 0)
        ts = fmt_ts(created)

        # Check for switch at this message time
        switch_note = ''
        for st, sw in switch_times.items():
            if abs(st - created) < 1000:  # within 1 second
                if sw['type'] == 'agent':
                    switch_note = f'\n\n🔄 Agente → **{sw["value"]}**'
                elif sw['type'] == 'model':
                    switch_note = f'\n\n🔄 Modelo → **{sw["value"]}**'

        msg_parts_out = []

        # Collect all part content
        reasoning_parts = []
        text_parts = []
        tool_parts = []
        file_parts = []
        step_parts = []
        compaction_parts = []
        agent_parts = []

        for p in msg['parts']:
            typ = p.get('type', 'unknown')
            if typ == 'text':
                t = p.get('text', '')
                if t:
                    text_parts.append(t)
            elif typ == 'reasoning':
                r = p.get('text', '')
                if r:
                    reasoning_parts.append(r)
            elif typ == 'tool':
                tool_parts.append(render_tool(p))
            elif typ == 'file':
                file_parts.append(render_file(p))
            elif typ == 'step-start':
                step_parts.append(render_step(p, True))
            elif typ == 'step-finish':
                step_parts.append(render_step(p, False))
            elif typ == 'compaction':
                compaction_parts.append(render_compaction(p))
            elif typ == 'agent':
                agent_parts.append(render_agent_delegation(p))

        # --- Render the message ---
        if role == 'user':
            combined = '\n'.join(text_parts)
            if combined:
                all_text += combined + '\n'
                content.append(f'## 👤 Usuário ({ts}){switch_note}')
                content.append('')
                content.append(combined)
                content.append('')
                if not first_user_encountered:
                    first_user_encountered = True

        elif role == 'assistant':
            combined_text = '\n'.join(text_parts)
            if combined_text:
                all_text += combined_text + '\n'

            # Reasoning (inline, open by default)
            if reasoning_parts:
                content.append(f'## 🤖 Assistente ({ts}) — Raciocínio{switch_note}')
                content.append('')
                for i, r in enumerate(reasoning_parts):
                    content.append(render_reasoning({'text': r}, i))
                content.append('')

            # Response text
            if combined_text:
                # Only add a new header if there was no reasoning section
                if not reasoning_parts:
                    content.append(f'## 🤖 Assistente ({ts}){switch_note}')
                else:
                    content.append('### Resposta')
                content.append('')
                content.append(combined_text)
                content.append('')

        elif role == 'tool':
            # Tool messages: show tools
            if tool_parts:
                content.append(f'## 🔧 Ferramentas ({ts}){switch_note}')
                content.append('')
                for t in tool_parts:
                    content.append(t)
                    content.append('')

        # --- Shared: parts that appear regardless of role ---
        # Steps: only show as inline marker, skip if only single step-start/finish
        non_noise_steps = [s for s in step_parts if 'Início' not in s and 'Fim' not in s]
        if step_parts:
            # Too noisy - just count them
            start_count = sum(1 for s in step_parts if 'Início' in s)
            if start_count > 1:
                content.append(f'*{plural(start_count, "novo passo")} nesta mensagem*')
            elif start_count == 1:
                content.append('*Novo passo iniciado*')
            content.append('')

        if compaction_parts:
            content.append('### Contexto')
            content.append('')
            for c in compaction_parts:
                content.append(c)
            content.append('')

        if agent_parts:
            content.append('### Agentes')
            content.append('')
            for a in agent_parts:
                content.append(a)
            content.append('')

        # --- File tracking from tool responses ---
        for p in msg['parts']:
            if p.get('type') == 'file':
                path = p.get('path', p.get('filename', ''))
                if path and path != 'clipboard':
                    files_changed[path] = p.get('action', 'anexado')

        # --- Summary diffs (from assistant metadata) ---
        if role == 'assistant':
            s = msg['data'].get('summary')
            if s and isinstance(s, dict):
                diffs = s.get('diffs', [])
                for d in diffs:
                    if isinstance(d, dict):
                        p = d.get('path', '')
                        if p:
                            files_changed[p] = d.get('action', d.get('type', 'modificado'))

        # --- Commands from tool parts ---
        for p in msg['parts']:
            if p.get('type') == 'tool':
                state = p.get('state', {})
                inp = state.get('input', {}) if isinstance(state, dict) else {}
                cmd = inp.get('command', '') if isinstance(inp, dict) else ''
                if cmd:
                    commands_run.append(cmd)

        # --- Tool usage from tool-role messages ---
        if role == 'tool' and not tool_parts:
            pass  # handled above

    # --- Post-processing: decisions ---
    decisions = find_decisions(all_text)

    # --- Computed summary in frontmatter mode ---
    content.append('---')
    content.append('')
    content.append(f'*{plural(len(msgs), "message")} | {plural(part_count, "part")} | 💰 ${float(fm["cost"]):.4f} | ⏱️ {fm["duration"] if fm.get("duration") else "?"}*')
    content.append('')

    output_path = SESSOES_DIR / f'{slug}.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

    print(f'    OK: {output_path.name} ({plural(len(msgs), "msg")}, {plural(part_count, "part")}, cost=${float(fm["cost"]):.4f})')
    return True


def fmt_tokens(n):
    if n >= 1_000_000_000:
        return f'{n/1_000_000_000:.1f}B'
    if n >= 1_000_000:
        return f'{n/1_000_000:.1f}M'
    if n >= 1_000:
        return f'{n/1_000:.1f}K'
    return str(n)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Extract max-detail live docs from opencode SQLite')
    parser.add_argument('--all', action='store_true', help='Process ALL sessions')
    parser.add_argument('--slug', type=str, help='Process a single session slug')
    args = parser.parse_args()

    session_map = get_session_map(sqlite3.connect(OPCODE_DB).cursor())

    if args.slug:
        slugs = [args.slug]
    elif args.all:
        slugs = list(session_map.keys())
    else:
        slugs = [s['slug'] for s in load_registry()
                 if s.get('project') == PROJECT_NAME
                 and s['slug'] in session_map]

    slug_set = set(slugs)
    slugs_in_db = [s for s in slug_set if s in session_map]
    slugs_missing = slug_set - set(slugs_in_db)

    print(f'Extracting {len(slugs_in_db)} live docs')
    if slugs_missing:
        print(f'  ({len(slugs_missing)} slugs not found in DB, skipped)')

    ok = 0
    skipped = 0
    for slug in sorted(slugs_in_db):
        if generate_live_doc(slug):
            ok += 1
        else:
            skipped += 1

    print()
    print(f'Done: {ok} generated, {skipped} skipped')
    print(f'Output: {SESSOES_DIR}')


if __name__ == '__main__':
    main()
