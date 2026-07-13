"""
retrospective-decisions.py
==========================
Fast retrospective analysis of all sessions. Reads frontmatter + first/last
messages from each live doc and compiles per-project decision timelines.

Output:
  kb/projetos/{slug}/decisoes.md   — categorized decision timeline
  kb/projetos/{slug}/ideias.md     — tool references, ideas, conflicts
  project-state/{slug}.json        — updated with decisions
"""

import json
import os
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
SESSOES_DIR = AI_TUTOR_DIR / 'kb' / 'sessoes'
PROJETOS_DIR = AI_TUTOR_DIR / 'kb' / 'projetos'
STATE_DIR = AI_TUTOR_DIR / 'project-state'
CLASSIFICATION_FILE = SESSOES_DIR / 'classification.json'

PROJECT_META = {
    'tcc': {'name': 'TCC — Ingrid (MD/Desalination)', 'slug': 'tcc', 'area': 'Academico'},
    'ai-stem-tutor': {'name': 'AI STEM Tutor — DeepTutor', 'slug': 'ai-stem-tutor', 'area': 'IA'},
    'notion-infra': {'name': 'Notion Infrastructure', 'slug': 'notion-infra', 'area': 'Ferramentas'},
    'luc-repport': {'name': 'Luc-Repport', 'slug': 'luc-repport', 'area': 'Ferramentas'},
    'pinns': {'name': 'PINNs', 'slug': 'pinns', 'area': 'Academico'},
    'plex': {'name': 'Plex / Media', 'slug': 'plex', 'area': 'Pessoal'},
    'personal': {'name': 'Personal / PC', 'slug': 'personal', 'area': 'Pessoal'},
    'opencode-explore': {'name': 'OpenCode Exploration', 'slug': 'opencode-explore', 'area': 'Ferramentas'},
}


def parse_frontmatter(text):
    """Parse YAML frontmatter."""
    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if m:
        for line in m.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def get_first_user_message(text):
    """Get first user message content."""
    m = re.search(r'^## 👤 Usuário.*?\n\n(.*?)(?=\n##\s|\Z)', text, re.DOTALL)
    if m:
        raw = m.group(1).strip()
        raw = re.sub(r'<details>.*?</details>', '', raw, flags=re.DOTALL)
        return raw.strip()[:500]
    return ''


def get_all_user_messages(text):
    """Get all user messages."""
    msgs = re.findall(r'^## 👤 Usuário.*?\n\n(.*?)(?=\n##\s|\Z)', text, re.DOTALL)
    combined = []
    for m in msgs:
        m = re.sub(r'<details>.*?</details>', '', m, flags=re.DOTALL)
        combined.append(m.strip())
    return combined


def extract_decision_items(text):
    """Extract decision-like items from markdown text between --- sections."""
    items = []
    # Find sections between --- markers that contain decisions
    sections = re.split(r'\n---\n', text)
    for sec in sections:
        sec_lower = sec.lower()
        if 'decis' in sec_lower or 'arquitetur' in sec_lower or 'escolh' in sec_lower:
            lines = sec.split('\n')
            for line in lines:
                line_s = line.strip()
                if line_s.startswith('- **') or line_s.startswith('- *'):
                    items.append(line_s.lstrip('- '))
                elif line_s.startswith('- ') and len(line_s) > 30:
                    content = line_s[2:]
                    if any(kw in content.lower() for kw in ['stack', 'framework', 'api', 'usar', 'implement', 'criar', 'migrar', 'adicionar', 'alterar']):
                        items.append(content)
    return items[:10]


def extract_tool_references(text, title):
    """Extract technology/tool names from session context."""
    tools = set()
    patterns = [
        r'(?:Stack|Stack tecnol.gica|Tecnologias|Ferramentas)[:\-]\s*([^\n]+)',
        r'(?:API|Biblioteca|Framework)[:\-]\s*([^\n]+)',
        r'(?i)(?:Usando|Utilizando|Implementado com)\s+([A-Z][A-Za-z0-9.+/-]{2,40})',
    ]
    for pat in patterns:
        for m in re.finditer(pat, text):
            val = m.group(1).strip()[:100]
            if val and len(val) > 2:
                tools.add(val)
    # Also extract capital-letter technology names from first message
    first = get_first_user_message(text)
    techs = re.findall(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)+)\b', first)
    for t in techs:
        if len(t) > 4:
            tools.add(t)
    return sorted(tools)


# ---------------------------------------------------------------------------

def analyze_session(slug):
    """Analyze a single session and return structured data."""
    path = SESSOES_DIR / f'{slug}.md'
    if not path.exists():
        return None

    text = path.read_text(encoding='utf-8')
    fm = parse_frontmatter(text)
    first_msg = get_first_user_message(text)
    all_msgs = get_all_user_messages(text)
    decisions = extract_decision_items(text)
    tools = extract_tool_references(text, fm.get('title', ''))

    return {
        'slug': slug,
        'title': fm.get('title', slug),
        'date': fm.get('date', ''),
        'agent': fm.get('agent', ''),
        'cost': float(fm.get('cost', 0)),
        'first_message': first_msg,
        'message_count': len(all_msgs),
        'decisions': decisions,
        'tools': tools,
    }


# ---------------------------------------------------------------------------

def build_project_timeline(project_slug):
    """Build a chronological timeline of sessions for a project."""
    classification = json.loads(open(CLASSIFICATION_FILE, 'r', encoding='utf-8').read())

    sessions_data = []
    all_tools = set()
    all_decisions = []

    session_files = sorted(SESSOES_DIR.glob('*.md'))
    for sf in session_files:
        slug = sf.stem
        if slug not in classification.get('classification', {}):
            continue
        info = classification['classification'][slug]
        if info.get('project_slug') != project_slug:
            continue

        data = analyze_session(slug)
        if data:
            sessions_data.append(data)
            all_decisions.extend(data['decisions'])
            all_tools.update(data['tools'])

    # Sort by date descending
    sessions_data.sort(key=lambda s: s.get('date', ''), reverse=True)

    # Categorize decisions
    by_category = defaultdict(list)
    for d in all_decisions:
        cat = 'other'
        text = d.lower()
        if any(k in text for k in ['stack', 'framework', 'api', 'biblioteca', 'linguagem']):
            cat = 'tooling'
        elif any(k in text for k in ['arquitetur', 'modulo', 'serviço', 'componente', 'pipeline']):
            cat = 'architecture'
        elif any(k in text for k in ['modelo', 'llm', 'gpt', 'deepseek', 'treinamento']):
            cat = 'model'
        elif any(k in text for k in ['interface', 'ui', 'frontend', 'component', 'tela', 'visualiza']):
            cat = 'ui-ux'
        elif any(k in text for k in ['dado', 'database', 'banco', 'kb', 'rag', 'documento']):
            cat = 'data'
        by_category[cat].append(d)

    return {
        'sessions': sessions_data,
        'total_sessions': len(sessions_data),
        'total_cost': sum(s['cost'] for s in sessions_data),
        'decisions': all_decisions,
        'tools': sorted(all_tools),
        'by_category': dict(by_category),
    }


# ---------------------------------------------------------------------------

def write_timeline_md(meta, data):
    """Write kb/projetos/{slug}/decisoes.md — timeline of sessions."""
    proj_dir = PROJETOS_DIR / meta['slug']
    os.makedirs(proj_dir, exist_ok=True)

    lines = []
    lines.append(f'# Decisões e Timeline — {meta["name"]}')
    lines.append('')
    lines.append(f'**{data["total_sessions"]} sessões** | **${data["total_cost"]:.2f} custo total**')
    if data['decisions']:
        lines.append(f'**{len(data["decisions"])} decisões extraídas**')
    if data['tools']:
        lines.append(f'**{len(data["tools"])} ferramentas/tecnologias referenciadas**')
    lines.append('')

    # Summary by category
    if data['by_category']:
        lines.append('## Decisões por Categoria')
        lines.append('')
        cat_names = {
            'architecture': 'Arquitetura',
            'tooling': 'Ferramentas / Stack',
            'model': 'Modelo / LLM',
            'data': 'Dados / KB',
            'ui-ux': 'Interface / UX',
            'other': 'Outros',
        }
        for cat_key in ['architecture', 'tooling', 'model', 'data', 'ui-ux', 'other']:
            items = data['by_category'].get(cat_key, [])
            if items:
                lines.append(f'### {cat_names.get(cat_key, cat_key)} ({len(items)})')
                lines.append('')
                for item in items[:15]:
                    lines.append(f'- {item}')
                if len(items) > 15:
                    lines.append(f'  *+{len(items)-15} mais...*')
                lines.append('')

    # Session timeline
    lines.append('')
    lines.append('## Timeline de Sessões')
    lines.append('')
    lines.append(f'| Data | Título | Agente | Custo | Resumo |')
    lines.append(f'|------|--------|--------|-------|--------|')

    for s in data['sessions']:
        date_str = s.get('date', '')[:10]
        title = s['title'][:60].replace('|', '/')
        agent = s.get('agent', '')[:8]
        cost_str = f'${s["cost"]:.2f}' if s['cost'] else ''
        summary = s['first_message'][:80].replace('\n', ' ').replace('|', '/') if s['first_message'] else ''
        link = f'[ver](sessoes/{s["slug"]}.md)'
        lines.append(f'| {date_str} | [{title}](sessoes/{s["slug"]}.md) | {agent} | {cost_str} | {summary} |')

    lines.append('')

    output_path = proj_dir / 'decisoes.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  {output_path} ({data["total_sessions"]} sessoes)')


def write_ideias_md(meta, data):
    """Write kb/projetos/{slug}/ideias.md."""
    proj_dir = PROJETOS_DIR / meta['slug']
    os.makedirs(proj_dir, exist_ok=True)

    lines = []
    lines.append(f'# Ideias e Referências — {meta["name"]}')
    lines.append('')

    # Technologies used
    if data['tools']:
        lines.append('## 🛠️ Stack e Tecnologias')
        lines.append('')
        for t in data['tools']:
            lines.append(f'- {t}')
        lines.append('')

    # Session first-message ideas (goals of each session)
    lines.append('## 💡 Objetivos por Sessão')
    lines.append('')
    for s in data['sessions']:
        if s['first_message']:
            goal = s['first_message'][:200].replace('\n', ' ')
            lines.append(f'- **{s["title"]}** ({s["date"]})')
            lines.append(f'  → {goal}')
            lines.append('')

    lines.append('')
    output_path = proj_dir / 'ideias.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  {output_path}')


def update_state_with_decisions(meta, data):
    """Update project-state with accumulated knowledge."""
    state_file = STATE_DIR / f'{meta["slug"]}.json'
    state = {'project': meta['name'], 'slug': meta['slug'], 'sessions': []}
    if state_file.exists():
        try:
            state = json.loads(state_file.read_text(encoding='utf-8-sig'))
        except (json.JSONDecodeError, OSError):
            pass

    state['total_decisions'] = len(data['decisions'])
    state['total_tools'] = len(data['tools'])
    state['total_sessions_analyzed'] = data['total_sessions']
    state['last_decision_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    state['decisions'] = data['decisions'][:100]
    state['tools'] = data['tools'][:50]

    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    print(f'  {state_file}')


# ---------------------------------------------------------------------------

def main():
    import sys
    print('=== Análise Retrospectiva de Decisões ===\n')

    classification = json.loads(open(CLASSIFICATION_FILE, 'r', encoding='utf-8').read())

    project_slugs = set()
    for info in classification.get('classification', {}).values():
        slug = info.get('project_slug', '')
        if slug and slug not in ('empty', 'unclassified'):
            project_slugs.add(slug)

    # Optionally filter to one project
    target = sys.argv[1] if len(sys.argv) > 1 else None

    for slug in sorted(project_slugs):
        if target and slug != target:
            continue
        meta = PROJECT_META.get(slug, {'name': slug, 'slug': slug})
        print(f'\n--- {meta["name"]} ---')
        data = build_project_timeline(slug)
        write_timeline_md(meta, data)
        write_ideias_md(meta, data)

        if slug == 'ai-stem-tutor':
            update_state_with_decisions(meta, data)

        print(f'     {data["total_sessions"]} sessoes, {len(data["decisions"])} decisoes, {len(data["tools"])} ferramentas')

    print('\n=== Concluído ===')
    print(f'Outputs: {PROJETOS_DIR}/{target or "{projeto}"}/decisoes.md')
    print(f'         {PROJETOS_DIR}/{target or "{projeto}"}/ideias.md')


if __name__ == '__main__':
    main()
