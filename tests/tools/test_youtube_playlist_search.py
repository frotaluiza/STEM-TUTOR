from __future__ import annotations

import os
from unittest.mock import AsyncMock, patch

import httpx
import pytest

from deeptutor.services.youtube_search import (
    YouTubePlaylistSearchClient,
    YouTubeSearchResponse,
    YouTubeSearchResult,
)
from deeptutor.tools.youtube_playlist_search import (
    YouTubePlaylistSearcher,
    youtube_playlist_search,
)


def _mock_response(status_code: int, json_data: dict) -> httpx.Response:
    return httpx.Response(
        status_code=status_code,
        json=json_data,
        request=httpx.Request("GET", "https://www.googleapis.com/youtube/v3/search"),
    )


def _make_playlist_item(
    playlist_id: str,
    title: str,
    channel: str = "Test Channel",
    description: str = "",
) -> dict:
    return {
        "id": {"playlistId": playlist_id},
        "snippet": {
            "title": title,
            "channelTitle": channel,
            "description": description,
            "publishedAt": "2024-01-01T00:00:00Z",
            "thumbnails": {
                "default": {"url": f"https://i.ytimg.com/vi/{playlist_id}/default.jpg"},
                "high": {"url": f"https://i.ytimg.com/vi/{playlist_id}/high.jpg"},
            },
        },
    }


def _make_video_item(
    video_id: str,
    title: str,
    channel: str = "Test Channel",
    description: str = "",
) -> dict:
    return {
        "id": {"videoId": video_id},
        "snippet": {
            "title": title,
            "channelTitle": channel,
            "description": description,
            "publishedAt": "2024-01-01T00:00:00Z",
            "thumbnails": {
                "default": {"url": f"https://i.ytimg.com/vi/{video_id}/default.jpg"},
                "high": {"url": f"https://i.ytimg.com/vi/{video_id}/high.jpg"},
            },
        },
    }


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class TestYouTubeSearchResult:
    def test_playlist_result(self) -> None:
        r = YouTubeSearchResult(
            kind="playlist",
            title="Linear Algebra",
            url="https://www.youtube.com/playlist?list=PL123",
            channel_title="Math Channel",
            description="Full course",
            thumbnail_url="https://i.ytimg.com/vi/123/default.jpg",
            published_at="2024-01-01T00:00:00Z",
            video_count=42,
            playlist_id="PL123",
        )
        assert r.kind == "playlist"
        assert r.video_count == 42
        assert r.playlist_id == "PL123"
        assert r.video_id is None

    def test_video_result(self) -> None:
        r = YouTubeSearchResult(
            kind="video",
            title="Intro to Calculus",
            url="https://www.youtube.com/watch?v=abc123",
            channel_title="Math Channel",
            description="Great intro",
            thumbnail_url="https://i.ytimg.com/vi/abc123/default.jpg",
            published_at="2024-01-01T00:00:00Z",
            video_id="abc123",
        )
        assert r.kind == "video"
        assert r.video_id == "abc123"
        assert r.video_count is None


class TestYouTubeSearchResponse:
    def test_has_results_true(self) -> None:
        r = YouTubeSearchResponse(
            query="test",
            results=[
                YouTubeSearchResult(
                    kind="playlist",
                    title="T",
                    url="https://youtube.com/playlist?list=PL1",
                    channel_title="C",
                    description="",
                    thumbnail_url="",
                    published_at="2024-01-01T00:00:00Z",
                )
            ],
        )
        assert r.has_results

    def test_has_results_false(self) -> None:
        r = YouTubeSearchResponse(query="test")
        assert not r.has_results

    def test_fallback_flag(self) -> None:
        r = YouTubeSearchResponse(
            query="test",
            results=[
                YouTubeSearchResult(
                    kind="video",
                    title="T",
                    url="https://youtube.com/watch?v=v1",
                    channel_title="C",
                    description="",
                    thumbnail_url="",
                    published_at="2024-01-01T00:00:00Z",
                    video_id="v1",
                )
            ],
            fallback_used=True,
        )
        assert r.fallback_used

    def test_error_response(self) -> None:
        r = YouTubeSearchResponse(query="test", error="API error")
        assert r.error == "API error"


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------


class TestYouTubePlaylistSearchClient:
    def test_no_api_key(self) -> None:
        client = YouTubePlaylistSearchClient(api_key="")
        assert not client._is_available()

    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_search_playlists_found(self, mock_get: AsyncMock) -> None:
        search_response = {
            "items": [
                _make_playlist_item("PL1", "Calculus 101", description="Full course"),
                _make_playlist_item("PL2", "Linear Algebra", description="Vectors"),
            ]
        }
        details_response = {
            "items": [
                {"id": "PL1", "contentDetails": {"itemCount": 30}},
                {"id": "PL2", "contentDetails": {"itemCount": 25}},
            ]
        }

        mock_get.side_effect = [
            _mock_response(200, search_response),
            _mock_response(200, details_response),
        ]

        client = YouTubePlaylistSearchClient(api_key="test-key")
        result = await client.search("calculus", max_results=5)

        assert result.has_results
        assert not result.fallback_used
        assert result.error is None
        assert len(result.results) == 2
        assert result.results[0].kind == "playlist"
        assert result.results[0].title == "Calculus 101"
        assert result.results[0].video_count == 30
        assert result.results[1].video_count == 25

    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_search_fallback_to_videos(self, mock_get: AsyncMock) -> None:
        search_playlist_response: dict = {"items": []}
        search_video_response = {
            "items": [
                _make_video_item("v1", "Intro to Calculus"),
                _make_video_item("v2", "Derivatives Explained"),
            ]
        }

        mock_get.side_effect = [
            _mock_response(200, search_playlist_response),
            _mock_response(200, search_video_response),
        ]

        client = YouTubePlaylistSearchClient(api_key="test-key")
        result = await client.search("calculus", max_results=5)

        assert result.has_results
        assert result.fallback_used
        assert len(result.results) == 2
        assert result.results[0].kind == "video"

    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_search_empty_query(self, mock_get: AsyncMock) -> None:
        client = YouTubePlaylistSearchClient(api_key="test-key")
        result = await client.search("", max_results=5)

        assert not result.has_results
        assert result.error == "Query is empty"
        mock_get.assert_not_called()

    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_search_no_results(self, mock_get: AsyncMock) -> None:
        mock_get.return_value = _mock_response(200, {"items": []})

        client = YouTubePlaylistSearchClient(api_key="test-key")
        result = await client.search("xyznonexistent", max_results=5)

        assert not result.has_results
        assert not result.fallback_used

    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_search_api_error(self, mock_get: AsyncMock) -> None:
        mock_get.side_effect = httpx.HTTPStatusError(
            "403 Forbidden",
            request=httpx.Request("GET", "https://example.com"),
            response=httpx.Response(403),
        )

        client = YouTubePlaylistSearchClient(api_key="test-key")
        result = await client.search("calculus", max_results=5)

        assert not result.has_results
        assert "403" in (result.error or "")

    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_search_no_api_key(self, mock_get: AsyncMock) -> None:
        client = YouTubePlaylistSearchClient(api_key="")
        result = await client.search("calculus", max_results=5)

        assert not result.has_results
        mock_get.assert_not_called()


# ---------------------------------------------------------------------------
# Searcher tool
# ---------------------------------------------------------------------------


class TestYouTubePlaylistSearcher:
    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_searcher_playlists(self, mock_get: AsyncMock) -> None:
        search_response = {
            "items": [
                _make_playlist_item("PL1", "Calculus"),
            ]
        }
        details_response = {
            "items": [
                {"id": "PL1", "contentDetails": {"itemCount": 42}},
            ]
        }
        mock_get.side_effect = [
            _mock_response(200, search_response),
            _mock_response(200, details_response),
        ]

        searcher = YouTubePlaylistSearcher(api_key="test-key")
        result = await searcher.search_playlists("calculus", max_results=5)

        assert len(result["results"]) == 1
        assert result["results"][0]["kind"] == "playlist"
        assert result["results"][0]["video_count"] == 42
        assert not result["fallback_used"]

    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_searcher_empty_query(self, mock_get: AsyncMock) -> None:
        searcher = YouTubePlaylistSearcher()
        result = await searcher.search_playlists("", max_results=5)

        assert result["error"] == "Query is empty"
        mock_get.assert_not_called()


class TestYouTubePlaylistSearchFunction:
    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_function_playlists(self, mock_get: AsyncMock) -> None:
        search_response = {
            "items": [
                _make_playlist_item("PL1", "Linear Algebra"),
            ]
        }
        details_response = {
            "items": [
                {"id": "PL1", "contentDetails": {"itemCount": 30}},
            ]
        }
        mock_get.side_effect = [
            _mock_response(200, search_response),
            _mock_response(200, details_response),
        ]

        with patch.dict(os.environ, {"YOUTUBE_API_KEY": "test-key"}, clear=False):
            result = await youtube_playlist_search(query="linear algebra", max_results=5)

        assert len(result["results"]) == 1
        assert result["results"][0]["kind"] == "playlist"
        assert result["results"][0]["title"] == "Linear Algebra"

    @patch.object(httpx.AsyncClient, "get")
    @pytest.mark.asyncio
    async def test_function_empty_query(self, mock_get: AsyncMock) -> None:
        result = await youtube_playlist_search(query="", max_results=5)

        assert result["error"] == "Query is empty"
        mock_get.assert_not_called()
