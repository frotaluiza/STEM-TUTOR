from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
import uuid

from pydantic import BaseModel, Field


class BlockType(str, Enum):
    TEXT = "text"
    HEADING = "heading"
    MARKDOWN = "markdown"
    ASK = "ask"
    COMMAND = "command"
    OUTPUT = "output"
    ATTACHMENT = "attachment"
    QUESTION = "question"


class QuestionOption(BaseModel):
    id: str = ""
    label: str = ""
    correct: bool = False


class AttachmentRef(BaseModel):
    id: str
    name: str
    mime_type: str
    path: str


class Block(BaseModel):
    id: str = Field(default_factory=lambda: uuid.uuid4().hex[:12])
    type: BlockType
    content: str = ""
    origin: str | None = None  # "human" | "opencode" | "tutor" | None
    collapsed: bool | None = None
    meta: dict[
        str, Any
    ] = {}  # { "flags": ["important","weak","remember","mastered"], "source": "..." }
    flags: list[
        str
    ] = []  # "important"(azul) | "remember"(laranja) | "weak"(vermelho) | "mastered"(verde) | "source"(cinza)


class Note(BaseModel):
    id: str = Field(default_factory=lambda: uuid.uuid4().hex[:12])
    title: str = "Untitled"
    blocks: list[Block] = []
    tags: list[str] = []
    level: str = ""  # iniciante | basico | intermediario | avancado
    level_topic: str = ""
    attachments: list[AttachmentRef] = []
    project: str | None = None
    session: str | None = None
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
