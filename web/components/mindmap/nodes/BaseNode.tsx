import { memo } from "react";
import { Handle, Position, type NodeProps } from "@xyflow/react";
import type { MindMapNodeData } from "../types";
import { NODE_COLORS, NODE_LABELS } from "../types";

interface BaseNodeProps extends NodeProps {
  data: MindMapNodeData;
}

function BaseNode({ data, selected }: BaseNodeProps) {
  const color = (data.color as string) || NODE_COLORS[data.type as string] || "#6b7280";
  const label = (data.label as string) || NODE_LABELS[data.type as string] || (data.type as string);

  return (
    <div
      className={`relative rounded-xl border-2 px-4 py-2.5 text-left transition-shadow ${
        selected ? "shadow-lg ring-2 ring-[var(--primary)]/40" : "shadow-sm"
      }`}
      style={{ borderColor: color, background: `${color}11` }}
    >
      <Handle type="target" position={Position.Top} className="!border-[var(--border)] !w-2 !h-2" />
      <div className="flex items-center gap-2">
        <span
          className="inline-block w-2.5 h-2.5 rounded-full shrink-0"
          style={{ background: color }}
        />
        <span className="text-xs font-semibold text-[var(--foreground)] leading-tight">{String(label)}</span>
      </div>
      {data.subtitle && (
        <p className="mt-0.5 text-[10px] text-[var(--muted-foreground)] leading-tight truncate max-w-40">
          {String(data.subtitle)}
        </p>
      )}
      {data.mastery !== undefined && Number(data.mastery) > 0 && (
        <div className="mt-1 h-1 w-full rounded-full bg-[var(--accent)] overflow-hidden">
          <div
            className="h-full rounded-full transition-all"
            style={{ width: `${Number(data.mastery) * 100}%`, background: color }}
          />
        </div>
      )}
      <Handle type="source" position={Position.Bottom} className="!border-[var(--border)] !w-2 !h-2" />
    </div>
  );
}

export default memo(BaseNode);
