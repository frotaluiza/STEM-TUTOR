from __future__ import annotations

from pathlib import Path

from deeptutor.noteblocks.models import Block, BlockType, Note
from deeptutor.noteblocks.storage import NoteStorage, markdown_to_note, note_to_markdown


def test_save_and_load(tmp_notes_dir: Path, sample_note: Note) -> None:
    storage = NoteStorage(tmp_notes_dir)
    storage.save(sample_note)
    loaded = storage.load(sample_note.id)
    assert loaded is not None
    assert loaded.title == sample_note.title
    assert len(loaded.blocks) == len(sample_note.blocks)
    assert loaded.blocks[0].content == sample_note.blocks[0].content
    assert loaded.tags == sample_note.tags


def test_load_nonexistent(tmp_notes_dir: Path) -> None:
    storage = NoteStorage(tmp_notes_dir)
    assert storage.load("nao-existe") is None


def test_delete(tmp_notes_dir: Path, sample_note: Note) -> None:
    storage = NoteStorage(tmp_notes_dir)
    storage.save(sample_note)
    assert storage.delete(sample_note.id) is True
    assert storage.load(sample_note.id) is None
    assert storage.delete(sample_note.id) is False


def test_list_ids(tmp_notes_dir: Path, sample_note: Note) -> None:
    storage = NoteStorage(tmp_notes_dir)
    assert storage.list_ids() == []
    storage.save(sample_note)
    assert sample_note.id in storage.list_ids()


def test_roundtrip_preserves_blocks(tmp_notes_dir: Path) -> None:
    note = Note(
        id="rt-1",
        title="Roundtrip",
        blocks=[
            Block(type=BlockType.HEADING, content="Section"),
            Block(type=BlockType.TEXT, content="Some text"),
            Block(type=BlockType.ASK, content="A question?"),
            Block(type=BlockType.COMMAND, content="npm test"),
        ],
    )
    storage = NoteStorage(tmp_notes_dir)
    storage.save(note)
    loaded = storage.load(note.id)
    assert loaded is not None
    assert loaded.title == "Roundtrip"
    assert loaded.blocks[0].type == BlockType.HEADING
    assert loaded.blocks[0].content == "Section"
    assert loaded.blocks[2].type == BlockType.ASK


def test_markdown_roundtrip(sample_note: Note) -> None:
    md = note_to_markdown(sample_note)
    restored = markdown_to_note(md)
    assert restored.title == sample_note.title
    assert len(restored.blocks) == len(sample_note.blocks)
    assert restored.tags == sample_note.tags


def test_invalid_markdown_raises() -> None:
    try:
        markdown_to_note("no frontmatter here")
        assert False, "Should have raised"
    except ValueError:
        pass
