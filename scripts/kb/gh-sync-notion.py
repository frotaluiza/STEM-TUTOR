"""
gh-sync-notion.py
=================
Called by GitHub Action sync-notion.yml to push KB markdown
changes to Notion databases (Sessões, Projetos, Documentacao).

Now supports:
  - Leitura de Projetos/{slug}/sessoes/ (nova estrutura)
  - Vinculo com Projeto 1 (relation)
  - Campo Origem (github_action | opencode_watcher)
  - Leitura de perfis/frota.yaml para mapear slugs → pages
"""

import os
from pathlib import Path
import re
import sys

import yaml

# --- Config from env ---
NOTION_API_KEY = os.environ.get('NOTION_API_KEY', os.environ.get('OPENCODE_WATCHER', ''))
SESSOES_DB_ID = os.environ.get('SESSOES_DB_ID', '372191ce-57f9-810c-99aa-d5fa31deb926')
PROJETOS_DB_ID = os.environ.get('PROJETOS_DB_ID', '9172be34-0056-4f38-aa2a-093339bb5790')

AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
PROJETOS_DIR = AI_TUTOR_DIR / 'Projetos'
PERFIS_DIR = PROJETOS_DIR / 'perfis'
OLD_SESSOES_DIR = AI_TUTOR_DIR / 'kb' / 'sessoes'  # fallback legacy

NOTION_VERSION = '2022-06-28'


# ---------------------------------------------------------------------------
# Notion API helpers
# ---------------------------------------------------------------------------

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
        print(f'  NOTION ERROR {resp.status_code}: {resp.text[:300]}')
        return None
    return resp.json()


def find_session_page(slug):
    resp = notion_request('POST', f'databases/{SESSOES_DB_ID}/query', {
        'filter': {
            'property': 'Chat ID',
            'rich_text': {'contains': slug}
        }
    })
    if resp and resp.get('results'):
        return resp['results'][0]['id']
    return None


# ---------------------------------------------------------------------------
# Project mapping from perfis/frota.yaml + fallback Notion query
# ---------------------------------------------------------------------------

_PROJECT_CACHE = None

def _load_project_map():
    """Build {slug: {nome, page_id}} from perfis/frota.yaml + Notion query."""
    global _PROJECT_CACHE
    if _PROJECT_CACHE:
        return _PROJECT_CACHE

    project_map = {}

    # 1. Read perfil
    perfil_path = PERFIS_DIR / 'frota.yaml'
    if perfil_path.exists():
        with open(perfil_path, encoding='utf-8') as f:
            perfil = yaml.safe_load(f)
        for p in perfil.get('projetos', []):
            slug = p.get('slug', '')
            nome = p.get('nome', slug)
            if slug:
                project_map[slug] = {'nome': nome, 'id': None}

    # 2. Query Notion Projetos DB for page IDs
    resp = notion_request('POST', f'databases/{PROJETOS_DB_ID}/query', {'page_size': 100})
    if resp:
        for row in resp.get('results', []):
            props = row.get('properties', {})
            title_objs = props.get('Projeto', {}).get('title', [])
            title = ''.join(t.get('plain_text', '') for t in title_objs if isinstance(t, dict))
            page_id = row.get('id', '')
            # Match by nome
            for slug, info in project_map.items():
                if info['nome'] == title:
                    info['id'] = page_id
                    break

    _PROJECT_CACHE = project_map
    return project_map


def get_project_page_id(slug):
    pmap = _load_project_map()
    info = pmap.get(slug)
    if info and info.get('id'):
        return info['id']
    return None


# ---------------------------------------------------------------------------
# Session scraping
# ---------------------------------------------------------------------------

def find_session_files():
    """Find session .md files in Projetos/{slug}/sessoes/ and legacy kb/sessoes/."""
    sessions = []

    # New structure: Projetos/{slug}/sessoes/
    if PROJETOS_DIR.exists():
        for proj_dir in sorted(PROJETOS_DIR.iterdir()):
            if not proj_dir.is_dir():
                continue
            sessoes_dir = proj_dir / 'sessoes'
            if not sessoes_dir.exists():
                continue
            projeto_slug = proj_dir.name
            for sf in sorted(sessoes_dir.glob('*.md')):
                sessions.append({
                    'path': sf,
                    'slug': sf.stem,
                    'projeto_slug': projeto_slug,
                })

    # Legacy fallback: kb/sessoes/
    if OLD_SESSOES_DIR.exists():
        for sf in sorted(OLD_SESSOES_DIR.glob('*.md')):
            if sf.name == 'classification.json':
                continue
            slug = sf.stem
            # Avoid duplicates
            if not any(s['slug'] == slug for s in sessions):
                sessions.append({
                    'path': sf,
                    'slug': slug,
                    'projeto_slug': None,
                })

    return sessions


def parse_frontmatter(text):
    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if m:
        for line in m.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def extract_preview(text):
    preview = ''
    m = re.search(r'^## 👤 Usuário.*?\n\n(.*?)(?=\n##\s|\Z)', text, re.DOTALL)
    if m:
        preview = re.sub(r'<details>.*?</details>', '', m.group(1), flags=re.DOTALL).strip()[:300]
    return preview


def session_to_notion_properties(fm, slug, preview, projeto_slug=None):
    # Read origem from frontmatter, default to github_action for GH sync
    origem = fm.get('origem', 'github_action')

    props = {
        'Sessão': {'title': [{'text': {'content': fm.get('title', slug)[:100]}}]},
        'Chat ID': {'rich_text': [{'text': {'content': slug}}]},
        'Data': {'date': {'start': fm.get('date', '')[:10]}},
        'Status': {'status': {'name': 'Concluído'}},
        'Resumo (curto)': {'rich_text': [{'text': {'content': preview[:150]}}]},
        'Título Resumido': {'rich_text': [{'text': {'content': fm.get('title', slug)[:60]}}]},
        'Origem': {'select': {'name': origem}},
    }

    # Link to project
    if projeto_slug:
        page_id = get_project_page_id(projeto_slug)
        if page_id:
            props['Projeto 1'] = {'relation': [{'id': page_id}]}

    return props


def upsert_session(sf_info):
    sf = sf_info['path']
    slug = sf_info['slug']
    projeto_slug = sf_info.get('projeto_slug')

    if not sf.exists():
        print(f'  {slug}: file not found')
        return

    text = sf.read_text(encoding='utf-8')
    fm = parse_frontmatter(text)
    preview = extract_preview(text)
    props = session_to_notion_properties(fm, slug, preview, projeto_slug)

    existing_id = find_session_page(slug)
    if existing_id:
        resp = notion_request('PATCH', f'pages/{existing_id}', {'properties': props})
        if resp:
            print(f'  {slug}: updated → {resp.get("url", "")}')
    else:
        resp = notion_request('POST', 'pages', {
            'parent': {'database_id': SESSOES_DB_ID},
            'properties': props,
        })
        if resp:
            print(f'  {slug}: created → {resp.get("url", "")}')


def sync_all():
    sessions = find_session_files()
    count = 0
    for s in sessions:
        upsert_session(s)
        count += 1
    print(f'\nSynced {count} sessions')


def sync_slugs(slugs):
    for s in slugs:
        sf_info = {'path': OLD_SESSOES_DIR / f'{s.strip()}.md', 'slug': s.strip(), 'projeto_slug': None}
        # Try new structure first
        sessions = find_session_files()
        for sess in sessions:
            if sess['slug'] == s.strip():
                sf_info = sess
                break
        upsert_session(sf_info)
    print(f'\nSynced {len(slugs)} sessions')


# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Sync KB markdown to Notion')
    parser.add_argument('--slugs', type=str, default='', help='Comma-separated slugs')
    parser.add_argument('--mode', type=str, default='batch', help='batch or single')
    parser.add_argument('--api-key', type=str, default='', help='Notion API key')
    args = parser.parse_args()

    if args.api_key:
        global NOTION_API_KEY
        NOTION_API_KEY = args.api_key

    # Also try env var OPENCODE_WATCHER (GitHub secret name)
    if not NOTION_API_KEY:
        NOTION_API_KEY = os.environ.get('OPENCODE_WATCHER', '')

    if not NOTION_API_KEY:
        print('ERROR: NOTION_API_KEY not set')
        sys.exit(1)

    print('=== Sync KB → Notion ===')
    print()

    # Preload project map
    pmap = _load_project_map()
    print(f'Loaded {len(pmap)} projects from perfil + Notion')

    if args.slugs:
        slugs = [s.strip() for s in args.slugs.split(',') if s.strip()]
        sync_slugs(slugs)
    else:
        sync_all()


if __name__ == '__main__':
    main()
