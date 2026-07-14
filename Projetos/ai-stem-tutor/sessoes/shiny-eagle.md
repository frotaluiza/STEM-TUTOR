---
title: "shiny-eagle"
slug: "shiny-eagle"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: shiny-eagle
title: "Explore Deeptutor project (@explore subagent)"
date: 2026-07-12
agent: explore
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h22m45s
messages: 8
parts: 63
cost: 0
tokens_input: 40700
tokens_output: 4396
tokens_reasoning: 268
tokens_cache_read: 172800
tokens_cache_write: 0
created: "2026-07-12 00:35:59 UTC"
updated: "2026-07-12 00:58:44 UTC"
---

SessÃ£o com **8 messages**, **63 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | ðŸ’¾ cache read: 172.8K | â±ï¸ 0h22m45s

## ðŸ‘¤ UsuÃ¡rio (2026-07-12 00:35:59 UTC)

Search the filesystem broadly for anything related to "deeptutor" or "Deeptutor". Look for:
1. Any project directories/files named deeptutor anywhere under C:\Users\frota or other common locations
2. Any package.json, pyproject.toml, or config files
3. The content and structure of the project

Start by searching with glob patterns like:
- **/deeptutor*/** (or */deeptutor*)
- **/DeepTutor*/**

Also search C:\Users\frota for deeptutor related files.

Return: full path to the project, what kind of project it is (JS/TS/Python/Rust), its main structure, and a summary of the tech stack used.

## ðŸ¤– Assistente (2026-07-12 00:35:59 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants me to search for anything related to "deeptutor" or "Deeptutor" on the filesystem. Let me start with broad searches using glob patterns and also search file contents.

</details>

### Resposta

I'll start by searching broadly across the filesystem for anything related to "deeptutor" using multiple strategies in parallel.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 00:36:10 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Great, I found a lot of results. The main project directory appears to be at `C:\Users\frota\Documents\Projetos\AI TUTOR`. Let me explore the key files there to understand the project structure and tech stack. Let me read the pyproject.toml, package.json if any, and the main directory structure.

</details>

### Resposta

Found a massive amount of results. The core project is at `C:\Users\frota\Documents\Projetos\AI TUTOR`. Let me now read its key files to understand the tech stack and structure.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 00:36:15 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me read the main pyproject.toml, the requirements, and explore the deeptutor directory structure and the web directory to understand the full tech stack.

</details>

### Resposta

Let me now explore the main `pyproject.toml`, the `web/` directory, and the core modules to get a complete picture.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 00:36:19 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me also read the web package.json to understand the frontend tech stack, and take a peek at the deeper structure of the deeptutor Python package.

</details>

### Resposta

Let me grab the `package.json` for the web frontend and explore a few more directories.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 00:36:24 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me also check for any deeptutor project files under other common locations, like the root of C:\, or under OneDrive, and look at the data directory and docker files.

</details>

### Resposta

Let me check for additional deeptutor-related files in other common locations and look at the Docker/compose configuration.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 00:58:20 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a comprehensive picture. Let me also check the .git/config to see the remote origin and confirm it's the HKUDS/DeepTutor repo.

</details>

### Resposta

Let me check the git remote and the secret baseline for the project origin.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 00:58:26 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

I now have a comprehensive picture. Let me compile the final response.

</details>

### Resposta

Here is the complete findings report.

---

## DeepTutor -- Full Search Results

### 1. Primary Project Location

**Absolute path:** `C:\Users\frota\Documents\Projetos\AI TUTOR`

This is a local clone of the open-source repository **HKUDS/DeepTutor** (University of Hong Kong), version **v1.5.1**.

---

### 2. What Kind of Project Is It?

**Hybrid Python + TypeScript project:**

| Layer    | Language   | Framework / Tooling                                                                 |
|----------|------------|-------------------------------------------------------------------------------------|
| Backend  | **Python** | Python 3.11+, FastAPI, Uvicorn, Typer CLI, WebSockets, LlamaIndex, Pydantic v2     |
| Frontend | **TypeScript** | Next.js 16, React 19, Tailwind CSS 3, TypeScript 5, Framer Motion, Chart.js, Mermaid, i18next |
| Infra    | Docker     | Multi-stage Dockerfile (frontend builder + Python runtime), Podman/Docker Compose   |

---

### 3. Main Project Structure

```
C:\Users\frota\Documents\Projetos\AI TUTOR\
â”œâ”€â”€ deeptutor/                  # Python backend package (core library)
â”‚   â”œâ”€â”€ __version__.py          # v1.5.1
â”‚   â”œâ”€â”€ agents/                 # Capability/agent implementations
â”‚   â”‚   â”œâ”€â”€ chat/               # Agentic chat loop
â”‚   â”‚   â”œâ”€â”€ comic/              # Comic agent
â”‚   â”‚   â”œâ”€â”€ math_animator/      # Manim animation agent
â”‚   â”‚   â”œâ”€â”€ research/           # Deep research agent
â”‚   â”‚   â”œâ”€â”€ solve/              # Deep solve agent
â”‚   â”‚   â”œâ”€â”€ question/           # Deep question agent
â”‚   â”‚   â”œâ”€â”€ visualize/          # Visualization agent
â”‚   â”‚   â””â”€â”€ vision_solver/      # Vision-based problem solver
â”‚   â”œâ”€â”€ api/                    # FastAPI web server
â”‚   â”‚   â”œâ”€â”€ main.py             # ASGI app entry
â”‚   â”‚   â”œâ”€â”€ routers/            # Route handlers (incl. unified_ws.py)
â”‚   â”‚   â””â”€â”€ run_server.py
â”‚   â”œâ”€â”€ app/                    # Application-level orchestration
â”‚   â”œâ”€â”€ capabilities/           # Built-in capability implementations
â”‚   â”œâ”€â”€ core/                   # Core abstractions
â”‚   â”‚   â”œâ”€â”€ capability_protocol.py
â”‚   â”‚   â”œâ”€â”€ tool_protocol.py
â”‚   â”‚   â”œâ”€â”€ context.py          # UnifiedContext
â”‚   â”‚   â”œâ”€â”€ stream.py / stream_bus.py
â”‚   â”‚   â””â”€â”€ agentic/            # Agent-loop framework
â”‚   â”œâ”€â”€ learning/               # Guided learning / mastery system
â”‚   â”œâ”€â”€ multi_user/             # Multi-tenant auth & RBAC
â”‚   â”œâ”€â”€ partners/               # IM channel connectors (multi-platform)
â”‚   â”‚   â””â”€â”€ channels/           # Telegram, Discord, Slack, WhatsApp, WeChat, etc.
â”‚   â”œâ”€â”€ runtime/                # ChatOrchestrator, launcher, registries
â”‚   â”œâ”€â”€ services/               # Various subsystems
â”‚   â”‚   â”œâ”€â”€ rag/                # RAG pipeline (LlamaIndex, GraphRAG, LightRAG)
â”‚   â”‚   â”œâ”€â”€ llm/                # LLM provider abstractions
â”‚   â”‚   â”œâ”€â”€ embedding/          # Embedding models
â”‚   â”‚   â”œâ”€â”€ memory/             # Memory system
â”‚   â”‚   â”œâ”€â”€ parsing/            # Document parsers
â”‚   â”‚   â”œâ”€â”€ sandbox/            # Code execution sandbox
â”‚   â”‚   â”œâ”€â”€ session/            # Session management
â”‚   â”‚   â””â”€â”€ auth.py             # PocketBase auth
â”‚   â”œâ”€â”€ tools/                  # Tool implementations
â”‚   â”‚   â”œâ”€â”€ builtin/            # RAG, web search, code exec, etc.
â”‚   â”‚   â”œâ”€â”€ rag_tool.py
â”‚   â”‚   â”œâ”€â”€ web_search.py
â”‚   â”‚   â”œâ”€â”€ exec_tool.py
â”‚   â”‚   â”œâ”€â”€ brainstrom.py
â”‚   â”‚   â””â”€â”€ ...
â”‚   â””â”€â”€ i18n/                   # Internationalization
â”‚
â”œâ”€â”€ deeptutor_cli/              # CLI entry point (Typer-based)
â”‚   â”œâ”€â”€ main.py                 # CLI commands (run, chat, kb, serve, partner, etc.)
â”‚   â”œâ”€â”€ chat.py                 # Interactive REPL
â”‚   â”œâ”€â”€ kb.py                   # Knowledge base management
â”‚   â”œâ”€â”€ session_cmd.py
â”‚   â”œâ”€â”€ partner.py
â”‚   â”œâ”€â”€ skill.py
â”‚   â””â”€â”€ ...
â”‚
â”œâ”€â”€ deeptutor_web/              # Thin package for bundled web assets
â”‚
â”œâ”€â”€ web/                        # Next.js 16 frontend (TypeScript)
â”‚   â”œâ”€â”€ app/                    # App router pages
â”‚   â”œâ”€â”€ components/             # React components
â”‚   â”œâ”€â”€ features/               # Feature modules
â”‚   â”œâ”€â”€ lib/                    # Utility libraries
â”‚   â”œâ”€â”€ locales/                # i18n translation files (en, zh, etc.)
â”‚   â”œâ”€â”€ context/                # React contexts
â”‚   â”œâ”€â”€ hooks/                  # Custom hooks
â”‚   â”œâ”€â”€ types/                  # TypeScript type definitions
â”‚   â”œâ”€â”€ public/                 # Static assets
â”‚   â””â”€â”€ package.json            # npm dependencies
â”‚
â”œâ”€â”€ data/                       # Runtime data (not tracked in git)
â”‚   â”œâ”€â”€ knowledge_bases/        # RAG knowledge bases
â”‚   â”œâ”€â”€ memory/                 # User memory
â”‚   â”œâ”€â”€ user/                   # User settings & logs
â”‚   â””â”€â”€ ...
â”‚
â”œâ”€â”€ packaging/                  # PyPI distribution packages
â”‚   â””â”€â”€ deeptutor-cli/          # CLI-only wheel
â”‚
â”œâ”€â”€ docker-compose.yml          # Docker Compose (full stack)
â”œâ”€â”€ compose.yaml                # Podman Compose (rootless)
â”œâ”€â”€ Dockerfile                  # Multi-stage build
â”œâ”€â”€ Dockerfile.runner           # Sandbox runner image
â”œâ”€â”€ pyproject.toml              # Python project config (466 lines)
â”œâ”€â”€ requirements.txt            # Dependency bundle
â”œâ”€â”€ requirements/               # Split dependency files
â”œâ”€â”€ tests/                      # Test suite
â””â”€â”€ scripts/                    # Utility scripts
```

---

### 4. All DeepTutor-Related Paths Found

| Path | Type |
|------|------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR` | **Project root** (git clone of HKUDS/DeepTutor) |
| `C:\Users\frota\data\user\logs\deeptutor.jsonl` | Runtime log file |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\assets\figs-archive\deeptutor-architecture.png` | Architecture diagram |
| `C:\Users\frota\OneDrive\Documentos\Obsidian Vault\Logs de conversas\DeepTutor_KB_API_+_Learning_Space_(@explore_subagent).md` | Obsidian session log |
| `C:\Users\frota\OneDrive\Documentos\Obsidian Vault\Leituras\_notion\DeepTutor- Towards Agentic Personalized Tutoring (arXiv-2604.26962).md` | Paper reading notes |

---

### 5. Tech Stack Summary

| Category | Technology |
|----------|-----------|
| **Backend language** | Python 3.11+ |
| **Web framework** | FastAPI + Uvicorn |
| **CLI framework** | Typer + Rich + prompt_toolkit |
| **Frontend** | Next.js 16 + React 19 + TypeScript 5 |
| **Styling** | Tailwind CSS 3 + Framer Motion |
| **Data validation** | Pydantic v2 |
| **RAG / Vector search** | LlamaIndex, FAISS, BM25 retriever, GraphRAG (opt-in), LightRAG (opt-in) |
| **LLM providers** | OpenAI, Anthropic, DashScope (Alibaba), Perplexity, plus any OpenAI-compatible |
| **Embedding** | Configurable via Settings (Ollama, OpenAI, etc.) |
| **Auth / storage** | PocketBase (optional sidecar) |
| **Messaging/Partner channels** | Telegram, Discord, Slack, WhatsApp, WeChat, Matrix, Zulip, DingTalk, Feishu/Lark, QQ, Microsoft Teams, Mattermost, email |
| **Code execution** | Sandboxed (bwrap / restricted subprocess) |
| **Document parsing** | PyMuPDF, MinerU, MarkItDown, Docling, PyMuPDF4LLM (pluggable engines) |
| **Math animations** | Manim (opt-in) |
| **Containerization** | Docker + Podman (rootless, read-only rootfs) |
| **Testing** | Pytest + Playwright (E2E) |
| **Linting** | Ruff + pre-commit + Bandit + MyPy (relaxed) |
| **CI** | GitHub Actions (inferred from `.github/`) |
| **C4 model** | `assets/` contains C4-model diagrams |
| **Sandbox runner** | Separate Dockerfile (`Dockerfile.runner`) |

---

### 6. Key Details

- **Version:** 1.5.1 (as of `__version__.py`)
- **License:** Apache 2.0
- **Origin repo:** `https://github.com/HKUDS/DeepTutor.git`
- **Personal fork:** `https://github.com/frotaluiza/STEM-TUTOR.git` (configured as `personal` remote)
- **Documentation:** https://deeptutor.info
- **Paper:** arXiv 2604.26962 ("DeepTutor: Towards Agentic Personalized Tutoring")
- **Architecture:** Two-layer plugin model -- **Tools** (single-shot functions invoked by LLM) and **Capabilities** (multi-stage pipelines that own the turn), routed through a `ChatOrchestrator` with a shared `StreamBus` for event fan-out. Three entry points: CLI (Typer), WebSocket API, and Python SDK.

*Novo passo iniciado*

---

*8 messages | 63 parts | ðŸ’° $0.0000 | â±ï¸ 0h22m45s*

