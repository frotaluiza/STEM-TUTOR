#!/usr/bin/env python
"""
Format textbook markdown: clean up raw PyMuPDF extraction into readable markdown.

What it does:
  - Removes page-number artifacts ("3", "4", "c h a p t e r", etc.)
  - Rejoins hyphenated line breaks ("engi-\nneering" → "engineering")
  - Fixes Unicode ligatures ("ﬁ" → "fi", "ﬂ" → "fl")
  - Detects and wraps equations in $$...$$ or $...$
  - Cleans up headers and section markers
  - Separates into proper paragraphs
  - Preserves RAW originals in a raw_text/ subfolder

Usage:
    python scripts/format_textbook.py
    python scripts/format_textbook.py --section ch01_11-introduction
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
MODULES_DIR = PROJECT_ROOT / "data" / "modules" / "sadiku"

# ── patterns ──────────────────────────────────────────────────────

PAGE_NUM_RE = re.compile(r"^\d{1,3}\s*$", re.MULTILINE)

CHAPTER_SPACED_RE = re.compile(
    r"c\s+h\s+a\s+p\s+t\s+e\s+r\s*[\s\n]*\d{1,2}", re.IGNORECASE
)

HYPHEN_BREAK_RE = re.compile(r"(\w)-\n(\w)")

LIGATURE_FI_RE = re.compile("ﬁ")
LIGATURE_FL_RE = re.compile("ﬂ")

SECTION_NUM_RE = re.compile(r"^([1-9]\d*)\.(\d+)\s*$", re.MULTILINE)

MULTI_BLANK_RE = re.compile(r"\n{3,}")

# Global counter for unique garbled IDs
_garbled_id_counter = 0

def next_garbled_id() -> int:
    global _garbled_id_counter
    _garbled_id_counter += 1
    return _garbled_id_counter

# Lines from diagrams/tables — high ratio of control chars or non-alpha symbols
GARBLED_BLOCK_MIN_CHARS = 3

# Circuit component patterns — these indicate schematic/diagram text
CIRCUIT_COMP_RE = re.compile(
    r"\b[RCLEFUQ]\d+\b",  # R1, C3, L1, E, U1, Q1
)

def is_garbled_block(text: str) -> float:
    """Score a text block for garble (0 = clean, 1 = total garble)."""
    if not text or len(text) < GARBLED_BLOCK_MIN_CHARS:
        # Ultra-short lines: check if pure circuit component
        if text.strip() and re.match(r"^[RCLEFUQ]\d+$", text.strip()):
            return 0.6  # "C3", "L1", "R5" etc
        return 0.0
    n_control = sum(1 for c in text if ord(c) < 32 and ord(c) not in (9, 10, 13))
    n_nonalpha = sum(1 for c in text if not c.isalpha() and not c.isspace() and ord(c) > 31)
    total = max(len(text), 1)
    control_score = n_control / total
    nonalpha_score = n_nonalpha / total

    # Single repeated non-alpha char is often a separator line, not garble
    unique_syms = len(set(c for c in text if not c.isalpha() and not c.isspace() and ord(c) > 31))
    if unique_syms <= 2 and n_nonalpha > 0:
        nonalpha_score *= 0.3

    # Circuit component detection — lines like "R1 47", "C3", "L1 10uH"
    circuit_matches = CIRCUIT_COMP_RE.findall(text)
    circuit_density = len(circuit_matches) / max(len(text.split()), 1) if text.split() else 0

    # If > 30% of "words" are circuit components, it's garble
    circuit_score = 0.0
    if circuit_density > 0.3:
        circuit_score = min(1.0, circuit_density)

    return max(control_score, nonalpha_score, circuit_score)

PAGE_REF_BLOCK_RE = re.compile(
    r"\n---+\s*\n\*Page \d+.*?\*?\s*\n!\[.*?\]\(.*?\)\s*", re.DOTALL,
)

PHOTO_CREDIT_RE = re.compile(r"^Photo by .*$", re.MULTILINE)
SINGLE_WORD_LINE_RE = re.compile(r"^[A-Za-z]{1,2}\s*$", re.MULTILINE)

# Garbled control characters that appear in place of math operators
GARBLED_CHARS_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")

# Known garbled replacements: char → likely math symbol
GARBLED_MAP = {
    "\x01": "=",
    "\x02": "-",
    "\x03": "+",
    "\x04": "×",
    "\x05": "÷",
    "\x06": "∂",
    "\x0e": "Δ",
    "\x0f": "∫",
    "\x10": "∑",
    "\x11": "√",
    "\x12": "∞",
    "\x13": "π",
    "\x14": "θ",
    "\x15": "ω",
    "\x16": "λ",
    "\x17": "μ",
    "\x18": "φ",
    "\x19": "→",
    "\x1a": "±",
    "\x1b": "≤",
    "\x1c": "≥",
    "\x1d": "≠",
    "\x1e": "≈",
    "\x1f": "•",
}

# Inline equation patterns: variable = expression, variable(pattern)
INLINE_EQ_RE = re.compile(
    r"\b([a-zA-Z])\s*=\s*", re.IGNORECASE
)

# Display equation patterns: lines that look like equations
# (contain math operators, have more than one math symbol, are short)
DISPLAY_EQ_RE = re.compile(
    r"^[^a-z]*[=+\−×÷∫∑∏√±≤≥∞→∂Δθωπφλμ][^a-z]*$"
)

# Common math keywords that indicate an equation follows
MATH_KW_RE = re.compile(
    r"\b(where|obtain|find|gives|using|hence|thus|then|so)\b",
    re.IGNORECASE,
)

# Unit patterns: number followed by unit
UNIT_RE = re.compile(r"(\d+)\s+(V|A|Ω|W|Hz|F|H|Wb|T|J|C|N|m|s|kg|Wb)(?:\b|$)")

TABLE_REF_RE = re.compile(r"^TABLE\s+\d+\.\d+", re.IGNORECASE)


def replace_garbled(text: str) -> str:
    for char, replacement in GARBLED_MAP.items():
        text = text.replace(char, replacement)
    text = GARBLED_CHARS_RE.sub("", text)
    return text


def has_math(content: str) -> bool:
    content = replace_garbled(content)
    # Must be short (less than a sentence) to be a display equation
    if len(content) > 80:
        return False
    # Must contain math operators AND be mostly non-alpha
    has_op = bool(re.search(r"[=+\−×÷∫∑∏√±≤≥∞→∂Δθωπφλμ]", content))
    if not has_op:
        return False
    # Ratio of digits+symbols to total chars > 30 %
    symbols = sum(1 for c in content if not c.isalpha() and not c.isspace())
    if symbols / max(len(content), 1) < 0.2:
        return False
    return True


def fix_garbled_math(line: str) -> str:
    """Replace garbled math characters with proper LaTeX."""
    line = replace_garbled(line)
    return line


def wrap_inline_math(line: str) -> str:
    if " $" in line or line.startswith("$"):
        return line
    line = UNIT_RE.sub(r"$\1\,\2$", line)
    line = re.sub(r"\b([a-zA-Z])\s*=\s*([a-zA-Z0-9_{}()^/+\-]+)", r"$\1 = \2$", line)
    return line


def _extract_page_num(text: str) -> int | None:
    """Extract first pgNNNN page number from text content."""
    m = re.search(r"pg(\d+)", text)
    return int(m.group(1)) if m else None


def format_file(md_path: Path) -> str:
    raw = md_path.read_text(encoding="utf-8")
    text = raw

    # Extract page number BEFORE removing reference blocks
    page_num = _extract_page_num(text)
    if page_num is None:
        # Also try from the filename itself (e.g. ch01 → page 35)
        stem = md_path.stem
        m = re.search(r"ch(\d+)", stem)
        if m:
            chapter_map = {1: 35, 2: 61, 3: 113, 4: 159, 5: 207, 6: 247, 7: 285,
                           8: 345, 9: 401, 10: 445, 11: 489, 12: 535, 13: 587,
                           14: 645, 15: 707, 16: 747, 17: 787, 18: 841}
            page_num = chapter_map.get(int(m.group(1)))
    # Page number now comes directly from the section file's embedded pgNNNN reference

    # 1. Remove page reference blocks
    text = PAGE_REF_BLOCK_RE.sub("\n", text)

    # 2. Remove "c h a p t e r" headers
    text = CHAPTER_SPACED_RE.sub("", text)

    # 3. Remove standalone page numbers
    text = PAGE_NUM_RE.sub("", text)

    # 4. Remove photo credits
    text = PHOTO_CREDIT_RE.sub("", text)

    # 5. Remove single-letter artifacts
    text = SINGLE_WORD_LINE_RE.sub("", text)

    # 6. Rejoin hyphenated words
    text = HYPHEN_BREAK_RE.sub(r"\1\2", text)

    # 7. Fix ligatures
    text = LIGATURE_FI_RE.sub("fi", text)
    text = LIGATURE_FL_RE.sub("fl", text)

    # 8. Fix garbled math characters globally
    text = fix_garbled_math(text)

    # 8b. Remove extraction-inserted "# N.M Title" headers — the raw PDF text
    #     already contains "N.M" and the title on subsequent lines, and the
    #     formatter will recreate proper headers from them. Keeping both
    #     causes duplicate section headings (e.g. "# 1.2 ..." + "## 1.2").
    text = re.sub(r"^# (\d+\.\d+) .*\n?", "", text, flags=re.MULTILINE)

    # 9. Section numbers
    text = SECTION_NUM_RE.sub(r"## \1.\2", text)

    # 10. Collapse blanks
    text = MULTI_BLANK_RE.sub("\n\n", text)

    # 11. Detect and replace garbled blocks (diagrams, tables, circuits)
    #     Group ALL garbled paragraphs on the same page into ONE tag.
    paragraphs = text.split("\n\n")
    new_paras: list[str] = []
    garbled_count = 0
    current_page_group: list[str] = []

    def flush_garbled():
        nonlocal garbled_count, current_page_group
        if not current_page_group:
            return
        garbled_count += 1
        gid = next_garbled_id()
        label = f"Diagram from page {page_num}" if page_num else "Diagram"
        new_paras.append(f'<garbled id="{gid}" page="{page_num or 1}" label="{label}" />')
        current_page_group = []

    for para in paragraphs:
        stripped = para.strip()
        if not stripped:
            flush_garbled()
            new_paras.append("")
            continue

        score = is_garbled_block(stripped)
        min_len = 8
        if score > 0.3:
            min_len = 4
        if score > 0.4 and len(stripped) > min_len:
            current_page_group.append(stripped)
        else:
            flush_garbled()
            new_paras.append(para)

    flush_garbled()
    text = "\n\n".join(new_paras)

    # 12. Line-by-line processing
    lines = text.split("\n")
    out: list[str] = []
    in_table = False
    skip_words = {"Basic Concepts", "Introduction", "Chapter 1", "Chapter 2",
                   "Chapter 3", "Chapter 4", "Chapter 5", "Enhancing Your Skills and Your Career"}

    for line in lines:
        stripped = line.strip()

        if re.match(r"^\d{1,3}$", stripped) and not in_table:
            continue

        if stripped in skip_words and not in_table:
            if out and out[-1] == "":
                continue

        if TABLE_REF_RE.match(stripped):
            in_table = True
            out.append("\n" + line)
            continue
        if in_table and stripped == "":
            in_table = False
            out.append("")
            continue

        # Math display equations (skip garbled tags)
        if not stripped.startswith("<garbled") and has_math(stripped) and len(stripped) > 3 and not in_table and not stripped.startswith("$"):
            out.append(f"\n$${stripped}$$\n")
            continue

        if not in_table and not stripped.startswith("#") and not stripped.startswith("!") and not stripped.startswith("<"):
            line = wrap_inline_math(line)

        out.append(line)

    text = "\n".join(out)
    text = MULTI_BLANK_RE.sub("\n\n", text)
    text = text.strip() + "\n"

    if garbled_count > 0:
        text += f"\n> ✂️ {garbled_count} diagram(s) detected — use the buttons above to crop.\n"

    return text


def process_section(name: str | None = None) -> None:
    """Process all section files, or a specific one."""
    sections_dir = MODULES_DIR / "sections"
    raw_dir = MODULES_DIR / "raw_text"

    files = []
    if name:
        target = sections_dir / f"{name}.md"
        if target.exists():
            files = [target]
        else:
            print(f"[format] Section '{name}.md' not found in {sections_dir}")
            return
    else:
        files = sorted(sections_dir.glob("*.md"))

    raw_dir.mkdir(parents=True, exist_ok=True)

    for md_path in files:
        print(f"[format] {md_path.name} ...", end=" ", flush=True)

        # 1. Preserve raw original
        raw_path = raw_dir / md_path.name
        if not raw_path.exists():
            shutil.copy2(str(md_path), str(raw_path))
            print("(raw saved)", end=" ", flush=True)

        # 2. Format
        formatted = format_file(md_path)
        md_path.write_text(formatted, encoding="utf-8")
        print("ok", flush=True)


def process_all() -> None:
    """Process all sections, chapters, and exercises."""
    for subdir in ["sections", "chapters", "exercises"]:
        dir_path = MODULES_DIR / subdir
        if not dir_path.exists():
            continue
        raw_dir = MODULES_DIR / "raw_text" / subdir
        raw_dir.mkdir(parents=True, exist_ok=True)

        for md_path in sorted(dir_path.glob("*.md")):
            print(f"[format] {subdir}/{md_path.name} ...", end=" ", flush=True)

            # Preserve raw
            raw_path = raw_dir / md_path.name
            if not raw_path.exists():
                shutil.copy2(str(md_path), str(raw_path))
                print("(raw saved)", end=" ", flush=True)

            # Format
            formatted = format_file(md_path)
            md_path.write_text(formatted, encoding="utf-8")
            print("ok", flush=True)


# ── CLI ───────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Format textbook markdown files")
    parser.add_argument(
        "--section", "-s", default=None,
        help="Specific section to format (e.g., ch01_11-introduction)",
    )
    parser.add_argument(
        "--all", "-a", action="store_true",
        help="Format ALL sections, chapters, and exercises",
    )
    args = parser.parse_args()

    if args.section:
        process_section(args.section)
    elif args.all:
        process_all()
    else:
        # Default: process single section
        process_section("ch01_11-introduction")


if __name__ == "__main__":
    main()
