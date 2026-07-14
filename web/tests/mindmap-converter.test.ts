import test from "node:test";
import assert from "node:assert/strict";
import type { MasteryMapResult } from "../lib/learning-api";
import { masteryMapToMindMap } from "../components/mindmap/converters";

const SAMPLE_PATH_ID = "test-path-123";

const SAMPLE_RESULT: MasteryMapResult = {
  book_id: SAMPLE_PATH_ID,
  next: {
    action: "continue",
    knowledge_point_name: "Ohm's Law",
    knowledge_point_type: "concept",
    status: "new",
    mastery: 0,
    threshold: 0.8,
    reason: "next in module order",
  },
  map: {
    counts: { mastered: 1, learning: 1, new: 1, total: 3 },
    due_reviews: 0,
    complete: false,
    modules: [
      {
        id: "mod-1",
        name: "Module 1: DC Circuits",
        order: 1,
        mastered: 1,
        total: 2,
        knowledge_points: [
          { id: "kp-1", name: "Ohm's Law", type: "concept", status: "mastered", mastery: 0.95 },
          { id: "kp-2", name: "Kirchhoff's Law", type: "concept", status: "learning", mastery: 0.6 },
        ],
      },
      {
        id: "mod-2",
        name: "Module 2: AC Circuits",
        order: 2,
        mastered: 0,
        total: 1,
        knowledge_points: [
          { id: "kp-3", name: "AC Power", type: "formula", status: "new", mastery: 0 },
        ],
      },
    ],
  },
};

test("masteryMapToMindMap produces correct node and edge counts", () => {
  const result = masteryMapToMindMap(SAMPLE_RESULT, SAMPLE_PATH_ID);

  assert.ok(result.nodes, "should have nodes");
  assert.ok(result.edges, "should have edges");
  assert.ok(result.meta, "should have meta");

  // 1 root + 2 modules + 3 KPs = 6 nodes
  assert.equal(result.nodes.length, 6);
  // 2 module edges + 3 KP edges = 5 edges
  assert.equal(result.edges.length, 5);
});

test("masteryMapToMindMap creates a root node with type project", () => {
  const result = masteryMapToMindMap(SAMPLE_RESULT, SAMPLE_PATH_ID);
  const root = result.nodes.find((n) => n.id === `path-${SAMPLE_PATH_ID}`);
  assert.ok(root, "root node should exist");
  assert.equal(root.type, "project");
  assert.ok((root.data as Record<string, unknown>)?.label, "root should have a label");
});

test("masteryMapToMindMap creates module nodes with progress", () => {
  const result = masteryMapToMindMap(SAMPLE_RESULT, SAMPLE_PATH_ID);
  const mod1 = result.nodes.find((n) => n.id === "mod-mod-1");
  assert.ok(mod1, "module 1 node should exist");
  assert.equal(mod1.type, "module");

  const modData = mod1.data as Record<string, unknown>;
  assert.equal(modData.label, "Module 1: DC Circuits");
  assert.equal(modData.subtitle, "1/2");
  assert.equal(Number(modData.mastery), 0.5); // 1/2 = 0.5
});

test("masteryMapToMindMap colors KPs by status", () => {
  const result = masteryMapToMindMap(SAMPLE_RESULT, SAMPLE_PATH_ID);
  const masteredKp = result.nodes.find((n) => n.id === "kp-kp-1");
  const learningKp = result.nodes.find((n) => n.id === "kp-kp-2");
  const newKp = result.nodes.find((n) => n.id === "kp-kp-3");

  assert.ok(masteredKp);
  assert.ok(learningKp);
  assert.ok(newKp);

  assert.equal((masteredKp.data as Record<string, unknown>)?.color, "#22c55e");
  assert.equal((learningKp.data as Record<string, unknown>)?.color, "#eab308");
  assert.equal((newKp.data as Record<string, unknown>)?.color, "#6b7280");
});

test("masteryMapToMindMap links root -> module -> KP via edges", () => {
  const result = masteryMapToMindMap(SAMPLE_RESULT, SAMPLE_PATH_ID);
  const rootId = `path-${SAMPLE_PATH_ID}`;

  // Should have edges from root to each module
  const rootEdges = result.edges.filter((e) => e.source === rootId);
  assert.equal(rootEdges.length, SAMPLE_RESULT.map.modules.length);

  // Should have edges from mod-1 to its KPs
  const mod1Edges = result.edges.filter((e) => e.source === "mod-mod-1");
  assert.equal(mod1Edges.length, 2);

  // Should have edges from mod-2 to its KP
  const mod2Edges = result.edges.filter((e) => e.source === "mod-mod-2");
  assert.equal(mod2Edges.length, 1);
});

test("masteryMapToMindMap sets meta properties", () => {
  const result = masteryMapToMindMap(SAMPLE_RESULT, SAMPLE_PATH_ID);
  assert.equal(result.meta.project, "Mastery Path");
  assert.equal(result.meta.branch, SAMPLE_PATH_ID);
  assert.equal(result.meta.path_id, SAMPLE_PATH_ID);
});

test("masteryMapToMindMap assigns unique positions to all nodes", () => {
  const result = masteryMapToMindMap(SAMPLE_RESULT, SAMPLE_PATH_ID);
  const positions = result.nodes.map((n) => `${(n as any).position.x},${(n as any).position.y}`);
  const uniquePositions = new Set(positions);
  assert.equal(uniquePositions.size, result.nodes.length, "all nodes should have unique positions");
});

test("masteryMapToMindMap handles empty modules", () => {
  const empty: MasteryMapResult = {
    book_id: "empty",
    next: { action: "complete", knowledge_point_name: "", knowledge_point_type: "", status: "", mastery: 0, threshold: 0, reason: "" },
    map: { counts: { mastered: 0, learning: 0, new: 0, total: 0 }, due_reviews: 0, complete: true, modules: [] },
  };
  const result = masteryMapToMindMap(empty, "empty");
  assert.equal(result.nodes.length, 1); // just the root
  assert.equal(result.edges.length, 0);
});

test("masteryMapToMindMap marks complete paths", () => {
  const complete: MasteryMapResult = {
    book_id: "done",
    next: { action: "complete", knowledge_point_name: "", knowledge_point_type: "", status: "", mastery: 0, threshold: 0, reason: "" },
    map: { counts: { mastered: 5, learning: 0, new: 0, total: 5 }, due_reviews: 0, complete: true, modules: [] },
  };
  const result = masteryMapToMindMap(complete, "done");
  const root = result.nodes[0];
  assert.match(String((root.data as Record<string, unknown>)?.label), /All Mastered/);
});
