"use client";

import { useCallback, useEffect, useState } from "react";
import { Loader2 } from "lucide-react";
import { NoteEditor } from "./Editor/NoteEditor";
import { LevelingModal } from "./LevelingModal";
import { WorkspaceLayout } from "./WorkspaceLayout";
import type { Note } from "../types";

interface NoteBlocksViewProps {
  noteId?: string;
  showLevelingOnMount?: boolean;
  sessionMode?: boolean;
  pathId?: string;
}

export function NoteBlocksView({
  noteId: externalNoteId,
  showLevelingOnMount = false,
  sessionMode = false,
  pathId,
}: NoteBlocksViewProps) {
  const [note, setNote] = useState<Note | null>(null);
  const [showLeveling, setShowLeveling] = useState(showLevelingOnMount);
  const [level, setLevel] = useState<string | null>(null);

  const hasSession = !!(note?.session);
  const effectivePathId = pathId || note?.module || undefined;

  useEffect(() => {
    if (!externalNoteId) return;
    fetch(`/api/v1/noteblocks/notes/${externalNoteId}`)
      .then((r) => (r.ok ? r.json() : null))
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

  return (
    <div className="flex h-full w-full bg-[#0a0a0a] text-gray-100">
      {showLeveling && (
        <LevelingModal
          topic="este assunto"
          onComplete={(l) => handleLevelComplete(l)}
          onSkip={handleLevelSkip}
        />
      )}

      <WorkspaceLayout
        sessionMode={sessionMode}
        hasSession={hasSession}
        noteId={externalNoteId}
        pathId={effectivePathId}
        sessionSlug={note?.session}
      />
    </div>
  );
}
