# Project State: AI STEM Tutor

## Versão
- **Branch:** feature/mind-map-module
- **Último commit:** 364c073b docs: estrutura de documentacao do AI STEM Tutor + README + diretorios arquitetura/anotacoes-artigos
- **Última atualização:** 2026-07-13 00:33:41 UTC

## Git Log (últimos 15 commits)
- 364c073b docs: estrutura de documentacao do AI STEM Tutor + README + diretorios arquitetura/anotacoes-artigos
- 384b6a70 feat: Project Mind Map visualization + project-state auto-sync
- d8e5dda3 feat: project-state tracking for cross-session context pipeline
- d36e8244 feat: mind map module + pedagogical guidelines + platform messages
- 3e3b9a6e release: v1.5.1
- df6922bb release: v1.5.0
- 3d5b669c minor fix
- bca6f6e9 release: v1.4.15
- 4fab4489 minor fix & new channel
- 0bbd4668 Merge pull request #604 from spring618/codex/fix-mastery-choice-persistence
- 85756d01 Merge pull request #602 from VectorPeak/codex/fix-chunk-overlap-zero
- 943e9fb7 fix mastery choice persistence and grading
- 8ba7dd2f fix: preserve zero LlamaIndex chunk overlap
- 8f39545d release: v1.4.14
- 3b823ae5 minor fixes

## Sessões (239)

- 2026-07-13: **Find nav items and page patterns (@explore subagent)** (cosmic-island) agent=explore cost=$0.0053
  - Very quick research. I need to find exactly these things in the DeepTutor frontend at C:\Users\frota\Documents\Projetos\AI TUTOR\web:

1. In SidebarShell.tsx - find where PRIMARY_NAV or SECONDARY_NAV 

- 2026-07-12: **Integração OpenCode STEM TUTOR** (witty-wizard) agent=build cost=$0.2431
  - Projeto: STEM TUTOR, entrada para pensar em um monitor de atividades do opencode associado aos projetos que estão no STEM TUTOR. Os dois sistemas estão unidos pela mesma kb global (project space), que
  - 🔧 **Contexto**: ... | **Escolha**: ... | **Stack**: ...
  - 📄 path/to/file.py (criado/modificado)

- 2026-07-12: **Explore opencode note setup (@explore subagent)** (calm-island) agent=explore
  - I need to understand the user's opencode setup for notes and sessions. Search for:

1. List files in C:\Users\frota\.local\share\opencode\docs\ - show the live doc files
2. List files in C:\Users\frot

- 2026-07-12: **Explore mind-map-module changes (@explore subagent)** (quick-panda) agent=explore
  - Explore the DeepTutor codebase at C:\Users\frota\Documents\Projetos\AI TUTOR\. The current branch is `feature/mind-map-module`.

1. Run `git log --oneline -5` to see recent commits
2. Run `git diff ma

- 2026-07-12: **Verify Ansari2022 and read new paper (@general subagent)** (crisp-mountain) agent=general
  - I need two things done in parallel:

**TASK 1: Verify Ansari2022 paper**
The paper "Downstream variations of air-gap membrane distillation and comparative study with direct contact membrane distillati

- 2026-07-12: **Explore Deeptutor project (@explore subagent)** (shiny-eagle) agent=explore
  - Search the filesystem broadly for anything related to "deeptutor" or "Deeptutor". Look for:
1. Any project directories/files named deeptutor anywhere under C:\Users\frota or other common locations
2. 

- 2026-07-12: **Run @session to push live doc (@session subagent)** (glowing-wolf) agent=session
  - Run @session to register this session in Notion. The live doc exists at C:\Users\frota\.local\share\opencode\docs\playful-mountain.md - read it and push it.

Session details:
- Slug: playful-mountain


- 2026-07-12: **Explore HKU codebase structure (@explore subagent)** (sunny-cactus) agent=explore
  - I need to understand the HKU DeepTutor codebase structure at `C:\Users\frota\Documents\Projetos\AI TUTOR\` on branch `feature/mind-map-module`.

Please explore deeply and return:

1. **High-level dire

- 2026-07-12: **Explore DeepTutor test setup (@explore subagent)** (lucky-mountain) agent=explore cost=$0.0072
  - I need to understand the DeepTutor project's testing and code quality setup in detail. Look at:

1. Read `C:\Users\frota\Documents\Projetos\AI TUTOR\pyproject.toml` — find all tool configurations (pyt

- 2026-07-12: **Explore DeepTutor frontend nav (@explore subagent)** (playful-rocket) agent=explore cost=$0.0096
  - Explore the DeepTutor frontend navigation structure at C:\Users\frota\Documents\Projetos\AI TUTOR\web\

I need to understand:
1. Read web/app/layout.tsx — the root layout with navigation/sidebar
2. Re

- 2026-07-12: **Registrar sessão no Notion (@session subagent)** (shiny-cabin) agent=session cost=$0.0243
  - Run the @session agent to register the current opencode session in Notion.

Session details:
- Session slug: calm-canyon
- Session ID: ses_0ae492764ffeAOuJOGtvkX1soy
- Session title: "Automação + Mind

- 2026-07-12: **Rodar @session para esta sessão (@session subagent)** (jolly-engine) agent=session cost=$0.0099
  - Execute o agente @session para registrar a sessão atual do opencode no Notion.

Siga estritamente o fluxo definido no AGENTS.md:

1. Consulte o SQLite:
   - `SELECT id, slug, title FROM session ORDER 

- 2026-07-12: **@session para playful-forest (@session subagent)** (swift-tiger) agent=session cost=$0.0137
  - Execute o agente @session para registrar a sessão `playful-forest` no Notion.

USE ESTES VALORES DIRETAMENTE (já obtidos do SQLite):
- Session ID: `ses_0ab94f654ffe4wk5aQvLyxV8Id`
- Slug: `playful-for

- 2026-07-12: **@session final para esta sessão (@session subagent)** (lucky-engine) agent=session cost=$0.0177
  - Execute o agente @session para registrar a sessão atual do opencode no Notion.

USE ESTES VALORES DIRETAMENTE:
- Session ID: `ses_0ab94f654ffe4wk5aQvLyxV8Id`
- Slug: `playful-forest`
- Live Doc Path: 
  - 🔧 **Contexto**: Criar editor de blocos estilo Notion dentro do DeepTutor para anotações conectadas com agente
  - 🔧 **Escolha**: Implementar como nova surface no menu lateral (`/noteblocks`), sem substituir o chat existente
  - 🔧 **Stack**: Slate.js (editor), xterm.js (terminal), FastAPI + WebSocket (backend), .md + frontmatter (storage)

- 2026-07-12: **TCC project state check (@explore subagent)** (misty-rocket) agent=explore cost=$0.0116
  - Check the TCC project state files. Read these files and return their full contents:
1. C:\Users\frota\.local\share\opencode\project-state\tcc.md (if exists)
2. C:\Users\frota\.local\share\opencode\pro

- 2026-07-12: **Research Sci-Hub MCP (@explore subagent)** (neon-moon) agent=explore cost=$0.0131
  - I need to research how to set up a Sci-Hub MCP (Model Context Protocol) server for use with OpenCode. Search the web and return:

1. What Sci-Hub MCP servers exist for OpenCode/Claude/Cline/etc
2. How

- 2026-07-12: **Nova entrada no STEM TUTOR** (quiet-pixel) agent=build cost=$0.1026
  - Nova entrada no projeto STEM TUTOR

- 2026-07-12: **Rodar front e back do Deep Tutor** (glowing-mountain) agent=build cost=$0.0069
  - roda o front e back do deep tutor na branch mais atual

- 2026-07-12: **Explore DeepTutor test structure (@explore subagent)** (hidden-garden) agent=explore
  - Very thorough exploration of the DeepTutor project's test structure. I need to understand:

1. What test frameworks are used (pytest, node test, playwright, etc.)
2. Where test files are located (all 

- 2026-07-12: **Criar database Test Reports no Notion (@general subagent)** (glowing-garden) agent=general cost=$0.0350
  - You need to create a new Notion database called "Relatórios de Testes (2026)" for documenting test reports.

Use the available Notion tools to:
1. Create a new database in the Notion workspace under t

- 2026-07-12: **Find TCC repo and bib files (@explore subagent)** (lucky-panda) agent=explore cost=$0.0185
  - I need to find the TCC (Trabalho de Conclusão de Curso) repository on the local filesystem. The TCC is about hybrid physical-data modeling for V-AGMD membrane distillation.

Search for:
1. Any .bib or

- 2026-07-12: **Criar database Relatórios de Testes 2026** (quick-canyon) agent=plan cost=$0.0085
  - "First, find the parent page of 'Tarefas da Semana' database (ID: 1d7bec7f-09b7-459b-89cc-01de4b71ec9d) using NOTION_QUERY_DATABASE or NOTION_FETCH_DATABASE. Then create a new Notion database called '

- 2026-07-12: **Criar database Test Reports Notion (@general subagent)** (cosmic-eagle) agent=general cost=$0.0195
  - Create a new Notion database called "Relatórios de Testes (2026)" in the workspace "Espaço de Luiza Costa".

The Composio Notion connection should already be active (it was used earlier in this same s

- 2026-07-12: **Notion Projetos 2026 page ID lookup** (shiny-tiger) agent=plan cost=$0.0074
  - "Query the Notion Projetos 2026 database (id: 9172be34-0056-4f38-aa2a-093339bb5790) and find the page for 'Mar da Elétrica — AI STEM Tutor'. Return only the page ID."

- 2026-07-12: **Documentar teste no Notion (@general subagent)** (eager-cabin) agent=general cost=$0.0294
  - Create an entry in the Notion database "Relatórios de Testes (2026)" (ID: 39b191ce-57f9-817f-95d0-e757b3bb821d) with the following test report:

- Nome do Teste: "Unified MindMap - TypeScript compilat

- 2026-07-12: **Documentar testes no Notion (@general subagent)** (calm-pixel) agent=general cost=$0.0282
  - Create TWO entries in the Notion database "Relatórios de Testes (2026)" (ID: 39b191ce-57f9-817f-95d0-e757b3bb821d).

The Composio Notion connection should already be active (was used earlier in this s

- 2026-07-12: **Register session in Notion (@session subagent)** (calm-nebula) agent=session cost=$0.0135
  - Register the current opencode session in Notion using the @session workflow:

1. Query SQLite for the current session: SELECT id, slug, title FROM session ORDER BY time_updated DESC LIMIT 1
2. Read th

- 2026-07-12: **New session - 2026-07-12T00:04:56.367Z** (curious-forest) agent=build cost=$0.0625
  - projeto: STEM TUTOR. Entrada

- 2026-07-12: **Find Zotero and TCC PDFs (@explore subagent)** (glowing-squid) agent=explore cost=$0.0120
  - I need to find the user's Zotero library and any existing PDF copies of academic papers in their filesystem. Search for:

1. Zotero installation and data directory - check:
   - C:\Users\frota\Zotero\

- 2026-07-12: **Generate detailed live docs (@general subagent)** (jolly-otter) agent=general cost=$0.0333
  - I need to generate detailed live docs for ~25 opencode sessions from the last 3 days and upload them to Notion. The session data is in a SQLite database at C:\Users\frota\.local\share\opencode\opencod

## Decisões Acumuladas
- **Iniciar robô watcher do live doc:**
- **Contexto:** O áudio da reunião estava em formato .aup3 (projeto Audacity).
- **Problema:** Out of memory ao processar áudio completo (2h50). Solução: split em chunks de 30 min.
- **Stack**: Slate.js (editor), xterm.js (terminal), FastAPI + WebSocket (backend), .md + frontmatter (storage)
- **Ferramenta:** `faster-whisper` com modelo `small` (244M parâmetros) para primeiro chunk, `base` para chunks restantes.
- **Alternativas:** Extrair samples do banco SQLite do aup3 vs usar .m4a exportado automaticamente.
- **Resultado:** Transcrição completa salva em `transcricao_reuniao_08-06-2026.txt` (85.9 KB, 1096 linhas).
- **Escolha:** Usar `Gravando (4).m4a` (260 MB, mesmo conteúdo) por ser formato padrão suportado pelo ffmpeg.
- **Sync**: Notion API via notion-client Python
- **Contexto**: Criar editor de blocos estilo Notion dentro do DeepTutor para anotações conectadas com agente
- **Contexto:** Sem API OpenAI disponível, optou-se por transcrição local.
- **Escolha**: Implementar como nova surface no menu lateral (`/noteblocks`), sem substituir o chat existente
- **Contexto**: ... | **Escolha**: ... | **Stack**: ...

## Issues Conhecidas
Nenhuma registrada

## Próximos Passos (Top 10)
- [ ] Criar `project-space/` com diretórios `kb/fontes/`, `kb/videos/`, `kb/sessoes/`, `project-state/`
- [ ] TODOs extraídos (19)
- [ ] Todos os 8 tipos de `part` (text, reasoning, tool, file, step, compaction, agent)
- [ ] Todos os 42 diretórios em `C:\Users\frota\OneDrive\Documentos\Obsidian Vault\2026\` contêm `index.md`
- [ ] Adicionar parâmetro `dataset_stem` para gerar os paths dinamicamente
- [ ] Todos os híbridos estão abaixo de 0.11
- [ ] Adicionar explicação sobre tentativa de replicar MLP_sklearn e por que não foi viável
- [ ] Adicionar discussão sobre tentativa de replicar MLP_sklearn.
- [ ] Fazer Stage 2 rodar corretamente com resultados plausíveis: baseline com R² Flux ≥ 0.92 **e** modelos híbridos melhorando a baseline (como ocorria em execuções anteriores).
- [ ] Todos os pontos têm o mesmo tamanho de barra ou varia por ponto?

---
*Auto-gerado por update-project-state.py em 2026-07-12 21:33*
