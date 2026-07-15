"""
Extract Hayt - Eletromagnetismo 7a Ed into full chapter markdown files.

Usage:
    python scripts/extract_hayt_full.py

Output:
    data/user/workspace/learning/hayt-eletromagnetismo-material.md  (full book)
    data/user/workspace/learning/hayt/chapter_XX.md                (per chapter)
"""

import re
import sys
from pathlib import Path

# Add project root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

HAYT_PATTERNS = [
    "C:/Users/frota/Downloads/Eletromagnetismo - William H. Hayt 7ª Edição - Livro.pdf",
    "C:/Users/frota/Downloads/Eletromagnetismo - William H. Hayt 7a Edicao - Livro.pdf",
    "C:/Users/frota/Downloads/*Hayt*",
]

import glob

def find_hayt_pdf():
    for pattern in HAYT_PATTERNS:
        if "*" in pattern:
            matches = sorted(glob.glob(pattern))
            for m in matches:
                if "(1)" not in m and "(2)" not in m:
                    return m
        else:
            p = Path(pattern)
            if p.exists():
                return str(p)
    return None

def extract_all():
    pdf_path = find_hayt_pdf()
    if not pdf_path:
        print("ERROR: Hayt PDF not found in Downloads.")
        print("Download it or copy to one of these locations:")
        for p in HAYT_PATTERNS:
            print(f"  {p}")
        sys.exit(1)

    print(f"Found: {pdf_path}")
    
    # Try pymupdf4llm first (best markdown output), fall back to pymupdf
    try:
        import pymupdf4llm
        print("Using pymupdf4llm for extraction...")
        md_text = pymupdf4llm.to_markdown(pdf_path)
        has_pymupdf4llm = True
    except ImportError:
        has_pymupdf4llm = False
        print("pymupdf4llm not available, falling back to pymupdf...")

    if not has_pymupdf4llm:
        import fitz  # pymupdf
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        print(f"PDF loaded: {total_pages} pages")
        
        # Get table of contents
        toc = doc.get_toc()
        if toc:
            print(f"\nTable of Contents ({len(toc)} entries):")
            for level, title, page in toc:
                indent = "  " * (level - 1)
                print(f"  {indent}p.{page}: {title[:100]}")
        else:
            print("No TOC found in PDF.")
        
        # Extract all pages as markdown
        md_pages = []
        for i in range(total_pages):
            page = doc[i]
            text = page.get_text().strip()
            
            # Basic markdown conversion
            lines = text.split('\n')
            md_lines = []
            for line in lines:
                stripped = line.strip()
                if not stripped:
                    md_lines.append('')
                elif any(stripped.lower().startswith(x) for x in ['capítulo', 'capitulo', 'chapter']):
                    md_lines.append(f'\n## {stripped}\n')
                elif re.match(r'^\d+\.\d+\s', stripped):
                    md_lines.append(f'\n### {stripped}\n')
                else:
                    md_lines.append(stripped)
            
            page_md = '\n'.join(md_lines)
            if len(page_md.strip()) > 50:  # Skip near-empty pages
                md_pages.append(f"\n\n--- Page {i+1} ---\n\n{page_md}")
            
            if (i + 1) % 10 == 0:
                print(f"  Extracted page {i+1}/{total_pages}...")
        
        md_text = '\n'.join(md_pages)
        doc.close()

    # === Save output ===

    output_dir = Path(__file__).resolve().parent.parent / "data" / "user" / "workspace" / "learning"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Full book material file
    material_path = output_dir / "hayt-eletromagnetismo-material.md"
    material_path.write_text(md_text, encoding="utf-8")
    total_chars = len(md_text)
    print(f"\nSaved full material: {material_path}")
    print(f"  Total: {total_chars:,} characters, ~{total_chars // 3000} pages of text")
    
    # Also split into chapters if we can detect chapter boundaries
    chapter_pattern = re.compile(r'^##\s+[Cc]ap[ií]tulo\s+(\d+)', re.MULTILINE)
    chapters = list(chapter_pattern.finditer(md_text))
    
    if chapters:
        chapter_dir = output_dir / "hayt"
        chapter_dir.mkdir(parents=True, exist_ok=True)
        
        for i, match in enumerate(chapters):
            ch_num = match.group(1)
            start = match.start()
            end = chapters[i + 1].start() if i + 1 < len(chapters) else len(md_text)
            chapter_md = md_text[start:end].strip()
            
            ch_path = chapter_dir / f"chapter_{ch_num.zfill(2)}.md"
            ch_path.write_text(chapter_md, encoding="utf-8")
            print(f"  Chapter {ch_num}: {ch_path.name} ({len(chapter_md):,} chars)")
    else:
        print("No chapter boundaries detected (saved full text only).")
        print("Chapter 1 key points already exist at capitulo1_hayt_key_points.md")

    print("\nDone! Refresh the NoteBlocks Material tab to see the content.")

if __name__ == "__main__":
    extract_all()
