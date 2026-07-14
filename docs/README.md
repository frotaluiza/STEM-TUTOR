# AI STEM Tutor — Documentação do Projeto

Este diretório contém a documentação completa do fork `frotaluiza/STEM-TUTOR` do DeepTutor.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `modificacoes-stem-tutor.md` | Alterações feitas no fork (features, configuração, comandos) |
| `arquitetura/` | Decisões arquiteturais, ADRs, diagramas |
| `anotacoes-artigos/` | Notas de leitura de artigos acadêmicos (Mastery Path) |

## Sincronização

Esta documentação é sincronizada bidirecionalmente com o Notion via DB `Documentacao de Projetos` + agente `@sync`.

## Fluxo de Documentação

1. **Durante a sessão:** o `watch-live-doc.ps1` registra alterações automaticamente no live doc
2. **Ao final:** `@session` sobe o live doc como corpo da página no Notion (DB Sessões opencode)
3. **Estado do projeto:** `@project-state` atualiza `project-state/` com decisões acumuladas
4. **Documentação contínua:** decisões arquiteturais viram ADRs em `docs/arquitetura/`
