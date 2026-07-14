from __future__ import annotations

from pathlib import Path

import pytest

from deeptutor.noteblocks.models import Block, BlockType, Note


@pytest.fixture
def tmp_notes_dir(tmp_path: Path) -> Path:
    return tmp_path / "notes"


@pytest.fixture
def sample_note() -> Note:
    return Note(
        id="test-1",
        title="Minha Nota",
        tags=["ai", "test"],
        blocks=[
            Block(id="b1", type=BlockType.TEXT, content="Hello world"),
            Block(id="b2", type=BlockType.ASK, content="O que é isso?"),
            Block(id="b3", type=BlockType.HEADING, content="Seção Importante"),
        ],
    )
