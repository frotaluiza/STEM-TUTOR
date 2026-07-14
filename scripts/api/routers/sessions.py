from fastapi import APIRouter, Query
from pathlib import Path
import yaml

router = APIRouter()

PROJETOS_DIR = Path(__file__).resolve().parents[3] / "Projetos"


def _load_yaml(path: Path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@router.get("/sessions")
def list_sessions(projeto: str = Query(None)):
    if projeto:
        sessoes_dir = PROJETOS_DIR / projeto / "sessoes"
        if not sessoes_dir.exists():
            return {"sessions": [], "count": 0}
        sessions = []
        for f in sorted(sessoes_dir.glob("*.md"), reverse=True):
            sessions.append({
                "slug": f.stem,
                "arquivo": f.name,
                "projeto": projeto,
            })
        return {"sessions": sessions, "count": len(sessions)}

    todas = []
    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir() or not (d / "project-state.yaml").exists():
            continue
        sessoes_dir = d / "sessoes"
        if not sessoes_dir.exists():
            continue
        for f in sorted(sessoes_dir.glob("*.md"), reverse=True):
            todas.append({
                "slug": f.stem,
                "arquivo": f.name,
                "projeto": d.name,
            })
    return {"sessions": todas, "count": len(todas)}


@router.get("/sessions/{slug}")
def get_session(slug: str, projeto: str = Query(None)):
    if projeto:
        sessao_path = PROJETOS_DIR / projeto / "sessoes" / f"{slug}.md"
        if sessao_path.exists():
            return {
                "slug": slug,
                "projeto": projeto,
                "conteudo": sessao_path.read_text(encoding="utf-8"),
            }

    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir():
            continue
        sessao_path = d / "sessoes" / f"{slug}.md"
        if sessao_path.exists():
            return {
                "slug": slug,
                "projeto": d.name,
                "conteudo": sessao_path.read_text(encoding="utf-8"),
            }

    return {"error": f"Sessão '{slug}' não encontrada"}
