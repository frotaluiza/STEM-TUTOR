"use client";

import { useState } from "react";
import type { Block } from "../../types";

interface QuestionBlockProps {
  block: Block;
  onAnswer: (blockId: string, answer: string, selectedOption?: string) => void;
}

export function QuestionBlock({ block, onAnswer }: QuestionBlockProps) {
  const [selected, setSelected] = useState<string>("");
  const [custom, setCustom] = useState("");
  const [answered, setAnswered] = useState(false);

  const options: { id: string; label: string }[] = block.meta?.options ?? [];
  const allowCustom = block.meta?.allow_custom ?? true;

  const handleSubmit = () => {
    const answer = selected === "__custom__" ? custom : selected;
    if (!answer.trim()) return;
    setAnswered(true);
    onAnswer(block.id, answer, selected);
  };

  if (answered) {
    return (
      <div className="text-sm text-gray-200 italic border-l-2 border-[#00ff80]/30 pl-3">
        {block.content}
        <div className="text-gray-300 mt-1">
          Resposta: {selected === "__custom__" ? custom : options.find((o) => o.id === selected)?.label || custom}
        </div>
      </div>
    );
  }

  return (
    <div className="border border-[#222] rounded-lg p-3 bg-[#0d0d0d]">
      <div className="flex items-start gap-2 mb-2">
        <span className="text-[#00ff80] text-sm font-mono shrink-0 mt-0.5">?</span>
        <span className="text-sm text-gray-200">{block.content}</span>
      </div>

      <div className="space-y-1 ml-5">
        {options.map((opt) => (
          <label
            key={opt.id}
            className={`flex items-center gap-2 px-2 py-1 rounded text-sm cursor-pointer transition-colors ${
              selected === opt.id ? "bg-[#00ff80]/10 text-[#00ff80]" : "text-gray-200 hover:text-gray-100 hover:bg-[#151515]"
            }`}
          >
            <input
              type="radio"
              name={`q-${block.id}`}
              value={opt.id}
              checked={selected === opt.id}
              onChange={() => setSelected(opt.id)}
              className="accent-[#00ff80]"
            />
            {opt.label}
          </label>
        ))}

        {allowCustom && (
          <div className="pt-1">
            <label
              className={`flex items-center gap-2 px-2 py-1 rounded text-sm cursor-pointer ${
                selected === "__custom__" ? "bg-[#151515]" : "text-gray-300 hover:text-gray-200"
              }`}
            >
              <input
                type="radio"
                name={`q-${block.id}`}
                value="__custom__"
                checked={selected === "__custom__"}
                onChange={() => setSelected("__custom__")}
                className="accent-[#00ff80]"
              />
              Outro:
            </label>
            {selected === "__custom__" && (
              <input
                value={custom}
                onChange={(e) => setCustom(e.target.value)}
                placeholder="Digite sua resposta..."
                className="ml-6 mt-1 w-full bg-[#0a0a0a] text-sm text-gray-300 border border-[#222] rounded px-2 py-1 outline-none placeholder-gray-700"
                autoFocus
              />
            )}
          </div>
        )}
      </div>

      <button
        onClick={handleSubmit}
        disabled={!selected || (selected === "__custom__" && !custom.trim())}
        className="mt-2 ml-5 px-3 py-1 text-xs bg-[#00ff80]/10 text-[#00ff80] border border-[#00ff80]/20 rounded hover:bg-[#00ff80]/20 disabled:opacity-30 disabled:cursor-not-allowed"
      >
        Enviar
      </button>
    </div>
  );
}
