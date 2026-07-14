import asyncio
import time
from typing import Optional

from deeptutor.services.sources import db as source_db
from deeptutor.services.sources.models import ProjectSource, SourceProvider
from deeptutor.services.sources.suggestions import suggest_for_area

_providers_registered = False


def _ensure_providers() -> None:
    global _providers_registered
    if not _providers_registered:
        from deeptutor.services.sources.providers import register_all_providers
        register_all_providers()
        _providers_registered = True


SourceQueryResult = dict


class SourceManager:
    def __init__(self) -> None:
        _ensure_providers()

    def list_providers(self, area: Optional[str] = None) -> list[SourceProvider]:
        return source_db.list_providers(area)

    def get_provider(self, provider_id: str) -> Optional[SourceProvider]:
        return source_db.get_provider(provider_id)

    def list_project_sources(self, project_slug: str, enabled_only: bool = True) -> list[ProjectSource]:
        return source_db.list_project_sources(project_slug, enabled_only)

    def add_source(self, project_slug: str, provider_id: str, config: Optional[dict] = None) -> ProjectSource:
        return source_db.add_project_source(project_slug, provider_id, config)

    def remove_source(self, project_slug: str, provider_id: str) -> None:
        source_db.remove_project_source(project_slug, provider_id)

    def toggle_source(self, project_slug: str, provider_id: str, enabled: bool) -> None:
        source_db.toggle_project_source(project_slug, provider_id, enabled)

    def suggest_sources(self, area: str) -> list[SourceProvider]:
        suggestion_ids = suggest_for_area(area)
        return [p for pid in suggestion_ids if (p := self.get_provider(pid))]

    def apply_suggestions(self, project_slug: str, area: str) -> list[ProjectSource]:
        return [self.add_source(project_slug, p.id) for p in self.suggest_sources(area)]

    async def search_project_sources(self, project_slug: str, query: str, limit: int = 10) -> list[SourceQueryResult]:
        project_sources = self.list_project_sources(project_slug, enabled_only=True)
        if not project_sources:
            return []

        from deeptutor.services.sources.registry import get_provider_class

        async def search_one(ps: ProjectSource) -> SourceQueryResult:
            cls = get_provider_class(ps.provider_id)
            if cls is None:
                return {"provider_id": ps.provider_id, "provider_name": ps.provider_id, "query": query, "results": [], "error": "provider not implemented"}
            provider = cls()
            start = time.time()
            try:
                results = await provider.search(query, limit=limit)
                elapsed = (time.time() - start) * 1000
                return {"provider_id": ps.provider_id, "provider_name": provider.provider_name, "query": query, "results": results, "error": None, "elapsed_ms": round(elapsed, 2)}
            except Exception as e:
                elapsed = (time.time() - start) * 1000
                return {"provider_id": ps.provider_id, "provider_name": ps.provider_id, "query": query, "results": [], "error": str(e), "elapsed_ms": round(elapsed, 2)}

        tasks = [search_one(ps) for ps in project_sources]
        return await asyncio.gather(*tasks)

    def get_active_providers(self, project_slug: str) -> list[str]:
        return [ps.provider_id for ps in self.list_project_sources(project_slug, enabled_only=True)]
