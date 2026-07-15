---
titulo: "ChatBlock no NoteBlocks"
slug: chatblock-noteblocks
projeto: ai-stem-tutor
prioridade: media
status: "A fazer"
criado_em: 2026-07-14
tags: ["noteblocks", "frontend"]
---

## Descrição

Novo tipo de bloco Slate.js no NoteBlocks que permite abrir
uma mini-sessão do opencode inline no documento.

### Especificação

- Bloco customizado com header "💬 Chat · {slug}"
- Input de texto + streaming de resposta
- Slug prefixado: `nb-{doc-id}-{block-index}`
- Origem: `noteblocks` (filtrável no PM)
- Capaz de gerar artefatos no project-space
