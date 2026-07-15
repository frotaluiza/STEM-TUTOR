# Changelog — Project Orchestrator + Multi-branch API
**Data:** 2026-07-14 | **Branch:** main | **Sessão:** encerramento-sessao

## Alterações Realizadas

### Project Orchestrator (infraestrutura)
- Skill `.opencode/skills/project-orchestrator/` com instruções pro LLM
- `watch-project-state.ps1`: watcher de arquivos + branch automática
- `init-environment.ps1`: verificação de ambiente pré-sessão
- `worktree-setup.ps1`: script para gerenciar múltiplas branches via git worktree

### API REST dos Project-States
- `scripts/api/main.py` + routers (projects, sessions, readings, tasks, daily_reports)
- `utils.py`: funções compartilhadas (resolve_projetos_dir, current_branch)
- `scripts/kb/start-api.ps1` + `install-api-autostart.ps1`: auto-start via Task Scheduler

### Sync bidirecional com Notion
- `gh-sync-notion.py`: push GitHub → Notion com Projeto 1 (relation) + Origem
- `notion-pull.py`: pull Notion → GitHub com detecção de conflitos
- `reconcile.py`: backfill inicial entre Notion e local
- `.github/workflows/sync-notion.yml`: push (trigger: commit) + pull (schedule: 30min)

### Estrutura Projetos/
- `Projetos/perfis/frota.yaml`: perfil do usuário
- `Projetos/ai-stem-tutor/project-state.yaml`: estado, decisões, próximos passos
- `Projetos/ai-stem-tutor/arquitetura/project-orchestrator.md`: artefato de arquitetura
- `Projetos/ai-stem-tutor/arquitetura/branch-hierarchy.md`: hierarquia de branches
- `Projetos/ai-stem-tutor/docs/branch-hierarchy.md`: documentação do usuário
- Projetos: tcc, curso-bateria, pc-windows com project-state.yaml

### Frontend (DeepTutor)
- `web/app/(workspace)/projects/`: páginas de listagem + detalhe
- `web/lib/projects-api.ts`: cliente da API de projetos
- `web/components/BranchSelector.tsx`: seletor de branches no frontend
- `web/proxy.ts` + `web/lib/proxy-policy.ts`: proxy `/orchestrator/*` → API
- Filtro de mini-sessões (`?origem=`) no frontend

### Correções
- Scroll nas páginas de projeto (main `overflow-y-auto`)
- `session_count` corrigido (contagem real dos .md no diretório)
- Ruff lint errors (45 auto-fix + 5 manuais)
- `pandas>=2.0.0` adicionado ao requirements
- UTF-8 BOM removido do `update-project-state.py`
- Bug no `_list_markdown_files` que causava 500 no detail endpoint

## Decisões
1. Centralizar todos os project-spaces no repositório STEM-TUTOR
2. API REST como ponte entre frontend e dados locais
3. Git worktree para múltiplas branches simultâneas
4. Sessões do NoteBlocks marcadas como `origem: noteblocks` (filtrável)
5. Branch hierarchy: sessao/{slug} → ps/{feature} (project-space) + feature/{feature}(código)
6. Watcher local + GitHub Action para sync bidirecional com Notion

## Arquivos Modificados
- `.opencode/skills/project-orchestrator/` (criação)
- `scripts/kb/*.ps1` (criação)
- `scripts/kb/gh-sync-notion.py` (modificação)
- `scripts/kb/notion-pull.py` (criação)
- `scripts/kb/reconcile.py` (criação)
- `scripts/api/` (criação)
- `.github/workflows/sync-notion.yml` (criação/modificação)
- `Projetos/` (criação)
- `web/app/(workspace)/projects/` (criação)
- `web/lib/projects-api.ts` (criação)
- `web/components/BranchSelector.tsx` (criação)
- `web/proxy.ts` (modificação)
- `web/lib/proxy-policy.ts` (modificação)
- `web/components/sidebar/SidebarShell.tsx` (modificação)
- `web/app/(workspace)/layout.tsx` (modificação)
- `AGENTS.md` (modificação)
- `.config/opencode/AGENTS.md` (modificação)
- `requirements/server.txt` (modificação)
