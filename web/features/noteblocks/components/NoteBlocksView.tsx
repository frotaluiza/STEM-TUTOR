"use client";

import { useCallback, useEffect, useState } from "react";
import { FileText, MessageSquare, Terminal } from "lucide-react";
import { NoteEditor } from "./Editor/NoteEditor";
import { TerminalPane } from "./Terminal/TerminalPane";
import { LevelingModal } from "./LevelingModal";
import SessionViewer from "@/components/pm/SessionViewer";
import type { Note } from "../types";

interface NoteBlocksViewProps {
  noteId?: string;
}

type ViewTab = "note" | "terminal";

export function NoteBlocksView({ noteId: externalNoteId }: NoteBlocksViewProps) {
  const [note, setNote] = useState<Note | null>(null);
  const [activeTab, setActiveTab] = useState<ViewTab>("note");
  const [showLeveling, setShowLeveling] = useState(!externalNoteId);
  const [level, setLevel] = useState<string | null>(null);
  const [navNoteId, setNavNoteId] = useState<string | undefined>(externalNoteId);

  const hasSession = !!(note?.session);

  // Load note metadata from API
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
    if (navNoteId) {
      try {
        await fetch(`/api/v1/noteblocks/agent/leveling/answer`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ note_id: navNoteId, level: selectedLevel, topic: "" }),
        });
      } catch {}
    }
  }, [navNoteId]);

  const handleLevelSkip = useCallback(() => setShowLeveling(false), []);

  const tabs: { id: ViewTab; label: string; icon: typeof FileText }[] = [
    { id: "note", label: "Nota", icon: FileText },
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

          {/* Session badge */}
          {hasSession && (
            <a
              href={`/session-viewer/${note!.session}`}
              className="ml-auto flex items-center gap-1.5 px-2.5 py-1 text-[11px] text-cyan-400/70 hover:text-cyan-300 rounded border border-[#1a1a1a] hover:bg-[#151515] transition-colors"
              title="Ver sessão completa"
            >
              <MessageSquare size={11} strokeWidth={1.8} />
              Sessão: {note!.session}
            </a>
          )}
        </div>

        {/* Content */}
        <div className="flex-1 min-h-0">
          {activeTab === "note" && <NoteEditor noteId={externalNoteId} />}
          {activeTab === "terminal" && <TerminalPane />}
        </div>
      </div>
    </div>
  );
}
