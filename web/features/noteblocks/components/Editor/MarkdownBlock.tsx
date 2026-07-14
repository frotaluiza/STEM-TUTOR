"use client";

import dynamic from "next/dynamic";
import { Eye, Pencil } from "lucide-react";
import { useCallback, useState } from "react";

const MarkdownRenderer = dynamic(() => import("@/components/common/MarkdownRenderer"), { ssr: false });

interface MarkdownBlockProps {
  content: string;
  onChange: (content: string) => void;
}

export function MarkdownBlock({ content, onChange }: MarkdownBlockProps) {
  const [preview, setPreview] = useState(true);

  const toggle = useCallback(() => setPreview((p) => !p), []);

  return (
    <div className="border border-[var(--border)]/30 rounded-lg overflow-hidden bg-[#0d0d0d]">
      {/* Toolbar */}
      <div className="flex items-center gap-1 px-2 py-1 border-b border-[var(--border)]/20 bg-[#111]">
        <button
          type="button"
          onClick={() => setPreview(true)}
          className={`flex items-center gap-1 px-2 py-0.5 text-[11px] rounded transition-colors ${
            preview ? "bg-[#1a1a1a] text-gray-200" : "text-gray-500 hover:text-gray-300"
          }`}
        >
          <Eye size={11} strokeWidth={1.8} />
          Preview
        </button>
        <button
          type="button"
          onClick={() => setPreview(false)}
          className={`flex items-center gap-1 px-2 py-0.5 text-[11px] rounded transition-colors ${
            !preview ? "bg-[#1a1a1a] text-gray-200" : "text-gray-500 hover:text-gray-300"
          }`}
        >
          <Pencil size={11} strokeWidth={1.8} />
          Editar
        </button>
      </div>

      {/* Content */}
      {preview ? (
        <div className="px-3 py-2 max-h-96 overflow-y-auto">
          {content.trim() ? (
            <MarkdownRenderer content={content} variant="prose" />
          ) : (
            <p className="text-gray-600 text-sm italic">(vazio — clique em Editar para escrever)</p>
          )}
        </div>
      ) : (
        <textarea
          value={content}
          onChange={(e) => onChange(e.target.value)}
          className="w-full bg-transparent text-sm text-gray-300 outline-none resize-none font-mono p-3 min-h-[120px] placeholder-gray-700"
          placeholder="Escreva markdown aqui...
## Título
**negrito** *itálico* `código`
```python
print('hello')
```
- lista
1. numerada"
          spellCheck={false}
        />
      )}
    </div>
  );
}
