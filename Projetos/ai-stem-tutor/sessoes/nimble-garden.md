---
title: "nimble-garden"
slug: "nimble-garden"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: nimble-garden
title: "Explore TUTOR project structure (@explore subagent)"
date: 2026-07-01
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h01m04s
messages: 10
parts: 100
cost: 0.009217
tokens_input: 46716
tokens_output: 6644
tokens_reasoning: 421
tokens_cache_read: 249344
tokens_cache_write: 0
created: "2026-07-01 19:55:36 UTC"
updated: "2026-07-01 19:56:41 UTC"
---

SessÃ£o com **10 messages**, **100 parts**, agente **explore**, modelo **deepseek-v4-flash** | ðŸ’° $0.0092 | ðŸ’¾ cache read: 249.3K | â±ï¸ 0h01m04s

## ðŸ‘¤ UsuÃ¡rio (2026-07-01 19:55:36 UTC)

Explore the codebase to find the TUTOR project. Look for:
1. Where the TUTOR project lives on the filesystem (search common locations like Desktop, Documents, C:\, D:\, repos, etc.)
2. How it is structured (main folders, entry points, architecture)
3. How subprojects/modules are organized within TUTOR (look for existing subprojects to understand the pattern)
4. Any configuration files that define subprojects (package.json, config files, etc.)

Search broadly - use glob patterns like "**/TUTOR/**", "**/tutor/**", "**/*tutor*", and also check common directories. Return:
- Full path to the TUTOR project root
- Directory listing of the root
- How subprojects are organized (structure and naming)
- Any configuration or manifest files that register subprojects
- A sample of an existing subproject (its folder structure and key files)

## ðŸ¤– Assistente (2026-07-01 19:55:36 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants me to explore the filesystem to find a TUTOR project. Let me search broadly using multiple strategies to locate it.

</details>

### Resposta

I'll conduct a thorough search for the TUTOR project across the filesystem using multiple strategies in parallel.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-01 19:55:43 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

I found the TUTOR project at `C:\Users\frota\Documents\Projetos\AI TUTOR`. Let me explore this directory in detail.

</details>

### Resposta

Found it! The TUTOR project is at `C:\Users\frota\Documents\Projetos\AI TUTOR`. Let me now explore it in depth.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-01 19:55:46 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me get the full directory listing and explore the key files to understand the project structure. I need to look at:
1. The root directory structure in more detail
2. pyproject.toml - key config file
3. AGENTS.md - project guidelines
4. The main Python package (deeptutor/)
5. Subprojects/modules structure
6. The web frontend (web/)
7. CLI module (deeptutor_cli/)

</details>

### Resposta

Let me get a deeper look at the key parts of the project.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-01 19:55:52 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me explore deeper into the key sub-modules within `deeptutor/` to understand how capabilities, tools, and the core architecture are organized. Let me also look at the `packaging/` directory, `skills/`, `agents/`, and `capabilities/` subdirectories.

</details>

### Resposta

Excellent! Now let me explore the internal structure of the main packages, capabilities, tools, and the packaging directory.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-01 19:55:58 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me now look at the packaging directory, the skills/builtin directory, and a sample capability and tool to understand the full picture. Also let me check the `deeptutor/learning/` directory and the `co_writer/` directory.

</details>

### Resposta

Let me now check a few more important subdirectories to complete the picture.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-01 19:56:03 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me look at a sample capability implementation, the builtin skills structure, and the agents sub-directories to understand the subproject pattern. Let me also look at the `prompts` inside capabilities and the vision_solver agent as an example.

</details>

### Resposta

Let me now look at sample subproject structures -- a builtin skill, a capability agent, and the vision solver.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-01 19:56:09 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me now read a sample SKILL.md file and a sample capability to get the full picture of subproject structure.

</details>

### Resposta

Let me read a couple of representative files to understand the patterns.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-01 19:56:13 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a comprehensive picture of the TUTOR project. Let me also check for the `packaging/deeptutor-cli/pyproject.toml` file and the `web/package.json` to understand the full packaging story.

</details>

### Resposta

Let me check the packaging CLI project and the web frontend package.json for completeness.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-01 19:56:17 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a comprehensive understanding of the TUTOR project. Let me compile my findings into a clear report.

</details>

### Resposta

Now I have a complete picture. Here is the comprehensive report:

---

## TUTOR Project (DeepTutor) -- Full Exploration Report

### 1. Project Location

**Root path:** `C:\Users\frota\Documents\Projetos\AI TUTOR`

The project is a clone of the open-source **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** repository (v1.4.5), an agent-native intelligent tutoring platform.

---

### 2. Root Directory Structure

```
C:\Users\frota\Documents\Projetos\AI TUTOR\
â”œâ”€â”€ deeptutor/                  # Main Python package (the core engine)
â”œâ”€â”€ deeptutor_cli/              # CLI entry point package (Typer-based)
â”œâ”€â”€ deeptutor_web/              # Web asset packaging shim (thin wrapper)
â”œâ”€â”€ deeptutor.egg-info/         # Egg metadata (installed in dev mode)
â”œâ”€â”€ web/                        # Next.js 16 frontend (TypeScript)
â”œâ”€â”€ site/                       # Astro-based documentation site (deeptutor.info)
â”œâ”€â”€ packaging/                  # Alternate distribution projects
â”‚   â””â”€â”€ deeptutor-cli/          #   CLI-only PyPI package definition
â”œâ”€â”€ data/                       # Runtime data (user settings, KBs, memory, partners)
â”œâ”€â”€ assets/                     # Logos, README translations, architecture diagrams
â”œâ”€â”€ docs/                       # Project-specific documentation
â”œâ”€â”€ scripts/                    # Utility scripts (extraction, ingestion, testing)
â”œâ”€â”€ tests/                      # Test suite
â”œâ”€â”€ requirements/               # Dependency requirement files (mirror extras)
â”œâ”€â”€ docs-html/                  # HTML/CSS tutorial docs (15 lessons)
â”œâ”€â”€ .github/                    # CI/CD workflows
â”œâ”€â”€ .venv/                      # Python virtual environment
â”‚
â”œâ”€â”€ pyproject.toml              # Python project config (setuptools + tooling)
â”œâ”€â”€ Dockerfile                  # Main Docker image
â”œâ”€â”€ Dockerfile.runner           # Sandbox runner sidecar
â”œâ”€â”€ docker-compose.yml          # Docker Compose (main)
â”œâ”€â”€ docker-compose.dev.yml      # Docker Compose (dev)
â”œâ”€â”€ docker-compose.ghcr.yml     # Docker Compose (GHCR)
â”œâ”€â”€ AGENTS.md                   # Project architecture guide for AI agents
â”œâ”€â”€ SKILL.md                    # Agent handoff doc (~150 lines)
â”œâ”€â”€ README.md                   # Full project documentation
â”œâ”€â”€ CONTRIBUTING.md             # Contribution guidelines
â”œâ”€â”€ CITATION.cff                # Citation metadata
â”œâ”€â”€ Communication.md            # Community communication channels
â”œâ”€â”€ LICENSE                     # Apache 2.0
â”œâ”€â”€ MANIFEST.in                 # Python sdist manifest
â”œâ”€â”€ .pre-commit-config.yaml     # Pre-commit hooks
â”œâ”€â”€ .secrets.baseline           # Secrets scanning baseline
â”œâ”€â”€ .gitignore / .gitattributes / .dockerignore
```

---

### 3. Architecture Overview

The project follows a **two-layer plugin model** organized around:

```
Entry Points:  CLI (Typer)  |  WebSocket /api/v1/ws  |  Python SDK
                    â†“                  â†“                     â†“
              â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
              â”‚              ChatOrchestrator                    â”‚
              â”‚   routes UnifiedContext â†’ selected Capability    â”‚
              â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                         â”‚              â”‚
              â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¼â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â–¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
              â”‚ ToolRegistry â”‚  â”‚ CapabilityRegistry â”‚
              â”‚  (Level 1)   â”‚  â”‚   (Level 2)        â”‚
              â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

- **Level 1 -- Tools:** Single-shot functions the LLM invokes on demand (e.g., `web_search`, `rag`, `exec`, `code_execution`, `ask_user`, `reason`, `brainstorm`, etc.)
- **Level 2 -- Capabilities:** Multi-stage pipelines that own the entire turn (e.g., `chat`, `deep_solve`, `deep_research`, `visualize`, `mastery_path`, `auto`, `math_animator`)

---

### 4. Subproject/Module Organization

The project is structured as a **monorepo** with these key packages and subprojects:

#### A. Core Python Package: `deeptutor/` (24 submodules)

| Submodule | Purpose |
|-----------|---------|
| `deeptutor/agents/` | Agent implementations per capability (chat, solve, research, visualize, vision_solver, auto, question, math_animator, comic) |
| `deeptutor/capabilities/` | Capability wrappers that register and run agents (chat, auto, deep_solve, deep_question, deep_research, visualize, mastery_path, math_animator) |
| `deeptutor/tools/` | Tool implementations (builtin, rag, web_search, paper_search, reason, brainstorm, exec, cron, vision, question, ask_user, etc.) |
| `deeptutor/core/` | Core abstractions: `BaseCapability`, `BaseTool`, `UnifiedContext`, `StreamBus`, streaming protocol |
| `deeptutor/runtime/` | Orchestrator, launcher, mode handling, bootstrap, registries |
| `deeptutor/services/` | Service layer: LLM, embedding, RAG, config, auth, memory, MCP, partners, sandbox, cron, search, sessions |
| `deeptutor/api/` | FastAPI WebSocket/HTTP API server |
| `deeptutor/app/` | `DeepTutorApp` -- Python SDK facade |
| `deeptutor/skills/` | Built-in office skills (docx, pdf, pptx, xlsx, skill-creator) |
| `deeptutor/book/` | Book Engine -- "living books" from compiled sources |
| `deeptutor/co_writer/` | Collaborative Markdown editing workspace |
| `deeptutor/learning/` | Mastery learning engine (mastery paths, grading, policy, scheduling) |
| `deeptutor/partners/` | IM-connected companion bots (Telegram, Slack, Feishu, etc.) |
| `deeptutor/events/` | Event bus for inter-component communication |
| `deeptutor/loop_plugins/` | Extensible agent loop plugin framework |
| `deeptutor/multi_user/` | Multi-user deployment (auth, grants, per-user isolation) |
| `deeptutor/knowledge/` | Knowledge Base management (LlamaIndex RAG) |
| `deeptutor/config/` | Configuration schema, defaults, settings accessors |
| `deeptutor/logging/` | Structured logging, adapters, stats |
| `deeptutor/utils/` | Shared utilities (JSON parser, document extractor, error handling, network) |
| `deeptutor/memory/` | 3-layer memory system |
| `deeptutor/__version__.py` | Version: **1.4.5** |

#### B. CLI Package: `deeptutor_cli/` (18 files)

- `main.py` -- Typer CLI entry point
- Subcommands: `chat.py`, `kb.py`, `memory.py`, `book.py`, `partner.py`, `skill.py`, `notebook.py`, `session_cmd.py`, `config_cmd.py`, `init_cmd.py`, `init_wizard.py`, `plugin.py`, `provider_cmd.py`, `common.py`

#### C. Web Frontend: `web/`

- Next.js 16 / React 19 / TypeScript
- Entry: `web/app/layout.tsx`, `web/app/globals.css`
- Config: `web/package.json` (name: `opentutor-web`), `next.config.js`, `tailwind.config.js`

#### D. Documentation Site: `site/`

- Astro-based static site (`site/astro.config.mjs`, `site/src/`)
- Deployed at `deeptutor.info`

#### E. Alternative Distribution: `packaging/deeptutor-cli/`

- Standalone `pyproject.toml` for CLI-only pip install (`deeptutor-cli`)

---

### 5. Configuration Files That Define Subprojects

| File | Purpose |
|------|---------|
| **`pyproject.toml`** (root) | Main Python project config. Defines package name `deeptutor`, entry point `deeptutor = "deeptutor_cli.main:main"`, find packages `include = ["deeptutor*", "deeptutor_cli*"]`, 8 dependency extras (`cli`, `server`, `partners`, `matrix`, `matrix-e2e`, `math-animator`, `dev`, `all`) |
| **`packaging/deeptutor-cli/pyproject.toml`** | CLI-only distribution. Package name `deeptutor-cli`, uses same source tree with `exclude = ["deeptutor_web*"]` |
| **`web/package.json`** | Frontend npm package (`opentutor-web`, Next.js 16) |
| **`site/package.json`** | Documentation site (`astro`) |
| **`docker-compose.yml`** | Defines main + runner services |
| **`Dockerfile`** | Main container build |
| **`Dockerfile.runner`** | Sandbox runner sidecar |
| **`AGENTS.md`** | Architecture documentation for AI agents (lives in root, loaded by OpenCode) |
| **`SKILL.md`** | Agent handoff doc that teaches any LLM how to drive DeepTutor |

---

### 6. Sample Subproject: Builtin Skill (`docx`)

**Path:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\skills\builtin\docx\`

**Structure:**
```
deeptutor/skills/builtin/docx/
â””â”€â”€ SKILL.md          # Single-file skill definition
```

This is the representative **subproject pattern**: each builtin skill is a folder with a single `SKILL.md` file that contains:
- YAML frontmatter: `name`, `description`, `tags`, `requires` (sandbox type)
- Markdown body: usage instructions, code examples, constraints

The same pattern is used by all 5 builtin skills:
- `deeptutor/skills/builtin/docx/SKILL.md`
- `deeptutor/skills/builtin/pdf/SKILL.md`
- `deeptutor/skills/builtin/pptx/SKILL.md`
- `deeptutor/skills/builtin/xlsx/SKILL.md`
- `deeptutor/skills/builtin/skill-creator/SKILL.md`

### 7. Sample Subproject: Agent (`vision_solver`)

**Path:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\agents\vision_solver\`

**Structure:**
```
deeptutor/agents/vision_solver/
â”œâ”€â”€ __init__.py
â”œâ”€â”€ vision_solver_agent.py    # Main agent class (735 lines, 4-stage pipeline)
â”œâ”€â”€ models.py                 # Pydantic data models
â””â”€â”€ prompts/
    â”œâ”€â”€ analysis.md           # Stage prompt: geometric analysis
    â”œâ”€â”€ bbox.md               # Stage prompt: bounding box detection
    â”œâ”€â”€ ggbscript.md          # Stage prompt: GeoGebra script generation
    â”œâ”€â”€ reflection.md         # Stage prompt: validation/reflection
    â””â”€â”€ tutor.md              # Tutoring prompt override
```

This is the standard **agent subproject pattern**: an `__init__.py`, a main agent module, supporting models, and a `prompts/` directory with markdown prompt files for each stage.

### 8. Sample Subproject: Capability (`chat`)

**Path:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\capabilities\chat.py`

Minimal registration file (27 lines) that:
- Declares a `CapabilityManifest` with name, description, stages, tools
- Runs the `AgenticChatPipeline` from `deeptutor.agents.chat`

---

### Summary of Subproject Patterns

The TUTOR project organizes subprojects/modules via:

1. **Python packages under `deeptutor/`**: Each domain (agents, capabilities, tools, services, etc.) is a subpackage with `__init__.py`. Agents and capabilities follow a consistent `manifest` + pipeline pattern.

2. **Builtin skills as single `SKILL.md` files**: Each skill is a folder with one `SKILL.md` containing YAML frontmatter and markdown instructions.

3. **Dependency extras in `pyproject.toml`**: `cli`, `server`, `partners`, `matrix`, `math-animator`, `dev`, `all` define installable subproject profiles.

4. **Separate distributable packages in `packaging/`**: Currently `deeptutor-cli` only.

5. **Frontend as `web/` package**: Independent Next.js app with its own `package.json`.

*Novo passo iniciado*

---

*10 messages | 100 parts | ðŸ’° $0.0092 | â±ï¸ 0h01m04s*

