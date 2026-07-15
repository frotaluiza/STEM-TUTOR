# Changelog — Encerramento de Sessão: Plano de Merge + Features
**Data:** 2026-07-14 | **Branch:** main | **Sessão:** jolly-knight

## Plano de Merge (Ordem)

1. **Mergear** `feature/source-providers-system` → `main`
2. **Mergear** `ps/mindmap-v2` → `main`
3. **Mergear** `feature/session-from-module` → `main`
4. **Criar branch** `monorepo-migration`
5. Migrar estrutura (`Projetos/` vira git root)
6. Testar exaustivamente
7. Mergear de volta pra `main`

## Features Implementadas

### PM Dashboard
- Branch selector com branches locais + remotas (☁️)
- Sync status (Synced/Ahead/Behind/Uncommitted)
- Tarefas (CRUD completo com add/toggle/delete)
- Análise de conflitos entre branches (merge-tree)
- Painel de conflitos com selects + resultados

### SessionViewer
- 3 abas: Chat + Live Doc + Terminal
- Filtro automático de processamento interno
- Live Doc gerado do opencode DB
- Botão Fork (opencode --fork)

### NoteBlocks
- Multi-modal com abas Nota + Live Doc + Terminal
- MarkdownBlock estilo Notion (preview-first, click-to-edit)
- Drag-and-drop para reordenar blocos

### Infra
- Auto-push hook (post-commit → personal remote)
- WScript start-dev.js para frontend persistente
- Artefatos no formato novo `{tipo}--{data}--{slug}--{descricao}.{ext}`
- _run_git_binary() para merge-tree com encoding robusto
- _resolve_ref() para branches remotas

## Arquivos Modificados
- `deeptutor/api/routers/pm_dashboard.py` (+conflicts, branches remotas, _resolve_ref, _run_git_binary)
- `web/components/pm/PMConflicts.tsx` (novo)
- `web/components/pm/PMBranchSelector.tsx` (+remote prop)
- `web/components/pm/PMReportSection.tsx` (fix todos object)
- `web/components/pm/types.ts` (fix todos type)
- `web/start-dev.js` (novo)
- `web/start-dev.bat` (novo)
- `web/start-dev.vbs` (novo)
