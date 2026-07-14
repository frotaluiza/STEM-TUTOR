# Project State: AI STEM Tutor

## Identidade
- **Projeto:** AI STEM Tutor
- **Slug:** ai-stem-tutor
- **Repo:** `C:\Users\frota\Documents\STEM-TUTOR\`

## Branch Atual
- **Project State Branch:** `ps/mindmap-v2` (branch ativa desta sessão)
- **Repo Branch:** `ps/mindmap-v2` (a branch do repo associada a esta sessão)
- **Branch do projeto criada nesta sessão:** `feature/source-providers-system` (a ser criada)

## Branching Strategy (definida nesta sessão)

```
Sessão opencode (lucky-wizard)
  └── Project State Branch (ps/mindmap-v2)
       └── Repo Branch (feature/source-providers-system)
```

**Regras:**
1. Cada sessão opencode equivale a uma branch do project state.
2. Dentro da sessão, pode-se criar uma branch do repositório do projeto.
3. A branch do repositório fica ASSOCIADA à branch do project state.
4. Decisões e alterações do project state vão para a branch onde a sessão ativou.
5. Ao final da sessão, project state mergeia para main.
6. A branch do repositório pode seguir em paralelo.

## Sessão Atual
- **slug:** lucky-wizard
- **title:** "Zona da Elétrica e fontes de engenharia elétrica"
- **data:** 2026-07-14
- **Live doc:** `C:\Users\frota\.local\share\opencode\docs\lucky-wizard.md`

## Decisões da Sessão Atual
1. **Source Providers System**: Criar módulo `deeptutor/services/sources/` com provedores de fonte personalizáveis por projeto, database SQLite, sugestões por área, e bridge para Search Providers existentes.
2. **Mar da Elétrica**: Projeto no sistema de fontes com fontes da área "eletrica". Mastery paths = implementação futura.
3. **Branching Strategy**: Sessão → branch do project state → branch do repo (documentado acima).

## Últimos Commits (repo STEM TUTOR)
- `3d0ee1b8` chore: iniciar branch ps/mindmap-v2 para melhorias no mindmap
- `ce4028be` Merge branch 'main' of https://github.com/frotaluiza/STEM-TUTOR
- `220ad923` feat: tarefas (tasks) system — backend API + PM panel + AGENTS.md guideline

## Sessões (últimas)
- 2026-07-14: **lucky-wizard** — "Zona da Elétrica e fontes de engenharia elétrica" (ATUAL)
- 2026-07-14: **jolly-knight** — "PM Dashboard v2 + NoteBlocks multi-modal"
- 2026-07-14: **gentle-nebula** — "Verificar sync GitHub Notion do STEM TUTOR"

## Próximos Passos (Top 5)
- [ ] Merge do project state (ps/mindmap-v2) → main
- [ ] Criar branch `feature/source-providers-system` no STEM TUTOR
- [ ] Implementar database layer: models.py + db.py (SQLite)
- [ ] Implementar manager.py + suggestions.py + api.py
- [ ] Implementar primeiro provider funcional (open_library.py)

---
*Atualizado em 2026-07-14 — Sessão lucky-wizard (Source Providers System)*
