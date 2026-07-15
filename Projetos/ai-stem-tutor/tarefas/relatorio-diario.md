---
titulo: "Relatório Diário Automático"
slug: relatorio-diario
projeto: ai-stem-tutor
prioridade: baixa
status: "A fazer"
criado_em: 2026-07-14
tags: ["automacao", "report"]
---

## Descrição

Script que ao final do dia:

1. Coleta alterações no `project-state.yaml` das últimas 24h
2. Associa conversas do opencode e entradas do Notion às decisões
3. Gera resumo em `Projetos/{slug}/relatorios/diarios/YYYY-MM-DD.md`
4. Faz commit automático
