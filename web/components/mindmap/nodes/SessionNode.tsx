import { memo } from "react";
import { Handle, Position, type NodeProps } from "@xyflow/react";
import type { MindMapNodeData } from "../types";

function SessionNode({ data, selected }: NodeProps) {
  const d = data as unknown as MindMapNodeData;
  return (
    <div
      className={`relative rounded-xl border-2 px-3 py-2 transition-shadow ${
        selected ? "shadow-lg ring-2 ring-blue-400/40" : "shadow-sm"
      }`}
      style={{ borderColor: "#3b82f6", background: "#3b82f611" }}
    >
      <Handle type="target" position={Position.Top} className="!border-[var(--border)] !w-2 !h-2" />
      <div className="flex items-center gap-1.5">
        <span className="text-lg">📝</span>
        <div className="min-w-0">
          <p className="text-xs font-medium text-[var(--foreground)] truncate max-w-36">{String(d.label)}</p>
          {d.subtitle && (
            <p className="text-[9px] text-[var(--muted-foreground)] truncate">{String(d.subtitle)}</p>
          )}
        </div>
      </div>
      <Handle type="source" position={Position.Bottom} className="!border-[var(--border)] !w-2 !h-2" />
    </div>
  );
}

export default memo(SessionNode);
