from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from .models import Note
from .storage import NoteStorage

router = APIRouter()

NOTES_DIR = Path("data/noteblocks/notes")
storage = NoteStorage(NOTES_DIR)


class ConnectionManager:
    def __init__(self) -> None:
        self._connections: dict[str, set[WebSocket]] = {}

    async def connect(self, note_id: str, ws: WebSocket) -> None:
        await ws.accept()
        if note_id not in self._connections:
            self._connections[note_id] = set()
        self._connections[note_id].add(ws)

    def disconnect(self, note_id: str, ws: WebSocket) -> None:
        self._connections.get(note_id, set()).discard(ws)
        if not self._connections.get(note_id):
            self._connections.pop(note_id, None)

    async def broadcast(self, note_id: str, message: dict[str, Any]) -> None:
        payload = json.dumps(message)
        for ws in self._connections.get(note_id, set()):
            try:
                await ws.send_text(payload)
            except Exception:
                pass


manager = ConnectionManager()


@router.websocket("/api/v1/noteblocks/ws/{note_id}")
async def note_websocket(ws: WebSocket, note_id: str) -> None:
    await manager.connect(note_id, ws)
    try:
        while True:
            raw = await ws.receive_text()
            data = json.loads(raw)
            action = data.get("action")

            if action == "update":
                blocks = data.get("blocks", [])
                note = storage.load(note_id)
                if note:
                    for upd in blocks:
                        for b in note.blocks:
                            if b.id == upd["id"]:
                                b.content = upd.get("content", b.content)
                                if "type" in upd:
                                    b.type = upd["type"]
                    storage.save(note)
                await manager.broadcast(note_id, {"action": "synced", "blocks": blocks})

            elif action == "save":
                note_data = data.get("note", {})
                note = Note(**note_data)
                storage.save(note)
                await manager.broadcast(note_id, {"action": "saved", "note_id": note_id})

            elif action == "load":
                note = storage.load(note_id)
                if note:
                    await ws.send_text(
                        json.dumps({"action": "loaded", "note": note.model_dump(mode="json")})
                    )
                else:
                    await ws.send_text(json.dumps({"action": "loaded", "note": None}))

    except WebSocketDisconnect:
        pass
    finally:
        manager.disconnect(note_id, ws)
