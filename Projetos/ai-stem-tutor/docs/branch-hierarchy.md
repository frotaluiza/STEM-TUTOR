# Hierarquia de Branches — Project State + Código

**Projeto:** Mar da Elétrica: AI STEM Tutor
**Data:** 2026-07-14
**Versão:** 1.0.0
**Autor:** Project Orchestrator — Perfil Frota

---

## 1. Conceito

Branches de código e branches de project state são acopladas em uma
hierarquia de três níveis, refletindo o ciclo de vida de uma sessão
de desenvolvimento.

```
STEM-TUTOR (project-space)           DEEPTUTOR (código)
═══════════════════════════           ═══════════════════════
main                                 main
  │                                    │
  └── sessao/{slug}                    │
       │                               │
       └── ps/{feature-name}           └── feature/{feature-name}
```

Cada nível herda o contexto do anterior. Uma branch `ps/` só existe
porque existe uma `sessao/` que a gerou.

---

## 2. Níveis

### Nível 1 — main

A branch estável. Todo merge converge para ela.

**Regras:**
- Nada é commitado diretamente
- Todo merge é automático (via watcher ou manual via PR)

### Nível 2 — sessao/{slug}

Criada automaticamente ao iniciar cada sessão do opencode.
Vive apenas durante a sessão.

**Contém:**
- Conversas da sessão
- Decisões tomadas
- Notas e anotações
- Alterações no project-state.yaml

**Regras:**
- Slug único por sessão (ex: `sessao/calm-canyon`)
- Commit automático via `watch-project-state.ps1`
- Mergeada para main ao final da sessão

### Nível 3 — ps/{feature-name}

Criada a partir da `sessao/{slug}` quando o usuário decide
implementar código. A branch de código correspondente é criada
no repositório do projeto (`feature/{feature-name}`).

**Contém:**
- Decisões específicas de implementação
- Artefatos de arquitetura da feature
- Nova entrada em `project-state.yaml` com `branch_codigo`

**Regras:**
- Nome descritivo da feature (ex: `ps/note-blocks-ui`)
- Vive até a feature ser finalizada (pode atravessar múltiplas sessões)
- Mergeada para `sessao/{slug}` quando a feature é concluída

---

## 3. Ciclo de Vida

```
───► INÍCIO DA SESSÃO
│
│   [opencode cria sessao/calm-canyon]
│
├──► USUÁRIO DECIDE IMPLEMENTAR
│   │
│   [cria ps/note-blocks-ui a partir de sessao/calm-canyon]
│   [cria feature/note-blocks-ui no repositório de código]
│
│   ┌─────────────────────────────────────────┐
│   │  Loop de desenvolvimento                │
│   │                                         │
│   │  feature/note-blocks-ui                 │
│   │    ├── commits de código                │
│   │    └── CI passa? ──► sim                │
│   │                                         │
│   │  ps/note-blocks-ui                      │
│   │    ├── decisões registradas             │
│   │    └── artefatos gerados                │
│   └─────────────────────────────────────────┘
│
├──► FEATURE PRONTA
│   │
│   [merge feature/note-blocks-ui → main (código)]
│   [merge ps/note-blocks-ui → sessao/calm-canyon]
│
├──► FIM DA SESSÃO
│   │
│   [merge sessao/calm-canyon → main]
│
▼
PRÓXIMA SESSÃO (começa de main)
```

---

## 4. Project State com Branch de Código

Quando uma branch `ps/` está ativa, o `project-state.yaml` reflete
o vínculo:

```yaml
projeto: "Mar da Elétrica: AI STEM Tutor"
slug: ai-stem-tutor
branch_atual: "ps/note-blocks-ui"
branch_codigo: "feature/note-blocks-ui"
repositorio_codigo: "frotaluiza/deeptutor"
ultima_sessao:
  slug: calm-canyon
  titulo: "Implementar NoteBlocks UI"
  data: 2026-07-14
  branch: "sessao/calm-canyon"
```

Se não há branch de código ativa:

```yaml
branch_atual: "sessao/calm-canyon"
branch_codigo: null
```

---

## 5. Comportamento do Watcher

| Evento | Ação do watcher |
|--------|----------------|
| Sessão inicia | Cria `sessao/{slug}` a partir de `main` |
| Usuário cria feature | Cria `ps/{feature}` a partir de `sessao/{slug}` |
| Commit em `ps/` | Atualiza `project-state.yaml` com `branch_codigo` |
| Merge de `ps/` → `sessao/` | Atualiza `project-state.yaml` (remove `branch_codigo`) |
| Merge de `sessao/` → `main` | Push + GitHub Action sync → Notion |

---

## 6. Visualização no PM

O Project Manager (DeepTutor) exibe:

```
Projeto: AI STEM Tutor
  Branch atual: ps/note-blocks-ui
  Branch código: feature/note-blocks-ui → frotaluiza/deeptutor
  Sessão pai: calm-canyon
  Status: código em desenvolvimento
```

Filtros disponíveis:
- Sessões principais (`origem: opencode`)
- Mini-sessões (`origem: noteblocks`)
- Todas

---

*Artefato gerado em 2026-07-14 pelo Project Orchestrator — Perfil Frota*
