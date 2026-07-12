"use client";

import { useEffect, useRef, useCallback, useState } from "react";
import cytoscape, { type Core, type ElementDefinition, type Stylesheet } from "cytoscape";
import { Loader2, AlertCircle } from "lucide-react";

interface GraphNode {
  id: string;
  label: string;
  type: string;
  subtitle: string;
  color: string;
}

interface GraphEdge {
  source: string;
  target: string;
  label: string;
}

interface ProjectMindMapData {
  nodes: GraphNode[];
  edges: GraphEdge[];
  project: string;
  branch: string;
  last_commit: string;
  last_updated: string;
}

const NODE_COLORS: Record<string, string> = {
  project: "#6366f1",
  branch: "#8b5cf6",
  commit: "#22c55e",
  session: "#3b82f6",
  decision: "#f59e0b",
  todo: "#ef4444",
  issue: "#dc2626",
  file: "#10b981",
};

export default function ProjectMindMap() {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const cyRef = useRef<Core | null>(null);
  const [ready, setReady] = useState(false);
  const [data, setData] = useState<ProjectMindMapData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/v1/project/state")
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((d: ProjectMindMapData) => {
        setData(d);
        setLoading(false);
      })
      .catch((e) => {
        setError(e.message);
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    if (!containerRef.current || !data || data.nodes.length === 0) return;

    const elements: ElementDefinition[] = [
      ...data.nodes.map((n) => ({
        data: {
          id: n.id,
          label: n.label,
          type: n.type,
          subtitle: n.subtitle,
          color: n.color,
        },
      })),
      ...data.edges.map((e, i) => ({
        data: {
          id: `edge-${i}`,
          source: e.source,
          target: e.target,
          label: e.label,
        },
      })),
    ];

    const byType: Record<string, number> = {};
    for (const n of data.nodes) {
      byType[n.type] = (byType[n.type] || 0) + 1;
    }

    const style: Stylesheet[] = [
      {
        selector: "node",
        style: {
          "background-color": "#6366f1",
          color: "#fff",
          "text-valign": "center",
          "text-halign": "center",
          "text-wrap": "wrap",
          "font-size": "11px",
          "font-weight": 600,
          width: 80,
          height: 80,
          "border-width": 2,
          "border-color": "#fff",
          "border-opacity": 0.3,
          shape: "ellipse",
          "min-zoomed-font-size": 6,
        },
      },
      {
        selector: "node[type='project']",
        style: {
          width: 120,
          height: 120,
          "font-size": "15px",
          "background-color": "#6366f1",
          "border-width": 3,
          "border-color": "#818cf8",
        },
      },
      {
        selector: "node[type='branch']",
        style: {
          "background-color": "#8b5cf6",
          shape: "round-rectangle",
          width: "label",
          height: "label",
          padding: "10px",
          "min-width": "100px",
        },
      },
      {
        selector: "node[type='commit']",
        style: {
          "background-color": "#22c55e",
          width: 60,
          height: 60,
          "font-size": "8px",
        },
      },
      {
        selector: "node[type='session']",
        style: {
          "background-color": "#3b82f6",
          shape: "round-rectangle",
          width: "label",
          height: "label",
          padding: "8px",
          "min-width": "90px",
        },
      },
      {
        selector: "node[type='decision']",
        style: {
          "background-color": "#f59e0b",
          shape: "diamond",
          width: 50,
          height: 50,
          "font-size": "8px",
        },
      },
      {
        selector: "node[type='todo']",
        style: {
          "background-color": "#ef4444",
          shape: "triangle",
          width: 50,
          height: 50,
          "font-size": "8px",
        },
      },
      {
        selector: "node[type='issue']",
        style: {
          "background-color": "#dc2626",
          shape: "vee",
          width: 50,
          height: 50,
          "font-size": "8px",
        },
      },
      {
        selector: "node[type='file']",
        style: {
          "background-color": "#10b981",
          width: 40,
          height: 40,
          "font-size": "7px",
        },
      },
      {
        selector: "edge",
        style: {
          width: 1.5,
          "line-color": "#4b5563",
          "line-opacity": 0.4,
          "target-arrow-shape": "triangle",
          "target-arrow-color": "#4b5563",
          "arrow-scale": 0.7,
          "curve-style": "bezier",
          "label": "data(label)",
          "font-size": "8px",
          "color": "#6b7280",
          "text-rotation": "autorotate",
          "text-background-color": "#1f2937",
          "text-background-opacity": 0.6,
          "text-background-padding": "2px",
        },
      },
    ];

    const cy = cytoscape({
      container: containerRef.current,
      elements,
      style,
      layout: {
        name: "breadthfirst",
        directed: true,
        spacingFactor: 1.5,
        avoidOverlap: true,
        roots: ["project-root"],
      },
      wheelSensitivity: 0.3,
      minZoom: 0.2,
      maxZoom: 3,
      userPanningEnabled: true,
      userZoomingEnabled: true,
    });

    cyRef.current = cy;
    setReady(true);

    const resizeObserver = new ResizeObserver(() => cy.resize());
    resizeObserver.observe(containerRef.current);

    return () => {
      resizeObserver.disconnect();
      cy.destroy();
      cyRef.current = null;
      setReady(false);
    };
  }, [data]);

  const fitToScreen = useCallback(() => {
    cyRef.current?.fit(undefined, 50);
  }, []);

  useEffect(() => {
    if (ready) setTimeout(fitToScreen, 100);
  }, [ready, fitToScreen]);

  if (loading) {
    return (
      <div className="absolute inset-0 flex items-center justify-center text-[var(--muted-foreground)]">
        <Loader2 className="w-5 h-5 animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="absolute inset-0 flex flex-col items-center justify-center gap-3 text-[var(--muted-foreground)]">
        <AlertCircle className="w-8 h-8 text-red-500" />
        <p>Failed to load project state: {error}</p>
        <p className="text-xs opacity-60">
          Make sure a project-state JSON file exists and the backend is running.
        </p>
      </div>
    );
  }

  return (
    <div className="relative h-full min-h-[400px]">
      <div ref={containerRef} className="absolute inset-0" />

      {!ready && (
        <div className="absolute inset-0 flex items-center justify-center text-[var(--muted-foreground)]">
          <Loader2 className="w-5 h-5 animate-spin" />
        </div>
      )}

      <div className="absolute top-3 right-3 flex items-center gap-2">
        <button
          onClick={fitToScreen}
          className="px-3 py-1.5 text-xs rounded-md bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-colors"
        >
          Fit
        </button>
      </div>

      {data && (
        <div className="absolute bottom-3 left-3 flex flex-wrap items-center gap-x-4 gap-y-1 text-[11px] text-[var(--muted-foreground)]">
          {Object.entries(NODE_COLORS).map(([type, color]) => (
            <span key={type} className="inline-flex items-center gap-1">
              <span
                className="inline-block w-2.5 h-2.5 rounded-full"
                style={{ background: color }}
              />
              {type.charAt(0).toUpperCase() + type.slice(1)}
            </span>
          ))}
        </div>
      )}

      {data && (
        <div className="absolute top-3 left-3 text-[11px] text-[var(--muted-foreground)] opacity-60">
          {data.project} &middot; {data.branch}
          <br />
          {data.nodes.length} nodes &middot; {data.edges.length} edges
        </div>
      )}
    </div>
  );
}
