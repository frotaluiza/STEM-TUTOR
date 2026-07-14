"""
classify-sessions.py
====================
Reads kb/sessoes/*.md, classifies each session to a project
based on title + first user message + agent + CWD patterns.

Output:
  - kb/sessoes/classification.json (slug → project mapping)
  - Prints summary of classification results
"""

import os
import re
import json
from pathlib import Path

AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
SESSOES_DIR = AI_TUTOR_DIR / 'kb' / 'sessoes'
CLASSIFICATION_FILE = SESSOES_DIR / 'classification.json'

# ---------------------------------------------------------------------------
# Classification rules (ordered by priority)
# ---------------------------------------------------------------------------

def compile_rules():
    """Returns list of (project_slug, project_name, matcher_function)."""
    rules = []

    def add(slug, name, keywords_title, keywords_user=None, agents=None):
        def matcher(fm, first_user_msg):
            title = fm.get('title', '').lower()
            agent = fm.get('agent', '').lower()

            # Agent filter
            if agents and agent not in agents:
                return False

            # Title keywords (primary signal)
            title_match = any(k.lower() in title for k in keywords_title)

            # User message keywords (secondary signal — only if no title match)
            user_match = False
            if not title_match and keywords_user and first_user_msg:
                user_msg_lower = first_user_msg.lower()
                user_match = any(k.lower() in user_msg_lower for k in keywords_user)

            return title_match or user_match

        rules.append((slug, name, matcher))

    # --- Luc-Repport ---
    add('luc-repport', 'Luc-Repport', [
        'luc-repport', 'luc repport', '(fork #',
    ])

    # --- PINNs ---
    add('pinns', 'PINNs', [
        'pinn', 'physics-informed',
    ], agents=['build', 'plan', 'explore', 'general'])

    # --- Plex / Media ---
    add('plex', 'Plex / Media', [
        'plex', 'radarr',
    ])

    # --- Music / Estudos ---
    add('estudos', 'Estudos / Music', [
        'music', 'estudo', 'teoria musical',
    ], agents=['build', 'explore'])

    # --- AI STEM Tutor / DeepTutor ---
    add('ai-stem-tutor', 'AI STEM Tutor — DeepTutor', [
        'stem tutor', 'stem_tutor', 'deeptutor', 'deep tutor',
        'mind-map', 'mindmap', 'noteblocks', 'note block',
        'deepseek deep', 'mcp sci-hub', 'sci-hub mcp',
        'caminhos do xadrez', 'project mind map',
        'tutor project structure',
    ], keywords_user=[
        'stem tutor', 'deeptutor', 'deep tutor',
        'mind map', 'noteblocks', 'deep tutor',
    ])

    # --- OpenCode exploration ---
    add('opencode-explore', 'OpenCode Exploration', [
        'explore opencode', 'opencode sqlite', 'project-manager',
        'opencode project',
    ], keywords_user=[
        'opencode sqlite', 'opencode database',
    ])

    # --- Notion / Infrastructure ---
    add('notion-infra', 'Notion Infrastructure', [
        'notion', 'guidelines', 'register session', 'reformat session',
        'push-to-notion', 'exportar-sessao', 'upload session',
        'documentar teste', 'criar database', 'page id lookup',
        '@session subagent', '@general subagent', 'test report',
        'central de noticias', '@update-guidelines',
        'checkboxes', 'tarefas', 'conversa continua',
    ], keywords_user=[
        'notion', 'guidelines', 'test report', 'criar database',
        'registrar sess', 'database de rotinas',
    ])

    # --- TCC / Ingrid (MD / Desalination) - comes after Notion to avoid false positives ---
    add('tcc', 'TCC — Ingrid (MD/Desalination)', [
        'tcc', 'ingrid', 'desalination', 'vmd', 'fluxo',
        'rmse', '0d ', 'md model',
        'surrogate', 'fluxograma', 'overlay plot', 'ode', 'slide',
        'per-output rmse', 'find 0d', 'find overlay',
        'extract ode', 'find fluxograma', 'lista de arquivos',
        'analise slide', 'todas as se',
        'pagina dashboard', 'dashboard 2026',
    ], keywords_user=[
        'tcc', 'ingrid', 'desalination', 'md model',
        'vmd', 'fluxo capilar', '0d model', 'pinn',
        'separa', 'memdist', 'surrogate', 'slide',
        'dashboard', 'desalination',
    ])

    # --- Personal / PC --- (catch-all for remaining)
    add('personal', 'Personal / PC', [
        'lentidao', 'bonjour', 'monitoramento',
        'aba de monitoramento', 'comando de voz',
        'notebooklm', 'opensource',
    ], keywords_user=[
        'lentidao', 'bonjour', 'monitoramento',
        'notebooklm', 'opensource', 'notebooklm',
    ])

    return rules


def extract_first_user_message(text):
    """Extract the first user message from a live doc markdown."""
    m = re.search(r'## 👤 Usuário.*?\n\n(.*?)(?=\n##\s|\Z)', text, re.DOTALL)
    if m:
        raw = m.group(1).strip()
        # Remove details blocks
        raw = re.sub(r'<details>.*?</details>', '', raw, flags=re.DOTALL)
        return raw.strip()
    return ''


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


def classify_all():
    """Classify all sessions by project."""
    rules = compile_rules()
    classification = {}
    counts = {}

    for sf in sorted(SESSOES_DIR.glob('*.md')):
        if sf.name == 'classification.json':
            continue
        slug = sf.stem
        text = sf.read_text(encoding='utf-8')
        fm = parse_frontmatter(text)
        first_user = extract_first_user_message(text)

        classified = False
        for proj_slug, proj_name, matcher in rules:
            if matcher(fm, first_user):
                classification[slug] = {
                    'project_slug': proj_slug,
                    'project_name': proj_name,
                    'title': fm.get('title', ''),
                    'date': fm.get('date', ''),
                    'agent': fm.get('agent', ''),
                    'model': fm.get('model', ''),
                    'cost': float(fm.get('cost', 0)),
                }
                counts[proj_name] = counts.get(proj_name, 0) + 1
                classified = True
                break

        if not classified:
            classification[slug] = {
                'project_slug': 'unclassified',
                'project_name': '** Unclassified **',
                'title': fm.get('title', ''),
                'date': fm.get('date', ''),
                'agent': fm.get('agent', ''),
                'model': fm.get('model', ''),
                'cost': float(fm.get('cost', 0)),
            }
            counts['** Unclassified **'] = counts.get('** Unclassified **', 0) + 1

    # -- Fallback: for remaining unclassified, try to identify by first user message content ---
    for slug, info in classification.items():
        if info['project_slug'] == 'unclassified':
            sf = SESSOES_DIR / f'{slug}.md'
            if sf.exists():
                text = sf.read_text(encoding='utf-8')
                first_user = extract_first_user_message(text)
                if not first_user or info.get('cost', 0) == 0:
                    info['project_slug'] = 'empty'
                    info['project_name'] = '** Empty (no content) **'
                    continue
                msg_lower = first_user.lower()
                for proj_slug, proj_name, matcher in rules:
                    if proj_slug in ('personal', 'empty'):
                        continue
                    fm = {'title': '', 'agent': 'fallback'}
                    if matcher(fm, first_user):
                        info['project_slug'] = proj_slug
                        info['project_name'] = proj_name
                        break

    return classification


def save_classification(classification):
    """Save classification result."""
    with open(CLASSIFICATION_FILE, 'w', encoding='utf-8') as f:
        json.dump({
            'classification': classification,
            'total': len(classification),
        }, f, indent=2, ensure_ascii=False)
    print(f'Saved: {CLASSIFICATION_FILE}')


def print_summary(classification):
    """Print classification summary."""
    by_project = {}
    total_cost = 0
    total_sessions = len(classification)

    for slug, info in classification.items():
        proj = info['project_name']
        if proj not in by_project:
            by_project[proj] = {'count': 0, 'cost': 0.0, 'slugs': []}
        by_project[proj]['count'] += 1
        by_project[proj]['cost'] += info['cost']
        by_project[proj]['slugs'].append(slug)
        total_cost += info['cost']

    print(f'\n{"=" * 60}')
    print(f'  Session Classification Summary')
    print(f'  Total: {total_sessions} sessions, ${total_cost:.2f} total cost')
    print(f'{"=" * 60}')
    print(f'{"Project":40s} {"Sessions":>8s} {"Cost":>10s}')
    print(f'{"-" * 60}')

    for proj in sorted(by_project.keys(), key=lambda p: -by_project[p]['count']):
        info = by_project[proj]
        print(f'{proj:40s} {info["count"]:>8d} ${info["cost"]:>8.2f}')

    print(f'{"-" * 60}')

    # Save unclassified list for review
    unclassified = [s for s, info in classification.items() if info['project_slug'] == 'unclassified']
    if unclassified:
        print(f'\n!!  {len(unclassified)} unclassified sessions:')
        for s in sorted(unclassified):
            info = classification[s]
            print(f'  * {s:25s} | {info["title"][:60]}')
        print(f'\nTo classify them manually, edit the rules in classify-sessions.py')
    
    return by_project


def main():
    print('Classifying sessions by project...')
    classification = classify_all()
    save_classification(classification)
    print_summary(classification)


if __name__ == '__main__':
    main()
