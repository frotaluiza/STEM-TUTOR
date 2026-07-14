---
title: "misty-canyon"
slug: "misty-canyon"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: misty-canyon
title: "DeepTutor KB and RAG analysis (@explore subagent)"
date: 2026-06-17
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h01m38s
messages: 16
parts: 114
cost: 0.022351
tokens_input: 123447
tokens_output: 8553
tokens_reasoning: 787
tokens_cache_read: 876288
tokens_cache_write: 0
created: "2026-06-17 01:57:30 UTC"
updated: "2026-06-17 01:59:09 UTC"
---

SessÃ£o com **16 messages**, **114 parts**, agente **explore**, modelo **deepseek-v4-flash** | ðŸ’° $0.0224 | ðŸ’¾ cache read: 876.3K | â±ï¸ 0h01m38s

## ðŸ‘¤ UsuÃ¡rio (2026-06-17 01:57:30 UTC)

Very thorough exploration of the DeepTutor codebase at C:\Users\frota\Documents\Projetos\AI TUTOR\ to answer these specific questions:

1. **Knowledge Base (KB) system**: How does DeepTutor handle knowledge bases / RAG? Look for:
   - Any "knowledge_base", "kb", "knowledge", "rag", "retrieval" directories or files
   - How documents are ingested (PDF, markdown, etc.)
   - How KBs are stored and queried
   - Configuration for KBs

2. **PDF processing**: Can DeepTutor process PDFs? Look for:
   - Any PDF parsing libraries (PyPDF2, pdfplumber, pdfminer, etc.) in pyproject.toml or requirements.txt
   - Any document ingestion pipelines
   - OCR capabilities (tesseract, easyocr, etc.)

3. **Image understanding**: 
   - Does the LLM integration support multimodal (image inputs)?
   - Any image description/analysis tools?
   - Can the visualize capability or any agent process images?

4. **Data directory structure**: Look at:
   - What's in C:\Users\frota\Documents\Projetos\AI TUTOR\data\
   - How user knowledge is organized
   - Any existing document collections

5. **RAG implementation details**:
   - Embedding models used
   - Chunking strategy
   - Vector store (ChromaDB, FAISS, etc.)
   - Retrieval parameters

Return VERY detailed findings about each of these areas, including specific file paths and code patterns.

## ðŸ¤– Assistente (2026-06-17 01:57:30 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants a very thorough exploration of the DeepTutor codebase. Let me start by understanding the structure of the project and then search for specific patterns related to their questions.

Let me begin with multiple parallel searches to understand the codebase structure.

</details>

### Resposta

I'll start with a broad exploration of the codebase structure, then drill into each area.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:57:34 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me now dig deeper into the specific areas. I need to:
1. Read the main pyproject.toml for dependencies
2. Read the requirements.txt
3. Look at the deeptutor/ directory structure
4. Read the KB config files
5. Search for RAG/knowledge/PDF/image related code

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:57:37 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Great! I can see the structure now. Key findings so far:
1. DeepTutor uses LlamaIndex as the RAG provider
2. PyMuPDF, pypdf, pdfplumber are all included for PDF processing
3. There's a `knowledge/` directory in the codebase
4. There's `deeptutor/knowledge/` which likely contains the RAG/knowledge base implementation

Let me now explore the `knowledge/` directory, the RAG-related code, and search for image understanding capabilities.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:57:41 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Excellent! Now I need to read the key files for RAG, knowledge management, PDF processing, and image understanding. Let me read the most important files in parallel.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:57:44 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Great progress! Now I need to read the key RAG service files, the embedding configuration, the document ingestion pipeline, the PDF parsing code, the vision/image tools, and more. Let me continue with a deep dive into the specific areas.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:57:48 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me continue exploring the LlamaIndex pipeline, the embedding adapters, the RAG smart retriever, file routing, and the document ingestion code (add_documents, initializer).

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:57:52 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me read the LlamaIndex pipeline and related files for chunking strategy, retrieval parameters, embedding adapters, document loading, etc.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:57:57 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Excellent! I'm getting a very clear picture now. Let me continue looking at:
1. The storage.py file (how the index is created and queries)
2. The config.py in the llamaindex pipeline
3. The vision/image_utils.py for image processing
4. The embedding client/adapter details
5. The document extractor utility
6. The initializer.py
7. Search for OCR or mineru references

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:58:02 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me look for the document extractor utility (used in document_loader.py), the embedding adapters, the LLM client (for multimodal support), and any OCR/mineru references. Let me also look at the visualize capability and other vision-related code.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:58:08 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Great! Now let me read the document extractor (for PDF processing), the LLM client for multimodal, the miners backends, and the embedding adapters. Let me also check the embedding_signature.py and look at the settings.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:58:13 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me also look at the MinerU cloud backend, the embedding adapters, the LLM client for multimodal support, and the main user settings file. Let me also look at the settings files for the embedding model catalog and the visualize capability.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:58:18 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me also look at the LLM client to understand multimodal support and how the visualize capability works. Let me also check the provider_runtime for embedding providers and the knowledge progress tracker.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:58:22 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me look at the LLM multimodal support, the visualize capability, and see if there are any image-related tools like a vision solver.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:58:26 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

I now have a comprehensive picture of the DeepTutor codebase. Let me now look at a few more things to complete my analysis - the question tool directory (MinerU), the builtin tools for RAG, and how the rag tool is registered/mounted.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:58:31 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a very comprehensive picture of the entire codebase. Let me compile the detailed findings for each area.

Let me also quickly check the data directory tree structure and whether there are any existing document collections.

</details>

### Resposta

Now I have a thorough understanding of the entire codebase. Here are my detailed findings:

---

## 1. Knowledge Base (KB) System

### Overall Architecture
DeepTutor uses **LlamaIndex** as its sole RAG provider (the `DEFAULT_PROVIDER = "llamaindex"`). The system is organized around a two-layer KB management system:

**Key file paths:**
- `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\knowledge\manager.py` â€” `KnowledgeBaseManager` class, manages all KB CRUD
- `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\knowledge\initializer.py` â€” `KnowledgeBaseInitializer` for creating new KBs
- `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\knowledge\add_documents.py` â€” `DocumentAdder` for incremental document addition
- `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\service.py` â€” `RAGService` unified entry point
- `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\factory.py` â€” Pipeline factory (always returns LlamaIndexPipeline)
- `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\pipelines\llamaindex\pipeline.py` â€” `LlamaIndexPipeline` orchestrator
- `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\tools\rag_tool.py` â€” The `rag_search` and `initialize_rag` wrapper functions

### KB Directory Structure
Each knowledge base lives under `data/knowledge_bases/<kb_name>/` with this layout:
```
data/knowledge_bases/<kb_name>/
    raw/                         # Source files (original uploaded docs)
    version-N/                   # LlamaIndex vector store (flat version dirs)
        docstore.json
        index_store.json
        default__vector_store.json
        graph_store.json
        image__vector_store.json
        meta.json                # {"version", "signature", "model", ...}
        bm25_retriever/          # Persisted BM25 sidecar index (if available)
    images/                      # Extracted images
    content_list/                # Content list files
    metadata.json                # KB metadata
    .progress.json               # Live progress tracking
```

The central config is at `data/knowledge_bases/kb_config.json` (line 204 of handler.py).

### Document Ingestion Pipeline
Documents are ingested through the `LlamaIndexDocumentLoader` (`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\pipelines\llamaindex\document_loader.py`). It classifies files using the `FileTypeRouter`:

1. **Parser files** (PDF, DOCX, XLSX, PPTX) â†’ extracted via `extract_text_from_path()` using PyMuPDF/pypdf/python-docx/openpyxl/python-pptx
2. **Text files** (.md, .txt, .py, .json, .html, .csv, .tex, etc. â€” 120+ extensions) â†’ direct UTF-8 reading with multi-encoding fallback
3. **Image files** (.png, .jpg, .gif, .webp, .bmp, .tiff) â†’ described by multimodal LLM, embedded by multimodal embedding model

### KB Configuration
`kb_config.json` (at `C:\Users\frota\Documents\Projetos\AI TUTOR\data\knowledge_bases\kb_config.json`) tracks:
```json
{
  "knowledge_bases": {
    "html-guide": {
      "path": "html-guide",
      "description": "Knowledge base: html-guide",
      "status": "error",
      "updated_at": "...",
      "progress": { "stage": "error", "message": "...", ... },
      "rag_provider": "llamaindex"
    }
  }
}
```
Currently, the `html-guide` KB is in **error** status because no embedding model is configured (`model_catalog.json` has `"active_model_id": null` under `"embedding"`).

### CLI Commands (from AGENTS.md)
```bash
deeptutor kb list
deeptutor kb create my-kb --doc textbook.pdf
```

---

## 2. PDF Processing

### Multi-Layer PDF Support
DeepTutor has **three distinct PDF processing layers**:

#### Layer 1: Chat Attachment Extraction (Bytes-in, Text-out)
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\utils\document_extractor.py`
- Uses **PyMuPDF (fitz)** as the primary PDF parser (line 35: `import fitz`)
- Falls back to **pypdf** if PyMuPDF fails (line 40: `from pypdf import PdfReader`)
- Extracts text page by page with `--- Page N ---` separators
- Per-file limit: 10MB (`MAX_DOC_BYTES`), 200K chars (`MAX_EXTRACTED_CHARS_PER_DOC`)
- Per-turn total: 25MB, 150K chars
- Validates PDF header magic bytes to prevent spoofing

#### Layer 2: KB Ingestion (RAG Pipeline)
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\file_routing.py`
- PDF is classified as a `DocumentType.PDF` (line 184: `".pdf"` in `PDF_EXTENSIONS`)
- Routes to `LlamaIndexDocumentLoader._extract_parser_text()` which uses the same `extract_text_from_path()` from Layer 1
- Uses `DocumentValidator.MAX_PDF_SIZE = 50MB` for PDFs (vs `MAX_FILE_SIZE = 100MB` for others)

#### Layer 3: MinerU â€” Advanced PDF Parsing with OCR
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\tools\question\`
- **Local CLI**: Uses `magic-pdf` or `mineru` CLI tool installed via `pip install mineru[core]`
- **Cloud API**: mineru.net v4 API (`POST /api/v4/file-urls/batch` â†’ upload â†’ poll â†’ download ZIP)
- Config stored in `data/user/settings/mineru.json`
- MinerU produces: `*.md` (markdown output), `*_content_list.json` (structured content), `images/` (extracted figures)
- OCR toggle: `"is_ocr": false` in mineru.json (can be enabled for scanned PDFs)
- The cloud backend supports language, formula, and table recognition

### Dependencies (from pyproject.toml)
```
PyMuPDF>=1.26.0       # Primary PDF parser (fitz)
pypdf>=4.0.0          # Fallback PDF parser
pdfplumber>=0.11.0    # Installed (but not explicitly used in the extraction code I found)
```

### No Native OCR
DeepTutor **does not** have native OCR (no tesseract, easyocr, paddleocr). OCR capability comes exclusively from **MinerU** (local CLI or cloud API), which provides its own OCR models for scanned PDFs.

---

## 3. Image Understanding

### Multimodal LLM Support
DeepTutor has comprehensive multimodal/image support:

**Vision-Capable Provider Bindings** (from `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\llm\capabilities.py`):
- `openai` â€” `supports_vision: True` (gpt-4o, gpt-4-turbo, gpt-4-vision via model overrides)
- `anthropic` / `claude` â€” `supports_vision: True`
- `volcengine` / `byteplus` â€” `supports_vision: True`
- `groq`, `together`, `mistral`, `openrouter` â€” `supports_vision: True`
- Model-specific: `gpt-4o`, `gpt-4-turbo`, `gpt-4-vision`, `claude-3`, `claude-4`, `gemini`, `llava`, `bakllava`, `moondream`, `minicpm-v`, `kimi-k2.5`, `kimi-k2.6`, `qwenvl` variants
- **DeepSeek** (`supports_vision: False`) â€” the currently configured LLM does NOT support images

### Multimodal Message Pipeline
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\llm\multimodal.py`
- `prepare_multimodal_messages()` â€” injects image attachments into user messages
- Supports both OpenAI-compatible (`image_url` blocks) and Anthropic (`image` source blocks) formats
- Two-stage fallback: Stage 1 injects optimistically, Stage 2 (`should_degrade_to_text`) strips images if the model rejects them

### Vision Solver Agent
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\agents\vision_solver\`
- `VisionSolverAgent` â€” dedicated agent for image analysis
- API endpoint: `POST /api/v1/vision/analyze` and WebSocket `/api/v1/vision/solve`
- Config in settings: `vision_solver` capability with `temperature: 0.3, max_tokens: 12000`

### Image Processing Tools
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\tools\vision\`
- `image_utils.py` â€” URL download, base64 conversion, format validation (JPEG, PNG, GIF, WebP)
- `block_parser.py` â€” GeoGebra block parsing for streaming content
- `coord_transform.py` â€” Coordinate system transforms for GeoGebra
- `ggb_validator.py` â€” GeoGebra command validation

### Image Embedding in RAG
The `LlamaIndexDocumentLoader._load_image_nodes()` method supports indexing images:
1. Checks if both embedding and LLM clients support multimodal
2. Loads image â†’ sends to multimodal LLM for description
3. Embeds the image via a multimodal embedding provider
4. Creates `ImageNode` with metadata + embedding

**However**, the currently configured LLM (DeepSeek, `supports_vision: False`) and no embedding model configured means image indexing is effectively disabled right now.

### Visualize Capability
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\capabilities\visualize.py`
Generates SVG, Chart.js, Mermaid, HTML, or Manim animations â€” this is about **generating** visualizations, not understanding them.

---

## 4. Data Directory Structure

### Top-level `data/` directory
```
C:\Users\frota\Documents\Projetos\AI TUTOR\data\
    knowledge_bases/
        kb_config.json                 # Central KB registry
        html-guide/                    # Existing KB (in error state)
            raw/                       # Source markdown files (15 files)
                01-estrutura-html.md through 15-js-router.md
            .progress.json
            metadata.json
    user/
        chat_history.db                # SQLite chat history
        workspace/
            skills/                    # User-installed skills
                tutor-ai/
                tutor/
                study-tutor/
                pinn-executor/
            notebook/                  # Jupyter-like notebooks
            book/                      # Book/exploration projects
            chat/                      # Turn event logs
        settings/
            main.yaml                  # System configuration
            model_catalog.json         # LLM/embedding provider catalog
            mineru.json                # MinerU PDF parser config
            agents.yaml
            system.json
            interface.json
            integrations.json
            auth.json
    memory/
        trace/chat/                    # Chat memory traces
        L3/preferences.md              # User preferences
```

### Existing Document Collection
The only existing KB is **html-guide** with 15 markdown files covering HTML/CSS/JS tutorial content. No PDFs have been ingested into any KB.

### Settings (model_catalog.json)
The current configuration has:
- **LLM**: DeepSeek Chat (`deepseek-chat`) via `api.deepseek.com` â€” **no vision support**
- **Embedding**: No active profile (`"active_profile_id": null`, `"profiles": []`) â€” **this is why KB init fails**

---

## 5. RAG Implementation Details

### Embedding Models
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\config\provider_runtime.py` defines supported embedding providers:

| Provider | Adapter | Default Model | Dim | Multimodal |
|---|---|---|---|---|
| OpenAI | openai_compat | text-embedding-3-large | 3072 | No |
| Gemini | openai_compat | gemini-embedding-001 | 3072 | No |
| Cohere | cohere | embed-v4.0 | 1024 | **Yes** |
| Jina | jina | jina-embeddings-v3 | 1024 | No |
| Ollama | ollama | nomic-embed-text | 768 | No |
| SiliconFlow | openai_compat | Qwen3-Embedding-8B | 4096 | **Yes** |
| Aliyun DashScope | dashscope_native | qwen3-vl-embedding | 2560 | **Yes** |

Adapters at `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\embedding\adapters\`:
- `openai_compatible.py` â€” OpenAI-compatible REST API
- `openai_sdk.py` â€” OpenAI Python SDK
- `ollama.py` â€” Local Ollama
- `cohere.py` â€” Cohere API
- `jina.py` â€” Jina API
- `dashscope_native.py` â€” Aliyun DashScope multimodal

### Chunking Strategy
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\pipelines\llamaindex\embedding_adapter.py` (line 142-143):
```python
Settings.chunk_size = 512
Settings.chunk_overlap = 50
```

The chunker is `SentenceSplitter` from LlamaIndex (in `ingestion.py`), which splits on sentence boundaries with 512 token chunks and 50 token overlap.

### Vector Store
DeepTutor uses **LlamaIndex's native vector store** (in-memory with JSON persistence). The stores are persisted as JSON files:
- `default__vector_store.json` â€” Main vector store
- `image__vector_store.json` â€” Image vector store (if images indexed)
- `docstore.json` â€” Document store
- `index_store.json` â€” Index metadata
- `graph_store.json` â€” Graph store

No external vector DB (ChromaDB, FAISS, Pinecone, Qdrant, Weaviate) is currently configured. It uses LlamaIndex's built-in `VectorStoreIndex` which stores everything in memory and persists to JSON.

### Retrieval Parameters
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\pipelines\llamaindex\config.py`:

```python
@dataclass(frozen=True)
class RetrievalConfig:
    profile: str = HYBRID_PROFILE      # "hybrid" (default) or "vector"
    vector_top_k_multiplier: int = 2
    bm25_top_k_multiplier: int = 2
    fusion_num_queries: int = 1
```

Default `top_k = 5` (passed from pipeline.py line 156: `top_k = kwargs.get("top_k", 5)`).

**Hybrid retrieval** combines vector similarity + BM25 keyword search using `QueryFusionRetriever` with `RECIPROCAL_RANK` fusion mode.

BM25 requires `llama-index-retrievers-bm25` (defined in pyproject.toml line 39).

### Embedding Signature / Versioning
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\index_versioning.py`
Each index version is keyed by an `EmbeddingSignature` containing `(binding, model, dimension, base_url, api_version)`. This allows switching embedding models without losing old indexes â€” the system finds the matching `version-N` directory for the active signature.

### Smart Retriever (Multi-Query)
`C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\smart_retriever.py`
Generates `max_queries=3` query variants using the LLM, retrieves for each, then aggregates with LLM summarization. Used by the higher-level question pipeline.

### RAG Pipeline Flow
```
User query â†’ rag_tool.rag_search()
    â†’ RAGService.search()
        â†’ LlamaIndexPipeline.search()
            â†’ resolve_storage_dir_for_read()  (find matching version)
            â†’ storage.retrieve_nodes()        (load index, build retriever)
                â†’ retrievers.build_retriever() (hybrid vector+BM25)
                â†’ retriever.retrieve(query)    (return nodes)
            â†’ _nodes_to_result()               (format response)
```

---

## Summary of Key Findings

| Area | Status |
|---|---|
| **KB/RAG** | Fully implemented, uses LlamaIndex with hybrid BM25+vector retrieval. Only one KB exists (html-guide, in error state). |
| **PDF processing** | 3 layers: PyMuPDF+pypdf for text extraction, pdfplumber available, MinerU for advanced parsing with OCR. |
| **Image understanding** | Comprehensive multimodal support across providers; VisionSolver agent exists. **Disabled with current DeepSeek config** (no vision). |
| **Embedding** | No active embedding profile â†’ KB operations fail. Supports OpenAI, Gemini, Cohere, Jina, Ollama, SiliconFlow, Aliyun DashScope. |
| **Vector store** | LlamaIndex built-in (JSON-persisted in-memory). No external vector DB. |
| **Chunking** | 512-token SentenceSplitter with 50-token overlap. |
| **Retrieval** | Hybrid by default: vector similarity + BM25 keyword with reciprocal rank fusion, top_k=5. |

*Novo passo iniciado*

---

*16 messages | 114 parts | ðŸ’° $0.0224 | â±ï¸ 0h01m38s*

