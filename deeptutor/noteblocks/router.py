from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException

from .models import Note
from .storage import NoteStorage

router = APIRouter(prefix="/api/v1/noteblocks", tags=["noteblocks"])

NOTES_DIR = Path("data/noteblocks/notes")
storage = NoteStorage(NOTES_DIR)


@router.get("/notes")
async def list_notes() -> list[str]:
    return storage.list_ids()


@router.get("/notes/{note_id}")
async def get_note(note_id: str) -> Note:
    note = storage.load(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.post("/notes", status_code=201)
async def create_note(note: Note) -> Note:
    storage.save(note)
    return note


@router.put("/notes/{note_id}")
async def update_note(note_id: str, note: Note) -> Note:
    if storage.load(note_id) is None:
        raise HTTPException(status_code=404, detail="Note not found")
    note.id = note_id
    storage.save(note)
    return note


@router.delete("/notes/{note_id}", status_code=204)
async def delete_note(note_id: str) -> None:
    if not storage.delete(note_id):
        raise HTTPException(status_code=404, detail="Note not found")
