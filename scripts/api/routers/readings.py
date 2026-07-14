from fastapi import APIRouter, Query
from pathlib import Path

router = APIRouter()

PROJETOS_DIR = Path(__file__).resolve().parents[3] / "Projetos"


@router.get("/readings")
def list_readings(projeto: str = Query(None), tipo: str = Query(None)):
    if projeto:
        fontes_dir = PROJETOS_DIR / projeto / "fontes"
        if not fontes_dir.exists():
            return {"readings": [], "count": 0}
        readings = []
        for f in sorted(fontes_dir.glob("*.md"), reverse=True):
            content = f.read_text(encoding="utf-8")
            readings.append({
                "slug": f.stem,
                "arquivo": f.name,
                "projeto": projeto,
                "conteudo": content,
            })
        if tipo:
            readings = [r for r in readings if f"tipo: {tipo}" in r["conteudo"]]
        return {"readings": readings, "count": len(readings)}

    todas = []
    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir() or not (d / "project-state.yaml").exists():
            continue
        fontes_dir = d / "fontes"
        if not fontes_dir.exists():
            continue
        for f in sorted(fontes_dir.glob("*.md"), reverse=True):
            content = f.read_text(encoding="utf-8")
            todas.append({
                "slug": f.stem,
                "arquivo": f.name,
                "projeto": d.name,
                "conteudo": content,
            })
    return {"readings": todas, "count": len(todas)}


@router.get("/readings/{slug}")
def get_reading(slug: str):
    for d in PROJETOS_DIR.iterdir():
        if not d.is_dir():
            continue
        fontes_dir = d / "fontes"
        if not fontes_dir.exists():
            continue
        for f in fontes_dir.glob(f"{slug}.md"):
            return {
                "slug": slug,
                "projeto": d.name,
                "conteudo": f.read_text(encoding="utf-8"),
            }
    return {"error": f"Leitura '{slug}' não encontrada"}
