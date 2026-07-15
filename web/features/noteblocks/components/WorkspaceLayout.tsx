"use client";

import dynamic from "next/dynamic";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import {
  BookOpen, FileText, GraduationCap, GripVertical, Library,
  Loader2, MessageSquare, PanelRightClose, Terminal, X,
} from "lucide-react";
import { NoteEditor } from "./Editor/NoteEditor";
import { TutorChatSidebar } from "./TutorChatSidebar";
import { ArtefactViewer } from "./ArtefactViewer";
import { MaterialViewer } from "./MaterialViewer";
import { TerminalPane } from "./Terminal/TerminalPane";
import type { Note } from "../types";

const MarkdownRenderer = dynamic(() => import("@/components/common/MarkdownRenderer"), { ssr: false });

// ── Types ──────────────────────────────────────────────────────────────────

type ViewTab = "note" | "chat" | "artefact" | "material" | "terminal" | "live-doc";

interface TabDef {
  id: ViewTab;
  label: string;
  icon: typeof FileText;
}

interface PanelState {
  id: string;
  tabId: ViewTab;
}

interface LayoutState {
  /** Panels currently open (ordered). */
  panels: PanelState[];
  /** Number of columns to split panels into. */
  columns: number;
}

const STORAGE_KEY = "dt:noteblocks:layout";

const ALL_TABS: TabDef[] = [
  { id: "note", label: "Nota", icon: FileText },
  { id: "material", label: "Material", icon: Library },
  { id: "chat", label: "Tutor", icon: GraduationCap },
  { id: "artefact", label: "Artefatos", icon: BookOpen },
  { id: "live-doc", label: "Live Doc", icon: MessageSquare },
  { id: "terminal", label: "Terminal", icon: Terminal },
];

const TAB_RENDERERS: Record<ViewTab, string> = {
  note: "note",
  material: "material",
  chat: "chat",
  artefact: "artefact",
  "live-doc": "live-doc",
  terminal: "terminal",
};

function defaultLayout(sessionMode: boolean, hasSession: boolean): LayoutState {
  const panels: PanelState[] = [];
  if (sessionMode) {
    panels.push({ id: "p-material", tabId: "material" });
    panels.push({ id: "p-chat", tabId: "chat" });
  } else {
    panels.push({ id: "p-note", tabId: "note" });
  }
  return { panels, columns: 2 };
}

function loadLayout(key: string, fallback: LayoutState): LayoutState {
  if (typeof window === "undefined") return fallback;
  try {
    const raw = window.localStorage.getItem(`${STORAGE_KEY}:${key}`);
    if (raw) return JSON.parse(raw) as LayoutState;
  } catch {}
  return fallback;
}

function saveLayout(key: string, layout: LayoutState) {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.setItem(`${STORAGE_KEY}:${key}`, JSON.stringify(layout));
  } catch {}
}

// ── Panel Content ───────────────────────────────────────────────────────────

interface PanelContentProps {
  tabId: ViewTab;
  noteId?: string;
  pathId?: string;
  sessionSlug?: string;
}

function PanelContent({ tabId, noteId, pathId, sessionSlug }: PanelContentProps) {
  switch (tabId) {
    case "note":
      return <NoteEditor noteId={noteId} />;
    case "material":
      return <MaterialViewer pathId={pathId} />;
    case "chat":
      return <TutorChatSidebar pathId={pathId} />;
    case "artefact":
      return <ArtefactViewer sourceId={pathId} />;
    case "live-doc":
      return <LiveDocPanel sessionSlug={sessionSlug} />;
    case "terminal":
      return <TerminalPane />;
    default:
      return <div className="flex items-center justify-center h-full text-gray-600 text-xs">Conteudo indisponivel</div>;
  }
}

function LiveDocPanel({ sessionSlug }: { sessionSlug?: string }) {
  if (!sessionSlug) return null;
  const [content, setContent] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetch(`/api/v1/pm/sessions/${sessionSlug}/live-doc`)
      .then((r) => r.ok ? r.text() : null)
      .then((text) => { if (!cancelled && text) { setContent(text); setLoading(false); } })
      .catch((e) => { if (!cancelled) { setError(e.message); setLoading(false); } });
    return () => { cancelled = true; };
  }, [sessionSlug]);

  if (loading) return <div className="flex items-center justify-center h-full text-gray-600"><Loader2 className="w-4 h-4 animate-spin" /></div>;
  if (error) return <div className="flex items-center justify-center h-full text-red-400 text-xs">{error}</div>;
  return (
    <div className="h-full flex flex-col">
      <div className="flex-1 overflow-y-auto px-4 py-3">
        <MarkdownRenderer content={content || ""} variant="prose" />
      </div>
    </div>
  );
}

// ── Main Component ──────────────────────────────────────────────────────────

export interface WorkspaceLayoutProps {
  sessionMode: boolean;
  hasSession: boolean;
  noteId?: string;
  pathId?: string;
  sessionSlug?: string;
}

export function WorkspaceLayout({ sessionMode, hasSession, noteId, pathId, sessionSlug }: WorkspaceLayoutProps) {
  const layoutKey = pathId || "default";
  const [layout, setLayout] = useState<LayoutState>(() => defaultLayout(sessionMode, hasSession));
  const [ready, setReady] = useState(false);
  const [dndTabId, setDndTabId] = useState<ViewTab | null>(null);
  const dropRef = useRef<HTMLDivElement | null>(null);

  // Load persisted layout on mount
  useEffect(() => {
    const saved = loadLayout(layoutKey, defaultLayout(sessionMode, hasSession));
    setLayout(saved);
    setReady(true);
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  // Persist on change
  useEffect(() => {
    if (ready) saveLayout(layoutKey, layout);
  }, [layout, layoutKey, ready]);

  // Available tabs (filter by context)
  const availableTabs = useMemo(() => {
    return ALL_TABS.filter((t) => {
      if (t.id === "live-doc") return hasSession;
      if (["material", "chat", "artefact"].includes(t.id)) return sessionMode || !!pathId;
      return true;
    });
  }, [hasSession, sessionMode, pathId]);

  // Tabs currently in panels
  const panelTabIds = useMemo(() => new Set(layout.panels.map((p) => p.tabId)), [layout.panels]);

  const availableAsBar = useMemo(
    () => availableTabs.filter((t) => !panelTabIds.has(t.id)),
    [availableTabs, panelTabIds],
  );

  const togglePanel = useCallback(
    (tabId: ViewTab) => {
      setLayout((prev) => {
        const exists = prev.panels.find((p) => p.tabId === tabId);
        if (exists) {
          return { ...prev, panels: prev.panels.filter((p) => p.id !== exists.id) };
        }
        return {
          ...prev,
          panels: [...prev.panels, { id: `p-${tabId}-${Date.now()}`, tabId }],
        };
      });
    },
    [],
  );

  const closePanel = useCallback((panelId: string) => {
    setLayout((prev) => ({
      ...prev,
      panels: prev.panels.filter((p) => p.id !== panelId),
    }));
  }, []);

  const swapColumns = useCallback(() => {
    setLayout((prev) => {
      const max = Math.min(prev.panels.length, 4);
      const next = prev.columns >= max ? 1 : prev.columns + 1;
      return { ...prev, columns: next };
    });
  }, []);

  // ── Drag and drop: tab bar -> panel area ──

  const handleTabDragStart = useCallback(
    (e: React.DragEvent, tabId: ViewTab) => {
      e.dataTransfer.setData("text/plain", tabId);
      e.dataTransfer.effectAllowed = "copy";
      setDndTabId(tabId);
    },
    [],
  );

  const handlePanelDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      const tabId = e.dataTransfer.getData("text/plain") as ViewTab;
      if (tabId) togglePanel(tabId);
      setDndTabId(null);
    },
    [togglePanel],
  );

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = "copy";
  }, []);

  const handleDragEnd = useCallback(() => setDndTabId(null), []);

  // ── Render ──

  const cols = Math.min(layout.columns, Math.max(layout.panels.length, 1));
  const gridRef = useRef<HTMLDivElement | null>(null);
  const [colFractions, setColFractions] = useState<number[]>([]);
  const draggingRef = useRef<{ index: number; startX: number; starts: number[] } | null>(null);

  // Init col fractions when panels change
  useEffect(() => {
    if (layout.panels.length === 0) { setColFractions([]); return; }
    const n = Math.min(layout.panels.length, cols);
    setColFractions(new Array(n).fill(100 / n));
  }, [layout.panels.length, cols]);

  const handleResizeStart = useCallback(
    (e: React.MouseEvent | React.TouchEvent, index: number) => {
      e.preventDefault();
      const grid = gridRef.current;
      if (!grid) return;
      const rect = grid.getBoundingClientRect();
      const clientX = "touches" in e ? e.touches[0].clientX : e.clientX;
      draggingRef.current = { index, startX: clientX, starts: [...colFractions] };

      const onMove = (ev: MouseEvent | TouchEvent) => {
        const dr = draggingRef.current;
        if (!dr) return;
        const cx = "touches" in ev ? (ev as TouchEvent).touches[0].clientX : (ev as MouseEvent).clientX;
        const delta = ((cx - dr.startX) / rect.width) * 100;
        const newFractions = [...dr.starts];
        const left = Math.max(10, dr.starts[dr.index] + delta);
        const right = Math.max(10, dr.starts[dr.index + 1] - delta);
        const total = left + right;
        newFractions[dr.index] = (left / total) * 100;
        newFractions[dr.index + 1] = (right / total) * 100;
        setColFractions(newFractions);
      };

      const onUp = () => {
        draggingRef.current = null;
        document.removeEventListener("mousemove", onMove);
        document.removeEventListener("mouseup", onUp);
        document.removeEventListener("touchmove", onMove);
        document.removeEventListener("touchend", onUp);
      };

      document.addEventListener("mousemove", onMove);
      document.addEventListener("mouseup", onUp);
      document.addEventListener("touchmove", onMove);
      document.addEventListener("touchend", onUp);
    },
    [colFractions],
  );

  const fracSum = colFractions.reduce((a, b) => a + b, 0) || 100;

  return (
    <div className="flex flex-col h-full w-full bg-[#0a0a0a] text-gray-100">
      {/* Tab bar */}
      <div
        className="flex shrink-0 items-center gap-0.5 border-b border-[#1a1a1a] bg-[#0d0d0d] px-3 pt-1.5 overflow-x-auto"
        onDragOver={handleDragOver}
        onDrop={handlePanelDrop}
      >
        {availableAsBar.map((t) => (
          <button
            key={t.id}
            type="button"
            draggable
            onDragStart={(e) => handleTabDragStart(e, t.id)}
            onClick={() => togglePanel(t.id)}
            className={`flex items-center gap-1.5 px-2.5 py-1.5 text-[11.5px] font-medium rounded-t-md transition-colors cursor-grab active:cursor-grabbing ${
              panelTabIds.has(t.id)
                ? "bg-[#0a0a0a] text-gray-100 border border-[#1a1a1a] border-b-transparent"
                : "text-gray-500 hover:text-gray-300 hover:bg-[#151515]"
            }`}
          >
            <t.icon size={12} strokeWidth={1.8} />
            {t.label}
          </button>
        ))}

        <div className="flex-1" />

        {layout.panels.length > 1 && (
          <button
            type="button"
            onClick={swapColumns}
            className="mr-1 p-1 rounded text-gray-600 hover:text-gray-300 hover:bg-[#151515] transition-colors"
            title="Alterar numero de colunas"
          >
            <PanelRightClose className="w-3.5 h-3.5" />
          </button>
        )}

        {hasSession && sessionSlug && (
          <a
            href={`/session-viewer/${sessionSlug}`}
            className="flex items-center gap-1 px-2 py-1 text-[11px] text-cyan-400/70 hover:text-cyan-300 rounded border border-[#1a1a1a] hover:bg-[#151515] transition-colors"
          >
            <MessageSquare size={11} strokeWidth={1.8} />
            {sessionSlug}
          </a>
        )}
      </div>

      {/* Panel area */}
      <div
        ref={dropRef}
        className="flex-1 min-h-0"
        onDragOver={handleDragOver}
        onDrop={handlePanelDrop}
      >
        {layout.panels.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full text-center px-6">
            <GripVertical className="w-8 h-8 text-gray-700 mb-3" />
            <p className="text-sm text-gray-500">Arraste abas para criar paineis</p>
            <p className="text-xs text-gray-700 mt-1">
              Clique em uma aba acima para adiciona-la como painel
            </p>
          </div>
        ) : (
          <div
            ref={gridRef}
            className="h-full relative select-none"
            style={{
              display: "grid",
              gridTemplateColumns: colFractions.map((f) => `${(f / fracSum) * 100}%`).join(" "),
              gridAutoRows: "100%",
            }}
          >
            {layout.panels.map((panel, i) => {
              const tab = ALL_TABS.find((t) => t.id === panel.tabId);
              if (!tab) return null;
              return (
                <div key={panel.id} className="flex flex-col min-w-0 relative">
                  <Panel
                    tab={tab}
                    onClose={() => closePanel(panel.id)}
                    onDragOver={handleDragOver}
                    onDrop={handlePanelDrop}
                  >
                    <PanelContent
                      tabId={panel.tabId}
                      noteId={noteId}
                      pathId={pathId}
                      sessionSlug={sessionSlug}
                    />
                  </Panel>
                  {/* Resize handle between panels */}
                  {i < layout.panels.length - 1 && (
                    <div
                      className="absolute top-0 right-0 w-1.5 h-full cursor-col-resize z-10 group"
                      onMouseDown={(e) => handleResizeStart(e, i)}
                      onTouchStart={(e) => handleResizeStart(e, i)}
                    >
                      <div className="w-0.5 h-full mx-auto bg-[#1a1a1a] group-hover:bg-emerald-500/50 group-active:bg-emerald-400 transition-colors" />
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}

// ── Panel Component ─────────────────────────────────────────────────────────



function Panel({
  tab,
  children,
  onClose,
  onDragOver,
  onDrop,
}: {
  tab: TabDef;
  children: React.ReactNode;
  onClose: () => void;
  onDragOver: (e: React.DragEvent) => void;
  onDrop: (e: React.DragEvent) => void;
}) {
  const ICON = tab.icon;

  return (
    <div
      className="flex flex-col min-w-0 h-full"
      onDragOver={onDragOver}
      onDrop={onDrop}
    >
      {/* Panel header */}
      <div className="flex shrink-0 items-center gap-1.5 px-3 py-1.5 border-b border-[#1a1a1a] bg-[#0d0d0d]">
        <GripVertical className="w-3 h-3 text-gray-700 cursor-grab" />
        <ICON size={12} strokeWidth={1.8} className="text-gray-400" />
        <span className="text-[11px] font-medium text-gray-400 truncate">{tab.label}</span>
        <div className="flex-1" />
        <button
          type="button"
          onClick={onClose}
          className="p-0.5 rounded text-gray-700 hover:text-gray-300 hover:bg-[#1a1a1a] transition-colors"
        >
          <X className="w-3 h-3" />
        </button>
      </div>

      {/* Panel body */}
      <div className="flex-1 min-h-0 overflow-hidden">
        {children}
      </div>
    </div>
  );
}
