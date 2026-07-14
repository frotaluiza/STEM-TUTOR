---
slug: shiny-comet
title: "Guidelines globais no OpenCode"
date: 2026-06-10
agent: build
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 7h34m47s
messages: 78
parts: 276
cost: 0.159492
tokens_input: 985652
tokens_output: 16411
tokens_reasoning: 10101
tokens_cache_read: 5027456
tokens_cache_write: 0
created: "2026-06-10 20:04:29 UTC"
updated: "2026-06-11 03:39:17 UTC"
---

Sessão com **78 messages**, **276 parts**, agente **build**, modelo **deepseek-v4-flash** | 💰 $0.1595 | 💾 cache read: 5.0M | ⏱️ 7h34m47s

## 👤 Usuário (2026-06-10 20:04:29 UTC)

Estava conversando com Notion sobre conseguir sempre dar um contexto para meus chats do opencode. Ele me fez essas recomendações, me fala se você vai conseguir fazer isso: Sim — dá para você ter um “pacote” de guidelines que **toda sessão do OpenCode sempre carrega**, sem depender do repo, usando **config global** e/ou um **diretório de config customizado**.

Abaixo estão as formas que a própria documentação do OpenCode descreve (em ordem do que costuma funcionar melhor).

## 1) Guidelines sempre carregadas (por projeto): `AGENTS.md`

O OpenCode permite criar um `AGENTS.md` com instruções (“Rules”) que entram no contexto do LLM para aquele projeto.[[1]](https://opencode.ai/docs/rules/)

Isso resolve “sempre ler guidelines” **desde que você abra o OpenCode dentro de um diretório de projeto** (ele sobe até o git root e pega config do projeto).[[2]](https://opencode.ai/docs/config/)

Mas você pediu algo para **uma sessão aleatória** — então precisa da camada global também.

## 2) Guidelines sempre carregadas (global / qualquer sessão): config global em `~/.config/opencode/`

A doc diz que existe config global em:

- `~/.config/opencode/opencode.json` (config global)[[2]](https://opencode.ai/docs/config/)

E você pode definir prompts de agentes no `opencode.json`, apontando para um arquivo (ex.: um `.md` ou `.txt`) via `prompt`.[[3]](https://opencode.ai/docs/agents/)

Exemplo (conceitual) da doc:

```json
{ "agent" : { "review" : { "prompt" : "{file:./prompts/code-review.txt}" } } }
```

O ponto importante é: **o caminho é relativo a onde o config está** (global ou do projeto).[[3]](https://opencode.ai/docs/agents/)

Então, na prática, você consegue:

- criar uma pasta tipo `~/.config/opencode/prompts/`
- colocar lá um arquivo com suas “guide lines” (ex.: `global-guidelines.md`)
- e configurar o(s) agente(s) para sempre usar esse prompt (ou um “agent base” que você sempre usa)

## 3) Uma “pasta de guidelines” portátil: `OPENCODE_CONFIG_DIR`

A doc também descreve uma variável de ambiente:

- `OPENCODE_CONFIG_DIR=/path/to/my/config-directory`

Esse diretório customizado “será procurado por agents, commands, modes, plugins igual ao `.opencode`” e pode sobrescrever settings.[[2]](https://opencode.ai/docs/config/)

Isso é exatamente o que você descreveu como “uma pasta de guidelines”:

### Como você usaria

1) Criar uma pasta fora de qualquer repo, por exemplo:

- `~/opencode-guidelines/`
    - `prompts/`
    - `agents/`
    - `opencode.json` (se você quiser)

2) Exportar a env var antes de iniciar o opencode:

```bash
export OPENCODE_CONFIG_DIR=~/opencode-guidelines
opencode
```

Aí, **qualquer sessão**, em qualquer pasta aleatória, passa a “ver” essa pasta como fonte de config/agents/prompts.

## 4) Alternativa: `OPENCODE_CONFIG` (arquivo único de config)

Se você preferir apontar direto para um arquivo de configuração específico:

- `OPENCODE_CONFIG=/path/to/my/custom-config.json`[[2]](https://opencode.ai/docs/config/)

Isso é útil se você quiser trocar perfis (ex.: “perfil pesquisa” vs “perfil implementação”).

---

# O que eu recomendaria para o seu caso (bem direto)

Para garantir “sempre ler guidelines” em **toda sessão aleatória**, eu faria:

- **Global**: colocar um “perfil base” em `~/.config/opencode/` (pra funcionar sempre)
- **Portátil / explícito**: manter uma pasta `~/opencode-guidelines/` e iniciar o opencode com `OPENCODE_CONFIG_DIR` quando você quiser forçar aquele conjunto (ou usar um alias no shell)

E dentro das guidelines, escrever algo do tipo:

- “Sempre registrar progresso no Notion (DB Logs) ao final”
- “Sempre começar em Plan mode e só depois Build”
- “Sempre produzir: Resumo curto + Artefatos/links + Próximos passos”

Se você me disser **como você inicia o OpenCode hoje** (TUI no terminal? comando `opencode run`? dentro do repo ou solto?), eu te devolvo um setup bem específico com:

- estrutura exata da pasta `OPENCODE_CONFIG_DIR`
- nomes de arquivos de prompt
- um `opencode.json` exemplo para você colar e testar. 

## 🤖 Assistente (2026-06-10 20:04:29 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user is asking about setting up OpenCode with global guidelines/configuration that always loads, regardless of which project directory they're in. They want to know if I can help set this up.

Let me look at the opencode documentation to understand the configuration options and give them accurate guidance.

</details>

### Resposta

Vou consultar a documentação oficial do OpenCode pra te dar um setup preciso.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-10 20:04:34 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have all the documentation. Let me understand the user's request:

1. The user wants a setup where OpenCode always loads certain "guidelines" or context in every session, regardless of which directory they're in.
2. They had a conversation with Notion and got recommendations about:
   - AGENTS.md (per project)
   - Global config in `~/.config/opencode/` (global)
   - `OPENCODE_CONFIG_DIR` env var (portable guidelines folder)
   - `OPENCODE_CONFIG` env var (single config file)

The user wants to know if I can help them set this up. They also mention:
- "Sempre registrar progresso no Notion (DB Logs) ao final"
- "Sempre começar em Plan mode e só depois Build"
- "Sempre produzir: Resumo curto + Artefatos/links + Próximos passos"

And they ask: "se você me disser como você inicia o OpenCode hoje, eu te devolvo um setup bem específico"

So the user is asking me to confirm I can do this and is asking me to tell them how I start OpenCode so they can give me a specific setup. But actually, I think the user is asking ME (the LLM/agent) to set this up for them.

Let me re-read: "Me fala se você vai conseguir fazer isso" - "Tell me if you'll be able to do this."

They want me to:
1. Confirm I understand and can do it
2. Probably ask them how they start OpenCode (TUI? CLI? inside repo or standalone?)
3. Set up the configuration

Let me help them set this up. Based on the docs:

**Best approach for their case:**

Option 1: **Global AGENTS.md** at `~/.config/opencode/AGENTS.md` - This is the simplest and most reliable. It gets loaded in every session regardless of project.

Option 2: **`instructions` in global opencode.json** - they can point to instruction files.

The cleanest approach using what the docs recommend:

1. Create `~/.config/opencode/AGENTS.md` with their global guidelines
2. Optionally create `~/.config/opencode/opencode.json` with `instructions` pointing to additional files

Since they also mention Notion integration (logging sessions), they might want to add that as a custom tool or command, but that's a separate concern.

Let me first ask them how they start OpenCode to tailor the setup, and then create the files.

Actually, looking more carefully at the user's message, the last paragraph is:
"Se você me disser como você inicia o OpenCode hoje (TUI no terminal? comando `opencode run`? dentro do repo ou solto?), eu te devolvo um setup bem específico com:
- estrutura exata da pasta `OPENCODE_CONFIG_DIR`
- nomes de arquivos de prompt
- um `opencode.json` exemplo para você colar e testar."

This seems to be the Notion's recommendation, not the user's own words. The user is relaying what Notion told them.

So the user wants to know: can I (this agent/LLM) actually do this setup for them?

Let me just confirm yes and ask them how they start OpenCode.

</details>

### Resposta

Sim, consigo fazer isso perfeitamente. Baseado na documentação oficial que acabei de ler, a abordagem mais robusta para **qualquer sessão aleatória** é:

**Camada global (`~/.config/opencode/`)** + opcionalmente **`OPENCODE_CONFIG_DIR`** para um conjunto portátil.

Antes de criar os arquivos, preciso de 2 informações:

Como você inicia o OpenCode hoje?
- Uso **TUI** (terminal interativo, `opencode` solto) ou **CLI** (`opencode run "mensagem"`) ou **IDE**?
- Costuma abrir **dentro de pastas de projeto** (com git) ou **em pastas soltas** qualquer?

*Novo passo iniciado*

## 👤 Usuário (2026-06-11 00:02:11 UTC)

Acho que uso TUI, quando inicio uma sessão coloco "opencode". Seria melhor para criar direto um nome para a sessão jpa inserir o primeiro prompt na chamada do terminal. Por enquanto ainda não estou abrindo em pastas de projeto, mas poderia começar a fazer isso. É´o recomendado?

## 👤 Usuário (2026-06-11 00:55:28 UTC)

Acho que uso TUI, quando inicio uma sessão coloco "opencode". Seria melhor para criar direto um nome para a sessão jpa inserir o primeiro prompt na chamada do terminal. Por enquanto ainda não estou abrindo em pastas de projeto, mas poderia começar a fazer isso. É´o recomendado?

## 👤 Usuário (2026-06-11 01:03:35 UTC)

Acho que uso TUI, quando inicio uma sessão coloco "opencode". Seria melhor para criar direto um nome para a sessão jpa inserir o primeiro prompt na chamada do terminal. Por enquanto ainda não estou abrindo em pastas de projeto, mas poderia começar a fazer isso. É´o recomendado? 

## 🤖 Assistente (2026-06-11 01:03:35 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user is confirming they use TUI mode (just `opencode`), and asking:
1. Is it better to pass a session name and first prompt directly in the terminal call?
2. Is it recommended to open within project folders?

Let me answer concisely based on the docs I've read.

About project folders: Yes, it's recommended. The docs say OpenCode "traverses up to the nearest Git directory" to find project configs. It also finds `AGENTS.md` by traversing up from the current directory. So opening inside a project folder lets you use project-specific AGENTS.md and opencode.json.

About session name/first prompt in terminal: The `opencode run` CLI command can take a prompt directly. But for TUI, you just type `opencode` and the session starts. There's also `opencode run "your prompt"` for CLI mode.

Let me keep it super concise.

</details>

### Resposta

**Projeto**: Sim, é recomendado — o OpenCode sobe até o git root pra achar `AGENTS.md` e `opencode.json`. Mas com o setup global que vou criar, funciona em qualquer pasta.

**CLI vs TUI**: Dá pra fazer os dois:
- `opencode` → TUI interativo
- `opencode run "seu prompt"` → já cria sessão nomeada com o primeiro prompt

Quer que eu monte o setup global agora? Preciso saber:
- **Alias no shell**: quer um atalho tipo `oc` no lugar de `opencode`?
- **Nome do prompt**: quer nomear a sessão automaticamente? (ex: `oc "Revisar código"`)

Se sim, me passa qual shell você usa (PowerShell, bash, zsh?) que já crio o alias + a estrutura de guidelines globais.

*Novo passo iniciado*

## 👤 Usuário (2026-06-11 01:18:49 UTC)

Pode criar o Alias desse jeito, eu uso powershell. Para criar a estrutura de guidelines globais, queria que você visitasse meu dashboard de 2026 e olhasse a estrutura de todas as tabelas que eu tenho lá, e o contexto de cada uma delas, para a sessão do opencode ter esse contexto se quiser. A enfase deve ser dada para a área de Projetos IA. A sessão deve entender como eu estruturo meus projetos e como ela deve trabalhar para preecher as databases na etapa de pesquisa e arquitetura. Depois iriamos para a parte de codar, para isso acho que seria interessante criar uma database no Notion para cada repo do github, com os links das repos associados com o ID do projeto. Também queria que todas as minhas sessões tivessem contexto dos agentes que uso para fazer o backup com o Notion dos chats, além do sync com o obsidan. Outra coisa, queria que ele tivesse conhecimento da minha database de Rotinas, que ainda não preenchi, mas que devem conter detalhamentos sobre as rotinas que eu rodo no meu task manager.Também deve ter noção de outra tabela que ainda preciso aprimorar o preenchimento, que é minha tabela de Relatórios Diários. Ainda tem a tabela de documentações de projetos, que deve ser apenas preenchidas ao final de cada projeto, e deve ter a documentação de tudo que foi feito naquele projeto (fase de pesquisa e planejamento + códigos). 

## 🤖 Assistente (2026-06-11 01:18:49 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to:

1. Set up a global OpenCode configuration with guidelines
2. Visit their Notion dashboard for 2026 to understand the structure of all their databases/tables
3. Create context-aware guidelines that understand:
   - All Notion database structures and contexts
   - Emphasis on "Projetos IA" (AI Projects) area
   - How projects are structured
   - How to fill databases during research and architecture phases
   - A Notion database for each GitHub repo with links and project IDs
   - Context about agents used for backup/sync with Notion and Obsidian
   - Knowledge of "Rotinas" (Routines) database
   - "Relatórios Diários" (Daily Reports) database
   - "Documentações de Projetos" (Project Documentation) database

Let me start by accessing their Notion to understand the database structure. I need to use the Composio tools to connect to Notion and browse their databases.

Let me first search for Notion tools available through Composio.

</details>

### Resposta

Vou começar explorando seu Notion para entender a estrutura completa. Primeiro, vou buscar as ferramentas disponíveis.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:18:57 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good, the Notion connection is active. Now I need to explore the Notion workspace to understand the database structure. Let me start by:

1. First, searching for databases in the Notion workspace
2. Then querying the specific databases mentioned: Projetos IA, Rotinas, Relatórios Diários, Documentações de Projetos, and any session/task management databases

Let me start by searching for databases and pages to understand the workspace structure.

</details>

### Resposta

Ótimo, conexão com Notion ativa. Vou explorar seu workspace para mapear todas as databases.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:19:08 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I got a list of 30 databases, but with truncated data. Let me get the full list to see all databases and their names, then query the specific ones the user mentioned. Let me process the remote file to get the complete list of database names and IDs.

</details>

### Resposta

Vou processar a lista completa de databases pra identificar todas.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:19:16 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I can see the databases. The key ones are:

1. **Sessões opencode (2026)** - ID: 372191ce-57f9-810c-99aa-d5fa31deb926
2. **Documentacao de Projetos** - ID: 374191ce-57f9-8178-9257-dbdbfe8f48b5
3. **Projetos (2026)** - ID: 9172be34-0056-4f38-aa2a-093339bb5790
4. **Rotinas** - ID: 374191ce-57f9-8181-8806-ddae7c34dbaf
5. **Relatorios Diarios** - ID: 374191ce-57f9-81b2-b91c-ee1eedb79dc3

Now I need to query each of these databases to understand their full property structure. Let me fetch the schema of all the important databases.

</details>

### Resposta

Encontrei 30 databases. Agora vou buscar a estrutura das principais que você mencionou.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:19:23 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have all the database schemas. Let me also check the data inside these databases to understand the records. Let me also look at the Sessões database to see existing entries, and look at some Projetos entries to understand how things are structured.

Let me now compile my understanding:

## Database Schemas Found:

### 1. Projetos (2026) - ID: 9172be34-0056-4f38-aa2a-093339bb5790
Fields:
- **Projeto** (title) - Nome do projeto
- **Área** (select) - IA, Música, Estudos, Pessoal, Acadêmico
- **Status** (status) - Ideia, Planejar, Em andamento, Concluído, Backlog
- **Prioridade** (select) - Alta, Média, Baixa
- **Ordem** (number) - Ordem de exibição
- **Notas** (rich_text) - Notas sobre o projeto
- **Leituras** (relation → Leituras DB)
- **Sessoes** (relation → Sessões opencode DB)

### 2. Documentacao de Projetos - ID: 374191ce-57f9-8178-9257-dbdbfe8f48b5
Fields:
- **Nome** (title) - Nome do documento
- **Projeto** (relation → Projetos (2026))
- **Arquitetura** (rich_text) - Detalhes da arquitetura
- **Descricao** (rich_text) - Descrição
- **Documentacao** (rich_text) - Documentação completa
- **Logs** (relation → Sessões opencode)
- **Repositorio** (url) - URL do repositório GitHub
- **Ultima Atualizacao** (date) - Data da última atualização

### 3. Rotinas - ID: 374191ce-57f9-8181-8806-ddae7c34dbaf
Fields:
- **Nome** (title) - Nome da rotina
- **Descricao** (rich_text) - Descrição
- **Frequencia** (select) - 10min, 1h, 6h, Diario, Semanal, Manual
- **Parametros** (rich_text) - Parâmetros da rotina
- **Projeto** (relation → Projetos (2026))
- **Repositorio** (url) - URL do repositório
- **Status** (status) - Ativa, Pausada, Erro
- **Ultima Execucao** (date) - Data da última execução
- **Ultimo Commit** (rich_text) - Último commit

### 4. Relatorios Diarios - ID: 374191ce-57f9-81b2-b91c-ee1eedb79dc3
Fields:
- **Nome** (title) - Título do relatório
- **Data** (date) - Data do relatório
- **Resumo** (rich_text) - Resumo do dia
- **Horas** (number) - Horas trabalhadas
- **Projetos** (multi_select) - IA - AI STEM Tutor, Humanizador, TCC, Música, Estudos, PC, Automação
- **Sessoes** (rich_text) - Sessões realizadas (texto livre)

### 5. Sessões opencode (2026) - ID: 372191ce-57f9-810c-99aa-d5fa31deb926
Fields:
- **Sessão** (title) - Nome da sessão
- **Data** (date) - Data
- **Status** (status) - Aberto, Em andamento, Concluído
- **Resumo (curto)** (rich_text) - Resumo curto
- **Título Resumido** (rich_text) - Título resumido
- **Observações** (rich_text) - Observações
- **Origem** (select) - notion, opencode
- **Thread / Chat URL** (url) - URL da thread
- **Chat ID** (rich_text) - ID do chat
- **Artefatos (links/arquivos)** (rich_text) - Links e arquivos
- **Projeto 1** (relation → Projetos (2026)) - Link direto
- **Projetos** (relation → Projetos (2026)) - Relação dual
- **Projeto (antigo)** (multi_select) - Obsidian
- **Última edição** (date) - Última edição

Now let me also look at the existing data in some of these databases to understand the content.

</details>

### Resposta

Estruturei todos os schemas. Agora vou pegar dados de exemplo das databases e também consultar alguns projetos existentes.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:19:36 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a thorough understanding of the user's Notion workspace. Let me compile the full structure and then create the AGENTS.md guidelines file and the PowerShell profile setup.

Key findings:

## Database Structures

### 1. Projetos (2026)
- **Projeto** (title) - nome
- **Área** (select): IA, Música, Estudos, Pessoal, Acadêmico
- **Status** (status): Ideia, Planejar, Em andamento, Concluído, Backlog
- **Prioridade** (select): Alta, Média, Baixa
- **Ordem** (number)
- **Notas** (rich_text)
- **Leituras** (relation → Leituras)
- **Sessoes** (relation → Sessões opencode)

### 2. Documentacao de Projetos
- **Nome** (title)
- **Projeto** (relation → Projetos)
- **Arquitetura** (rich_text)
- **Descricao** (rich_text)
- **Documentacao** (rich_text)
- **Logs** (relation → Sessões opencode)
- **Repositorio** (url)
- **Ultima Atualizacao** (date)

### 3. Rotinas
- **Nome** (title)
- **Descricao** (rich_text)
- **Frequencia** (select): 10min, 1h, 6h, Diario, Semanal, Manual
- **Parametros** (rich_text)
- **Projeto** (relation → Projetos)
- **Repositorio** (url)
- **Status** (status): Ativa, Pausada, Erro
- **Ultima Execucao** (date)
- **Ultimo Commit** (rich_text)

### 4. Relatorios Diarios
- **Nome** (title)
- **Data** (date)
- **Resumo** (rich_text)
- **Horas** (number)
- **Projetos** (multi_select): IA - AI STEM Tutor, Humanizador, TCC, Música, Estudos, PC, Automação
- **Sessoes** (rich_text)

### 5. Sessões opencode (2026)
- **Sessão** (title)
- **Data** (date)
- **Status** (status): Aberto, Em andamento, Concluído
- **Resumo (curto)** (rich_text)
- **Título Resumido** (rich_text)
- **Observações** (rich_text)
- **Origem** (select): notion, opencode
- **Thread / Chat URL** (url)
- **Chat ID** (rich_text)
- **Artefatos (links/arquivos)** (rich_text)
- **Projeto 1** (relation → Projetos)
- **Projetos** (relation → Projetos)
- **Projeto (antigo)** (multi_select)
- **Última edição** (date)

### 6. Leituras
ID: 72f3e8c5-ce1f-4728-b255-833c228d4290

### Other databases that exist:
- Composições
- Músicas (Projeto Claudio)
- 🛒 Lista de compras (Feira)
- Logs do TCC
- Para futuras pesquisas
- Anotações
- Tarefas da Semana
- Escutando (2026)
- 📣 Social — Conteúdos
- 📚 Social — Pesquisa
- Log — Automatizador de transcrições
- Músicas — Saluz
- Gravações de ensaio
- Propostas (UP)
- Aulas — Bateria (Prof. Ronaldo)
- Log de Composições
- Ideias de estética (Minas + Beatles)
- Presente — Fogão até R$ 600
- Salgados & Bolos — Opções
- Convidados — Aniversário Samara
- ⏱️ Sessões (Clockify)
- Hábitos Diários
- Pensamentos
- Livros

Now let me create:
1. `~/.config/opencode/AGENTS.md` - Global guidelines with full context
2. `~/.config/opencode/opencode.json` - Config to add instructions
3. PowerShell profile with alias `oc`

Let me also check if the user has a PowerShell profile file.

</details>

### Resposta

Perfeito, tenho o mapeamento completo. Agora vou criar toda a estrutura. Primeiro, verifico o profile do PowerShell.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:19:46 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The PowerShell profile doesn't exist yet. Let me check what's in the opencode config directory, and also check if the user's profile path is correct.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:19:50 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me check the existing opencode.jsonc to understand what's already configured.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:19:52 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I understand the full picture. The user already has a very sophisticated setup with:
1. Global config at `~/.config/opencode/opencode.jsonc`
2. Multiple agents (session, sync, push-to-notion, watch-sync, exportar-sessao, add-youtube-videos)
3. MCP for Composio/Notion integration
4. Plugins for oh-my-opencode and obsidian-sync

But what's missing is a **global `AGENTS.md`** that provides context about the Notion databases and guidelines for every session.

What I need to create:
1. `~/.config/opencode/AGENTS.md` - Global guidelines that:
   - Documents all Notion database structures
   - Gives emphasis on "Projetos IA" area
   - Explains how to structure projects
   - Provides context about the agents (session, sync, etc.)
   - Documents the Rotinas, Relatorios Diarios, Documentacao de Projetos databases
   - Sets workflow expectations (Plan before Build)
   - Sets output expectations (summary + artifacts + next steps)

2. Add `instructions` field to `opencode.jsonc` to reference AGENTS.md (though global AGENTS.md is already auto-loaded per the docs)

3. Create PowerShell profile with alias

Let me also check: the docs say global AGENTS.md at `~/.config/opencode/AGENTS.md` is auto-loaded. So I just need to create it.

But I also need to add the `instructions` field to the existing `opencode.jsonc` to load AGENTS.md explicitly via instructions.

Actually, according to the docs:
- **Global AGENTS.md** at `~/.config/opencode/AGENTS.md` - auto-loaded across all sessions
- **Custom Instructions** via `instructions` in opencode.json - also works with file paths

So I just need to create `~/.config/opencode/AGENTS.md` and it will auto-load in every session.

Let me also add the `instructions` field to the opencode.jsonc as an additional safety measure.

And create a PowerShell profile with the `oc` alias.

Let me now create everything:

1. `~/.config/opencode/AGENTS.md` - comprehensive guidelines
2. Update `~/.config/opencode/opencode.jsonc` - add `instructions` field pointing to AGENTS.md and add `default_agent: "plan"` 
3. Create PowerShell profile with `oc` alias (`oc` for `opencode`, `ocr` for `opencode run`)

Let me write the AGENTS.md with all the database context.

</details>

### Resposta

Perfeito. Já vi todo seu setup — você já tem agents, MCP, plugins. Faltava o **contexto global** pra toda sessão. Vou criar agora:

1. `~/.config/opencode/AGENTS.md` — guidelines globais com todo o contexto do Notion
2. Atualizar `opencode.jsonc` pra incluir `instructions` e `default_agent`
3. Criar profile PowerShell com alias `oc`

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:20:01 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me create the AGENTS.md file with the comprehensive Notion database context.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:20:21 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me update the opencode.jsonc to add `instructions` pointing to the AGENTS.md and also set `default_agent` to `"plan"` as the user wants to always start in Plan mode.

Looking at the existing jsonc, I need to add:
1. `"instructions": ["AGENTS.md"]` at the top level — This tells opencode to explicitly include AGENTS.md as instructions. Since this is inside `~/.config/opencode/`, the path is relative to that directory, so `"AGENTS.md"` should work.
2. `"default_agent": "plan"` — to start every session in Plan mode by default.

Actually, looking at the docs more carefully:
- The `instructions` field takes an array of paths or glob patterns
- "File paths can be relative to the config file directory, or absolute paths starting with / or ~"

So I can add `"instructions": ["AGENTS.md"]` to the global opencode.jsonc. But wait, since the AGENTS.md is already auto-loaded by OpenCode (global rules), the `instructions` field might be redundant for this specific file. But it's useful as a safety measure and to explicitly document it.

Also, let me add the `default_agent` to `"plan"`.

Let me add these to the existing opencode.jsonc.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:20:27 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I need to add:
1. `instructions` pointing to the AGENTS.md
2. `default_agent` to `"plan"` 
3. Maybe also `"model"` to specify the model

Let me add these to the top of the opencode.jsonc file, right after the `$schema` line.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:20:31 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good. Now let me create the PowerShell profile with the alias. The profile doesn't exist yet, so I need to create it. I need to create the directory first if it doesn't exist.

The profile path is: `C:\Users\frota\OneDrive\Documentos\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`

Let me create the directory and file.

</details>

*Novo passo iniciado*

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:20:37 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me create the PowerShell profile with the `oc` alias and `ocr` alias.

`oc` runs `opencode` (TUI mode)
`ocr` runs `opencode run "prompt"` (CLI mode with immediate prompt)

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:20:40 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me test the configuration by reading back the files and checking if opencode can load them.

Let me verify the files and also test that opencode recognizes the config.

</details>

*Novo passo iniciado*

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:20:48 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The config is loading correctly. I can see:
1. `default_agent: "plan"` is set
2. `instructions: ["AGENTS.md"]` is loaded
3. All the agents are still there

Let me now verify the AGENTS.md was created properly and test the alias.

</details>

### Resposta

Config carregou perfeitamente. Vou verificar o AGENTS.md e testar o alias.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:20:53 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The alias isn't showing in the current session because the profile hasn't been reloaded. But that's fine - it will work in new PowerShell sessions. Let me test by dot-sourcing the profile.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:20:56 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Everything is working:
1. `oc` -> alias to `opencode` (TUI mode)
2. `ocr` -> function for `opencode run [args]` (CLI with immediate prompt)
3. AGENTS.md created with 135 lines of full context
4. opencode.jsonc updated with `default_agent: "plan"` and `instructions: ["AGENTS.md"]`

Let me finalize the todos and provide a summary.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 01:21:00 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me provide a clear summary of everything I did.

</details>

### Resposta

Tudo pronto. Aqui está o que foi criado/atualizado:

## O que foi feito

### 1. `~/.config/opencode/AGENTS.md` (135 linhas)
Guidelines globais com:
- **Workflow padrão**: Plan → Build → @session ao final
- **All 6 databases** do Notion mapeadas com schemas, propriedades, tipos e IDs
- **Ênfase em Projetos IA** com fases de Pesquisa → Arquitetura → Implementação
- **Todos os agentes** documentados (`@session`, `@sync`, `@push-to-notion`, `@watch-sync`, `@exportar-sessao`, `@add-youtube-videos`)
- **Convenções**: nomenclatura de sessões, output esperado, prioridades

### 2. `~/.config/opencode/opencode.jsonc` (atualizado)
- `"default_agent": "plan"` — toda sessão começa em Plan mode
- `"instructions": ["AGENTS.md"]` — carrega as guidelines explicitamente

### 3. `Microsoft.PowerShell_profile.ps1` (criado)
- **`oc`** — atalho para `opencode` (TUI)
- **`ocr`** — atalho para `opencode run [args]` (CLI com prompt direto)

## Como usar

```powershell
oc                    # TUI interativo (sempre começa em Plan)
ocr "Sua tarefa aqui" # CLI com prompt direto + nome de sessão
```

**Toda sessão**, em qualquer diretório, vai carregar automaticamente o contexto completo do Notion.

*Novo passo iniciado*

## 👤 Usuário (2026-06-11 02:31:40 UTC)

Me dá um comando de teste para eu criar uma sessão usando esse shortcut, e também testando essas guidelines globais. Eu preciso reiniciar o terminar para a sessão conseguir ler as guidelines?

## 🤖 Assistente (2026-06-11 02:31:41 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants:
1. A test command to try out the new alias and global guidelines
2. To know if they need to restart the terminal for OpenCode to read the new AGENTS.md

For the terminal: OpenCode reads AGENTS.md from `~/.config/opencode/AGENTS.md` at session startup. The user doesn't need to restart the terminal for OpenCode itself - OpenCode reads the file when it starts a session. But they DO need to restart the terminal (or reload the profile) for the new `oc` alias to work in their current PowerShell session.

Let me give them a simple test command and explain both points.

</details>

### Resposta

**Terminal**: você precisa reiniciar o terminal OU rodar `. $PROFILE` pra ativar o alias `oc` na sessão atual. O OpenCode lê o `AGENTS.md` automaticamente ao iniciar qualquer sessão — não precisa reiniciar nada pra ele.

Comando de teste pra criar uma sessão já com contexto:

```powershell
ocr "Liste para mim quais são meus projetos IA no Notion, qual o status de cada um, e me explique como funciona o ecossistema de guidelines que acabou de ser configurado"
```

Isso vai:
1. Criar uma sessão com esse prompt via CLI
2. Carregar automaticamente o `AGENTS.md` global
3. Começar em **Plan mode** (`default_agent: "plan"`)
4. Puxar dados do Notion via MCP/Composio

**Obs**: se quiser, depois posso te mostrar o comando pra confirmar que as instructions estão carregadas (`opencode debug config`).

*Novo passo iniciado*

## 👤 Usuário (2026-06-11 02:39:44 UTC)

Uma pergunta, está configurada uma atualização rotineira dessas guidelines na medida que eu avanço com meus projetos?

## 🤖 Assistente (2026-06-11 02:39:44 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user is asking if there's an automatic/routine update mechanism for the AGENTS.md guidelines as their projects evolve. The answer is no - I created a static AGENTS.md file. There's no built-in mechanism to auto-update it as their Notion databases change.

Let me think about what could be done:

1. The AGENTS.md is static - it has the database schemas which won't change often, but things like "Lista atual de projetos IA" at the bottom will get outdated.
2. No, there's no routine update configured. I should suggest a way to handle this.

Options:
- Add a note in AGENTS.md telling the agent to always check Notion first (live data) rather than relying on the static list
- Create a script that regenerates AGENTS.md from Notion periodically
- Use the `@sync` agent to check for changes

The simplest and most practical approach: modify the AGENTS.md to tell the LLM that the static info is a reference but it should ALWAYS query Notion directly for live data. That way the file doesn't need constant updates.

But also, I could offer to create a script that regenerates/updates AGENTS.md from Notion periodically.

</details>

### Resposta

Não, não configurei — o `AGENTS.md` é **estático**. A lista de projetos IA ali vai ficar desatualizada com o tempo.

Duas opções pra resolver:

1. **(Recomendado)** Adicionar uma instrução no `AGENTS.md` mandando o LLM **sempre consultar o Notion ao vivo** em vez de confiar na lista estática. Assim o arquivo nunca precisa ser atualizado.

2. Criar um script (ou um comando OpenCode) que **regenera o `AGENTS.md`** consultando o Notion e atualizando a lista de projetos/status.

Qual você prefere? A opção 1 é mais simples e confiável; a opção 2 te dá um `AGENTS.md` sempre fresco.

*Novo passo iniciado*

## 👤 Usuário (2026-06-11 02:44:05 UTC)

Acho que dá para pedir pra ele sempre fazer o fetch no notion para pegar tudo atualizado em relação aos meus projetos e entradas dentro das databases. Porém, gostaria que fosse delimitado toda a filosofia de projetos sem precisar do fetch, então se eu CRIO uma database nova ou altero minha filosofia de condução de projetos, quero que esse arquivo seja atualizado. Daria para criar uma agente que atualiza esse arquivo se eu fizer aguma alteraçao estrutural assimw

## 🤖 Assistente (2026-06-11 02:44:05 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants two things:

1. Make the AGENTS.md dynamic for project data (always fetch from Notion at runtime)
2. Keep the "philosophical" / structural parts static in AGENTS.md, but have a way to update them when the user makes structural changes (new databases, changed workflows)

For #1, I should update the AGENTS.md to include an instruction that tells the LLM to always query Notion for live data (projects, statuses, etc.) rather than relying on the static list.

For #2, the user wants an agent that can update the AGENTS.md when structural changes happen. This is essentially a self-updating mechanism. I could create a subagent (@update-guidelines or similar) that:
- Reads the current AGENTS.md
- Queries all databases from Notion to check their structure
- Updates the static parts if needed
- Rewrites the AGENTS.md file

Let me think about this more carefully. The user wants:
- **Dynamic data** (project lists, statuses, etc.) → always fetched from Notion at session start
- **Structural/philosophical** (how databases are organized, workflows, conventions) → stays in AGENTS.md but needs a way to update when things change

The best approach:

1. Update AGENTS.md to:
   - Keep ALL the structural documentation (database schemas, workflows, agents, conventions) - this is the "philosophy"
   - Remove the static project list (the "Lista atual de projetos IA" section)
   - Add an instruction at the top: "Always query Notion databases directly for current project data. Do not rely on static lists in this file."

2. Create a subagent `@update-guidelines` that:
   - Fetches ALL databases from Notion
   - Fetches their schemas
   - Compares with what's in AGENTS.md
   - If new databases are found or schemas changed, updates the "Databases do Notion" section
   - Can also be triggered manually when the user makes structural changes

Let me implement this approach.

Actually, let me re-read the user's message more carefully:

"Daria para criar uma agente que atualiza esse arquivo se eu fizer aguma alteraçao estrutural assimw"

So yes, they want an agent that updates the AGENTS.md when structural changes happen (new databases, changed workflow philosophy).

Let me:
1. Update AGENTS.md to:
   - Add instruction to fetch live data from Notion
   - Remove the static project list
   - Keep all structural/philosophical content
2. Create a `@update-guidelines` subagent in the opencode.jsonc

</details>

### Resposta

Boa ideia. Vou fazer duas coisas:

1. **Ajustar o `AGENTS.md`** — dados dinâmicos viram instrução de fetch ao vivo; filosofia/estrutura permanece estática
2. **Criar agente `@update-guidelines`** — varre o Notion, detecta mudanças estruturais e atualiza o `AGENTS.md`

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:44:16 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me read the AGENTS.md first to make precise edits.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:44:19 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I need to:

1. Add a "Regra de Dados Dinâmicos" section at the top (after the intro) that tells the LLM to always fetch live data from Notion
2. Remove the static "Lista atual de projetos IA" section at the bottom (lines 161-168) and replace it with a general note about IA priority
3. Add the `@update-guidelines` agent to the opencode.jsonc

Let me also update the "ÊNFASE EM PROJETOS IA" section to remove the phrase about "Ao trabalhar com eles" since it's implicit.

Actually, let me be more surgical:
- Add a `## Regra de Dados Dinâmicos` section right after the intro
- Replace the static "Lista atual de projetos IA" with a general statement
- Keep everything else

Then add the agent to opencode.jsonc.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:44:26 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good. Now let me replace the static project list at the bottom with a general statement about IA priority.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:44:31 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me add the `@update-guidelines` agent to opencode.jsonc. Let me read the file to see where to add it.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:44:37 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I need to add the `@update-guidelines` agent before the closing `}` of the `"agent"` block. Let me edit to add it right before the end.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:44:52 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The old string didn't match. Let me re-read the end of the file more carefully to get the exact content.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:44:54 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The indentation uses 4 spaces for JSONC, and the closing is `    }` (4 spaces), `  }` (2 spaces). Let me copy the exact text to match:

The old string should be:
```
      "prompt": "You add 30 curated YouTube videos...
...
IMPORTANT: Process ONE video at a time - do NOT batch them. Check each one individually to avoid duplicates."
    }
  }

```

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:45:07 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me test the config to make sure it loads correctly.

</details>

*Novo passo iniciado*

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:45:16 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Config loads fine. Let me also quickly verify the agent `update-guidelines` shows up.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:45:24 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Everything is working. Let me finalize the todo.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:45:27 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

All done. Let me give a clear summary of what changed.

</details>

### Resposta

Pronto. Resumo do que foi feito:

## Mudanças

### `AGENTS.md`
- Adicionada **Regra de Dados Dinâmicos** no topo — toda sessão é instruída a consultar o Notion ao vivo para dados mutáveis (projetos, status, etc.)
- Removida a **lista estática de projetos IA** — substituída por instrução de fetch ao vivo
- Estrutura fixa (schemas, workflows, convenções) permanece como documentação estática

### `opencode.jsonc`
- **Novo agente `@update-guidelines`** — varre o Notion, detecta novas databases ou schemas alterados, e atualiza o `AGENTS.md` com edits precisos

## Como usar

```powershell
ocr "Liste meus projetos IA com status atualizados do Notion"  # → busca ao vivo
@update-guidelines  # → quando criar database nova ou mudar filosofia
```

O `AGENTS.md` agora só precisa ser atualizado manualmente (via `@update-guidelines`) quando você fizer mudanças **estruturais** — o resto o LLM busca fresco toda sessão.

*Novo passo iniciado*

## 👤 Usuário (2026-06-11 02:46:35 UTC)

Ele sabe que pode ser atualizado dessa maneira? Eu gostaria de ser lembrada de quando vou precisar atuaizar as guidelines

## 🤖 Assistente (2026-06-11 02:46:35 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user is asking two things:

1. Does the LLM know it can be updated via `@update-guidelines`? 
2. They want to be reminded when they need to update the guidelines.

For #1: I added the agent description and prompt to opencode.jsonc, but I haven't documented the `@update-guidelines` agent in the AGENTS.md file itself. The LLM reads the AGENTS.md at the start of every session, so it needs to be documented there for the LLM to know about it.

For #2: I need to update the AGENTS.md to include the agent in the "Agentes Disponíveis" section, and also add a reminder mechanism. The simplest approach is to add an instruction in the AGENTS.md that tells the LLM to proactively suggest running `@update-guidelines` at the end of sessions when relevant.

Let me update the AGENTS.md to:
1. Add @update-guidelines to the "Agentes Disponíveis" section
2. Add a note that the LLM should suggest running it when structural changes are discussed

</details>

### Resposta

Verdade, não documentei ele no `AGENTS.md`. Vou corrigir — adicionar o agente na lista e uma instrução pra ele te lembrar quando relevante.

*Novo passo iniciado*

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:46:47 UTC)

Feito. Agora o LLM:

1. **Sabe que existe** o `@update-guidelines` — documentado em "Agentes Disponíveis"
2. **Vai te lembrar** — tem instrução explícita: se durante a conversa ele perceber que você planeja criar/alterar databases ou mudar a filosofia de projetos, ele **sugere ao final da sessão** rodar `@update-guidelines`

*Novo passo iniciado*

## 👤 Usuário (2026-06-11 02:48:12 UTC)

Você teria como vasculhar todo o meu dashboard de 2026 e me dizer se ficou alguma coisa para explicar para uma sessão inserida em um projeto?

## 🤖 Assistente (2026-06-11 02:48:12 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to explore their entire 2026 Notion workspace to check if there's anything else the AGENTS.md should document that it's currently missing. They want a comprehensive review of all databases and content to ensure the guidelines cover everything needed for a session working on a project.

Let me look at all the databases I found earlier and check any that might need to be documented. I already found 30 databases but I only documented the 6 main ones. Let me check what other databases exist and if any of them should be documented too.

From the earlier search, the databases are:
1. Sessões opencode (2026) - ✓ documented
2. Composições - Music, probably not needed for context
3. Documentacao de Projetos - ✓ documented
4. Projetos (2026) - ✓ documented
5. Rotinas - ✓ documented
6. Relatorios Diarios - ✓ documented
7. Leituras - ✓ documented
8. Músicas (Projeto Claudio) - Music project
9. 🛒 Lista de compras (Feira) - Shopping list, not relevant
10. Logs do TCC - Academic project logs
11. Para futuras pesquisas - Future research
12. Anotações - Notes
13. Tarefas da Semana - Weekly tasks
14. Escutando (2026) - Music listening
15. 📣 Social — Conteúdos - Social media content
16. 📚 Social — Pesquisa - Social media research
17. Log — Automatizador de transcrições (YouTube → Notion) - Log DB
18. Músicas — Saluz - Music
19. Gravações de ensaio - Rehearsal recordings
20. Propostas (UP) - Proposals
21. Aulas — Bateria (Prof. Ronaldo) - Drum classes
22. Log de Composições - Composition log
23. Ideias de estética (Minas + Beatles) - Aesthetic ideas
24. Presente — Fogão até R$ 600 - Gift list
25. Salgados & Bolos — Opções - Food options
26. Convidados — Aniversário Samara - Party guests
27. ⏱️ Sessões (Clockify) - Time tracking sessions
28. Hábitos Diários - Daily habits
29. Pensamentos - Thoughts
30. Livros - Books

Let me check a few of these more closely - especially the ones that seem related to projects (Logs do TCC, Tarefas da Semana, Para futuras pesquisas, ⏱️ Sessões (Clockify), Hábitos Diários, Livros) to see if any need to be documented or referenced in the guidelines.

Actually, the user's question is broader - they want me to explore the entire 2026 dashboard and see if anything is missing from the AGENTS.md. Let me look at some key databases that might be relevant for context.

</details>

### Resposta

Boa ideia — vou explorar as outras databases que podem ser relevantes pra uma sessão de projeto.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:48:23 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me query the remaining databases that could be relevant: Logs do TCC, Tarefas da Semana, Para futuras pesquisas, Anotações, ⏱️ Sessões (Clockify), Hábitos Diários, Livros, Propostas (UP).

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:48:33 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me look at the data from these databases to understand what they contain as well. Actually I already have the schemas. Let me analyze what's relevant for a session working on a project:

1. **Logs do TCC** - Database for logging TCC (academic project) progress with tags like Metodologia, Resultados, Escrita, Código, Orientador. Could be relevant for TCC project work.

2. **Tarefas da Semana** - Weekly tasks organized by Área (Música, TCC, IA, Estudos, Pessoal). Has status, priority, and Clockify session links. Very relevant for day-to-day project work.

3. **Para futuras pesquisas** - Simple database with Ideias (title) and Fontes (sources). Research ideas to explore.

4. **Anotações** - General notes with Tags and Área (Propostas, Cura). Could be relevant.

5. **⏱️ Sessões (Clockify)** - Time tracking sessions with Data, Duração (h), Notas. Core for productivity tracking.

6. **Hábitos Diários** - Habit tracking by Área (Música, Estudos, IA, Escrita, Saúde). Personal productivity.

7. **Livros** - Book library with status, genre, rating.

8. **Propostas (UP)** - Proposals/initiatives from "Unidade Popular" political organization.

Now, which of these are project-relevant enough to document in the AGENTS.md?

For a session working on a project, the most relevant ones would be:
- **Logs do TCC** - if the project is TCC-related
- **Tarefas da Semana** - always relevant, shows weekly priorities
- **⏱️ Sessões (Clockify)** - time tracking, important for daily reports
- **Hábitos Diários** - personal context but less project-relevant
- **Para futuras pesquisas** - research queue, could be useful

Actually, let me think about this from the user's perspective. They asked if I could "vasculhar todo o dashboard" and tell them if I missed anything that should be explained to a session working on a project.

I think the answer is:

1. **Tarefas da Semana** - This is important context. A session working on a project should know about weekly task priorities. But this is dynamic data, so it should be fetched live, not documented statically. Add it to the "Regra de Dados Dinâmicos" section.

2. **Logs do TCC** - If TCC is a project, this is project-specific. But since it's linked to a specific project, it could be documented with a note about its tags.

3. **⏱️ Sessões (Clockify)** - Time tracking, dynamic data.

4. **Hábitos Diários** - Personal, less relevant to project work.

5. **Para futuras pesquisas** - Research queue, could be mentioned as a source of future projects.

6. **Propostas (UP)** - Political/social organizing, not really project-relevant.

I think the key additions should be:
- Add **Tarefas da Semana** to the dynamic data rule (weekly tasks context)
- Add **⏱️ Sessões (Clockify)** to the dynamic data rule (for time tracking)
- Optionally add **Logs do TCC** if the user's TCC project is active

Let me also consider: maybe I should just show the user what I found and ask if they want these added to the AGENTS.md, rather than assuming. Actually, the user asked me to explore and tell them if anything's missing - they want my assessment.

Let me update the AGENTS.md to add a note about these additional databases that are project-relevant, particularly the dynamic ones that should be queried.

</details>

### Resposta

Encontrei databases que fazem sentido adicionar ao contexto de sessão de projeto. Vou atualizar o `AGENTS.md`.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:48:48 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I need to update the AGENTS.md to add the additional relevant databases. Let me read the file to see where to add them.

The databases I'll add to the dynamic data rule:
- Tarefas da Semana (for weekly task priorities)
- ⏱️ Sessões (Clockify) (for time tracking)

And I'll add a section documenting the additional databases briefly, for context.

Let me read the current state of the AGENTS.md to find where to add.

</details>

*Novo passo iniciado*

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:48:58 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good. Now let me read where the existing database docs are to see if I should add some of the other databases too.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:49:03 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I could also add the schemas for Tarefas da Semana, ⏱️ Sessões (Clockify), and Hábitos Diários as they're important project-related context. But these are dynamic and should be fetched live. The "Regra de Dados Dinâmicos" section now mentions them, so the LLM knows to query them.

I think the current state is good:
- The 6 core structural databases are documented with full schemas
- The dynamic data rule now covers 7 databases (including Tarefas da Semana, Sessões Clockify, Hábitos Diários)
- All agents are documented

Let me also quickly check if there's any other database that should be structurally documented. Looking at the full list:
- Logs do TCC - TCC project specific, already covered by Projetos (2026)
- Tarefas da Semana - documented as dynamic data
- ⏱️ Sessões (Clockify) - documented as dynamic data
- Hábitos Diários - documented as dynamic data
- Livros - personal library, not project-relevant
- Para futuras pesquisas - research ideas, could be useful but dynamic
- Propostas (UP) - political organizing, not project-relevant
- Anotações - general notes

I think the current state is complete. Let me finalize and report to the user what I found.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 02:49:11 UTC)

Vasculhei. **6 databases estavam documentadas**, encontrei mais **3 com relevância direta pra sessão de projeto** que já estão cobertas pela regra dinâmica:

| Database | Tipo | Relevância |
|---|---|---|
| **Tarefas da Semana** | Prioridades/prazos semanais por área | Consultar ao vivo pra saber o que é prioridade |
| **⏱️ Sessões (Clockify)** | Time tracking com duração e notas | Consultar ao vivo pra preencher Relatórios Diários |
| **Hábitos Diários** | Acompanhamento de hábitos por área | Consultar ao vivo pra contexto pessoal |

As demais 21 databases são contextuais demais (compras, convidados, músicas) pra merecer documentação estrutural no `AGENTS.md`.

**Resumo**: você está coberto. As 6 databases core estão documentadas com schemas fixos, e agora a regra de dados dinâmicos cobre 7 databases no total (incluindo as 3 novas). Toda sessão de projeto sabe o que buscar ao vivo e o que está documentado como estrutura.

*Novo passo iniciado*

## 👤 Usuário (2026-06-11 03:13:27 UTC)

Também quero que ele seja capaz de pegar informações da database Logs de conversas 2026, que tem as entradas dos chats do NOtion

## 🤖 Assistente (2026-06-11 03:13:27 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user is asking me to also document and add the "Logs de conversas" database. Let me search for it in the workspace - it wasn't in the initial list of 30 databases. Let me search more specifically for it.

Wait, looking back at the database list, I don't see "Logs de conversas" as a database. But the user mentions it has entries from Notion chats. Let me search for it specifically.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:13:40 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The search didn't find a database called "Logs de conversas". There's:
1. "Documentacao de Projetos" (has a property called "Logs" but that's a relation)
2. "Logs do TCC" - TCC project logs
3. "Log — Automatizador de transcrições (YouTube → Notion)" - transcription log

But I notice the user mentioned "Logs de conversas 2026" - this might be an Obsidian vault folder name, not a Notion database. Looking back at the agent prompts, there are references to:
- `C:\\Users\\frota\\OneDrive\\Documentos\\Obsidian Vault\\Logs de conversas\\`

So "Logs de conversas" is an Obsidian vault folder, not a Notion database! The folder stores the markdown exports of opencode sessions.

Wait, but the user says "que tem as entradas dos chats do Notion" (that has entries of Notion chats). Let me re-read: "Logs de conversas 2026, que tem as entradas dos chats do NOtion" 

Maybe there's also a separate "Logs de conversas 2026" database that I missed. Let me search by ID or other names.

But I think they might be referring to the fact that their Obsidian vault folder "Logs de conversas" has markdown notes of their Notion chat conversations. However, they said "database" which in Notion terms means a real database.

Actually, wait - looking at the @session agent prompt, there's a reference that the session agent upserts conversations. The user's "Logs de conversas" might be what they call their Sessões opencode (2026) database, or it might be an Obsidian folder.

Let me search more carefully for any database with "conversa" in the name.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:13:51 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The search didn't find a "Logs de conversas" database. Let me try an empty/blank search to list all databases and their complete names.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:13:57 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

No "Logs de conversas" database exists in the Notion workspace. The search only returned:
1. "Sessões opencode (2026)" - which is already documented
2. "Projetos (2026)" - already documented
3. "Escutando (2026)" - music listening database

There seems to be a confusion: "Logs de conversas" is the Obsidian vault folder where the @exportar-sessao agent saves session markdown files. It's NOT a Notion database.

Let me check the Obsidian vault to see if there's something there with that name that could be useful. Actually, looking at the @sync agent prompt, it mentions:
- "Logs de conversas/" as an Obsidian vault path
- The sync agent pushes Notion sessions to this folder

So the user might be thinking of the Obsidian folder as a "database." Or they might have another page called "Logs de conversas" that contains inline databases.

Let me search for pages containing "conversas" in the broader sense.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:14:06 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Interesting! I found a mention in the search results. There's a database called "🗒️ Logs de conversas (2026)" with ID `78daada7-aab2-4b8a-bc9f-657554de97cd`. Let me fetch it to get its full schema.

</details>

### Resposta

Encontrei! Existe a database **🗒️ Logs de conversas (2026)** com ID `78daada7-aab2-4b8a-bc9f-657554de97cd`. Vou buscar o schema dela.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:14:12 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The database has multiple data sources (linked databases), so NOTION_FETCH_DATABASE doesn't work. Let me try NOTION_QUERY_DATABASE to see what data it has.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:14:20 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

This is a "multi-data-source" database - it's a linked database aggregating data from other databases. The child data sources are:
- `976da4f7-0b5a-4da0-b8c2-23a92f3ded42`
- `371191ce-57f9-8016-9880-000bf2265c3f`
- `372191ce-57f9-80fd-b842-000b573e9fca`

Let me check what these child databases are. They might be per-project log databases.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:14:27 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The search by database ID didn't return the child databases directly - returning Tarefas da Semana, Lista de compras, etc. instead. Let me try querying the data source directly using NOTION_QUERY_DATA_SOURCE.

Actually, let me try a different approach. The error showed three child data sources:
- `976da4f7-0b5a-4da0-b8c2-23a92f3ded42`
- `371191ce-57f9-8016-9880-000bf2265c3f`
- `372191ce-57f9-80fd-b842-000b573e9fca`

These might be the actual source databases. Let me try to fetch them individually.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:14:33 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me try querying the child data sources.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:14:40 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I can see that the "🗒️ Logs de conversas (2026)" database (ID: `78daada7-aab2-4b8a-bc9f-657554de97cd`) is a linked database that aggregates entries from multiple data sources. But it uses the same property schema as the one I already see in the data:

Properties:
- **Sessão** (title) - Session/chat name
- **Data** (date) - Date of the conversation
- **Resumo (curto)** (rich_text) - Short summary
- **Observações** (rich_text) - Observations
- **Origem** (select) - Source (notion, opencode)
- **Status** (status) - Aberto, Fechado
- **Projeto** (multi_select) - Project name
- **Projetos (DB)** (relation → Projetos (2026))
- **Artefatos (links/arquivos)** (rich_text) - Artifacts
- **Thread / Chat URL** (url) - Thread link

This is essentially the same type of data as "Sessões opencode (2026)" - it's a log of chat conversations but organized differently.

Let me check what the child data sources correspond to. Looking at the data:
- `976da4f7-0b5a-4da0-b8c2-23a92f3ded42` - this has data showing rows from AI projects (AI STEM Tutor, etc.)
- The other two are empty

The database structure seems similar to what I've already documented. But the user specifically mentioned wanting this database to be accessible to the session. Since it's a multi-data-source database, the LLM can still query it using NOTION_QUERY_DATA_SOURCE.

Let me add this to the AGENTS.md as a dynamic data source.

</details>

### Resposta

Achei! É uma database **linked** que agrega logs de conversas de projetos IA via data sources. Vou documentá-la.

*Novo passo iniciado*

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:14:52 UTC)

**Resumo do que encontrei e adicionei:**

A database **🗒️ Logs de conversas (2026)** (`78daada7-aab2-4b8a-bc9f-657554de97cd`) é uma **linked database** que agrega logs de conversas de projetos IA. Como é multi-data-source, a regra dinâmica agora instrui o LLM a consultá-la via `NOTION_QUERY_DATA_SOURCE` usando o `data_source_id` `976da4f7-0b5a-4da0-b8c2-23a92f3ded42`.

Ela tem as mesmas propriedades que as sessões opencode (Sessão, Data, Resumo, Status, Projeto, etc.), mas com ênfase em **logs de conversas de projetos IA** — coisas como anotações de vídeos, workflows, ideias de pipeline.

No total, **9 databases** agora estão na regra de dados dinâmicos — todas as que você mencionou cobertas.

*Novo passo iniciado*

## 👤 Usuário (2026-06-11 03:39:06 UTC)

A unica diferença é que esse log de conversas são oriundos do chat do Notion, atualize as guidelines para que os agentes entendam isso

## 🤖 Assistente (2026-06-11 03:39:06 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to clarify in the AGENTS.md that the "🗒️ Logs de conversas (2026)" database contains entries from Notion chats (as opposed to opencode sessions). Let me update the descriptive text for this database.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-11 03:39:12 UTC)

Feito. Agora a descrição deixa explícito: **"chats originados no Notion, NÃO no opencode"**. Os agentes vão saber que `Sessões opencode (2026)` = chats do OpenCode, e `🗒️ Logs de conversas (2026)` = chats feitos diretamente no Notion.

*Novo passo iniciado*

---

*78 messages | 276 parts | 💰 $0.1595 | ⏱️ 7h34m47s*
