"""
gh-sync-notion.py
=================
Called by GitHub Action sync-notion.yml to push KB markdown
changes to Notion databases (Sessões, Projetos, Documentacao).

Uses Notion API directly via HTTP (no Composio dependency in CI).
"""

import json
import os
import re
import sys
from pathlib import Path

# --- Config from env ---
NOTION_API_KEY = os.environ.get('NOTION_API_KEY', '')
SESSOES_DB_ID = os.environ.get('SESSOES_DB_ID', '372191ce-57f9-810c-99aa-d5fa31deb926')
PROJETOS_DB_ID = os.environ.get('PROJETOS_DB_ID', '9172be34-0056-4f38-aa2a-093339bb5790')

AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
SESSOES_DIR = AI_TUTOR_DIR / 'kb' / 'sessoes'
CLASSIFICATION_FILE = SESSOES_DIR / 'classification.json'
PROJECT_STATE_DIR = AI_TUTOR_DIR / 'project-state'

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
    """Make a Notion API request."""
    import httpx
    url = f'https://api.notion.com/v1/{endpoint}'
    resp = httpx.request(method, url, headers=notion_headers(), json=data, timeout=30)
    if resp.status_code >= 400:
        print(f'  NOTION ERROR {resp.status_code}: {resp.text[:300]}')
        return None
    return resp.json()


def find_session_page(slug):
    """Find existing Notion page for a session slug."""
    resp = notion_request('POST', f'databases/{SESSOES_DB_ID}/query', {
        'filter': {
            'property': 'Chat ID',
            'rich_text': {'contains': slug}
        }
    })
    if resp and resp.get('results'):
        return resp['results'][0]['id']
    return None


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


def session_to_notion_properties(fm, slug, preview):
    """Convert session frontmatter to Notion page properties."""
    return {
        'Sessão': {'title': [{'text': {'content': fm.get('title', slug)[:100]}}]},
        'Chat ID': {'rich_text': [{'text': {'content': slug}}]},
        'Data': {'date': {'start': fm.get('date', '')[:10]}},
        'Status': {'status': {'name': 'Concluído'}},
        'Resumo (curto)': {'rich_text': [{'text': {'content': preview[:150]}}]},
        'Título Resumido': {'rich_text': [{'text': {'content': fm.get('title', slug)[:60]}}]},
    }


def upsert_session(slug):
    """Create or update a Notion page for a session."""
    sf = SESSOES_DIR / f'{slug}.md'
    if not sf.exists():
        print(f'  {slug}: live doc not found')
        return

    text = sf.read_text(encoding='utf-8')
    fm = parse_frontmatter(text)

    # Extract preview from first user message
    preview = ''
    m = re.search(r'^## 👤 Usuário.*?\n\n(.*?)(?=\n##\s|\Z)', text, re.DOTALL)
    if m:
        preview = re.sub(r'<details>.*?</details>', '', m.group(1), flags=re.DOTALL).strip()[:300]

    props = session_to_notion_properties(fm, slug, preview)

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
    """Sync all sessions that have live docs."""
    count = 0
    for sf in sorted(SESSOES_DIR.glob('*.md')):
        if sf.name == 'classification.json':
            continue
        slug = sf.stem
        upsert_session(slug)
        count += 1
    print(f'\nSynced {count} sessions')


def sync_slugs(slugs):
    """Sync specific slugs."""
    for s in slugs:
        upsert_session(s.strip())
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

    if not NOTION_API_KEY:
        print('ERROR: NOTION_API_KEY not set')
        sys.exit(1)

    print('=== Sync KB → Notion ===')
    print()

    if args.slugs:
        slugs = [s.strip() for s in args.slugs.split(',') if s.strip()]
        sync_slugs(slugs)
    else:
        sync_all()


if __name__ == '__main__':
    main()
