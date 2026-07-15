from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from deeptutor.services.sources.manager import SourceManager

router = APIRouter(prefix="/api/v1/sources", tags=["Sources"])
manager = SourceManager()


@router.get("")
async def list_sources(area: Optional[str] = Query(None, description="Filtrar por área")):
    providers = manager.list_providers(area)
    return {"providers": [p.__dict__ for p in providers]}


@router.get("/{provider_id}")
async def get_source(provider_id: str):
    p = manager.get_provider(provider_id)
    if not p:
        raise HTTPException(404, f"Provider '{provider_id}' não encontrado")
    return p.__dict__


@router.get("/projects/{slug}/sources")
async def list_project_sources(slug: str, all: bool = Query(False, alias="all")):
    sources = manager.list_project_sources(slug, enabled_only=not all)
    return {"project_slug": slug, "sources": [s.__dict__ for s in sources]}


@router.post("/projects/{slug}/sources")
async def add_project_source(slug: str, provider_id: str = Query(...)):
    p = manager.get_provider(provider_id)
    if not p:
        raise HTTPException(404, f"Provider '{provider_id}' não existe no catálogo")
    ps = manager.add_source(slug, provider_id)
    return {"project_slug": slug, "source": ps.__dict__}


@router.delete("/projects/{slug}/sources/{provider_id}")
async def remove_project_source(slug: str, provider_id: str):
    manager.remove_source(slug, provider_id)
    return {"status": "removed", "project_slug": slug, "provider_id": provider_id}


@router.patch("/projects/{slug}/sources/{provider_id}")
async def toggle_project_source(slug: str, provider_id: str, enabled: bool = Query(...)):
    manager.toggle_source(slug, provider_id, enabled)
    return {"status": "updated", "project_slug": slug, "provider_id": provider_id, "enabled": enabled}


@router.post("/projects/{slug}/sources/suggest")
async def suggest_sources(slug: str, area: str = Query(...)):
    info = manager.suggest_sources(area)
    return {"area": area, "suggestion": [p.__dict__ for p in info]}


@router.post("/projects/{slug}/sources/apply-suggestions")
async def apply_suggestions(slug: str, area: str = Query(...)):
    applied = manager.apply_suggestions(slug, area)
    return {"area": area, "applied": [s.__dict__ for s in applied]}


@router.get("/projects/{slug}/sources/search")
async def search_project_sources(slug: str, q: str = Query(..., min_length=1), limit: int = Query(10, ge=1, le=50)):
    results = await manager.search_project_sources(slug, q, limit=limit)
    return {
        "query": q,
        "project_slug": slug,
        "results": results,
    }
