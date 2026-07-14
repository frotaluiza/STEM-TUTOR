"""
notion-pull.py
==============
Pull entries from Notion databases (Sessoes, Projetos, Fontes, etc.)
into local Projetos/ structure.

Called by:
  - GitHub Action (schedule 15min or workflow_dispatch)
  - Local watcher (manual trigger)

Flow:
  1. Read last pull timestamp from .last_pull_timestamp
  2. Query Notion DBs for entries modified since then
  3. For each new/updated entry:
     a. Determine project slug (via Projeto 1 relation)
     b. Save as .md in Projetos/{slug}/{database}/
     c. If local file is newer → save to conflitos/ instead
  4. Update .last_pull_timestamp
  5. Commit (if called from GitHub Action)
"""

import json
import os
import re
import sys
import time
import yaml
from datetime import datetime, timezone
from pathlib import Path

# --- Config from env ---
NOTION_API_KEY = os.environ.get('NOTION_API_KEY', os.environ.get('OPENCODE_WATCHER', ''))
SESSOES_DB_ID = os.environ.get('SESSOES_DB_ID', '372191ce-57f9-810c-99aa-d5fa31deb926')
PROJETOS_DB_ID = os.environ.get('PROJETOS_DB_ID', '9172be34-0056-4f38-aa2a-093339bb5790')

NOTION_VERSION = '2022-06-28'

AI_TUTOR_DIR = Path(__file__).resolve().parents[2]
PROJETOS_DIR = AI_TUTOR_DIR / 'Projetos'
CONFLITOS_DIR = PROJETOS_DIR / 'conflitos'
TIMESTAMP_FILE = AI_TUTOR_DIR / 'scripts' / 'kb' / '.last_pull_timestamp'

# Map Notion database IDs → local subdirectory names
DB_DIR_MAP = {
    SESSOES_DB_ID: 'sessoes',
    # Future: map other databases as they're integrated
}

# Reverse map: project names (from Notion) → project slugs (from perfil)
_PROJECT_SLUG_MAP = None


def _load_project_slug_map():
    global _PROJECT_SLUG_MAP
    if _PROJECT_SLUG_MAP:
        return _PROJECT_SLUG_MAP

    perfil_path = PROJETOS_DIR / 'perfis' / 'frota.yaml'
    slug_map = {}
    if perfil_path.exists():
        with open(perfil_path, encoding='utf-8') as f:
            perfil = yaml.safe_load(f)
        for p in perfil.get('projetos', []):
            slug = p.get('slug', '')
            nome = p.get('nome', slug)
            slug_map[nome] = slug
            slug_map[slug] = slug  # also key by slug itself

    _PROJECT_SLUG_MAP = slug_map
    return slug_map


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
        print(f'  NOTION ERROR {resp.status_code}: {resp.text[:200]}')
        return None
    return resp.json()


# ---------------------------------------------------------------------------
# Timestamp tracking
# ---------------------------------------------------------------------------

def read_last_pull():
    if TIMESTAMP_FILE.exists():
        raw = TIMESTAMP_FILE.read_text(encoding='utf-8').strip()
        if raw:
            return raw
    # Default: pull last 7 days
    return datetime.now(timezone.utc).isoformat()


def write_last_pull(ts=None):
    if ts is None:
        ts = datetime.now(timezone.utc).isoformat()
    TIMESTAMP_FILE.write_text(ts, encoding='utf-8')


# ---------------------------------------------------------------------------
# Resolve project slug from Notion relation
# ---------------------------------------------------------------------------

def _fetch_project_page_name(page_id):
    """Get the project name from a Projetos DB page ID."""
    resp = notion_request('GET', f'pages/{page_id}')
    if not resp:
        return None
    props = resp.get('properties', {})
    title_objs = props.get('Projeto', {}).get('title', [])
    return ''.join(t.get('plain_text', '') for t in title_objs if isinstance(t, dict))


def resolve_project_slug(notion_page):
    """Determine which project slug a Notion session belongs to."""
    props = notion_page.get('properties', {})

    # Try Projeto 1 relation
    rel = props.get('Projeto 1', {}).get('relation', [])
    if rel:
        proj_page_id = rel[0].get('id', '')
        proj_name = _fetch_project_page_name(proj_page_id)
        if proj_name:
            slug_map = _load_project_slug_map()
            slug = slug_map.get(proj_name)
            if slug:
                return slug

    # Try Projeto (antigo) multi_select
    ms = props.get('Projeto (antigo)', {}).get('multi_select', [])
    for item in ms:
        name = item.get('name', '')
        slug_map = _load_project_slug_map()
        slug = slug_map.get(name)
        if slug:
            return slug

    # Try matching by session title keywords
    title_objs = props.get('Sessão', {}).get('title', [])
    title = ''.join(t.get('plain_text', '') for t in title_objs if isinstance(t, dict)).lower()
    for slug, info in _load_project_slug_map().items():
        if slug in title:
            return slug if slug != info else slug

    return None


# ---------------------------------------------------------------------------
# Pull sessions
# ---------------------------------------------------------------------------

def pull_sessions(since_ts):
    """Pull new/updated sessions from Notion Sessoes DB."""
    print(f'Pulling sessions modified since {since_ts}...')

    query = {
        'page_size': 100,
        'sorts': [{'timestamp': 'last_edited_time', 'direction': 'descending'}],
        'filter': {
            'timestamp': 'last_edited_time',
            'last_edited_time': {'on_or_after': since_ts[:10]},
        },
    }

    resp = notion_request('POST', f'databases/{SESSOES_DB_ID}/query', query)
    if not resp:
        print('  No response from Notion')
        return 0

    results = resp.get('results', [])
    if not results:
        print('  No new sessions found')
        return 0

    count = 0
    for page in results:
        props = page.get('properties', {})
        title_objs = props.get('Sessão', {}).get('title', [])
        title = ''.join(t.get('plain_text', '') for t in title_objs if isinstance(t, dict))

        chat_id_objs = props.get('Chat ID', {}).get('rich_text', [])
        slug = ''.join(t.get('plain_text', '') for t in chat_id_objs if isinstance(t, dict))
        if not slug:
            slug = title.lower().replace(' ', '-')[:30]

        projeto_slug = resolve_project_slug(page)
        if not projeto_slug:
            print(f'  {slug}: could not determine project, saving to _unassigned')
            projeto_slug = '_unassigned'

        # Determine target directory
        target_dir = PROJETOS_DIR / projeto_slug / 'sessoes'
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / f'{slug}.md'

        # Build content
        last_edited = page.get('last_edited_time', '')
        created = page.get('created_time', '')
        page_id = page.get('id', '')

        frontmatter = {
            'title': title,
            'slug': slug,
            'notion_page_id': page_id,
            'created': created,
            'last_edited': last_edited,
            'origem': 'notion_pull',
        }

        fm_lines = ['---']
        for k, v in frontmatter.items():
            fm_lines.append(f'{k}: "{v}"')
        fm_lines.append('---')

        content = '\n'.join(fm_lines)
        content += f'\n\n# {title}\n\n'
        content += f'_Pulled from Notion at {datetime.now(timezone.utc).isoformat()}_\n\n'
        content += f'- **Criado em**: {created}\n'
        content += f'- **Última edição**: {last_edited}\n'
        content += f'- **Origem**: Notion\n'

        # Conflict detection
        if target_file.exists():
            local_content = target_file.read_text(encoding='utf-8')
            local_mtime = target_file.stat().st_mtime
            local_dt = datetime.fromtimestamp(local_mtime, tz=timezone.utc)

            notion_dt = datetime.fromisoformat(last_edited.replace('Z', '+00:00')) if last_edited else local_dt

            if local_dt > notion_dt:
                # Local is newer → conflict
                CONFLITOS_DIR.mkdir(parents=True, exist_ok=True)
                conflito_file = CONFLITOS_DIR / f'{slug}.conflito.md'
                conflito_content = (
                    f'# Conflito: {slug}\n\n'
                    f'**Arquivo local**: {target_file}\n'
                    f'**Última modificação local**: {local_dt.isoformat()}\n'
                    f'**Última modificação Notion**: {notion_dt.isoformat()}\n\n'
                    f'---\n'
                    f'## Versão Local\n\n{local_content}\n\n'
                    f'---\n'
                    f'## Versão Notion\n\n{content}\n\n'
                    f'---\n'
                    f'*Resolva manualmente e remova este arquivo.*\n'
                )
                conflito_file.write_text(conflito_content, encoding='utf-8')
                print(f'  {slug}: CONFLITO → {conflito_file}')
                continue

        target_file.write_text(content, encoding='utf-8')
        print(f'  {slug}: saved → {target_file}')
        count += 1

    return count


# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Pull Notion entries to local Projetos/')
    parser.add_argument('--since', type=str, default='', help='ISO timestamp to pull since')
    parser.add_argument('--api-key', type=str, default='', help='Notion API key')
    parser.add_argument('--commit', action='store_true', help='Auto-commit changes (for GH Action)')
    args = parser.parse_args()

    if args.api_key:
        global NOTION_API_KEY
        NOTION_API_KEY = args.api_key

    if not NOTION_API_KEY:
        NOTION_API_KEY = os.environ.get('OPENCODE_WATCHER', '')

    if not NOTION_API_KEY:
        print('ERROR: NOTION_API_KEY not set')
        sys.exit(1)

    since = args.since or read_last_pull()
    print('=== Notion → Local Pull ===')
    print(f'Sessions DB: {SESSOES_DB_ID}')
    print(f'Since: {since}')
    print()

    total = pull_sessions(since)

    write_last_pull()
    print(f'\nPulled {total} entries')

    if args.commit and total > 0:
        import subprocess
        repo_dir = AI_TUTOR_DIR
        subprocess.run(['git', '-C', repo_dir, 'add', '-A'], capture_output=True)
        result = subprocess.run(
            ['git', '-C', repo_dir, 'commit', '-m', f'auto: pull {total} entradas do Notion'],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print(f'Committed: {result.stdout.strip()}')
        else:
            print(f'Commit: {result.stderr.strip()}')


if __name__ == '__main__':
    main()
