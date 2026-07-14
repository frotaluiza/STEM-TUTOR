"use client";

import { GitBranch } from "lucide-react";
import { useCallback, useEffect, useState } from "react";

interface BranchInfo {
  name: string;
  current: boolean;
}

interface PMBranchSelectorProps {
  currentBranch: string | null;
  onSelect: (branch: string) => void;
}

export default function PMBranchSelector({ currentBranch, onSelect }: PMBranchSelectorProps) {
  const [branches, setBranches] = useState<BranchInfo[]>([]);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    fetch("/api/v1/pm/branches")
      .then((r) => r.ok ? r.json() : null)
      .then((d) => { if (d?.branches) setBranches(d.branches); })
      .catch(() => {});
  }, []);

  const handleSelect = useCallback((name: string) => {
    onSelect(name);
    setOpen(false);
  }, [onSelect]);

  const current = currentBranch || branches.find((b) => b.current)?.name || "main";

  return (
    <div className="relative">
      <button
        type="button"
        onClick={() => setOpen(!open)}
        className="flex items-center gap-1.5 rounded-lg border border-[var(--border)] bg-[var(--card)] px-2.5 py-1.5 text-[12px] text-[var(--foreground)] hover:bg-[var(--accent)]/50 transition-colors"
      >
        <GitBranch size={12} strokeWidth={1.7} className="text-[var(--muted-foreground)]" />
        <span className="font-mono truncate max-w-[160px]">{current}</span>
        <span className="text-[10px] text-[var(--muted-foreground)]">▼</span>
      </button>

      {open && (
        <>
          <div className="fixed inset-0 z-10" onClick={() => setOpen(false)} />
          <div className="absolute top-full left-0 mt-1 z-20 w-[220px] rounded-lg border border-[var(--border)] bg-[var(--card)] shadow-lg py-1 max-h-[40vh] overflow-y-auto">
            {branches.map((b) => (
              <button
                key={b.name}
                type="button"
                onClick={() => handleSelect(b.name)}
                className={`flex items-center gap-2 w-full px-3 py-1.5 text-[12px] text-left transition-colors hover:bg-[var(--accent)]/50 ${
                  b.name === current ? "bg-[var(--accent)]/20 text-[var(--foreground)]" : "text-[var(--foreground)]/85"
                }`}
              >
                <GitBranch size={11} strokeWidth={1.5} className="shrink-0 text-[var(--muted-foreground)]" />
                <span className="flex-1 font-mono truncate">{b.name}</span>
                {b.current && <span className="text-[10px] text-green-500">●</span>}
              </button>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
