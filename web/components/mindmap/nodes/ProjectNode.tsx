import { memo } from "react";
import { Handle, Position, type NodeProps } from "@xyflow/react";
import type { MindMapNodeData } from "../types";

function ProjectNode({ data, selected }: NodeProps) {
  const d = data as unknown as MindMapNodeData;
  return (
    <div
      className={`relative rounded-2xl border-2 px-5 py-3 text-center transition-shadow ${
        selected ? "shadow-lg ring-2 ring-indigo-400/40" : "shadow-md"
      }`}
      style={{ borderColor: "#6366f1", background: "linear-gradient(135deg, #6366f111, #4f46e522)" }}
    >
      <Handle type="target" position={Position.Top} className="!border-[var(--border)]" />
      <span className="text-sm font-bold text-indigo-600 leading-tight">{String(d.label)}</span>
      {d.subtitle && (
        <p className="mt-0.5 text-[10px] text-[var(--muted-foreground)]">{String(d.subtitle)}</p>
      )}
      <Handle type="source" position={Position.Bottom} className="!border-[var(--border)]" />
    </div>
  );
}

export default memo(ProjectNode);
