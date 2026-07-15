"use client";

import { ExternalLink, GitBranch, GitCommit, Calendar, Lightbulb, ListChecks, Loader2 } from "lucide-react";
import type { ProjectDetail } from "./types";

interface PMReportSectionProps {
  project: ProjectDetail | null;
  loading: boolean;
  branchData?: any;
}

export default function PMReportSection({ project, loading }: PMReportSectionProps) {
  if (loading) {
    return (
      <div className="bg-[var(--card)] rounded-lg border border-[var(--border)] p-6 flex items-center justify-center text-[var(--muted-foreground)]">
        <Loader2 className="w-4 h-4 animate-spin mr-2" />
        Carregando...
      </div>
    );
  }

  if (!project) {
    return (
      <div className="bg-[var(--card)] rounded-lg border border-[var(--border)] p-6 text-center text-sm text-[var(--muted-foreground)]">
        Selecione um projeto para ver o relatório
      </div>
    );
  }

  return (
    <div className="bg-[var(--card)] rounded-lg border border-[var(--border)] divide-y divide-[var(--border)]/20">
      {/* Header */}
      <div className="px-4 py-3">
        <h3 className="text-sm font-semibold text-[var(--foreground)]">Relatório</h3>
      </div>

      {/* Meta info */}
      <div className="px-4 py-3 space-y-2.5 text-[12.5px]">
        {project.branch && (
          <div className="flex items-center gap-2 text-[var(--muted-foreground)]">
            <GitBranch size={13} strokeWidth={1.6} className="shrink-0" />
            <span className="font-mono text-[var(--foreground)]">{project.branch}</span>
          </div>
        )}
        {project.last_commit && (
          <div className="flex items-center gap-2 text-[var(--muted-foreground)]">
            <GitCommit size={13} strokeWidth={1.6} className="shrink-0" />
            <span className="font-mono text-[var(--foreground)]">{project.last_commit}</span>
          </div>
        )}
        {project.last_updated && (
          <div className="flex items-center gap-2 text-[var(--muted-foreground)]">
            <Calendar size={13} strokeWidth={1.6} className="shrink-0" />
            <span>{project.last_updated}</span>
          </div>
        )}
        {project.date_range?.min && (
          <div className="text-[var(--muted-foreground)] ml-[21px]">
            {project.date_range.min} — {project.date_range.max}
          </div>
        )}
      </div>

      {/* Stats */}
      <div className="px-4 py-3 grid grid-cols-3 gap-3">
        <div className="text-center">
          <div className="text-lg font-bold text-[var(--foreground)]">{project.total_sessions}</div>
          <div className="text-[10px] text-[var(--muted-foreground)] uppercase tracking-wider">Sessões</div>
        </div>
        <div className="text-center">
          <div className="text-lg font-bold text-[var(--foreground)]">${project.total_cost.toFixed(2)}</div>
          <div className="text-[10px] text-[var(--muted-foreground)] uppercase tracking-wider">Custo</div>
        </div>
        <div className="text-center">
          <div className="text-lg font-bold text-[var(--foreground)]">{project.session_files_available}</div>
          <div className="text-[10px] text-[var(--muted-foreground)] uppercase tracking-wider">Arquivos</div>
        </div>
      </div>

      {/* Decisions */}
      {project.decisions.length > 0 && (
        <div className="px-4 py-3">
          <div className="flex items-center gap-1.5 mb-2 text-[11px] font-semibold text-[var(--muted-foreground)] uppercase tracking-wider">
            <Lightbulb size={12} strokeWidth={1.8} />
            Decisões ({project.decisions.length})
          </div>
          <div className="space-y-1.5 max-h-40 overflow-y-auto">
            {project.decisions.map((d, i) => (
              <div key={i} className="text-[11.5px] leading-snug">
                <div className="text-[var(--foreground)]/85 line-clamp-2">{d.text}</div>
                {d.session_slug && (
                  <div className="flex items-center gap-1 mt-0.5">
                    <ExternalLink size={9} strokeWidth={1.8} className="text-[var(--muted-foreground)]/50" />
                    <span className="font-mono text-[10px] text-[var(--muted-foreground)]/60">{d.session_slug}</span>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Todos */}
      {project.todos.length > 0 && (
        <div className="px-4 py-3">
          <div className="flex items-center gap-1.5 mb-2 text-[11px] font-semibold text-[var(--muted-foreground)] uppercase tracking-wider">
            <ListChecks size={12} strokeWidth={1.8} />
            Próximos passos ({project.todos.length})
          </div>
          <div className="space-y-1">
            {project.todos.map((t: string | Record<string, unknown>, i: number) => (
              <div key={i} className="flex items-start gap-2 text-[11.5px] text-[var(--foreground)]/85">
                <span className="w-1.5 h-1.5 rounded-full bg-amber-500 mt-1.5 shrink-0" />
                {typeof t === "string" ? t : String(t.task || t.text || t.descricao || "")}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
