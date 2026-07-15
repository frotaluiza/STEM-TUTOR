---
titulo: "Visualização de Worktree no PM"
slug: visualizar-worktree
projeto: ai-stem-tutor
prioridade: media
status: "A fazer"
criado_em: 2026-07-14
tags: ["pm", "frontend"]
---

## Descrição

Mostrar no Project Manager (DeepTutor) quais worktrees/branches
estão disponíveis e em qual branch cada API está servindo.

### Endpoints já criados

- `GET /api/v1/branches` — lista worktrees
- `GET /api/v1/projects?branch=X` — filtra por branch

Falta integrar no frontend do PM.
