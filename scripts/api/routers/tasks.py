from pathlib import Path

from fastapi import APIRouter, Query

router = APIRouter()

PROJETOS_DIR = Path(__file__).resolve().parents[3] / "Projetos"


@router.get("/tasks")
def list_tasks(projeto: str = Query(None)):
    if projeto:
        tasks = _load_tasks_for_project(projeto)
        return {"tasks": tasks, "count": len(tasks)}

    todas = []
    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir() or not (d / "project-state.yaml").exists():
            continue
        todas.extend(_load_tasks_for_project(d.name))
    return {"tasks": todas, "count": len(todas)}


def _load_tasks_for_project(slug: str):
    tasks = []
    tarefas_dir = PROJETOS_DIR / slug / "tarefas"
    if not tarefas_dir.exists():
        return tasks
    for f in sorted(tarefas_dir.glob("*.md"), reverse=True):
        content = f.read_text(encoding="utf-8")
        tasks.append({
            "slug": f.stem,
            "arquivo": f.name,
            "projeto": slug,
            "conteudo": content,
        })
    return tasks
