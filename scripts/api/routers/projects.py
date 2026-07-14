from pathlib import Path

from fastapi import APIRouter, HTTPException
import yaml

router = APIRouter()

PROJETOS_DIR = Path(__file__).resolve().parents[3] / "Projetos"


def _session_counts() -> dict[str, int]:
    """Return {slug: count} from Projetos/{slug}/sessoes/ directories."""
    counts: dict[str, int] = {}
    if not PROJETOS_DIR.exists():
        return counts
    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir() or not (d / "project-state.yaml").exists():
            continue
        sessoes_dir = d / "sessoes"
        if sessoes_dir.exists():
            counts[d.name] = len(list(sessoes_dir.glob("*.md")))
    return counts


def _list_project_dirs():
    if not PROJETOS_DIR.exists():
        return []
    return sorted(
        d.name for d in PROJETOS_DIR.iterdir()
        if d.is_dir() and (d / "project-state.yaml").exists()
    )


def _load_yaml(path: Path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _list_markdown_files(dir_path: Path, subdir: str):
    target = dir_path / subdir
    if not target.exists():
        return []
    files = []
    for f in sorted(target.iterdir()):
        if f.suffix in (".md", ".yaml", ".yml"):
            content = f.read_text(encoding="utf-8") if f.suffix == ".md" else None
            files.append({
                "nome": f.stem,
                "arquivo": f.name,
                "caminho": str(f.relative_to(PROJETOS_DIR)),
                "conteudo": content,
            })
    return files


@router.get("/projects")
def list_projects():
    projetos = _list_project_dirs()
    session_counts = _session_counts()
    result = []
    for slug in projetos:
        state = _load_yaml(PROJETOS_DIR / slug / "project-state.yaml")
        result.append({
            "slug": slug,
            "nome": state.get("projeto", slug) if state else slug,
            "area": state.get("area") if state else None,
            "status": state.get("status") if state else None,
            "repositorio_codigo": state.get("repositorio_codigo") if state else None,
            "objetivo": state.get("objetivo") if state else None,
            "session_count": session_counts.get(slug, 0),
        })
    return {"projects": result, "count": len(result)}


@router.get("/projects/{slug}")
def get_project(slug: str):
    project_dir = PROJETOS_DIR / slug
    if not project_dir.exists() or not (project_dir / "project-state.yaml").exists():
        raise HTTPException(status_code=404, detail=f"Projeto '{slug}' não encontrado")

    state = _load_yaml(project_dir / "project-state.yaml")
    if not state:
        raise HTTPException(status_code=500, detail=f"Erro ao ler project-state de '{slug}'")

    # Fontes (diretórios dentro do projeto)
    fontes = {}
    for sub in ["fontes", "arquitetura", "tarefas", "rotinas", "frameworks", "ferramentas", "docs", "sessoes", "conversas"]:
        fontes[sub] = _list_markdown_files(project_dir, sub)

    # Relatórios
    relatorios = {}
    rel_dir = project_dir / "relatorios"
    if rel_dir.exists():
        for sub in rel_dir.iterdir():
            if sub.is_dir():
                relatorios[sub.name] = _list_markdown_files(project_dir, f"relatorios/{sub.name}")

    return {
        "slug": slug,
        "project_state": state,
        "repositorio_codigo": state.get("repositorio_codigo"),
        "fontes": fontes,
        "relatorios": relatorios,
    }


@router.get("/projects/{slug}/state")
def get_project_state(slug: str):
    project_dir = PROJETOS_DIR / slug
    if not project_dir.exists():
        raise HTTPException(status_code=404, detail=f"Projeto '{slug}' não encontrado")
    state = _load_yaml(project_dir / "project-state.yaml")
    if not state:
        raise HTTPException(status_code=404, detail="project-state.yaml não encontrado")
    return state


@router.get("/projects/{slug}/mastery-paths")
def get_mastery_paths(slug: str):
    project_dir = PROJETOS_DIR / slug
    if not project_dir.exists():
        raise HTTPException(status_code=404, detail=f"Projeto '{slug}' não encontrado")
    state = _load_yaml(project_dir / "project-state.yaml")
    paths = state.get("mastery_paths", []) if state else []
    return {"mastery_paths": paths, "count": len(paths)}


@router.get("/projects/{slug}/{database}")
def get_project_database(slug: str, database: str):
    project_dir = PROJETOS_DIR / slug
    if not project_dir.exists():
        raise HTTPException(status_code=404, detail=f"Projeto '{slug}' não encontrado")

    allowed = {"fontes", "arquitetura", "tarefas", "rotinas", "frameworks", "ferramentas", "docs", "sessoes", "conversas"}
    if database not in allowed:
        raise HTTPException(status_code=400, detail=f"Database inválida. Use: {', '.join(sorted(allowed))}")

    return {database: _list_markdown_files(project_dir, database)}


@router.get("/profile")
def get_profile():
    profile_path = PROJETOS_DIR / "perfis" / "frota.yaml"
    profile = _load_yaml(profile_path)
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil Frota não encontrado")
    return profile
