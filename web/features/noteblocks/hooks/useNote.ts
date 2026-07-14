"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { Block, Note } from "../types";

interface UseNoteOptions {
  noteId: string;
}

function emptyNote(): Note {
  return {
    id: "",
    title: "Untitled",
    blocks: [{ id: "b1", type: "text", content: "" }],
    tags: [],
    created: new Date().toISOString(),
    updated: new Date().toISOString(),
  };
}

export function useNote({ noteId }: UseNoteOptions) {
  const [note, setNote] = useState<Note>(emptyNote);
  const [connected, setConnected] = useState(false);
  const wsRef = useRef<WebSocket | null>(null);
  const pendingRef = useRef<Block[]>([]);

  useEffect(() => {
    const apiBase = process.env.NEXT_PUBLIC_API_BASE || `http://${window.location.host}`;
    const wsBase = apiBase.replace(/^http/, "ws");
    const url = `${wsBase}/api/v1/noteblocks/ws/${noteId}`;

    const ws = new WebSocket(url);
    wsRef.current = ws;

    ws.onopen = () => {
      setConnected(true);
      ws.send(JSON.stringify({ action: "load" }));

      if (pendingRef.current.length > 0) {
        ws.send(
          JSON.stringify({ action: "update", blocks: pendingRef.current })
        );
        pendingRef.current = [];
      }
    };

    ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        if (data.action === "loaded" && data.note) {
          setNote(data.note);
        } else if (data.action === "synced") {
          setNote((prev) => ({
            ...prev,
            blocks: prev.blocks.map(
              (b) =>
                data.blocks.find((u: Block) => u.id === b.id) ?? b
            ),
          }));
        }
      } catch {
        // ignore parse errors
      }
    };

    ws.onclose = () => setConnected(false);

    return () => {
      ws.close();
    };
  }, [noteId]);

  const updateBlock = useCallback(
    (blockId: string, content: string) => {
      setNote((prev) => {
        const updated: Note = {
          ...prev,
          updated: new Date().toISOString(),
          blocks: prev.blocks.map((b) =>
            b.id === blockId ? { ...b, content } : b
          ),
        };
        return updated;
      });

      const msg = JSON.stringify({
        action: "update",
        blocks: [{ id: blockId, content }],
      });

      if (wsRef.current?.readyState === WebSocket.OPEN) {
        wsRef.current.send(msg);
      } else {
        pendingRef.current.push({ id: blockId, type: "text", content });
      }
    },
    []
  );

  const addBlock = useCallback(
    (type: Block["type"] = "text") => {
      setNote((prev) => ({
        ...prev,
        updated: new Date().toISOString(),
        blocks: [
          ...prev.blocks,
          { id: `b${Date.now()}`, type, content: "" },
        ],
      }));
    },
    []
  );

  const setTitle = useCallback((title: string) => {
    setNote((prev) => ({ ...prev, title, updated: new Date().toISOString() }));
  }, []);

  return { note, connected, updateBlock, addBlock, setTitle };
}
