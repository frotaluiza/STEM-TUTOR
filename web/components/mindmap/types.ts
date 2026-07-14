import type { Node, Edge } from "@xyflow/react";

export type MindMapNodeType =
  | "project"
  | "branch"
  | "commit"
  | "session"
  | "decision"
  | "todo"
  | "module"
  | "kp";

export interface MindMapNodeData extends Record<string, unknown> {
  label: string;
  subtitle?: string;
  color?: string;
  status?: string;
  mastery?: number;
  type: MindMapNodeType;
}

export type MindMapNode = Node<MindMapNodeData, MindMapNodeType>;
export type MindMapEdge = Edge;

export interface MindMapMeta {
  project: string;
  branch: string;
  last_commit: string;
  last_updated: string;
  path_id: string;
}

export interface MindMapResponse {
  nodes: MindMapNode[];
  edges: MindMapEdge[];
  meta: MindMapMeta;
}

export const NODE_COLORS: Record<string, string> = {
  project: "#6366f1",
  branch: "#8b5cf6",
  commit: "#22c55e",
  session: "#3b82f6",
  decision: "#f59e0b",
  todo: "#ef4444",
  module: "#a855f7",
  kp: "#6b7280",
};

export const NODE_LABELS: Record<string, string> = {
  project: "Project",
  branch: "Branch",
  commit: "Commit",
  session: "Session",
  decision: "Decision",
  todo: "Next Step",
  module: "Module",
  kp: "Knowledge Point",
};
