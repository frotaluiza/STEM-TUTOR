"use client";

import { useCallback, useEffect, useState } from "react";

type WatcherStatus = {
  running: boolean;
  pid: number | null;
  last_healthy_pulse: string | null;
  last_pulse_seconds_ago: number | null;
  sessions_processed: number;
  sessions_tracked: number;
};

type LogResponse = {
  lines: string[];
};

type ProjectInfo = {
  name: string;
  slug: string;
  count: number;
  cost: number;
};

type ProjectsResponse = {
  projects: ProjectInfo[];
  total_sessions: number;
  total_cost: number;
};

type SessionInfo = {
  slug: string;
  title: string;
  project: string;
  project_slug: string;
  date: string;
  agent: string;
  cost: number;
};

type RecentSessionsResponse = {
  sessions: SessionInfo[];
};

type StatsResponse = {
  total_sessions: number;
  total_cost: number;
  total_live_docs: number;
  total_projects: number;
  stem_tutor_sessions: number;
  stem_tutor_cost: number;
};

type HealthResponse = {
  healthy: boolean;
  watcher_running: boolean;
  last_log: string;
  timestamp: string;
};

async function fetchJson<T>(url: string, signal?: AbortSignal): Promise<T | null> {
  try {
    const res = await fetch(url, { signal });
    if (!res.ok) return null;
    return (await res.json()) as T;
  } catch {
    return null;
  }
}

function WatcherBadge({ running, pulse }: { running: boolean; pulse: number | null }) {
  const color = running ? (pulse !== null && pulse < 300 ? "bg-green-500" : "bg-yellow-500") : "bg-red-500";
  const label = running ? (pulse !== null && pulse < 300 ? "Online" : "Unresponsive") : "Offline";
  return (
    <span className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-medium text-white ${color}`}>
      <span className="w-1.5 h-1.5 rounded-full bg-white animate-pulse" />
      {label}
    </span>
  );
}

function ProjectCard({ project }: { project: ProjectInfo }) {
  const colors: Record<string, string> = {
    "ai-stem-tutor": "border-l-blue-500",
    "tcc": "border-l-purple-500",
    "notion-infra": "border-l-amber-500",
    "luc-repport": "border-l-teal-500",
    "pinns": "border-l-rose-500",
    "plex": "border-l-emerald-500",
    "personal": "border-l-gray-500",
    "opencode-explore": "border-l-cyan-500",
  };
  const borderColor = colors[project.slug] || "border-l-gray-400";
  return (
    <div className={`border-l-4 ${borderColor} bg-white dark:bg-gray-800 rounded-lg shadow-sm p-4`}>
      <div className="flex justify-between items-start">
        <div>
          <h3 className="font-medium text-sm text-gray-900 dark:text-gray-100">{project.name}</h3>
          <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">{project.slug}</p>
        </div>
        <span className="text-xs font-mono text-gray-400">{project.count} sessões</span>
      </div>
      {project.cost > 0 && (
        <p className="text-xs text-gray-500 mt-2">💰 ${project.cost.toFixed(2)}</p>
      )}
    </div>
  );
}

export default function PMDashboard() {
  const [status, setStatus] = useState<WatcherStatus | null>(null);
  const [logs, setLogs] = useState<string[]>([]);
  const [projects, setProjects] = useState<ProjectsResponse | null>(null);
  const [sessions, setSessions] = useState<SessionInfo[]>([]);
  const [stats, setStats] = useState<StatsResponse | null>(null);
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [autoRefresh, setAutoRefresh] = useState(true);

  const fetchAll = useCallback(async (signal?: AbortSignal) => {
    const [s, l, p, sess, st, h] = await Promise.all([
      fetchJson<WatcherStatus>("/api/v1/pm/status", signal),
      fetchJson<LogResponse>("/api/v1/pm/logs?tail=20", signal),
      fetchJson<ProjectsResponse>("/api/v1/pm/projects", signal),
      fetchJson<RecentSessionsResponse>("/api/v1/pm/sessions/recent?limit=10", signal),
      fetchJson<StatsResponse>("/api/v1/pm/stats", signal),
      fetchJson<HealthResponse>("/api/v1/pm/health", signal),
    ]);
    if (s) setStatus(s);
    if (l) setLogs(l.lines);
    if (p) setProjects(p);
    if (sess) setSessions(sess.sessions);
    if (st) setStats(st);
    if (h) setHealth(h);
  }, []);

  useEffect(() => {
    const abort = new AbortController();
    fetchAll(abort.signal);
    return () => abort.abort();
  }, [fetchAll]);

  useEffect(() => {
    if (!autoRefresh) return;
    const interval = setInterval(() => {
      const abort = new AbortController();
      fetchAll(abort.signal);
    }, 15000);
    return () => clearInterval(interval);
  }, [autoRefresh, fetchAll]);

  return (
    <div className="p-6 max-w-7xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">Project Manager</h1>
          <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
            Monitoramento do watcher, sessões e projetos
          </p>
        </div>
        <div className="flex items-center gap-4">
          {status && <WatcherBadge running={status.running} pulse={status.last_pulse_seconds_ago} />}
          <label className="flex items-center gap-2 text-sm text-gray-500">
            <input
              type="checkbox"
              checked={autoRefresh}
              onChange={(e) => setAutoRefresh(e.target.checked)}
              className="rounded border-gray-300"
            />
            Auto-refresh (15s)
          </label>
        </div>
      </div>

      {/* Stats cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <StatCard label="Sessões totais" value={stats?.total_sessions ?? "..."} />
        <StatCard label="Custo total" value={stats ? `$${stats.total_cost.toFixed(2)}` : "..."} />
        <StatCard label="Live docs" value={stats?.total_live_docs ?? "..."} />
        <StatCard label="Projetos" value={stats?.total_projects ?? "..."} />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left: Watcher + Projects */}
        <div className="lg:col-span-2 space-y-6">
          {/* Watcher status */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-4">
            <h2 className="text-sm font-semibold text-gray-900 dark:text-gray-100 mb-3">Watcher</h2>
            {status ? (
              <div className="grid grid-cols-2 gap-4 text-sm">
                <div>
                  <span className="text-gray-500">Status: </span>
                  <span className={status.running ? "text-green-600" : "text-red-600"}>
                    {status.running ? "Rodando" : "Parado"}
                  </span>
                </div>
                <div><span className="text-gray-500">PID: </span>{status.pid ?? "—"}</div>
                <div><span className="text-gray-500">Processadas: </span>{status.sessions_processed}</div>
                <div><span className="text-gray-500">Rastreadas: </span>{status.sessions_tracked}</div>
                <div className="col-span-2">
                  <span className="text-gray-500">Último pulso: </span>
                  {status.last_pulse_seconds_ago !== null
                    ? `${status.last_pulse_seconds_ago}s atrás`
                    : "Nunca"}
                </div>
              </div>
            ) : (
              <p className="text-sm text-gray-400">Carregando...</p>
            )}
          </div>

          {/* Projects */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-4">
            <div className="flex justify-between items-center mb-3">
              <h2 className="text-sm font-semibold text-gray-900 dark:text-gray-100">Projetos</h2>
              {projects && (
                <span className="text-xs text-gray-500">
                  {projects.total_sessions} sessões · ${projects.total_cost.toFixed(2)}
                </span>
              )}
            </div>
            <div className="space-y-2">
              {projects?.projects
                .filter((p) => p.count > 0 && p.slug !== "empty")
                .map((p) => <ProjectCard key={p.slug} project={p} />)}
            </div>
          </div>
        </div>

        {/* Right: Sessions + Logs */}
        <div className="space-y-6">
          {/* Recent sessions */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-4">
            <h2 className="text-sm font-semibold text-gray-900 dark:text-gray-100 mb-3">Sessões Recentes</h2>
            <div className="space-y-2 max-h-80 overflow-y-auto">
              {sessions.length === 0 && <p className="text-sm text-gray-400">Nenhuma</p>}
              {sessions.map((s) => (
                <div key={s.slug} className="text-xs border-b border-gray-100 dark:border-gray-700 pb-2 last:border-0">
                  <div className="flex justify-between">
                    <span className="font-medium text-gray-800 dark:text-gray-200 truncate max-w-[200px]">
                      {s.title}
                    </span>
                    <span className="text-gray-400 ml-2 shrink-0">{s.agent}</span>
                  </div>
                  <div className="flex justify-between mt-0.5">
                    <span className="text-gray-400">{s.project}</span>
                    <span className="text-gray-400">{s.date}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Health */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-4">
            <h2 className="text-sm font-semibold text-gray-900 dark:text-gray-100 mb-3">Health</h2>
            {health ? (
              <div className="text-xs space-y-1">
                <div className="flex justify-between">
                  <span className="text-gray-500">Watcher:</span>
                  <span className={health.watcher_running ? "text-green-600" : "text-red-600"}>
                    {health.watcher_running ? "OK" : "Offline"}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-500">Sistema:</span>
                  <span className={health.healthy ? "text-green-600" : "text-yellow-600"}>
                    {health.healthy ? "Saudável" : "Degradado"}
                  </span>
                </div>
                <div className="mt-2 text-gray-400 truncate">{health.last_log}</div>
              </div>
            ) : (
              <p className="text-xs text-gray-400">—</p>
            )}
          </div>

          {/* Logs */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-4">
            <h2 className="text-sm font-semibold text-gray-900 dark:text-gray-100 mb-3">Logs</h2>
            <pre className="text-[10px] text-gray-500 dark:text-gray-400 font-mono max-h-60 overflow-y-auto whitespace-pre-wrap">
              {logs.length === 0 ? "—" : logs.map((l, i) => <span key={i}>{l}{"\n"}</span>)}
            </pre>
          </div>
        </div>
      </div>
    </div>
  );
}

function StatCard({ label, value }: { label: string; value: string | number }) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-4">
      <p className="text-xs text-gray-500 dark:text-gray-400">{label}</p>
      <p className="text-2xl font-bold text-gray-900 dark:text-gray-100 mt-1">{value}</p>
    </div>
  );
}
