from fastapi import APIRouter, Query
from pathlib import Path

router = APIRouter()

PROJETOS_DIR = Path(__file__).resolve().parents[3] / "Projetos"


@router.get("/reports/daily")
def list_daily_reports(projeto: str = Query(None)):
    if projeto:
        reports = _load_reports_for_project(projeto)
        return {"reports": reports, "count": len(reports)}

    todas = []
    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir() or not (d / "project-state.yaml").exists():
            continue
        todas.extend(_load_reports_for_project(d.name))
    return {"reports": todas, "count": len(todas)}


def _load_reports_for_project(slug: str):
    reports = []
    rel_dir = PROJETOS_DIR / slug / "relatorios" / "diarios"
    if not rel_dir.exists():
        return reports
    for f in sorted(rel_dir.glob("*.md"), reverse=True):
        content = f.read_text(encoding="utf-8")
        reports.append({
            "slug": f.stem,
            "arquivo": f.name,
            "projeto": slug,
            "conteudo": content,
        })
    return reports
