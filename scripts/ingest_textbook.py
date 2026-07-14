#!/usr/bin/env python
"""
Ingest textbook PDF -> structured Markdown notebook + images + DeepTutor KB.

Produces:
  - textbook.md              Full book
  - chapters/ch{nn}.md       Per chapter
  - sections/ch{nn}_{sec}.md Per sub-section
  - exercises/ch{nn}-{type}.md  Review Questions + Problems per chapter
  - figures/                 All images, per-page filenames
  - meta.json                Full metadata
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

import fitz

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
DEEPTUTOR_APP_DIR = PROJECT_ROOT / "deeptutor"

CHAPTER_TITLES = {
    1: "Basic Concepts",
    2: "Basic Laws",
    3: "Methods of Analysis",
    4: "Circuit Theorems",
    5: "Operational Amplifiers",
    6: "Capacitors and Inductors",
    7: "First-Order Circuits",
    8: "Second-Order Circuits",
    9: "Sinusoids and Phasors",
    10: "Sinusoidal Steady-State Analysis",
    11: "AC Power Analysis",
    12: "Three-Phase Circuits",
    13: "Magnetically Coupled Circuits",
    14: "Frequency Response",
    15: "Laplace Transform",
    16: "Fourier Series",
    17: "Fourier Transform",
    18: "Two-Port Networks",
}

CHAPTER_SPACED_RE = re.compile(
    r'c\s+h\s+a\s+p\s+t\s+e\s+r\s*[\s\n]*(\d+)', re.IGNORECASE
)
SECTION_RE = re.compile(r'^(\d+)\.(\d+)\s*$')
EXERCISE_HEADERS = {"Review Questions", "Problems"}
MAX_CHAPTER = 18


def resolve_pdf_path(path: str) -> Path:
    p = Path(path)
    return p if p.is_absolute() else (PROJECT_ROOT / path).resolve()


def detect_chapters(doc: fitz.Document) -> list[tuple[int, int]]:
    starts: dict[int, int] = {}
    for pn in range(doc.page_count):
        text = doc[pn].get_text().lower()
        m = CHAPTER_SPACED_RE.search(text)
        if not m:
            continue
        cn = int(m.group(1))
        if cn > MAX_CHAPTER or cn not in CHAPTER_TITLES or cn in starts:
            continue
        if starts and cn < max(starts.keys()):
            continue
        if pn < 30 and cn != 1:
            continue
        starts[cn] = pn + 1
        print(f"  Ch.{cn}: {CHAPTER_TITLES[cn]} -> page {pn+1}", flush=True)
    return sorted(starts.items(), key=lambda x: x[1])


def slugify(text: str, max_len: int = 50) -> str:
    s = text.lower().strip()
    s = s.encode('ascii', 'replace').decode('ascii')
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s).strip('-')
    return s[:max_len]


_img_counter: int = 0


def next_img_id() -> int:
    global _img_counter
    _img_counter += 1
    return _img_counter


_seen_content_hashes: set[int] = set()
_fig_counter: int = 0


def _img_hash(data: bytes) -> int:
    return hash(data[:1024])


FIG_CAPTION_RE = re.compile(r'(?:Fig(?:ure)?[.\s]*\d+\.\d+)', re.IGNORECASE)


def extract_figure_num(text: str) -> str | None:
    m = re.search(r'(?:Fig(?:ure)?)[.\s]*(\d+\.\d+)', text, re.IGNORECASE)
    return m.group(1) if m else None


def get_page_content(doc: fitz.Document, chapter_num: int, page_num: int,
                     figures_dir: Path) -> tuple[str, int]:
    """Return page markdown with figures rendered from page regions.

    For each 'Figure X.Y' caption found on the page, renders the page region
    just above the caption (capturing vector diagrams). Also includes any
    standalone extractable images not near a caption, plus a full-page reference.
    """
    global _seen_content_hashes, _fig_counter
    page = doc[page_num]
    blocks = page.get_text("dict")["blocks"]
    img_count = 0

    # 1. Collect all text blocks with their Y positions
    text_elements: list[tuple[float, str]] = []
    text_blocks_with_content: list[tuple[float, str]] = []

    for block in blocks:
        if block.get("type") != 0:
            continue
        text = ""
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text += span.get("text", "")
            if text.strip():
                text += "\n"
        if text.strip():
            text_blocks_with_content.append((block["bbox"][1], text.strip()))
            text_elements.append((block["bbox"][1], text))

    # 2. Full-page render at the end — no individual figure extraction.
    # PDF circuit diagrams are vector drawings that can't be extracted individually
    # on low-RAM machines. The full-page render shows ALL content faithfully.
    try:
        pix = page.get_pixmap(dpi=72)
        render_name = f"pg{page_num+1:04d}.png"
        dst = figures_dir / render_name
        if not dst.exists():
            pix.save(str(dst))
        text_elements.append((99999, f"\n\n---\n*Page {page_num+1}*\n![Page {page_num+1}](figures/{render_name})\n"))
        img_count += 1
    except Exception:
        pass

    # 6. Sort everything by Y position
    text_elements.sort(key=lambda e: e[0])

    # 7. Build final markdown
    md = "\n".join(part for _, part in text_elements)

    # 8. Add full-page reference
    try:
        pix = page.get_pixmap(dpi=72)
        render_name = f"pg{page_num+1:04d}.png"
        dst = figures_dir / render_name
        if not dst.exists():
            pix.save(str(dst))
        md += f"\n\n---\n*Page {page_num+1} (reference)*\n![Page {page_num+1}](figures/{render_name})\n"
    except Exception:
        pass

    return md, img_count


class TextbookIngester:

    def __init__(
        self,
        pdf_path: str,
        output_dir: str | Path = "data/modules/",
        kb_name: str | None = None,
        register_kb: bool = True,
    ):
        self.pdf_path = resolve_pdf_path(pdf_path)
        self.kb_name = kb_name or self.pdf_path.stem.lower().replace(" ", "-")
        self.output_dir = Path(output_dir).resolve()
        self.book_dir = self.output_dir / self.kb_name
        self.register_kb = register_kb
        self.sections_dir = self.book_dir / "sections"
        self.exercises_dir = self.book_dir / "exercises"
        self.figures_dir = self.book_dir / "figures"
        self.chapters_dir = self.book_dir / "chapters"

    def extract(self) -> None:
        doc = fitz.open(str(self.pdf_path))
        print(f"[ingest] PDF: {doc.page_count} pages", flush=True)
        self.book_dir.mkdir(parents=True, exist_ok=True)
        self.figures_dir.mkdir(parents=True, exist_ok=True)
        self.chapters_dir.mkdir(parents=True, exist_ok=True)
        self.sections_dir.mkdir(parents=True, exist_ok=True)
        self.exercises_dir.mkdir(parents=True, exist_ok=True)

        chapter_starts = detect_chapters(doc)
        all_chapter_meta = []
        all_section_meta = []
        all_exercise_meta = []

        for idx, (ch_num, start_1idx) in enumerate(chapter_starts):
            end_1idx = (
                chapter_starts[idx + 1][1] - 1
                if idx + 1 < len(chapter_starts)
                else doc.page_count
            )
            ch_title = CHAPTER_TITLES.get(ch_num, "")
            ch_slug = f"ch{ch_num:02d}"
            print(f"\n[ingest] {ch_slug}: {ch_title} (pages {start_1idx}-{end_1idx})", flush=True)

            # Collect pages for this chapter — each page: text, images, section info
            pages_data: list[dict] = []
            detected_sections: list[tuple[str, int, str]] = []  # (sec_num, page_1idx, title)
            seen_sections: set[str] = set()
            in_review_questions = False
            in_problems = False
            review_start_page = None
            problems_start_page = None

            for pg in range(start_1idx - 1, end_1idx):
                is_exercise = in_review_questions or in_problems
                page_md, page_img_count = get_page_content(
                    doc, ch_num, pg, self.figures_dir,
                )

                # Detect sections and exercise boundaries from raw text
                raw_text = doc[pg].get_text()
                lines = raw_text.split("\n")
                sec_num_this_page = None
                sec_title_this_page = None

                for li, line in enumerate(lines):
                    stripped = line.strip()
                    sm = SECTION_RE.match(stripped)
                    if sm and int(sm.group(1)) == ch_num:
                        # Skip blank lines to find the title (sometimes there's a blank
                        # line between "1.2" and "Systems of Units" in running text, but
                        # not in running headers — we need to handle both)
                        title_line = None
                        for skip in range(1, 4):
                            if li + skip < len(lines):
                                candidate = lines[li + skip].strip()
                                if candidate:
                                    title_line = candidate
                                    break
                        if title_line and len(title_line) > 3 and title_line[0].isupper() and not title_line[0].isdigit():
                            sec_num_this_page = f"{sm.group(1)}.{sm.group(2)}"
                            sec_title_this_page = title_line
                            # Skip running headers / duplicate section numbers
                            if sec_num_this_page not in seen_sections:
                                seen_sections.add(sec_num_this_page)
                                detected_sections.append((sec_num_this_page, pg + 1, title_line))

                    if stripped == "Review Questions" and not in_review_questions:
                        in_review_questions = True
                        review_start_page = pg + 1
                    if stripped == "Problems" and in_review_questions and not in_problems:
                        in_problems = True
                        problems_start_page = pg + 1

                pages_data.append({
                    "page_1idx": pg + 1,
                    "text": page_md,
                    "img_count": page_img_count,
                    "in_review": in_review_questions,
                    "in_problems": in_problems,
                    "sec_num": sec_num_this_page,
                    "sec_title": sec_title_this_page,
                })

            # ── Build section boundaries ────────────────────────
            # Section boundaries from detected sections
            section_boundaries = []  # (sec_num, start_page_1idx, title)
            for sn, sp, st in detected_sections:
                section_boundaries.append((sn, sp, st))

            # Sort by page
            section_boundaries.sort(key=lambda x: x[1])

            # No explicit section 1.1 detected (it's the intro), create it
            if not section_boundaries or section_boundaries[0][1] > start_1idx:
                intro_page = start_1idx
                intro_end = section_boundaries[0][1] - 1 if section_boundaries else problems_start_page or end_1idx
                if intro_end >= intro_page:
                    section_boundaries.insert(0, (f"{ch_num}.1", intro_page, "Introduction"))

            # Exercise boundaries
            if review_start_page:
                review_end = (problems_start_page - 1) if problems_start_page else end_1idx
            if problems_start_page:
                problems_end = end_1idx

            # ── Generate files ───────────────────────────────────

            # --- Full chapter Markdown ---
            ch_text = f"# Chapter {ch_num}: {ch_title}\n\n" + "\n".join(pd_["text"] for pd_ in pages_data)
            (self.chapters_dir / f"{ch_slug}.md").write_text(ch_text, encoding="utf-8")

            ch_img_count = sum(pd_["img_count"] for pd_ in pages_data)
            ch_char_count = sum(len(pd_["text"]) for pd_ in pages_data)
            all_chapter_meta.append({
                "chapter": ch_num,
                "heading": f"Chapter {ch_num}: {ch_title}",
                "file": f"{ch_slug}.md",
                "pages": [p["page_1idx"] for p in pages_data],
                "chars": ch_char_count,
                "images": ch_img_count,
            })
            print(f"  Chapter: {ch_char_count}c, {ch_img_count}img", flush=True)

            # --- Section-level Markdown ---
            for si, (sec_num, sec_start, sec_title) in enumerate(section_boundaries):
                sec_end = (
                    section_boundaries[si + 1][1] - 1
                    if si + 1 < len(section_boundaries)
                    else (review_start_page or problems_start_page or end_1idx) - 1
                )
                # If this section ends at or after exercise start, clip it
                if review_start_page and sec_end >= review_start_page:
                    sec_end = review_start_page - 1
                if sec_end < sec_start:
                    continue

                sec_pages = [p for p in pages_data if sec_start <= p["page_1idx"] <= sec_end]
                sec_slug_base = f"{ch_slug}_{slugify(f'{sec_num}-{sec_title}', 40)}"
                sec_slug = sec_slug_base
                dedup = 2
                while (self.sections_dir / f"{sec_slug}.md").exists():
                    sec_slug = f"{sec_slug_base}-{dedup}"
                    dedup += 1
                sec_text = f"# {sec_num} {sec_title}\n\n" + "\n".join(sp_["text"] for sp_ in sec_pages)
                sec_file = f"{sec_slug}.md"
                (self.sections_dir / sec_file).write_text(sec_text, encoding="utf-8")

                sec_img_count = sum(p["img_count"] for p in sec_pages)
                sec_char_count = sum(len(p["text"]) for p in sec_pages)
                all_section_meta.append({
                    "chapter": ch_num,
                    "section": sec_num,
                    "title": sec_title,
                    "file": sec_file,
                    "pages": [p["page_1idx"] for p in sec_pages],
                    "chars": sec_char_count,
                    "images": sec_img_count,
                })
                safe_title = sec_title.encode('ascii', 'replace').decode('ascii')
                print(f"  Section {sec_num}: {safe_title} -> {sec_file} ({sec_char_count}c, {sec_img_count}img)", flush=True)

            # --- Exercise files ---
            def write_exercise(name_tag: str, start_pg: int | None, end_pg: int) -> None:
                if start_pg is None or start_pg >= end_pg:
                    return
                ex_pages = [p for p in pages_data if start_pg <= p["page_1idx"] <= end_pg]
                ex_text = f"# Chapter {ch_num}: {name_tag}\n\n" + "\n".join(ep["text"] for ep in ex_pages)
                ex_file = f"{ch_slug}-{slugify(name_tag)}.md"
                (self.exercises_dir / ex_file).write_text(ex_text, encoding="utf-8")
                ex_img_count = sum(p["img_count"] for p in ex_pages)
                ex_char_count = sum(len(p["text"]) for p in ex_pages)
                all_exercise_meta.append({
                    "chapter": ch_num,
                    "type": name_tag,
                    "file": ex_file,
                    "pages": [p["page_1idx"] for p in ex_pages],
                    "chars": ex_char_count,
                    "images": ex_img_count,
                })
                print(f"  Exercises: {name_tag} -> {ex_file} ({ex_char_count}c, {ex_img_count}img)", flush=True)

            if review_start_page and problems_start_page:
                write_exercise("Review-Questions", review_start_page, problems_start_page - 1)
            if problems_start_page:
                write_exercise("Problems", problems_start_page, end_1idx)

        doc.close()

        # ── Save combined textbook.md ─────────────────────────
        combined = []
        for cm in all_chapter_meta:
            ch_path = self.chapters_dir / cm["file"]
            if ch_path.exists():
                combined.append(ch_path.read_text(encoding="utf-8"))
        (self.book_dir / "textbook.md").write_text(
            "\n\n---\n\n".join(combined), encoding="utf-8"
        )

        # ── Save metadata ──────────────────────────────────────
        meta = {
            "title": self.pdf_path.stem,
            "kb_name": self.kb_name,
            "source": str(self.pdf_path),
            "created": datetime.now().isoformat(),
            "chapters": all_chapter_meta,
            "sections": all_section_meta,
            "exercises": all_exercise_meta,
            "total_chapters": len(all_chapter_meta),
            "total_sections": len(all_section_meta),
            "total_exercises": len(all_exercise_meta),
            "total_chars": sum(c["chars"] for c in all_chapter_meta),
            "total_images": sum(c["images"] for c in all_chapter_meta),
        }
        (self.book_dir / "meta.json").write_text(
            json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(
            f"\n[ingest] {meta['total_chapters']} chapters, {meta['total_sections']} sections, "
            f"{meta['total_exercises']} exercise sets, {meta['total_images']} images"
        )

        # ── Save raw copies before formatting ───────────────────
        raw_text_dir = self.book_dir / "raw_text"
        raw_text_dir.mkdir(parents=True, exist_ok=True)
        for subdir in ["sections", "chapters", "exercises"]:
            d = self.book_dir / subdir
            if not d.exists():
                continue
            raw_subdir = raw_text_dir / subdir
            raw_subdir.mkdir(parents=True, exist_ok=True)
            for f in d.glob("*.md"):
                shutil.copy2(str(f), str(raw_subdir / f.name))
        print(f"[ingest] Raw text backed up to {raw_text_dir}", flush=True)

        # ── Format all markdown files ──────────────────────────
        print("[ingest] Formatting markdown files...", flush=True)
        import subprocess
        result = subprocess.run(
            [sys.executable, str(PROJECT_ROOT / "scripts" / "format_textbook.py"), "--all"],
            capture_output=True, text=True, cwd=str(PROJECT_ROOT),
        )
        if result.returncode == 0:
            lines = [l for l in result.stdout.split("\n") if l.strip()]
            print(f"[ingest] Formatted {len(lines)} files")
        else:
            print(f"[ingest] Format warning: {result.stderr[:200]}")

    async def register_knowledge_base(self) -> None:
        if not self.register_kb:
            return
        md_path = self.book_dir / "textbook.md"
        if not md_path.exists():
            print("[ingest] textbook.md not found, skipping KB registration")
            return

        sys.path.insert(0, str(DEEPTUTOR_APP_DIR.parent))
        from deeptutor.knowledge import KnowledgeBaseInitializer

        kb_base = PROJECT_ROOT / "data" / "knowledge_bases"
        kb_init = KnowledgeBaseInitializer(
            kb_name=self.kb_name, base_dir=str(kb_base),
        )
        kb_init.create_directory_structure()
        kb_init.copy_documents([str(md_path), str(self.book_dir / "meta.json")])

        if self.figures_dir.exists():
            shutil.copytree(
                self.figures_dir, Path(kb_init.raw_dir).parent / "figures",
                dirs_exist_ok=True,
            )
        await kb_init.process_documents()
        print(f"[ingest] KB '{self.kb_name}' registered and indexed.")

    async def run(self) -> None:
        print(f"[ingest] Output: {self.book_dir}")
        self.extract()
        await self.register_knowledge_base()
        print(f"[ingest] Done - notebook at {self.book_dir}")


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ingest textbook PDF -> Markdown notebook + sections + exercises + DeepTutor KB"
    )
    parser.add_argument("pdf", help="Path to the textbook PDF")
    parser.add_argument("-o", "--output-dir", default="data/modules/")
    parser.add_argument("--kb-name", default=None)
    parser.add_argument("--no-kb", action="store_true")
    args = parser.parse_args()
    ingester = TextbookIngester(
        pdf_path=args.pdf,
        output_dir=args.output_dir,
        kb_name=args.kb_name,
        register_kb=not args.no_kb,
    )
    await ingester.run()


if __name__ == "__main__":
    asyncio.run(main())
