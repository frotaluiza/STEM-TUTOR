"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { GraduationCap, Loader2, Plug, Send, Sparkles, User, GitCompare, XCircle } from "lucide-react";

interface ChatMessage {
  role: "tutor" | "learner";
  content: string;
  id: string;
}

type TutorStyle = "deeptutor" | "memphis";

interface TutorChatSidebarProps {
  pathId?: string;
  tutorStyle?: TutorStyle;
  onDragBlock?: (content: string, origin: string) => void;
}

export function TutorChatSidebar({ pathId, tutorStyle = "deeptutor", onDragBlock }: TutorChatSidebarProps) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [connected, setConnected] = useState(false);
  const [busy, setBusy] = useState(false);
  const [style, setStyle] = useState<TutorStyle>(tutorStyle);
  const [activated, setActivated] = useState(false);
  const wsRef = useRef<WebSocket | null>(null);
  const endRef = useRef<HTMLDivElement | null>(null);
  const sessionIdRef = useRef<string | null>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const connect = useCallback(() => {
    if (wsRef.current) return;
    setActivated(true);
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const wsUrl = `${protocol}//${window.location.host}/api/v1/ws`;
    const ws = new WebSocket(wsUrl);
    wsRef.current = ws;

    ws.onopen = () => {
      setConnected(true);
      const startPayload: Record<string, unknown> = {
        action: "start_turn",
        capability: "mastery_path",
        content: "Hello tutor! I'm ready to learn.",
        config: { tutor_style: style },
      };
      if (pathId) {
        startPayload.config = { ...(startPayload.config as object), mastery_path_id: pathId };
      }
      ws.send(JSON.stringify(startPayload));
    };

    ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        if (data.type === "session" && data.metadata?.session_id) {
          sessionIdRef.current = data.metadata.session_id;
        }
        if (data.type === "content" && data.content) {
          setMessages((prev) => [
            ...prev,
            { role: "tutor", content: data.content, id: `t-${Date.now()}` },
          ]);
        }
        if (data.type === "done") {
          setBusy(false);
        }
      } catch {
        // ignore parse errors
      }
    };

    ws.onerror = () => setConnected(false);
    ws.onclose = () => setConnected(false);
  }, [pathId, style]);

  const disconnect = useCallback(() => {
    if (wsRef.current) {
      wsRef.current.close();
      wsRef.current = null;
    }
    setConnected(false);
    setActivated(false);
    setMessages([]);
    sessionIdRef.current = null;
  }, []);

  const handleSend = useCallback(() => {
    const text = input.trim();
    if (!text || !wsRef.current || busy) return;

    setMessages((prev) => [
      ...prev,
      { role: "learner", content: text, id: `l-${Date.now()}` },
    ]);
    setInput("");
    setBusy(true);

    wsRef.current.send(
      JSON.stringify({
        action: "start_turn",
        capability: "mastery_path",
        content: text,
        session_id: sessionIdRef.current,
        config: { tutor_style: style, ...(pathId ? { mastery_path_id: pathId } : {}) },
      }),
    );
  }, [input, busy, pathId, style]);

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        if (activated) handleSend();
      }
    },
    [handleSend, activated],
  );

  // Disconnected/not activated state — show connect button
  if (!activated) {
    return (
      <div className="flex flex-col h-full bg-[#0a0a0a]">
        <div className="flex items-center gap-2 px-3 py-2 border-b border-[#1a1a1a] bg-[#0d0d0d] shrink-0">
          <GraduationCap className="w-4 h-4 text-emerald-400" />
          <span className="text-xs font-medium text-gray-300">Tutor</span>
        </div>
        <div className="flex-1 flex flex-col items-center justify-center text-center px-6 gap-4">
          <div className="w-12 h-12 rounded-full bg-emerald-500/10 flex items-center justify-center">
            <GraduationCap className="w-6 h-6 text-emerald-400" />
          </div>
          <div>
            <p className="text-sm text-gray-300 font-medium">Tutor de Estudo</p>
            <p className="text-xs text-gray-600 mt-1 max-w-xs">
              Conecte-se ao tutor para começar a sessão de aprendizado.
              Ele usará o mastery path para guiar seus estudos.
            </p>
          </div>

          {/* Style selector before connecting */}
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={() => setStyle("deeptutor")}
              className={`px-3 py-1.5 text-xs rounded-md border transition-colors ${
                style === "deeptutor"
                  ? "border-cyan-500/40 text-cyan-300 bg-cyan-500/10"
                  : "border-[#252525] text-gray-500 hover:text-gray-300"
              }`}
            >
              DeepTutor
            </button>
            <button
              type="button"
              onClick={() => setStyle("memphis")}
              className={`px-3 py-1.5 text-xs rounded-md border transition-colors ${
                style === "memphis"
                  ? "border-emerald-500/40 text-emerald-300 bg-emerald-500/10"
                  : "border-[#252525] text-gray-500 hover:text-gray-300"
              }`}
            >
              Memphis EMT
            </button>
          </div>

          <button
            type="button"
            onClick={connect}
            className="flex items-center gap-2 px-4 py-2 text-sm rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white transition-colors"
          >
            <Plug className="w-4 h-4" />
            Conectar ao tutor
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full bg-[#0a0a0a]">
      {/* Header */}
      <div className="flex items-center gap-2 px-3 py-2 border-b border-[#1a1a1a] bg-[#0d0d0d] shrink-0">
        <GraduationCap className="w-4 h-4 text-emerald-400" />
        <span className="text-xs font-medium text-gray-300">
          {style === "deeptutor" ? "DeepTutor" : "Tutor Memphis"}
        </span>
        <button
          type="button"
          onClick={() => {
            disconnect();
            setActivated(false);
          }}
          className="ml-2 p-0.5 rounded text-gray-600 hover:text-red-400 transition-colors"
          title="Desconectar"
        >
          <XCircle className="w-3.5 h-3.5" />
        </button>
        <button
          type="button"
          onClick={() => {
            const next = style === "deeptutor" ? "memphis" : "deeptutor";
            setStyle(next);
            disconnect();
            setTimeout(() => connect(), 100);
          }}
          className={`ml-1 flex items-center gap-1 px-1.5 py-0.5 text-[10px] rounded border transition-colors ${
            style === "memphis"
              ? "border-emerald-500/30 text-emerald-400 bg-emerald-500/10"
              : "border-cyan-500/30 text-cyan-400 bg-cyan-500/10"
          }`}
          title="Trocar estilo do tutor"
        >
          <GitCompare className="w-2.5 h-2.5" />
          {style === "deeptutor" ? "Memphis" : "DeepTutor"}
        </button>
        <div className="flex-1" />
        <span className={`w-1.5 h-1.5 rounded-full ${connected ? "bg-emerald-500" : "bg-red-500"}`} />
        <span className="text-[10px] text-gray-600">{connected ? "conectado" : "desconectado"}</span>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-3 py-2 space-y-2">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-center px-4">
            <Sparkles className="w-6 h-6 text-emerald-500/50 mb-2" />
            <p className="text-xs text-gray-600">
              {connected
                ? "Tutor pronto! Pergunte algo sobre o material de estudo."
                : "Conectando..."}
            </p>
            {!connected && <Loader2 className="w-4 h-4 animate-spin text-gray-600 mt-2" />}
          </div>
        )}

        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`flex gap-2 ${msg.role === "learner" ? "flex-row-reverse" : ""}`}
          >
            <div
              className={`w-6 h-6 rounded-full flex items-center justify-center shrink-0 text-[10px] ${
                msg.role === "tutor"
                  ? "bg-emerald-500/20 text-emerald-400"
                  : "bg-cyan-500/20 text-cyan-400"
              }`}
            >
              {msg.role === "tutor" ? (
                <GraduationCap className="w-3 h-3" />
              ) : (
                <User className="w-3 h-3" />
              )}
            </div>
            <div
              className={`max-w-[80%] rounded-lg px-3 py-1.5 text-xs leading-relaxed ${
                msg.role === "tutor"
                  ? "bg-[#151515] text-gray-200 border border-[#252525]"
                  : "bg-emerald-500/10 text-emerald-100 border border-emerald-500/20"
              }`}
            >
              {msg.content}
              {msg.role === "tutor" && onDragBlock && (
                <button
                  type="button"
                  draggable
                  onDragStart={(e) => {
                    e.dataTransfer.setData(
                      "text/plain",
                      JSON.stringify({ origin: "tutor", content: msg.content, type: "text" }),
                    );
                    e.dataTransfer.effectAllowed = "copy";
                  }}
                  className="mt-1 text-[10px] text-gray-600 hover:text-gray-300 flex items-center gap-1 opacity-0 hover:opacity-100 transition-opacity"
                  title="Arraste para a Nota"
                >
                  ⠿ Arrastar para Nota
                </button>
              )}
            </div>
          </div>
        ))}
        <div ref={endRef} />
      </div>

      {/* Input */}
      <div className="shrink-0 border-t border-[#1a1a1a] p-2">
        <div className="flex items-center gap-1.5">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Responda ao tutor..."
            rows={1}
            className="flex-1 bg-[#151515] text-xs text-gray-200 placeholder-gray-600 rounded-md px-2.5 py-1.5 border border-[#252525] resize-none outline-none focus:border-emerald-500/40 transition-colors"
            disabled={busy || !connected}
          />
          <button
            type="button"
            onClick={handleSend}
            disabled={busy || !connected || !input.trim()}
            className="p-1.5 rounded-md bg-emerald-600/20 text-emerald-400 hover:bg-emerald-600/30 disabled:opacity-30 transition-colors"
          >
            {busy ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Send className="w-3.5 h-3.5" />}
          </button>
        </div>
      </div>
    </div>
  );
}
