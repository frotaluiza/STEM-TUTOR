"use client";

import dynamic from "next/dynamic";
import { useCallback, useEffect, useRef, useState } from "react";
import { BookOpen, FileText, Import, Loader2, MessageSquare, Terminal } from "lucide-react";
import { NoteEditor } from "./Editor/NoteEditor";
import { TerminalPane } from "./Terminal/TerminalPane";
import { LevelingModal } from "./LevelingModal";
import SessionViewer from "@/components/pm/SessionViewer";
import type { Note } from "../types";

const MarkdownRenderer = dynamic(() => import("@/components/common/MarkdownRenderer"), { ssr: false });

interface NoteBlocksViewProps {
  noteId?: string;
}

type ViewTab = "note" | "terminal" | "live-doc";

function LiveDocPanel({ sessionSlug }: { sessionSlug: string }) {
  const [content, setContent] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [importing, setImporting] = useState(false);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    fetch(`/api/v1/pm/sessions/${sessionSlug}/live-doc`)
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
  }, [sessionSlug]);

  const handleImport = useCallback(async () => {
    if (!content || importing) return;
    setImporting(true);
    try {
      // Use the built-in browser clipboard API to copy the markdown
      // Then navigate to the note tab for the user to paste
      await navigator.clipboard.writeText(content);
      alert("Conteudo copiado! Va na aba Nota e cole (Ctrl+V) como um bloco markdown.");
    } catch {
      // Fallback: create a new note from the session
      const res = await fetch(`/api/v1/pm/sessions/${sessionSlug}/to-note`, { method: "POST" });
      if (res.ok) {
        const data = await res.json();
        window.location.href = `/noteblocks?noteId=${data.note_id}`;
      }
    } finally {
      setImporting(false);
    }
  }, [content, importing, sessionSlug]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full text-gray-500">
        <Loader2 className="w-4 h-4 animate-spin mr-2" />
        Carregando live doc...
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-full text-gray-500">
        <p className="text-red-400">Erro: {error}</p>
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col">
      {/* Toolbar */}
      <div className="flex shrink-0 items-center gap-2 px-4 py-2 border-b border-[#1a1a1a] bg-[#0d0d0d]">
        <span className="text-xs text-gray-500 font-mono">{sessionSlug}.md</span>
        <span className="text-[10px] text-gray-600">{(content?.length || 0).toLocaleString()} bytes</span>
        <div className="flex-1" />
        <button
          type="button"
          onClick={handleImport}
          disabled={importing}
          className="flex items-center gap-1.5 px-2.5 py-1 text-[11px] text-gray-300 hover:text-gray-100 bg-[#1a1a1a] rounded border border-[#333] hover:bg-[#222] transition-colors disabled:opacity-40"
        >
          <Import size={11} strokeWidth={1.8} />
          {importing ? "Copiando..." : "Importar para nota"}
        </button>
      </div>

      {/* Rendered markdown */}
      <div className="flex-1 overflow-y-auto px-6 py-4">
        <MarkdownRenderer content={content || ""} variant="prose" />
      </div>
    </div>
  );
}

export function NoteBlocksView({ noteId: externalNoteId }: NoteBlocksViewProps) {
  const [note, setNote] = useState<Note | null>(null);
  const [activeTab, setActiveTab] = useState<ViewTab>("note");
  const [showLeveling, setShowLeveling] = useState(!externalNoteId);
  const [level, setLevel] = useState<string | null>(null);

  const hasSession = !!(note?.session);

  useEffect(() => {
    if (!externalNoteId) return;
    fetch(`/api/v1/noteblocks/notes/${externalNoteId}`)
      .then((r) => r.ok ? r.json() : null)
      .then((data: Note | null) => {
        if (data) setNote(data);
      })
      .catch(() => {});
  }, [externalNoteId]);

  const handleLevelComplete = useCallback(async (selectedLevel: string) => {
    setLevel(selectedLevel);
    setShowLeveling(false);
    if (note?.id) {
      try {
        await fetch(`/api/v1/noteblocks/agent/leveling/answer`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ note_id: note.id, level: selectedLevel, topic: "" }),
        });
      } catch {}
    }
  }, [note]);

  const handleLevelSkip = useCallback(() => setShowLeveling(false), []);

  const tabs: { id: ViewTab; label: string; icon: typeof FileText }[] = [
    { id: "note", label: "Nota", icon: FileText },
    ...(hasSession ? [{ id: "live-doc" as ViewTab, label: "Live Doc", icon: BookOpen }] : []),
    { id: "terminal", label: "Terminal", icon: Terminal },
  ];

  return (
    <div className="flex h-full w-full bg-[#0a0a0a] text-gray-100">
      {showLeveling && (
        <LevelingModal
          topic="este assunto"
          onComplete={(l) => handleLevelComplete(l)}
          onSkip={handleLevelSkip}
        />
      )}

      <div className="flex flex-col flex-1 min-w-0">
        {/* Tab bar */}
        <div className="flex shrink-0 items-center gap-0.5 border-b border-[#1a1a1a] bg-[#0d0d0d] px-3 pt-1.5">
          {tabs.map((t) => (
            <button
              key={t.id}
              type="button"
              onClick={() => setActiveTab(t.id)}
              className={`flex items-center gap-1.5 px-3 py-1.5 text-[11.5px] font-medium rounded-t-md transition-colors ${
                activeTab === t.id
                  ? "bg-[#0a0a0a] text-gray-100 border border-[#1a1a1a] border-b-transparent"
                  : "text-gray-500 hover:text-gray-300 hover:bg-[#151515]"
              }`}
            >
              <t.icon size={12} strokeWidth={1.8} />
              {t.label}
            </button>
          ))}

          {hasSession && (
            <a
              href={`/session-viewer/${note!.session}`}
              className="ml-auto flex items-center gap-1.5 px-2.5 py-1 text-[11px] text-cyan-400/70 hover:text-cyan-300 rounded border border-[#1a1a1a] hover:bg-[#151515] transition-colors"
              title="Ver sessão completa"
            >
              <MessageSquare size={11} strokeWidth={1.8} />
              {note!.session}
            </a>
          )}
        </div>

        {/* Content */}
        <div className="flex-1 min-h-0">
          {activeTab === "note" && <NoteEditor noteId={externalNoteId} />}
          {activeTab === "terminal" && <TerminalPane />}
          {activeTab === "live-doc" && note?.session && <LiveDocPanel sessionSlug={note.session} />}
        </div>
      </div>
    </div>
  );
}
