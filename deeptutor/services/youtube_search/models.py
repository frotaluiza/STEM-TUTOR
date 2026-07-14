from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


@dataclass
class YouTubeSearchResult:
    kind: Literal["playlist", "video"]
    title: str
    url: str
    channel_title: str
    description: str
    thumbnail_url: str
    published_at: str
    video_count: int | None = None
    playlist_id: str | None = None
    video_id: str | None = None


@dataclass
class YouTubeSearchResponse:
    query: str
    results: list[YouTubeSearchResult] = field(default_factory=list)
    fallback_used: bool = False
    error: str | None = None

    @property
    def has_results(self) -> bool:
        return len(self.results) > 0
