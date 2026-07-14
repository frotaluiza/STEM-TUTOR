"use client";

import { Terminal, MessageSquare } from "lucide-react";
import { useState } from "react";
import SessionViewer from "@/components/pm/SessionViewer";
import { TerminalPane } from "@/features/noteblocks";

type Tab = "chat" | "terminal";

export default function SessionViewerPage({ params }: { params: Promise<{ slug: string }> }) {
  const [slug, setSlug] = useState<string | null>(null);
  const [tab, setTab] = useState<Tab>("chat");

  params.then((p) => setSlug(p.slug));

  if (!slug) {
    return (
      <div className="flex items-center justify-center h-full text-[var(--muted-foreground)] text-sm">
        Carregando...
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full">
      {/* Tab bar */}
      <div className="flex shrink-0 items-center gap-1 border-b border-[var(--border)] bg-[var(--card)] px-3 pt-2">
        <button
          type="button"
          onClick={() => setTab("chat")}
          className={`flex items-center gap-1.5 px-3 py-1.5 text-[12px] font-medium rounded-t-md transition-colors ${
            tab === "chat"
              ? "bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] border-b-transparent"
              : "text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)]/30"
          }`}
        >
          <MessageSquare size={13} strokeWidth={1.7} />
          Chat
        </button>
        <button
          type="button"
          onClick={() => setTab("terminal")}
          className={`flex items-center gap-1.5 px-3 py-1.5 text-[12px] font-medium rounded-t-md transition-colors ${
            tab === "terminal"
              ? "bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] border-b-transparent"
              : "text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)]/30"
          }`}
        >
          <Terminal size={13} strokeWidth={1.7} />
          Terminal
        </button>
      </div>

      {/* Content */}
      <div className="flex-1 min-h-0">
        {tab === "chat" ? <SessionViewer slug={slug} /> : <TerminalPane />}
      </div>
    </div>
  );
}
