from abc import ABC, abstractmethod
from typing import Any


class BaseSourceProvider(ABC):
    provider_id: str = ""
    provider_name: str = ""

    @abstractmethod
    async def search(self, query: str, limit: int = 10) -> list[dict[str, Any]]:
        ...

    def normalize_result(self, raw: dict[str, Any]) -> dict[str, Any]:
        return {
            "title": raw.get("title", ""),
            "url": raw.get("url", ""),
            "snippet": raw.get("snippet", ""),
            "source": self.provider_id,
            "type": raw.get("type", "unknown"),
            "thumbnail": raw.get("thumbnail", ""),
            "author": raw.get("author"),
            "year": raw.get("year"),
        }
