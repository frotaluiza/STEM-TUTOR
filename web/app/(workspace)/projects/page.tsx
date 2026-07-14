"use client";

import { useCallback, useEffect, useState } from "react";
import Link from "next/link";
import { useTranslation } from "react-i18next";
import { fetchProjects, type ProjectSummary } from "@/lib/projects-api";

const AREA_COLORS: Record<string, string> = {
  IA: "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200",
  Academico:
    "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200",
  Musica: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
  Pessoal: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
  Estudos:
    "bg-cyan-100 text-cyan-800 dark:bg-cyan-900 dark:text-cyan-200",
};

export default function ProjectsPage() {
  const { t } = useTranslation();
  const [projects, setProjects] = useState<ProjectSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchProjects();
      setProjects(data);
    } catch (e) {
      setError("Não foi possível carregar os projetos. A API do Orchestrator está rodando?");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    void load();
  }, [load]);

  if (loading) {
    return (
      <div className="flex h-full items-center justify-center p-8">
        <div className="text-center">
          <div className="mx-auto mb-4 h-8 w-8 animate-spin rounded-full border-4 border-[var(--border)] border-t-[var(--accent)]" />
          <p className="text-sm text-[var(--muted-foreground)]">
            Carregando projetos...
          </p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex h-full items-center justify-center p-8">
        <div className="max-w-md text-center">
          <p className="mb-4 text-sm text-red-500">{error}</p>
          <button
            onClick={load}
            className="rounded-md bg-[var(--accent)] px-4 py-2 text-sm text-white"
          >
            Tentar novamente
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto h-full max-w-5xl overflow-y-auto p-6">
      <div className="mb-6">
        <h1 className="text-2xl font-bold">Projetos</h1>
        <p className="mt-1 text-sm text-[var(--muted-foreground)]">
          Todos os seus project-spaces
        </p>
      </div>

      {projects.length === 0 ? (
        <div className="rounded-lg border border-dashed border-[var(--border)] p-12 text-center">
          <p className="text-sm text-[var(--muted-foreground)]">
            Nenhum projeto encontrado em Projetos/
          </p>
        </div>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2">
          {projects.map((project) => (
            <Link
              key={project.slug}
              href={`/projects/${project.slug}`}
              className="group rounded-lg border border-[var(--border)] bg-[var(--card)] p-5 transition-colors hover:border-[var(--accent)]"
            >
              <div className="mb-3 flex items-start justify-between">
                <h2 className="text-lg font-semibold">{project.nome}</h2>
                {project.area && (
                  <span
                    className={`ml-2 shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ${
                      AREA_COLORS[project.area] ?? "bg-gray-100 text-gray-800"
                    }`}
                  >
                    {project.area}
                  </span>
                )}
              </div>

              {project.objetivo && (
                <p className="mb-3 line-clamp-2 text-sm text-[var(--muted-foreground)]">
                  {project.objetivo}
                </p>
              )}

              <div className="flex items-center gap-3 text-xs text-[var(--muted-foreground)]">
                {project.status && (
                  <span className="flex items-center gap-1">
                    <span
                      className={`h-1.5 w-1.5 rounded-full ${
                        project.status === "Em andamento"
                          ? "bg-green-500"
                          : project.status === "Ideia"
                            ? "bg-yellow-500"
                            : "bg-gray-400"
                      }`}
                    />
                    {project.status}
                  </span>
                )}
                {project.repositorio_codigo && (
                  <span className="truncate font-mono">
                    {project.repositorio_codigo}
                  </span>
                )}
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
