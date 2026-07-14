from __future__ import annotations

import os
from pathlib import Path

from notion_client import Client

from .models import Note
from .storage import NoteStorage, note_to_markdown

NOTION_TOKEN_ENV = "NOTION_TOKEN"
NOTION_SESSOES_DB = "NOTION_SESSOES_DB_ID"

NOTES_DIR = Path("data/noteblocks/notes")
storage = NoteStorage(NOTES_DIR)


def _get_client() -> Client | None:
    token = os.environ.get(NOTION_TOKEN_ENV)
    if not token:
        return None
    return Client(auth=token)


def note_to_notion_blocks(note: Note) -> list[dict]:
    blocks: list[dict] = []

    for block in note.blocks:
        text = block.content
        if not text:
            continue

        if block.type == "heading":
            blocks.append(
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"type": "text", "text": {"content": text[:2000]}}]
                    },
                }
            )
        elif block.type == "ask":
            blocks.append(
                {
                    "object": "block",
                    "type": "callout",
                    "callout": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": f"@ask {text[:2000]}"},
                            }
                        ],
                        "color": "green_background",
                    },
                }
            )
        elif block.type == "command":
            blocks.append(
                {
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": text[:2000]},
                            }
                        ],
                        "language": "shell",
                    },
                }
            )
        elif block.type == "output":
            blocks.append(
                {
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": text[:2000]},
                            }
                        ],
                        "language": "plain text",
                    },
                }
            )
        else:
            blocks.append(
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": text[:2000]}}]
                    },
                }
            )

    return blocks


async def sync_note_to_notion(note_id: str, database_id: str | None = None) -> dict:
    note = storage.load(note_id)
    if note is None:
        return {"error": "Note not found"}

    client = _get_client()
    if client is None:
        return {"error": f"Notion token not set. Set {NOTION_TOKEN_ENV} env var."}

    db_id = database_id or os.environ.get(NOTION_SESSOES_DB)
    if not db_id:
        return {"error": f"Database ID not set. Set {NOTION_SESSOES_DB} env var."}

    title = note.title[:2000]
    md_content = note_to_markdown(note)
    summary = md_content[:2000]

    try:
        page = client.pages.create(
            parent={"database_id": db_id},
            properties={
                "title": {"title": [{"type": "text", "text": {"content": title}}]},
                "Resumo (curto)": {"rich_text": [{"type": "text", "text": {"content": summary}}]},
            },
        )

        page_id = page["id"]
        blocks = note_to_notion_blocks(note)
        if blocks:
            for i in range(0, len(blocks), 100):
                chunk = blocks[i : i + 100]
                client.blocks.children.append(block_id=page_id, children=chunk)

        return {
            "success": True,
            "page_id": page_id,
            "url": page.get("url", ""),
        }

    except Exception as e:
        return {"error": str(e)}
