"""
update-project-state.py
=======================
Reads kb/sessoes/*.md live docs and updates project-state/ai-stem-tutor.json
and project-state/ai-stem-tutor.md.

Usage:
    python scripts/kb/update-project-state.py
"""

import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
SESSOES_DIR = AI_TUTOR_DIR / 'kb' / 'sessoes'
PROJECT_STATE_DIR = AI_TUTOR_DIR / 'project-state'
STATE_JSON = PROJECT_STATE_DIR / 'ai-stem-tutor.json'
STATE_MD = PROJECT_STATE_DIR / 'ai-stem-tutor.md'

PROJECT_NAME = 'AI STEM Tutor'
PROJECT_SLUG = 'ai-stem-tutor'

os.makedirs(PROJECT_STATE_DIR, exist_ok=True)


def parse_frontmatter(text):
    """Parse YAML frontmatter from markdown."""
    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if m:
        for line in m.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                fm[k] = v
    return fm


def extract_sections(text):
    """Extract structured sections from markdown body."""
    sections = {}

    # Find all ## headers and capture content until next ##
    pattern = r'^##\s+(.*?)$\n(.*?)(?=^##\s|\Z)'
    matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
    for title, content in matches:
        sections[title.strip().lower()] = content.strip()

    # Extract decisions between --- markers (heuristic)
    decisions = []
    decision_section = sections.get('decisões', '') or sections.get('decisoes', '')
    if decision_section:
        for line in decision_section.split('\n'):
            line = line.strip()
            if line.startswith('- **') or line.startswith('- *'):
                decisions.append(line.lstrip('- '))

    # Extract files
    files = []
    files_section = sections.get('arquivos alterados', '') or sections.get('arquivos alterados', '')
    if files_section:
        for line in files_section.split('\n'):
            line = line.strip()
            if line.startswith('- '):
                files.append(line[2:])

    # Extract todos from the content
    todos = []
    for line in text.split('\n'):
        line = line.strip()
        if re.match(r'^[-*]\s*(?:TODO|Fazer|Implementar|Criar|Adicionar|Refatorar|Pr[óo]ximo)', line, re.IGNORECASE):
            todos.append(line.lstrip('-* '))

    return {
        'decisions': decisions[:20],
        'files': files[:20],
        'todos': todos[:10]
    }


def get_git_info():
    """Get current git branch and recent log."""
    branch = ''
    git_log = ''
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True, text=True, cwd=AI_TUTOR_DIR, timeout=10
        )
        if result.returncode == 0:
            branch = result.stdout.strip()
    except Exception:
        pass

    try:
        result = subprocess.run(
            ['git', 'log', '--oneline', '-15'],
            capture_output=True, text=True, cwd=AI_TUTOR_DIR, timeout=10
        )
        if result.returncode == 0:
            git_log = result.stdout.strip()
    except Exception:
        pass

    return branch, git_log


def load_state():
    """Load existing project state or create default."""
    if STATE_JSON.exists():
        with open(STATE_JSON, 'r', encoding='utf-8-sig') as f:
            return json.load(f)
    return {
        'project': PROJECT_NAME,
        'slug': PROJECT_SLUG,
        'created': datetime.now(timezone.utc).isoformat(),
        'last_updated': '',
        'branch': '',
        'last_commit': '',
        'git_log': '',
        'sessions': [],
        'decisions': [],
        'issues': [],
        'todos': []
    }


def build_state():
    """Build project state from live docs."""
    state = load_state()
    branch, git_log = get_git_info()

    state['branch'] = branch or state.get('branch', '')
    if git_log:
        state['git_log'] = git_log
        first_commit = git_log.split('\n')[0] if git_log else ''
        state['last_commit'] = first_commit

    # Process all live docs
    all_decisions = set()
    all_todos = []

    session_files = sorted(SESSOES_DIR.glob('*.md'), key=lambda p: p.stat().st_mtime, reverse=True)

    # Build session index from current state
    existing_sessions = {s['id']: s for s in state.get('sessions', [])}

    new_sessions = []
    seen_ids = set()

    for sf in session_files:
        slug = sf.stem
        if slug in seen_ids:
            continue
        seen_ids.add(slug)

        text = sf.read_text(encoding='utf-8')
        fm = parse_frontmatter(text)
        sections = extract_sections(text)

        # Build summary from first user message (exclude reasoning/details blocks)
        summary = ''
        user_msg_match = re.search(r'^## 👤.*?\n\n(.*?)(?=\n#{1,6}\s|\Z)', text, re.MULTILINE | re.DOTALL)
        if user_msg_match:
            raw = user_msg_match.group(1).strip()
            # Strip <details> blocks (reasoning)
            raw = re.sub(r'<details>.*?</details>', '', raw, flags=re.DOTALL)
            summary = raw.strip()[:500]

        session_entry = {
            'id': slug,
            'title': fm.get('title', slug),
            'date': fm.get('date', ''),
            'agent': fm.get('agent', ''),
            'model': fm.get('model', ''),
            'cost': float(fm.get('cost', 0)),
            'tokens_input': int(fm.get('tokens_input', 0)) if fm.get('tokens_input', '0').isdigit() else 0,
            'tokens_output': int(fm.get('tokens_output', 0)) if fm.get('tokens_output', '0').isdigit() else 0,
            'summary': summary,
            'decisions': sections.get('decisions', []),
            'files': sections.get('files', []),
            'todos': sections.get('todos', [])
        }

        new_sessions.append(session_entry)
        all_decisions.update(sections.get('decisions', []))
        all_todos.extend(sections.get('todos', []))

    # Update state (sort by date descending)
    new_sessions.sort(key=lambda s: s.get('date', ''), reverse=True)
    state['sessions'] = new_sessions
    state['decisions'] = list(all_decisions)
    state['todos'] = all_todos[:30]
    state['last_updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

    return state


def save_json(state):
    """Save project state as JSON."""
    with open(STATE_JSON, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    print(f'JSON: {STATE_JSON}')


def save_markdown(state):
    """Save project state as human-readable markdown."""
    lines = []
    lines.append(f'# Project State: {state["project"]}')
    lines.append('')
    lines.append('## Versão')
    lines.append(f'- **Branch:** {state.get("branch", "")}')
    lines.append(f'- **Último commit:** {state.get("last_commit", "")}')
    lines.append(f'- **Última atualização:** {state.get("last_updated", "")}')
    lines.append('')

    if state.get('git_log'):
        lines.append('## Git Log (últimos 15 commits)')
        for c in state['git_log'].split('\n')[:15]:
            lines.append(f'- {c}')
        lines.append('')

    sessions = state.get('sessions', [])
    lines.append(f'## Sessões ({len(sessions)})')
    lines.append('')
    for s in sessions[:30]:
        agent_info = f" agent={s.get('agent', '')}" if s.get('agent') else ''
        cost_info = f" cost=${float(s.get('cost', 0)):.4f}" if s.get('cost') else ''
        lines.append(f'- {s["date"]}: **{s["title"]}** ({s["id"]}){agent_info}{cost_info}')
        summary = s.get('summary', '')
        if summary:
            lines.append(f'  - {summary[:200]}')
        if s.get('decisions'):
            for d in s['decisions'][:3]:
                lines.append(f'  - 🔧 {d[:150]}')
        if s.get('files'):
            for f in s['files'][:3]:
                lines.append(f'  - 📄 {f[:120]}')
        lines.append('')

    decisions = state.get('decisions', [])
    if decisions:
        lines.append('## Decisões Acumuladas')
        for d in decisions[:20]:
            lines.append(f'- {d}')
        lines.append('')

    issues = state.get('issues', [])
    lines.append('## Issues Conhecidas')
    if issues:
        for i in issues:
            lines.append(f'- {i}')
    else:
        lines.append('Nenhuma registrada')
    lines.append('')

    todos = state.get('todos', [])
    lines.append('## Próximos Passos (Top 10)')
    if todos:
        for t in todos[:10]:
            lines.append(f'- [ ] {t}')
    else:
        lines.append('Nenhum registrado')
    lines.append('')

    lines.append('---')
    lines.append(f'*Auto-gerado por update-project-state.py em {datetime.now().strftime("%Y-%m-%d %H:%M")}*')
    lines.append('')

    with open(STATE_MD, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'MD:  {STATE_MD}')


def main():
    print('Building project state from live docs...')
    state = build_state()
    save_json(state)
    save_markdown(state)
    print(f'\n{len(state["sessions"])} sessions processed')
    print(f'{len(state["decisions"])} decisions accumulated')
    print(f'{len(state["todos"])} todos extracted')


if __name__ == '__main__':
    main()
