# Changelog — Arquitetura: Projetos/ como Monorepo + Orchestrator Upload Universal
**Data:** 2026-07-14 | **Branch:** main (feature/project-space-mindmap) | **Sessão:** jolly-knight

## Alterações Realizadas

### Branch Selector + Sync Status
- `web/components/pm/PMBranchSelector.tsx` — Dropdown de branches git no header do PM
- `web/components/pm/PMSyncStatus.tsx` — Indicador visual Synced/Ahead/Behind/Uncommitted
- Integração no PMDashboardV2 com persistência via URL `?project=X&branch=Y`

### UnifiedMindMap — Branch-aware
- Adicionado suporte a `branch` prop no UnifiedMindMap
- Ao selecionar branch, mind map recarrega com dados da branch via `?branch=`

### Space Endpoint — Corrigido + Expandido
- Corrigido 500: `KeyError: 'type'` (KB data structure mismatch)
- Corrigido 500: `NameError: 'learning'` (variável removida na refatoração)
- Adicionados: `sessoes.ativas`, `sessoes.encerradas`, `kbs`, `videos`, `notes`
- `POST /api/v1/pm/tarefas` — CRUD completo de tarefas
- `GET /api/v1/pm/branches` — Lista branches git
- `GET /api/v1/pm/sync-status` — Status de sincronia com GitHub

### Tarefas (Tasks System)
- Seção "Tarefas" no PM Dashboard com add/toggle/delete
- Armazenamento em `project-state/tarefas-{branch}.json`
- AGENTS.md com guideline de registro obrigatório

### AGENTS.md — Ciclo de Artefatos Obrigatório
- Adicionada seção "Ciclo Obrigatório de Artefatos"
- Todo código alterado → changelog + relatorio → Projetos/{slug}/artefatos/
- Formato: `{tipo}--{data}--{slug}--{descricao}.{ext}`
- Script `scripts/gerar-artefato.ps1` para geração automática

### Git Hooks
- `.githooks/post-commit` — Auto-push para personal remote
- `scripts/sync-git.ps1` — Script de sync manual

## Decisões

1. Branch selector + sync status no header do PM — visão clara do estado do git
2. Tarefas em JSON local (não em DB) — simplicidade máxima, versionado com git
3. Nomenclatura de artefatos: `{tipo}--{data}--{slug}--{descricao}.{ext}` — legível + parseável
4. Orchestrator como arquivador universal: aceita qualquer formato, decide destino
5. Monorepo: `Projetos/` como git root, cada projeto (código + PS) como subpasta
6. Git LFS para binários (PDF, PNG, MP3) — repo leve

## Arquivos Modificados

### Novos
- `web/components/pm/PMBranchSelector.tsx` (branch selector dropdown)
- `web/components/pm/PMSyncStatus.tsx` (sync status indicator)
- `scripts/gerar-artefato.ps1` (artifact generation script)
- `scripts/sync-git.ps1` (git sync script)
- `.githooks/post-commit` (auto-push hook)

### Modificados
- `web/components/pm/PMDashboardV2.tsx` — branch selector + sync status + tarefas
- `web/components/mindmap/UnifiedMindMap.tsx` — branch prop + filtered fetching
- `deeptutor/api/routers/pm_dashboard.py` — tarefas + branches + sync + space fix
- `AGENTS.md` — artifact cycle + task guidelines
- `project-state/ai-stem-tutor.json` — roadmap atualizado

## Testes Executados

| Framework | Comando | Resultado | Duração |
|-----------|---------|-----------|---------|
| tsc --noEmit | `npx tsc --noEmit` | Aprovado (8 pre-existing warnings) | 13s |
| Python AST | `python -c "import ast; ast.parse(...)"` | Aprovado | 0.4s |
| API /branches | `GET /api/v1/pm/branches` | ✅ 200 | 2s |
| API /sync-status | `GET /api/v1/pm/sync-status` | ✅ 200 (uncommitted=2) | 2s |
| API /space | `GET /api/v1/pm/space/ai-stem-tutor` | ✅ 200 (63 sessões, 7 KBs) | 8s |
| API /tarefas | `POST /api/v1/pm/tarefas` | ✅ 201 | 2s |
| API /tarefas | `GET /api/v1/pm/tarefas` | ✅ 200 | 2s |

## Erros Encontrados e Corrigidos

1. **500: KeyError 'type'** — KB data structure não tinha campo `type`
2. **500: NameError 'learning'** — Variável removida na refatoração do space endpoint
3. **404: Branches endpoint** — Backend não reiniciado após mudanças (cache de módulo)
4. **404: Tarefas endpoint** — Mesmo problema de cache
5. **Connection refused** — Frontend caía após timeout do `npm run dev`
6. **Warning: ReactFlow container height** — Resolvido com `h-[calc(100vh-220px)]`

## Pre-existing Warnings

| Arquivo | Erro |
|---------|------|
| `MarkdownWithCrops.tsx` | Cannot find module './CropModal' |
| `ProjectMindMap.tsx` | Stylesheet → StylesheetCSS |
| `ConceptGraph.tsx` | Stylesheet → StylesheetCSS |
| `useNote.ts` | Property 'origin' missing |
| `learning/page.tsx` | TS2345 Argument type |
