"""
reconcile.py
============
Sync initial / backfill entre Notion e repositorio local.

Varre:
  1. Todas as sessoes no Notion (DB Sessoes) → cria .md local se nao existir
  2. Todas as sessoes locais (Projetos/*/sessoes/) → sobe para Notion se nao existir
  3. Corrige project-state.yaml (decisoes, proximos passos) a partir das sessoes
  4. Gera relatorio de inconsistencias

Uso:
  python scripts/kb/reconcile.py [--dry-run]
"""

import json
import os
import sys
import yaml
from datetime import datetime, timezone
from pathlib import Path

NOTION_API_KEY = os.environ.get('NOTION_API_KEY', os.environ.get('OPENCODE_WATCHER', ''))
SESSOES_DB_ID = os.environ.get('SESSOES_DB_ID', '372191ce-57f9-810c-99aa-d5fa31deb926')
PROJETOS_DB_ID = os.environ.get('PROJETOS_DB_ID', '9172be34-0056-4f38-aa2a-093339bb5790')
NOTION_VERSION = '2022-06-28'

AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
PROJETOS_DIR = AI_TUTOR_DIR / 'Projetos'


def notion_headers():
    return {
        'Authorization': f'Bearer {NOTION_API_KEY}',
        'Content-Type': 'application/json',
        'Notion-Version': NOTION_VERSION,
    }


def notion_request(method, endpoint, data=None):
    import httpx
    url = f'https://api.notion.com/v1/{endpoint}'
    resp = httpx.request(method, url, headers=notion_headers(), json=data, timeout=30)
    if resp.status_code >= 400:
        print(f'  NOTION ERROR {resp.status_code}: {resp.text[:200]}')
        return None
    return resp.json()


def get_all_sessions_from_notion():
    """Get all session pages from Notion, paginated."""
    all_pages = []
    cursor = None
    while True:
        query = {'page_size': 100}
        if cursor:
            query['start_cursor'] = cursor
        resp = notion_request('POST', f'databases/{SESSOES_DB_ID}/query', query)
        if not resp:
            break
        results = resp.get('results', [])
        all_pages.extend(results)
        if not resp.get('has_more'):
            break
        cursor = resp.get('next_cursor')
    return all_pages


def extract_text(rich_text):
    return ''.join(t.get('plain_text', '') for t in rich_text if isinstance(t, dict))


def resolve_project_slug(page):
    """Try to find which project slug a session belongs to."""
    props = page.get('properties', {})
    title_objs = props.get('Sessão', {}).get('title', [])
    title = extract_text(title_objs)

    # Try Projeto 1 relation
    rel = props.get('Projeto 1', {}).get('relation', [])
    if rel:
        proj_id = rel[0].get('id', '')
        resp = notion_request('GET', f'pages/{proj_id}')
        if resp:
            pprops = resp.get('properties', {})
            proj_title = extract_text(pprops.get('Projeto', {}).get('title', []))
            # Map project title to slug
            for d in PROJETOS_DIR.iterdir():
                if not d.is_dir():
                    continue
                ps_path = d / 'project-state.yaml'
                if ps_path.exists():
                    with open(ps_path, encoding='utf-8') as f:
                        ps = yaml.safe_load(f)
                    if ps and ps.get('projeto') == proj_title:
                        return d.name

    # Fallback: search by session title keywords in project slugs
    title_lower = title.lower()
    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir():
            continue
        ps_path = d / 'project-state.yaml'
        if ps_path.exists():
            with open(ps_path, encoding='utf-8') as f:
                ps = yaml.safe_load(f)
            if ps:
                slug = ps.get('slug', '')
                if slug and slug in title_lower:
                    return slug

    return '_unassigned'


def _push_session_to_notion(local_path, slug, projeto_slug):
    """Push a local session .md to Notion."""
    text = local_path.read_text(encoding='utf-8')

    # Parse frontmatter
    fm = {}
    import re
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if m:
        for line in m.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")

    # Extract preview from first user message
    preview = ''
    m2 = re.search(r'^## 👤 Usuário.*?\n\n(.*?)(?=\n##\s|\Z)', text, re.DOTALL)
    if m2:
        preview = m2.group(1).strip()[:300]

    title = fm.get('title', slug)[:100]
    data = fm.get('date', '')[:10]

    props = {
        'Sessão': {'title': [{'text': {'content': title}}]},
        'Chat ID': {'rich_text': [{'text': {'content': slug}}]},
        'Data': {'date': {'start': data}},
        'Status': {'status': {'name': 'Concluído'}},
        'Resumo (curto)': {'rich_text': [{'text': {'content': preview[:150]}}]},
        'Título Resumido': {'rich_text': [{'text': {'content': title[:60]}}]},
        'Origem': {'select': {'name': 'github_action'}},
    }

    # Link to project
    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir() or d.name != projeto_slug:
            continue
        ps_path = d / 'project-state.yaml'
        if ps_path.exists():
            with open(ps_path, encoding='utf-8') as f:
                ps = yaml.safe_load(f)
            if ps:
                proj_name = ps.get('projeto', '')
                # Query Notion for the project page ID
                resp = notion_request('POST', f'databases/{PROJETOS_DB_ID}/query', {
                    'filter': {'property': 'Projeto', 'title': {'equals': proj_name}},
                })
                if resp and resp.get('results'):
                    proj_page_id = resp['results'][0]['id']
                    props['Projeto 1'] = {'relation': [{'id': proj_page_id}]}
        break

    # Find existing or create
    existing = notion_request('POST', f'databases/{SESSOES_DB_ID}/query', {
        'filter': {'property': 'Chat ID', 'rich_text': {'contains': slug}},
    })
    if existing and existing.get('results'):
        page_id = existing['results'][0]['id']
        notion_request('PATCH', f'pages/{page_id}', {'properties': props})
    else:
        notion_request('POST', 'pages', {
            'parent': {'database_id': SESSOES_DB_ID},
            'properties': props,
        })


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Reconcile Notion ↔ local')
    parser.add_argument('--dry-run', action='store_true', help='Only report, no changes')
    args = parser.parse_args()

    if not NOTION_API_KEY:
        print('ERROR: NOTION_API_KEY not set')
        sys.exit(1)

    print('=== Reconcile Notion ↔ Local ===')
    if args.dry_run:
        print('DRY RUN — no changes will be made')
    print()

    # ── Step 1: Pull from Notion ──
    print('── Step 1: Notion → Local ──')
    notion_sessions = get_all_sessions_from_notion()
    print(f'  Found {len(notion_sessions)} sessions in Notion')

    local_by_slug = {}
    for proj_dir in PROJETOS_DIR.iterdir():
        if not proj_dir.is_dir():
            continue
        sessoes_dir = proj_dir / 'sessoes'
        if not sessoes_dir.exists():
            continue
        for sf in sessoes_dir.glob('*.md'):
            local_by_slug[sf.stem] = sf

    pulled = 0
    for page in notion_sessions:
        props = page.get('properties', {})
        chat_id = extract_text(props.get('Chat ID', {}).get('rich_text', []))
        slug = chat_id if chat_id else page.get('id', '')[:20]
        title = extract_text(props.get('Sessão', {}).get('title', []))

        if not slug or slug in local_by_slug:
            continue

        projeto_slug = resolve_project_slug(page)
        target_dir = PROJETOS_DIR / projeto_slug / 'sessoes'

        content = f"""---
title: "{title}"
slug: "{slug}"
notion_page_id: "{page.get('id', '')}"
created: "{page.get('created_time', '')}"
last_edited: "{page.get('last_edited_time', '')}"
origem: "notion_pull"
---

# {title}

_Pulled from Notion via reconcile at {datetime.now(timezone.utc).isoformat()}_
"""
        if not args.dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            (target_dir / f'{slug}.md').write_text(content, encoding='utf-8')
            print(f'  Created: {target_dir / slug}.md')
        else:
            print(f'  Would create: {target_dir / slug}.md')
        pulled += 1

    print(f'  Pulled {pulled} new sessions from Notion')

    # ── Step 2: Push to Notion ──
    print()
    print('── Step 2: Local → Notion ──')
    pushed = 0
    notion_slugs = set()
    for page in notion_sessions:
        chat_id = extract_text(page.get('properties', {}).get('Chat ID', {}).get('rich_text', []))
        if chat_id:
            notion_slugs.add(chat_id)

    for slug, local_path in local_by_slug.items():
        if slug in notion_slugs:
            continue

        # Determine project from path
        projeto_slug = local_path.parent.parent.name
        text = local_path.read_text(encoding='utf-8')

        # Simple frontmatter parse
        title = slug
        for line in text.split('\n'):
            if line.startswith('title:'):
                title = line.split(':', 1)[1].strip().strip('"').strip("'")
                break

        if not args.dry_run:
            _push_session_to_notion(local_path, slug, projeto_slug)
            print(f'  Pushed: {slug}')
        else:
            print(f'  Would push: {slug} (projeto: {projeto_slug})')
        pushed += 1

    print(f'  Pushed {pushed} local sessions to Notion')

    # ── Step 3: Summary ──
    print()
    print('── Summary ──')
    print(f'  Notion sessions: {len(notion_sessions)}')
    print(f'  Local sessions:  {len(local_by_slug)}')
    print(f'  Pulled:          {pulled}')
    print(f'  Pushed:          {pushed}')
    print(f'  In sync:         {len(notion_sessions) + len(local_by_slug) - pulled - pushed}')
    print()


if __name__ == '__main__':
    main()
