from fastapi import APIRouter, Query
from pathlib import Path
import re
import yaml

router = APIRouter()

PROJETOS_DIR = Path(__file__).resolve().parents[3] / "Projetos"


def _parse_frontmatter(text: str):
    """Parse YAML frontmatter from a markdown file."""
    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if m:
        for line in m.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def _load_yaml(path: Path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _list_session_files(projeto_dir: Path, origem: str = None):
    """List session files, optionally filtered by origem frontmatter."""
    sessoes_dir = projeto_dir / "sessoes"
    if not sessoes_dir.exists():
        return []
    sessions = []
    for f in sorted(sessoes_dir.glob("*.md"), reverse=True):
        text = f.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        file_origem = fm.get("origem", "opencode")
        if origem and file_origem != origem:
            continue
        sessions.append({
            "slug": f.stem,
            "arquivo": f.name,
            "projeto": projeto_dir.name,
            "origem": file_origem,
        })
    return sessions


@router.get("/sessions")
def list_sessions(
    projeto: str = Query(None),
    origem: str = Query(None, description="Filtrar por origem: opencode, noteblocks, github_action, notion_pull"),
):
    if projeto:
        sessions = _list_session_files(PROJETOS_DIR / projeto, origem)
        return {"sessions": sessions, "count": len(sessions)}

    todas = []
    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir() or not (d / "project-state.yaml").exists():
            continue
        todas.extend(_list_session_files(d, origem))
    return {"sessions": todas, "count": len(todas)}


@router.get("/sessions/{slug}")
def get_session(slug: str, projeto: str = Query(None)):
    if projeto:
        sessao_path = PROJETOS_DIR / projeto / "sessoes" / f"{slug}.md"
        if sessao_path.exists():
            content = sessao_path.read_text(encoding="utf-8")
            fm = _parse_frontmatter(content)
            return {
                "slug": slug,
                "projeto": projeto,
                "origem": fm.get("origem", "opencode"),
                "conteudo": content,
            }

    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir():
            continue
        sessao_path = d / "sessoes" / f"{slug}.md"
        if sessao_path.exists():
            content = sessao_path.read_text(encoding="utf-8")
            fm = _parse_frontmatter(content)
            return {
                "slug": slug,
                "projeto": d.name,
                "origem": fm.get("origem", "opencode"),
                "conteudo": content,
            }

    return {"error": f"Sessão '{slug}' não encontrada"}
