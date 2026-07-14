---
title: "clever-cactus"
slug: "clever-cactus"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: clever-cactus
title: "Research Mathpix alternatives (@general subagent)"
date: 2026-06-02
agent: general
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h00m43s
messages: 5
parts: 26
cost: 0
tokens_input: 75908
tokens_output: 2070
tokens_reasoning: 1507
tokens_cache_read: 85888
tokens_cache_write: 0
created: "2026-06-02 01:07:16 UTC"
updated: "2026-06-02 01:07:59 UTC"
---

SessÃ£o com **5 messages**, **26 parts**, agente **general**, modelo **deepseek-v4-flash-free** | ðŸ’¾ cache read: 85.9K | â±ï¸ 0h00m43s

## ðŸ‘¤ UsuÃ¡rio (2026-06-02 01:07:16 UTC)

Research extensively on the internet for tools and services that can do what Mathpix does - OCR for mathematical equations, converting printed/handwritten math to LaTeX. I need:

1. A comprehensive list of alternative tools to Mathpix (both free/paid, open-source/closed)
2. For each tool, note: name, API availability, open-source status, pricing model, accuracy level, supported formats (image PDF equation)
3. Specifically look for open-source options first
4. Look for tools that can be integrated programmatically (API or CLI)

Search for:
- Mathpix alternatives 2026
- LaTeX OCR open source
- Equation recognition tools
- Image to LaTeX converters
- Mathematical formula OCR API
- Tools like Mathpix but free
- GitHub projects for math OCR
- pix2tex, LaTeX-OCR, MathOCR, etc.

Return a structured table with columns: Tool Name, Open Source (Yes/No), Has API (Yes/No), Pricing, Key Features, Integration Method (API/CLI/lib), Notes

## ðŸ¤– Assistente (2026-06-02 01:07:16 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants a comprehensive research on Mathpix alternatives for OCR of mathematical equations. Let me search the web extensively for this information.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-02 01:07:25 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me search for more specific tools that I want to make sure I cover comprehensively.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-02 01:07:31 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me also search for a few more tools that I want to cover in the comparison - InftyReader, SimpleTex, Mathpix itself for reference, and some other cloud APIs.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-02 01:07:37 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have enough information to compile a comprehensive comparison table. Let me organize the data I've gathered.

## Open Source Tools:

1. **pix2tex (LaTeX-OCR)** - GitHub: lukas-blecher/LaTeX-OCR - 16.4k stars, MIT license
   - Open source: Yes (MIT)
   - API: Yes (Python API + CLI + built-in API server)
   - Pricing: Free
   - Key features: ViT-based, ~88% exact match, 93% BLEU, GUI available
   - Integration: CLI, Python lib, API server (Streamlit), Docker

2. **Pix2Text** - GitHub: breezedeus/Pix2Text - 3.1k stars, MIT license
   - Open source: Yes (MIT)
   - API: Yes (Python API + CLI + HTTP service)
   - Pricing: Free
   - Key features: Layout analysis, table OCR, math formula recognition, 80+ languages, Markdown output
   - Integration: CLI, Python lib, HTTP service

3. **TexTeller** - GitHub: OleehyO/TexTeller - Apache 2.0
   - Open source: Yes (Apache 2.0)
   - API: Yes (Python API + CLI + server)
   - Pricing: Free
   - Key features: Trained on 80M image-formula pairs, highest accuracy, supports handwritten formulas, Chinese/English mixed
   - Integration: CLI, Python lib, Docker

4. **RapidLaTeXOCR** - GitHub: RapidAI/RapidLaTeXOCR - 385 stars, MIT
   - Open source: Yes (MIT)
   - API: Yes (Python API + CLI)
   - Pricing: Free
   - Key features: ONNX-based, faster inference, easier deployment
   - Integration: CLI, Python lib (pip install rapid_latex_ocr)

5. **DeepSeek-OCR** - GitHub: deepseek-ai/DeepSeek-OCR - 23.1k stars, MIT
   - Open source: Yes (MIT)
   - API: Yes (Python API via transformers + vLLM)
   - Pricing: Free
   - Key features: 3B params, 97% accuracy, formula recognition, table extraction, Markdown output, multi-language
   - Integration: Python lib, vLLM, CLI

6. **MathOCR** - GitHub: chungkwong/MathOCR - 176 stars, GPL-3.0
   - Open source: Yes (GPL-3.0)
   - API: Limited (Java library + CLI)
   - Pricing: Free
   - Key features: Pure Java, printed scientific document recognition, pre-alpha stage
   - Integration: Java lib, CLI

7. **Sumen** - GitHub: hoang-quoc-trung/sumen
   - Open source: Yes
   - API: TBD
   - Pricing: Free
   - Key features: End-to-end transformer, large dataset

8. **Im2Latex** (research paper) - Open source model weights available
   - Open source: Yes
   - API: Via transformers
   - Pricing: Free
   - Key features: Swin Transformer + GPT-2 decoder, 240M params, BLEU 0.67

9. **PaddleOCR (LaTeX-OCR module)** - GitHub: PaddlePaddle/PaddleOCR
   - Open source: Yes (Apache 2.0)
   - API: Yes (Python API)
   - Pricing: Free
   - Key features: Implements LaTeX-OCR in PaddlePaddle, formula recognition pipeline

## Commercial/Paid Tools:

1. **Mathpix** - mathpix.com
   - Open source: No
   - API: Yes (Convert API)
   - Pricing: Free tier (10 PDF pages, 10 images/month), Pro $4.99/mo, API $0.002/image
   - Features: Most accurate STEM OCR, chemistry, handwriting, tables, full PDF conversion
   - Integration: REST API, Python SDK

2. **Tiny OCR** - tiny-ocr.com
   - Open source: No
   - API: Yes
   - Pricing: $0.001/image, 50 free/month
   - Features: STEM-native, chemistry (SMILES), handwriting, 99.7% STEM accuracy, <50ms latency
   - Integration: REST API

3. **ScanRead.ai**
   - Open source: No
   - API: Yes
   - Pricing: Free 20 pages/day, Pro $10/mo
   - Features: Mathâ†’LaTeX, CJK, handwriting, tables

4. **SimpleTex**
   - Open source: No
   - API: Yes
   - Pricing: Check their site

5. **InftyReader** - inftyreader.org
   - Open source: No
   - API: No (Desktop app)
   - Pricing: Â£595 one-time
   - Features: Mature math OCR, scientific documents, LaTeX/MathML/HTML output, Braille support

6. **OCR.space**
   - Open source: No
   - API: Yes (REST API)
   - Pricing: Free (25K requests/month), Pro $30/mo, Pro PDF $60/mo
   - Features: General OCR with math support via Engine 2/3

7. **Google Cloud Vision API**
   - Open source: No
   - API: Yes
   - Pricing: $1.50/1000 pages, 1000 free/month
   - Features: General OCR, not specialized for math

8. **AWS Textract**
   - Open source: No
   - API: Yes
   - Pricing: $1.50/1000 pages basic OCR
   - Features: Tables, forms, no math specialization

9. **ABBYY OCR API**
   - Open source: No
   - API: Yes
   - Pricing: Custom/Enterprise
   - Features: Document AI, structured extraction

10. **Mistral OCR**
    - Open source: No (model available)
    - API: Yes (via Mistral platform)
    - Pricing: Check Mistral pricing
    - Features: Strong document layout understanding

11. **Free web tools** (online only, no API):
    - FreeAIOCR.com
    - DeepSeekOCR.io (online)
    - i2OCR.com
    - Mathcheap.xyz
    - LaTeX-Tools.online
    - YesChat.ai Image to LaTeX

Let me organize this into a comprehensive table.

</details>

### Resposta

Based on extensive research, here is the comprehensive comparison:

## Mathpix Alternatives â€” Comprehensive Comparison (2026)

| Tool | Open Source | Has API | Pricing | Key Features | Integration Method | Notes |
|---|---|---|---|---|---|---|
| **pix2tex (LaTeX-OCR)** | Yes (MIT) | Yes | Free | ViT encoder + GPT-2 decoder, ~88% exact match, GUI, handwritten support | CLI, Python lib, API server, Docker | 16.4k â˜… on GitHub; best open-source starting point |
| **Pix2Text** | Yes (MIT) | Yes | Free | Layout analysis, table OCR, math â†’ LaTeX, 80+ languages, Markdown output | CLI, Python lib, HTTP service | 3.1k â˜…; full Mathpix alternative pipeline |
| **TexTeller** | Yes (Apache 2.0) | Yes | Free | Trained on 80M image-formula pairs, highest open-source accuracy, handwritten + Chinese | CLI, Python lib, Docker, HuggingFace | Superior generalization vs pix2tex |
| **RapidLaTeXOCR** | Yes (MIT) | Yes | Free | ONNX-based port of pix2tex, faster inference, easier deployment | CLI, Python lib (`pip install rapid_latex_ocr`) | 385 â˜…; good for production deployment |
| **DeepSeek-OCR** | Yes (MIT) | Yes | Free | 3B param VLM, 97% accuracy, formula+table+layout, 100 languages | Transformers, vLLM, REST API | 23.1k â˜…; SOTA open-source OCR |
| **Sumen** | Yes | TBD | Free | End-to-end transformer, 350M params, BLEU 0.47 | Python lib | Research-focused, less documented |
| **Im2Latex** | Yes | Via HF | Free | Swin + GPT-2, 240M params, BLEU 0.67 | Transformers | Academic project, good for fine-tuning |
| **PaddleOCR (LaTeX-OCR)** | Yes (Apache 2.0) | Yes | Free | Baidu's framework, formula recognition pipeline | Python lib (PaddleOCR) | Good if already using PaddlePaddle |
| **MathOCR (chungkwong)** | Yes (GPL-3.0) | Limited | Free | Pure Java, printed doc recognition | Java lib, CLI | Pre-alpha, not production-ready |
| **Mathpix** | No | Yes (REST + Python SDK) | Free tier (10 pg/mo), Pro $4.99/mo, API $0.002/img | Gold standard STEM OCR, chemistry, handwriting, full PDF conversion | REST API, Python SDK | Most accurate but expensive at scale |
| **Tiny OCR** | No | Yes (REST) | $0.001/img, 50 free/mo | 99.7% STEM accuracy, <50ms latency, SMILES for chemistry | REST API | New entrant; chemistry-native |
| **InftyReader** | No | No (desktop app) | Â£595 one-time | Mature math OCR for scientific docs, Braille output | Desktop GUI | Good for archival, no programmatic use |
| **OCR.space** | No | Yes (REST) | Free (25K/mo), Pro $30/mo | General OCR with math engine, 100+ languages | REST API | Math not specialized but affordable |
| **SimpleTex** | No | Yes | Freemium | Online + API, LaTeX/Markdown output | REST API | Chinese origin, good accuracy |
| **ScanRead.ai** | No | Yes | Free 20 pg/day, Pro $10/mo | Mathâ†’LaTeX, CJK, handwriting, 22 specialized tools | REST API | Good free tier for Mathpix-like needs |
| **ABBYY OCR API** | No | Yes | Enterprise/custom | Document AI, structured extraction | REST API | Enterprise-grade, not math-specific |
| **Google Cloud Vision** | No | Yes (REST/ gRPC) | $1.50/1000 pg, 1000 free/mo | General OCR, no math specialization | REST API, client libs | Use only for printed text |
| **AWS Textract** | No | Yes (REST) | $1.50/1000 pg basic OCR | Tables & forms, no math support | SDKs, REST API | Not suitable for equations |
| **Mistral OCR** | Model weights available | Yes | Usage-based | Strong document layout, VLM-based | REST API, self-host | New; good for complex layouts |

### Free Online Tools (No API, Web Only)
- **DeepSeekOCR.io** â€” free online, formula â†’ LaTeX, no signup
- **FreeAIOCR.com** â€” math image â†’ LaTeX, free + no signup
- **i2OCR.com** â€” free math equation OCR, premium batch option
- **Mathcheap.xyz** â€” completely free, OCR + LaTeX editor, no login
- **LaTeX-Tools.online** â€” OCR + handwriting + table â†’ LaTeX, 100% free
- **YesChat.ai** â€” image â†’ LaTeX via chat UI

### Top Recommendations

**Best open-source (self-hosted):** Start with **pix2tex/LaTeX-OCR** for pure equation â†’ LaTeX. If you need layout + tables + full document â†’ Markdown, use **Pix2Text**. For highest accuracy, use **TexTeller** (80M training pairs) or **DeepSeek-OCR** (general document understanding with math).

**Best free API:** **OCR.space** (25K requests/mo free) or **Mathcheap.xyz** (unlimited, no signup).

**Best paid API (if accuracy > cost):** **Mathpix** remains the gold standard for STEM OCR. **Tiny OCR** is a strong new competitor at 10x cheaper.

**Best CLI/library integration:** `pip install pix2tex` for math-only; `pip install pix2text` for full document pipeline; `pip install rapid_latex_ocr` for faster ONNX-based inference.

*Novo passo iniciado*

---

*5 messages | 26 parts | ðŸ’° $0.0000 | â±ï¸ 0h00m43s*

