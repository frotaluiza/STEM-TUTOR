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

Sessão com **8 messages**, **63 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | 💾 cache read: 172.8K | ⏱️ 0h22m45s

## 👤 Usuário (2026-07-12 00:35:59 UTC)

Search the filesystem broadly for anything related to "deeptutor" or "Deeptutor". Look for:
1. Any project directories/files named deeptutor anywhere under C:\Users\frota or other common locations
2. Any package.json, pyproject.toml, or config files
3. The content and structure of the project

Start by searching with glob patterns like:
- **/deeptutor*/** (or */deeptutor*)
- **/DeepTutor*/**

Also search C:\Users\frota for deeptutor related files.

Return: full path to the project, what kind of project it is (JS/TS/Python/Rust), its main structure, and a summary of the tech stack used.

## 🤖 Assistente (2026-07-12 00:35:59 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to search for anything related to "deeptutor" or "Deeptutor" on the filesystem. Let me start with broad searches using glob patterns and also search file contents.

</details>

### Resposta

I'll start by searching broadly across the filesystem for anything related to "deeptutor" using multiple strategies in parallel.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 00:36:10 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Great, I found a lot of results. The main project directory appears to be at `C:\Users\frota\Documents\Projetos\AI TUTOR`. Let me explore the key files there to understand the project structure and tech stack. Let me read the pyproject.toml, package.json if any, and the main directory structure.

</details>

### Resposta

Found a massive amount of results. The core project is at `C:\Users\frota\Documents\Projetos\AI TUTOR`. Let me now read its key files to understand the tech stack and structure.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 00:36:15 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the main pyproject.toml, the requirements, and explore the deeptutor directory structure and the web directory to understand the full tech stack.

</details>

### Resposta

Let me now explore the main `pyproject.toml`, the `web/` directory, and the core modules to get a complete picture.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 00:36:19 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me also read the web package.json to understand the frontend tech stack, and take a peek at the deeper structure of the deeptutor Python package.

</details>

### Resposta

Let me grab the `package.json` for the web frontend and explore a few more directories.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 00:36:24 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me also check for any deeptutor project files under other common locations, like the root of C:\, or under OneDrive, and look at the data directory and docker files.

</details>

### Resposta

Let me check for additional deeptutor-related files in other common locations and look at the Docker/compose configuration.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 00:58:20 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive picture. Let me also check the .git/config to see the remote origin and confirm it's the HKUDS/DeepTutor repo.

</details>

### Resposta

Let me check the git remote and the secret baseline for the project origin.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 00:58:26 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

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
├── deeptutor/                  # Python backend package (core library)
│   ├── __version__.py          # v1.5.1
│   ├── agents/                 # Capability/agent implementations
│   │   ├── chat/               # Agentic chat loop
│   │   ├── comic/              # Comic agent
│   │   ├── math_animator/      # Manim animation agent
│   │   ├── research/           # Deep research agent
│   │   ├── solve/              # Deep solve agent
│   │   ├── question/           # Deep question agent
│   │   ├── visualize/          # Visualization agent
│   │   └── vision_solver/      # Vision-based problem solver
│   ├── api/                    # FastAPI web server
│   │   ├── main.py             # ASGI app entry
│   │   ├── routers/            # Route handlers (incl. unified_ws.py)
│   │   └── run_server.py
│   ├── app/                    # Application-level orchestration
│   ├── capabilities/           # Built-in capability implementations
│   ├── core/                   # Core abstractions
│   │   ├── capability_protocol.py
│   │   ├── tool_protocol.py
│   │   ├── context.py          # UnifiedContext
│   │   ├── stream.py / stream_bus.py
│   │   └── agentic/            # Agent-loop framework
│   ├── learning/               # Guided learning / mastery system
│   ├── multi_user/             # Multi-tenant auth & RBAC
│   ├── partners/               # IM channel connectors (multi-platform)
│   │   └── channels/           # Telegram, Discord, Slack, WhatsApp, WeChat, etc.
│   ├── runtime/                # ChatOrchestrator, launcher, registries
│   ├── services/               # Various subsystems
│   │   ├── rag/                # RAG pipeline (LlamaIndex, GraphRAG, LightRAG)
│   │   ├── llm/                # LLM provider abstractions
│   │   ├── embedding/          # Embedding models
│   │   ├── memory/             # Memory system
│   │   ├── parsing/            # Document parsers
│   │   ├── sandbox/            # Code execution sandbox
│   │   ├── session/            # Session management
│   │   └── auth.py             # PocketBase auth
│   ├── tools/                  # Tool implementations
│   │   ├── builtin/            # RAG, web search, code exec, etc.
│   │   ├── rag_tool.py
│   │   ├── web_search.py
│   │   ├── exec_tool.py
│   │   ├── brainstrom.py
│   │   └── ...
│   └── i18n/                   # Internationalization
│
├── deeptutor_cli/              # CLI entry point (Typer-based)
│   ├── main.py                 # CLI commands (run, chat, kb, serve, partner, etc.)
│   ├── chat.py                 # Interactive REPL
│   ├── kb.py                   # Knowledge base management
│   ├── session_cmd.py
│   ├── partner.py
│   ├── skill.py
│   └── ...
│
├── deeptutor_web/              # Thin package for bundled web assets
│
├── web/                        # Next.js 16 frontend (TypeScript)
│   ├── app/                    # App router pages
│   ├── components/             # React components
│   ├── features/               # Feature modules
│   ├── lib/                    # Utility libraries
│   ├── locales/                # i18n translation files (en, zh, etc.)
│   ├── context/                # React contexts
│   ├── hooks/                  # Custom hooks
│   ├── types/                  # TypeScript type definitions
│   ├── public/                 # Static assets
│   └── package.json            # npm dependencies
│
├── data/                       # Runtime data (not tracked in git)
│   ├── knowledge_bases/        # RAG knowledge bases
│   ├── memory/                 # User memory
│   ├── user/                   # User settings & logs
│   └── ...
│
├── packaging/                  # PyPI distribution packages
│   └── deeptutor-cli/          # CLI-only wheel
│
├── docker-compose.yml          # Docker Compose (full stack)
├── compose.yaml                # Podman Compose (rootless)
├── Dockerfile                  # Multi-stage build
├── Dockerfile.runner           # Sandbox runner image
├── pyproject.toml              # Python project config (466 lines)
├── requirements.txt            # Dependency bundle
├── requirements/               # Split dependency files
├── tests/                      # Test suite
└── scripts/                    # Utility scripts
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

*8 messages | 63 parts | 💰 $0.0000 | ⏱️ 0h22m45s*
