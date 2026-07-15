# Changelog — Source Providers System + Branching Strategy
**Data:** 2026-07-14 | **Branch:** ps/mindmap-v2 | **Sessão:** lucky-wizard

## Alterações Realizadas (Artefatos)
- Definição da arquitetura do Source Providers System (módulo `deeptutor/services/sources/`)
- Definição da Branching Strategy: sessão → branch do project state → branch do repo
- Provedores de fonte personalizáveis por projeto com database SQLite
- Sugestões automáticas de fontes por área do projeto
- Integração bridge com Search Providers existentes do DeepTutor
- Mar da Elétrica como projeto com fontes sugeridas da área "eletrica"

## Decisões
1. **Branching Strategy**: Sessão ≡ branch do project state. Dentro dela, pode haver branch do repo. Project state registra associação.
2. **Source Providers System**: Módulo novo dentro do DeepTutor, não API separada.
3. **Mar da Elétrica**: Projeto no sistema de fontes. Mastery paths = futuro.

## Arquivos Modificados (Fase 1 — Código)
- `deeptutor/services/sources/__init__.py` (criação)
- `deeptutor/services/sources/models.py` (criação)
- `deeptutor/services/sources/db.py` (criação)
- `deeptutor/services/sources/registry.py` (criação)
- `deeptutor/services/sources/manager.py` (criação)
- `deeptutor/services/sources/suggestions.py` (criação)
- `deeptutor/services/sources/api.py` (criação)
- `deeptutor/services/sources/providers/__init__.py` (criação)
- `deeptutor/services/sources/providers/base.py` (criação)
- `deeptutor/services/sources/providers/open_library.py` (criação)
- `tests/sources/__init__.py` (criação)
- `tests/sources/test_db.py` (criação)
- `tests/sources/test_manager.py` (criação)
- `tests/sources/test_suggestions.py` (criação)
- `scripts/run_sources_api.py` (criação)

## Tarefas Pendentes (Futuras)
### Fase 2 — Integração Backend + Providers
- [ ] Registrar router no `deeptutor/api/main.py`
- [ ] Provider: Zona da Elétrica (scraper)
- [ ] Provider: Newton Braga (scraper)
- [ ] Provider: Perplexity DeepSearch (API key)
- [ ] Provider: Google Books (API key)

### Fase 3 — Tool de Chat
- [ ] Criar tool `source_search` em `deeptutor/tools/source_search.py`
- [ ] Registrar no `deeptutor/tools/builtin/__init__.py`
- [ ] Renderizar tool call no `TracePanels.tsx`

### Fase 4 — Frontend (Sources Manager)
- [ ] Adicionar `/sources` na `SECONDARY_NAV` do `SidebarShell.tsx`
- [ ] Criar página `web/app/(workspace)/sources/page.tsx`
- [ ] Criar API client `web/lib/sources-api.ts`
- [ ] Criar página de configuração em `/settings/sources`

### Fase 5 — OpenCode Integration
- [ ] Documentar API endpoints para acesso pelo opencode
- [ ] Criar tool customizado no opencode.jsonc apontando pra API do DeepTutor
