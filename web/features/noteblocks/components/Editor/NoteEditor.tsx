"use client";

import { useState, useCallback, useRef, useEffect } from "react";
import type { Block, Note, BlockType, BlockOrigin } from "../../types";
import { BLOCK_ORIGIN_LABELS } from "../../types";
import { QuestionBlock } from "./QuestionBlock";
import { MarkdownBlock } from "./MarkdownBlock";

const STORAGE_KEY = "noteblocks_note";
const SAVE_DELAY = 1500;

const PROJECTS = [
  { slug: "ai-stem-tutor", name: "AI STEM Tutor — DeepTutor", icon: "🤖" },
  { slug: "tcc", name: "TCC — Ingrid (MD/Desalination)", icon: "📄" },
  { slug: "notion-infra", name: "Notion Infrastructure", icon: "🗂️" },
  { slug: "pinns", name: "PINNs", icon: "🧮" },
  { slug: "luc-repport", name: "Luc-Repport", icon: "📊" },
  { slug: "", name: "Sessão avulsa (sem projeto)", icon: "📝" },
];

const MODULES: Record<string, { slug: string; name: string }[]> = {
  "ai-stem-tutor": [
    { slug: "grade-eletrica", name: "Grade da Elétrica" },
    { slug: "note-blocks", name: "NoteBlocks" },
    { slug: "mind-map", name: "Mind Map" },
    { slug: "mastery-path", name: "Mastery Path" },
    { slug: "geral", name: "Geral" },
  ],
  tcc: [
    { slug: "modelagem-0d", name: "Modelagem 0D" },
    { slug: "pinns", name: "PINNs" },
    { slug: "slides", name: "Slides" },
    { slug: "geral", name: "Geral" },
  ],
};

interface NoteEditorProps {
  noteId?: string;
}

function emptyNote(): Note {
  return {
    id: `note_${Date.now()}`,
    title: "",
    blocks: [{ id: `b${Date.now()}`, type: "text", origin: "human", content: "" }],
    tags: [],
    created: new Date().toISOString(),
    updated: new Date().toISOString(),
  };
}

function loadFromStorage(): Note | null {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    return JSON.parse(raw) as Note;
  } catch { return null; }
}

function saveToStorage(note: Note) {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(note)); } catch { }
}

function noteToMarkdown(note: Note): string {
  const lines: string[] = [];
  lines.push("---");
  lines.push(`title: "${note.title}"`);
  lines.push(`project: ${note.project || ""}`);
  if (note.module) lines.push(`module: ${note.module}`);
  if (note.node) lines.push(`node: ${note.node}`);
  lines.push(`created: ${note.created}`);
  lines.push(`updated: ${note.updated}`);
  lines.push("---");
  lines.push("");
  for (const block of note.blocks) {
    if (block.origin === "human" || block.pinned) {
      if (block.type === "heading") {
        lines.push(`## ${block.content}`);
      } else if (block.type === "command") {
        lines.push("```bash");
        lines.push(block.content);
        lines.push("```");
      } else if (block.type === "output") {
        lines.push("```");
        lines.push(block.content);
        lines.push("```");
      } else {
        lines.push(block.content);
      }
      lines.push("");
    }
  }
  return lines.join("\n");
}

export function NoteEditor({ noteId }: NoteEditorProps) {
  const [note, setNote] = useState<Note>(() => loadFromStorage() ?? emptyNote());
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [assistPrompt, setAssistPrompt] = useState("");
  const [showAssist, setShowAssist] = useState(false);
  const [saveStatus, setSaveStatus] = useState<"saved" | "saving" | "unsaved">("saved");
  const [showProjectPicker, setShowProjectPicker] = useState(false);
  const [showExportMenu, setShowExportMenu] = useState(false);
  const titleRef = useRef<HTMLInputElement>(null);
  const saveTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const markChanged = useCallback(() => {
    setSaveStatus("unsaved");
    if (saveTimerRef.current) clearTimeout(saveTimerRef.current);
    saveTimerRef.current = setTimeout(() => {
      setNote((prev) => {
        const updated = { ...prev, updated: new Date().toISOString() };
        saveToStorage(updated);
        setSaveStatus("saved");
        return updated;
      });
    }, SAVE_DELAY);
  }, []);

  const setProject = useCallback((slug: string) => {
    setNote((prev) => ({ ...prev, project: slug || undefined, module: undefined, node: undefined }));
    markChanged();
    setShowProjectPicker(false);
  }, [markChanged]);

  const setModule = useCallback((mod: string) => {
    setNote((prev) => ({ ...prev, module: mod || undefined, node: undefined }));
    markChanged();
  }, [markChanged]);

  const updateTitle = useCallback((title: string) => {
    setNote((prev) => ({ ...prev, title }));
    markChanged();
  }, [markChanged]);

  const updateBlock = useCallback((blockId: string, content: string) => {
    setNote((prev) => ({
      ...prev,
      blocks: prev.blocks.map((b) => b.id === blockId ? { ...b, content } : b),
    }));
    markChanged();
  }, [markChanged]);

  const toggleSelect = useCallback((blockId: string) => {
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(blockId)) next.delete(blockId);
      else next.add(blockId);
      return next;
    });
  }, []);

  const addBlock = useCallback((type: BlockType = "text", origin: BlockOrigin = "human") => {
    setNote((prev) => ({
      ...prev,
      blocks: [
        ...prev.blocks,
        { id: `b${Date.now()}`, type, origin, content: "", collapsed: origin !== "human" },
      ],
    }));
    markChanged();
  }, [markChanged]);

  const toggleCollapse = useCallback((blockId: string) => {
    setNote((prev) => ({
      ...prev,
      blocks: prev.blocks.map((b) => b.id === blockId ? { ...b, collapsed: !b.collapsed } : b),
    }));
    markChanged();
  }, [markChanged]);

  const togglePin = useCallback((blockId: string) => {
    setNote((prev) => ({
      ...prev,
      blocks: prev.blocks.map((b) => b.id === blockId ? { ...b, pinned: !b.pinned } : b),
    }));
    markChanged();
  }, [markChanged]);

  const runAsk = useCallback((blockId: string) => {
    const block = note.blocks.find((b) => b.id === blockId);
    if (!block || !block.content.trim()) return;
    setNote((prev) => ({
      ...prev,
      blocks: prev.blocks.map((b) =>
        b.id === blockId ? { ...b, type: "output", content: `[Agent would process: "${b.content}"]` } : b
      ),
    }));
    markChanged();
  }, [note.blocks, markChanged]);

  const assistEdit = useCallback(() => {
    if (!assistPrompt.trim() || selected.size === 0) return;
    setNote((prev) => ({
      ...prev,
      blocks: prev.blocks.map((b) =>
        selected.has(b.id) ? { ...b, content: `${b.content}\n\n[Assist: ${assistPrompt}]` } : b
      ),
    }));
    setShowAssist(false);
    setAssistPrompt("");
    setSelected(new Set());
    markChanged();
  }, [assistPrompt, selected, markChanged]);

  const handleQuestionAnswer = useCallback((blockId: string, answer: string) => {
    setNote((prev) => ({
      ...prev,
      blocks: prev.blocks.map((b) =>
        b.id === blockId ? { ...b, type: "output" as BlockType, content: `[Respondido] ${answer}` } : b
      ),
    }));
    markChanged();
  }, [markChanged]);

  const handleExport = useCallback((mode: "clean" | "full") => {
    const md = mode === "clean"
      ? noteToMarkdown(note)
      : JSON.stringify(note, null, 2);
    const blob = new Blob([md], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${note.title || "nota"}.${mode === "clean" ? "md" : "json"}`;
    a.click();
    URL.revokeObjectURL(url);
    setShowExportMenu(false);
  }, [note]);

  const handleNewNote = useCallback(() => {
    const fresh = emptyNote();
    setNote(fresh);
    saveToStorage(fresh);
    setSaveStatus("saved");
    setSelected(new Set());
    titleRef.current?.focus();
  }, []);

  // Load note from API when noteId is provided
  useEffect(() => {
    if (!noteId) return;
    let cancelled = false;
    fetch(`/api/v1/noteblocks/notes/${noteId}`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((data: Note) => {
        if (!cancelled) {
          setNote(data);
          saveToStorage(data);
          setSaveStatus("saved");
        }
      })
      .catch(() => {});
    return () => { cancelled = true; };
  }, [noteId]);

  // Auto-save on page unload
  useEffect(() => {
    const handleBeforeUnload = () => { saveToStorage(note); };
    window.addEventListener("beforeunload", handleBeforeUnload);
    return () => window.removeEventListener("beforeunload", handleBeforeUnload);
  }, [note]);

  const curProject = PROJECTS.find((p) => p.slug === note.project);
  const availableModules = note.project ? MODULES[note.project] : undefined;
  const saveIcon = saveStatus === "saved" ? "✓" : saveStatus === "saving" ? "⋯" : "○";
  const saveColor = saveStatus === "saved" ? "text-green-500" : "text-yellow-500";

  return (
    <div className="flex flex-col h-full overflow-y-auto">
      {/* Project context bar */}
      <div className="sticky top-0 z-20 bg-[#0a0a0a]/95 backdrop-blur-md border-b border-[#1a1a1a] px-8 py-2">
        <div className="flex items-center gap-3 flex-wrap text-xs">
          {/* Project picker */}
          <div className="relative">
            <button
              onClick={() => setShowProjectPicker(!showProjectPicker)}
              className="flex items-center gap-1.5 px-2 py-1 rounded hover:bg-[#151515] text-gray-400 hover:text-gray-200"
            >
              <span>{curProject ? curProject.icon : "📁"}</span>
              <span>{curProject ? curProject.name : "Projeto: (nenhum)"}</span>
              <span className="text-gray-600">▼</span>
            </button>
            {showProjectPicker && (
              <>
                <div className="fixed inset-0 z-10" onClick={() => setShowProjectPicker(false)} />
                <div className="absolute top-full left-0 mt-1 z-20 bg-[#0a0a0a]/95 backdrop-blur-md border border-[#333] rounded-lg shadow-xl py-1 min-w-[240px]">
                  {PROJECTS.map((p) => (
                    <button
                      key={p.slug || "__avulsa"}
                      onClick={() => setProject(p.slug)}
                      className={`flex items-center gap-2 w-full px-3 py-1.5 text-left hover:bg-[#1a1a1a] ${
                        note.project === p.slug ? "text-gray-100" : "text-gray-400"
                      }`}
                    >
                      <span>{p.icon}</span>
                      <span>{p.name}</span>
                      {note.project === p.slug && <span className="ml-auto text-[10px] text-green-500">●</span>}
                    </button>
                  ))}
                </div>
              </>
            )}
          </div>

          {/* Module picker (only when project selected) */}
          {note.project && availableModules && (
            <>
              <span className="text-gray-700">/</span>
              <select
                value={note.module || ""}
                onChange={(e) => setModule(e.target.value)}
                className="bg-transparent text-gray-400 hover:text-gray-200 outline-none cursor-pointer"
              >
                <option value="">Módulo: (nenhum)</option>
                {availableModules.map((m) => (
                  <option key={m.slug} value={m.slug}>{m.name}</option>
                ))}
              </select>
            </>
          )}

          <span className="flex-1" />

          {/* Save status */}
          <span className={`${saveColor} font-mono`}>{saveIcon}</span>

          {/* New note */}
          <button onClick={handleNewNote} className="text-gray-500 hover:text-gray-300 px-1.5">+</button>

          {/* Export */}
          <div className="relative">
            <button
              onClick={() => setShowExportMenu(!showExportMenu)}
              className="text-gray-500 hover:text-gray-300 px-1.5"
              title="Exportar"
            >
              💾
            </button>
            {showExportMenu && (
              <>
                <div className="fixed inset-0 z-10" onClick={() => setShowExportMenu(false)} />
                <div className="absolute right-0 top-full mt-1 z-20 bg-[#0a0a0a]/95 backdrop-blur-md border border-[#333] rounded-lg shadow-xl py-1 min-w-[160px]">
                  <button onClick={() => handleExport("clean")} className="block w-full text-left px-3 py-1.5 text-xs text-gray-400 hover:text-gray-200 hover:bg-[#1a1a1a]">
                    📄 Exportar .md (limpo)
                  </button>
                  <button onClick={() => handleExport("full")} className="block w-full text-left px-3 py-1.5 text-xs text-gray-400 hover:text-gray-200 hover:bg-[#1a1a1a]">
                    📦 Exportar .json (completo)
                  </button>
                  <button
                    onClick={() => { navigator.clipboard.writeText(noteToMarkdown(note)); setShowExportMenu(false); }}
                    className="block w-full text-left px-3 py-1.5 text-xs text-gray-400 hover:text-gray-200 hover:bg-[#1a1a1a]"
                  >
                    📋 Copiar .md
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      </div>

      {/* Title */}
      <div className="px-8 py-4 pb-2">
        <input
          ref={titleRef}
          value={note.title}
          onChange={(e) => updateTitle(e.target.value)}
          className="w-full bg-transparent text-2xl font-semibold text-gray-100 outline-none placeholder-gray-700"
          placeholder="Título da anotação..."
        />
      </div>

      {/* Blocks */}
      <div className="flex-1 px-8 pb-32 space-y-1">
        {note.blocks.map((block) => {
          const originLabel = BLOCK_ORIGIN_LABELS[block.origin];
          const isBot = block.origin !== "human";

          return (
            <div key={block.id} className="group">
              {isBot && (
                <div
                  onClick={() => toggleCollapse(block.id)}
                  className="flex items-center gap-2 px-2 py-1 mt-2 mb-1 cursor-pointer rounded hover:bg-[#151515] select-none"
                >
                  <span className="text-xs text-gray-600">{block.collapsed ? "▶" : "▼"}</span>
                  <span className={`text-xs font-mono ${originLabel.color}`}>
                    {originLabel.icon} {originLabel.label}
                  </span>
                  <span className="text-[10px] text-gray-600 flex-1">
                    {block.collapsed ? "(clique para expandir)" : ""}
                  </span>
                  {block.pinned && <span className="text-[10px] text-yellow-500">📌</span>}
                </div>
              )}

              <div
                className={`flex gap-2 py-1 rounded transition-opacity duration-100 ${
                  isBot && block.collapsed ? "hidden" : ""
                } ${selected.has(block.id) ? "bg-[#151515]" : ""}`}
              >
                <div className="flex flex-col items-center pt-2 opacity-0 group-hover:opacity-40 transition-opacity">
                  <input
                    type="checkbox"
                    checked={selected.has(block.id)}
                    onChange={() => toggleSelect(block.id)}
                    className="w-3 h-3 cursor-pointer accent-[#00ff80]"
                  />
                  <span onClick={() => addBlock("text")} className="text-xs text-gray-700 cursor-pointer hover:text-gray-300 mt-1">+</span>
                </div>

                {!isBot && (
                  <div className="flex items-start pt-2 shrink-0">
                    <span className={`text-xs font-mono ${originLabel.color}`}>{originLabel.icon}</span>
                  </div>
                )}

                <div className="flex-1 min-w-0">
                  {block.type === "heading" ? (
                    <input value={block.content} onChange={(e) => updateBlock(block.id, e.target.value)}
                      className="w-full bg-transparent text-lg font-semibold text-gray-100 outline-none" placeholder="Heading" />
                  ) : block.type === "ask" ? (
                    <div className="flex items-start gap-2">
                      <span className="text-[#00ff80] text-sm font-mono mt-1 shrink-0">@</span>
                      <div className="flex-1">
                        <input value={block.content} onChange={(e) => updateBlock(block.id, e.target.value)}
                          className="w-full bg-transparent text-sm text-[#00ff80] outline-none placeholder-[#00ff80]/30 font-mono" placeholder="Ask the agent..." />
                        {block.content.trim() && (
                          <button onClick={() => runAsk(block.id)}
                            className="mt-1 px-2 py-0.5 text-xs text-[#00ff80]/60 border border-[#00ff80]/20 rounded hover:bg-[#00ff80]/5">▶ Run</button>
                        )}
                      </div>
                    </div>
                  ) : block.type === "command" ? (
                    <div className="flex items-center gap-2">
                      <span className="text-yellow-500 text-sm font-mono mt-1 shrink-0">$</span>
                      <input value={block.content} onChange={(e) => updateBlock(block.id, e.target.value)}
                        className="w-full bg-transparent text-sm text-yellow-400/80 outline-none placeholder-yellow-400/30 font-mono" placeholder="command..." />
                    </div>
                  ) : block.type === "output" ? (
                    <pre className="text-sm text-white/90 whitespace-pre-wrap bg-[#0d0d0d] p-3 rounded border border-[#1a1a1a]">
                      {block.content || "No output yet"}
                    </pre>
                  ) : block.type === "question" ? (
                    <QuestionBlock block={block} onAnswer={handleQuestionAnswer} />
                  ) : block.type === "markdown" ? (
                    <MarkdownBlock content={block.content} onChange={(c) => updateBlock(block.id, c)} />
                  ) : (
                    <textarea value={block.content} onChange={(e) => updateBlock(block.id, e.target.value)}
                      className="w-full bg-transparent text-sm text-gray-300 outline-none resize-none placeholder-gray-700 min-h-[1.5em]"
                      placeholder="Type something..." rows={Math.max(1, (block.content.match(/\n/g) || []).length + 1)} />
                  )}

                  {isBot && (
                    <div className="mt-1 opacity-0 group-hover:opacity-100 transition-opacity">
                      <button onClick={() => togglePin(block.id)}
                        className={`text-[10px] px-1.5 py-0.5 rounded ${block.pinned ? "text-yellow-500 bg-yellow-500/10" : "text-gray-600 hover:text-gray-400"}`}>
                        {block.pinned ? "📌 Fixado" : "📌 Fixar"}
                      </button>
                    </div>
                  )}
                </div>
              </div>
            </div>
          );
        })}

        <div className="flex gap-2 pt-3 flex-wrap">
          <button onClick={() => addBlock("text")} className="text-xs text-gray-400 hover:text-gray-200 px-2 py-1 rounded hover:bg-[#151515]">+ text</button>
          <button onClick={() => addBlock("heading")} className="text-xs text-gray-400 hover:text-gray-200 px-2 py-1 rounded hover:bg-[#151515]">+ heading</button>
          <button onClick={() => addBlock("ask")} className="text-xs text-gray-400 hover:text-gray-200 px-2 py-1 rounded hover:bg-[#151515]">+ @ask</button>
          <button onClick={() => addBlock("command")} className="text-xs text-gray-400 hover:text-gray-200 px-2 py-1 rounded hover:bg-[#151515]">+ /command</button>
          <button onClick={() => addBlock("markdown")} className="text-xs text-purple-400 hover:text-purple-300 px-2 py-1 rounded hover:bg-purple-500/10">+ **md**</button>
          <span className="w-px h-4 bg-[#222] mx-1 self-center" />
          <button onClick={() => addBlock("text", "opencode")} className="text-xs text-cyan-500 hover:text-cyan-300 px-2 py-1 rounded hover:bg-cyan-500/10">+ 🤖 opencode</button>
          <button onClick={() => addBlock("text", "tutor")} className="text-xs text-emerald-500 hover:text-emerald-300 px-2 py-1 rounded hover:bg-emerald-500/10">+ 🎓 Tutor</button>
        </div>
      </div>

      {selected.size > 0 && (
        <div className="fixed bottom-4 left-1/2 -translate-x-1/2 z-50 flex items-center gap-2 bg-[#0a0a0a]/90 backdrop-blur-md border border-[#333] rounded-lg px-3 py-2 shadow-xl">
          <span className="text-xs text-gray-300">{selected.size} block(s)</span>
          <button onClick={() => setShowAssist(true)} className="px-3 py-1 text-xs bg-[#00ff80]/10 text-[#00ff80] border border-[#00ff80]/20 rounded hover:bg-[#00ff80]/20">✏️ Assist</button>
          <button onClick={() => setSelected(new Set())} className="px-2 py-1 text-xs text-gray-400 hover:text-gray-200">Clear</button>
        </div>
      )}

      {showAssist && (
        <div className="fixed inset-0 bg-black/80 flex items-center justify-center z-[100]">
          <div className="bg-[#111] border border-[#222] rounded-lg p-4 w-96 shadow-2xl">
            <div className="text-sm text-gray-100 mb-2">Assistant Edit</div>
            <textarea value={assistPrompt} onChange={(e) => setAssistPrompt(e.target.value)}
              placeholder="Describe what to do with the selected blocks..."
              className="w-full bg-[#0a0a0a] text-sm text-gray-300 border border-[#222] rounded p-2 outline-none resize-none h-20 placeholder-gray-700" />
            <div className="flex justify-end gap-2 mt-2">
              <button onClick={() => setShowAssist(false)} className="px-3 py-1 text-xs text-gray-400 hover:text-gray-200">Cancel</button>
              <button onClick={assistEdit} className="px-3 py-1 text-xs bg-[#00ff80]/10 text-[#00ff80] border border-[#00ff80]/20 rounded hover:bg-[#00ff80]/20">Apply</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
