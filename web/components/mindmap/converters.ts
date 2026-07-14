import type { MindMapNode, MindMapEdge, MindMapResponse } from "./types";
import type { MasteryMapResult } from "@/lib/learning-api";

export function masteryMapToMindMap(data: MasteryMapResult, pathId: string): MindMapResponse {
  const nodes: MindMapNode[] = [];
  const edges: MindMapEdge[] = [];
  let edgeId = 0;

  const X_SPACING = 220;
  const Y_SPACING = 80;
  const KP_X_SPACING = 140;
  const KP_Y_SPACING = 70;

  function eid() {
    edgeId++;
    return `e-${edgeId}`;
  }

  const rootId = `path-${pathId}`;
  nodes.push({
    id: rootId,
    type: "project",
    position: { x: (data.map.modules.length - 1) * X_SPACING / 2, y: 0 },
    data: {
      label: data.map.complete ? "All Mastered! 🎉" : "Mastery Path",
      subtitle: `${data.map.counts.mastered}/${data.map.counts.total} mastered · ${data.map.counts.learning} in progress`,
      color: "#6366f1",
      type: "project",
    },
  });

  data.map.modules.forEach((mod, mi) => {
    const modId = `mod-${mod.id}`;
    const cols = Math.max(1, Math.ceil(Math.sqrt(mod.knowledge_points.length)));

    nodes.push({
      id: modId,
      type: "module",
      position: { x: mi * X_SPACING, y: Y_SPACING },
      data: {
        label: mod.name,
        subtitle: `${mod.mastered}/${mod.total}`,
        color: "#a855f7",
        type: "module",
        mastery: mod.total > 0 ? mod.mastered / mod.total : 0,
      },
    });
    edges.push({
      id: eid(),
      source: rootId,
      target: modId,
    });

    mod.knowledge_points.forEach((kp, ki) => {
      const kpId = `kp-${kp.id}`;
      const row = Math.floor(ki / cols);
      const col = ki % cols;
      const statusColor =
        kp.status === "mastered" ? "#22c55e" : kp.status === "learning" ? "#eab308" : "#6b7280";
      nodes.push({
        id: kpId,
        type: "kp",
        position: { x: mi * X_SPACING + (col - (cols - 1) / 2) * KP_X_SPACING, y: Y_SPACING * 2 + row * KP_Y_SPACING },
        data: {
          label: kp.name,
          subtitle: `${kp.type} · ${Math.round(kp.mastery * 100)}%`,
          color: statusColor,
          status: kp.status,
          mastery: kp.mastery,
          type: "kp",
        },
      });
      edges.push({
        id: eid(),
        source: modId,
        target: kpId,
      });
    });
  });

  return {
    nodes,
    edges,
    meta: {
      project: "Mastery Path",
      branch: pathId,
      last_commit: "",
      last_updated: "",
      path_id: pathId,
    },
  };
}
