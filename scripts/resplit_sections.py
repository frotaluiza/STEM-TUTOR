"""
Re-split chapter files into section files with fixed boundary detection
(no duplicate running headers). Reads from raw_text/chapters/, outputs to sections/.

Usage: python scripts/resplit_sections.py
"""
from __future__ import annotations

from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
MODULES_DIR = PROJECT_ROOT / "data" / "modules" / "sadiku"
RAW_CHAPTERS = MODULES_DIR / "raw_text" / "chapters"
RAW_SECTIONS = MODULES_DIR / "raw_text" / "sections"
RAW_EXERCISES = MODULES_DIR / "raw_text" / "exercises"
SECTIONS_DIR = MODULES_DIR / "sections"
EXERCISES_DIR = MODULES_DIR / "exercises"

SECTION_RE = re.compile(r"^(\d+)\.(\d+)$")

# Page reference marker: ---\n*Page N (reference)*\n![Page N](figures/pgNNNN.png)
PAGE_SPLIT_RE = re.compile(r"\n---\s*\n\*Page \d+ \(reference\)\*\s*\n!\[.*?\]\(.*?\)")

# Known chapter info: (ch_num, start_page, end_page, title)
CHAPTER_INFO = [
    (1, 35, 60, "Basic Concepts"),
    (2, 61, 112, "Basic Laws"),
    (3, 113, 158, "Methods of Analysis"),
    (4, 159, 206, "Circuit Theorems"),
    (5, 207, 246, "Operational Amplifiers"),
    (6, 247, 284, "Capacitors and Inductors"),
    (7, 285, 344, "First-Order Circuits"),
    (8, 345, 400, "Second-Order Circuits"),
    (9, 401, 444, "Sinusoids and Phasors"),
    (10, 445, 488, "Sinusoidal Steady-State Analysis"),
    (11, 489, 534, "AC Power Analysis"),
    (12, 535, 586, "Three-Phase Circuits"),
    (13, 587, 644, "Magnetically Coupled Circuits"),
    (14, 645, 706, "Frequency Response"),
    (15, 707, 746, "Laplace Transform"),
    (16, 747, 786, "Applications of the Laplace Transform"),
    (17, 787, 840, "Two-Port Networks"),
    (18, 841, 868, "Fourier Transform"),
]


def slugify(text: str, maxlen: int = 50) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s[:maxlen].rstrip("-")


def parse_chapter(text: str, ch_start: int) -> list[dict]:
    """Split chapter text into page segments. Each segment has page_1idx and text."""
    # Split on the (reference) marker. Each separator marks the end of page N.
    # The content BEFORE the separator belongs to page N.
    # Format of separator: ---\n*Page N (reference)*\n![Page N](figures/pgNNNN.png)
    sep_re = re.compile(
        r"\n---\s*\n\*Page (\d+) \(reference\)\*\s*\n!\[.*?\]\(.*?pg(\d{4})\.png\)"
    )

    parts = sep_re.split(text)
    # parts layout: [text0, page_num, pg_num, text1, page_num, pg_num, text2, ...]
    # The first element (text0) is content before first separator = page 35 (ch_start)
    # Each subsequent textN follows after a separator's page_num

    REF_STRIP = re.compile(
        r"\n---\s*\n\*Page \d+.*?\*?\s*\n!\[.*?\]\(.*?\)", re.DOTALL
    )

    pages = []
    # First block = page ch_start content
    first = parts[0].strip()
    if first:
        first = REF_STRIP.sub("", first).strip()
    if first:
        pages.append({"page_1idx": ch_start, "text": first})

    # Remaining blocks alternate: page_num, pgNNNN, text
    for i in range(1, len(parts), 3):
        page_num = int(parts[i])
        text_block = parts[i + 2].strip() if i + 2 < len(parts) else ""
        if text_block:
            text_block = REF_STRIP.sub("", text_block).strip()
        if text_block:
            pages.append({"page_1idx": page_num + 1, "text": text_block})

    return pages


def resplit_chapter(ch_num: int, start_page: int, end_page: int, ch_title: str) -> list[dict]:
    """Re-split a chapter into section files with fixed boundary detection."""
    ch_slug = f"ch{ch_num:02d}"
    ch_file = RAW_CHAPTERS / f"{ch_slug}.md"
    if not ch_file.exists():
        print(f"  SKIP: {ch_file.name} not found")
        return []

    text = ch_file.read_text(encoding="utf-8")

    # Parse into pages (approximate from chapter text)
    pages_data = parse_chapter(text, start_page)
    if not pages_data:
        print(f"  SKIP: {ch_file.name} has no parseable pages")
        return []

    print(f"  Parsed {len(pages_data)} pages from {ch_file.name}")

    # Detect sections from page text (same logic as ingest, but with dedup fix)
    detected_sections: list[tuple[str, int, str]] = []
    seen_sections: set[str] = set()
    in_review_questions = False
    in_problems = False
    review_start_page = None
    problems_start_page = None

    for pd_ in pages_data:
        pg = pd_["page_1idx"]
        page_text = pd_["text"]

        sec_num_this_page = None
        sec_title_this_page = None

        lines = page_text.split("\n")
        for li, line in enumerate(lines):
            stripped = line.strip()
            sm = SECTION_RE.match(stripped)
            if sm and int(sm.group(1)) == ch_num:
                # Skip blank lines to find the title
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
                        detected_sections.append((sec_num_this_page, pg, title_line))

            if stripped == "Review Questions" and not in_review_questions:
                in_review_questions = True
                review_start_page = pg
            if stripped == "Problems" and in_review_questions and not in_problems:
                in_problems = True
                problems_start_page = pg

    # Build section boundaries
    section_boundaries: list[tuple[str, int, str]] = list(detected_sections)
    section_boundaries.sort(key=lambda x: x[1])

    # Find text split points for pages shared by two sections (e.g. page 36
    # where both 1.1 and 1.2 have their headers). The earlier section gets the
    # page text before the later section's header; the later section gets text
    # from that header onwards.
    page_splits: dict[int, tuple[int, str]] = {}  # page_1idx -> (split_offset, later_sec_num)
    for si in range(len(section_boundaries) - 1):
        cur = section_boundaries[si]
        nxt = section_boundaries[si + 1]
        if cur[1] == nxt[1]:  # same start page
            shared_pg = cur[1]
            page_text = next(p["text"] for p in pages_data if p["page_1idx"] == shared_pg)
            pattern = f"\n{nxt[0]}\n\n{nxt[2]}"
            offset = page_text.find(pattern)
            if offset >= 0:
                page_splits[shared_pg] = (offset, nxt[0])

    # Sections start at the detected page.
    # The chapter intro content (e.g. "Enhancing Your Skills") is chapter-level,
    # not section-level — no intro insertion needed.

    # Generate section files
    section_meta = []
    for si, (sec_num, sec_start, sec_title) in enumerate(section_boundaries):
        if si + 1 < len(section_boundaries):
            sec_end = section_boundaries[si + 1][1] - 1
        else:
            sec_end = (review_start_page or problems_start_page or end_page) - 1
        
        if review_start_page and sec_end >= review_start_page:
            sec_end = review_start_page - 1
        
        # If sec_end < sec_start, check if this section shares a page with the next
        if sec_end < sec_start:
            if si + 1 < len(section_boundaries) and section_boundaries[si + 1][1] == sec_start:
                # Earlier section on a shared page — give it just this one page
                sec_end = sec_start
            else:
                continue
        
        if sec_start > end_page:
            continue
        
        # Build section page content, trimming shared pages
        # Running header pattern: section_num\nTitle\npage_number\n
        RUNNING_HEADER_RE = re.compile(
            r"^" + re.escape(sec_num) + r"\n"       # section number
            + re.escape(sec_title) + r"\n"           # section title
            + r"\d{1,3}\s*\n"                       # page number
        )
        sec_pages = []
        for pd_ in pages_data:
            if sec_start <= pd_["page_1idx"] <= sec_end:
                text = pd_["text"]
                pg = pd_["page_1idx"]
                if pg in page_splits:
                    split_offset, later_sec = page_splits[pg]
                    if sec_num == later_sec:
                        text = text[split_offset:]
                    else:
                        text = text[:split_offset]
                # Strip running headers from subsequent pages
                if pd_["page_1idx"] != sec_start:
                    text = RUNNING_HEADER_RE.sub("", text, count=1).strip()
                sec_pages.append(text)
        if not sec_pages:
            continue

        sec_slug_base = f"{ch_slug}_{slugify(f'{sec_num}-{sec_title}', 40)}"
        sec_slug = sec_slug_base
        dedup = 2
        existing = [f.stem for f in SECTIONS_DIR.glob("*.md")]
        while sec_slug in existing:
            sec_slug = f"{sec_slug_base}-{dedup}"
            dedup += 1
        sec_text = f"# {sec_num} {sec_title}\n\n" + "\n\n".join(sec_pages)
        # Add page reference for the formatter's _extract_page_num
        first_page = sec_start
        sec_text += f"\n\n![Page {first_page}](figures/pg{first_page:04d}.png)"
        sec_file = f"{sec_slug}.md"
        (SECTIONS_DIR / sec_file).write_text(sec_text, encoding="utf-8")

        safe_title = sec_title.encode("ascii", "replace").decode("ascii")
        page_range = f"{sec_start}-{sec_end}"
        print(f"    {sec_num}: {safe_title} -> {sec_file} (pages {page_range})")
        section_meta.append({
            "section": sec_num,
            "title": sec_title,
            "file": sec_file,
            "pages": list(range(sec_start, sec_end + 1)),
        })

    return section_meta


def main():
    SECTIONS_DIR.mkdir(parents=True, exist_ok=True)
    EXERCISES_DIR.mkdir(parents=True, exist_ok=True)
    RAW_SECTIONS.mkdir(parents=True, exist_ok=True)

    for ch_num, start_page, end_page, ch_title in CHAPTER_INFO:
        print(f"\nChapter {ch_num}: {ch_title}")
        resplit_chapter(ch_num, start_page, end_page, ch_title)

    print("\nDone. All sections re-split with fixed boundary detection.")


if __name__ == "__main__":
    main()
