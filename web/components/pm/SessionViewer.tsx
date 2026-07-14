"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Bot, ChevronDown, ChevronRight, ChevronUp, Code2, Loader2, Terminal, User } from "lucide-react";

interface PartData {
  type: string;
  text?: string;
  tool?: string;
  state?: { status?: string; input?: unknown; output?: string };
  reason?: string;
  tokens?: unknown;
}

interface MessageData {
  role: string;
  id: string;
  parts: PartData[];
  time?: { created?: number };
  agent?: string;
  is_internal?: boolean;
  modelID?: string;
  cost?: number;
  tokens?: { total?: number; input?: number; output?: number; reasoning?: number };
}

interface SessionViewerProps {
  slug: string;
}

function formatTime(ms: number): string {
  if (!ms) return "";
  const d = new Date(ms);
  return d.toLocaleString("pt-BR", { day: "2-digit", month: "2-digit", hour: "2-digit", minute: "2-digit" });
}

function CollapsibleSection({
  title,
  defaultOpen = false,
  children,
}: {
  title: string;
  defaultOpen?: boolean;
  children: React.ReactNode;
}) {
  const [open, setOpen] = useState(defaultOpen);
  return (
    <div className="border border-[var(--border)]/30 rounded-lg overflow-hidden">
      <button
        type="button"
        onClick={() => setOpen(!open)}
        className="flex items-center gap-2 w-full px-3 py-2 text-left text-[12px] font-medium text-[var(--muted-foreground)] hover:bg-[var(--accent)]/30 transition-colors"
      >
        {open ? <ChevronDown size={12} /> : <ChevronRight size={12} />}
        {title}
      </button>
      {open && <div className="px-3 pb-2">{children}</div>}
    </div>
  );
}

function ToolCall({ part }: { part: PartData }) {
  const toolName = part.tool || "";
  const state = part.state || {};
  const status = state.status || "";
  const inp = state.input as Record<string, unknown> | undefined;
  const cmd = (inp?.command as string) || "";
  const out = (state.output as string) || "";
  const [showOutput, setShowOutput] = useState(false);

  if (toolName === "task") {
    const desc = (inp?.description as string) || "";
    return (
      <div className="text-[11px] text-cyan-500/70 font-mono py-1">
        🧠 Subagente: {desc}
      </div>
    );
  }

  if (toolName === "bash" || toolName === "powershell") {
    return (
      <div className="space-y-1 my-1">
        {cmd && (
          <div className="flex items-start gap-1.5 text-[11.5px] font-mono">
            <Terminal size={12} className="shrink-0 mt-0.5 text-yellow-500/70" />
            <span className="text-yellow-500/80">{cmd}</span>
          </div>
        )}
        {status === "completed" && out && (
          <>
            <button
              type="button"
              onClick={() => setShowOutput(!showOutput)}
              className="flex items-center gap-1 text-[10.5px] text-[var(--muted-foreground)]/60 hover:text-[var(--muted-foreground)]"
            >
              {showOutput ? <ChevronUp size={10} /> : <ChevronDown size={10} />}
              Output {showOutput ? "▲" : "▼"}
            </button>
            {showOutput && (
              <pre className="text-[11px] text-[var(--muted-foreground)]/70 bg-[var(--muted)]/20 p-2 rounded overflow-x-auto max-h-40 overflow-y-auto">
                {out.slice(0, 2000)}
              </pre>
            )}
          </>
        )}
        {status === "error" && (
          <div className="text-[11px] text-red-400/80">Error: {out.slice(0, 300)}</div>
        )}
      </div>
    );
  }

  return (
    <div className="text-[11px] text-[var(--muted-foreground)]/50 font-mono py-0.5">
      [{toolName}] {status}
    </div>
  );
}

function MessageBubble({ msg, index }: { msg: MessageData; index: number }) {
  const isUser = msg.role === "user";
  const [collapsed, setCollapsed] = useState(false);
  const [showReasoning, setShowReasoning] = useState(false);

  const textParts = msg.parts.filter((p) => p.type === "text" && !p.text?.startsWith("<task"));
  const reasoningParts = msg.parts.filter((p) => p.type === "reasoning");
  const toolParts = msg.parts.filter((p) => p.type === "tool");
  const hasTools = toolParts.length > 0;

  return (
    <div className={`flex gap-3 ${isUser ? "" : ""}`}>
      {/* Avatar column */}
      <div className="flex flex-col items-center shrink-0 w-7">
        <div
          className={`w-7 h-7 rounded-full flex items-center justify-center text-[11px] ${
            isUser ? "bg-blue-500/20 text-blue-400" : "bg-cyan-500/20 text-cyan-400"
          }`}
        >
          {isUser ? <User size={13} /> : <Bot size={13} />}
        </div>
      </div>

      {/* Content */}
      <div className="flex-1 min-w-0">
        {/* Header */}
        <div className="flex items-center gap-2 mb-1">
          <span className="text-[11.5px] font-medium text-[var(--foreground)]">
            {isUser ? "Você" : "Assistente"}
          </span>
          {msg.agent && (
            <span className="text-[10px] px-1.5 py-0.5 rounded bg-[var(--muted)]/30 text-[var(--muted-foreground)]/60 font-mono">
              {msg.agent}
            </span>
          )}
          {msg.time?.created && (
            <span className="text-[10px] text-[var(--muted-foreground)]/40 ml-auto">
              {formatTime(msg.time.created)}
            </span>
          )}
        </div>

        {/* Collapse toggle for assistant */}
        {!isUser && textParts.length > 0 && (
          <button
            type="button"
            onClick={() => setCollapsed(!collapsed)}
            className="flex items-center gap-1.5 mb-1 text-[11px] text-[var(--muted-foreground)]/50 hover:text-[var(--muted-foreground)] transition-colors"
          >
            {collapsed ? (
              <><ChevronRight size={12} /> Expandir resposta</>
            ) : (
              <><ChevronDown size={12} /> Recolher resposta</>
            )}
          </button>
        )}

        {/* Text content */}
        {!collapsed && (
          <div className="space-y-2">
            {/* User message - full visible */}
            {isUser && textParts.map((p, i) => (
              <div key={i} className="text-[13px] text-[var(--foreground)] leading-relaxed whitespace-pre-wrap">
                {p.text}
              </div>
            ))}

            {/* Assistant message - visible */}
            {!isUser && textParts.map((p, i) => (
              <div key={i} className="text-[13px] text-[var(--foreground)]/90 leading-relaxed whitespace-pre-wrap">
                {p.text}
              </div>
            ))}

            {/* Tool calls */}
            {hasTools && !isUser && (
              <div className="space-y-0.5 border-l-2 border-[var(--border)]/20 pl-3 my-1">
                {toolParts.map((p, i) => (
                  <ToolCall key={i} part={p} />
                ))}
              </div>
            )}

            {/* Reasoning toggle */}
            {reasoningParts.length > 0 && !isUser && (
              <CollapsibleSection
                title={`🧠 Raciocínio (${reasoningParts.length})`}
                defaultOpen={showReasoning}
              >
                <div className="text-[12px] text-[var(--muted-foreground)]/70 italic leading-relaxed whitespace-pre-wrap max-h-60 overflow-y-auto">
                  {reasoningParts.map((p, i) => (
                    <p key={i}>{p.text}</p>
                  ))}
                </div>
              </CollapsibleSection>
            )}
          </div>
        )}

        {/* Cost/tokens summary */}
        {!isUser && msg.cost !== undefined && msg.tokens && (
          <div className="flex items-center gap-3 mt-1.5 text-[10px] text-[var(--muted-foreground)]/30">
            {msg.cost > 0 && <span>💰 ${msg.cost.toFixed(4)}</span>}
            {msg.tokens?.total && <span>📊 {msg.tokens.total} tokens</span>}
          </div>
        )}
      </div>
    </div>
  );
}

function InternalGroup({ count, visible }: { count: number; visible: boolean }) {
  return (
    <div className="border border-[var(--border)]/20 rounded-lg bg-[var(--muted)]/10 px-3 py-2">
      <div className="flex items-center gap-2 text-[12px] text-[var(--muted-foreground)]/50">
        <span className="text-[11px] px-1.5 py-0.5 rounded bg-[var(--muted)]/30">⚙️</span>
        Processamento interno ({count} mensagens)
        {visible && <span className="text-[10px] ml-auto">(exibindo)</span>}
      </div>
    </div>
  );
}

export default function SessionViewer({ slug }: SessionViewerProps) {
  const [messages, setMessages] = useState<MessageData[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showInternals, setShowInternals] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);

    fetch(`/api/v1/pm/sessions/${slug}/export`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((data) => {
        if (!cancelled && data.messages) {
          setMessages(data.messages);
        }
        if (!cancelled) setLoading(false);
      })
      .catch((e) => {
        if (!cancelled) {
          setError(e.message);
          setLoading(false);
        }
      });

    return () => { cancelled = true; };
  }, [slug]);

  // Group consecutive internal messages
  const groupedMessages = useMemo(() => {
    const result: ({ type: "message"; msg: MessageData } | { type: "internal-group"; count: number; messages: MessageData[] })[] = [];
    let internalBuffer: MessageData[] = [];

    for (const msg of messages) {
      if (msg.is_internal) {
        internalBuffer.push(msg);
      } else {
        if (internalBuffer.length > 0) {
          result.push({ type: "internal-group", count: internalBuffer.length, messages: internalBuffer });
          internalBuffer = [];
        }
        result.push({ type: "message", msg });
      }
    }
    if (internalBuffer.length > 0) {
      result.push({ type: "internal-group", count: internalBuffer.length, messages: internalBuffer });
    }
    return result;
  }, [messages]);

  const userCount = messages.filter((m) => m.role === "user").length;
  const visibleCount = groupedMessages.filter((g): g is { type: "message"; msg: MessageData } => g.type === "message").length;

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12 text-[var(--muted-foreground)]">
        <Loader2 className="w-4 h-4 animate-spin mr-2" />
        Carregando sessão...
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center py-12 text-[var(--muted-foreground)]">
        <p className="text-red-400">Erro: {error}</p>
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col bg-[var(--background)]">
      {/* Header */}
      <div className="sticky top-0 z-10 bg-[var(--card)] border-b border-[var(--border)] px-4 py-2.5 flex items-center justify-between">
        <div>
          <h2 className="text-sm font-semibold text-[var(--foreground)]">Sessão: {slug}</h2>
          <p className="text-[11px] text-[var(--muted-foreground)]/60">{userCount} perguntas · {visibleCount} turnos</p>
        </div>
        <button
          type="button"
          onClick={() => setShowInternals(!showInternals)}
          className="text-[11px] px-2.5 py-1 rounded border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)] hover:bg-[var(--accent)]/30 transition-colors"
        >
          {showInternals ? "Ocultar processamento" : "Mostrar processamento"}
        </button>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-4 py-4 space-y-6">
        {groupedMessages.map((group, i) => {
          if (group.type === "internal-group") {
            if (!showInternals) {
              return <InternalGroup key={`int-${i}`} count={group.count} visible={showInternals} />;
            }
            return group.messages.map((msg, j) => (
              <MessageBubble key={msg.id || `${i}-${j}`} msg={msg} index={i + j} />
            ));
          }
          const g = group as { type: "message"; msg: MessageData };
          return <MessageBubble key={g.msg.id || i} msg={g.msg} index={i} />;
        })}
        <div ref={bottomRef} />
      </div>
    </div>
  );
}
