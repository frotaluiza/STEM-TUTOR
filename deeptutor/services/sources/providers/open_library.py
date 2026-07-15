import httpx
from typing import Any

from deeptutor.services.sources.providers.base import BaseSourceProvider
from deeptutor.services.sources.registry import register_provider_class


@register_provider_class("open_library")
class OpenLibraryProvider(BaseSourceProvider):
    provider_id = "open_library"
    provider_name = "Open Library"

    async def search(self, query: str, limit: int = 10) -> list[dict[str, Any]]:
        url = "https://openlibrary.org/search.json"
        async with httpx.AsyncClient(timeout=15) as client:
            resp = await client.get(url, params={"q": query, "limit": limit, "fields": "key,title,author_name,first_publish_year,isbn,cover_i,subtitle"})
            resp.raise_for_status()
            data = resp.json()

        results = []
        for doc in data.get("docs", []):
            cover_id = doc.get("cover_i")
            results.append(self.normalize_result({
                "title": doc.get("title", "Sem título"),
                "url": f"https://openlibrary.org{doc['key']}" if doc.get("key") else None,
                "snippet": doc.get("subtitle") or "",
                "author": ", ".join(doc.get("author_name", [])) if doc.get("author_name") else None,
                "year": doc.get("first_publish_year"),
                "type": "book",
                "thumbnail": f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg" if cover_id else None,
            }))
        return results
