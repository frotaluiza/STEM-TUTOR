"use client";

import dynamic from "next/dynamic";
import { useCallback, useEffect, useState } from "react";
import { BookOpen, FileText, Globe, Loader2, RefreshCw } from "lucide-react";

const MarkdownRenderer = dynamic(
  () => import("@/components/common/MarkdownRenderer"),
  { ssr: false },
);

interface MaterialSection {
  title: string;
  content: string;
}

interface MaterialViewerProps {
  pathId?: string;
}

export function MaterialViewer({ pathId }: MaterialViewerProps) {
  const [sections, setSections] = useState<MaterialSection[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [translating, setTranslating] = useState(false);
  const [translatedSections, setTranslatedSections] = useState<MaterialSection[] | null>(null);
  const [showTranslated, setShowTranslated] = useState(false);

  const loadMaterial = useCallback(async () => {
    if (!pathId) return;
    setLoading(true);
    setError(null);
    setTranslatedSections(null);
    setShowTranslated(false);
    try {
      const res = await fetch(`/api/v1/learning/progress/${encodeURIComponent(pathId)}/material`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setSections(data.sections || []);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Falha ao carregar material");
      setSections([]);
    } finally {
      setLoading(false);
    }
  }, [pathId]);

  useEffect(() => {
    loadMaterial();
  }, [loadMaterial]);

  const handleTranslate = useCallback(async () => {
    if (!pathId || translating) return;
    // Combine all sections into one text for translation
    const fullContent = sections.map((s) => `# ${s.title}\n\n${s.content}`).join("\n\n---\n\n");
    if (!fullContent.trim()) return;

    setTranslating(true);
    try {
      const res = await fetch(
        `/api/v1/learning/progress/${encodeURIComponent(pathId)}/material/translate`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ content: fullContent, target_language: "pt-BR" }),
        },
      );
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setTranslatedSections([{ title: "Traduzido para Português", content: data.translated }]);
      setShowTranslated(true);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Falha na tradução");
    } finally {
      setTranslating(false);
    }
  }, [pathId, sections, translating]);

  if (!pathId) {
    return (
      <div className="flex items-center justify-center h-full text-gray-600 text-xs">
        <BookOpen className="w-4 h-4 mr-2 opacity-50" />
        Nenhum caminho de estudo selecionado.
      </div>
    );
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full text-gray-600">
        <Loader2 className="w-4 h-4 animate-spin mr-2" />
        Carregando material...
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-full text-center px-6">
        <FileText className="w-8 h-8 text-gray-700 mb-2" />
        <p className="text-xs text-red-400">{error}</p>
        <button
          type="button"
          onClick={loadMaterial}
          className="mt-2 flex items-center gap-1 text-xs text-gray-500 hover:text-gray-300"
        >
          <RefreshCw className="w-3 h-3" /> Tentar novamente
        </button>
      </div>
    );
  }

  if (sections.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center h-full text-center px-6">
        <BookOpen className="w-8 h-8 text-gray-700 mb-2" />
        <p className="text-xs text-gray-600">
          Nenhum material disponível para este caminho.
        </p>
        <p className="text-xs text-gray-700 mt-1">
          Adicione um arquivo markdown em{" "}
          <code className="text-[10px]">data/user/workspace/learning/{pathId}-material.md</code>
        </p>
      </div>
    );
  }

  const displaySections = showTranslated && translatedSections ? translatedSections : sections;
  const allContent = sections.map((s) => s.content).join("\n");
  const isEnglish = /[A-Za-z]{10,}/.test(allContent) && !/[à-üÀ-Ü].{5,}/.test(allContent);

  return (
    <div className="h-full flex flex-col">
      <div className="flex items-center justify-between px-4 py-2 border-b border-[#1a1a1a] shrink-0">
        <div className="flex items-center gap-2">
          <span className="text-xs text-gray-400 font-mono">
            {sections.length} seção(ões)
          </span>
          {translatedSections && (
            <button
              type="button"
              onClick={() => setShowTranslated(!showTranslated)}
              className={`text-[10px] px-2 py-0.5 rounded-full border transition-colors ${
                showTranslated
                  ? "border-emerald-500/40 text-emerald-400 bg-emerald-500/10"
                  : "border-gray-700 text-gray-500 hover:text-gray-300"
              }`}
            >
              {showTranslated ? "Traduzido" : "Original"}
            </button>
          )}
        </div>
        <div className="flex items-center gap-1">
          {isEnglish && !translating && !translatedSections && (
            <button
              type="button"
              onClick={handleTranslate}
              className="flex items-center gap-1 px-2 py-1 text-[11px] text-gray-400 hover:text-emerald-300 rounded hover:bg-[#151515] transition-colors"
              title="Traduzir para português"
            >
              <Globe className="w-3 h-3" />
              Traduzir
            </button>
          )}
          {translating && (
            <span className="flex items-center gap-1 text-[11px] text-emerald-400 px-2">
              <Loader2 className="w-3 h-3 animate-spin" />
              Traduzindo...
            </span>
          )}
          <button
            type="button"
            onClick={loadMaterial}
            className="p-1 rounded hover:bg-[#151515] text-gray-600 hover:text-gray-300"
            title="Recarregar"
          >
            <RefreshCw className="w-3 h-3" />
          </button>
        </div>
      </div>
      <div className="flex-1 overflow-y-auto px-6 py-4 space-y-6">
        {displaySections.map((section, i) => (
          <div key={i}>
            <MarkdownRenderer content={section.content} variant="prose" />
          </div>
        ))}
      </div>
    </div>
  );
}
