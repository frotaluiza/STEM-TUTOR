"use client";

import { useState } from "react";

interface LevelingModalProps {
  topic: string;
  onComplete: (level: string, customDescription: string) => void;
  onSkip: () => void;
}

export function LevelingModal({ topic, onComplete, onSkip }: LevelingModalProps) {
  const [selected, setSelected] = useState("");
  const [custom, setCustom] = useState("");

  const options = [
    {
      id: "iniciante",
      label: `Iniciante — nunca vi ${topic}`,
    },
    {
      id: "basico",
      label: `Básico — já ouvi falar sobre ${topic}`,
    },
    {
      id: "intermediario",
      label: `Intermediário — já estudei ${topic} antes`,
    },
    {
      id: "avancado",
      label: `Avançado — domino ${topic}`,
    },
  ];

  const handleSubmit = () => {
    if (selected === "__custom__") {
      onComplete("personalizado", custom);
    } else if (selected) {
      onComplete(selected, "");
    }
  };

  return (
    <div className="fixed inset-0 bg-black flex items-center justify-center z-[100]">
      <div className="bg-[#111] border border-[#222] rounded-xl p-6 w-[440px] shadow-2xl">
        <div className="flex items-center gap-2 mb-4">
          <span className="text-lg">🎯</span>
          <h2 className="text-base font-semibold text-gray-200">Nivelamento Inicial</h2>
        </div>

        <p className="text-sm text-gray-200 mb-4">
          Qual seu nível em <span className="text-gray-200">{topic}</span>?
        </p>

        <div className="space-y-1">
          {options.map((opt) => (
            <label
              key={opt.id}
              className={`flex items-center gap-3 px-3 py-2 rounded-lg text-sm cursor-pointer transition-colors ${
                selected === opt.id
                  ? "bg-[#00ff80]/10 text-[#00ff80] border border-[#00ff80]/20"
                  : "text-gray-200 hover:text-gray-100 hover:bg-[#151515] border border-transparent"
              }`}
            >
              <input
                type="radio"
                name="level"
                value={opt.id}
                checked={selected === opt.id}
                onChange={() => setSelected(opt.id)}
                className="accent-[#00ff80]"
              />
              {opt.label}
            </label>
          ))}

          <div className="pt-1">
            <label
              className={`flex items-center gap-3 px-3 py-2 rounded-lg text-sm cursor-pointer transition-colors ${
                selected === "__custom__"
                  ? "bg-[#151515] border border-[#333]"
                  : "text-gray-300 hover:text-gray-200 border border-transparent"
              }`}
            >
              <input
                type="radio"
                name="level"
                value="__custom__"
                checked={selected === "__custom__"}
                onChange={() => setSelected("__custom__")}
                className="accent-[#00ff80]"
              />
              ✏️ Descrever meu nível:
            </label>
            {selected === "__custom__" && (
              <textarea
                value={custom}
                onChange={(e) => setCustom(e.target.value)}
                placeholder="Descreva seu conhecimento sobre o assunto..."
                className="mt-2 ml-8 w-[calc(100%-24px)] bg-[#0a0a0a] text-sm text-gray-300 border border-[#222] rounded px-3 py-2 outline-none resize-none h-16 placeholder-gray-700"
                autoFocus
              />
            )}
          </div>
        </div>

        <div className="flex justify-between items-center mt-5">
          <button
            onClick={onSkip}
            className="text-xs text-gray-400 hover:text-gray-200"
          >
            Pular
          </button>
          <button
            onClick={handleSubmit}
            disabled={!selected || (selected === "__custom__" && !custom.trim())}
            className="px-4 py-1.5 text-sm bg-[#00ff80]/10 text-[#00ff80] border border-[#00ff80]/20 rounded-lg hover:bg-[#00ff80]/20 disabled:opacity-30 disabled:cursor-not-allowed"
          >
            Iniciar Sessão Personalizada
          </button>
        </div>
      </div>
    </div>
  );
}
