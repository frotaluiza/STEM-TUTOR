from __future__ import annotations

from pathlib import Path
import uuid

from fastapi import APIRouter, UploadFile

from .models import AttachmentRef

router = APIRouter(prefix="/api/v1/noteblocks/attachments", tags=["noteblocks-attachments"])

ATTACHMENTS_DIR = Path("data/noteblocks/attachments")
ATTACHMENTS_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_attachment(file: UploadFile) -> AttachmentRef:
    ext = Path(file.filename or "file").suffix if file.filename else ""
    file_id = uuid.uuid4().hex[:12]
    dest = ATTACHMENTS_DIR / f"{file_id}{ext}"
    content = await file.read()
    dest.write_bytes(content)

    mime = file.content_type or "application/octet-stream"
    ref = AttachmentRef(id=file_id, name=file.filename or "file", mime_type=mime, path=str(dest))
    return ref


@router.get("/{file_id}")
async def get_attachment(file_id: str) -> dict:
    for p in ATTACHMENTS_DIR.iterdir():
        if p.stem == file_id:
            return {"id": file_id, "name": p.name, "path": str(p)}
    return {"error": "not found"}
