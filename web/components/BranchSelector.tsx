"use client";

import { useCallback, useEffect, useState } from "react";
import { fetchBranches, type BranchInfo } from "@/lib/projects-api";
import { GitBranch } from "lucide-react";

interface Props {
  selected: string;
  onChange: (branch: string) => void;
}

export default function BranchSelector({ selected, onChange }: Props) {
  const [branches, setBranches] = useState<BranchInfo[]>([]);
  const [loading, setLoading] = useState(true);
  const [open, setOpen] = useState(false);

  const load = useCallback(async () => {
    try {
      const data = await fetchBranches();
      setBranches(data.branches);
    } catch {
      // offline
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    void load();
  }, [load]);

  if (loading || branches.length === 0) return null;

  return (
    <div className="relative">
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-1.5 rounded-md border border-[var(--border)] px-2.5 py-1.5 text-xs font-medium transition-colors hover:bg-[var(--accent)] hover:text-white"
      >
        <GitBranch className="h-3.5 w-3.5" />
        <span>{selected || "branch"}</span>
      </button>

      {open && (
        <>
          <div
            className="fixed inset-0 z-10"
            onClick={() => setOpen(false)}
          />
          <div className="absolute right-0 top-full z-20 mt-1 w-44 rounded-lg border border-[var(--border)] bg-[var(--card)] py-1 shadow-lg">
            {branches.map((b) => (
              <button
                key={b.branch}
                onClick={() => {
                  onChange(b.branch);
                  setOpen(false);
                }}
                className={`flex w-full items-center gap-2 px-3 py-1.5 text-left text-xs transition-colors hover:bg-[var(--accent)] hover:text-white ${
                  b.branch === selected ? "font-semibold text-[var(--accent)]" : ""
                }`}
              >
                <span className="h-1.5 w-1.5 rounded-full bg-current" />
                {b.branch}
              </button>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
