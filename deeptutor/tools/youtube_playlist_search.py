from __future__ import annotations

import logging

from deeptutor.services.youtube_search import YouTubePlaylistSearchClient

logger = logging.getLogger(__name__)


class YouTubePlaylistSearcher:
    def __init__(self, api_key: str | None = None) -> None:
        self.client = YouTubePlaylistSearchClient(api_key=api_key)

    async def search_playlists(
        self,
        query: str,
        max_results: int = 5,
        allow_video_fallback: bool = True,
    ) -> dict:
        query = (query or "").strip()
        if not query:
            return {
                "query": "",
                "results": [],
                "fallback_used": False,
                "error": "Query is empty",
            }

        response = await self.client.search(query=query, max_results=max_results)

        return {
            "query": response.query,
            "results": [
                {
                    "kind": r.kind,
                    "title": r.title,
                    "url": r.url,
                    "channel_title": r.channel_title,
                    "description": r.description[:300] if r.description else "",
                    "thumbnail_url": r.thumbnail_url,
                    "published_at": r.published_at,
                    "video_count": r.video_count,
                    "playlist_id": r.playlist_id,
                    "video_id": r.video_id,
                }
                for r in response.results
            ],
            "fallback_used": response.fallback_used,
            "error": response.error,
        }


async def youtube_playlist_search(
    query: str,
    max_results: int = 5,
    allow_video_fallback: bool = True,
) -> dict:
    searcher = YouTubePlaylistSearcher()
    return await searcher.search_playlists(
        query=query,
        max_results=max_results,
        allow_video_fallback=allow_video_fallback,
    )


async def main():
    searcher = YouTubePlaylistSearcher()

    print("Search: calculus")
    result = await searcher.search_playlists(query="calculus", max_results=3)

    print(f"\nFallback used: {result['fallback_used']}")
    print(f"Error: {result['error']}")
    print(f"Found {len(result['results'])} results:\n")

    for i, item in enumerate(result["results"], 1):
        if item["kind"] == "playlist":
            print(f"{i}. [PLAYLIST] {item['title']}")
            print(f"   Channel: {item['channel_title']}")
            print(f"   Videos: {item['video_count']}")
        else:
            print(f"{i}. [VIDEO] {item['title']}")
            print(f"   Channel: {item['channel_title']}")
        print(f"   URL: {item['url']}")
        print()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
