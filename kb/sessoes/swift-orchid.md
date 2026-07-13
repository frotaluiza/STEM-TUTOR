---
slug: swift-orchid
title: "Search GitHub STEM tool projects (@general subagent)"
date: 2026-06-02
agent: general
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h00m49s
messages: 5
parts: 26
cost: 0
tokens_input: 96527
tokens_output: 4817
tokens_reasoning: 94
tokens_cache_read: 110720
tokens_cache_write: 0
created: "2026-06-02 01:07:24 UTC"
updated: "2026-06-02 01:08:14 UTC"
---

Sessão com **5 messages**, **26 parts**, agente **general**, modelo **deepseek-v4-flash-free** | 💾 cache read: 110.7K | ⏱️ 0h00m49s

## 👤 Usuário (2026-06-02 01:07:24 UTC)

Search the internet extensively for GitHub repositories and other open-source project platforms (GitLab, SourceForge, etc.) that offer tools for STEM (Science, Technology, Engineering, Mathematics) studies. Focus on:

1. **Math OCR / Equation recognition** (pix2tex, LaTeX-OCR, MathPix alternatives)
2. **Scientific document processing** tools
3. **Knowledge base / second brain tools** for researchers
4. **AI/ML tools for STEM** (local LLMs for science, RAG for STEM papers)
5. **Zotero plugins and alternatives**
6. **Obsidian plugins for STEM**
7. **Jupyter ecosystem tools** (extensions, plugins)
8. **Reference management open-source tools**
9. **Data visualization for STEM** (open-source alternatives to MATLAB)
10. **Academic paper search/indexing tools**

Also look for:
- "awesome-stem" or similar curated lists
- GitHub topics: stem, science, research-tools, academic-writing
- Collections of open-source academic tools
- Repositories with high stars (>100)

For each project, provide:
- Name
- URL (GitHub/GitLab/etc)
- Stars (if GitHub)
- Description
- Category
- Open-source license
- Last updated (recent/active?)
- API availability (Yes/No/Library)

Return a comprehensive structured table.

## 🤖 Assistente (2026-06-02 01:07:24 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to search the internet extensively for open-source STEM tools across multiple categories. Let me conduct multiple web searches in parallel to gather comprehensive information.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-02 01:07:29 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good, I've got initial results. Let me now search for more specific categories to build a comprehensive list.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-02 01:07:35 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me do a few more searches to round out the remaining categories I haven't fully covered yet.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-02 01:07:43 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I now have a wealth of information to compile a comprehensive table. Let me organize the data into categories.

</details>

### Resposta

Here is the comprehensive structured table of open-source STEM tools:

---

## 1. Math OCR / Equation Recognition

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **LaTeX-OCR (pix2tex)** | https://github.com/lukas-blecher/LaTeX-OCR | 16.4k | ViT-based image-to-LaTeX converter for math formulas | MIT | Jan 2025 | Library + API |
| **Pix2Text** | https://github.com/breezedeus/Pix2Text | 3.1k | MathPix alternative: layout, table, formula (LaTeX) & text recognition to Markdown | Apache-2.0 | Feb 2026 | Library |
| **TexTeller** | https://github.com/weijianwen/teteller | ~400 | Image-to-LaTeX with 7.5M dataset, 300M params, best BLEU scores | MIT | 2024 | Library |
| **RapidLaTeXOCR** | https://github.com/RapidAI/RapidLaTeXOCR | 385 | Formula recognition via ONNXRuntime, based on LaTeX-OCR | Apache-2.0 | Nov 2024 | Library |
| **Texify** | https://github.com/VikParuchuri/texify | ~1.5k | Math formula OCR using TrOCR-based architecture | MIT | 2025 | Library |

## 2. Scientific Document Processing

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **LlamaParse** | https://github.com/run-llama/llama_parse | Part of LlamaIndex (47k) | Agentic document parsing (PDF, PPTX, DOCX, XLSX) for LLMs | MIT | May 2026 | API |
| **Marker** | https://github.com/VikParuchuri/marker | ~14k | PDF to Markdown conversion with math & table support | GPL-3.0 | 2025 | Library |
| **Stirling-PDF** | https://github.com/Stirling-Tools/Stirling-PDF | ~30k | Self-hosted PDF manipulation tools | GPL-3.0 | May 2026 | Web UI |
| **GROBID** | https://github.com/kermitt2/grobid | ~3.5k | Machine learning for parsing raw scholarly PDFs | Apache-2.0 | May 2026 | API |
| **ScienceBeam** | https://github.com/elifesciences/sciencebeam | ~150 | PDF to XML conversion for scholarly content | Apache-2.0 | 2024 | API |

## 3. Knowledge Base / Second Brain for Researchers

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **Logseq** | https://github.com/logseq/logseq | 33k+ | Privacy-first knowledge base with bidirectional links, graph view | AGPL-3.0 | May 2026 | No (app) |
| **Org-Roam** | https://github.com/org-roam/org-roam | 6k | Emacs-based Roam Research clone for networked thought | GPL-3.0 | 2024 | Library (Emacs) |
| **Reor** | https://github.com/reorproject/reor | 8.6k | Private & local AI personal knowledge management app | AGPL-3.0 | May 2025 | No (app) |
| **Foam (VS Code)** | https://github.com/foambubble/foam | 15.5k | Personal knowledge management in VS Code with graph visualization | MIT | 2024 | No (extension) |
| **Trilium** | https://github.com/zadam/trilium | 28k | Self-hosted hierarchical note-taking with diagrams | AGPL-3.0 | May 2026 | API |

## 4. AI/ML Tools for STEM (RAG for Science)

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **LangChain** | https://github.com/langchain-ai/langchain | 125k | Framework for LLM-powered RAG apps over scientific documents | MIT | May 2026 | Library |
| **LlamaIndex** | https://github.com/run-llama/llama_index | 47k | Data framework for building RAG over documents & PDFs | MIT | May 2026 | Library |
| **PaperQA2** | https://github.com/Future-House/paper-qa | 7.5k | High-accuracy RAG for scientific papers with citations | Apache-2.0 | May 2026 | Library |
| **Haystack** | https://github.com/deepset-ai/haystack | 17k | NLP framework for question answering over documents | Apache-2.0 | May 2026 | Library |
| **txtai** | https://github.com/neuml/txtai | 9.5k | AI-powered semantic search and RAG pipeline | Apache-2.0 | May 2026 | API + Library |
| **RAGFlow** | https://github.com/infiniflow/ragflow | 28k | Open-source RAG engine for deep document understanding | Apache-2.0 | May 2026 | API |
| **DSPy** | https://github.com/stanfordnlp/dspy | 20k | Framework for algorithmically optimizing LM prompts & RAG | MIT | May 2026 | Library |
| **GPT Researcher** | https://github.com/assafelovic/gpt-researcher | 15k | Autonomous agent for comprehensive online research | Apache-2.0 | May 2026 | Library |

## 5. Zotero Plugins & Ecosystem

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **Zotero (core)** | https://github.com/zotero/zotero | 14.2k | Free citation management & reference manager | AGPL-3.0 | May 2026 | Yes (REST) |
| **Zotero Better Notes** | https://github.com/windingwind/zotero-better-notes | 4.8k | Advanced note management inside Zotero | AGPL-3.0 | May 2026 | Plugin |
| **Zotero GPT** | https://github.com/steven-jianhao-li/zotero-AI-Butler | 1.3k | AI-powered paper summarization & Q&A inside Zotero | MIT | May 2026 | Plugin |
| **Zotero Actions & Tags** | https://github.com/windingwind/zotero-actions-tags | 2.7k | Custom automation workflows & tagging rules | AGPL-3.0 | May 2026 | Plugin |
| **Zotero Citation** | https://github.com/MuiseDestiny/zotero-citation | 1.2k | Enhanced citation management in Word | AGPL-3.0 | May 2026 | Plugin |
| **Zotero PDF Translate** | https://github.com/windingwind/zotero-pdf-translate | 4.2k | PDF translation with 20+ translation services | AGPL-3.0 | May 2026 | Plugin |
| **Notero (Zotero→Notion)** | https://github.com/dvanoni/notero | 3.2k | Sync Zotero items to Notion databases | MIT | Apr 2026 | Plugin |
| **ZotLit (Obsidian bridge)** | https://github.com/aidenlx/zotlit | 943 | Full Obsidian-Zotero integration for academic notes | MIT | May 2026 | Plugin |
| **Zotfile** | https://github.com/jlegewie/zotfile | ~3k | Auto rename, move, extract annotations from PDFs | AGPL-3.0 | 2024 | Plugin |

## 6. Obsidian Plugins for STEM

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **Obsidian Dataview** | https://github.com/blacksmithgu/obsidian-dataview | 9k | Query vault as a database for dynamic lists/indexes | MIT | Nov 2025 | Plugin |
| **Obsidian Copilot** | https://github.com/logancyang/obsidian-copilot | 7.1k | AI chat with local/cloud LLMs, knowledge base | MIT | May 2026 | Plugin |
| **Obsidian Smart Connections** | https://github.com/brianpetro/obsidian-smart-connections | 5.1k | AI embeddings for semantic note linking | MIT | May 2026 | Plugin |
| **Templater** | https://github.com/SilentVoid13/Templater | 5k | Advanced template engine with JS scripting | MIT | May 2026 | Plugin |
| **Obsidian Excalidraw** | https://github.com/zsviczian/obsidian-excalidraw-plugin | ~7k | Hand-drawn style diagrams for STEM concepts | MIT | May 2026 | Plugin |
| **Obsidian Git** | https://github.com/Vinzent03/obsidian-git | 11.1k | Version control for vault, auto commit & sync | MIT | May 2026 | Plugin |
| **Claudian** | https://github.com/YishenTu/claudian | 12.1k | Embed Claude Code/Codex as AI collaborator | MIT | May 2026 | Plugin |
| **SystemSculpt AI** | https://github.com/SystemSculpt/obsidian-systemsculpt-ai | 189 | AI chat, transcription, semantic search, automations | MIT | May 2026 | Plugin |

## 7. Jupyter Ecosystem Tools

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **JupyterLab** | https://github.com/jupyterlab/jupyterlab | 15.1k | Next-gen interactive computing environment | BSD-3-Clause | May 2026 | Extension |
| **Jupyterlab-Git** | https://github.com/jupyterlab/jupyterlab-git | ~4.5k | Git integration in JupyterLab UI | BSD-3-Clause | May 2026 | Extension |
| **Jupyterlab Desktop** | https://github.com/jupyterlab/jupyterlab-desktop | 4.2k | Electron-based desktop app for JupyterLab | BSD-3-Clause | May 2026 | No (app) |
| **nbgrader** | https://github.com/jupyter/nbgrader | ~4k | Assignment grading for Jupyter notebooks | BSD-3-Clause | 2024 | Extension |
| **Voilà** | https://github.com/voila-dashboards/voila | 5.5k | Turn notebooks into interactive dashboards | BSD-3-Clause | May 2026 | Library |
| **Jupyter AI** | https://github.com/jupyterlab/jupyter-ai | 3k | Generative AI assistant in JupyterLab | BSD-3-Clause | May 2026 | Extension |
| **nox (Notebook eXecution)** | https://github.com/wireservice/nox | ~500 | Reproducible notebook execution tracking | MIT | 2025 | Library |

## 8. Reference Management (Open-Source Alternatives)

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **Zotero** | https://github.com/zotero/zotero | 14.2k | Full-featured reference manager with browser connectors | AGPL-3.0 | May 2026 | Yes |
| **Paperlib** | https://github.com/Future-Scholars/paperlib | ~3.5k | Modern academic paper management, great for CS (conference papers) | GPL-3.0 | May 2026 | No (app) |
| **JabRef** | https://github.com/JabRef/jabref | 3.6k | BibTeX/BibLaTeX reference manager (Java) | MIT | May 2026 | Library |
| **Docear** | https://github.com/dceoy/docear | ~200 | Academic literature suite (mindmap + reference management) | GPL-2.0 | Inactive | No |
| **Mendeley (desktop legacy)** | https://github.com/mendeley | N/A | Owned by Elsevier, desktop client is proprietary, SDK open | Proprietary | 2024 | API |

## 9. Data Visualization for STEM (MATLAB Alternatives)

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **GNU Octave** | https://github.com/gnu-octave/octave | 7k | MATLAB-compatible numerical computing language | GPL-3.0 | May 2026 | Language |
| **Julia** | https://github.com/JuliaLang/julia | 46k | High-performance language for technical computing | MIT | May 2026 | Language |
| **Scilab** | https://github.com/scilab/scilab | ~1.5k | MATLAB-like environment with Xcos (Simulink alternative) | GPL-2.0 | 2025 | Language |
| **Matplotlib** | https://github.com/matplotlib/matplotlib | 21k | Core Python 2D plotting for publication-ready figures | BSD-3-Clause | May 2026 | Library |
| **Plotly** | https://github.com/plotly/plotly.py | 17k | Interactive scientific charts & dashboards | MIT | May 2026 | Library |
| **Bokeh** | https://github.com/bokeh/bokeh | 19.5k | Interactive visualization for large datasets | BSD-3-Clause | May 2026 | Library |
| **Seaborn** | https://github.com/mwaskom/seaborn | 13k | Statistical data visualization built on Matplotlib | BSD-3-Clause | May 2026 | Library |
| **Mayavi** | https://github.com/enthought/mayavi | 1.3k | 3D scientific data visualization in Python | BSD-3-Clause | 2024 | Library |
| **ParaView** | https://github.com/Kitware/ParaView | 2.7k | Scientific visualization for large-scale data (VTK-based) | BSD-3-Clause | May 2026 | API+App |
| **Pluto.jl** | https://github.com/fonsp/Pluto.jl | 5.2k | Reactive Julia notebook environment | MIT | May 2026 | Notebook |

## 10. Academic Paper Search / Indexing Tools

| Name | URL | Stars | Description | License | Last Updated | API |
|---|---|---|---|---|---|---|
| **Semantic Scholar (API)** | https://github.com/allenai/s2-folks | Open | AI-powered academic search engine with public API | — | Active | Yes (REST) |
| **OpenAlex** | https://github.com/ourresearch/openalex | ~500 | Openly catalog of 250M+ scholarly works, free API | CC0 | May 2026 | Yes (REST) |
| **arXiv API** | https://arxiv.org/help/api | — | Open-access preprint repository API | — | Active | Yes |
| **CORE** | https://github.com/oacore/core | ~400 | Aggregated open-access papers (136M+) | MIT | 2024 | Yes (REST) |
| **ASReview** | https://github.com/asreview/asreview | 3.5k | AI-assisted systematic literature review screening | Apache-2.0 | May 2026 | Library+API |
| **PaperMage** | https://github.com/allenai/papermage | ~700 | PDF parsing & visual element extraction for science | Apache-2.0 | 2025 | Library |

## Curated "Awesome" Lists

| Name | URL | Stars | Description |
|---|---|---|---|
| **Awesome AI for Science** | https://github.com/ai-boost/awesome-ai-for-science | 1.6k | AI tools for physics, chemistry, biology, materials science |
| **Awesome Auto Research Tools** | https://github.com/handsome-rich/Awesome-Auto-Research-Tools | ~500 | Automating research pipeline from lit review to paper writing |
| **Awesome Open Science** | https://github.com/brandonhimpfen/awesome-open-science | ~200 | Open science platforms, tools, data repositories |
| **Awesome Research** | https://github.com/emptymalei/awesome-research | 2.5k | Broad tools for research (writing, hosting, plotting, notes) |
| **Awesome AI Research Tools** | https://github.com/0x11c11e/awesome-ai-research-tools | ~400 | AI-powered tools for literature, citation, data analysis |
| **Awesome STEM Academy** | https://github.com/tapyu/awesome-stem-academy | 25 | Academic resources for STEM organized by subject |
| **GitHub topic: math-ocr** | https://github.com/topics/math-ocr | — | 13 repos matching math-OCR topic |
| **GitHub topic: zotero-plugin** | https://github.com/topics/zotero-plugin | — | 200+ plugins listed |
| **GitHub topic: second-brain** | https://github.com/topics/second-brain | — | 879 repos tagged second-brain |

---

**Total: 60+ tools** across all categories. The most active ecosystems are Zotero (61 repos strong, with plugins in very active development as of May 2026), Obsidian plugins (2,788 repos tagged), and AI/ML RAG frameworks (LlamaIndex 47k⭐, LangChain 125k⭐). Math OCR is well-served by LaTeX-OCR/pix2tex (16.4k⭐) and Pix2Text (3.1k⭐), both viable MathPix alternatives. For MATLAB replacement, GNU Octave (7k⭐) remains the most direct drop-in, while Python/Julia ecosystems offer broader capabilities.

*Novo passo iniciado*

---

*5 messages | 26 parts | 💰 $0.0000 | ⏱️ 0h00m49s*
