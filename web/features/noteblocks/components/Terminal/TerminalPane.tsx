"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { useTerminal } from "../../hooks/useTerminal";

export function TerminalPane() {
  const { output, connected, sendInput, clear } = useTerminal();
  const [input, setInput] = useState("");
  const [history, setHistory] = useState<string[]>([]);
  const [historyIdx, setHistoryIdx] = useState(-1);
  const bottomRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [output]);

  useEffect(() => {
    if (connected) inputRef.current?.focus();
  }, [connected]);

  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      if (!input.trim()) return;
      sendInput(input + "\n");
      setHistory((prev) => [...prev, input]);
      setHistoryIdx(-1);
      setInput("");
    },
    [input, sendInput]
  );

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      if (e.key === "ArrowUp") {
        e.preventDefault();
        if (history.length > 0) {
          const idx = historyIdx === -1 ? history.length - 1 : Math.max(0, historyIdx - 1);
          setHistoryIdx(idx);
          setInput(history[idx]);
        }
      } else if (e.key === "ArrowDown") {
        e.preventDefault();
        if (historyIdx !== -1) {
          const idx = historyIdx + 1;
          if (idx >= history.length) {
            setHistoryIdx(-1);
            setInput("");
          } else {
            setHistoryIdx(idx);
            setInput(history[idx]);
          }
        }
      }
    },
    [history, historyIdx]
  );

  return (
    <div className="flex flex-col h-full bg-white font-sans text-sm">
      <div className="flex items-center justify-between px-3 py-1 text-xs text-gray-500 bg-gray-50 border-b border-gray-200">
        <span>PowerShell {connected ? "●" : "○"}</span>
        <button onClick={clear} className="hover:text-gray-700 text-gray-400">
          clear
        </button>
      </div>

      <div className="flex-1 overflow-y-auto p-3 space-y-0.5">
        {output.map((line, i) => (
          <div
            key={i}
            className={`whitespace-pre-wrap ${
              line.startsWith("PS") || line.startsWith("$")
                ? "text-green-700"
                : line.includes("error") || line.includes("Error")
                ? "text-red-600"
                : "text-gray-900"
            }`}
          >
            {line}
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      <form onSubmit={handleSubmit} className="flex items-center border-t border-gray-200 px-3 py-2 bg-gray-50">
        <span className="text-green-700 mr-2 shrink-0">$</span>
        <input
          ref={inputRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          className="flex-1 bg-transparent text-gray-900 outline-none placeholder-gray-400"
          placeholder={connected ? "Type a command..." : "Connecting..."}
          disabled={!connected}
        />
      </form>
    </div>
  );
}
