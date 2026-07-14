# Changelog — PM Dashboard v2 + NoteBlocks Multi-modal + Mind Map Project Space
**Data:** 2026-07-14 | **Branch:** feature/pm-dashboard-v2 → main, fix/projects-session-count → main, feature/project-space-mindmap | **Sessão:** jolly-knight

## Alterações Realizadas

### PM Dashboard v2
- Criado `deeptutor/api/routers/pm_dashboard.py` — 10+ endpoints (projects, sessions, stats, export, fork, live-doc, space)
- Criado `web/components/pm/PMDashboardV2.tsx` — Dashboard principal com tabelas sort/filter
- Criado `web/components/pm/PMTable.tsx` — Tabela estilo Notion (sort, filter, linhas clicáveis)
- Criado `web/components/pm/PMProjectSelector.tsx` — Dropdown de projetos
- Criado `web/components/pm/PMReportSection.tsx` — Relatório do projeto
- Criado `web/components/pm/SessionViewer.tsx` — Visualizador de sessão estilo chat com toggles
- Criado `web/components/pm/usePMData.ts` — Hook de dados
- Adicionado URL persistence (`/pm?project=slug`)
- Auto-select do projeto mais recente (por `last_date`)

### SessionViewer
- 3 abas: Chat + Live Doc + Terminal
- Filtro automático de processamento interno (214/654 msgs ocultas)
- Live Doc gerado do opencode DB (encoding corrigido)
- Botão Fork (`opencode --fork` em nova janela)

### NoteBlocks Multi-modal
- Abas: Nota + Live Doc + Terminal
- MarkdownBlock estilo Notion (preview-first, click-to-edit)
- Drag-and-drop nativo HTML5 para reordenar blocos
- Live Doc tab com MarkdownRenderer + botão Importar
- LevelingModal só para Mastery Path, bg-black opaco

### Mind Map como Project Space
- Endpoint `GET /api/v1/pm/space/{slug}` — 51 nodes multi-fonte
- Suporte a nodes: project, branch, session, decision, kb, note, module
- Dagre layout horizontal (LR)
- Seletor de projeto integrado

### Projects Page
- Criada `web/app/(workspace)/projects/` — listagem + detalhe
- Integração com Orchestrator API (:8080)
- Session count da classification.json

### Infra
- Proxy configurado para `/orchestrator/` → :8080
- Git hook `post-checkout` — PS por branch
- Sidebar: Projects + Project Manager

### Dados Restaurados
- `kb/sessoes/classification.json` (239 sessions, 9 projetos)
- `kb/projetos/*/index.md` (índices)
- `project-state/ai-stem-tutor.json`

## Decisões

1. PM Dashboard como página dedicada no DeepTutor (`/pm`) com persistência de URL
2. SessionViewer com abas Chat + Live Doc + Terminal + Fork
3. Filtro de processamento interno baseado em flag `is_internal`
4. MarkdownBlock com toggle preview-first estilo Notion
5. Live Doc gerado do opencode DB (evitando corrupção de encoding)
6. Fork de sessões via `opencode --fork` em nova janela
7. LevelingModal desativado por padrão, só para Mastery Path
8. Project auto-select pelo mais recente + URL query param

## Arquivos Modificados

### Novos
- `deeptutor/api/routers/pm_dashboard.py` (887 linhas)
- `deeptutor/api/routers/project_state.py`
- `deeptutor/api/routers/mindmap.py`
- `deeptutor/noteblocks/*` (17 arquivos — models, storage, router, ws, agent, runner, terminal)
- `web/components/pm/*` (7 arquivos)
- `web/components/mindmap/*` (6 arquivos)
- `web/features/noteblocks/*` (8 arquivos)
- `web/app/(workspace)/pm/page.tsx`
- `web/app/(workspace)/session-viewer/[slug]/page.tsx`
- `web/app/(workspace)/noteblocks/page.tsx`
- `web/app/(workspace)/projects/*`
- `scripts/api/*` (orchestrator API)
- `.git/hooks/post-checkout`

### Modificados
- `deeptutor/api/main.py` — router registrations
- `deeptutor/noteblocks/models.py` — BlockType MARKDOWN
- `deeptutor/noteblocks/storage.py` — markdown block round-trip
- `web/features/noteblocks/types.ts` — BlockType markdown
- `web/features/noteblocks/index.ts` — export TerminalPane
- `web/components/ThemeScript.tsx` — suppressHydrationWarning
- `web/components/sidebar/SidebarShell.tsx` — Projects + PM nav
- `web/proxy.ts` — orchestrator rewrite
- `web/lib/projects-api.ts` — ProjectSummary tipo
- `AGENTS.md` — ciclo de artefatos

## Sessões Relacionadas
- `calm-canyon` — Mind Maps + DebugAgent
- `shiny-wolf` — MCP Sci-Hub + Mermaid
- `playful-forest` — NoteBlocks
