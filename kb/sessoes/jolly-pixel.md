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

Sessão com **6 messages**, **38 parts**, agente **general**, modelo **deepseek-v4-flash** | 💰 $0.0188 | 💾 cache read: 199.6K | ⏱️ 0h00m54s

## 👤 Usuário (2026-06-17 02:26:18 UTC)

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

5. **MinerU alternatives**: Any other free tools similar to MinerU for PDF → structured markdown + images
   - Search: "PDF to structured markdown open source", "PDF extraction with figure separation", "marker PDF extraction"

6. **HuggingFace models**: Search HuggingFace for:
   - "circuit" in models
   - "schematic" in models
   - "technical diagram" in models
   - "engineering drawing" in models

Return all findings with URLs and descriptions. Focus on tools that are FREE and preferably OPEN SOURCE.

## 🤖 Assistente (2026-06-17 02:26:18 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants a comprehensive web search for free/open-source tools that can read and understand technical diagrams, circuit schematics, and engineering drawings. Let me perform multiple web searches to cover all the topics they've listed.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 02:26:22 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good, I got some results from HuggingFace. Let me now do more targeted web searches for each of the categories the user asked about.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 02:26:29 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good, I got a lot of information. Now let me search for more specific tools in the remaining categories.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 02:26:36 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me search for more specific tools for circuit diagram understanding and STEM VLM models.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 02:26:43 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I now have a comprehensive collection of findings. Let me compile this into a well-organized response covering all 6 categories the user asked about.

</details>

### Resposta

Aqui está um resumo abrangente de todas as ferramentas e modelos gratuitos/de código aberto encontrados:

---

## 1. Compreensão de Diagramas de Circuito

**Status atual:** Não existem modelos especializados de código aberto que convertam imagens de circuitos → netlists SPICE. Esta é uma lacuna de pesquisa ativa.

Ferramentas relacionadas encontradas:

| Ferramenta | Descrição | Link |
|---|---|---|
| **DeepPCB** | Detecção de componentes PCB + rastreamento de traços com YOLO/SegFormer | *(extinto/privado)* |
| **PCB-Component-Recognition** | Reconhecimento de componentes em placas de circuito usando CNN | *(extinto/privado)* |
| **Universal-1 (Mathpix)** | Comercial – faz reconhecimento de diagramas, incluindo circuitos, mas é pago | [mathpix.com](https://mathpix.com) |

**Abordagem prática:** Use **Surya** (layout detection) para segmentar figuras de livros didáticos e, em seguida, alimente os recortes de diagramas em um **VLM** como Qwen2.5-VL (ou o Granite Docling 258M como ponto de partida para doc understanding). Nenhum modelo código aberto é treinado especificamente para netlists.

---

## 2. OCR de Diagramas Técnicos

| Ferramenta | Stars | Descrição | Link |
|---|---|---|---|
| **Surya v2** | 20.8k | Modelo VLM de 650M params – OCR multilíngue, análise de layout (detecta `Diagram`, `Equation`, `Table`, `Figure`, `Form`, `ChemicalBlock`, `Code`), ordem de leitura, reconhecimento de tabelas. Layout标签 inclui `ChemicalBlock`, `Diagram` – específico para docs técnicos. | [github.com/datalab-to/surya](https://github.com/datalab-to/surya) |
| **Marker** | 36.2k | Converte PDF → Markdown/JSON estruturado. Usa Surya para OCR/layout, Texify para equações. Pipeline completo para transformers de documentos técnicos. | [github.com/datalab-to/marker](https://github.com/datalab-to/marker) |
| **Docling** | 61.7k | IBM – Análise avançada de PDF (layout, estruturas de tabelas, código, fórmulas, classificação de imagens). Suporta Granite Docling VLM. Saída JSON/DocTags preservando hierarquia. | [github.com/docling-project/docling](https://github.com/docling-project/docling) |
| **NotShrirang/detr-for-engineering-drawing-object-detection** | (41.6M params) | Modelo DETR no HuggingFace para detectar objetos em desenhos de engenharia. | [huggingface.co/NotShrirang](https://huggingface.co/NotShrirang/detr-for-engineering-drawing-object-detection) |
| **Models-Object-Detection-and-OCR-System-for-Engineering-Drawings** | (8B params) | Modelo grande no HF para detecção + OCR em desenhos de engenharia. | [huggingface.co/Nghiaub257](https://huggingface.co/Nghiaub257/Models-Object-Detection-and-OCR-System-for-Engineering-Drawings) |

---

## 3. Extração de Figuras de PDF + Legendagem

| Ferramenta | Descrição | Link |
|---|---|---|
| **pdfigures2** (Allen AI) | Extrai figuras, tabelas, legendas, títulos de seções de PDFs acadêmicos. Scala. Saída: bounding boxes, texto da figura, texto da legenda, nome da figura. | [github.com/allenai/pdffigures2](https://github.com/allenai/pdffigures2) |
| **GROBID** | Extrai/estrutura PDFs acadêmicos → TEI XML. Cobre metadados, referências, texto completo, coordenadas de figuras/tabelas. Muito utilizado em produção (Semantic Scholar, ResearchGate). | [github.com/kermitt2/grobid](https://github.com/kermitt2/grobid) |
| **Nougat** (Meta/Facebook) | OCR neural ponta a ponta para documentos acadêmicos. Converte PDF → Mathpix Markdown (.mmd) com LaTeX. Não extrai figuras separadamente, mas as coloca inline. | [github.com/facebookresearch/nougat](https://github.com/facebookresearch/nougat) |
| **Marker** | Extrai e salva imagens de PDFs, preserva legendas. Saída markdown com links de imagens + metadados de bounding box. | [github.com/datalab-to/marker](https://github.com/datalab-to/marker) |

---

## 4. Modelos Multimodais Ajustados para STEM

| Modelo | Params | Descrição | Link |
|---|---|---|---|
| **Granite Docling 258M** | 258M | IBM – VLM compacto para conversão de documentos. Suporta equações, código, tabelas, gráficos. Fine-tunado em SynthCodeNet + SynthFormulaNet + SynthChartNet. Apache 2.0. | [huggingface.co/ibm-granite/granite-docling-258M](https://huggingface.co/ibm-granite/granite-docling-258M) |
| **Donut** (NAVER) | Base ~200M | Transformer de compreensão de documentos sem OCR. Modelo base para fine-tuning em tarefas como classificação de documentos/extração. MIT. | [huggingface.co/naver-clova-ix/donut-base](https://huggingface.co/naver-clova-ix/donut-base) |
| **Texify** (depreciado → Surya) | – | OCR de equações matemáticas → LaTeX. Agora incorporado ao Surya. | [github.com/VikParuchuri/texify](https://github.com/VikParuchuri/texify) |
| **Surya v2** | 650M | Único VLM para layout + OCR + tabelas + equações matemáticas (tags `<math>`). 83,3% no olmOCR-bench. | [github.com/datalab-to/surya](https://github.com/datalab-to/surya) |

HuggingFace para STEM geral: **0 resultados** para termos `circuit schematic`, `stem diagram`, `technical diagram`. Apenas 3 modelos para `engineering drawing` — limitados a detecção de objetos, não compreensão completa.

---

## 5. Alternativas ao MinerU

| Ferramenta | Descrição | Diferença do MinerU | Link |
|---|---|---|---|
| **Marker** (Datalab) | PDF/DOCX/PPTX/XLSX → Markdown/JSON/HTML. Extrai imagens, equações, tabelas. GPU/CPU/MPS. **36.2k estrelas.** | + Mais rápido, + LLM híbrido opcional, + Extração estruturada (JSON schema). Code GPL. | [github.com/datalab-to/marker](https://github.com/datalab-to/marker) |
| **Docling** (IBM) | PDF/DOCX/PPTX/XLSX/HTML/EPUB/áudio → Documento unificado → Markdown/JSON/HTML/DocTags. Suporta VLM + pipeline tradicional. **61.7k estrelas.** MIT. | + Mais formatos de entrada (áudio, email), + Suporte nativo a VLM (Granite Docling), + Padrão da indústria (LF AI & Data). | [github.com/docling-project/docling](https://github.com/docling-project/docling) |
| **Nougat** (Meta) | PDF → Markdown com LaTeX. Focado em artigos acadêmicos. CC-BY-NC. | – Apenas PDF, – Licença restritiva, + Melhor para docs matemáticos. | [github.com/facebookresearch/nougat](https://github.com/facebookresearch/nougat) |
| **GROBID** | PDF → TEI XML estruturado. Java. Focado em metadados de literatura científica. Apache 2.0. | – Sem saída Markdown, + Melhor para metadados de referências, + Produção comprovada (Semantic Scholar). | [github.com/kermitt2/grobid](https://github.com/kermitt2/grobid) |

**Recomendação:** **Docling** (MIT, mais formatos, mais ativo) ou **Marker** (mais rápido, LLM híbrido). Ambos superam MinerU em precisão nos benchmarks.

---

## 6. Modelos do HuggingFace (Resumo)

Pesquisado: `circuit`, `schematic`, `technical diagram`, `engineering drawing`, `stem diagram`

| Consulta | Resultados |
|---|---|
| `circuit schematic` | **0 modelos** |
| `technical diagram` | **0 modelos** |
| `stem diagram` | **0 modelos** |
| `engineering drawing` | **3 modelos**: DETR para detecção de objetos (41.6M), modelo ensemble 8B, FRCNN X101. Todos apenas **detecção de objetos**, não compreensão semântica. |

---

## Conclusão: Lacuna Principal

**Não existe ferramenta open source que entenda diagramas de circuitos** (reconhecer um resistor vs. capacitor vs. transistor e extrair uma netlist). O ecossistema cobre bem:

- ✅ OCR/layout de documentos → **Surya + Marker + Docling**
- ✅ Extração/estruturação de PDFs acadêmicos → **Docling, GROBID, pdffigures2**
- ✅ OCR de equações matemáticas → **Surya (texify integrado)**
- ✅ Detecção de objetos em desenhos de engenharia → **Modelos DETR/YOLO (HF)**

Mas diagramas de circuitos compreendendo relacionamentos espaciais e reconhecimento de componentes → **apenas soluções comerciais** (Mathpix, Wolfram Alpha) ou pesquisa (sem repositórios públicos). Isso exigiria fine-tuning de um VLM (Qwen2.5-VL, Granite Docling) ou treinar um modelo específico do zero.

*Novo passo iniciado*

---

*6 messages | 38 parts | 💰 $0.0188 | ⏱️ 0h00m54s*
