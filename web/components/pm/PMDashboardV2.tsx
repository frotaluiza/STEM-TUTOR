"use client";

import dynamic from "next/dynamic";
import { useCallback, useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import { Activity, BarChart3, Database, ExternalLink, FileDown, Github, Layers, Loader2 } from "lucide-react";
import PMProjectSelector from "./PMProjectSelector";
import PMReportSection from "./PMReportSection";
import PMTable from "./PMTable";
import type { Column } from "./PMTable";
import { usePMData } from "./usePMData";
import type { Decision, SessionBrief } from "./types";

const ProjectMindMap = dynamic(() => import("@/components/mindmap/UnifiedMindMap"), { ssr: false });

function StatCard({ label, value, icon: Icon }: { label: string; value: string | number; icon: React.ComponentType<{ size?: number; strokeWidth?: number; className?: string }> }) {
  return (
    <div className="bg-[var(--card)] rounded-lg border border-[var(--border)] p-4 flex items-center gap-3">
      <div className="w-9 h-9 rounded-lg bg-[var(--accent)]/40 flex items-center justify-center shrink-0">
        <Icon size={16} strokeWidth={1.6} className="text-[var(--foreground)]/70" />
      </div>
      <div>
        <div className="text-lg font-bold text-[var(--foreground)]">{value}</div>
        <div className="text-[10.5px] text-[var(--muted-foreground)] uppercase tracking-wider">{label}</div>
      </div>
    </div>
  );
}

export default function PMDashboardV2() {
  const router = useRouter();
  const {
    projects,
    totalCost,
    totalSessions,
    selectedSlug,
    selectedProject,
    sessions,
    sessionsTotal,
    stats,
    loading,
    selectProject,
  } = usePMData();

  const [activeView, setActiveView] = useState<"dashboard" | "mindmap">("dashboard");

  const handleSessionClick = useCallback(
    (row: SessionBrief) => {
      router.push(`/session-viewer/${row.slug}`);
    },
    [router],
  );

  const defaultSlug = useMemo(() => {
    if (selectedSlug) return selectedSlug;
    const stem = projects.find((p) => p.slug === "ai-stem-tutor");
    return stem?.slug || projects[0]?.slug || null;
  }, [projects, selectedSlug]);

  const handleProjectSelect = useCallback(
    (slug: string) => {
      selectProject(slug);
    },
    [selectProject],
  );

  const sessionColumns = useMemo<Column<SessionBrief>[]>(
    () => [
      {
        key: "slug",
        label: "Slug",
        width: "110px",
        sortable: true,
        render: (r) => <span className="font-mono text-[var(--muted-foreground)]">{r.slug}</span>,
        filterValue: (r) => r.slug,
      },
      {
        key: "title",
        label: "Título",
        sortable: true,
        render: (r) => <span className="truncate max-w-[200px] inline-block">{r.title}</span>,
        filterValue: (r) => r.title,
      },
      {
        key: "agent",
        label: "Agente",
        width: "70px",
        sortable: true,
        render: (r) => (
          <span className="text-[11px] px-1.5 py-0.5 rounded bg-[var(--muted)]/40 text-[var(--muted-foreground)]">
            {r.agent}
          </span>
        ),
      },
      {
        key: "date",
        label: "Data",
        width: "85px",
        sortable: true,
        sortValue: (r) => r.date,
        render: (r) => <span className="text-[var(--muted-foreground)]">{r.date}</span>,
      },
      {
        key: "cost",
        label: "Custo",
        width: "65px",
        sortable: true,
        sortValue: (r) => r.cost,
        render: (r) => (
          <span className="font-mono text-[var(--muted-foreground)]">
            {r.cost > 0 ? `$${r.cost.toFixed(2)}` : "—"}
          </span>
        ),
      },
      {
        key: "actions",
        label: "",
        width: "60px",
        render: (r) => (
          <div className="flex items-center gap-1">
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                window.open(`/api/v1/pm/sessions/${r.slug}/live-doc`, "_blank", "noopener,noreferrer");
              }}
              className="inline-flex items-center gap-1 rounded px-1.5 py-1 text-[11px] font-medium text-[var(--muted-foreground)] hover:text-[var(--primary)] hover:bg-[var(--accent)]/40 transition-colors"
              title="Exportar live doc"
            >
              <FileDown size={12} strokeWidth={1.7} />
              <span>MD</span>
            </button>
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                router.push(`/session-viewer/${r.slug}`);
              }}
              className="inline-flex items-center gap-1 rounded px-1.5 py-1 text-[11px] font-medium text-[var(--muted-foreground)] hover:text-[var(--primary)] hover:bg-[var(--accent)]/40 transition-colors"
              title="Ver sessão"
            >
              <ExternalLink size={12} strokeWidth={1.7} />
              <span>NB</span>
            </button>
          </div>
        ),
      },
    ],
    [router],
  );

  return (
    <div className="p-6 max-w-[1440px] mx-auto space-y-5 h-full overflow-y-auto">
      {/* Header */}
      <div className="flex items-center justify-between flex-wrap gap-3">
        <div>
          <h1 className="text-xl font-bold text-[var(--foreground)] flex items-center gap-2">
            <Activity size={20} strokeWidth={1.8} />
            Project Manager
          </h1>
          <p className="text-[12px] text-[var(--muted-foreground)] mt-0.5">
            Gerenciamento de todos os projetos
          </p>
        </div>
        <div className="flex items-center gap-3">
          <PMProjectSelector
            projects={projects}
            selectedSlug={selectedSlug || defaultSlug}
            onSelect={handleProjectSelect}
          />
          <div className="flex rounded-lg border border-[var(--border)] overflow-hidden">
            <button
              type="button"
              onClick={() => setActiveView("dashboard")}
              className={`px-3 py-1.5 text-[12px] font-medium transition-colors ${
                activeView === "dashboard"
                  ? "bg-[var(--primary)] text-[var(--primary-foreground)]"
                  : "bg-[var(--card)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]"
              }`}
            >
              Dashboard
            </button>
            <button
              type="button"
              onClick={() => setActiveView("mindmap")}
              className={`px-3 py-1.5 text-[12px] font-medium transition-colors ${
                activeView === "mindmap"
                  ? "bg-[var(--primary)] text-[var(--primary-foreground)]"
                  : "bg-[var(--card)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]"
              }`}
            >
              Mind Map
            </button>
          </div>
        </div>
      </div>

      {/* Stats cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        <StatCard label="Sessões totais" value={stats?.total_sessions ?? totalSessions ?? "..."} icon={Database} />
        <StatCard label="Custo total" value={stats ? `$${stats.total_cost.toFixed(2)}` : totalCost ? `$${totalCost.toFixed(2)}` : "..."} icon={BarChart3} />
        <StatCard label="Live docs" value={stats?.total_live_docs ?? "..."} icon={Layers} />
        <StatCard label="Projetos" value={stats?.total_projects ?? projects.length ?? "..."} icon={Github} />
      </div>

      {activeView === "mindmap" ? (
        /* Mind Map view */
        <div className="bg-[var(--card)] rounded-lg border border-[var(--border)] overflow-hidden min-h-[500px] relative">
          <ProjectMindMap />
        </div>
      ) : (
        /* Dashboard view */
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
          {/* Left: Report + MindMap preview */}
          <div className="lg:col-span-1 space-y-5">
            <PMReportSection project={selectedProject} loading={loading} />
          </div>

          {/* Right: Tables */}
          <div className="lg:col-span-2 space-y-5">
            {/* Sessions table */}
            <PMTable
              title="Sessões"
              columns={sessionColumns}
              data={sessions}
              total={sessionsTotal}
              emptyMessage={loading ? "Carregando..." : "Nenhuma sessão encontrada"}
              defaultSort={{ key: "date", dir: "desc" }}
              onRowClick={handleSessionClick}
            />

            {/* Decisions table */}
            {selectedProject && selectedProject.decisions.length > 0 && (
              <PMTable
                title="Decisões"
                columns={[
                  {
                    key: "text",
                    label: "Decisão",
                    sortable: true,
                    render: (r: Decision) => (
                      <span className="line-clamp-2 text-[12px] leading-snug">{r.text}</span>
                    ),
                    filterValue: (r) => r.text,
                  },
                  {
                    key: "session",
                    label: "Sessão",
                    width: "100px",
                    render: (r: Decision) =>
                      r.session_slug ? (
                        <span className="font-mono text-[11px] text-[var(--muted-foreground)] hover:text-[var(--primary)] transition-colors">
                          {r.session_slug}
                        </span>
                      ) : (
                        <span className="text-[11px] text-[var(--muted-foreground)]/50">—</span>
                      ),
                  },
                ]}
                data={selectedProject.decisions}
                total={selectedProject.decisions.length}
                emptyMessage="Nenhuma decisão"
                defaultSort={{ key: "text", dir: "asc" }}
                filterable={false}
                onRowClick={(row) => {
                  if (row.session_slug) {
                    router.push(`/session-viewer/${row.session_slug}`);
                  }
                }}
              />
            )}
          </div>
        </div>
      )}
    </div>
  );
}
