"""Artefacts API — tutor-generated summaries, explanations, and outputs."""

from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

ARTEFACT_DIRS = [
    Path("data/noteblocks/notes"),
    Path("data/user/workspace/learning"),
    Path("data/user/workspace/outputs"),
]


@router.get("/noteblocks/artefacts")
async def list_artefacts(source: str = Query("", description="Source id (path_id or session_id)")):
    """List all artefacts available for a given source id.

    Artefacts are markdown/text/image files the tutor generated during
    a mastery path session: summaries, explanations, code outputs, etc.
    """
    if not source:
        raise HTTPException(status_code=400, detail="source query param is required")

    entries = []
    seen_paths: set[str] = set()

    for base_dir in ARTEFACT_DIRS:
        if not base_dir.exists():
            continue

        # Look for files named after or containing the source id
        for f in base_dir.iterdir():
            if not f.is_file():
                continue
            name_lower = f.stem.lower()
            source_lower = source.lower()
            if source_lower not in name_lower:
                continue

            if f.suffix in (".md", ".txt", ".json", ".yaml", ".yml"):
                kind = "markdown"
                try:
                    content = f.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    content = ""
            elif f.suffix in (".png", ".jpg", ".jpeg", ".gif", ".svg"):
                kind = "image"
                content = ""
            elif f.suffix in (".py", ".js", ".ts", ".html", ".css"):
                kind = "code"
                try:
                    content = f.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    content = ""
            else:
                kind = "other"
                content = ""

            if f.name not in seen_paths:
                seen_paths.add(f.name)
                entries.append({
                    "name": f.name,
                    "path": str(f.resolve()),
                    "content": content[:50000],  # cap at 50KB
                    "type": kind,
                    "size": f.stat().st_size,
                    "updated": str(f.stat().st_mtime),
                })

    if not entries:
        # Return empty list instead of 404 so the frontend shows "no artefacts"
        return {"entries": [], "source": source}

    entries.sort(key=lambda e: e["updated"], reverse=True)
    return {"entries": entries, "source": source}
