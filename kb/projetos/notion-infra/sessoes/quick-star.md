---
slug: quick-star
title: "Projetos IA e ecossistema guidelines"
date: 2026-06-11
agent: plan
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h00m40s
messages: 7
parts: 25
cost: 0.005319
tokens_input: 30017
tokens_output: 1593
tokens_reasoning: 1188
tokens_cache_read: 120704
tokens_cache_write: 0
created: "2026-06-11 02:32:16 UTC"
updated: "2026-06-11 02:32:57 UTC"
---

Sessão com **7 messages**, **25 parts**, agente **plan**, modelo **deepseek-v4-flash** | 💰 $0.0053 | 💾 cache read: 120.7K | ⏱️ 0h00m40s

## 👤 Usuário (2026-06-11 02:32:20 UTC)

"Liste para mim quais são meus projetos IA no Notion, qual o status de cada um, e me explique como funciona o ecossistema de guidelines que acabou de ser configurado"

## 🤖 Assistente (2026-06-11 02:32:20 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user is asking me two things:

1. List their AI projects in Notion with their status
2. Explain how the ecosystem of guidelines that was just configured works

Since I'm in Plan mode (READ-ONLY), I can only read/search. I should use the Notion tools via Composio to fetch their projects, and also explain the AGENTS.md guidelines.

Let me first search for Notion tools to query the database, then explain the guidelines.

The user has Notion already connected (per the system info). Let me search for the right tools.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:32:31 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I have the Notion database ID for projects: `9172be34-0056-4f38-aa2a-093339bb5790`. Let me first fetch the database schema to understand the property names and types, then query it filtered by area="IA".

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:32:35 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me first fetch the database schema to see the property names and types, then query for IA projects.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:32:39 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have the schema. The properties are:
- Projeto (title) - project name
- Área (select) - area, with options: IA, Música, Estudos, Pessoal, Acadêmico
- Status (status) - with options: Ideia, Planejar, Em andamento, Concluído, Backlog
- Prioridade (select) - Alta, Média, Baixa
- Ordem (number)
- Notas (rich_text)
- Leituras (relation)
- Sessoes (relation)

I need to query for projects where Área = "IA". Let me do that now.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:32:50 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The response was large with 27 items. I need to process the remote file to extract the project names, statuses, and priorities. Let me use the workbench to parse it.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:32:57 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The results show all projects with Área="IA". There are duplicates (some projects appear multiple times with different statuses). Let me look more carefully - some have Status: N/A which likely means they were created without a status set, or they might be duplicate entries. 

Let me filter to only show the unique, current projects with their proper statuses. Some entries have "N/A" for status which likely means the status property was never set for those entries. Many seem to be duplicates.

Let me focus on the meaningful entries (those with an explicit status set):

1. **Feed de notícias (esquerda & geopolítica) — Resumos + Chat** | Ideia | N/A
2. **Conversando com Trabalhos Longos** | Planejar | Média
3. **Integração workflows** | Em andamento | Alta
4. **Automatizador de transcrições (YouTube → Notion)** | N/A | N/A
5. **Marcador de aulas** | N/A | N/A
6. **n8n Workflow para Snipo** | N/A | N/A
7. **Escolhendo ENV** | N/A | N/A
8. **Entendendo a CLI do n8n** | Ideia | Média
9. **Obsidian** | Ideia | N/A
10. **6 - PC Windows (diagnóstico + performance)** | N/A | N/A
11. **Criando redes independentes conectadas** | N/A | N/A
12. **Agente de diagnóstico e otimização de fluxo de trabalho** | N/A | N/A
13. **Parametrizar tipos de chats** | N/A | N/A
14. **Modelagem do chat do Notion — guidelines** | N/A | N/A
15. **Preparador de debates** | N/A | N/A
16. **Automação: sinalizador (emoji) → pesquisa multi-fontes** | N/A | N/A
17. **5 - Automação: enviar PDFs/EPUBs/MOBIs para o Kindle** | N/A | N/A
18. **Assistente pessoal (PC + celular) — compromissos e rotinas** | N/A | N/A
19. **Gerador de pensadores** | Ideia | N/A
20. **3 - AI STEM Tutor** | Planejar | Alta
21. **4 - IA para auxílio em investimentos** | Baixa | Baixa
22. **3 - Kevy Kev — Desenho animado com IA** | Baixa | Baixa
23. **1 - Humanizador recursivo / Revisador de papers** | Em andamento | Alta

There are duplicates - some projects appear multiple times. Let me focus on the unique ones with status set.

For the user's question, let me provide a clean summary. The projects with assigned status are:

1. Feed de notícias (esquerda & geopolítica) — Ideia
2. Conversando com Trabalhos Longos — Planejar (Média)
3. Integração workflows — Em andamento (Alta)
4. Entendendo a CLI do n8n — Ideia (Média)
5. Obsidian — Ideia
6. Gerador de pensadores — Ideia
7. AI STEM Tutor — Planejar (Alta)
8. IA para auxílio em investimentos — Baixa
9. Kevy Kev — Desenho animado com IA — Baixa
10. Humanizador recursivo / Revisador de papers — Em andamento (Alta)

And many others without status set.

Now let me also explain the AGENTS.md guidelines ecosystem. This is based on what was loaded in the system prompt.

</details>

### Resposta

Aqui estão seus **projetos IA** no Notion (database `Projetos (2026)`):

| Projeto | Status | Prioridade |
|---|---|---|
| **Humanizador recursivo / Revisador de papers** | Em andamento | Alta |
| **Integração workflows** | Em andamento | Alta |
| **AI STEM Tutor** | Planejar | Alta |
| **Conversando com Trabalhos Longos** | Planejar | Média |
| **Feed de notícias (esquerda & geopolítica)** | Ideia | — |
| **Entendendo a CLI do n8n** | Ideia | Média |
| **Obsidian** | Ideia | — |
| **Gerador de pensadores** | Ideia | — |
| **IA para auxílio em investimentos** | — | Baixa |
| **Kevy Kev — Desenho animado com IA** | — | Baixa |

Há também ~13 projetos IA sem status definido (ex: Automatizador de transcrições, Marcador de aulas, n8n/Snipo, etc).

---

**Sobre o ecossistema de guidelines recém-configurado:**

O arquivo `AGENTS.md` em `~/.config/opencode/` é carregado em **toda sessão do OpenCode** e define:

1. **Workflow Padrão (Plan → Build → Resumo)** — sempre começar analisando/arquitetando antes de codar, e ao final de cada sessão registrar resumo + artefatos + próximos passos.

2. **Notion como fonte da verdade** — mapeamento completo de 6 databases:
   - **Projetos (2026)** — central, com status, área, prioridade
   - **Sessões opencode** — log automático de cada conversa
   - **Documentação de Projetos** — docs técnicos/arquiteturais
   - **Rotinas** — automações/scripts agendados
   - **Relatórios Diários** — registro de atividades
   - **Leituras** — artigos/papers vinculados a projetos

3. **Agentes especializados** disponíveis via `@`:
   - `@session` — registra sessão no Notion
   - `@exportar-sessao` — salva conversa em Markdown no Obsidian vault
   - `@sync` — sincronização bidirecional Notion ↔ Obsidian
   - `@push-to-notion` — vault → Notion
   - `@watch-sync` — orquestrador que monitora o vault e sincroniza
   - `@add-youtube-videos` — adiciona vídeos curados ao Notion

4. **Ênfase em projetos IA** — são prioridade. O fluxo é: Pesquisa → Arquitetura → Implementação, sempre vinculando sessões ao projeto correto.

Resumindo: é um sistema de **gestão de conhecimento integrado** onde Notion (fonte da verdade), Obsidian (vault local Markdown) e OpenCode (agente/CLI) se comunicam via scripts e agentes, com foco em rastrear cada sessão e manter tudo sincronizado automaticamente.

*Novo passo iniciado*

---

*7 messages | 25 parts | 💰 $0.0053 | ⏱️ 0h00m40s*
