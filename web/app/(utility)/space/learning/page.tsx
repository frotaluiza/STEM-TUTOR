"use client";

import { useCallback, useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useTranslation } from "react-i18next";
import {
  GraduationCap,
  Loader2,
  RotateCcw,
  Trash2,
  MessageSquare,
  Network,
  List,
} from "lucide-react";

import {
  fetchAllProgress,
  fetchMasteryMap,
  deleteProgress,
  redoProgress,
  type ProgressSummary,
  type MasteryMapResult,
} from "@/lib/learning-api";
import ModuleMap from "@/components/learning/ModuleMap";
import ConceptGraph from "@/components/learning/ConceptGraph";

/**
 * Mastery Path dashboard — the persistent "screen" of the mastery experience.
 *
 * The tutoring itself runs on the chat agent loop (pick "Mastery Path" mode in
 * Chat); this page is the map of where the learner stands. It reads the
 * gate-accurate snapshot from ``/progress/{id}/map`` (per-type status computed
 * by ``deeptutor.learning.policy``) so the colours here agree with the gate the
 * tutor enforces. A path is keyed by its chat session, so "Continue" reopens
 * that session in mastery mode.
 */
export default function MasteryPathPage() {
  const { i18n } = useTranslation();
  const zh = i18n.language?.toLowerCase().startsWith("zh");
  const tr = useCallback((cn: string, en: string) => (zh ? cn : en), [zh]);
  const router = useRouter();

  const [paths, setPaths] = useState<ProgressSummary[]>([]);
  const [selected, setSelected] = useState<string | null>(null);
  const [detail, setDetail] = useState<MasteryMapResult | null>(null);
  const [loadingList, setLoadingList] = useState(true);
  const [loadingDetail, setLoadingDetail] = useState(false);
  const [viewMode, setViewMode] = useState<"list" | "graph">("list");

  const loadList = useCallback(async () => {
    setLoadingList(true);
    try {
      const result = await fetchAllProgress();
      const withContent = result.summaries
        .filter((s) => s.kp_count > 0)
        .sort((a, b) => b.updated_at - a.updated_at);
      setPaths(withContent);
      setSelected((prev) => prev ?? withContent[0]?.book_id ?? null);
    } catch {
      setPaths([]);
    } finally {
      setLoadingList(false);
    }
  }, []);

  useEffect(() => {
    loadList();
  }, [loadList]);

  useEffect(() => {
    if (!selected) {
      setDetail(null);
      return;
    }
    let cancelled = false;
    setLoadingDetail(true);
    fetchMasteryMap(selected)
      .then((result) => {
        if (!cancelled) setDetail(result);
      })
      .catch(() => {
        if (!cancelled) setDetail(null);
      })
      .finally(() => {
        if (!cancelled) setLoadingDetail(false);
      });
    return () => {
      cancelled = true;
    };
  }, [selected]);

  const handleDelete = useCallback(
    async (pathId: string) => {
      if (
        !window.confirm(
          tr("确定删除这条精通之路？", "Delete this mastery path?"),
        )
      )
        return;
      await deleteProgress(pathId);
      if (selected === pathId) setSelected(null);
      await loadList();
    },
    [selected, loadList, tr],
  );

  const handleRedo = useCallback(
    async (pathId: string) => {
      if (
        !window.confirm(
          tr(
            "重置进度？知识点保留，但掌握度与复习计划清空。",
            "Reset progress? Objectives are kept, but mastery and reviews are cleared.",
          ),
        )
      )
        return;
      await redoProgress(pathId);
      const result = await fetchMasteryMap(pathId);
      setDetail(result);
    },
    [tr],
  );

  return (
    <div className="flex h-full">
      {/* Path list */}
      <aside className="w-64 shrink-0 border-r border-[var(--border)] flex flex-col">
        <header className="px-4 py-3 border-b border-[var(--border)]">
          <div className="flex items-center gap-2 text-[var(--foreground)]">
            <GraduationCap className="w-4 h-4" />
            <h1 className="text-sm font-semibold">
              {tr("精通之路", "Mastery Path")}
            </h1>
          </div>
          <p className="mt-1 text-xs text-[var(--muted-foreground)]">
            {tr(
              "掌握式学习：硬门槛 + 间隔复习",
              "Mastery-based learning: hard gate + spaced review",
            )}
          </p>
        </header>
        <div className="flex-1 overflow-y-auto p-2 space-y-1">
          {loadingList ? (
            <div className="flex items-center justify-center py-8 text-[var(--muted-foreground)]">
              <Loader2 className="w-4 h-4 animate-spin" />
            </div>
          ) : paths.length === 0 ? (
            <p className="px-2 py-3 text-xs text-[var(--muted-foreground)] leading-relaxed">
              {tr(
                "还没有精通之路。去「对话」选择 Mastery Path 模式，让导师根据你的材料建一条。",
                "No paths yet. Open Chat, pick Mastery Path mode, and ask the tutor to build one from your materials.",
              )}
            </p>
          ) : (
            paths.map((path) => (
              <button
                key={path.book_id}
                onClick={() => setSelected(path.book_id)}
                className={`w-full text-left px-3 py-2 rounded-md transition-colors cursor-pointer ${
                  selected === path.book_id
                    ? "bg-[var(--primary)]/10 ring-1 ring-[var(--primary)]/30"
                    : "hover:bg-[var(--accent)]"
                }`}
              >
                <div className="truncate text-sm text-[var(--foreground)]">
                  {path.name}
                </div>
                <div className="mt-0.5 text-xs text-[var(--muted-foreground)]">
                  {path.kp_count} {tr("个知识点", "objectives")} ·{" "}
                  {path.avg_mastery_pct}%
                </div>
              </button>
            ))
          )}
        </div>
        <footer className="p-2 border-t border-[var(--border)]">
          <button
            onClick={() => router.push("/home")}
            className="w-full flex items-center justify-center gap-1.5 px-3 py-2 text-sm rounded-md bg-[var(--primary)] text-[var(--primary-foreground)] hover:opacity-90 transition-opacity cursor-pointer"
          >
            <MessageSquare className="w-3.5 h-3.5" />
            {tr("新建（在对话中）", "New (in Chat)")}
          </button>
        </footer>
      </aside>

      {/* Selected path map */}
      <section className="flex-1 overflow-y-auto">
        {loadingDetail ? (
          <div className="flex items-center justify-center h-full text-[var(--muted-foreground)]">
            <Loader2 className="w-5 h-5 animate-spin" />
          </div>
        ) : !detail ? (
          <div className="flex flex-col items-center justify-center h-full text-center px-6 text-[var(--muted-foreground)]">
            <GraduationCap className="w-10 h-10 mb-3 opacity-40" />
            <p className="text-sm max-w-sm leading-relaxed">
              {tr(
                "选择一条精通之路查看进度地图，或在「对话」里用 Mastery Path 模式开始。",
                "Select a path to see its progress map, or start one in Chat with Mastery Path mode.",
              )}
            </p>
          </div>
        ) : (
          <>
            <div className="flex items-center justify-between px-6 pt-3 pb-1">
              <div className="flex items-center gap-1 rounded-lg border border-[var(--border)] p-0.5">
                <button
                  onClick={() => setViewMode("list")}
                  className={`flex items-center gap-1.5 px-2.5 py-1 text-xs rounded-md transition-colors cursor-pointer ${
                    viewMode === "list"
                      ? "bg-[var(--primary)]/10 text-[var(--primary)]"
                      : "text-[var(--muted-foreground)] hover:text-[var(--foreground)]"
                  }`}
                >
                  <List className="w-3.5 h-3.5" />
                  List
                </button>
                <button
                  onClick={() => setViewMode("graph")}
                  className={`flex items-center gap-1.5 px-2.5 py-1 text-xs rounded-md transition-colors cursor-pointer ${
                    viewMode === "graph"
                      ? "bg-[var(--primary)]/10 text-[var(--primary)]"
                      : "text-[var(--muted-foreground)] hover:text-[var(--foreground)]"
                  }`}
                >
                  <Network className="w-3.5 h-3.5" />
                  Graph
                </button>
              </div>
              <div className="flex items-center gap-1.5">
                <button
                  onClick={() => selected && handleRedo(selected)}
                  title={tr("重置进度", "Reset progress")}
                  className="p-1.5 rounded-md text-[var(--muted-foreground)] hover:bg-[var(--accent)] cursor-pointer"
                >
                  <RotateCcw className="w-4 h-4" />
                </button>
                <button
                  onClick={() => selected && handleDelete(selected)}
                  title={tr("删除", "Delete")}
                  className="p-1.5 rounded-md text-[var(--muted-foreground)] hover:bg-red-500/10 hover:text-red-500 cursor-pointer"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            </div>
            <div className="flex-1 overflow-y-auto">
              {viewMode === "list" ? (
                <ModuleMap
                  result={detail}
                  onContinue={() =>
<<<<<<< Updated upstream
                    selected && router.push(
                      `/noteblocks?session=1&pathId=${encodeURIComponent(selected)}`
                    )
                  }
                  onModuleStudy={(moduleId) => {
                    const encodedPath = encodeURIComponent(selected!);
                    const encodedModule = encodeURIComponent(moduleId);
                    router.push(`/noteblocks?session=1&pathId=${encodedPath}&module=${encodedModule}`);
=======
                    selected && router.push(`/noteblocks?session=1&pathId=${encodeURIComponent(selected)}`)
                  }
                  onModuleStudy={(moduleId, moduleName) => {
                    if (!selected) return;
                    router.push(`/noteblocks?session=1&pathId=${encodeURIComponent(selected)}&module=${encodeURIComponent(moduleId)}`);
>>>>>>> Stashed changes
                  }}
                />
              ) : (
                <ConceptGraph
                  result={detail}
<<<<<<< Updated upstream
                  onNodeClick={(kpId) =>
                    router.push(
                      `/noteblocks?session=1&pathId=${encodeURIComponent(selected!)}&kp=${kpId}`
                    )
                  }
=======
                  onNodeClick={(kpId) => {
                    if (!selected) return;
                    router.push(`/noteblocks?session=1&pathId=${encodeURIComponent(selected)}&kp=${kpId}`);
                  }}
>>>>>>> Stashed changes
                />
              )}
            </div>
          </>
        )}
      </section>
    </div>
  );
}

// MapView replaced by ModuleMap (components/learning/ModuleMap.tsx)
