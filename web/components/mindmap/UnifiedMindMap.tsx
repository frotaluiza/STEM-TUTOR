"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState,
  addEdge,
  type Connection,
  type Edge,
  type Node,
  useReactFlow,
  ReactFlowProvider,
  Panel,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import dagre from "@dagrejs/dagre";
import { Loader2, AlertCircle, Plus, Save, LayoutGrid } from "lucide-react";
import BaseNode from "./nodes/BaseNode";
import ProjectNode from "./nodes/ProjectNode";
import SessionNode from "./nodes/SessionNode";
import type { MindMapNode, MindMapEdge, MindMapResponse, MindMapMeta, MindMapNodeType, MindMapNodeData } from "./types";
import { NODE_COLORS } from "./types";

function layoutNodes(nodes: Node[], edges: Edge[], direction: "LR" | "TB" = "LR"): Node[] {
  const g = new dagre.graphlib.Graph();
  g.setDefaultEdgeLabel(() => ({}));
  g.setGraph({ rankdir: direction, nodesep: 60, ranksep: 100, marginx: 40, marginy: 40 });

  nodes.forEach((n) => {
    const w = n.type === "project" ? 160 : n.type === "session" ? 140 : 120;
    const h = 60;
    g.setNode(n.id, { width: w, height: h });
  });
  edges.forEach((e) => g.setEdge(e.source, e.target));

  dagre.layout(g);

  return nodes.map((n) => {
    const pos = g.node(n.id);
    return { ...n, position: { x: pos.x - (pos.width || 120) / 2, y: pos.y - (pos.height || 60) / 2 } };
  });
}

interface UnifiedMindMapProps {
  pathId?: string;
  slug?: string;
  branch?: string;
  apiBase?: string;
  initialData?: MindMapResponse | null;
  onSave?: (data: MindMapResponse) => void;
  readOnly?: boolean;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const nodeTypes: Record<string, any> = {
  project: ProjectNode,
  branch: BaseNode,
  commit: BaseNode,
  session: SessionNode,
  decision: BaseNode,
  todo: BaseNode,
  module: BaseNode,
  kp: BaseNode,
  kb: BaseNode,
  note: BaseNode,
  issue: BaseNode,
};

function Flow({ pathId = "default", slug, branch, apiBase = "/api/v1/mindmap", initialData, onSave, readOnly = false }: UnifiedMindMapProps) {
  const [nodes, setNodes, onNodesChange] = useNodesState<Node>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<Edge>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [meta, setMeta] = useState<MindMapMeta | null>(null);
  const rfRef = useRef<ReturnType<typeof useReactFlow> | null>(null);
  rfRef.current = useReactFlow();
  const fitViewRef = useRef<() => void>(() => {});

  const doFitView = useCallback(() => {
    if (rfRef.current) {
      rfRef.current.fitView({ padding: 0.2, duration: 300 });
    }
  }, []);
  fitViewRef.current = doFitView;

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);

    const url = slug
      ? `/api/v1/pm/space/${encodeURIComponent(slug)}${branch ? `?branch=${encodeURIComponent(branch)}` : ""}`
      : pathId
        ? `${apiBase}/${encodeURIComponent(pathId)}`
        : null;
    if (!url && !initialData) {
      setError("No pathId, slug, or initialData provided");
      setLoading(false);
      return;
    }

    const dataPromise: Promise<MindMapResponse> = initialData
      ? Promise.resolve(initialData)
      : fetch(url!).then((r) => {
          if (!r.ok) throw new Error(`HTTP ${r.status}`);
          return r.json();
        });

    dataPromise
      .then((data) => {
        if (cancelled) return;
        const rfNodes: Node[] = data.nodes.map((n, i) => ({
          id: n.id,
          type: n.type as string,
          position: { x: 0, y: i * 80 },
          data: n as unknown as Record<string, unknown>,
        }));
        const rfEdges: Edge[] = data.edges.map((e) => ({
          id: e.id,
          source: e.source,
          target: e.target,
          label: e.label,
          style: { stroke: "#4b5563", strokeOpacity: 0.4 },
        }));
        const laidOut = layoutNodes(rfNodes, rfEdges, "LR");
        setNodes(laidOut);
        setEdges(rfEdges);
        setMeta(data.meta);
        setLoading(false);

        setTimeout(() => fitViewRef.current(), 150);
      })
      .catch((e) => {
        if (!cancelled) {
          setError(e.message);
          setLoading(false);
        }
      });

    return () => { cancelled = true; };
  }, [pathId, slug, branch, apiBase, initialData, setNodes, setEdges]);

  const onConnect = useCallback(
    (params: Connection) => {
      if (readOnly) return;
      setEdges((eds) => addEdge({ ...params, style: { stroke: "#4b5563", strokeOpacity: 0.4 } }, eds));
    },
    [setEdges, readOnly],
  );

  const handleLayout = useCallback(() => {
    fitViewRef.current();
  }, []);

  const handleAddNode = useCallback(() => {
    if (readOnly) return;
    const id = `node-${Date.now()}`;
    const rf = rfRef.current;
    const center = rf ? rf.screenToFlowPosition({ x: window.innerWidth / 2, y: window.innerHeight / 2 }) : { x: 0, y: 0 };
    const newNode: Node = {
      id,
      type: "kp",
      position: center,
      data: { label: "New Node", type: "kp", color: NODE_COLORS.kp },
    };
    setNodes((nds) => [...nds, newNode]);
  }, [readOnly, setNodes]);

  const handleSave = useCallback(() => {
    if (!onSave) return;
    const currentNodes = nodes.map((n) => ({
      id: n.id,
      type: (n.data as Record<string, unknown>)?.type as string || "generic",
      label: (n.data as Record<string, unknown>)?.label as string || "",
      subtitle: (n.data as Record<string, unknown>)?.subtitle as string || "",
      color: (n.data as Record<string, unknown>)?.color as string || "#6b7280",
      status: (n.data as Record<string, unknown>)?.status as string || "",
      mastery: (n.data as Record<string, unknown>)?.mastery as number || 0,
    }));
    const currentEdges = edges.map((e) => ({
      id: e.id,
      source: e.source,
      target: e.target,
      label: e.label || "",
    }));
    onSave({ nodes: currentNodes as unknown as MindMapNode[], edges: currentEdges as unknown as MindMapEdge[], meta: meta || { project: "", branch: "", last_commit: "", last_updated: "", path_id: pathId } });
  }, [nodes, edges, meta, pathId, onSave]);

  if (loading) {
    return (
      <div className="absolute inset-0 flex items-center justify-center">
        <Loader2 className="w-6 h-6 animate-spin text-[var(--muted-foreground)]" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="absolute inset-0 flex flex-col items-center justify-center gap-3 text-[var(--muted-foreground)]">
        <AlertCircle className="w-8 h-8 text-red-500" />
        <p className="text-sm">Failed to load mind map: {error}</p>
      </div>
    );
  }

  return (
    <div className="relative w-full h-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        fitView
        attributionPosition="bottom-left"
        minZoom={0.1}
        maxZoom={4}
        panOnDrag
        selectNodesOnDrag
        deleteKeyCode={readOnly ? null : "Delete"}
        multiSelectionKeyCode="Shift"
      >
        <Background color="#4b5563" gap={20} size={1} />
        <Controls position="bottom-right" style={{ zIndex: 60 }} />
        <MiniMap
          position="bottom-left"
          nodeStrokeColor="#4b5563"
          nodeColor={(n) => ((n.data as Record<string, unknown>)?.color as string) || "#6b7280"}
          maskColor="rgba(0,0,0,0.1)"
          style={{ borderRadius: 8, border: "1px solid var(--border)", zIndex: 60 }}
        />
        <Panel position="top-right" style={{ zIndex: 60 }}>
          {!readOnly && (
            <div className="flex items-center gap-1.5 bg-[var(--background)]/90 backdrop-blur-sm rounded-lg border border-[var(--border)] p-1 shadow-sm">
              <button
                onClick={handleAddNode}
                className="inline-flex h-8 w-8 items-center justify-center rounded-md text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)] transition-colors"
                title="Add node"
              >
                <Plus size={15} />
              </button>
              <button
                onClick={handleLayout}
                className="inline-flex h-8 w-8 items-center justify-center rounded-md text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)] transition-colors"
                title="Auto-fit"
              >
                <LayoutGrid size={14} />
              </button>
              <div className="w-px h-5 bg-[var(--border)]" />
              <button
                onClick={handleSave}
                className="inline-flex h-8 items-center gap-1 rounded-md text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)] px-2 text-xs font-medium transition-colors"
                title="Save mind map"
              >
                <Save size={13} />
                Save
              </button>
            </div>
          )}
        </Panel>
        <Panel position="top-left" style={{ zIndex: 60 }}>
          {meta && (
            <div className="text-[11px] text-[var(--muted-foreground)] opacity-60 bg-[var(--background)]/70 backdrop-blur-sm rounded-lg px-2.5 py-1.5 border border-[var(--border)]/50">
              {meta.project} · {meta.branch}
              <br />
              {nodes.length} nodes · {edges.length} edges
            </div>
          )}
        </Panel>
      </ReactFlow>
    </div>
  );
}

export default function UnifiedMindMap(props: UnifiedMindMapProps) {
  return (
    <ReactFlowProvider>
      <Flow {...props} />
    </ReactFlowProvider>
  );
}
