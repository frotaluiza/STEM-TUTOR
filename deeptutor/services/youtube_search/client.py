from __future__ import annotations

import logging
import os

import httpx

from .models import YouTubeSearchResponse, YouTubeSearchResult

YOUTUBE_API_KEY_ENV = "YOUTUBE_API_KEY"
YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"
MAX_RESULTS_CAP = 20
REQUEST_TIMEOUT_S = 15

logger = logging.getLogger(__name__)


class YouTubePlaylistSearchClient:
    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.environ.get(YOUTUBE_API_KEY_ENV, "")

    def _is_available(self) -> bool:
        return bool(self.api_key)

    async def search(self, query: str, max_results: int = 5) -> YouTubeSearchResponse:
        query = (query or "").strip()
        if not query:
            return YouTubeSearchResponse(query=query, error="Query is empty")

        max_results = max(1, min(int(max_results), MAX_RESULTS_CAP))

        try:
            result = await self._search_playlists(query, max_results)
            if result.has_results:
                return result

            return await self._search_videos(query, max_results)

        except httpx.HTTPStatusError as exc:
            logger.warning("YouTube API HTTP error: %s", exc)
            return YouTubeSearchResponse(
                query=query,
                error=f"YouTube API error: {exc.response.status_code}",
            )
        except Exception:
            logger.exception("YouTube search failed for query: %s", query)
            return YouTubeSearchResponse(query=query, error="YouTube search failed")

    async def _search_playlists(self, query: str, max_results: int) -> YouTubeSearchResponse:
        items = await self._call_search_api(query, "playlist", max_results)
        if not items:
            return YouTubeSearchResponse(query=query)

        playlist_ids = [item["id"]["playlistId"] for item in items]
        playlist_details = await self._fetch_playlist_details(playlist_ids)

        results = [
            YouTubeSearchResult(
                kind="playlist",
                title=item["snippet"]["title"],
                url=(f"https://www.youtube.com/playlist?list={item['id']['playlistId']}"),
                channel_title=item["snippet"]["channelTitle"],
                description=item["snippet"]["description"],
                thumbnail_url=(
                    item["snippet"]["thumbnails"]
                    .get("high", item["snippet"]["thumbnails"].get("default", {}))
                    .get("url", "")
                ),
                published_at=item["snippet"]["publishedAt"],
                video_count=playlist_details.get(item["id"]["playlistId"]),
                playlist_id=item["id"]["playlistId"],
            )
            for item in items
        ]

        return YouTubeSearchResponse(query=query, results=results)

    async def _search_videos(self, query: str, max_results: int) -> YouTubeSearchResponse:
        items = await self._call_search_api(query, "video", max_results)
        if not items:
            return YouTubeSearchResponse(query=query)

        results = [
            YouTubeSearchResult(
                kind="video",
                title=item["snippet"]["title"],
                url=(f"https://www.youtube.com/watch?v={item['id']['videoId']}"),
                channel_title=item["snippet"]["channelTitle"],
                description=item["snippet"]["description"],
                thumbnail_url=(
                    item["snippet"]["thumbnails"]
                    .get("high", item["snippet"]["thumbnails"].get("default", {}))
                    .get("url", "")
                ),
                published_at=item["snippet"]["publishedAt"],
                video_id=item["id"]["videoId"],
            )
            for item in items
        ]

        return YouTubeSearchResponse(query=query, results=results, fallback_used=True)

    async def _call_search_api(self, query: str, search_type: str, max_results: int) -> list[dict]:
        if not self._is_available():
            logger.warning(
                "YouTube API key not configured. Set %s env var.",
                YOUTUBE_API_KEY_ENV,
            )
            return []

        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT_S) as client:
            response = await client.get(
                f"{YOUTUBE_API_BASE}/search",
                params={
                    "part": "snippet",
                    "q": query,
                    "type": search_type,
                    "maxResults": max_results,
                    "key": self.api_key,
                },
            )
            response.raise_for_status()
            data = response.json()
            return data.get("items", [])

    async def _fetch_playlist_details(self, playlist_ids: list[str]) -> dict[str, int]:
        if not playlist_ids or not self._is_available():
            return {}

        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT_S) as client:
            response = await client.get(
                f"{YOUTUBE_API_BASE}/playlists",
                params={
                    "part": "contentDetails",
                    "id": ",".join(playlist_ids),
                    "key": self.api_key,
                },
            )
            response.raise_for_status()
            data = response.json()

        return {item["id"]: item["contentDetails"]["itemCount"] for item in data.get("items", [])}
