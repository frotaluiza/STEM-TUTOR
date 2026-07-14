---
slug: witty-nebula
title: "Deep search technical image VLMs (@general subagent)"
date: 2026-06-17
agent: general
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h00m51s
messages: 6
parts: 32
cost: 0.016212
tokens_input: 101288
tokens_output: 4297
tokens_reasoning: 184
tokens_cache_read: 277504
tokens_cache_write: 0
created: "2026-06-17 02:31:28 UTC"
updated: "2026-06-17 02:32:20 UTC"
---

Sessão com **6 messages**, **32 parts**, agente **general**, modelo **deepseek-v4-flash** | 💰 $0.0162 | 💾 cache read: 277.5K | ⏱️ 0h00m51s

## 👤 Usuário (2026-06-17 02:31:28 UTC)

Search exhaustively for vision-language models (VLMs) that have been TRAINED or FINE-TUNED on technical/scientific/document images. I need models that can understand diagrams, charts, schematics, and technical figures - not just natural images.

Search specifically for:

1. **Qwen2.5-VL** — Was it fine-tuned on technical documents? What can it understand? Search for benchmarks on diagram/chart understanding.

2. **InternVL2 / InternVL2.5** — Same questions. Any fine-tuning on technical/scientific figures?

3. **Granite Docling 258M / 7B** (IBM) — This was specifically trained for document conversion. What can it understand? Circuit diagrams?

4. **Florence-2** (Microsoft) — Was trained on rich captions. Does it understand diagrams/charts?

5. **SmolVLM** (HuggingFace) — Lightweight. Benchmarks on document understanding?

6. **Idefics3 / Idefics2** — Document understanding capabilities?

7. **Phi-3.5-vision / Phi-4-vision** (Microsoft) — Trained on scientific data? Chart understanding?

8. **molmo** (Allen AI) — Any document/figure capabilities?

9. **DocOwl** / **mPLUG-DocOwl** — Specifically for document understanding.

10. **Any VLM that appears on the ChartQA, DocVQA, or InfoVQA leaderboards** — These are benchmarks for technical/chart/document understanding.

For each model found, return:
- Model name
- Size (parameters)
- License
- Can it run locally? (VRAM requirements)
- What technical content it understands
- Links to HuggingFace model page
- Specific benchmarks scores on: ChartQA, DocVQA, InfoVQA, or similar technical benchmarks

Also search for any papers about using VLMs for circuit/electronics diagram understanding specifically.

## 🤖 Assistente (2026-06-17 02:31:29 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to exhaustively search for vision-language models (VLMs) that are trained or fine-tuned on technical/scientific/document images. This is a research-oriented question requiring web searches. Let me fetch information from multiple sources.

Let me search for each model and the benchmarks.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 02:31:34 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now fetch the remaining models: Phi-3.5-vision / Phi-4-vision, molmo, DocOwl/mPLUG-DocOwl, and search for papers on VLMs for circuit/electronics diagram understanding.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 02:31:40 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I have gathered a lot of information. Now let me also search for Phi-4-vision, and also search for circuit/electronics diagram understanding papers more specifically.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 02:31:44 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have enough information to compile a comprehensive answer. Let me also search for more papers on circuit/electronics diagram understanding with VLMs.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 02:31:48 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me compile all the information I've gathered into a comprehensive response.

</details>

### Resposta

Here is the exhaustive research on VLMs for technical/scientific/document images:

---

## 1. Qwen2.5-VL (Alibaba)

| Property | Value |
|---|---|
| **Sizes** | 3B, 7B, 72B params |
| **License** | Apache 2.0 |
| **Run locally?** | Yes — 7B needs ~16GB VRAM (BF16), 3B needs ~8GB |
| **HF page** | https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct |
| **Technical understanding** | **Excellent.** Explicitly trained on charts, icons, graphics, layouts, invoices, forms, tables. Structured output support for document scans. |
| **Benchmarks** (7B) | **ChartQA: 87.3**, **DocVQA: 95.7**, **InfoVQA: 82.6**, OCRBench: 864, TextVQA: 84.9, MMMU: 58.6 |

**Verdict:** Top-tier for all document/chart/schematic tasks. Best-in-class on ChartQA, DocVQA, InfoVQA among open models in this size range.

---

## 2. InternVL2.5 (OpenGVLab / Shanghai AI Lab)

| Property | Value |
|---|---|
| **Sizes** | 1B, 2B, 4B, 8B, 26B, 38B, 78B |
| **License** | MIT |
| **Run locally?** | Yes — 8B needs ~16GB VRAM |
| **HF page** | https://huggingface.co/OpenGVLab/InternVL2_5-8B |
| **Technical understanding** | **Excellent.** Stage 1.5 training specifically enhances "rare domains like multilingual OCR and mathematical charts." Strong document/chart performance. |
| **Benchmarks** (8B) | ChartQA: 84.3, DocVQA: 93.0, InfoVQA: 77.6, TextVQA: 79.1, MMMU: 50.6, MathVista: 56.7 |

**Verdict:** Very strong on technical document understanding. Close behind Qwen2.5-VL on most benchmarks. Available in many sizes for deployment flexibility.

---

## 3. Granite Vision 3.1 (IBM) — 2B-preview (3B total with encoder)

| Property | Value |
|---|---|
| **Sizes** | 3B total (2B LLM + vision encoder) |
| **License** | Apache 2.0 |
| **Run locally?** | Yes — very lightweight, ~6GB VRAM |
| **HF page** | https://huggingface.co/ibm-granite/granite-vision-3.1-2b-preview |
| **Technical understanding** | **Purpose-built for documents.** Trained specifically for "visual document understanding, enabling automated content extraction from tables, charts, infographics, plots, diagrams." Uses synthetic data for document tasks. |
| **Benchmarks** | **ChartQA: 86.0**, **DocVQA: 88.0**, **InfoVQA: 63.0**, AI2D: 78.0, TextVQA: 76.0, OCRBench: 75.0, LiveXiv VQA: 61.0, LiveXiv TQA: 55.0 |

**Verdict:** Best performance-per-parameter for document tasks. Beats Phi-3.5v on ChartQA, DocVQA, InfoVQA despite smaller size. Updated version Granite Vision 4.1 (4B) now available.

---

## 4. Florence-2 (Microsoft)

| Property | Value |
|---|---|
| **Sizes** | 0.23B (base), 0.77B (large) |
| **License** | MIT |
| **Run locally?** | Yes — extremely lightweight, <2GB VRAM |
| **HF page** | https://huggingface.co/microsoft/Florence-2-large |
| **Technical understanding** | Good for OCR and captioning. Supports `<OCR>` and `<OCR_WITH_REGION>` task prompts. Trained on FLD-5B dataset with rich captions. Not specifically optimized for charts/diagrams — more of a generalist. |
| **Benchmarks** | No direct ChartQA/DocVQA scores in zero-shot. Finetuned: TextCaps 151.1 CIDEr, TextVQA 73.5, VizWiz 72.6. COCO Det mAP 43.4. |

**Verdict:** Great tiny model for OCR and general captioning, but **not** the best choice for diagram/chart understanding — it lacks the specialized document training of the others. Use it as an OCR preprocessing step.

---

## 5. SmolVLM2 (HuggingFace)

| Property | Value |
|---|---|
| **Sizes** | 256M, 500M, 2.2B |
| **License** | Apache 2.0 |
| **Run locally?** | Yes — 2.2B needs ~5.2GB VRAM (very efficient) |
| **HF page** | https://huggingface.co/HuggingFaceTB/SmolVLM2-2.2B-Instruct |
| **Technical understanding** | Decent. Built on Idefics3 architecture. Trained on LLaVA-OneVision, M4-Instruct, Mammoth datasets (which include some chart data). |
| **Benchmarks** (2.2B) | **ChartQA: 68.84**, **DocVQA: 79.98**, AI2D: 70.0, MathVista: 51.5, MMMU: 42.0, OCRBench: 72.9, TextVQA: 73.21, ScienceQA: 90.0 |

**Verdict:** Extremely efficient for its size but significantly behind Granite Vision on chart/document tasks. Good for on-device applications where compute is constrained.

---

## 6. Idefics3 (HuggingFace)

| Property | Value |
|---|---|
| **Sizes** | 8B |
| **License** | Apache 2.0 |
| **Run locally?** | Yes — ~16GB VRAM |
| **HF page** | https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3 |
| **Technical understanding** | **Specifically improved over Idefics2 for document understanding.** Trained on Docmatix dataset and extended The Cauldron with document data. |
| **Benchmarks** | **DocVQA: 87.7**, TextVQA: 74.9, MMMU: 46.6, MathVista: 58.4, MMStar: 55.9 |

**Verdict:** Good document understanding capability (7th best DocVQA in its class). SmolVLM2 is built on this architecture.

---

## 7. Phi-3.5-vision / Phi-4-multimodal (Microsoft)

| Property | Phi-3.5-vision | Phi-4-multimodal |
|---|---|---|
| **Sizes** | 4.2B | 5.6B |
| **License** | MIT | MIT |
| **Run locally?** | Yes (~8GB VRAM) | Yes (~10GB VRAM) |
| **HF page** | [Link](https://huggingface.co/microsoft/Phi-3.5-vision-instruct) | [Link](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) |

**Phi-3.5-vision:** Trained on "chart/table/diagram/slides" synthetic data + multi-image data. Intended use includes "chart and table understanding." Benchmarks: ChartQA: 81.8, AI2D: 78.1, TextVQA: 72.0, MMMU: 43.0, MathVista: 43.9.

**Phi-4-multimodal:** Significantly improved. Benchmarks: **ChartQA: 81.4**, **DocVQA: 93.2**, **InfoVQA: 72.7**, AI2D: 82.3, TextVQA: 75.6, OCRBench: 84.4, MMMU: 55.1, MathVista: 62.4, ScienceQA: 97.5. Also supports **speech+vision** simultaneously (s_DocVQA: 87.3, s_ChartQA: 69.0).

**Verdict:** Phi-4-multimodal is excellent for document/chart tasks and adds audio modality. Phi-3.5v is still solid but surpassed by newer models.

---

## 8. Molmo (Allen AI / Ai2)

| Property | Value |
|---|---|
| **Sizes** | 7B-D, 7B-O, 72B, MolmoE 1B |
| **License** | Apache 2.0 |
| **Run locally?** | Yes — 7B needs ~16GB VRAM |
| **HF page** | https://huggingface.co/allenai/Molmo-7B-D-0924 |
| **Technical understanding** | Generalist. Trained on PixMo dataset (1M curated image-text pairs). Decent on charts but not specialized. |
| **Benchmarks** (7B-D) | ChartQA test: ~60, DocQA: ~66, InfoVQA: ~44, AI2D: ~63. Average score on 11 benchmarks: 77.3 (competitive with GPT-4V on some tasks). |

**Verdict:** Not the best for document-specific tasks. Strong generalist but Granite Vision at 3B beats it on every document/chart benchmark. Good if you need a general-purpose VLM.

---

## 9. DocOwl / mPLUG-DocOwl Series

| Model | Size | License | HF Page |
|---|---|---|---|
| **DocOwl2** | ~9B | Apache 2.0 | https://huggingface.co/mPLUG/DocOwl2 |
| **DocOwl1.5** | Various | Apache 2.0 | Search mPLUG on HF |

**DocOwl2:** Specialized for **OCR-free multi-page document understanding**. Uses "High-resolution DocCompressor" — each page encoded with just 324 tokens. Designed specifically for document QA across multiple pages. Benchmarks: Strong on DocVQA, InfoVQA (exact scores not on model card but reported in paper).

**DocOwl1.5:** Earlier version, still solid for document tasks.

**Verdict:** **Best for multi-page document workflows.** Less general than Qwen2.5-VL but purpose-built for document understanding. The token compression makes it efficient for long documents.

---

## 10. Other VLMs on ChartQA / DocVQA / InfoVQA Leaderboards

Based on leaderboard data from the models above:

| Model | ChartQA | DocVQA | InfoVQA | Notes |
|---|---|---|---|---|
| **Qwen2.5-VL-7B** | **87.3** | **95.7** | **82.6** | Best overall |
| **InternVL2.5-8B** | 84.3 | 93.0 | 77.6 | Strong all-around |
| **Granite Vision 3.1-2B** | **86.0** | 88.0 | 63.0 | Best small model |
| **Phi-4-multimodal-5.6B** | 81.4 | 93.2 | 72.7 | Good + audio |
| **Phi-3.5-vision-4B** | 81.8 | — | — | Older but decent |
| **Idefics3-8B** | — | 87.7 | — | Solid document |
| **SmolVLM2-2.2B** | 68.8 | 80.0 | — | Efficient but weaker |

Additional models to investigate:
- **PaliGemma 2** (Google) — good on DocVQA
- **Pixtral** (Mistral) — 12B, decent on charts
- **LLaVA-OneVision** — strong generalist, decent on documents
- **MiniCPM-V 2.6** — strong OCR capabilities

---

## Circuit/Electronics Diagram Understanding — Papers

Only **one relevant paper** was found on arXiv:

**"A Large Language Model Powered Integrated Circuit Footprint Geometry Understanding"** (arXiv:2508.03725, Jul 2025)
- Treats IC mechanical drawings as images for structured geometric interpretation
- Proposes **LLM4-IC8K** framework with a **two-stage training**: synthetic IC footprint diagrams → real-world datasheet drawings
- Introduces **ICGeo8K dataset**: 8,608 labeled samples of IC footprint geometry
- Sub-tasks: pin counting, center coordinate computation, pin dimension estimation
- Finds that current LMMs "severely suffer from inaccurate geometric perception" for circuit diagrams

**No papers were found** specifically about VLM understanding of electronic **schematic/circuit diagrams** (transistors, resistors, logic gates, etc.). This is a **gap in the research**.

---

## Executive Summary

| Use Case | Best Model |
|---|---|
| **Charts & plots** | Qwen2.5-VL-7B (87.3 ChartQA) or Granite Vision 3.1-2B (86.0, smaller) |
| **Documents (multi-page)** | DocOwl2 (specialized) or Qwen2.5-VL-7B |
| **OCR-heavy workflows** | Qwen2.5-VL-7B (95.7 DocVQA) or Florence-2 (lightweight) |
| **On-device / constrained** | Granite Vision 3.1-2B (best perf/param) or SmolVLM2-2.2B |
| **General purpose + docs** | InternVL2.5-8B or Qwen2.5-VL-7B |
| **Circuit diagrams** | **No existing VLM is good at this** — ICGeo8K paper shows all current models fail at geometric perception of electronic diagrams. This needs custom fine-tuning. |

**Key gap:** No VLM has been specifically trained or benchmarked on electronic circuit schematics (schematic diagrams). The ICGeo8K paper is the closest (IC footprint diagrams), but it's about PCB package geometry, not logic/circuit schematics. This would require a custom dataset + fine-tuning approach.

*Novo passo iniciado*

---

*6 messages | 32 parts | 💰 $0.0162 | ⏱️ 0h00m51s*
