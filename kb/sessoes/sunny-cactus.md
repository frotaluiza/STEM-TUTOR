---
slug: sunny-cactus
title: "Explore HKU codebase structure (@explore subagent)"
date: 2026-07-12
agent: explore
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h02m49s
messages: 24
parts: 143
cost: 0
tokens_input: 85239
tokens_output: 13704
tokens_reasoning: 1159
tokens_cache_read: 1125760
tokens_cache_write: 0
created: "2026-07-12 02:00:28 UTC"
updated: "2026-07-12 02:03:17 UTC"
---

Sessão com **24 messages**, **143 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | 💾 cache read: 1.1M | ⏱️ 0h02m49s

## 👤 Usuário (2026-07-12 02:00:28 UTC)

I need to understand the HKU DeepTutor codebase structure at `C:\Users\frota\Documents\Projetos\AI TUTOR\` on branch `feature/mind-map-module`.

Please explore deeply and return:

1. **High-level directory tree** of `deeptutor/` (top 3 levels) — key subsystems and what they do
2. **Key files in these areas** (with paths and brief purpose):
   - Tutoring / dialogue engine (how does the tutoring loop work?)
   - Student modeling (how does it track student knowledge?)
   - Dialogue management (how does it manage conversation turns?)
   - Knowledge base / RAG (how are knowledge bases used?)
   - Assessment / feedback (how does it evaluate student answers?)
   - Mastery learning / adaptive path (how does it adapt to the student?)
   - Mind-map module (the feature branch we're on — what new stuff is here?)
   - MCP integration (how are MCP servers used in tutoring?)
3. **Git diff on feature/mind-map-module vs main** — what files changed? Just the high-level summary.
4. **Main entry points** — `deeptutor_cli/main.py`, `deeptutor/app.py`, `deeptutor/api/`

Be very thorough. Read key files to understand the architecture. Return all findings so I can do a cross-reference analysis with Memphis seminal papers on intelligent tutoring systems.

## 🤖 Assistente (2026-07-12 02:00:28 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants a deep exploration of the HKU DeepTutor codebase. Let me start by exploring the directory structure, then dive into key files. Let me begin systematically.

First, let me explore the top-level structure.

</details>

### Resposta

I'll start by exploring the repository structure broadly, then dive deep into each subsystem.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:00:31 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good, we're on `feature/mind-map-module`. Let me explore the directory tree structure.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:00:34 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

This is a large codebase. Let me now dive into the key files. I'll start by reading the main entry points and then explore each subsystem.

</details>

### Resposta

Now let me read the key entry points and core subsystem files in parallel:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:00:37 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now read the key files: the orchestrator, the app facade, core protocols, and the feature branch files related to mind maps.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:00:41 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good, I'm getting a picture of the architecture. Now let me dive deeper into specific areas: the chat capability (tutoring loop), student modeling (learning), knowledge/RAG, assessment, mastery learning, mind-map module, and MCP integration.

</details>

### Resposta

Now let me dive into the chat capability (the core tutoring loop), student modeling, mastery learning, mind map module, and MCP:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:00:45 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the key files in the learning subsystem, mastery capability, the mind-map module files, and the MCP service.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:00:48 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Great, I'm building up a picture. Now let me look at:
1. The grading module
2. The mastery capability loop (chat loop with mastery tools)
3. The mind-map module files
4. The MCP service
5. The RAG service
6. The knowledge module
7. Git diff

</details>

### Resposta

Now let me read the grading module, the mastery capability loop, the mind-map module, and MCP/RAG:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:00:53 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the MCP service files, the mind-map module files, the agentic chat pipeline, the RAG service, and the knowledge module.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:00:56 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me continue reading key files: RAG service, knowledge manager, agentic chat pipeline, the tools used in mastery, the mind-map module files and the scheduler.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:00 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me look at the mind-map module, which is the feature branch. Let me find relevant files.

</details>

### Resposta

Now let me find the mind-map module files and the scheduler, then check git diff:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:04 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The mind-map module might not be named with those patterns. Let me search more broadly and look at the git diff.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:08 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Interesting - the "mind-map module" seems to be related to the project state visualization. Let me look at the `project_state.py` router and related files more carefully. Let me also continue exploring the git diff to see what changed in the feature branch, and look at the scheduler, agent loop, and more core areas.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:12 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me get the rest of the diff and also look at the project_state router in detail, since it seems to be the mind-map related file.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:15 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me get more details about the scheduler, the agent_loop, the book module, and the knowledge module to complete the picture.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:19 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me look at the scheduler, the git diff summary, and the `deeptutor_cli/common.py` and `deeptutor/agents/chat/capability.py` to understand the routing further. Let me also check the git log on the feature branch and see the main changes.

</details>

### Resposta

Let me get the detailed git diff stats and a few more key files:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:24 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me get the diff stats in a PowerShell-friendly way and look at the remaining key files.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:29 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now look at the remaining diff details to understand what was changed in the feature branch vs main. I also want to look at the `learning/prompts/en/platform_messages.yaml` file, which was mentioned in the git diff, and understand the project-state directory.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:33 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the project state files to complete the mind-map picture, and also look at the tools/builtin/__init__.py to see how tools are registered.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:36 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me also look at the remaining key files: the web frontend for the mind-map, the learning prompts, and the updated scripts that were mentioned in the diff.

</details>

### Resposta

Let me look at the web frontend mind-map component and the update script:

*Novo passo iniciado*

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:44 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me look at the update scripts and a few more critical files to complete the picture.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:49 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me search more broadly.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:01:52 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Excellent! Now I have a very comprehensive picture of the entire codebase and the changes in the feature/mind-map-module branch. Let me compile all findings into a thorough report.

Key findings from the git diff:
1. The `loop_plugins/` directory was REMOVED and replaced with `capabilities/` - the old `LoopPlugin` protocol became `LoopCapability` protocol, and the `active_loop_plugins` / `LOOP_PLUGINS` were moved to `capabilities/__init__.py` with `active_loop_capabilities` / `LOOP_CAPABILITIES`
2. The mastery path plugin was moved from `loop_plugins/mastery/` to `capabilities/mastery/` - this is a major architectural refactor
3. New `i18n/` package was added with `metadata_i18n.py` (localized descriptions for tools/capabilities) and `status_i18n.py` (per-capability localized status strings via `StatusI18n`)
4. New `platform_messages.yaml` was added with full pedagogical guidelines (onboarding, status labels, progress bar, next step, module/objective, graph, summary)
5. New `project_state.py` API router + `ProjectMindMap.tsx` web component were added for the mind-map visualization

The mind-map module is essentially two parts:
1. **Backend**: `deeptutor/api/routers/project_state.py` - REST API that reads `project-state/ai-stem-tutor.json` and builds a `ProjectMindMap` (nodes + edges) with project, branch, commits, sessions, decisions, files, todos, and issues
2. **Frontend**: `web/components/project/ProjectMindMap.tsx` - Cytoscape.js-based interactive graph visualization of the project state

Also related: `scripts/update-project-state.ps1` - auto-sync script that generates the JSON state file.

Now let me write the comprehensive report.

</details>

### Resposta

Now I have a thorough understanding. Let me compile the full report.

---

## Complete DeepTutor Codebase Analysis — `feature/mind-map-module`

### 1. High-Level Directory Tree (`deeptutor/` — Top 3 Levels)

```
deeptutor/
├── agents/                          # Agent pipelines (entry points for capabilities)
│   ├── _shared/                     # Shared tool composition, capability results
│   ├── auto/                        # Auto-delegation pipeline (multi-agent orchestration)
│   ├── chat/                        # **Core tutoring loop** (agent_loop, agentic_pipeline, prompts)
│   ├── comic/                       # Comic strip generation agent
│   ├── math_animator/               # Manim animation generation agent
│   ├── notebook/                    # Notebook generation from sources
│   ├── question/                    # Deep Question generation pipeline
│   ├── research/                    # Deep Research pipeline (decompose → research → report)
│   ├── solve/                       # Deep Solve pipeline (plan → reason → write)
│   ├── vision_solver/               # Vision-based problem solver (GeoGebra integration)
│   └── visualize/                   # Visualization pipeline (SVG/Chart.js/Mermaid/Manim)
│
├── api/                             # FastAPI web API
│   ├── routers/                     # Route handlers (auth, knowledge, partners, settings,
│   │                                #   skills, subagents, tools, vision_solver, voice,
│   │                                #   project_state — mind-map endpoint)
│   ├── utils/                       # Task log streaming, tool options
│   └── main.py                      # FastAPI app factory + lifespan
│
├── app/                             # Python SDK facade
│   └── facade.py                    # DeepTutorApp — turn lifecycle, capability resolution
│
├── book/                            # Interactive Book engine (multi-page structured content)
│   ├── agents/                      # Page planner, spine synthesizer
│   ├── blocks/                      # Content block types (concept graph, etc.)
│   ├── compiler.py, engine.py, etc. # Compilation, execution, streaming
│   └── prompts/                     # en/zh prompt files
│
├── capabilities/                    # **Loop capabilities** (NEW in feature branch — replaces loop_plugins/)
│   ├── explore_context/             # Context exploration capability
│   ├── mastery/                     # **Mastery Path capability** (tools, loop, choices, prompts)
│   ├── obsidian/                    # Obsidian vault integration capability
│   ├── solve/                       # Solve capability (within chat loop)
│   ├── subagent/                    # Subagent capability
│   ├── protocol.py                  # LoopCapability / KnowledgeCapability protocol
│   └── registry.py                  # LOOP_CAPABILITIES registry
│
├── config/                          # App configuration
│
├── core/                            # Core abstractions (protocols, streams, context)
│   ├── agentic/                     # LLM client, tool dispatch, usage tracking
│   ├── capability_protocol.py       # BaseCapability + CapabilityManifest
│   ├── context.py                   # UnifiedContext (the single turn data object)
│   ├── stream.py / stream_bus.py    # StreamEvent protocol + async fan-out bus
│   ├── tool_protocol.py             # BaseTool + ToolDefinition + ToolResult
│   ├── trace.py                     # Tracing / observability
│   └── errors.py / i18n.py          # Error types, core i18n
│
├── events/                          # Event bus (EventBus for lifecycle events)
│
├── i18n/                            # NEW: Localization package
│   ├── metadata_i18n.py             # Localized capability/tool descriptions (en/zh)
│   └── status_i18n.py               # StatusI18n helper for streaming localized UI strings
│
├── knowledge/                       # Knowledge Base management
│   ├── manager.py                   # KB Manager (create, list, delete, provision)
│   ├── kb_types.py                  # KB type definitions (LightRAG, Obsidian, subagent, linked)
│   ├── initializer.py               # KB initialization
│   └── add_documents.py             # Document addition
│
├── learning/                        # **Student Modeling & Mastery Engine**
│   ├── grading.py                   # Deterministic answer grading (choice/short/open)
│   ├── mastery.py                   # Recency-weighted mastery scoring
│   ├── models.py                    # Pydantic models (KnowledgePoint, LearningProgress, etc.)
│   ├── policy.py                    # Mastery gate logic (is_mastered, next_objective, map_summary)
│   ├── scheduler.py                 # Spaced repetition scheduler (interval sequences per KP type)
│   ├── service.py                   # LearningService (orchestrates grading + mastery + scheduling)
│   ├── storage.py                   # JSON file-based persistence (LearningStore)
│   ├── prompts.py                   # Prompt template loading (diagnostic, explain, feynman, etc.)
│   ├── prompts/en/                  # English pedagogical prompts + platform_messages.yaml
│   └── tests/                       # Unit tests for mastery tools and choices
│
├── logging/                         # Structured logging (adapters, stats)
│
├── loop_plugins/                    # **REMOVED in this branch** — replaced by capabilities/
│
├── multi_user/                      # Multi-tenant identity, grants, model/knowledge/tool access
│
├── partners/                        # IM channel integrations (Telegram, Mattermost, etc.)
│
├── runtime/                         # Runtime orchestration & registries
│   ├── orchestrator.py              # ChatOrchestrator — unified entry point
│   ├── launcher.py                  # Backend + frontend lifecycle
│   ├── bootstrap/                   # Built-in capability/tool registration
│   ├── registry/                    # ToolRegistry + CapabilityRegistry
│   └── request_contracts.py         # Turn request schema definitions
│
├── services/                        # Backend services
│   ├── config/                      # Runtime settings, model catalog, provider config
│   ├── llm/                         # LLM client abstraction, providers, context window
│   ├── mcp/                         # **MCP server connection manager** (stdio/SSE/HTTP)
│   ├── memory/                      # Persistent memory (3-layer consolidation)
│   ├── rag/                         # **RAG service** (multi-provider: LlamaIndex, LightRAG, GraphRAG, PageIndex)
│   ├── session/                     # Session & turn runtime (SQLite + PocketBase stores)
│   ├── embedding/                   # Embedding service adapters
│   ├── imagegen/videogen/voice/     # Media generation services
│   ├── parsing/                     # Document parsing (Docling, MinerU, MarkItDown, PyMuPDF4LLM, text)
│   ├── sandbox/                     # Code execution sandbox
│   ├── search/                      # Web search providers
│   ├── skill/                       # Skill hub (ClawHub) integration
│   └── subagent/                    # Claude Code / Codex subagent management
│
├── skills/                          # Builtin skills (PDF skill, skill-creator)
│
├── tools/                           # Tool definitions
│   ├── builtin/                     # All built-in tool wrappers
│   ├── prompting/                   # Prompting tools (hints etc.)
│   ├── question/                    # Question tools
│   ├── vision/                      # Vision tools
│   ├── mastery_tool.py              # Compatibility re-exports for mastery tools
│   ├── media_gen_tool.py            # Image/video generation tool
│   ├── partner_memory.py            # Partner memory tool
│   └── solve_tool.py                # Solve tool
│
└── utils/                           # Utility modules (network, document validation)
```

### 2. Key Files by Subsystem

#### A. Tutoring / Dialogue Engine (How does the tutoring loop work?)

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\runtime\orchestrator.py` | **ChatOrchestrator** — the unified entry point. Routes a `UnifiedContext` to the selected capability (default: `chat`). Manages `StreamBus` lifecycle for streaming events. Publishes `CAPABILITY_COMPLETE` events. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\core\context.py` | **UnifiedContext** — single data object flowing through orchestrator → capability → tools. Contains `session_id`, `user_message`, `conversation_history`, `enabled_tools`, `active_capability`, `knowledge_bases`, `attachments`, `memory_context`, `persona_context`, `skills_manifest`, `source_manifest`. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\agents\chat\agent_loop.py` | **AgentLoop** — the core tutoring loop. One turn = one agent loop over a single growing conversation. Each round: LLM call → text streams as `content` block → tool calls dispatched with `role=tool` results appended back. A round without tool calls = finish. Has `ask_user` pause/resume for interactive questions. Max 8 rounds default. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\agents\chat\agentic_pipeline.py` | **AgenticChatPipeline** — assembles the full chat turn: tool composition, prompt assembly, multi-modal message preparation, KB seeding, memory injection, deferred tool loading. Runs the `AgentLoop`. Default max 8 LLM rounds. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\agents\chat\capability.py` | **ChatCapability** — wraps `AgenticChatPipeline` behind `BaseCapability`. Has stages `["exploring", "responding"]`. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\core\capability_protocol.py` | **BaseCapability** — abstract base. Manifest (name, description, stages, tools_used). Single `run(context, stream)` method. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\app\facade.py` | **DeepTutorApp** — Python SDK facade. `start_turn()`, `stream_turn()`, `cancel_turn()`, `submit_user_reply()`. Used by CLI and WebSocket. |

**How the loop works:** The Orchestrator receives a `UnifiedContext` -> resolves capability name -> creates a `StreamBus` -> calls `capability.run(context, bus)` -> the chat capability runs `AgenticChatPipeline` which assembles tools + prompts -> runs `AgentLoop` (LLM call loop with tool dispatch) -> streams events back through the `StreamBus` -> emits `DONE` event.

#### B. Student Modeling (How does it track student knowledge?)

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\models.py` | **Core data models**: `LearningProgress` (mastery levels per KP, quiz attempts, error records, repetition states, review queue, pending question, Feynman check retries). `KnowledgeType` (MEMORY/CONCEPT/PROCEDURE/DESIGN). `ErrorType` (structural/deviation/application/metacognitive). `LearningStage` (diagnostic→explain→feynman_check→practice→error_diagnosis→review→completed). |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\mastery.py` | **`compute_mastery()`** — recency-weighted accuracy scoring. Weights: `(0.5, 0.7, 0.85, 0.95, 1.0)`. Confidence caps: 1 attempt → max 0.5, 2 attempts → max 0.8. Single swap-able function — to plug IRT/BKT, replace this alone. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\service.py` | **LearningService** — orchestrates the full lifecycle: get/create progress, init modules, record quiz attempts, calculate/update mastery, grade_and_record (full post-answer pipeline), record_qualitative (CONCEPT/DESIGN Feynman gate), list_progress. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\storage.py` | **LearningStore** — JSON file persistence. Atomic writes with temp-file + replace. Thread-safe via module-level lock. Stores per `book_id` in workspace `learning/` directory. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\grading.py` | **Deterministic answer grading**: `grade_answer(user, expected, type)` — choice (exact match), short (exact or SequenceMatcher >= 0.85 for <= 30 chars), open (keyword overlap >= 60%). `classify_error()` — blank → METACOGNITIVE, else → APPLICATION. |

#### C. Dialogue Management (How does it manage conversation turns?)

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\session\turn_runtime.py` | **TurnRuntime** — manages turn lifecycle: start_turn, subscribe_turn, cancel_turn, submit_user_reply. Each turn is a task with `TurnContext` holding the session, bus reference, and cancellation support. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\session\sqlite_store.py` | **SqliteSessionStore** — persistent session storage in SQLite. CRUD for sessions, conversation history, turn events. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\core\stream_bus.py` | **StreamBus** — async fan-out bus. Capabilities emit `StreamEvent`s (content, tool_call, progress, error, done, etc.). Multiple consumers subscribe. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\core\stream.py` | **StreamEvent** protocol — typed events with `type`, `source`, `content`, `metadata`. Types: `SESSION`, `CONTENT`, `THINKING`, `TOOL_CALL`, `TOOL_RESULT`, `PROGRESS`, `ERROR`, `DONE`, etc. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\api\routers\unified_ws.py` | **WebSocket endpoint** (`/api/v1/ws`) — adapts the StreamBus to WebSocket frames. Bidirectional: receives user messages, streams back events. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\agents\chat\agentic_pipeline.py` | **Prompt assembly** — `ChatPromptAssembler` builds the system prompt from: persona, skills manifest, mastery tutor block, source manifest, KB seed, memory context. Handles `ask_user` pause/resume flow. |

**Turn flow:** 1. User sends message → 2. `DeepTutorApp.start_turn()` creates session+turn → 3. `ChatOrchestrator.handle()` routes to capability → 4. Capability runs pipeline which calls `AgentLoop` → 5. Loop streams events via `StreamBus` → 6. Consumer (CLI/WebSocket/SDK) subscribes to bus → 7. `@session` agent persists to Notion at end.

#### D. Knowledge Base / RAG (How are knowledge bases used?)

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\knowledge\manager.py` | **KnowledgeBaseManager** — full KB lifecycle: create, list, delete, provision (parse→chunk→embed), reindex, detect provider type, handle obsidian/linked/subagent KBs. 1788 lines. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\service.py` | **RAGService** — unified search entry point. Resolves provider per KB (LlamaIndex, LightRAG, GraphRAG, PageIndex, LightRAG Server). Routes search, initialize, add_documents to the bound pipeline. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\smart_retriever.py` | Smart retrieval with query rewriting, hybrid search (dense + sparse/BM25), and result fusion. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\rag\pipelines/` | Pipeline implementations: `llamaindex/`, `lightrag/`, `lightrag_server/`, `graphrag/`, `pageindex/`. Each has pipeline.py, config.py, storage.py. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\tools\builtin\__init__.py` | The `rag` tool — mounted auto-matically when KBs are present. Calls `RAGService.search()` with the query + kb_name. |

**RAG flow:** User attaches KBs → tool composition detects them → `rag` tool auto-mounted → tool calls `RAGService.search(query, kb_name)` → resolves provider (e.g. LlamaIndex) → runs pipeline search (embedding + retrieval + optional reranking) → returns content.

#### E. Assessment / Feedback (How does it evaluate student answers?)

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\grading.py` | **Deterministic grading** engine — `grade_answer(user, expected, type)`. Choice: exact match. Short: exact or fuzzy (SequenceMatcher >= 0.85). Open: keyword overlap >= 60%. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\capabilities\mastery\tools.py` | **MasteryGradeTool** — takes learner's answer, calls `LearningService.grade_and_record()`, returns `{is_correct, mastery, threshold, mastered, next}`. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\capabilities\mastery\tools.py` | **MasteryAssessTool** — qualitative assessment for CONCEPT/DESIGN. Records tutor's judgement (passed/failed + feedback). Used for Feynman-style checks. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\capabilities\mastery\choices.py` | **Choice question resolution** — parsing options, recovering from turn events, resolving answers with labels. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\prompts.py` | **Prompt templates** for each learning stage: diagnostic, explain, feynman, practice, error_diagnosis, review. Per-stage system + user prompts. |

**Assessment flow:** 1. Model calls `mastery_quiz` → registers question + expected answer server-side → 2. Model presents via `ask_user` tool → 3. Learner answers → 4. Model calls `mastery_grade` with answer → 5. `grade_answer()` compares deterministically → 6. `record_quiz_attempt()` updates mastery + spaced repetition → 7. Returns `{mastered: bool}` → 8. Model gives feedback.

#### F. Mastery Learning / Adaptive Path (How does it adapt to the student?)

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\policy.py` | **Mastery gate engine** — pure logic, no LLM calls. `QUANTITATIVE_GATE` (MEMORY/PROCEDURE → 0.9 threshold). `QUALITATIVE_TYPES` (CONCEPT/DESIGN — boolean gate). `is_mastered()` — hard gate. `next_objective()` — determines what to work on next. `map_summary()` — full map for dashboard. Priority: pending question → due review → first unmastered KP → complete. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\scheduler.py` | **SpacedRepetitionScheduler** — interval sequences per type: MEMORY=[0,1,3,7,14,30,60] days, CONCEPT=[3,7,14,30], PROCEDURE=[3,7,14], DESIGN=[14,28]. Correct → advance interval, 2 consecutive → advance 2 steps. Wrong → regress interval. Error KPs get priority in review queue. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\capabilities\mastery\capability.py` | **MasteryPathCapability** — sets `mastery_mode=True`, resolves path ID, runs standard `AgenticChatPipeline` with mastery tools mounted. The chat loop IS the tutor. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\capabilities\mastery\loop.py` | **MasteryLoopCapability** — LoopCapability that adds `mastery_tutor` system prompt block, injects `_mastery_path_id`/`_session_id`/`_turn_id` into tool kwargs. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\capabilities\mastery\tools.py` | **Five mastery tools**: `mastery_status` (read map), `mastery_quiz` (register question), `mastery_grade` (grade answer), `mastery_assess` (Feynman gate), `mastery_build` (create path). |

**Adaptation flow:** 1. Model calls `mastery_status` → gets `next_objective` from policy engine → 2. If `probe` → test-out question → 3. If `practice` → quiz (MEMORY/PROCEDURE) or Feynman check (CONCEPT/DESIGN) → 4. Grade answer → update mastery levels → 5. If gate cleared → `next_objective` returns next KP → 6. If not → keep working same KP → 7. Spaced repetition schedules reviews → `due_reviews` inserted at priority.

**Key design axiom:** "the intelligence lives at the loop's exit — the model decides what to teach and how to question — while the gate that decides whether the learner may advance is a deterministic engine call."

#### G. Mind-Map Module (The feature branch — what's new?)

The `feature/mind-map-module` branch introduces three major additions and one major refactor:

**New — Project State + Mind Map Visualization:**

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\api\routers\project_state.py` | **REST API** (`GET /api/v1/project/state`) — reads `project-state/ai-stem-tutor.json`, builds `ProjectMindMap` DTO with nodes (project, branch, commits, sessions, decisions, files, todos, issues) and edges. Each node has id/label/type/subtitle/color. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\web\components\project\ProjectMindMap.tsx` | **Cytoscape.js component** — interactive graph visualization. Fetches from `/api/v1/project/state`, renders force-directed layout with color-coded node types (project=indigo, branch=purple, commit=green, session=blue, decision=amber, todo=red, issue=red, file=emerald). Includes loading state, error handling, empty state. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\project-state\ai-stem-tutor.json` | **Persisted project state** — auto-generated by `update-project-state.ps1`. Contains project metadata, git log, sessions, decisions, todos, issues. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\project-state\ai-stem-tutor.md` | **Human-readable project state summary** — auto-generated markdown with git log, recent sessions, accumulated decisions, next steps. |
| `C:\Users\frota\.local\share\opencode\scripts\update-project-state.ps1` | **Auto-sync script** — generates the JSON state file from live doc + git log. Versioned in git alongside the project. |

**New — Pedagogical Guidelines & Platform Messages:**

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\learning\prompts\en\platform_messages.yaml` | Full i18n platform messages: onboarding, status labels (new/learning/mastered/due_review), next step actions (probe/practice/assess/review/complete), module/objective display, concept graph labels, and **pedagogical summary suggestions** ("write a paragraph summarizing..."). |

**New — i18n Infrastructure:**

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\i18n\__init__.py` | Package init exporting `StatusI18n`, `capability_description_i18n`, `tool_description_i18n`. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\i18n\metadata_i18n.py` | Localized descriptions for all 7 capabilities and 7 tools in en/zh. Used by settings UI. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\i18n\status_i18n.py` | `StatusI18n` class — per-capability localized status string lookup via `PromptManager`. Replaces hardcoded English strings with locale-aware `.t(key, default, **kwargs)`. |

**Major Refactor — `loop_plugins/` → `capabilities/`:**

The entire `loop_plugins/` directory (protocol, registry, mastery plugin, mastery tools, mastery prompts) was **deleted** and reimplemented as `capabilities/`:

- **Old:** `deeptutor/loop_plugins/{protocol.py, registry.py, mastery/{__init__.py, plugin.py, tools.py, prompts/}}`
- **New:** `deeptutor/capabilities/{protocol.py, registry.py, __init__.py, mastery/{__init__.py, loop.py, capability.py, tools.py, prompts/}}`

Key changes:
- `LoopPlugin` protocol → `LoopCapability` protocol (with `exclusive_tools` support for KnowledgeCapability subclasses)
- `active_loop_plugins()` → `active_loop_capabilities()` 
- `LOOP_PLUGINS` → `LOOP_CAPABILITIES`
- Mastery tool kwargs injection now adds `_session_id` and `_turn_id` alongside `_mastery_path_id`
- New `KnowledgeCapability` class for KB-bound exclusive-turn capabilities

#### H. MCP Integration (How are MCP servers used in tutoring?)

| File | Purpose |
|------|---------|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\mcp\manager.py` | **MCPConnectionManager** — app-level singleton owning all MCP server connections. `ensure_started()` (lazy connect), `reload()` (diff config, restart changed servers). Each server gets a dedicated connection task with `AsyncExitStack`. Supports stdio, SSE, streamableHttp transports. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\mcp\config.py` | **MCPConfig / MCPServerConfig** — Pydantic models for deployment-global MCP config (`settings/mcp.json`). Per-server: type (auto-detected), command/args/env (stdio), url/headers (HTTP), tool_timeout, enabled_tools whitelist. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\mcp\session_state.py` | Session state management for MCP connections. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\mcp\network.py` | Network utilities for MCP connections. |
| `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\mcp\__init__.py` | Exports `MCPConnectionManager`, `MCPToolAdapter`, `mcp_config_path`, `wrapped_tool_name`. |

**MCP tool adapter:** Each MCP server tool is wrapped as `MCPToolAdapter(BaseTool)` with `deferred=True` (schemas reach the model via `load_tools` progressive disclosure, not initial tool list). Tool names are prefixed `mcp_<server>_<tool>`. They execute via `MCPConnectionManager.call_tool()`. Adapters are synced into the global `ToolRegistry` for standard dispatch.

**MCP lifecycle:** Config loaded from `settings/mcp.json` → `ensure_started()` connects all enabled servers → each server gets a task owning `AsyncExitStack` → connects transport → publishes tool adapters to `ToolRegistry` → waits on shutdown event → exits. `reload()` diffs config and only restarts changed servers.

### 3. Git Diff — `feature/mind-map-module` vs `main`

**Summary: 889 files changed, 62,565 insertions(+), 40,224 deletions(-)**

The branch is based on `v1.5.1` (main was `v1.4.5`). Three dedicated commits:

| Commit | Message |
|--------|---------|
| `d36e8244` | **feat: mind map module + pedagogical guidelines + platform messages** |
| `d8e5dda3` | **feat: project-state tracking for cross-session context pipeline** |
| `384b6a70` | **feat: Project Mind Map visualization + project-state auto-sync** |

**Major changes:**

1. **New `deeptutor/i18n/` package** — `metadata_i18n.py`, `status_i18n.py`, `__init__.py`
2. **New `deeptutor/learning/prompts/en/platform_messages.yaml`** — full pedagogical i18n labels
3. **New API router** — `deeptutor/api/routers/project_state.py`
4. **New web component** — `web/components/project/ProjectMindMap.tsx`
5. **New project-state files** — `project-state/ai-stem-tutor.json`, `project-state/ai-stem-tutor.md`
6. **Deleted `deeptutor/loop_plugins/`** (entire directory: protocol, registry, mastery plugin + tools + prompts)
7. **Created `deeptutor/capabilities/`** — `protocol.py`, `registry.py`, `__init__.py`, plus `mastery/` (moved from loop_plugins with enhancements), `explore_context/`, `obsidian/`, `solve/`, `subagent/`
8. **Updated** all agent pipelines (chat, solve, question, research, visualize, math_animator) to use new capabilities pattern
9. **Version bump** `v1.4.5` → `v1.5.1`
10. **Various API routers updated** (auth, imports, knowledge, partners, plugins, settings, skills, subagents, tools, vision_solver, voice)
11. **Updated** RAG pipelines (GraphRAG, LightRAG, LightRAG Server, LlamaIndex, PageIndex)
12. **Updated** services (memory, parsing, session, skill, subagent, partners)
13. **Updated** multi-user auth, grants, and access control
14. **Updated** CLI (`deeptutor_cli/main.py`) with new subcommands

### 4. Main Entry Points

#### CLI: `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor_cli\main.py`

Typer-based CLI with subcommands:
- `deeptutor run <capability> <message>` — run any capability in a single turn
- `deeptutor chat` — interactive REPL
- `deeptutor serve --port` — API server only
- `deeptutor start` — backend + frontend together
- `deeptutor partner`, `deeptutor kb`, `deeptutor skill(s)`, `deeptutor memory`, `deeptutor plugin`, `deeptutor config`, `deeptutor session`, `deeptutor notebook`, `deeptutor provider`, `deeptutor book`, `deeptutor init`

The `run` command accepts `--tool`, `--kb`, `--notebook-ref`, `--history-ref`, `--language`, `--config`, `--config-json`, `--format`.

#### SDK Facade: `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\app\facade.py`

`DeepTutorApp` class:
- `resolve_capability(value)` — resolves name/alias → canonical capability
- `get_capability_contracts()` — all manifests + availability
- `start_turn(request)` — creates session + turn, returns `(session, turn)`
- `stream_turn(turn_id, after_seq)` — async generator of turn events
- `cancel_turn(turn_id)` — cancellation
- `submit_user_reply(turn_id, text, answers)` — for `ask_user` pause/resume

`TurnRequest` dataclass: content, capability, session_id, tools, knowledge_bases, language, config, notebook_references, history_references, attachments, skills.

#### API: `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\api\main.py`

FastAPI app with:
- Lifespan: ensures runtime settings, exports to env, configures logging
- Validation: `validate_tool_consistency()` checks capability manifests reference only registered tools
- Mounts: WebSocket endpoint, REST routers, static files (whitelisted via `SafeOutputStaticFiles`)
- CORS middleware
- Routers: auth, imports, knowledge, partners, plugins, project_state, settings, skills, subagents, tools, vision_solver, voice
- WebSocket endpoint at `/api/v1/ws` — bidirectional streaming

---

### Architecture Diagram (Simplified)

```
Entry Points
  CLI (deeptutor_cli/main.py)   WebSocket (/api/v1/ws)   Python SDK (DeepTutorApp)
          │                            │                        │
          └────────────────────────────┼────────────────────────┘
                                       ▼
                           ChatOrchestrator
                        (runtime/orchestrator.py)
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
          CapabilityRegistry      ToolRegistry
          (runtime/registry/)    (runtime/registry/)
                    │                     │
                    ▼                     ▼
          BaseCapability.run()        BaseTool.execute()
          (core/capability_protocol)  (core/tool_protocol)
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
   Chat Capability        MasteryPath Capability
   (agents/chat/)         (capabilities/mastery/)
         │                     │
         ▼                     ▼
   AgenticChatPipeline    AgenticChatPipeline  (same loop!)
   ┌─────────────────┐   ┌──────────────────────┐
   │ 1. Tool compose  │   │ + MasteryLoopCapability │
   │ 2. Prompt build  │   │ + Mastery tools mounted │
   │ 3. AgentLoop     │   │ + Tutor system prompt   │
   │    (LLM ↔ tools) │   └──────────┬───────────────┘
   └────────┬─────────┘              │
            ▼                        ▼
       AgentLoop (agents/chat/agent_loop.py)
       ┌─────────────────────────────────┐
       │ Round 1: LLM → text + tool calls │
       │ Round 2: tool results → LLM      │
       │ ... until no tool calls → finish  │
       └──────────┬──────────────────────┘
                  │
                  ▼
           LearningService
         (learning/service.py)
         ┌──────────────────────────┐
         │ grade_and_record()       │
         │  → grade_answer()        │
         │  → compute_mastery()     │
         │  → scheduler.schedule()  │
         │  → record_quiz_attempt() │
         └──────────┬───────────────┘
                    ▼
            LearningStore (JSON)
         + SpacedRepetitionScheduler
         + Mastery Policy (next_objective)
```

### Cross-Reference Notes for Memphis Papers

Key architectural points relevant to ITS literature (Anderson's ACT-R tutors, VanLehn's 2-sigma / 4-component architecture, Bloom's mastery learning):

1. **Mastery gate (0.9 threshold)** mirrors Alpha School's "90% before you advance" — pure behavioral mastery criterion.

2. **Knowledge type taxonomy** (MEMORY/CONCEPT/PROCEDURE/DESIGN) maps to Anderson's ACT-R declarative → procedural distinction, plus Krathwohl's revision of Bloom's taxonomy.

3. **Recency-weighted mastery** with confidence caps is a simpler alternative to BKT/IRT — intentionally swappable via `compute_mastery()`.

4. **Feynman-style qualitative assessment** for CONCEPT/DESIGN types mirrors VanLehn's "assess" stage in the 4-component architecture.

5. **Spaced repetition scheduler** per knowledge type with error-based priority mirrors Leitner + SM-2 principles.

6. **Chat loop IS the tutor** — the model handles pedagogical strategy (Socratic dialogue, scaffolding, worked examples), while the gate is deterministic — a hybrid of generative AI and rule-based classical ITS.

7. **Multi-layer architecture** (Orchestrator → Capability → Agent Loop → Tools → Services) mirrors VanLehn's 4-component architecture (tutor → domain → student → interface).

*Novo passo iniciado*

---

*24 messages | 143 parts | 💰 $0.0000 | ⏱️ 0h02m49s*
