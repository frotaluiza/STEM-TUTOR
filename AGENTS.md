# DeepTutor — Agent-Native Architecture

## ⚠️ Ciclo Obrigatório de Artefatos — Aplicável a TODOS os Agentes

**Toda alteração de código, decisão arquitetural, ou finalização de sessão DEVE gerar artefatos markdown no diretório `Projetos/{slug}/artefatos/`.**

### Estrutura Obrigatória

```
Projetos/ai-stem-tutor/
├── artefatos/
│   ├── YYYY-MM-DD--{slug-da-sessao}--changelog.md   ← log de alterações
│   └── YYYY-MM-DD--{slug-da-sessao}--relatorio.md   ← relatório de testes/erros
├── relatorios/                                       ← relatórios periódicos
├── sessoes/                                          ← live docs (watcher)
└── project-state.yaml                                ← orchestrator
```

### Formato do Changelog

```markdown
# Changelog — {Título da Sessão}
**Data:** YYYY-MM-DD | **Branch:** {branch} | **Sessão:** {slug}

## Alterações Realizadas
- {arquivo}: {descrição da mudança}
- ...

## Decisões
- {decisão}

## Arquivos Modificados
- `{caminho/do/arquivo}` (criação/modificação)
```

### Formato do Relatório

```markdown
# Relatório — {Título da Sessão}
**Data:** YYYY-MM-DD | **Branch:** {branch}

## Testes Executados
| Framework | Comando | Resultado | Duração |
|-----------|---------|-----------|---------|
| tsc --noEmit | `npx tsc --noEmit` | Aprovado/Falhou | Xs |

## Erros Encontrados
```
{log de erros, se houver}
```

## Observações
- {notas relevantes}
```

### Ciclo Obrigatório

1. **Antes de codar**: Planejar artefatos que serão gerados
2. **Durante**: Manter changelog mental
3. **Ao final da sessão (OU a cada commit significativo)**:
   a. Gerar `changelog.md` com todas as alterações
   b. Executar testes (tsc --noEmit, pytest, etc.)
   c. Gerar `relatorio.md` com resultados
   d. Atualizar `project-state.yaml` (orquestrador)
   e. Atualizar `project-state/` (branch atual)
    f. Commitar artefatos junto com o código

## ✅ Tarefas de Sessão — Registro Obrigatório

**Toda ideia, tarefa pendente, ou próximo passo identificado durante uma conversa DEVE ser registrado como tarefa no PM.**

### Como registrar

Via API REST:

```bash
curl -X POST http://localhost:8001/api/v1/pm/tarefas \
  -H "Content-Type: application/json" \
  -d '{"text": "Implementar feature X", "branch": "feature/y", "session_slug": "calm-canyon", "prioridade": "alta"}'
```

Ou diretamente pelo **PM Dashboard** → painel **Tarefas** → campo "Nova tarefa".

### Campos

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `text` | string | ✅ | Descrição da tarefa |
| `feito` | boolean | — | `false` por padrão |
| `prioridade` | string | — | `alta`, `media` (default), `baixa` |
| `session_slug` | string | — | Slug da sessão opencode que gerou a tarefa |
| `branch` | string | — | Branch do projeto (default: `main`) |
| `tags` | string[] | — | Tags para categorização |

### Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/api/v1/pm/tarefas?branch=main` | Listar tarefas |
| `POST` | `/api/v1/pm/tarefas` | Criar tarefa |
| `PATCH` | `/api/v1/pm/tarefas/{id}` | Atualizar (toggle feito, texto, prioridade) |
| `DELETE` | `/api/v1/pm/tarefas/{id}?branch=main` | Excluir tarefa |

### Ciclo

1. ⚡ Durante a conversa, ao identificar uma tarefa → **registrar imediatamente** via `POST /api/v1/pm/tarefas`
2. 🔄 Ao concluir → toggle `feito: true` via PM Dashboard ou `PATCH`
3. 📋 O PM mostra em tempo real o painel **Tarefas** com contagem de pendentes

## Guidelines Pedagógicas — Aplicável a TODOS os Agentes

Sempre que um agente estiver explicando ou conduzindo um aluno por um conceito, módulo ou seção de estudo, ele DEVE:

1. **Sugerir resumo escrito**: Ao final de cada mini-módulo ou seção conceitual, sugerir que o aluno escreva um resumo do que aprendeu naquela seção.
2. **Modularizar a sessão**: Organizar a explicação em blocos claros que o aluno possa processar um de cada vez.
3. **Incentivar a escrita ativa**: Escrever com as próprias palavras é mais eficaz que reler passivamente.
4. **Contextualizar o resumo**: Conectar o resumo atual com conceitos de módulos anteriores.

---

## Overview

DeepTutor is an **agent-native** intelligent learning companion organized
around a two-layer plugin model — single-shot **Tools** invoked by the
LLM, and multi-stage **Capabilities** that take over a turn — exposed
through three entry points: CLI, WebSocket API, and Python SDK.

## Architecture

```
Entry Points:  CLI (Typer)  |  WebSocket /api/v1/ws  |  Python SDK
                    ↓                   ↓                   ↓
              ┌─────────────────────────────────────────────────┐
              │              ChatOrchestrator                    │
              │   routes UnifiedContext → selected Capability    │
              │   (defaults to `chat`)                           │
              └──────────┬──────────────┬───────────────────────┘
                         │              │
              ┌──────────▼──┐  ┌────────▼──────────┐
              │ ToolRegistry │  │ CapabilityRegistry │
              │  (Level 1)   │  │   (Level 2)        │
              └──────────────┘  └────────────────────┘
```

All capabilities emit on a shared `StreamBus`; the orchestrator fans
events out to consumers. Runtime settings live in
`data/user/settings/*.json` — project-root `.env` files are intentionally
ignored.

### Level 1 — Tools

Single-function tools the LLM picks on demand. Four user-toggleable tools
surface in `/settings/tools`:

| Tool           | Description                                   |
| -------------- | --------------------------------------------- |
| `brainstorm`   | Breadth-first idea exploration with rationale |
| `web_search`   | Web search with citations                     |
| `paper_search` | arXiv preprint search                         |
| `reason`       | Dedicated deep-reasoning LLM call             |

The rest are **context-gated**: the chat capability auto-mounts them from
`ToolMountFlags` (presence of a KB, attachments, sandbox availability, …), and
any of them can also be force-enabled via `--tool`. Auto-mounted set: `rag`,
`read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`,
`exec`, `code_execution` (sandboxed Python: NL intent → code → run),
`list_notebook`, `write_note`, `web_fetch`, `github`, `cron`,
`ask_user` (pauses the turn and resumes with the user's reply), plus the
mastery-path tools. `geogebra_analysis` is parked under
`COMING_SOON_TOOL_TYPES`.

### Level 2 — Capabilities

Multi-stage pipelines that own the turn:

| Capability       | Stages                                                |
| ---------------- | ----------------------------------------------------- |
| `chat`           | exploring → responding (single agentic loop, default) |
| `mastery_path`   | responding (Guided Learning — chat loop + mastery tools, gated per topic type) |
| `deep_solve`     | planning → reasoning → writing                        |
| `deep_question`  | ideation → generation                                 |
| `deep_research`  | rephrasing → decomposing → researching → reporting    |
| `visualize`      | analyzing → generating → reviewing (SVG / Chart.js / Mermaid / HTML; or routes to Manim sub-stages via `render_type`) |
| `math_animator`  | concept_analysis → concept_design → code_generation → code_retry → summary → render_output |

All capabilities converge on `emit_capability_result()` in
`deeptutor/capabilities/_shared.py` so every turn emits the same envelope
(response payload + `cost_summary` from `UsageTracker`). Status copy and
prompts are i18n'd via `capabilities/prompts/{en,zh}/<name>.yaml`.

## CLI Usage

```bash
# Install
pip install deeptutor      # Full app (CLI + Web/API + packaged Web assets)
pip install deeptutor-cli  # CLI-only

# Run any capability
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2=4" -t rag --kb my-kb
deeptutor run visualize "Animate sine wave" --config render_mode=manim_video

# Interactive REPL
deeptutor chat
# (inside the REPL: /regenerate or /retry re-runs the last user message)

# Partners (IM-connected companions)
deeptutor partner list

# Knowledge bases, memory, server
deeptutor kb list
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor serve --port 8001       # API server only
deeptutor start                   # backend + frontend together
```

## Key Files

| Path                                       | Purpose                              |
| ------------------------------------------ | ------------------------------------ |
| `deeptutor/runtime/orchestrator.py`        | `ChatOrchestrator` — unified entry   |
| `deeptutor/runtime/launcher.py`            | Backend + frontend lifecycle / port discovery |
| `deeptutor/runtime/registry/`              | Tool + Capability registries         |
| `deeptutor/runtime/bootstrap/builtin_capabilities.py` | Built-in capability class paths |
| `deeptutor/services/config/runtime_settings.py` | JSON settings + process-env overrides |
| `deeptutor/core/stream.py`, `stream_bus.py` | StreamEvent protocol + async fan-out |
| `deeptutor/core/tool_protocol.py`          | `BaseTool` + `ToolDefinition`         |
| `deeptutor/core/capability_protocol.py`    | `BaseCapability` + `CapabilityManifest` |
| `deeptutor/core/context.py`                | `UnifiedContext` dataclass            |
| `deeptutor/tools/builtin/__init__.py`      | All built-in tool wrappers           |
| `deeptutor/capabilities/`                  | Built-in capability implementations  |
| `deeptutor/app.py`                         | `DeepTutorApp` — Python SDK facade    |
| `deeptutor_cli/main.py`                    | Typer CLI entry point                |
| `deeptutor/api/routers/unified_ws.py`      | Unified WebSocket endpoint           |

## Project Orchestrator — Skill de Orquestração

Habilitada automaticamente no início de cada sessão do opencode.
Carrega as instruções em `.opencode/skills/project-orchestrator/instructions.md`.

### Estrutura do Repositório Projetos/

```
Projetos/                        ← repositório único de project-spaces
├── perfis/
│   └── frota.yaml               ← perfil do usuário
├── {projeto-slug}/
│   ├── project-state.yaml       ← estado, objetivo, caminho
│   ├── fontes/                  ← vídeos, leituras, artigos, anotações
│   ├── arquitetura/             ← decisões arquiteturais
│   ├── tarefas/                 ← tasks do projeto
│   ├── rotinas/                 ← agendador de eventos
│   ├── frameworks/              ← frameworks usadas
│   ├── ferramentas/             ← ferramentas conectadas
│   ├── docs/                    ← NoteBlocks
│   ├── sessoes/                 ← sessões opencode
│   ├── conversas/               ← conversas Notion
│   └── relatorios/
│       ├── testes/
│       └── diarios/
├── scripts/kb/                  ← scripts compartilhados
├── .github/workflows/
│   └── sync-notion.yml
└── .opencode/skills/
    └── project-orchestrator/
```

### Fluxo de Branch

```
Início da sessão
  → init-environment.ps1 cria branch sessao/{slug}
  → LLM altera arquivos direto
  → watch-project-state.ps1 commita automaticamente

Final da sessão
  → end-session mergeia sessao/{slug} → main
  → GitHub Action sync → Notion
```

### Comandos da Skill

| Comando | Ação |
|---------|------|
| `@init-environment` | Verifica git, repo, Python, Notion API |
| `@start-session` | Cria branch de sessão + inicia watcher |
| `@end-session` | Merge + push + sync |
| `@sync-notion` | Sobe alterações locais → Notion |
| `@pull-notion` | Puxa alterações do Notion → local |
| `@generate-report` | Gera resumo diário do projeto |

### Múltiplas Branches ao Mesmo Tempo

A API dos project-states (`scripts/api/`) pode servir branches diferentes
simultaneamente usando `git worktree`:

```powershell
# Cria worktree da main e inicia APIs nas portas 8080 e 8081
.\scripts\kb\worktree-setup.ps1 -Branches "main" -StartAPIs

# STEM-TUTOR/           → branch atual → :8080
# STEM-TUTOR-main/      → main         → :8081
```

Cada worktree é uma pasta separada com seu próprio checkout Git,
compartilhando o mesmo repositório remoto. Útil para comparar
comportamento entre branches sem precisar fazer checkout.

---

## Dependency Layers

Public install paths and source extras are defined in `pyproject.toml`.
Requirements files mirror the same dependency groups for Docker/CI installs.

```
pip install deeptutor      — Full app (CLI + Web/API + packaged Web assets)
pip install deeptutor-cli  — CLI-only (LLM + RAG + providers + document parsing)
pip install -e .           — Source install for development

Source extras (.[ extra ], defined in pyproject.toml):
.[cli]            — CLI-only dependency set
.[server]         — Web/API server dependencies
.[partners]       — Partner channel SDKs + MCP client  (legacy alias: .[tutorbot])
.[matrix]         — Matrix channel for Partners (matrix-nio; needs libolm)
.[matrix-e2e]     — Matrix with end-to-end encryption (matrix-nio[e2e])
.[math-animator]  — Manim addon (powers `visualize` Manim renders + `deeptutor run math_animator`)
.[dev]            — Test / lint tooling
.[all]            — Everything above
```
