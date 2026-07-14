"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { useParams } from "next/navigation";
import {
  fetchProject,
  fetchSessions,
  type ProjectDetail,
  type SessionEntry,
} from "@/lib/projects-api";

const DB_LABELS: Record<string, string> = {
  fontes: "Fontes",
  arquitetura: "Arquitetura",
  tarefas: "Tarefas",
  rotinas: "Rotinas",
  frameworks: "Frameworks",
  ferramentas: "Ferramentas",
  docs: "Documentos",
  sessoes: "Sessões",
  conversas: "Conversas",
};

export default function ProjectDetailPage() {
  const { slug } = useParams<{ slug: string }>();
  const [project, setProject] = useState<ProjectDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [sessions, setSessions] = useState<SessionEntry[]>([]);
  const [showMiniSessions, setShowMiniSessions] = useState(false);

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const [proj, sess] = await Promise.all([
        fetchProject(slug),
        fetchSessions(slug),
      ]);
      setProject(proj);
      setSessions(sess);
    } catch {
      setError(`Projeto "${slug}" não encontrado.`);
    } finally {
      setLoading(false);
    }
  }, [slug]);

  useEffect(() => {
    void load();
  }, [load]);

  // Filter sessions by origem
  const filteredSessions = showMiniSessions
    ? sessions
    : sessions.filter((s) => s.origem !== "noteblocks");

  useEffect(() => {
    void load();
  }, [load]);

  if (loading) {
    return (
      <div className="flex h-full items-center justify-center p-8">
        <div className="mx-auto h-8 w-8 animate-spin rounded-full border-4 border-[var(--border)] border-t-[var(--accent)]" />
      </div>
    );
  }

  if (error || !project) {
    return (
      <div className="flex h-full items-center justify-center p-8">
        <div className="max-w-md text-center">
          <p className="mb-4 text-sm text-red-500">{error}</p>
          <Link
            href="/projects"
            className="text-sm text-[var(--accent)] hover:underline"
          >
            ← Voltar para projetos
          </Link>
        </div>
      </div>
    );
  }

  const state = project.project_state;

  return (
    <div className="mx-auto max-w-5xl p-6">
      {/* Header */}
      <div className="mb-6">
        <Link
          href="/projects"
          className="mb-2 inline-block text-sm text-[var(--accent)] hover:underline"
        >
          ← Projetos
        </Link>
        <div className="flex items-start justify-between">
          <div>
            <h1 className="text-2xl font-bold">{state.projeto}</h1>
            <p className="mt-1 text-sm text-[var(--muted-foreground)]">
              {state.area} &middot; {state.objetivo}
            </p>
          </div>
          <span
            className={`shrink-0 rounded-full px-3 py-1 text-xs font-medium ${
              state.status === "Em andamento"
                ? "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200"
                : state.status === "Ideia"
                  ? "bg-yellow-100 text-yellow-800"
                  : "bg-gray-100 text-gray-800"
            }`}
          >
            {state.status}
          </span>
        </div>
      </div>

      <div className="grid gap-6 lg:grid-cols-3">
        {/* Coluna da esquerda: state info */}
        <div className="space-y-4 lg:col-span-1">
          {/* Project State */}
          <section className="rounded-lg border border-[var(--border)] bg-[var(--card)] p-4">
            <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-[var(--muted-foreground)]">
              Project State
            </h2>
            <dl className="space-y-2 text-sm">
              <div className="flex justify-between">
                <dt className="text-[var(--muted-foreground)]">Status</dt>
                <dd>{state.status}</dd>
              </div>
              {state.repositorio_codigo && (
                <div className="flex justify-between">
                  <dt className="text-[var(--muted-foreground)]">Repositório</dt>
                  <dd className="font-mono text-xs">
                    {state.repositorio_codigo}
                  </dd>
                </div>
              )}
              {state.ultima_atualizacao && (
                <div className="flex justify-between">
                  <dt className="text-[var(--muted-foreground)]">
                    Última atualização
                  </dt>
                  <dd>{state.ultima_atualizacao}</dd>
                </div>
              )}
            </dl>
          </section>

          {/* Caminho / Fases */}
          {state.caminho && state.caminho.length > 0 && (
            <section className="rounded-lg border border-[var(--border)] bg-[var(--card)] p-4">
              <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-[var(--muted-foreground)]">
                Caminho
              </h2>
              <ol className="space-y-3">
                {state.caminho.map((fase, i) => (
                  <li key={i} className="flex gap-3">
                    <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-[var(--accent)] text-xs font-bold text-white">
                      {i + 1}
                    </span>
                    <div>
                      <p className="text-sm font-medium">{fase.fase}</p>
                      <p className="text-xs text-[var(--muted-foreground)]">
                        {fase.descricao}
                      </p>
                    </div>
                  </li>
                ))}
              </ol>
            </section>
          )}

          {/* Próximos Passos */}
          {state.proximos_passos && state.proximos_passos.length > 0 && (
            <section className="rounded-lg border border-[var(--border)] bg-[var(--card)] p-4">
              <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-[var(--muted-foreground)]">
                Próximos Passos
              </h2>
              <ul className="space-y-2">
                {state.proximos_passos.map((t, i) => (
                  <li key={i} className="flex items-start gap-2 text-sm">
                    <span
                      className={`mt-0.5 h-2 w-2 shrink-0 rounded-full ${
                        t.prioridade === "alta"
                          ? "bg-red-500"
                          : t.prioridade === "media"
                            ? "bg-yellow-500"
                            : "bg-gray-400"
                      }`}
                    />
                    <span>{t.descricao}</span>
                  </li>
                ))}
              </ul>
            </section>
          )}
        </div>

        {/* Coluna da direita: databases/entradas */}
        <div className="space-y-4 lg:col-span-2">
          <h2 className="text-sm font-semibold uppercase tracking-wide text-[var(--muted-foreground)]">
            Databases
          </h2>

          {/* Sessões */}
          <section className="rounded-lg border border-[var(--border)] bg-[var(--card)]">
            <div className="flex items-center justify-between border-b border-[var(--border)] px-4 py-3">
              <div>
                <h3 className="text-sm font-medium">Sessões</h3>
                <p className="text-xs text-[var(--muted-foreground)]">
                  {filteredSessions.length} sessões
                  {!showMiniSessions && sessions.length > filteredSessions.length &&
                    ` (${sessions.length - filteredSessions.length} mini-sessões ocultas)`}
                </p>
              </div>
              <label className="flex items-center gap-2 text-xs text-[var(--muted-foreground)]">
                <input
                  type="checkbox"
                  checked={showMiniSessions}
                  onChange={(e) => setShowMiniSessions(e.target.checked)}
                  className="h-3.5 w-3.5 rounded border-[var(--border)]"
                />
                Mostrar mini-sessões
              </label>
            </div>
            <div className="divide-y divide-[var(--border)]">
              {filteredSessions.slice(0, 15).map((s) => (
                <div key={s.slug} className="flex items-center justify-between px-4 py-2.5">
                  <div className="flex items-center gap-2">
                    <span className={`h-1.5 w-1.5 shrink-0 rounded-full ${
                      s.origem === "noteblocks" ? "bg-purple-400" : "bg-blue-400"
                    }`} />
                    <span className="text-sm font-medium">{s.slug}</span>
                  </div>
                  {s.origem && (
                    <span className={`rounded-full px-2 py-0.5 text-[10px] font-medium ${
                      s.origem === "noteblocks"
                        ? "bg-purple-100 text-purple-700 dark:bg-purple-900 dark:text-purple-300"
                        : "bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300"
                    }`}>
                      {s.origem}
                    </span>
                  )}
                </div>
              ))}
              {filteredSessions.length === 0 && (
                <div className="px-4 py-6 text-center text-xs text-[var(--muted-foreground)]">
                  Nenhuma sessão encontrada.
                </div>
              )}
            </div>
          </section>

          {Object.entries(DB_LABELS).map(([key, label]) => {
            const entries = project.fontes[key];
            if (!entries || entries.length === 0) return null;

            return (
              <section
                key={key}
                className="rounded-lg border border-[var(--border)] bg-[var(--card)]"
              >
                <div className="border-b border-[var(--border)] px-4 py-3">
                  <h3 className="text-sm font-medium">{label}</h3>
                  <p className="text-xs text-[var(--muted-foreground)]">
                    {entries.length}{" "}
                    {entries.length === 1 ? "entrada" : "entradas"}
                  </p>
                </div>
                <div className="divide-y divide-[var(--border)]">
                  {entries.slice(0, 10).map((entry) => (
                    <div key={entry.arquivo} className="px-4 py-2.5">
                      <p className="text-sm font-medium">{entry.nome}</p>
                      {entry.conteudo && (
                        <p className="mt-1 line-clamp-2 text-xs text-[var(--muted-foreground)]">
                          {entry.conteudo.slice(0, 200)}
                          {entry.conteudo.length > 200 ? "..." : ""}
                        </p>
                      )}
                    </div>
                  ))}
                </div>
              </section>
            );
          })}
        </div>
      </div>
    </div>
  );
}
