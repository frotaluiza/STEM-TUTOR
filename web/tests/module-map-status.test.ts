import test from "node:test";
import assert from "node:assert/strict";
import type {
  MasteryMapResult,
  MapModule,
  MapKnowledgePoint,
  ObjectiveStatus,
} from "../lib/learning-api";

function nodeColor(status: MapKnowledgePoint["status"]): string {
  if (status === "mastered") return "#22c55e";
  if (status === "learning") return "#eab308";
  return "#6b7280";
}

function computeProgress(kps: MapKnowledgePoint[]): {
  mastered: number;
  learning: number;
  new: number;
} {
  let mastered = 0;
  let learning = 0;
  let new_ = 0;
  for (const kp of kps) {
    if (kp.status === "mastered") mastered++;
    else if (kp.status === "learning") learning++;
    else new_++;
  }
  return { mastered, learning, new: new_ };
}

function moduleForKp(
  modules: MapModule[],
  kpName: string,
): MapModule | undefined {
  return modules.find((m) =>
    m.knowledge_points.some((kp) => kp.name === kpName),
  );
}

test("nodeColor returns correct hex for each status", () => {
  assert.equal(nodeColor("mastered"), "#22c55e");
  assert.equal(nodeColor("learning"), "#eab308");
  assert.equal(nodeColor("new"), "#6b7280");
});

test("computeProgress counts statuses correctly", () => {
  const kps: MapKnowledgePoint[] = [
    { id: "1", name: "A", type: "concept", status: "mastered", mastery: 1 },
    { id: "2", name: "B", type: "concept", status: "mastered", mastery: 0.94 },
    { id: "3", name: "C", type: "formula", status: "learning", mastery: 0.5 },
    { id: "4", name: "D", type: "theorem", status: "new", mastery: 0 },
  ];
  const p = computeProgress(kps);
  assert.equal(p.mastered, 2);
  assert.equal(p.learning, 1);
  assert.equal(p.new, 1);
});

test("computeProgress handles empty array", () => {
  const p = computeProgress([]);
  assert.equal(p.mastered, 0);
  assert.equal(p.learning, 0);
  assert.equal(p.new, 0);
});

test("computeProgress handles all same status", () => {
  const kps: MapKnowledgePoint[] = [
    { id: "1", name: "A", type: "x", status: "new", mastery: 0 },
    { id: "2", name: "B", type: "x", status: "new", mastery: 0 },
    { id: "3", name: "C", type: "x", status: "new", mastery: 0 },
  ];
  const p = computeProgress(kps);
  assert.equal(p.mastered, 0);
  assert.equal(p.learning, 0);
  assert.equal(p.new, 3);
});

test("moduleForKp finds the correct module for a given KP name", () => {
  const modules: MapModule[] = [
    {
      id: "m1",
      name: "Module 1",
      order: 1,
      mastered: 1,
      total: 2,
      knowledge_points: [
        { id: "kp1", name: "Ohm's Law", type: "concept", status: "mastered", mastery: 1 },
        { id: "kp2", name: "Kirchhoff's Law", type: "concept", status: "new", mastery: 0 },
      ],
    },
    {
      id: "m2",
      name: "Module 2",
      order: 2,
      mastered: 0,
      total: 1,
      knowledge_points: [
        { id: "kp3", name: "AC Power", type: "concept", status: "new", mastery: 0 },
      ],
    },
  ];

  const found = moduleForKp(modules, "Ohm's Law");
  assert.ok(found);
  assert.equal(found!.id, "m1");

  const found2 = moduleForKp(modules, "AC Power");
  assert.ok(found2);
  assert.equal(found2!.id, "m2");
});

test("moduleForKp returns undefined for non-existent KP", () => {
  const modules: MapModule[] = [
    {
      id: "m1",
      name: "M1",
      order: 1,
      mastered: 0,
      total: 1,
      knowledge_points: [
        { id: "kp1", name: "X", type: "t", status: "new", mastery: 0 },
      ],
    },
  ];
  const found = moduleForKp(modules, "NonExistent");
  assert.equal(found, undefined);
});
