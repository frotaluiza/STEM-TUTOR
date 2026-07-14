"use client";

import { ChevronDown } from "lucide-react";
import { useCallback, useRef, useState } from "react";
import type { ProjectInfo } from "./types";

const SLUG_COLORS: Record<string, string> = {
  "ai-stem-tutor": "bg-blue-500",
  tcc: "bg-purple-500",
  "notion-infra": "bg-amber-500",
  "luc-repport": "bg-teal-500",
  pinns: "bg-rose-500",
  plex: "bg-emerald-500",
  personal: "bg-gray-500",
  "opencode-explore": "bg-cyan-500",
};

function slugColor(slug: string): string {
  return SLUG_COLORS[slug] || "bg-gray-400";
}

interface PMProjectSelectorProps {
  projects: ProjectInfo[];
  selectedSlug: string | null;
  onSelect: (slug: string) => void;
}

export default function PMProjectSelector({ projects, selectedSlug, onSelect }: PMProjectSelectorProps) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);
  const selected = projects.find((p) => p.slug === selectedSlug) || projects[0];

  const handleSelect = useCallback(
    (slug: string) => {
      onSelect(slug);
      setOpen(false);
    },
    [onSelect],
  );

  return (
    <div ref={ref} className="relative">
      <button
        type="button"
        onClick={() => setOpen(!open)}
        className="flex items-center gap-2.5 rounded-lg border border-[var(--border)] bg-[var(--card)] px-3 py-2 text-sm text-[var(--foreground)] hover:bg-[var(--accent)]/50 transition-colors min-w-[220px]"
      >
        {selected && (
          <>
            <span className={`w-2.5 h-2.5 rounded-full shrink-0 ${slugColor(selected.slug)}`} />
            <span className="flex-1 text-left truncate">{selected.name}</span>
            <span className="text-[11px] text-[var(--muted-foreground)]">{selected.count}</span>
          </>
        )}
        <ChevronDown size={14} className={`shrink-0 text-[var(--muted-foreground)] transition-transform ${open ? "rotate-180" : ""}`} />
      </button>

      {open && (
        <>
          <div className="fixed inset-0 z-10" onClick={() => setOpen(false)} />
          <div className="absolute top-full left-0 mt-1 z-20 w-full min-w-[280px] rounded-lg border border-[var(--border)] bg-[var(--card)] shadow-lg py-1 max-h-[50vh] overflow-y-auto">
            {projects.map((p) => (
              <button
                key={p.slug}
                type="button"
                onClick={() => handleSelect(p.slug)}
                className={`flex items-center gap-2.5 w-full px-3 py-2 text-sm text-left transition-colors hover:bg-[var(--accent)]/50 ${
                  p.slug === selectedSlug ? "bg-[var(--accent)]/30 text-[var(--foreground)]" : "text-[var(--foreground)]/85"
                }`}
              >
                <span className={`w-2.5 h-2.5 rounded-full shrink-0 ${slugColor(p.slug)}`} />
                <span className="flex-1 truncate">{p.name}</span>
                <span className="text-[11px] text-[var(--muted-foreground)] shrink-0">{p.count} sess.</span>
                {p.cost > 0 && <span className="text-[11px] text-[var(--muted-foreground)] shrink-0">${p.cost.toFixed(2)}</span>}
              </button>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
