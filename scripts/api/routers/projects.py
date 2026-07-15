import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.api.utils import resolve_projetos_dir, current_branch, PROJETOS_DIR, REPO_DIR
from fastapi import APIRouter, HTTPException, Query
import yaml

router = APIRouter()


def _list_project_dirs(projetos_dir: Path):
    if not projetos_dir.exists():
        return []
    return sorted(
        d.name for d in projetos_dir.iterdir()
        if d.is_dir() and (d / "project-state.yaml").exists()
    )


def _load_yaml(path: Path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _list_markdown_files(projetos_dir: Path, project_slug: str, subdir: str):
    target = projetos_dir / project_slug / subdir
    if not target.exists():
        return []
    files = []
    for f in sorted(target.iterdir()):
        if f.suffix in (".md", ".yaml", ".yml"):
            content = f.read_text(encoding="utf-8") if f.suffix == ".md" else None
            rel_path = f.relative_to(projetos_dir.parent) if f.is_relative_to(projetos_dir.parent) else f
            files.append({
                "nome": f.stem,
                "arquivo": f.name,
                "caminho": str(rel_path),
                "conteudo": content,
            })
    return files


@router.get("/projects")
def list_projects(branch: str = Query(None, description="Branch do worktree (ex: main)")):
    projetos_dir, real_branch = resolve_projetos_dir(branch)
    projetos = _list_project_dirs(projetos_dir)
    result = []
    for slug in projetos:
        state = _load_yaml(projetos_dir / slug / "project-state.yaml")
        sessoes_dir = projetos_dir / slug / "sessoes"
        session_count = len(list(sessoes_dir.glob("*.md"))) if sessoes_dir.exists() else 0
        result.append({
            "slug": slug,
            "nome": state.get("projeto", slug) if state else slug,
            "area": state.get("area") if state else None,
            "status": state.get("status") if state else None,
            "repositorio_codigo": state.get("repositorio_codigo") if state else None,
            "objetivo": state.get("objetivo") if state else None,
            "session_count": session_count,
        })
    return {"projects": result, "count": len(result), "branch": real_branch}


@router.get("/projects/{slug}")
def get_project(slug: str, branch: str = Query(None)):
    projetos_dir, real_branch = resolve_projetos_dir(branch)
    project_dir = projetos_dir / slug
    if not project_dir.exists() or not (project_dir / "project-state.yaml").exists():
        raise HTTPException(status_code=404, detail=f"Projeto '{slug}' não encontrado")
    state = _load_yaml(project_dir / "project-state.yaml")
    if not state:
        raise HTTPException(status_code=500, detail=f"Erro ao ler project-state de '{slug}'")
    fontes = {}
    for sub in ["fontes", "arquitetura", "tarefas", "rotinas", "frameworks", "ferramentas", "docs", "sessoes", "conversas"]:
        fontes[sub] = _list_markdown_files(projetos_dir, slug, sub)
    relatorios = {}
    rel_dir = project_dir / "relatorios"
    if rel_dir.exists():
        for sub in rel_dir.iterdir():
            if sub.is_dir():
                relatorios[sub.name] = _list_markdown_files(projetos_dir, slug, f"relatorios/{sub.name}")
    return {
        "slug": slug,
        "project_state": state,
        "repositorio_codigo": state.get("repositorio_codigo"),
        "fontes": fontes,
        "relatorios": relatorios,
    }


@router.get("/projects/{slug}/state")
def get_project_state(slug: str, branch: str = Query(None)):
    projetos_dir, real_branch = resolve_projetos_dir(branch)
    project_dir = projetos_dir / slug
    if not project_dir.exists():
        raise HTTPException(status_code=404, detail=f"Projeto '{slug}' não encontrado")
    state = _load_yaml(project_dir / "project-state.yaml")
    if not state:
        raise HTTPException(status_code=404, detail="project-state.yaml não encontrado")
    return {**state, "branch_detectada": real_branch}


@router.get("/projects/{slug}/mastery-paths")
def get_mastery_paths(slug: str, branch: str = Query(None)):
    projetos_dir, real_branch = resolve_projetos_dir(branch)
    project_dir = projetos_dir / slug
    if not project_dir.exists():
        raise HTTPException(status_code=404, detail=f"Projeto '{slug}' não encontrado")
    state = _load_yaml(project_dir / "project-state.yaml")
    paths = state.get("mastery_paths", []) if state else []
    return {"mastery_paths": paths, "count": len(paths)}


@router.get("/projects/{slug}/{database}")
def get_project_database(slug: str, database: str, branch: str = Query(None)):
    projetos_dir, real_branch = resolve_projetos_dir(branch)
    project_dir = projetos_dir / slug
    if not project_dir.exists():
        raise HTTPException(status_code=404, detail=f"Projeto '{slug}' não encontrado")
    allowed = {"fontes", "arquitetura", "tarefas", "rotinas", "frameworks", "ferramentas", "docs", "sessoes", "conversas"}
    if database not in allowed:
        raise HTTPException(status_code=400, detail=f"Database inválida. Use: {', '.join(sorted(allowed))}")
    return {database: _list_markdown_files(projetos_dir, slug, database)}


@router.get("/branches")
def list_branches():
    import subprocess
    try:
        result = subprocess.run(
            ["git", "worktree", "list"],
            capture_output=True, text=True, cwd=REPO_DIR, timeout=5
        )
        branches = []
        for line in result.stdout.strip().split("\n"):
            parts = line.split()
            if len(parts) >= 3:
                branches.append({"path": parts[0], "branch": parts[2].strip("[]")})
            elif len(parts) >= 2:
                branches.append({"path": parts[0], "branch": parts[1]})
        return {"branches": branches, "current": current_branch()}
    except Exception as e:
        return {"branches": [], "current": current_branch(), "error": str(e)}


@router.get("/profile")
def get_profile(branch: str = Query(None)):
    projetos_dir, real_branch = resolve_projetos_dir(branch)
    profile_path = projetos_dir / "perfis" / "frota.yaml"
    profile = _load_yaml(profile_path)
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil Frota não encontrado")
    return profile
