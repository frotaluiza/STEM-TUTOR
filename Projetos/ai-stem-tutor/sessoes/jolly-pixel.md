---
title: "jolly-pixel"
slug: "jolly-pixel"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: jolly-pixel
title: "Research technical diagram OCR (@general subagent)"
date: 2026-06-17
agent: general
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h00m54s
messages: 6
parts: 38
cost: 0.018761
tokens_input: 122225
tokens_output: 3755
tokens_reasoning: 140
tokens_cache_read: 199552
tokens_cache_write: 0
created: "2026-06-17 02:26:18 UTC"
updated: "2026-06-17 02:27:13 UTC"
---

SessÃ£o com **6 messages**, **38 parts**, agente **general**, modelo **deepseek-v4-flash** | ðŸ’° $0.0188 | ðŸ’¾ cache read: 199.6K | â±ï¸ 0h00m54s

## ðŸ‘¤ UsuÃ¡rio (2026-06-17 02:26:18 UTC)

Search the web extensively for free/open-source tools that can READ and UNDERSTAND technical diagrams, circuit schematics, and engineering drawings from textbooks. Specifically:

1. **Circuit diagram understanding**: Tools/Models that parse circuit schematics (resistors, capacitors, transistors, etc.) and output netlists or descriptions
   - Search: "circuit diagram recognition deep learning", "schematic understanding AI", "PCB netlist extraction from image"
   - Any HuggingFace models for circuit/electronics diagram understanding

2. **Technical diagram OCR**: Tools that go beyond general OCR and understand the structure of technical diagrams
   - Search: "technical diagram understanding open source", "engineering drawing OCR", "figure understanding AI"
   - Look for: datasets, models, papers

3. **PDF figure extraction + captioning**: Tools that specifically extract figures from academic PDFs and generate captions/descriptions
   - Search: "PDF figure extraction and captioning", "automatic diagram captioning", "scientific figure understanding"
   - Look for: Nougat, GROBID, PDFFigures, PaLI, or similar

4. **Multimodal models fine-tuned for STEM diagrams**: 
   - Search: "STEM diagram understanding model", "scientific figure QA open source", "math formula OCR"
   - Any open-source VLM fine-tuned on technical content

5. **MinerU alternatives**: Any other free tools similar to MinerU for PDF â†’ structured markdown + images
   - Search: "PDF to structured markdown open source", "PDF extraction with figure separation", "marker PDF extraction"

6. **HuggingFace models**: Search HuggingFace for:
   - "circuit" in models
   - "schematic" in models
   - "technical diagram" in models
   - "engineering drawing" in models

Return all findings with URLs and descriptions. Focus on tools that are FREE and preferably OPEN SOURCE.

## ðŸ¤– Assistente (2026-06-17 02:26:18 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants a comprehensive web search for free/open-source tools that can read and understand technical diagrams, circuit schematics, and engineering drawings. Let me perform multiple web searches to cover all the topics they've listed.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 02:26:22 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Good, I got some results from HuggingFace. Let me now do more targeted web searches for each of the categories the user asked about.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 02:26:29 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Good, I got a lot of information. Now let me search for more specific tools in the remaining categories.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 02:26:36 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me search for more specific tools for circuit diagram understanding and STEM VLM models.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 02:26:43 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

I now have a comprehensive collection of findings. Let me compile this into a well-organized response covering all 6 categories the user asked about.

</details>

### Resposta

Aqui estÃ¡ um resumo abrangente de todas as ferramentas e modelos gratuitos/de cÃ³digo aberto encontrados:

---

## 1. CompreensÃ£o de Diagramas de Circuito

**Status atual:** NÃ£o existem modelos especializados de cÃ³digo aberto que convertam imagens de circuitos â†’ netlists SPICE. Esta Ã© uma lacuna de pesquisa ativa.

Ferramentas relacionadas encontradas:

| Ferramenta | DescriÃ§Ã£o | Link |
|---|---|---|
| **DeepPCB** | DetecÃ§Ã£o de componentes PCB + rastreamento de traÃ§os com YOLO/SegFormer | *(extinto/privado)* |
| **PCB-Component-Recognition** | Reconhecimento de componentes em placas de circuito usando CNN | *(extinto/privado)* |
| **Universal-1 (Mathpix)** | Comercial â€“ faz reconhecimento de diagramas, incluindo circuitos, mas Ã© pago | [mathpix.com](https://mathpix.com) |

**Abordagem prÃ¡tica:** Use **Surya** (layout detection) para segmentar figuras de livros didÃ¡ticos e, em seguida, alimente os recortes de diagramas em um **VLM** como Qwen2.5-VL (ou o Granite Docling 258M como ponto de partida para doc understanding). Nenhum modelo cÃ³digo aberto Ã© treinado especificamente para netlists.

---

## 2. OCR de Diagramas TÃ©cnicos

| Ferramenta | Stars | DescriÃ§Ã£o | Link |
|---|---|---|---|
| **Surya v2** | 20.8k | Modelo VLM de 650M params â€“ OCR multilÃ­ngue, anÃ¡lise de layout (detecta `Diagram`, `Equation`, `Table`, `Figure`, `Form`, `ChemicalBlock`, `Code`), ordem de leitura, reconhecimento de tabelas. Layoutæ ‡ç­¾ inclui `ChemicalBlock`, `Diagram` â€“ especÃ­fico para docs tÃ©cnicos. | [github.com/datalab-to/surya](https://github.com/datalab-to/surya) |
| **Marker** | 36.2k | Converte PDF â†’ Markdown/JSON estruturado. Usa Surya para OCR/layout, Texify para equaÃ§Ãµes. Pipeline completo para transformers de documentos tÃ©cnicos. | [github.com/datalab-to/marker](https://github.com/datalab-to/marker) |
| **Docling** | 61.7k | IBM â€“ AnÃ¡lise avanÃ§ada de PDF (layout, estruturas de tabelas, cÃ³digo, fÃ³rmulas, classificaÃ§Ã£o de imagens). Suporta Granite Docling VLM. SaÃ­da JSON/DocTags preservando hierarquia. | [github.com/docling-project/docling](https://github.com/docling-project/docling) |
| **NotShrirang/detr-for-engineering-drawing-object-detection** | (41.6M params) | Modelo DETR no HuggingFace para detectar objetos em desenhos de engenharia. | [huggingface.co/NotShrirang](https://huggingface.co/NotShrirang/detr-for-engineering-drawing-object-detection) |
| **Models-Object-Detection-and-OCR-System-for-Engineering-Drawings** | (8B params) | Modelo grande no HF para detecÃ§Ã£o + OCR em desenhos de engenharia. | [huggingface.co/Nghiaub257](https://huggingface.co/Nghiaub257/Models-Object-Detection-and-OCR-System-for-Engineering-Drawings) |

---

## 3. ExtraÃ§Ã£o de Figuras de PDF + Legendagem

| Ferramenta | DescriÃ§Ã£o | Link |
|---|---|---|
| **pdfigures2** (Allen AI) | Extrai figuras, tabelas, legendas, tÃ­tulos de seÃ§Ãµes de PDFs acadÃªmicos. Scala. SaÃ­da: bounding boxes, texto da figura, texto da legenda, nome da figura. | [github.com/allenai/pdffigures2](https://github.com/allenai/pdffigures2) |
| **GROBID** | Extrai/estrutura PDFs acadÃªmicos â†’ TEI XML. Cobre metadados, referÃªncias, texto completo, coordenadas de figuras/tabelas. Muito utilizado em produÃ§Ã£o (Semantic Scholar, ResearchGate). | [github.com/kermitt2/grobid](https://github.com/kermitt2/grobid) |
| **Nougat** (Meta/Facebook) | OCR neural ponta a ponta para documentos acadÃªmicos. Converte PDF â†’ Mathpix Markdown (.mmd) com LaTeX. NÃ£o extrai figuras separadamente, mas as coloca inline. | [github.com/facebookresearch/nougat](https://github.com/facebookresearch/nougat) |
| **Marker** | Extrai e salva imagens de PDFs, preserva legendas. SaÃ­da markdown com links de imagens + metadados de bounding box. | [github.com/datalab-to/marker](https://github.com/datalab-to/marker) |

---

## 4. Modelos Multimodais Ajustados para STEM

| Modelo | Params | DescriÃ§Ã£o | Link |
|---|---|---|---|
| **Granite Docling 258M** | 258M | IBM â€“ VLM compacto para conversÃ£o de documentos. Suporta equaÃ§Ãµes, cÃ³digo, tabelas, grÃ¡ficos. Fine-tunado em SynthCodeNet + SynthFormulaNet + SynthChartNet. Apache 2.0. | [huggingface.co/ibm-granite/granite-docling-258M](https://huggingface.co/ibm-granite/granite-docling-258M) |
| **Donut** (NAVER) | Base ~200M | Transformer de compreensÃ£o de documentos sem OCR. Modelo base para fine-tuning em tarefas como classificaÃ§Ã£o de documentos/extraÃ§Ã£o. MIT. | [huggingface.co/naver-clova-ix/donut-base](https://huggingface.co/naver-clova-ix/donut-base) |
| **Texify** (depreciado â†’ Surya) | â€“ | OCR de equaÃ§Ãµes matemÃ¡ticas â†’ LaTeX. Agora incorporado ao Surya. | [github.com/VikParuchuri/texify](https://github.com/VikParuchuri/texify) |
| **Surya v2** | 650M | Ãšnico VLM para layout + OCR + tabelas + equaÃ§Ãµes matemÃ¡ticas (tags `<math>`). 83,3% no olmOCR-bench. | [github.com/datalab-to/surya](https://github.com/datalab-to/surya) |

HuggingFace para STEM geral: **0 resultados** para termos `circuit schematic`, `stem diagram`, `technical diagram`. Apenas 3 modelos para `engineering drawing` â€” limitados a detecÃ§Ã£o de objetos, nÃ£o compreensÃ£o completa.

---

## 5. Alternativas ao MinerU

| Ferramenta | DescriÃ§Ã£o | DiferenÃ§a do MinerU | Link |
|---|---|---|---|
| **Marker** (Datalab) | PDF/DOCX/PPTX/XLSX â†’ Markdown/JSON/HTML. Extrai imagens, equaÃ§Ãµes, tabelas. GPU/CPU/MPS. **36.2k estrelas.** | + Mais rÃ¡pido, + LLM hÃ­brido opcional, + ExtraÃ§Ã£o estruturada (JSON schema). Code GPL. | [github.com/datalab-to/marker](https://github.com/datalab-to/marker) |
| **Docling** (IBM) | PDF/DOCX/PPTX/XLSX/HTML/EPUB/Ã¡udio â†’ Documento unificado â†’ Markdown/JSON/HTML/DocTags. Suporta VLM + pipeline tradicional. **61.7k estrelas.** MIT. | + Mais formatos de entrada (Ã¡udio, email), + Suporte nativo a VLM (Granite Docling), + PadrÃ£o da indÃºstria (LF AI & Data). | [github.com/docling-project/docling](https://github.com/docling-project/docling) |
| **Nougat** (Meta) | PDF â†’ Markdown com LaTeX. Focado em artigos acadÃªmicos. CC-BY-NC. | â€“ Apenas PDF, â€“ LicenÃ§a restritiva, + Melhor para docs matemÃ¡ticos. | [github.com/facebookresearch/nougat](https://github.com/facebookresearch/nougat) |
| **GROBID** | PDF â†’ TEI XML estruturado. Java. Focado em metadados de literatura cientÃ­fica. Apache 2.0. | â€“ Sem saÃ­da Markdown, + Melhor para metadados de referÃªncias, + ProduÃ§Ã£o comprovada (Semantic Scholar). | [github.com/kermitt2/grobid](https://github.com/kermitt2/grobid) |

**RecomendaÃ§Ã£o:** **Docling** (MIT, mais formatos, mais ativo) ou **Marker** (mais rÃ¡pido, LLM hÃ­brido). Ambos superam MinerU em precisÃ£o nos benchmarks.

---

## 6. Modelos do HuggingFace (Resumo)

Pesquisado: `circuit`, `schematic`, `technical diagram`, `engineering drawing`, `stem diagram`

| Consulta | Resultados |
|---|---|
| `circuit schematic` | **0 modelos** |
| `technical diagram` | **0 modelos** |
| `stem diagram` | **0 modelos** |
| `engineering drawing` | **3 modelos**: DETR para detecÃ§Ã£o de objetos (41.6M), modelo ensemble 8B, FRCNN X101. Todos apenas **detecÃ§Ã£o de objetos**, nÃ£o compreensÃ£o semÃ¢ntica. |

---

## ConclusÃ£o: Lacuna Principal

**NÃ£o existe ferramenta open source que entenda diagramas de circuitos** (reconhecer um resistor vs. capacitor vs. transistor e extrair uma netlist). O ecossistema cobre bem:

- âœ… OCR/layout de documentos â†’ **Surya + Marker + Docling**
- âœ… ExtraÃ§Ã£o/estruturaÃ§Ã£o de PDFs acadÃªmicos â†’ **Docling, GROBID, pdffigures2**
- âœ… OCR de equaÃ§Ãµes matemÃ¡ticas â†’ **Surya (texify integrado)**
- âœ… DetecÃ§Ã£o de objetos em desenhos de engenharia â†’ **Modelos DETR/YOLO (HF)**

Mas diagramas de circuitos compreendendo relacionamentos espaciais e reconhecimento de componentes â†’ **apenas soluÃ§Ãµes comerciais** (Mathpix, Wolfram Alpha) ou pesquisa (sem repositÃ³rios pÃºblicos). Isso exigiria fine-tuning de um VLM (Qwen2.5-VL, Granite Docling) ou treinar um modelo especÃ­fico do zero.

*Novo passo iniciado*

---

*6 messages | 38 parts | ðŸ’° $0.0188 | â±ï¸ 0h00m54s*

