"use client";

import { Cloud, CloudOff, GitPullRequest, Loader2, RefreshCw } from "lucide-react";
import { useCallback, useEffect, useState } from "react";

interface SyncInfo {
  status: string;
  ahead: number;
  behind: number;
  uncommitted: number;
  last_commit: string;
  repositorio: { slug: string; status: string };
}

const STATUS_MAP: Record<string, { color: string; label: string; dot: string }> = {
  synced: { color: "text-green-500", label: "Synced", dot: "bg-green-500" },
  ahead: { color: "text-blue-500", label: "Ahead", dot: "bg-blue-500" },
  behind: { color: "text-yellow-500", label: "Behind", dot: "bg-yellow-500" },
  diverged: { color: "text-red-500", label: "Diverged", dot: "bg-red-500" },
  "uncommitted": { color: "text-orange-400", label: "Uncommitted", dot: "bg-orange-400" },
  "no-remote": { color: "text-gray-500", label: "Local only", dot: "bg-gray-400" },
};

export default function PMSyncStatus({ branch }: { branch?: string }) {
  const [sync, setSync] = useState<SyncInfo | null>(null);
  const [loading, setLoading] = useState(true);

  const fetchSync = useCallback(async () => {
    setLoading(true);
    try {
      const params = branch ? `?branch=${encodeURIComponent(branch)}` : "";
      const res = await fetch(`/api/v1/pm/sync-status${params}`);
      if (res.ok) setSync(await res.json());
    } catch {} finally { setLoading(false); }
  }, [branch]);

  useEffect(() => { fetchSync(); }, [fetchSync]);

  if (loading) return <Loader2 size={12} className="animate-spin text-[var(--muted-foreground)]" />;
  if (!sync) return null;

  const st = STATUS_MAP[sync.status] || STATUS_MAP["no-remote"];
  const hasRepo = sync.repositorio?.slug;
  const details: string[] = [];
  if (sync.ahead > 0) details.push(`+${sync.ahead}`);
  if (sync.behind > 0) details.push(`-${sync.behind}`);
  if (sync.uncommitted > 0) details.push(`~${sync.uncommitted}`);

  return (
    <div className="flex items-center gap-2 text-[11px]">
      <button
        type="button"
        onClick={fetchSync}
        className="flex items-center gap-1.5 rounded border border-[var(--border)] px-2 py-1 text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)]/30 transition-colors"
        title="Refresh sync status"
      >
        <span className={`w-1.5 h-1.5 rounded-full ${st.dot}`} />
        <span className={st.color}>{st.label}</span>
        {details.length > 0 && (
          <span className="text-[10px] font-mono text-[var(--muted-foreground)]/60">
            {details.join(" ")}
          </span>
        )}
        <RefreshCw size={10} strokeWidth={1.6} className="ml-0.5 text-[var(--muted-foreground)]/40" />
      </button>

      {hasRepo && (
        <a
          href={`https://github.com/${sync.repositorio.slug}`}
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center gap-1 rounded border border-[var(--border)] px-2 py-1 text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)]/30 transition-colors"
          title={`${sync.repositorio.slug}`}
        >
          <Cloud size={10} strokeWidth={1.6} />
          <span className="truncate max-w-[120px]">{sync.repositorio.slug}</span>
        </a>
      )}
    </div>
  );
}
