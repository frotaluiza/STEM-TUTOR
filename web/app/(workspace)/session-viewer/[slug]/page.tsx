"use client";

import dynamic from "next/dynamic";
import { BookOpen, Loader2, MessageSquare, Terminal } from "lucide-react";
import { useEffect, useState } from "react";
import SessionViewer from "@/components/pm/SessionViewer";
import { TerminalPane } from "@/features/noteblocks";

const MarkdownRenderer = dynamic(() => import("@/components/common/MarkdownRenderer"), { ssr: false });

type Tab = "chat" | "terminal" | "live-doc";

function LiveDocPanel({ slug }: { slug: string }) {
  const [content, setContent] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    fetch(`/api/v1/pm/sessions/${slug}/live-doc`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.text();
      })
      .then((text) => {
        if (!cancelled) { setContent(text); setLoading(false); }
      })
      .catch((e) => {
        if (!cancelled) { setError(e.message); setLoading(false); }
      });
    return () => { cancelled = true; };
  }, [slug]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full text-[var(--muted-foreground)]">
        <Loader2 className="w-4 h-4 animate-spin mr-2" />
        Carregando live doc...
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-full text-[var(--muted-foreground)]">
        <p className="text-red-400">Erro: {error}</p>
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col bg-[var(--background)]">
      <div className="flex shrink-0 items-center gap-2 px-4 py-2 border-b border-[var(--border)] bg-[var(--card)]">
        <span className="text-[12px] text-[var(--muted-foreground)] font-mono">{slug}.md</span>
        <span className="text-[10px] text-[var(--muted-foreground)]/50">{(content?.length || 0).toLocaleString()} bytes</span>
      </div>
      <div className="flex-1 overflow-y-auto px-6 py-4">
        <MarkdownRenderer content={content || ""} variant="prose" />
      </div>
    </div>
  );
}

export default function SessionViewerPage({ params }: { params: Promise<{ slug: string }> }) {
  const [slug, setSlug] = useState<string | null>(null);
  const [tab, setTab] = useState<Tab>("chat");

  useEffect(() => { params.then((p) => setSlug(p.slug)); }, [params]);

  if (!slug) {
    return (
      <div className="flex items-center justify-center h-full text-[var(--muted-foreground)] text-sm">
        Carregando...
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex shrink-0 items-center gap-1 border-b border-[var(--border)] bg-[var(--card)] px-3 pt-2">
        <button type="button" onClick={() => setTab("chat")}
          className={`flex items-center gap-1.5 px-3 py-1.5 text-[12px] font-medium rounded-t-md transition-colors ${
            tab === "chat"
              ? "bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] border-b-transparent"
              : "text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)]/30"
          }`}
        >
          <MessageSquare size={13} strokeWidth={1.7} />
          Chat
        </button>
        <button type="button" onClick={() => setTab("live-doc")}
          className={`flex items-center gap-1.5 px-3 py-1.5 text-[12px] font-medium rounded-t-md transition-colors ${
            tab === "live-doc"
              ? "bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] border-b-transparent"
              : "text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)]/30"
          }`}
        >
          <BookOpen size={13} strokeWidth={1.7} />
          Live Doc
        </button>
        <button type="button" onClick={() => setTab("terminal")}
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

      <div className="flex-1 min-h-0">
        {tab === "chat" && <SessionViewer slug={slug} />}
        {tab === "live-doc" && <LiveDocPanel slug={slug} />}
        {tab === "terminal" && <TerminalPane />}
      </div>
    </div>
  );
}
