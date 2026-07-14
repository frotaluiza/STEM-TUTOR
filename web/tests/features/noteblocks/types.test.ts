import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { BLOCK_ORIGIN_LABELS } from "../../../features/noteblocks/types";

type BlockOrigin = keyof typeof BLOCK_ORIGIN_LABELS;
type BlockType = "text" | "heading" | "ask" | "command" | "output" | "attachment" | "question" | "toggle";

interface Block {
  id: string;
  type: BlockType;
  origin: BlockOrigin;
  content: string;
  collapsed?: boolean;
  pinned?: boolean;
  meta?: Record<string, unknown>;
}

interface Note {
  id: string;
  title: string;
  blocks: Block[];
  tags: string[];
  project?: string;
  session?: string;
  module?: string;
  node?: string;
  created: string;
  updated: string;
}

function createBlock(overrides: Partial<Block> = {}): Block {
  const origin = overrides.origin ?? "human";
  return {
    id: "b1",
    type: "text",
    origin,
    content: "",
    collapsed: origin !== "human",
    pinned: false,
    ...overrides,
  };
}

function createNote(overrides: Partial<Note> = {}): Note {
  return {
    id: "",
    title: "Test",
    blocks: [createBlock()],
    tags: [],
    created: new Date().toISOString(),
    updated: new Date().toISOString(),
    ...overrides,
  };
}

describe("Block model", () => {
  it("should create a human block with default collapsed=false and pinned=false", () => {
    const block = createBlock({ origin: "human" });
    assert.equal(block.origin, "human");
    assert.equal(block.collapsed, false);
    assert.equal(block.pinned, false);
  });

  it("should create an opencode block with collapsed=true by default", () => {
    const block = createBlock({ origin: "opencode" });
    assert.equal(block.origin, "opencode");
    assert.equal(block.collapsed, true);
  });

  it("should create a tutor block with collapsed=true by default", () => {
    const block = createBlock({ origin: "tutor" });
    assert.equal(block.origin, "tutor");
    assert.equal(block.collapsed, true);
  });

  it("should toggle collapsed state", () => {
    const block = createBlock({ origin: "opencode", collapsed: true });
    const toggled = { ...block, collapsed: !block.collapsed };
    assert.equal(toggled.collapsed, false);
    const toggledBack = { ...toggled, collapsed: !toggled.collapsed };
    assert.equal(toggledBack.collapsed, true);
  });

  it("should toggle pinned state", () => {
    const block = createBlock({ origin: "opencode" });
    assert.equal(block.pinned, false);
    const pinned = { ...block, pinned: true };
    assert.equal(pinned.pinned, true);
    const unpinned = { ...pinned, pinned: false };
    assert.equal(unpinned.pinned, false);
  });

  it("should accept all block types", () => {
    const types: BlockType[] = ["text", "heading", "ask", "command", "output", "attachment", "question", "toggle"];
    for (const t of types) {
      const block = createBlock({ type: t });
      assert.equal(block.type, t);
    }
  });

  it("should accept session_id in meta", () => {
    const block = createBlock({
      origin: "opencode",
      meta: { session_id: "ses_123" },
    });
    assert.equal(block.meta?.session_id, "ses_123");
  });

  it("should accept model and agent in meta", () => {
    const block = createBlock({
      origin: "opencode",
      meta: { model: "deepseek-v4", agent: "build", command: "ls -la" },
    });
    assert.equal(block.meta?.model, "deepseek-v4");
    assert.equal(block.meta?.agent, "build");
    assert.equal(block.meta?.command, "ls -la");
  });
});

describe("Note model", () => {
  it("should create a note with blocks", () => {
    const note = createNote({
      title: "Cálculo I",
      project: "ai-stem-tutor",
      module: "calculo-i",
      node: "Cálculo I",
    });
    assert.equal(note.title, "Cálculo I");
    assert.equal(note.project, "ai-stem-tutor");
    assert.equal(note.module, "calculo-i");
    assert.equal(note.node, "Cálculo I");
    assert.equal(note.blocks.length, 1);
    assert.equal(note.blocks[0].origin, "human");
  });

  it("should accept tags and session", () => {
    const note = createNote({
      tags: ["ufrj", "engenharia"],
      session: "ses_123",
    });
    assert.deepEqual(note.tags, ["ufrj", "engenharia"]);
    assert.equal(note.session, "ses_123");
  });
});

describe("BLOCK_ORIGIN_LABELS", () => {
  it("should have all three origins", () => {
    assert.ok(BLOCK_ORIGIN_LABELS.human);
    assert.ok(BLOCK_ORIGIN_LABELS.opencode);
    assert.ok(BLOCK_ORIGIN_LABELS.tutor);
  });

  it("should have unique icons per origin", () => {
    const icons = Object.values(BLOCK_ORIGIN_LABELS).map((l) => l.icon);
    assert.equal(new Set(icons).size, 3);
  });

  it("should have distinct colors per origin", () => {
    const colors = Object.values(BLOCK_ORIGIN_LABELS).map((l) => l.color);
    assert.equal(new Set(colors).size, 3);
  });
});
