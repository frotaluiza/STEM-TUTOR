"use client";

import { useEffect, useRef, useCallback, useState, useMemo } from "react";
import cytoscape, {
  type Core,
  type ElementDefinition,
  type Stylesheet,
} from "cytoscape";
import { useTranslation } from "react-i18next";
import { Loader2 } from "lucide-react";
import type {
  MasteryMapResult,
  MapModule,
  MapKnowledgePoint,
} from "@/lib/learning-api";

interface ConceptGraphProps {
  result: MasteryMapResult;
  onNodeClick?: (kpId: string) => void;
}

type NodeType = "module-group" | "kp-new" | "kp-learning" | "kp-mastered";

const COLOR = {
  moduleBg: "var(--primary)",
  moduleText: "var(--primary-foreground)",
  mastered: "#22c55e",
  learning: "#eab308",
  new: "#6b7280",
  border: "var(--border)",
  bg: "var(--background)",
};

function nodeType(status: MapKnowledgePoint["status"]): NodeType {
  return `kp-${status}` as NodeType;
}

function nodeColor(status: MapKnowledgePoint["status"]): string {
  if (status === "mastered") return COLOR.mastered;
  if (status === "learning") return COLOR.learning;
  return COLOR.new;
}

export default function ConceptGraph({ result, onNodeClick }: ConceptGraphProps) {
  const { t } = useTranslation();
  const containerRef = useRef<HTMLDivElement | null>(null);
  const cyRef = useRef<Core | null>(null);
  const [ready, setReady] = useState(false);

  const elements = useMemo((): ElementDefinition[] => {
    const els: ElementDefinition[] = [];
    const modules = result.map.modules;
    let yOffset = 0;

    for (const mod of modules) {
      const groupId = `module-${mod.id}`;
      els.push({
        data: {
          id: groupId,
          label: mod.name,
          type: "module-group",
        },
        position: { x: 0, y: yOffset },
        classes: "module-group",
      });

      mod.knowledge_points.forEach((kp, i) => {
        const kpId = `kp-${kp.id}`;
        const cols = Math.ceil(Math.sqrt(mod.knowledge_points.length));
        const row = Math.floor(i / cols);
        const col = i % cols;
        const px = (col - cols / 2) * 140;
        const py = row * 70 + 60;

        els.push({
          data: {
            id: kpId,
            label: kp.name,
            parent: groupId,
            type: nodeType(kp.status),
            mastery: kp.mastery,
            originalId: kp.id,
          },
          position: { x: px, y: py },
          classes: nodeType(kp.status),
        });

        els.push({
          data: {
            id: `edge-${kp.id}`,
            source: groupId,
            target: kpId,
          },
          classes: "kp-edge",
        });
      });

      yOffset += 160 + Math.ceil(mod.knowledge_points.length / 4) * 80;
    }

    return els;
  }, [result]);

  useEffect(() => {
    if (!containerRef.current || elements.length === 0) return;

    const cy = cytoscape({
      container: containerRef.current,
      elements,
      style: [
        {
          selector: "node[type='module-group']",
          style: {
            "background-color": COLOR.moduleBg,
            color: COLOR.moduleText,
            "text-valign": "top",
            "text-halign": "center",
            "text-wrap": "wrap",
            "font-size": "13px",
            "font-weight": 600,
            "padding": "12px",
            "border-width": 1,
            "border-color": COLOR.border,
            "border-opacity": 0.3,
            "shape": "round-rectangle",
            width: "label",
            height: "label",
            "min-width": "180px",
          },
        },
        {
          selector: "node[type='kp-mastered']",
          style: {
            "background-color": COLOR.mastered,
            color: "#fff",
            width: 36,
            height: 36,
            "text-valign": "center",
            "text-halign": "center",
            "font-size": "8px",
            "text-wrap": "wrap",
            "border-width": 0,
            shape: "ellipse",
          },
        },
        {
          selector: "node[type='kp-learning']",
          style: {
            "background-color": COLOR.learning,
            color: "#000",
            width: 36,
            height: 36,
            "text-valign": "center",
            "text-halign": "center",
            "font-size": "8px",
            "text-wrap": "wrap",
            "border-width": 2,
            "border-color": "#a16207",
            shape: "ellipse",
          },
        },
        {
          selector: "node[type='kp-new']",
          style: {
            "background-color": COLOR.new,
            color: "#fff",
            width: 36,
            height: 36,
            "text-valign": "center",
            "text-halign": "center",
            "font-size": "8px",
            "text-wrap": "wrap",
            "border-width": 1,
            "border-color": "#9ca3af",
            "border-opacity": 0.5,
            shape: "ellipse",
          },
        },
        {
          selector: "edge.kp-edge",
          style: {
            width: 1,
            "line-color": COLOR.border,
            "line-opacity": 0.25,
            "target-arrow-shape": "none",
            "curve-style": "haystack",
          },
        },
      ],
      layout: { name: "preset" },
      wheelSensitivity: 0.3,
      minZoom: 0.3,
      maxZoom: 3,
      userPanningEnabled: true,
      userZoomingEnabled: true,
    });

    cy.on("tap", "node[kpId]", (evt) => {
      const id = evt.target.data("kpId");
      onNodeClick?.(id);
    });

    cy.on("tap", (evt) => {
      if (evt.target === cy) {
        // background tap — could deselect
      }
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
  }, [elements, onNodeClick]);

  const fitToScreen = useCallback(() => {
    cyRef.current?.fit(undefined, 40);
  }, []);

  useEffect(() => {
    if (ready) fitToScreen();
  }, [ready, fitToScreen]);

  return (
    <div className="relative h-full min-h-[300px]">
      <div ref={containerRef} className="absolute inset-0" />

      {!ready && (
        <div className="absolute inset-0 flex items-center justify-center text-[var(--muted-foreground)]">
          <Loader2 className="w-5 h-5 animate-spin" />
        </div>
      )}

      <div className="absolute bottom-3 left-3 flex items-center gap-3 text-[11px] text-[var(--muted-foreground)]">
        <span className="inline-flex items-center gap-1">
          <span
            className="inline-block w-2.5 h-2.5 rounded-full"
            style={{ background: COLOR.mastered }}
          />
          {t("Mastered")}
        </span>
        <span className="inline-flex items-center gap-1">
          <span
            className="inline-block w-2.5 h-2.5 rounded-full"
            style={{ background: COLOR.learning }}
          />
          {t("In progress")}
        </span>
        <span className="inline-flex items-center gap-1">
          <span
            className="inline-block w-2.5 h-2.5 rounded-full"
            style={{ background: COLOR.new }}
          />
          {t("Not started")}
        </span>
      </div>
    </div>
  );
}
