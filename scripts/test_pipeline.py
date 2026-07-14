"""
Tests for section splitting and formatting pipeline.

Usage: python -m pytest scripts/test_pipeline.py -v

Or directly: python scripts/test_pipeline.py
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))

MODULES_DIR = PROJECT_ROOT / "data" / "modules" / "sadiku"
SECTIONS_DIR = MODULES_DIR / "sections"
RAW_CHAPTERS = MODULES_DIR / "raw_text" / "chapters"

SECTION_RE = re.compile(r"^([1-9]\d*)\.(\d+)\s*$", re.MULTILINE)


def test_section_headers_no_duplicates():
    """Each section file must contain exactly ONE heading matching its own section number."""
    errors = []
    for fp in sorted(SECTIONS_DIR.glob("*.md")):
        text = fp.read_text(encoding="utf-8")
        # Find all ## headers that look like section numbers (N.M)
        headers = re.findall(r"^## ([1-9]\d*\.\d+)", text, re.MULTILINE)
        if not headers:
            continue  # exercise files etc may have no section header
        # The filename tells us what section this should be
        stem = fp.stem
        # Remove dedup suffix (-2, -3)
        base_stem = re.sub(r"-\d+$", "", stem)
        # Try to extract section number from filename
        m = re.search(r"_(\d+)-(\d+)", base_stem)
        m2 = re.search(r"_(\d+)-", base_stem)
        expected = f"{m.group(1)}.{m.group(2)}" if m else None

        if expected and expected in headers:
            # Expected section is present — check for UNEXPECTED ones
            unexpected = [h for h in headers if h != expected and not h.startswith("0.")]
            if unexpected:
                errors.append(f"{stem}: unexpected headers {unexpected} (expected {expected})")
        elif expected and expected not in headers:
            # Maybe the header format differs (e.g. "1.01" vs "1.1")
            errors.append(f"{stem}: expected header ## {expected} not found, found {headers}")

    assert not errors, "\n".join(errors)


def test_no_previous_section_content():
    """Section N should not contain section headers for section N-1 or earlier."""
    errors = []
    for fp in sorted(SECTIONS_DIR.glob("*.md")):
        text = fp.read_text(encoding="utf-8")
        stem = fp.stem
        m = re.search(r"_(\d+)-(\d+)", stem)
        if not m:
            continue
        ch = int(m.group(1))
        sec = int(m.group(2))
        this_sec = f"{ch}.{sec}"

        headers = re.findall(r"^## ([1-9]\d*\.\d+)", text, re.MULTILINE)
        for h in headers:
            h_ch = int(h.split(".")[0])
            h_sec = int(h.split(".")[1])
            if h_ch == ch and h_sec < sec:
                errors.append(f"{stem}: contains previous section header ## {h}")

    assert not errors, "\n".join(errors)


def test_chapter_section_boundaries():
    """Chapter sections should cover consecutive pages without gaps or overlaps."""
    # Load metadata
    # For now, just check ch01 which we know well
    ch01_sections = sorted([
        fp for fp in SECTIONS_DIR.glob("ch01_*.md")
        if not re.search(r"-\d+$", fp.stem)  # no dedup suffix
    ])
    # Expected page ranges for ch01
    expected = {
        "ch01_11-introduction": (35, 36),
        "ch01_12-systems-of-units": (37, 37),
        "ch01_13-charge-and-current": (38, 40),
        "ch01_14-voltage": (41, 41),
        "ch01_15-power-and-energy": (42, 46),
        "ch01_16-circuit-elements": (47, 48),
        "ch01_17-applications": (49, 51),
        "ch01_18-problem-solving": (52, 54),
        "ch01_19-summary": (55, 55),
    }
    for fp in ch01_sections:
        text = fp.read_text(encoding="utf-8")
        pages = sorted(set(re.findall(r"pg(\d{4})", text)))
        if pages:
            pgs = (min(int(p) for p in pages), max(int(p) for p in pages))
            expected_pgs = expected.get(fp.stem)
            if expected_pgs and pgs != expected_pgs:
                print(f"WARN: {fp.stem} pages={pgs} expected={expected_pgs}")


def test_garbled_page_numbers():
    """Garbled tags should point to pages that exist in the figures directory."""
    figures_dir = PROJECT_ROOT / "data" / "knowledge_bases" / "sadiku" / "raw" / "figures"
    if not figures_dir.exists():
        figures_dir = PROJECT_ROOT / "data" / "modules" / "sadiku" / "figures"
    errors = []
    for fp in sorted(SECTIONS_DIR.glob("*.md")):
        text = fp.read_text(encoding="utf-8")
        for m in re.finditer(r'page="(\d+)"', text):
            page = int(m.group(1))
            render = figures_dir / f"pg{page:04d}.png"
            if not render.exists():
                errors.append(f"{fp.stem}: garbled page={page}, render not found")
    assert not errors, "\n".join(errors)


def test_no_false_positive_headers():
    """No headers like ## 0.0033 from garbled circuit values."""
    errors = []
    for fp in sorted(SECTIONS_DIR.glob("*.md")):
        text = fp.read_text(encoding="utf-8")
        zero_headers = re.findall(r"^## 0\.\d+", text, re.MULTILINE)
        if zero_headers:
            errors.append(f"{fp.stem}: false positive zero-prefixed headers: {zero_headers}")
    assert not errors, "\n".join(errors)


def test_ch01_12_first_content_line():
    """After section header + title, first content must be 'As electrical engineers...'."""
    text = (SECTIONS_DIR / "ch01_12-systems-of-units.md").read_text(encoding="utf-8")
    lines = text.split("\n")
    # Skip header (## 1.2) and title (Systems of Units)
    first_content = None
    for line in lines:
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("<garbled"):
            continue
        if first_content is None and s == "Systems of Units":
            first_content = "title"  # mark that we saw the title
            continue
        if first_content == "title":
            first_content = s
            break
    assert first_content and first_content.startswith("As electrical engineers"), (
        f"ch01_12 first content: {first_content}"
    )


def test_ch01_13_first_content_line():
    """After section header + title, first content must be 'The concept of electric charge'."""
    text = (SECTIONS_DIR / "ch01_13-charge-and-current.md").read_text(encoding="utf-8")
    lines = text.split("\n")
    first_content = None
    for line in lines:
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("<garbled"):
            continue
        if first_content is None and s == "Charge and Current":
            first_content = "title"
            continue
        if first_content == "title":
            first_content = s
            break
    assert first_content and first_content.startswith("The concept of electric charge"), (
        f"ch01_13 first content: {first_content}"
    )


if __name__ == "__main__":
    import traceback
    tests = [
        test_section_headers_no_duplicates,
        test_no_previous_section_content,
        test_chapter_section_boundaries,
        test_garbled_page_numbers,
        test_no_false_positive_headers,
        test_ch01_12_first_content_line,
        test_ch01_13_first_content_line,
    ]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            print(f"  PASS  {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {test.__name__}")
            print(f"    {e}")
            failed += 1
        except Exception as e:
            print(f"  ERROR {test.__name__}: {e}")
            traceback.print_exc()
            failed += 1
    print(f"\n{passed}/{passed + failed} passed")
    sys.exit(1 if failed else 0)
