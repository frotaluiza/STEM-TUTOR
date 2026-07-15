---
titulo: "Pipeline Agent Robusto"
slug: pipeline-agent
projeto: ai-stem-tutor
prioridade: alta
status: "A fazer"
criado_em: 2026-07-14
tags: ["infra", "automacao"]
---

## Descrição

Criar um watcher contínuo em Python (Windows Service) que substitua
os scripts PowerShell atuais e garanta:

- Criação automática de branch `sessao/{slug}` ao iniciar sessão
- Criação de branch `ps/{feature}` + `feature/{feature}` ao alterar código
- Commit automático via FileSystemWatcher
- Merge automático ao finalizar sessão
- Push + sync com Notion

**Não depende do LLM lembrar de executar** — o watcher detecta
mudanças nos arquivos e age automaticamente.
