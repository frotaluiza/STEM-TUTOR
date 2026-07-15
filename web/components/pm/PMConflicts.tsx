"use client";

import { AlertCircle, CheckCircle2, GitCompare, Loader2, XCircle } from "lucide-react";
import { useCallback, useEffect, useState } from "react";

interface Conflict {
  file: string;
  type: string;
  description: string;
}

interface ConflictsData {
  source: string;
  target: string;
  has_conflicts: boolean;
  conflicts: Conflict[];
  conflict_count: number;
  auto_merge_count: number;
  ahead: number;
  behind: number;
  files_changed: number;
  insertions: number;
  deletions: number;
  commits: string[];
}

export default function PMConflicts({ branch, onSelect }: { branch?: string; onSelect?: (b: string) => void }) {
  const [data, setData] = useState<ConflictsData | null>(null);
  const [loading, setLoading] = useState(false);
  const [source, setSource] = useState("");
  const [target, setTarget] = useState("main");
  const [branches, setBranches] = useState<{ name: string; current: boolean }[]>([]);

  // Fetch branches from API
  useEffect(() => {
    fetch("/api/v1/pm/branches")
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => {
        if (d?.branches) {
          setBranches(d.branches);
          // Auto-select current branch if available
          const current = d.current;
          if (current && current !== "main") setSource(current);
        }
      })
      .catch(() => {});
  }, []);

  const analyze = useCallback(async () => {
    if (!source) return;
    setLoading(true);
    try {
      const res = await fetch(`/api/v1/pm/conflicts?source=${encodeURIComponent(source)}&target=${encodeURIComponent(target)}`);
      if (res.ok) setData(await res.json());
    } catch {} finally { setLoading(false); }
  }, [source, target]);

  return (
    <div className="bg-[var(--card)] rounded-lg border border-[var(--border)] p-4 space-y-3">
      <div className="flex items-center gap-2">
        <GitCompare size={14} strokeWidth={1.7} />
        <span className="text-sm font-semibold text-[var(--foreground)]">Análise de Conflitos</span>
      </div>

      <div className="flex items-center gap-2">
        <select
          value={source}
          onChange={(e) => setSource(e.target.value)}
          className="flex-1 bg-transparent text-[12px] text-[var(--foreground)] border border-[var(--border)] rounded px-2 py-1 outline-none"
        >
          <option value="">Selecionar branch...</option>
          {branches.map((b) => (
            <option key={b.name} value={b.name}>
              {b.name} {b.current ? "(atual)" : ""}
            </option>
          ))}
        </select>
        <span className="text-[11px] text-[var(--muted-foreground)]">→</span>
        <select
          value={target}
          onChange={(e) => setTarget(e.target.value)}
          className="flex-1 bg-transparent text-[12px] text-[var(--foreground)] border border-[var(--border)] rounded px-2 py-1 outline-none"
        >
          {branches.map((b) => (
            <option key={b.name} value={b.name}>
              {b.name}
            </option>
          ))}
        </select>
        <button
          type="button"
          onClick={analyze}
          disabled={!source || loading}
          className="px-2.5 py-1 text-[11px] font-medium rounded bg-[var(--primary)]/10 text-[var(--primary)] hover:bg-[var(--primary)]/20 disabled:opacity-30 transition-colors"
        >
          {loading ? <Loader2 size={11} className="animate-spin" /> : "Analisar"}
        </button>
      </div>

      {data && (
        <div className="space-y-2 text-[12px]">
          <div className="flex items-center gap-2">
            {data.has_conflicts ? (
              <XCircle size={13} className="text-red-500" />
            ) : (
              <CheckCircle2 size={13} className="text-green-500" />
            )}
            <span className={data.has_conflicts ? "text-red-400" : "text-green-400"}>
              {data.has_conflicts
                ? `${data.conflict_count} conflito(s) detectado(s)`
                : `${data.auto_merge_count} arquivo(s) mergeáveis automaticamente`}
            </span>
          </div>

          <div className="flex gap-3 text-[11px] text-[var(--muted-foreground)]">
            <span>📊 {data.files_changed} arquivos</span>
            <span>➕ {data.insertions} inserções</span>
            <span>➖ {data.deletions} deleções</span>
            <span>🔀 {data.commits.length} commits</span>
          </div>

          {data.conflicts.length > 0 && (
            <div className="max-h-32 overflow-y-auto space-y-1">
              {data.conflicts.map((c, i) => (
                <div key={i} className={`flex items-center gap-1.5 py-0.5 text-[11px] ${
                  c.type === "content" ? "text-red-400" : "text-green-500"
                }`}>
                  {c.type === "content" ? <XCircle size={10} /> : <CheckCircle2 size={10} />}
                  <span className="font-mono">{c.file}</span>
                  <span className="text-[var(--muted-foreground)]/60">{c.type === "content" ? "⚡ conflito" : "✅ auto-merge"}</span>
                </div>
              ))}
            </div>
          )}

          {data.commits.length > 0 && (
            <details className="text-[11px]">
              <summary className="cursor-pointer text-[var(--muted-foreground)] hover:text-[var(--foreground)]">
                📋 {data.commits.length} commits a mergear
              </summary>
              <div className="mt-1 max-h-24 overflow-y-auto space-y-0.5">
                {data.commits.map((c, i) => (
                  <div key={i} className="font-mono text-[10px] text-[var(--muted-foreground)]/70">{c}</div>
                ))}
              </div>
            </details>
          )}
        </div>
      )}
    </div>
  );
}
