"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { ProjectDetail, ProjectInfo, ProjectsResponse, SessionBrief, StatsResponse } from "./types";

async function fetchJson<T>(url: string, signal?: AbortSignal): Promise<T | null> {
  try {
    const res = await fetch(url, { signal });
    if (!res.ok) return null;
    return (await res.json()) as T;
  } catch {
    return null;
  }
}

export function usePMData() {
  const [projects, setProjects] = useState<ProjectInfo[]>([]);
  const [totalCost, setTotalCost] = useState(0);
  const [totalSessions, setTotalSessions] = useState(0);
  const [selectedSlug, setSelectedSlug] = useState<string | null>(null);
  const [selectedProject, setSelectedProject] = useState<ProjectDetail | null>(null);
  const [sessions, setSessions] = useState<SessionBrief[]>([]);
  const [sessionsTotal, setSessionsTotal] = useState(0);
  const [stats, setStats] = useState<StatsResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const abortRef = useRef<AbortController | null>(null);

  const fetchProjects = useCallback(async (signal?: AbortSignal) => {
    const data = await fetchJson<ProjectsResponse>("/api/v1/pm/projects", signal);
    if (data) {
      const filtered = data.projects.filter((p) => p.slug !== "empty" && p.slug !== "unclassified");
      setProjects(filtered);
      setTotalCost(data.total_cost);
      setTotalSessions(data.total_sessions);
    }
  }, []);

  const fetchStats = useCallback(async (signal?: AbortSignal) => {
    const data = await fetchJson<StatsResponse>("/api/v1/pm/stats", signal);
    if (data) setStats(data);
  }, []);

  const fetchProjectDetail = useCallback(async (slug: string, signal?: AbortSignal) => {
    const data = await fetchJson<ProjectDetail>(`/api/v1/pm/projects/${slug}`, signal);
    if (data) setSelectedProject(data);
  }, []);

  const fetchProjectSessions = useCallback(async (slug: string, signal?: AbortSignal) => {
    const data = await fetchJson<{ sessions: SessionBrief[]; total: number }>(
      `/api/v1/pm/projects/${slug}/sessions?limit=50`,
      signal,
    );
    if (data) {
      setSessions(data.sessions);
      setSessionsTotal(data.total);
    }
  }, []);

  const fetchAll = useCallback(
    async (slug: string | null, signal?: AbortSignal) => {
      setLoading(true);
      await Promise.all([fetchProjects(signal), fetchStats(signal)]);
      if (slug) {
        await Promise.all([fetchProjectDetail(slug, signal), fetchProjectSessions(slug, signal)]);
      }
      setLoading(false);
    },
    [fetchProjects, fetchStats, fetchProjectDetail, fetchProjectSessions],
  );

  const selectProject = useCallback(
    (slug: string) => {
      setSelectedSlug(slug);
      if (abortRef.current) abortRef.current.abort();
      const abort = new AbortController();
      abortRef.current = abort;
      setLoading(true);
      Promise.all([fetchProjectDetail(slug, abort.signal), fetchProjectSessions(slug, abort.signal)]).finally(
        () => setLoading(false),
      );
    },
    [fetchProjectDetail, fetchProjectSessions],
  );

  useEffect(() => {
    const abort = new AbortController();
    abortRef.current = abort;
    fetchAll(null, abort.signal);
    return () => abort.abort();
  }, [fetchAll]);

  return {
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
  };
}
