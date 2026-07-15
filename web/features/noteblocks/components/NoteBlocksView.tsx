"use client";

<<<<<<< Updated upstream
import { useCallback, useEffect, useState } from "react";
import { Loader2 } from "lucide-react";
=======
import dynamic from "next/dynamic";
import { useCallback, useEffect, useRef, useState } from "react";
import {
  BookOpen, FileText, GraduationCap, Import, Library, Loader2, MessageSquare, Terminal,
} from "lucide-react";
>>>>>>> Stashed changes
import { NoteEditor } from "./Editor/NoteEditor";
import { LevelingModal } from "./LevelingModal";
import { WorkspaceLayout } from "./WorkspaceLayout";
import type { Note } from "../types";

interface NoteBlocksViewProps {
  noteId?: string;
  showLevelingOnMount?: boolean;
<<<<<<< Updated upstream
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
=======
  /** When true, shows Material + Tutor tabs for a mastery path session. */
  sessionMode?: boolean;
  /** The mastery path book_id for loading material and tutor context. */
  pathId?: string;
}

type ViewTab = "note" | "chat" | "artefact" | "material" | "terminal" | "live-doc";

function LiveDocPanel({ sessionSlug }: { sessionSlug: string }) {
  const [content, setContent] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [importing, setImporting] = useState(false);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    fetch(`/api/v1/pm/sessions/${sessionSlug}/live-doc`)
      .then((r) => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.text(); })
      .then((text) => { if (!cancelled) { setContent(text); setLoading(false); } })
      .catch((e) => { if (!cancelled) { setError(e.message); setLoading(false); } });
    return () => { cancelled = true; };
  }, [sessionSlug]);

  const handleImport = useCallback(async () => {
    if (!content || importing) return;
    setImporting(true);
    try {
      await navigator.clipboard.writeText(content);
      alert("Conteudo copiado! Va na aba Nota e cole (Ctrl+V) como um bloco markdown.");
    } catch {
      const res = await fetch(`/api/v1/pm/sessions/${sessionSlug}/to-note`, { method: "POST" });
      if (res.ok) {
        const data = await res.json();
        window.location.href = `/noteblocks?noteId=${data.note_id}`;
      }
    } finally { setImporting(false); }
  }, [content, importing, sessionSlug]);

  if (loading) return <div className="flex items-center justify-center h-full text-gray-500"><Loader2 className="w-4 h-4 animate-spin mr-2" />Carregando live doc...</div>;
  if (error) return <div className="flex flex-col items-center justify-center h-full text-gray-500"><p className="text-red-400">Erro: {error}</p></div>;

  return (
    <div className="h-full flex flex-col">
      <div className="flex shrink-0 items-center gap-2 px-4 py-2 border-b border-[#1a1a1a] bg-[#0d0d0d]">
        <span className="text-xs text-gray-500 font-mono">{sessionSlug}.md</span>
        <span className="text-[10px] text-gray-600">{(content?.length || 0).toLocaleString()} bytes</span>
        <div className="flex-1" />
        <button type="button" onClick={handleImport} disabled={importing}
          className="flex items-center gap-1.5 px-2.5 py-1 text-[11px] text-gray-300 hover:text-gray-100 bg-[#1a1a1a] rounded border border-[#333] hover:bg-[#222] transition-colors disabled:opacity-40">
          <Import size={11} strokeWidth={1.8} />
          {importing ? "Copiando..." : "Importar para nota"}
        </button>
      </div>
      <div className="flex-1 overflow-y-auto px-6 py-4">
        <MarkdownRenderer content={content || ""} variant="prose" />
      </div>
    </div>
  );
}

function MaterialViewer({ pathId }: { pathId?: string }) {
  const [content, setContent] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
>>>>>>> Stashed changes

  useEffect(() => {
    if (!pathId) return;
    fetch(`/api/v1/learning/progress/${encodeURIComponent(pathId)}/material`)
      .then((r) => r.ok ? r.json() : null)
      .then((data) => { if (data?.sections?.length) setContent(data.sections.map((s: any) => s.content).join("\n\n")); setLoading(false); })
      .catch((e) => { setError(e.message); setLoading(false); });
  }, [pathId]);

  if (!pathId) return <div className="flex items-center justify-center h-full text-gray-600 text-xs"><Library className="w-4 h-4 mr-2 opacity-50" />Nenhum material selecionado.</div>;
  if (loading) return <div className="flex items-center justify-center h-full text-gray-600"><Loader2 className="w-4 h-4 animate-spin mr-2" />Carregando...</div>;
  if (error) return <div className="flex items-center justify-center h-full text-red-400 text-xs">{error}</div>;
  if (!content) return <div className="flex items-center justify-center h-full text-gray-600 text-xs">Nenhum material disponivel.</div>;

  return (
    <div className="h-full flex flex-col">
      <div className="flex-1 overflow-y-auto px-6 py-4">
        <MarkdownRenderer content={content} variant="prose" />
      </div>
    </div>
  );
}

function TutorChatSidebar({ pathId }: { pathId?: string }) {
  const [connected, setConnected] = useState(false);
  const [activated, setActivated] = useState(false);
  const [messages, setMessages] = useState<{ role: string; content: string; id: string }[]>([]);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [style, setStyle] = useState<"deeptutor" | "memphis">("deeptutor");
  const wsRef = useRef<WebSocket | null>(null);
  const endRef = useRef<HTMLDivElement | null>(null);
  const sessionIdRef = useRef<string | null>(null);

  useEffect(() => { endRef.current?.scrollIntoView({ behavior: "smooth" }); }, [messages]);

  const connect = useCallback(() => {
    if (wsRef.current) return;
    setActivated(true);
    const ws = new WebSocket(`${window.location.protocol === "https:" ? "wss:" : "ws:"}//${window.location.host}/api/v1/ws`);
    wsRef.current = ws;
    ws.onopen = () => {
      setConnected(true);
      ws.send(JSON.stringify({ action: "start_turn", capability: "mastery_path", content: "Ola tutor!", config: { tutor_style: style, ...(pathId ? { mastery_path_id: pathId } : {}) } }));
    };
    ws.onmessage = (event) => {
      try {
        const d = JSON.parse(event.data);
        if (d.type === "session" && d.metadata?.session_id) sessionIdRef.current = d.metadata.session_id;
        if (d.type === "content") setMessages((p) => [...p, { role: "tutor", content: d.content, id: `t-${Date.now()}` }]);
        if (d.type === "done") setBusy(false);
      } catch {}
    };
    ws.onerror = () => setConnected(false);
    ws.onclose = () => setConnected(false);
  }, [pathId, style]);

  const disconnect = useCallback(() => {
    wsRef.current?.close(); wsRef.current = null; setConnected(false); setActivated(false); setMessages([]);
  }, []);

  const handleSend = useCallback(() => {
    if (!input.trim() || !wsRef.current || busy) return;
    setMessages((p) => [...p, { role: "learner", content: input, id: `l-${Date.now()}` }]);
    wsRef.current.send(JSON.stringify({ action: "start_turn", capability: "mastery_path", content: input, session_id: sessionIdRef.current, config: { tutor_style: style, ...(pathId ? { mastery_path_id: pathId } : {}) } }));
    setInput(""); setBusy(true);
  }, [input, busy, pathId, style]);

  if (!activated) {
    return (
      <div className="flex flex-col h-full bg-[#0a0a0a]">
        <div className="flex items-center gap-2 px-3 py-2 border-b border-[#1a1a1a] bg-[#0d0d0d] shrink-0">
          <GraduationCap className="w-4 h-4 text-emerald-400" />
          <span className="text-xs font-medium text-gray-300">Tutor</span>
        </div>
        <div className="flex-1 flex flex-col items-center justify-center gap-4 px-6">
          <GraduationCap className="w-10 h-10 text-emerald-500/50" />
          <div className="text-center">
            <p className="text-sm text-gray-300 font-medium">Tutor de Estudo</p>
            <p className="text-xs text-gray-600 mt-1">Conecte-se ao tutor para comecar a sessao.</p>
          </div>
          <div className="flex gap-2">
            <button onClick={() => setStyle("deeptutor")} className={`px-3 py-1.5 text-xs rounded-md border ${style === "deeptutor" ? "border-cyan-500/40 text-cyan-300 bg-cyan-500/10" : "border-[#252525] text-gray-500"}`}>DeepTutor</button>
            <button onClick={() => setStyle("memphis")} className={`px-3 py-1.5 text-xs rounded-md border ${style === "memphis" ? "border-emerald-500/40 text-emerald-300 bg-emerald-500/10" : "border-[#252525] text-gray-500"}`}>Memphis EMT</button>
          </div>
          <button onClick={connect} className="flex items-center gap-2 px-4 py-2 text-sm rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white transition-colors">Conectar ao tutor</button>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full bg-[#0a0a0a]">
      <div className="flex items-center gap-2 px-3 py-2 border-b border-[#1a1a1a] bg-[#0d0d0d] shrink-0">
        <GraduationCap className="w-4 h-4 text-emerald-400" />
        <span className="text-xs font-medium text-gray-300">{style === "deeptutor" ? "DeepTutor" : "Tutor Memphis"}</span>
        <button onClick={() => { const n = style === "deeptutor" ? "memphis" : "deeptutor"; setStyle(n); disconnect(); setTimeout(() => connect(), 100); }}
          className="ml-auto flex items-center gap-1 px-1.5 py-0.5 text-[10px] rounded border text-cyan-400 border-cyan-500/30 bg-cyan-500/10">{style === "deeptutor" ? "Memphis" : "DeepTutor"}</button>
        <span className={`w-1.5 h-1.5 rounded-full ${connected ? "bg-emerald-500" : "bg-red-500"}`} />
      </div>
      <div className="flex-1 overflow-y-auto px-3 py-2 space-y-2">
        {messages.map((m) => (
          <div key={m.id} className={`flex gap-2 ${m.role === "learner" ? "flex-row-reverse" : ""}`}>
            <div className={`w-6 h-6 rounded-full flex items-center justify-center text-[10px] ${m.role === "tutor" ? "bg-emerald-500/20 text-emerald-400" : "bg-cyan-500/20 text-cyan-400"}`}>{m.role === "tutor" ? <GraduationCap className="w-3 h-3" /> : <span>👤</span>}</div>
            <div className={`max-w-[80%] rounded-lg px-3 py-1.5 text-xs leading-relaxed ${m.role === "tutor" ? "bg-[#151515] text-gray-200 border border-[#252525]" : "bg-emerald-500/10 text-emerald-100 border border-emerald-500/20"}`}>{m.content}</div>
          </div>
        ))}
        <div ref={endRef} />
      </div>
      <div className="shrink-0 border-t border-[#1a1a1a] p-2">
        <div className="flex gap-1.5">
          <textarea value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); handleSend(); } }}
            placeholder="Responda ao tutor..." rows={1}
            className="flex-1 bg-[#151515] text-xs text-gray-200 placeholder-gray-600 rounded-md px-2.5 py-1.5 border border-[#252525] resize-none outline-none focus:border-emerald-500/40 transition-colors" disabled={busy || !connected} />
          <button onClick={handleSend} disabled={busy || !connected || !input.trim()}
            className="p-1.5 rounded-md bg-emerald-600/20 text-emerald-400 hover:bg-emerald-600/30 disabled:opacity-30 transition-colors">
            {busy ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <MessageSquare className="w-3.5 h-3.5" />}
          </button>
        </div>
      </div>
    </div>
  );
}

export function NoteBlocksView({
  noteId: externalNoteId, showLevelingOnMount = false, sessionMode = false, pathId,
}: NoteBlocksViewProps) {
  const [note, setNote] = useState<Note | null>(null);
  const [activeTab, setActiveTab] = useState<ViewTab>(sessionMode ? "material" : "note");
  const [showLeveling, setShowLeveling] = useState(showLevelingOnMount);
  const hasSession = !!(note?.session);
  const effectivePathId = pathId || note?.module || undefined;

  useEffect(() => {
    if (!externalNoteId) return;
    fetch(`/api/v1/noteblocks/notes/${externalNoteId}`)
<<<<<<< Updated upstream
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
=======
      .then((r) => r.ok ? r.json() : null)
      .then((data: Note | null) => { if (data) setNote(data); })
      .catch(() => {});
  }, [externalNoteId]);

  const allTabs = [
    { id: "note" as ViewTab, label: "Nota", icon: FileText },
    ...(sessionMode || effectivePathId ? [{ id: "material" as ViewTab, label: "Material", icon: Library }] : []),
    ...(sessionMode || effectivePathId ? [{ id: "chat" as ViewTab, label: "Tutor", icon: GraduationCap }] : []),
    ...(sessionMode || effectivePathId ? [{ id: "artefact" as ViewTab, label: "Artefatos", icon: BookOpen }] : []),
    ...(hasSession ? [{ id: "live-doc" as ViewTab, label: "Live Doc", icon: MessageSquare }] : []),
    { id: "terminal" as ViewTab, label: "Terminal", icon: Terminal },
  ];

  return (
    <div className="flex h-full w-full bg-[#0a0a0a] text-gray-100">
      {showLeveling && <LevelingModal topic="este assunto" onComplete={() => setShowLeveling(false)} onSkip={() => setShowLeveling(false)} />}
      <div className="flex flex-col flex-1 min-w-0">
        <div className="flex shrink-0 items-center gap-0.5 border-b border-[#1a1a1a] bg-[#0d0d0d] px-3 pt-1.5 overflow-x-auto">
          {allTabs.map((t) => (
            <button key={t.id} type="button" onClick={() => setActiveTab(t.id)}
              className={`flex items-center gap-1.5 px-3 py-1.5 text-[11.5px] font-medium rounded-t-md transition-colors ${activeTab === t.id ? "bg-[#0a0a0a] text-gray-100 border border-[#1a1a1a] border-b-transparent" : "text-gray-500 hover:text-gray-300 hover:bg-[#151515]"}`}>
              <t.icon size={12} strokeWidth={1.8} />{t.label}
            </button>
          ))}
          {hasSession && <a href={`/session-viewer/${note!.session}`} className="ml-auto flex items-center gap-1.5 px-2.5 py-1 text-[11px] text-cyan-400/70 hover:text-cyan-300 rounded border border-[#1a1a1a] hover:bg-[#151515] transition-colors"><MessageSquare size={11} strokeWidth={1.8} />{note!.session}</a>}
        </div>
        <div className="flex-1 min-h-0">
          {activeTab === "note" && <NoteEditor noteId={externalNoteId} />}
          {activeTab === "material" && <MaterialViewer pathId={effectivePathId} />}
          {activeTab === "chat" && <TutorChatSidebar pathId={effectivePathId} />}
          {activeTab === "artefact" && <LiveDocPanel sessionSlug={effectivePathId || ""} />}
          {activeTab === "terminal" && <TerminalPane />}
          {activeTab === "live-doc" && note?.session && <LiveDocPanel sessionSlug={note.session} />}
        </div>
      </div>
>>>>>>> Stashed changes
    </div>
  );
}
