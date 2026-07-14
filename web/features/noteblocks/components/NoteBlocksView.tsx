"use client";

import { useCallback, useEffect, useState } from "react";
import { NoteEditor } from "./Editor/NoteEditor";
import { TerminalPane } from "./Terminal/TerminalPane";
import { LevelingModal } from "./LevelingModal";
import { VideoPane } from "./VideoPane";

interface NoteBlocksViewProps {
  noteId?: string;
}

export function NoteBlocksView({ noteId: externalNoteId }: NoteBlocksViewProps) {
  const [leftPanel, setLeftPanel] = useState<"terminal" | "video" | "agent" | null>(null);
  const [syncing, setSyncing] = useState(false);
  const [showLeveling, setShowLeveling] = useState(!externalNoteId);
  const [level, setLevel] = useState<string | null>(null);
  const [noteId, setNoteId] = useState<string | undefined>(externalNoteId);

  const handleLevelComplete = useCallback(async (selectedLevel: string, _customDescription: string) => {
    setLevel(selectedLevel);
    setShowLeveling(false);
    if (noteId) {
      try {
        await fetch(`/api/v1/noteblocks/agent/leveling/answer`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ note_id: noteId, level: selectedLevel, topic: "" }),
        });
      } catch {
        // ignore
      }
    }
  }, [noteId]);

  const handleLevelSkip = useCallback(() => {
    setShowLeveling(false);
  }, []);

  const handleSync = async () => {
    if (!noteId || syncing) return;
    setSyncing(true);
    try {
      const res = await fetch(`/api/v1/noteblocks/agent/sync-to-notion/${noteId}`, {
        method: "POST",
      });
      const data = await res.json();
      if (data.success) {
        alert(`Synced to Notion: ${data.url}`);
      } else {
        alert(`Sync failed: ${data.error}`);
      }
    } catch {
      alert("Sync error");
    } finally {
      setSyncing(false);
    }
  };

  return (
    <div className="flex h-full w-full bg-[#0a0a0a] text-gray-100">
      {showLeveling && (
        <LevelingModal
          topic="este assunto"
          onComplete={handleLevelComplete}
          onSkip={handleLevelSkip}
        />
      )}

      {leftPanel && (
        <div className="flex flex-col border-r border-[#1a1a1a] w-1/2">
          <div className="flex items-center gap-1 px-2 py-1 text-xs text-gray-400 border-b border-[#1a1a1a]">
            <button
              onClick={() => setLeftPanel("terminal")}
              className={`px-2 py-0.5 rounded ${leftPanel === "terminal" ? "bg-[#1a1a1a] text-gray-100" : "hover:text-gray-200"}`}
            >
              Terminal
            </button>
            <button
              onClick={() => setLeftPanel("video")}
              className={`px-2 py-0.5 rounded ${leftPanel === "video" ? "bg-[#1a1a1a] text-gray-100" : "hover:text-gray-200"}`}
            >
              Video
            </button>
            <button
              onClick={() => setLeftPanel("agent")}
              className={`px-2 py-0.5 rounded ${leftPanel === "agent" ? "bg-[#1a1a1a] text-gray-100" : "hover:text-gray-200"}`}
            >
              Agent
            </button>
            <button
              onClick={() => setLeftPanel(null)}
              className="ml-auto px-2 py-0.5 text-gray-400 hover:text-gray-200"
            >
              Hide
            </button>
          </div>
          <div className="flex-1 min-h-0">
            {leftPanel === "terminal" && <TerminalPane />}
            {leftPanel === "video" && <VideoPane />}
            {leftPanel === "agent" && (
              <div className="p-4 text-gray-300 text-sm">Agent output will appear here</div>
            )}
          </div>
        </div>
      )}

      <div className="flex flex-col flex-1 min-w-0 relative">
        <div className="absolute top-2 right-2 z-10 flex items-center gap-2">
          {noteId && (
            <button
              onClick={handleSync}
              disabled={syncing}
              className="px-2 py-1 text-xs text-gray-300 hover:text-gray-100 bg-[#0a0a0a]/80 rounded border border-[#1a1a1a] disabled:opacity-40"
            >
              {syncing ? "..." : "sync notion"}
            </button>
          )}
          <button
            onClick={() => setLeftPanel(leftPanel ? null : "terminal")}
            className="px-2 py-1 text-xs text-gray-400 hover:text-gray-200 bg-[#0a0a0a]/80 rounded border border-[#1a1a1a]"
          >
            {leftPanel ? "Full" : "Split"}
          </button>
        </div>
        <NoteEditor noteId={noteId} />
      </div>
    </div>
  );
}
