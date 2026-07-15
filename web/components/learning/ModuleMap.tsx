"use client";

import { useState, useMemo, useCallback } from "react";
import { useTranslation } from "react-i18next";
import {
  ChevronDown,
  ChevronRight,
  Circle,
  CircleCheck,
  CircleDot,
  GraduationCap,
} from "lucide-react";
import type {
  MasteryMapResult,
  MapModule,
  MapKnowledgePoint,
  ObjectiveStatus,
} from "@/lib/learning-api";

interface ModuleMapProps {
  result: MasteryMapResult;
  onContinue: () => void;
  onKpClick?: (kpId: string) => void;
  onModuleStudy?: (moduleId: string, moduleName: string) => void;
}

const STATUS_META: Record<ObjectiveStatus, { className: string }> = {
  mastered: { className: "text-green-500" },
  learning: { className: "text-yellow-500" },
  new: { className: "text-[var(--muted-foreground)]" },
};

function StatusIcon({ status }: { status: ObjectiveStatus }) {
  const cls = `w-3.5 h-3.5 shrink-0 ${STATUS_META[status].className}`;
  if (status === "mastered") return <CircleCheck className={cls} />;
  if (status === "learning") return <CircleDot className={cls} />;
  return <Circle className={cls} />;
}

export default function ModuleMap({ result, onContinue, onKpClick, onModuleStudy }: ModuleMapProps) {
  const { t } = useTranslation();
  const { map, next } = result;
  const [expanded, setExpanded] = useState<Set<string>>(() => {
    // Auto-expand the module containing the next step
    const moduleId = map.modules.find((m) =>
      m.knowledge_points.some((kp) => kp.name === next.knowledge_point_name),
    )?.id;
    return moduleId ? new Set([moduleId]) : new Set(map.modules.length > 0 ? [map.modules[0].id] : []);
  });

  const pct = map.counts.total
    ? Math.round((map.counts.mastered / map.counts.total) * 100)
    : 0;

  const toggle = useCallback((id: string) => {
    setExpanded((prev) => {
      const nextSet = new Set(prev);
      if (nextSet.has(id)) nextSet.delete(id);
      else nextSet.add(id);
      return nextSet;
    });
  }, []);

  const handleKpClick = useCallback(
    (kp: MapKnowledgePoint) => {
      if (kp.status !== "mastered") onKpClick?.(kp.id);
    },
    [onKpClick],
  );

  return (
    <div className="max-w-2xl mx-auto px-6 py-5">
      {/* Progress header */}
      <div className="flex items-center gap-3 mb-4">
        <div className="flex-1">
          <div className="flex items-center justify-between text-sm">
            <span className="text-[var(--muted-foreground)]">
              {map.counts.mastered}/{map.counts.total} {t("mastered")}
              {map.due_reviews > 0 && (
                <span className="ml-2 text-yellow-600">
                  · {map.due_reviews} {t("due for review")}
                </span>
              )}
            </span>
            <span className="text-xs text-[var(--muted-foreground)] tabular-nums">
              {pct}%
            </span>
          </div>
          <div className="mt-1.5 h-2 w-full rounded-full bg-[var(--accent)] overflow-hidden">
            <div
              className="h-full bg-green-500 transition-all rounded-full"
              style={{ width: `${pct}%` }}
            />
          </div>
        </div>
      </div>

      {/* Next step card */}
      <button
        onClick={onContinue}
        className="w-full text-left rounded-lg border border-[var(--border)] hover:border-[var(--primary)]/40 hover:bg-[var(--accent)] p-3 mb-4 transition-colors cursor-pointer"
      >
        <div className="text-xs text-[var(--muted-foreground)]">{t("Next")}</div>
        <div className="mt-0.5 text-sm font-medium text-[var(--foreground)] flex items-center gap-2">
          {next.action === "complete" ? (
            t("All mastered! 🎉")
          ) : (
            <>
              <StatusIcon status={next.status as ObjectiveStatus} />
              {next.knowledge_point_name}
              <span className="text-[10px] uppercase tracking-wider text-[var(--muted-foreground)]">
                {next.knowledge_point_type}
              </span>
            </>
          )}
        </div>
        <div className="mt-1 text-xs text-[var(--primary)]">
          {t("Continue in NoteBlocks →")}
        </div>
      </button>

      {/* Accordion module list */}
      <div className="space-y-1">
        {map.modules.map((mod) => {
          const isOpen = expanded.has(mod.id);
          const mastered = mod.mastered;
          const total = mod.total;

          return (
            <div
              key={mod.id}
              className="rounded-lg border border-[var(--border)] overflow-hidden"
            >
              {/* Module header (clickable) */}
              <button
                onClick={() => toggle(mod.id)}
                className="w-full flex items-center gap-2 px-3 py-2.5 text-sm hover:bg-[var(--accent)] transition-colors cursor-pointer text-left"
              >
                {isOpen ? (
                  <ChevronDown className="w-4 h-4 shrink-0 text-[var(--muted-foreground)]" />
                ) : (
                  <ChevronRight className="w-4 h-4 shrink-0 text-[var(--muted-foreground)]" />
                )}
                <span className="flex-1 font-medium text-[var(--foreground)] truncate">
                  {mod.name}
                </span>
                <span className="text-xs text-[var(--muted-foreground)] tabular-nums whitespace-nowrap">
                  {mastered}/{total}
                </span>
                <div className="w-16 h-1.5 rounded-full bg-[var(--accent)] overflow-hidden shrink-0">
                  <div
                    className="h-full bg-green-500 rounded-full transition-all"
                    style={{ width: `${total ? (mastered / total) * 100 : 0}%` }}
                  />
                </div>
                {onModuleStudy && (
                  <button
                    type="button"
                    onClick={(e) => {
                      e.stopPropagation();
                      onModuleStudy(mod.id, mod.name);
                    }}
                    className="ml-1.5 p-1 rounded text-[var(--muted-foreground)] hover:text-[var(--primary)] hover:bg-[var(--accent)] transition-colors"
                    title="Estudar este módulo no NoteBlocks"
                  >
                    <GraduationCap className="w-3.5 h-3.5" />
                  </button>
                )}
              </button>

              {/* KP list (collapsible) */}
              {isOpen && (
                <div className="border-t border-[var(--border)]">
                  {mod.knowledge_points.length === 0 ? (
                    <p className="px-4 py-3 text-xs text-[var(--muted-foreground)]">
                      {t("No objectives defined yet.")}
                    </p>
                  ) : (
                    mod.knowledge_points.map((kp) => (
                      <button
                        key={kp.id}
                        onClick={() => handleKpClick(kp)}
                        disabled={kp.status === "mastered"}
                        className="w-full flex items-center gap-2 px-4 py-2 text-sm hover:bg-[var(--accent)] transition-colors cursor-pointer disabled:opacity-60 disabled:cursor-default text-left"
                      >
                        <StatusIcon status={kp.status} />
                        <span className="flex-1 truncate text-[var(--foreground)]">
                          {kp.name}
                        </span>
                        <span className="text-[10px] uppercase tracking-wider text-[var(--muted-foreground)]">
                          {kp.type}
                        </span>
                      </button>
                    ))
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
