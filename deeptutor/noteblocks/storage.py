from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from .models import AttachmentRef, Block, BlockType, Note


def _collect_block_meta(blocks: list[Block]) -> list[dict]:
    """Collect origin/collapsed from blocks for frontmatter storage."""
    meta = []
    for b in blocks:
        entry: dict = {}
        if b.origin:
            entry["origin"] = b.origin
        if b.collapsed:
            entry["collapsed"] = True
        meta.append(entry)
    return meta


def _apply_block_meta(blocks: list[Block], meta: list[dict]) -> list[Block]:
    """Apply origin/collapsed from frontmatter metadata back to blocks."""
    result = []
    for i, b in enumerate(blocks):
        if i < len(meta):
            entry = meta[i]
            origin = entry.get("origin")
            collapsed = entry.get("collapsed", False)
            result.append(Block(
                id=b.id, type=b.type, content=b.content,
                origin=origin, collapsed=collapsed,
                meta=b.meta, flags=b.flags,
            ))
        else:
            result.append(b)
    return result


def note_to_markdown(note: Note) -> str:
    frontmatter: dict[str, Any] = {
        "title": note.title,
        "created": note.created.isoformat(),
        "updated": note.updated.isoformat(),
        "tags": note.tags,
    }
    if note.project:
        frontmatter["project"] = note.project
    if note.session:
        frontmatter["session"] = note.session
    if note.level:
        frontmatter["level"] = note.level
    if note.level_topic:
        frontmatter["level_topic"] = note.level_topic
    if note.attachments:
        frontmatter["attachments"] = [
            {"id": a.id, "name": a.name, "mime_type": a.mime_type} for a in note.attachments
        ]

    block_meta = _collect_block_meta(note.blocks)
    has_meta = any(m for m in block_meta)
    if has_meta:
        frontmatter["_blocks"] = block_meta

    body_parts: list[str] = []
    for block in note.blocks:
        if block.type == BlockType.HEADING:
            body_parts.append(f"## {block.content}")
        elif block.type == BlockType.ASK:
            body_parts.append(f"@ask {block.content}")
        elif block.type == BlockType.COMMAND:
            body_parts.append(f"/command {block.content}")
        elif block.type == BlockType.OUTPUT:
            body_parts.append(f"~~~output\n{block.content}\n~~~")
        elif block.type == BlockType.MARKDOWN:
            body_parts.append(f"~~~markdown\n{block.content}\n~~~")
        elif block.type == BlockType.ATTACHMENT:
            body_parts.append(f"📎 {block.content}")
        else:
            body_parts.append(block.content)
        body_parts.append("")

    fm = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False).strip()
    return f"---\n{fm}\n---\n\n" + "\n".join(body_parts)


def markdown_to_note(text: str) -> Note:
    parts = text.split("---\n", 2)
    if len(parts) < 3 or not parts[0].strip() == "":
        raise ValueError("Invalid frontmatter format")

    frontmatter = yaml.safe_load(parts[1]) or {}
    body = parts[2].strip()

    blocks: list[Block] = []
    in_markdown_block = False
    markdown_buffer: list[str] = []

    for line in body.split("\n"):
        stripped = line.strip()

        # Handle ~~~markdown ... ~~~ blocks
        if stripped == "~~~markdown":
            in_markdown_block = True
            markdown_buffer = []
            continue
        if in_markdown_block:
            if stripped == "~~~":
                blocks.append(Block(type=BlockType.MARKDOWN, content="\n".join(markdown_buffer)))
                in_markdown_block = False
                continue
            markdown_buffer.append(line)
            continue

        if not stripped:
            continue
        if stripped.startswith("## "):
            blocks.append(Block(type=BlockType.HEADING, content=stripped[3:]))
        elif stripped.startswith("@ask "):
            blocks.append(Block(type=BlockType.ASK, content=stripped[5:]))
        elif stripped.startswith("❓ "):
            blocks.append(Block(type=BlockType.QUESTION, content=stripped[2:]))
        elif stripped.startswith("/command "):
            blocks.append(Block(type=BlockType.COMMAND, content=stripped[9:]))
        elif stripped.startswith("~~~output"):
            continue
        elif stripped == "~~~":
            continue
        elif stripped.startswith("📎 "):
            blocks.append(Block(type=BlockType.ATTACHMENT, content=stripped[2:]))
        else:
            blocks.append(Block(type=BlockType.TEXT, content=stripped))

    block_meta = frontmatter.get("_blocks")
    if block_meta and isinstance(block_meta, list):
        blocks = _apply_block_meta(blocks, block_meta)

    attachments_raw = frontmatter.get("attachments") or []
    attachments = [AttachmentRef(**a) if isinstance(a, dict) else a for a in attachments_raw]

    return Note(
        id=frontmatter.get("id", ""),
        title=frontmatter.get("title", "Untitled"),
        blocks=blocks,
        tags=frontmatter.get("tags", []),
        level=frontmatter.get("level", ""),
        level_topic=frontmatter.get("level_topic", ""),
        attachments=attachments,
        project=frontmatter.get("project"),
        session=frontmatter.get("session"),
    )


class NoteStorage:
    def __init__(self, base_dir: str | Path) -> None:
        self._base = Path(base_dir)
        self._base.mkdir(parents=True, exist_ok=True)

    def _path(self, note_id: str) -> Path:
        return self._base / f"{note_id}.md"

    def save(self, note: Note) -> None:
        note.updated = datetime.now(timezone.utc)
        self._path(note.id).write_text(note_to_markdown(note), encoding="utf-8")

    def load(self, note_id: str) -> Note | None:
        path = self._path(note_id)
        if not path.exists():
            return None
        text = path.read_text(encoding="utf-8")
        return markdown_to_note(text)

    def delete(self, note_id: str) -> bool:
        path = self._path(note_id)
        if path.exists():
            path.unlink()
            return True
        return False

    def list_ids(self) -> list[str]:
        return [p.stem for p in self._base.glob("*.md")]
