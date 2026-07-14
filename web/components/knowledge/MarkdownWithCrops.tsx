"use client";

import { useCallback, useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { BookOpen } from "lucide-react";
import MarkdownRenderer from "@/components/common/MarkdownRenderer";
import { useTextSource } from "@/components/chat/preview/previewers/useTextSource";
import CropModal from "./CropModal";
import NotebookEditor from "./NotebookEditor";

interface MarkdownWithCropsProps {
  url: string;
  kbName: string;
  filename?: string;
}

const BACKEND = "http://localhost:8001";

type Segment =
  | { kind: "text"; content: string }
  | { kind: "garbled"; id: string; page: number; label: string };

export default function MarkdownWithCrops({
  url,
  kbName,
  filename,
}: MarkdownWithCropsProps) {
  const { t } = useTranslation();
  const state = useTextSource(url);
  const [activeCrop, setActiveCrop] = useState<{ garbledId: string; page: number } | null>(null);
  const [notebookMode, setNotebookMode] = useState(false);

  const storageKey = `crops:${kbName}:${filename ?? "unknown"}`;
  // Key = garbled id, value = saved image URL
  const [crops, setCrops] = useState<Record<string, string>>(() => {
    try { return JSON.parse(localStorage.getItem(storageKey) || "{}"); } catch { return {}; }
  });

  useEffect(() => {
    try { localStorage.setItem(storageKey, JSON.stringify(crops)); } catch {}
  }, [crops, storageKey]);

  const handleCropDone = useCallback(
    (garbledId: string) => (relativeUrl: string) => {
      const absUrl = relativeUrl.startsWith("http") ? relativeUrl : `${BACKEND}${relativeUrl}`;
      setCrops((prev) => ({ ...prev, [garbledId]: absUrl }));
      setActiveCrop(null);
    }, [],
  );

  if (state.kind === "loading") {
    return (
      <div className="flex h-full items-center justify-center text-[13px] text-[var(--muted-foreground)]">
        {t("Loading preview.")}
      </div>
    );
  }
  if (state.kind === "error") {
    return (
      <div className="flex h-full items-center justify-center px-6 text-center text-[13px] text-[var(--muted-foreground)]">
        {state.message}
      </div>
    );
  }

  // ── Split into segments ─────────────────────────────────────

  // Match both old format (<garbled page="35" ...>) and new (<garbled id="1" page="35" label="...">)
  const segments: Segment[] = [];
  let lastIdx = 0;
  const garbledRe = /<garbled\s+id="?(\d+)"?\s+page="?(\d+)"?\s+label="([^"]*)"?\s*\/>|<garbled\s+page="?(\d+)"?\s+label="([^"]*)"?\s*\/>/g;
  let m: RegExpExecArray | null;
  while ((m = garbledRe.exec(state.text)) !== null) {
    if (m.index > lastIdx) {
      segments.push({ kind: "text", content: state.text.slice(lastIdx, m.index) });
    }
    const id = m[1] || `p${m[4]}`;  // use new id if available, else fallback to "p{page}"
    const page = parseInt(m[2] || m[4], 10);
    const label = m[3] || m[5] || "Table/figure";
    segments.push({ kind: "garbled", id, page, label });
    lastIdx = m.index + m[0].length;
  }
  if (lastIdx < state.text.length) {
    segments.push({ kind: "text", content: state.text.slice(lastIdx) });
  }

  // ── Notebook content ────────────────────────────────────────

  const notebookContent = segments
    .map((s) =>
      s.kind === "garbled" ? `<crop page="${s.page}" label="${s.label}" />` : s.content
    )
    .join("");

  if (notebookMode) {
    return (
      <NotebookEditor
        initialContent={notebookContent}
        title={filename ?? "Textbook Chapter"}
        kbName={kbName}
        onClose={() => setNotebookMode(false)}
      />
    );
  }

  // ── Render with inline crop buttons ─────────────────────────

  return (
    <div className="px-6 py-5">
      <div className="mb-4 flex justify-end">
        <button
          type="button"
          onClick={() => setNotebookMode(true)}
          className="inline-flex items-center gap-1.5 rounded-lg border border-[var(--border)] px-3 py-1.5 text-[12px] font-medium text-[var(--foreground)] transition-colors hover:bg-[var(--muted)]"
        >
          <BookOpen size={13} />
          {t("Open in Notebook")}
        </button>
      </div>

      {/* Segments rendered INLINE — but group garbled by page */}
      {(() => {
        type Grouped = { id: string; page: number; label: string; index: number };
        const groupedByPage = new Map<number, Grouped>();
        const ordered: Grouped[] = [];

        for (const seg of segments) {
          if (seg.kind === "garbled") {
            if (!groupedByPage.has(seg.page)) {
              const g: Grouped = { id: seg.id, page: seg.page, label: seg.label, index: ordered.length };
              groupedByPage.set(seg.page, g);
              ordered.push(g);
            }
          }
        }

        // Build a set of pages that HAVE garbled content (for quick lookup)
        const garbledPages = new Set(ordered.map((g) => g.page));
        let garbledIdx = 0;

        return segments.map((seg, i) => {
          if (seg.kind === "text") {
            return <MarkdownRenderer key={i} content={seg.content} variant="prose" />;
          }

          // Only render the FIRST garbled occurrence per page
          if (garbledIdx < ordered.length && ordered[garbledIdx].id === seg.id) {
            const g = ordered[garbledIdx];
            garbledIdx++;
            const croppedUrl = crops[g.id];

            if (croppedUrl) {
              return (
                <div key={i} className="my-4">
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={croppedUrl} alt={g.label} className="max-w-full rounded-lg border border-[var(--border)]" />
                  <button type="button" onClick={() => setActiveCrop({ garbledId: g.id, page: g.page })}
                    className="mt-1 text-[11px] text-[var(--muted-foreground)] underline transition-colors hover:text-[var(--foreground)]">
                    {t("Re-crop")}
                  </button>
                </div>
              );
            }

            return (
              <div key={i} className="my-4">
                <button type="button" onClick={() => setActiveCrop({ garbledId: g.id, page: g.page })}
                  className="flex w-full items-center gap-3 rounded-lg border-2 border-dashed border-[var(--border)] px-4 py-3 text-left transition-colors hover:border-[var(--primary)]/40">
                  <span className="text-lg">✂️</span>
                  <div className="flex-1">
                    <div className="text-[13px] font-medium text-[var(--foreground)]">{g.label}</div>
                    <div className="text-[11px] text-[var(--muted-foreground)]">
                      {t("Page")} {g.page} — {t("click to crop")}
                    </div>
                  </div>
                </button>
              </div>
            );
          }

          return null; // skip duplicate garbled for same page
        });
      })()}

      {activeCrop !== null && (
        <CropModal
          kbName={kbName}
          pageNum={activeCrop.page}
          pageImageUrl={`${BACKEND}/api/v1/knowledge/${kbName}/files/figures/pg${String(activeCrop.page).padStart(4, "0")}.png`}
          suggestedName={`page${activeCrop.page}`}
          onCropDone={handleCropDone(activeCrop.garbledId)}
          onClose={() => setActiveCrop(null)}
        />
      )}
    </div>
  );
}
