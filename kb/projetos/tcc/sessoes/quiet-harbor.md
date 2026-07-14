---
slug: quiet-harbor
title: "Analyze corrections plan (@explore subagent)"
date: 2026-05-29
agent: explore
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h00m28s
messages: 4
parts: 24
cost: 0
tokens_input: 30309
tokens_output: 3047
tokens_reasoning: 61
tokens_cache_read: 32128
tokens_cache_write: 0
created: "2026-05-29 15:02:53 UTC"
updated: "2026-05-29 15:03:22 UTC"
---

Sessão com **4 messages**, **24 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | 💾 cache read: 32.1K | ⏱️ 0h00m28s

## 👤 Usuário (2026-05-29 15:02:53 UTC)

Read these files and summarize their structure for me. I need to understand how to make surgical edits to specific slides without regenerating everything.

1. Read `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\slidegen\latex_assembler.py` — list all render functions and what they produce
2. Read `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\slidegen\consolidator.py` — understand how sections are aggregated
3. Read `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\slidegen\compiler.py` — understand `_inject_into_chapter`, `_resolve_chapter_copy`, and `_KEYWORD_MAP`
4. Read `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\template\chapters\` — list ALL template chapter files and their content
5. Read `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\template\presentationTCC.tex` — find the `\include` statements for chapters
6. Read `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\slidegen\config.py` — find how `paths` and `chapters_dir_abs` are defined

Return: a structured summary of:
- All template chapter files and their include order in presentationTCC.tex
- The _KEYWORD_MAP mapping from TCC chapters to template files
- The `active_chapters` config value
- How the consolidator currently aggregates slides
- Each render function in latex_assembler.py and what frame_type it handles

## 🤖 Assistente (2026-05-29 15:02:53 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to read multiple files and understand the structure of their slide generation system. Let me start by reading all the requested files in parallel.

</details>

### Resposta

I'll read all requested files in parallel to gather the full picture.

*Novo passo iniciado*

## 🤖 Assistente (2026-05-29 15:02:59 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read all the template chapter files to see their content.

</details>

### Resposta

Now let me read all five template chapter files to see their placeholder content.

*Novo passo iniciado*

## 🤖 Assistente (2026-05-29 15:03:03 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have all the data. Let me compose the structured summary the user requested.

</details>

### Resposta

Here is the complete structured summary.

---

## 1. Template Chapter Files and Include Order

**File:** `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\template\presentationTCC.tex`

The `\include` statements on lines 114-118 appear in this exact order:

| Line | `\include` path             | Template file (absolute) |
|------|-----------------------------|--------------------------|
| 114  | `\include{chapters/1_introducao}` | `...\template\chapters\1_introducao.tex` |
| 115  | `\include{chapters/2_revisao}`     | `...\template\chapters\2_revisao.tex`    |
| 116  | `\include{chapters/3_metodologia}` | `...\template\chapters\3_metodologia.tex` |
| 117  | `\include{chapters/4_resultados}`  | `...\template\chapters\4_resultados.tex`  |
| 118  | `\include{chapters/5_conclusoes}`  | `...\template\chapters\5_conclusoes.tex`  |

**Each template chapter file** has the same structural pattern:
- Line 1: `\section{Title}` -- the section heading preserved by `_inject_into_chapter`
- Lines 2+: Placeholder slide content (example `slide` environments with columns, figures, items, equations)
- Separated by `%===================================NEXT SLIDE===================================`
- No `% INSERT_SLIDES_HERE` marker -- injection works by **replacing everything after the `\section{}` line**.

---

## 2. `_KEYWORD_MAP` (compiler.py lines 208-217)

Maps keywords from **TCC chapter titles** to **template chapter filenames**:

```python
_KEYWORD_MAP = {
    "introdu":    "introdu",       # Introdução
    "revis":      "revis",         # Revisão Bibliográfica
    "fundament":  "revis",         # Fundamentação Teórica → revisão slot
    "metodolog":  "metodolog",     # Metodologia
    "resultado":  "resultado",     # Resultados
    "conclus":    "conclus",       # Conclusões
    "discuss":    "conclus",       # Discussão → conclusões slot
}
```

This is **Strategy 1** in `_resolve_chapter_copy()`. If the TCC chapter title contains one of these keywords (case-insensitive), it picks the template chapter whose filename stem contains the corresponding template keyword.

**Strategies (in priority order):**
1. **Keyword match** (above map) -- most reliable
2. **Position match** -- compare index in `active_chapters` vs `\include` order in `main_tex`
3. **Numeric fallback** -- match chapter number via regex on filename
4. **Last resort** -- first template chapter file found

---

## 3. `active_chapters` Config Value

Defined in `config.py` lines 60-63:

```python
active_chapters: list[str] = Field(default_factory=lambda: [
    "chapter01", "chapter02", "chapter03",
    "chapter04", "chapter06", "chapter07",
])
```

These are **TCC chapter stems** (from `tcc/Textual/`). Note:
- `chapter05` is **absent** (skipped)
- `chapter06` and `chapter07` are included even though there are only 5 template chapter files
- This list is used by Strategy 2 in `_resolve_chapter_copy` to align TCC chapters to template `\include` positions by index

---

## 4. How the Consolidator Aggregates Slides

**File:** `consolidator.py` -- `run_consolidate(cfg, run_id)`

Steps:

1. **Scans all sections** from `sections_map.json`
2. **Copies template** into `runs/<run_id>/deck/`
3. **Links TCC images** (`tcc_images/` symlink/junction)
4. **Groups approved sections by template chapter:**
   - Reads `\include{chapters/...}` from `presentationTCC.tex` to know what template chapters exist
   - For each section, uses `_resolve_chapter_copy()` to map its `chapter_file` (e.g. `chapter04`) to a template stem (e.g. `4_resultados`)
   - Only sections with `status == "APPROVED"` are included
   - Collects their `section_slides.tex` content into `tmpl_slides[tmpl_stem]`
5. **Injects per chapter:** For each template chapter file, concatenates all approved sections' slides with `\n\n` separator, then calls `_inject_into_chapter(chap_file, combined, "")` -- replacing content after the `\section{}` line
6. **Merges .bib** from all approved drafts' citation keys into `references/bibFile.bib`
7. **Patches preamble** (adds `booktabs`, optional speaker notes)
8. **Compiles** with `pdflatex` (3-pass + bibtex) into `deck_final.pdf`

**Key insight:** The consolidator does NOT regenerate individual slides. It reuses pre-generated `section_slides.tex` files from each approved section. If you need to edit one slide, you must:
- Re-run `assemble` for that specific section (produces new `section_slides.tex`)
- Re-run `consolidate` to re-inject all approved sections into the deck

---

## 5. All Render Functions in `latex_assembler.py`

The dispatch dictionary (lines 148-160) maps each `FrameType` to a render function:

| FrameType enum       | Render function           | LaTeX environment(s) produced                         |
|----------------------|---------------------------|-------------------------------------------------------|
| `SECTION_TITLE`      | `_render_section_title`   | `wideframe` (centered title, no slide env)            |
| `WIDEFRAME`          | `_render_section_title`   | `wideframe` (same as section_title)                   |
| `TITLE_BULLETS`      | `_render_title_bullets`   | `slide` + `Item` (bullet list)                        |
| `SUMMARY`            | `_render_title_bullets`   | `slide` + `Item` (same as title_bullets)              |
| `TWO_COLUMNS`        | `_render_two_columns`     | `slide` + `columns` (2-column bullet split)           |
| `FIGURE_TEXT`         | `_render_figure_text`     | `slide` + `columns` (left: Item, right: figure)       |
| `EQUATION`           | `_render_equation`        | `slide` + `myTitledBox` containing `equation`         |
| `DEFINITION`         | `_render_definition`      | `slide` + `myTitledBox` (bullets as text, optional eq)|
| `TABLE`              | `_render_table`           | `slide` + `table` + `tabular` (booktabs style)        |
| `SLIDE_WITH_CODE`    | `_render_title_bullets`   | `slide` + `Item` (simplified, no code listing)        |
| `SLIDE_FRAME_BREAKS` | `_render_title_bullets`   | `slide` + `Item` (same as title_bullets)              |

Each render function also appends:
- `\note{...}` if `speaker_notes` is set (via `_note_block`)
- Citation footer as `\vfill\hfill{\scriptsize ...}` with ABNT plain-text labels (via `_citations_footer`)
- A frame separator comment: `%===================================NEXT SLIDE===================================`

The `_render_frame` dispatcher also calls `_resolve_figure_ref` before rendering to resolve LaTeX labels to real image paths.

---

## 6. `_inject_into_chapter` (compiler.py lines 256-274)

This is the key function for surgical editing understanding:

```python
def _inject_into_chapter(chapter_copy, slides_content, chapter_title):
```

- Reads the current chapter `.tex` file
- **Finds the first `\section{...}` line** via regex `r"(\\section\{[^}]*\}[^\n]*\n)"`
- **Preserves** everything up to and including that `\section{}` line
- **Appends** the entire `slides_content` after it
- Writes back to the same file

This means the `\section{}` heading and its position in the TOC are always retained. Everything below the `\section{}` line is replaced wholesale. There is no `% INSERT_SLIDES_HERE` marker in the chapter templates -- injection works by truncating at the `\section` boundary.

---

## How to Make Surgical Edits (Summary)

To edit a single slide without regenerating everything:

1. **Manual edit:** Open `runs/<run_id>/sections/<section_id>/v1/section_slides.tex`, find the slide (separated by `%===NEXT SLIDE===`), edit the LaTeX directly, then re-run consolidation.

2. **Regenerate one section:** Run `python -m slidegen assemble --run <run_id> --section <section_id>` (replaces just that section's `section_slides.tex`), then re-run consolidation.

3. **The consolidation step** (`python -m slidegen consolidate --run <run_id>`) will:
   - Collect all approved `section_slides.tex` files
   - Concatenate them per template chapter
   - Call `_inject_into_chapter` to replace everything after `\section{}` in each template chapter file
   - Recompile the deck

The key constraint is that `_inject_into_chapter` does **not** merge -- it replaces. So if you hand-edit a chapter file in `deck/chapters/`, running consolidation again will overwrite those changes. The correct workflow is to edit at the `section_slides.tex` level (per-section) and then consolidate.

*Novo passo iniciado*

---

*4 messages | 24 parts | 💰 $0.0000 | ⏱️ 0h00m28s*
