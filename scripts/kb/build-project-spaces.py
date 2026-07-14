"""
build-project-spaces.py
=======================
Reads kb/sessoes/classification.json + all live docs,
groups by project, and generates per-project state files.

Output:
  kb/projetos/{slug}/
    index.md           — Project overview with session list
    sessoes/           — Symlinks or copies of relevant session live docs
  Also updates project-state/ for projects that already have one.
"""

from datetime import datetime
import json
import os
from pathlib import Path
import re
import shutil

AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
SESSOES_DIR = AI_TUTOR_DIR / 'kb' / 'sessoes'
PROJETOS_DIR = AI_TUTOR_DIR / 'kb' / 'projetos'
CLASSIFICATION_FILE = SESSOES_DIR / 'classification.json'
STATE_DIR = AI_TUTOR_DIR / 'project-state'

PROJECT_META = {
    'tcc': {
        'name': 'TCC — Ingrid (MD/Desalination)',
        'slug': 'tcc',
        'area': 'Academico',
        'repo': '',
        'desc': 'Trabalho de Conclusao de Curso sobre dessalinizacao por membranas (MD/VMD), modelagem 0D, PINNs, e geracao de slides.'
    },
    'ai-stem-tutor': {
        'name': 'AI STEM Tutor — DeepTutor',
        'slug': 'ai-stem-tutor',
        'area': 'IA',
        'repo': 'https://github.com/frotaluiza/STEM-TUTOR',
        'desc': 'Tutor STEM inteligente baseado no HKU DeepTutor. Inclui fork pessoal com NoteBlocks, Mind Maps, e framework de projetos.'
    },
    'notion-infra': {
        'name': 'Notion Infrastructure',
        'slug': 'notion-infra',
        'area': 'Ferramentas',
        'repo': '',
        'desc': 'Automacoes e integracoes com Notion: databases, sync, guidelines, test reports, rotinas.'
    },
    'luc-repport': {
        'name': 'Luc-Repport',
        'slug': 'luc-repport',
        'area': 'Ferramentas',
        'repo': '',
        'desc': 'Ferramenta de geracao de relatorios Luc-Repport.'
    },
    'pinns': {
        'name': 'PINNs',
        'slug': 'pinns',
        'area': 'Academico',
        'repo': '',
        'desc': 'Physics-Informed Neural Networks para modelagem de processos de dessalinizacao.'
    },
    'plex': {
        'name': 'Plex / Media',
        'slug': 'plex',
        'area': 'Pessoal',
        'repo': '',
        'desc': 'Gerenciamento de midia Plex, Radarr, etc.'
    },
    'personal': {
        'name': 'Personal / PC',
        'slug': 'personal',
        'area': 'Pessoal',
        'repo': '',
        'desc': 'Configuracoes pessoais, diagnostico de PC, exploracoes diversas.'
    },
    'opencode-explore': {
        'name': 'OpenCode Exploration',
        'slug': 'opencode-explore',
        'area': 'Ferramentas',
        'repo': '',
        'desc': 'Sessoes de exploracao do proprio OpenCode (SQLite, project-manager, etc).'
    },
    'empty': {
        'name': 'Empty (no content)',
        'slug': 'empty',
        'area': '',
        'repo': '',
        'desc': 'Sessoes vazias sem conteudo gerado.'
    },
}


def ensure_dir(d):
    os.makedirs(d, exist_ok=True)


def load_classification():
    with open(CLASSIFICATION_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_projects():
    """Group sessions by project and build per-project space."""
    data = load_classification()
    classification = data['classification']

    # Group by project
    projects = {}
    for slug, info in classification.items():
        proj_slug = info['project_slug']
        if proj_slug not in projects:
            projects[proj_slug] = {
                'slug': proj_slug,
                'meta': PROJECT_META.get(proj_slug, {'name': proj_slug, 'slug': proj_slug, 'area': '', 'repo': '', 'desc': ''}),
                'sessions': []
            }
        projects[proj_slug]['sessions'].append({
            'slug': slug,
            'title': info['title'],
            'date': info['date'],
            'agent': info['agent'],
            'model': info['model'],
            'cost': info['cost']
        })

    # Sort sessions within each project by date descending
    for proj in projects.values():
        proj['sessions'].sort(key=lambda s: s.get('date', ''), reverse=True)

    return projects


def count_cost(sessions):
    return sum(s.get('cost', 0) for s in sessions)


def write_project_index(proj):
    """Write kb/projetos/{slug}/index.md"""
    proj_dir = PROJETOS_DIR / proj['slug']
    ensure_dir(proj_dir)
    sessoes_link_dir = proj_dir / 'sessoes'
    ensure_dir(sessoes_link_dir)

    meta = proj['meta']
    sessions = proj['sessions']
    total_cost = count_cost(sessions)
    total_msgs = 0
    total_parts = 0

    lines = []
    lines.append(f'# {meta["name"]}')
    lines.append('')
    if meta.get('desc'):
        lines.append(f'{meta["desc"]}')
        lines.append('')
    if meta.get('area'):
        lines.append(f'- **Area:** {meta["area"]}')
    if meta.get('repo'):
        lines.append(f'- **Repo:** {meta["repo"]}')
    lines.append(f'- **Sessoes:** {len(sessions)}')
    lines.append(f'- **Custo total:** ${total_cost:.2f}')
    lines.append('')

    lines.append('## Sessoes')
    lines.append('')
    lines.append('| Data | Titulo | Agente | Custo |')
    lines.append('|------|--------|--------|-------|')

    for s in sessions:
        cost_str = f'${s["cost"]:.2f}' if s['cost'] else ''
        date_str = s.get('date', '')[:10]
        title = s['title'][:60].replace('|', '/')
        agent = s.get('agent', '')
        # Create symlink/copy to project's sessoes dir
        src = SESSOES_DIR / f'{s["slug"]}.md'
        dst = sessoes_link_dir / f'{s["slug"]}.md'
        if src.exists() and not dst.exists():
            try:
                shutil.copy2(src, dst)
            except Exception:
                pass
        lines.append(f'| {date_str} | [{title}](sessoes/{s["slug"]}.md) | {agent} | {cost_str} |')

    lines.append('')

    index_path = proj_dir / 'index.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  {index_path}')


def update_stem_tutor_state(project):
    """Update project-state/ai-stem-tutor.json with all AI STEM Tutor sessions."""
    state_file = STATE_DIR / 'ai-stem-tutor.json'
    sessions = project['sessions']

    state = {
        'project': 'AI STEM Tutor',
        'slug': 'ai-stem-tutor',
        'sessions': [],
        'total_sessions': len(sessions),
        'total_cost': count_cost(sessions),
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    for s in sessions:
        # Read live doc for summary
        live_doc = SESSOES_DIR / f'{s["slug"]}.md'
        summary = ''
        if live_doc.exists():
            text = live_doc.read_text(encoding='utf-8')
            m = re.search(r'^## 👤 Usuário.*?\n\n(.*?)(?=\n##\s|\Z)', text, re.DOTALL)
            if m:
                raw = m.group(1).strip()
                raw = re.sub(r'<details>.*?</details>', '', raw, flags=re.DOTALL)
                summary = raw.strip()[:300]

        entry = {
            'id': s['slug'],
            'title': s['title'],
            'date': s['date'],
            'agent': s['agent'],
            'cost': s['cost'],
            'summary': summary
        }
        state['sessions'].append(entry)

    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    print(f'  {state_file} ({len(sessions)} sessions)')


def main():
    print('Building project spaces...')
    print()
    projects = build_projects()

    for proj_slug, proj in sorted(projects.items()):
        if proj_slug == 'empty':
            continue
        print(f'  {proj["meta"]["name"]}: {len(proj["sessions"])} sessions')
        write_project_index(proj)

    print()
    print('Updating project-state for STEM TUTOR...')
    if 'ai-stem-tutor' in projects:
        update_stem_tutor_state(projects['ai-stem-tutor'])
    print()
    print('Done!')

    print('\n Summary:')
    print(f'  Projects: {len([p for p in projects if p != "empty"])}')
    total_sessions = sum(len(proj['sessions']) for proj in projects.values() if proj['slug'] != 'empty')
    print(f'  Total classified sessions: {total_sessions}')
    print(f'  Output: {PROJETOS_DIR}')


if __name__ == '__main__':
    main()
