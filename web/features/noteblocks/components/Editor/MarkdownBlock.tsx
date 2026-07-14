"use client";

import dynamic from "next/dynamic";
import { useCallback, useEffect, useRef, useState } from "react";

const MarkdownRenderer = dynamic(() => import("@/components/common/MarkdownRenderer"), { ssr: false });

interface MarkdownBlockProps {
  content: string;
  onChange: (content: string) => void;
}

export function MarkdownBlock({ content, onChange }: MarkdownBlockProps) {
  const [editing, setEditing] = useState(!content.trim());
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const previewRef = useRef<HTMLDivElement>(null);

  const startEdit = useCallback(() => setEditing(true), []);

  const stopEdit = useCallback(() => {
    if (content.trim()) setEditing(false);
  }, [content]);

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      if (e.key === "Escape") {
        e.preventDefault();
        stopEdit();
      }
    },
    [stopEdit],
  );

  useEffect(() => {
    if (editing && textareaRef.current) {
      textareaRef.current.focus();
      textareaRef.current.setSelectionRange(content.length, content.length);
    }
  }, [editing, content.length]);

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [content, editing]);

  if (editing) {
    return (
      <div className="border border-[var(--border)]/30 rounded-lg overflow-hidden bg-[#0d0d0d]">
        <textarea
          ref={textareaRef}
          value={content}
          onChange={(e) => onChange(e.target.value)}
          onBlur={stopEdit}
          onKeyDown={handleKeyDown}
          className="w-full bg-transparent text-sm text-gray-300 outline-none resize-none font-mono p-3 min-h-[80px] placeholder-gray-700"
          placeholder="Write markdown... **bold** `code`"
          spellCheck={false}
        />
        <div className="px-3 pb-2 text-[10px] text-gray-600">
          Esc · sair · ↵ · nova linha
        </div>
      </div>
    );
  }

  return (
    <div
      ref={previewRef}
      onClick={startEdit}
      className="border border-transparent hover:border-[var(--border)]/20 rounded-lg px-3 py-2 -mx-1 cursor-text transition-colors"
    >
      {content.trim() ? (
        <MarkdownRenderer content={content} variant="prose" />
      ) : (
        <p className="text-gray-600 text-sm italic">Clique para escrever markdown...</p>
      )}
    </div>
  );
}
