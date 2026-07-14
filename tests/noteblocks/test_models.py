from __future__ import annotations

from deeptutor.noteblocks.models import Block, BlockType, Note


def test_block_default_id() -> None:
    b = Block(type=BlockType.TEXT, content="hello")
    assert b.id
    assert len(b.id) == 12


def test_block_different_types() -> None:
    b1 = Block(type=BlockType.ASK, content="question?")
    assert b1.type == BlockType.ASK

    b2 = Block(type=BlockType.COMMAND, content="ls -la")
    assert b2.type == BlockType.COMMAND


def test_note_creation(sample_note: Note) -> None:
    assert sample_note.title == "Minha Nota"
    assert len(sample_note.blocks) == 3
    assert sample_note.tags == ["ai", "test"]


def test_note_default_id() -> None:
    n = Note(title="Test")
    assert n.id
    assert len(n.id) == 12


def test_note_with_blocks(sample_note: Note) -> None:
    assert sample_note.blocks[0].type == BlockType.TEXT
    assert sample_note.blocks[1].type == BlockType.ASK
    assert sample_note.blocks[2].type == BlockType.HEADING
