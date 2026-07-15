# Project State: AI STEM Tutor

## Identidade
- **Projeto:** AI STEM Tutor
- **Slug:** ai-stem-tutor
- **Repo:** `C:\Users\frota\Documents\STEM-TUTOR\`

## Branch Atual
- **Sessão:** lucky-wizard
- **Project State Branch:** `feature/source-providers-system`
- **Repo Branch:** `feature/source-providers-system`
- **Status:** Fase 1 concluída, aguardando merge → main

## Branching Strategy
```
Sessão (lucky-wizard)
  └── Project State Branch (feature/source-providers-system)
       └── Repo Branch (feature/source-providers-system)
```

## Sessão Atual
- **slug:** lucky-wizard
- **title:** "Source Providers System — Fase 1"
- **data:** 2026-07-14
- **Live doc:** `C:\Users\frota\.local\share\opencode\docs\lucky-wizard.md`

## Decisões da Sessão
1. **Source Providers System**: Criado módulo `deeptutor/services/sources/` com database SQLite, registry decorator, manager orquestrador, sugestões por área, API REST, e provider Open Library funcional.
2. **Mar da Elétrica**: Projeto no sistema de fontes com fontes da área "elétrica". Mastery paths = implementação futura.
3. **Branching Strategy documentada**: Sessão → branch do project state → branch do repo.
4. **Frontend planejado**: Sources Manager (`/sources`) + tool `source_search` + integração settings.

## Artefatos Gerados
- `Projetos/ai-stem-tutor/artefatos/2026-07-14--lucky-wizard--changelog.md`
- `Projetos/ai-stem-tutor/artefatos/2026-07-14--lucky-wizard--relatorio.md`

## Testes
- **15/15** testes unitários passando (db, manager, suggestions)
- **7/7** endpoints manuais da API testados com sucesso

## Tarefas Pendentes
### Fase 2 — Integração Backend + Providers
- [ ] Registrar router no `deeptutor/api/main.py`
- [ ] Provider: Zona da Elétrica (scraper)
- [ ] Provider: Newton Braga (scraper)
- [ ] Provider: Perplexity DeepSearch (API key)
- [ ] Provider: Google Books (API key)

### Fase 3 — Tool de Chat
- [ ] Criar tool `source_search` em `deeptutor/tools/source_search.py`

### Fase 4 — Frontend (Sources Manager)
- [ ] Adicionar `/sources` na `SECONDARY_NAV` da sidebar
- [ ] Criar página `web/app/(workspace)/sources/page.tsx`

### Fase 5 — OpenCode Integration
- [ ] Documentar API para acesso pelo opencode

## Roadmap
### Concluído
- [x] Módulo `deeptutor/services/sources/` (models, db, registry, manager, suggestions, api)
- [x] Provider Open Library funcional
- [x] 7 provedores seed no SQLite
- [x] 15 testes passando
- [x] API standalone rodando
- [x] Branching Strategy documentada
- [x] Planejamento frontend + chat + opencode

### Pendente
- [ ] Integração router no DeepTutor
- [ ] Scrapers (Zona, Newton, etc.)
- [ ] Provider DeepSearch + Google Books
- [ ] Tool `source_search` no chat
- [ ] Frontend Sources Manager
- [ ] Integração OpenCode

---
*Atualizado em 2026-07-14 — Sessão lucky-wizard (Source Providers System)*
