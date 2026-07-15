"use client";

import dynamic from "next/dynamic";
import { useCallback, useEffect, useState } from "react";
import { Download, FileText, Loader2, RefreshCw } from "lucide-react";

const MarkdownRenderer = dynamic(
  () => import("@/components/common/MarkdownRenderer"),
  { ssr: false },
);

interface ArtefactEntry {
  name: string;
  path: string;
  content: string;
  type: "markdown" | "image" | "code" | "other";
  size: number;
  updated: string;
}

interface ArtefactViewerProps {
  /** The mastery path id or session id to load artefacts for. */
  sourceId?: string;
}

export function ArtefactViewer({ sourceId }: ArtefactViewerProps) {
  const [artefacts, setArtefacts] = useState<ArtefactEntry[]>([]);
  const [selected, setSelected] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const selectedEntry = artefacts.find((a) => a.name === selected);

  const loadArtefacts = useCallback(async () => {
    if (!sourceId) return;
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`/api/v1/noteblocks/artefacts?source=${sourceId}`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setArtefacts(data.entries || []);
      if (data.entries?.length > 0 && !selected) {
        setSelected(data.entries[0].name);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Falha ao carregar artefatos");
      setArtefacts([]);
    } finally {
      setLoading(false);
    }
  }, [sourceId, selected]);

  useEffect(() => {
    loadArtefacts();
  }, [loadArtefacts]);

  const handleDownload = useCallback(() => {
    if (!selectedEntry) return;
    const blob = new Blob([selectedEntry.content], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${selectedEntry.name}.md`;
    a.click();
    URL.revokeObjectURL(url);
  }, [selectedEntry]);

  if (!sourceId) {
    return (
      <div className="flex items-center justify-center h-full text-gray-600 text-xs">
        <FileText className="w-4 h-4 mr-2 opacity-50" />
        Nenhuma sessão ativa para carregar artefatos.
      </div>
    );
  }

  if (error && artefacts.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center h-full text-center px-6">
        <p className="text-xs text-red-400">{error}</p>
        <button
          type="button"
          onClick={loadArtefacts}
          className="mt-2 flex items-center gap-1 text-xs text-gray-500 hover:text-gray-300"
        >
          <RefreshCw className="w-3 h-3" /> Tentar novamente
        </button>
      </div>
    );
  }

  if (loading && artefacts.length === 0) {
    return (
      <div className="flex items-center justify-center h-full text-gray-600">
        <Loader2 className="w-4 h-4 animate-spin mr-2" />
        Carregando artefatos...
      </div>
    );
  }

  if (artefacts.length === 0) {
    return (
      <div className="flex items-center justify-center h-full text-gray-600 text-xs">
        <FileText className="w-4 h-4 mr-2 opacity-50" />
        Nenhum artefato gerado ainda. Os resumos e explicações do tutor aparecerão aqui.
      </div>
    );
  }

  return (
    <div className="flex h-full">
      {/* Artefact list sidebar */}
      <aside className="w-48 shrink-0 border-r border-[#1a1a1a] flex flex-col">
        <div className="flex items-center justify-between px-3 py-2 border-b border-[#1a1a1a]">
          <span className="text-[11px] font-medium text-gray-400">Artefatos</span>
          <button
            type="button"
            onClick={loadArtefacts}
            className="p-1 rounded hover:bg-[#151515] text-gray-600 hover:text-gray-300"
            title="Recarregar"
          >
            <RefreshCw className="w-3 h-3" />
          </button>
        </div>
        <div className="flex-1 overflow-y-auto p-1 space-y-0.5">
          {artefacts.map((a) => (
            <button
              key={a.name}
              type="button"
              onClick={() => setSelected(a.name)}
              className={`w-full text-left px-2.5 py-1.5 text-[11px] rounded transition-colors ${
                selected === a.name
                  ? "bg-emerald-500/10 text-emerald-300 border border-emerald-500/20"
                  : "text-gray-500 hover:text-gray-300 hover:bg-[#111]"
              }`}
            >
              <div className="truncate">{a.name}</div>
              <div className="text-[10px] text-gray-700">
                {(a.size / 1024).toFixed(1)} KB · {a.type}
              </div>
            </button>
          ))}
        </div>
      </aside>

      {/* Artefact content */}
      <div className="flex-1 flex flex-col min-w-0">
        <div className="flex items-center justify-between px-4 py-2 border-b border-[#1a1a1a] shrink-0">
          <span className="text-xs text-gray-400 font-mono">{selectedEntry?.name}</span>
          <button
            type="button"
            onClick={handleDownload}
            className="flex items-center gap-1 px-2 py-1 text-[11px] text-gray-500 hover:text-gray-300 rounded hover:bg-[#151515]"
          >
            <Download className="w-3 h-3" /> Download
          </button>
        </div>
        <div className="flex-1 overflow-y-auto px-6 py-4">
          {selectedEntry?.type === "markdown" || selectedEntry?.type === "code" ? (
            <MarkdownRenderer content={selectedEntry.content} variant="prose" />
          ) : selectedEntry?.type === "image" ? (
            <img
              src={selectedEntry.path}
              alt={selectedEntry.name}
              className="max-w-full rounded"
            />
          ) : (
            <pre className="text-xs text-gray-400 font-mono whitespace-pre-wrap">
              {selectedEntry?.content}
            </pre>
          )}
        </div>
      </div>
    </div>
  );
}
