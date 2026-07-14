# Decisões e Timeline — Notion Infrastructure

**76 sessões** | **$4.00 custo total**
**176 decisões extraídas**
**33 ferramentas/tecnologias referenciadas**

## Decisões por Categoria

### Arquitetura (5)

- **Linha 24:** `Pipeline com validação cruzada (prática ainda ausente em estudos similares de hibridização físico-dados)`
- **Pipeline de IA**: resumos automáticos das notícias
- Qual arquitetura híbrida usaram (residual, feature-based, loss regularization, etc.)
- **Blocks 200-296**: Sections 13-25 (ML fundamentals, Model families, Pipeline, CV, HPO, Architectures, Results, Conclusions)
- **Documentação de Projetos** — docs técnicos/arquiteturais

### Ferramentas / Stack (26)

- **Contexto:** Sem API OpenAI disponível, optou-se por transcrição local.
- **DeepTutor** existe em `C:\Users\frota\Documents\Projetos\AI TUTOR` — Next.js 16 + FastAPI + Python, sua plataforma de tutoria com chat, RAG e agentes
- `deeptutor/core/agentic/` - agent loop framework
- Option B: Build the agent directly in DeepTutor (reusing existing agentic framework)
- Or implement direct Notion API calls in Python
- Cons: Tight coupling, hard to maintain, opencode was not designed as an API
- Reuses DeepTutor's existing agent framework, tool system, sandbox
- **Framework de agentes** (`deeptutor/core/agentic/`) com tool protocol
- `POST https://api.composio.dev/api/v1/actions/{action_id}/execute`
- **Scraping automático** de várias fontes:
- Pesquisar framework de curadoria de fontes
- Database: Fontes (nome, tipo, URL, categoria, frequência de scraping)
- happy-engine (ses_0accc1c27ffeXIbYyoYsvpaApo) - DeepTutor KB API
- Documented: Diretriz (title), Projeto (relation), Framework (select), Fase Atual (rich_text), Prioridade (select), Diretrizes (rich_text), Ultima Atualizacao (date)
- They use Composio (MCP) for Notion integration - the MCP server handles it via `x-api-key`
  *+11 mais...*

### Modelo / LLM (9)

- **Ferramenta:** `faster-whisper` com modelo `small` (244M parâmetros) para primeiro chunk, `base` para chunks restantes.
- **Blocks 100-200**: Sections 6-12 (V-AGMD, Motivação, Abordagens, Panorama, Lacunas, Princípios, Modelo 0D)
- **Title**: Surrogate do modelo 0D (from SQLite)
- **Resumo curto**: "Documentação técnica do surrogate MLP regularizado para substituir o modelo 0D em C por uma rede neural diferenciável em TensorFlow."
- **Título Resumido**: "Surrogate MLP do modelo 0D"
- **⚠️ Embedding**: precisa configurar em **Settings > Catalog** no DeePTutor (nenhum modelo ativo ainda)
- **Criar/modificar o agente `session`** para extrair mensagens do SQLite e preencher o corpo da página corretamente, além de gerar um título resumido via LLM
- **Tabela de metadados** (título, modelo, custo, tokens)
- **AI tools for STEM learning:** ChatGPT vs Claude (Skill Leap AI), STEM AI for educators (STEMconnector).

### Dados / KB (10)

- **Alternativas:** Extrair samples do banco SQLite do aup3 vs usar .m4a exportado automaticamente.
- **Resultado:** Transcrição completa salva em `transcricao_reuniao_08-06-2026.txt` (85.9 KB, 1096 linhas).
- **Linha 38 (note):** `uso de validação cruzada — prática sistematicamente ausente na literatura de hibridização físico-dados para MD`
- **Finished** - checkbox
- **Notion como backend** - databases para logs, categorização
- **Parent**: Tarefas da Semana database (`1d7bec7f-09b7-459b-89cc-01de4b71ec9d`)
- **Livro de Visitas**: mensagens salvas no `localStorage` + **Cbox chat ao vivo**
- **Rotinas** — automações/scripts agendados
- **Banco de dados:** Sessões opencode (2026)
- **Banco de dados:** Logs do TCC (`967e26df-6102-413f-b776-2b7de27eea68`)

### Interface / UX (9)

- **Geopolítica** (1º priority) - fontes: YouTube, podcasts, Reddit, artigos, pesquisadores específicos (Thiago Machado)
- **Pesquisas/Explorações**: What was researched
- **Blocks 297-299**: Footer (Arquivos Locais with source path and DB info)
- **Pra se guiar**: índice de documentação HTML/CSS/JS com links âncora
- **KB `html-guide`**: raw documents em `docs-html/`
- **Notebook `html-guide`**: criado com 15 registros (um por documento)
- **Portátil / explícito**: manter uma pasta `~/opencode-guidelines/` e iniciar o opencode com `OPENCODE_CONFIG_DIR` quando você quiser forçar aquele conjunto (ou usar um alias no shell)
- Sessao dedicada a editar slides de contribuicoes e criar sistema de logging duplo
- Resumo (curto) (rich_text): "Sessão para aprimorar slides de contribuições do TCC com foco em dessalinização e criar sistema de logging duplo com watcher"

### Outros (117)

- **Contexto:** O áudio da reunião estava em formato .aup3 (projeto Audacity).
- **Escolha:** Usar `Gravando (4).m4a` (260 MB, mesmo conteúdo) por ser formato padrão suportado pelo ffmpeg.
- **Problema:** Out of memory ao processar áudio completo (2h50). Solução: split em chunks de 30 min.
- **Sessão**: "Transcrever reunião e criar plano — Introdução TCC"
- **Resumo (curto)**: "Transcrição de 2h50 de reunião sobre apresentação TCC + plano de implementação para introdução e slides"
- **Título Resumido**: "Transcrever reunião + plano introdução"
- **OpenCode** tem todo o ecossistema de sessões, live docs, agents `@session`/`@sync` via Composio → Notion
- **NoteBlocks** seria implementado **dentro do DeepTutor**, estendendo-o para ser seu workspace diário de anotações + terminal
- **Sandbox de execução** (`deeptutor/services/sandbox/`) para rodar código Python com segurança
- "Criar/abrir o doc vivo" - but I'm in Plan Mode, so I can't create files
- **Title** - title (video name)
- **Link** - url (YouTube link)
- **Note** - rich_text
- **Status** - select (To Learn, In Progress, Completed)
- **Tags** - multi_select (content creator names, various YouTubers)
  *+102 mais...*


## Timeline de Sessões

| Data | Título | Agente | Custo | Resumo |
|------|--------|--------|-------|--------|
| 2026-07-12 | [New session - 2026-07-12T00:23:03.700Z](sessoes/clever-garden.md) | build | $1.47 |  |
| 2026-07-12 | [Criar database Test Reports Notion (@general subagent)](sessoes/cosmic-eagle.md) | general | $0.02 |  |
| 2026-07-12 | [Verify Ansari2022 and read new paper (@general subagent)](sessoes/crisp-mountain.md) | general |  |  |
| 2026-07-12 | [Criar database Fontes Projetos Notion (@general subagent)](sessoes/crisp-squid.md) | general | $0.03 |  |
| 2026-07-12 | [Criar database Test Reports no Notion (@general subagent)](sessoes/glowing-garden.md) | general | $0.04 |  |
| 2026-07-12 | [Upload 25 fixed-encoding sessions (@session subagent)](sessoes/glowing-nebula.md) | session | $0.06 |  |
| 2026-07-12 | [Generate detailed live docs (@general subagent)](sessoes/jolly-otter.md) | general | $0.03 |  |
| 2026-07-12 | [Upload 25 analyzed sessions (@session subagent)](sessoes/mighty-meadow.md) | session | $0.08 |  |
| 2026-07-12 | [Upload 25 live docs to Notion (@session subagent)](sessoes/misty-planet.md) | session | $0.07 |  |
| 2026-07-12 | [Register PM-1 test report (@general subagent)](sessoes/neon-wizard.md) | general | $0.00 |  |
| 2026-07-12 | [Criar database Relatórios de Testes 2026](sessoes/quick-canyon.md) | plan | $0.01 |  |
| 2026-07-12 | [Upload 25 reformatted sessions (@session subagent)](sessoes/shiny-canyon.md) | session | $0.03 |  |
| 2026-07-12 | [Reformat sessions using opencode export (@general subagent)](sessoes/stellar-engine.md) | general | $0.02 |  |
| 2026-07-12 | [Upload reformatted sessions via @session (@session subagent)](sessoes/tidy-comet.md) | session | $0.06 |  |
| 2026-07-11 | [Check live doc and AGENTS.md (@explore subagent)](sessoes/quick-nebula.md) | explore |  |  |
| 2026-07-08 | [New session - 2026-07-08T18:28:28.478Z](sessoes/curious-canyon.md) | build |  |  |
| 2026-07-08 | [New session - 2026-07-08T18:40:15.135Z](sessoes/curious-engine.md) | build |  |  |
| 2026-06-30 | [Registrar sessão no Notion (@session subagent)](sessoes/neon-nebula.md) | session | $0.02 |  |
| 2026-06-28 | [Update Notion with new roteiro (@session subagent)](sessoes/clever-rocket.md) | session | $0.00 |  |
| 2026-06-28 | [Central de notícias no Notion](sessoes/curious-meadow.md) | build | $0.02 |  |
| 2026-06-28 | [Update Notion with new roteiro (@session subagent)](sessoes/happy-island.md) | session | $0.03 |  |
| 2026-06-28 | [Explore Notion news project (@explore subagent)](sessoes/kind-nebula.md) | explore | $0.02 |  |
| 2026-06-28 | [Update Notion with roteiro.md (@session subagent)](sessoes/witty-otter.md) | session | $0.05 |  |
| 2026-06-27 | [Registrar sessão no Notion (@session subagent)](sessoes/eager-wolf.md) | session | $0.01 |  |
| 2026-06-27 | [Update TCC log in Notion (@session subagent)](sessoes/misty-star.md) | session | $0.02 |  |
| 2026-06-27 | [Find Logs TCC database (@session subagent)](sessoes/nimble-star.md) | session | $0.03 |  |
| 2026-06-22 | [Find article by PII number (@general subagent)](sessoes/witty-knight.md) | general | $0.01 |  |
| 2026-06-17 | [Find Sadiku PDF download (@general subagent)](sessoes/calm-sailor.md) | general | $0.00 |  |
| 2026-06-17 | [Verify AndresManas 2023 V-AGMD (@general subagent)](sessoes/crisp-forest.md) | general | $0.02 |  |
| 2026-06-17 | [Research academic papers (@general subagent)](sessoes/curious-cabin.md) | general | $0.01 |  |
| 2026-06-17 | [Verify Yang 2023 AGMD (@general subagent)](sessoes/eager-wizard.md) | general | $0.01 |  |
| 2026-06-17 | [Verify Lisboa variables (@general subagent)](sessoes/gentle-cactus.md) | general | $0.01 |  |
| 2026-06-17 | [Verify Khayet 2012 AGMD (@general subagent)](sessoes/gentle-circuit.md) | general | $0.01 |  |
| 2026-06-17 | [Search hybrid architectures AGMD (@general subagent)](sessoes/happy-wizard.md) | general | $0.02 |  |
| 2026-06-17 | [Research comic/visual tools (@general subagent)](sessoes/hidden-cabin.md) | general | $0.01 |  |
| 2026-06-17 | [Research technical diagram OCR (@general subagent)](sessoes/jolly-pixel.md) | general | $0.02 |  |
| 2026-06-17 | [Verify Kim 2022 V-AGMD (@general subagent)](sessoes/lucky-canyon.md) | general | $0.00 |  |
| 2026-06-17 | [Verify Lisboa 2024 V-AGMD (@general subagent)](sessoes/mighty-comet.md) | general | $0.01 |  |
| 2026-06-17 | [Compare V-AGMD papers (@general subagent)](sessoes/quick-harbor.md) | general | $0.01 |  |
| 2026-06-17 | [Verify Jawed 2025 AGMD (@general subagent)](sessoes/shiny-mountain.md) | general | $0.01 |  |
| 2026-06-17 | [Verify Khalifa 2017 AGMD (@general subagent)](sessoes/shiny-squid.md) | general | $0.01 |  |
| 2026-06-17 | [Verify Shirazian 2017 AGMD (@general subagent)](sessoes/silent-island.md) | general | $0.01 |  |
| 2026-06-17 | [Read Ibnouf2024 AI review (@general subagent)](sessoes/sunny-pixel.md) | general | $0.02 |  |
| 2026-06-17 | [Find Requena 2023 paper PDF (@general subagent)](sessoes/sunny-sailor.md) | general | $0.01 |  |
| 2026-06-17 | [Extend V-AGMD comparison table (@general subagent)](sessoes/swift-river.md) | general | $0.01 |  |
| 2026-06-17 | [Verify Abdulrahim 2026 AGMD (@general subagent)](sessoes/tidy-pixel.md) | general | $0.01 |  |
| 2026-06-17 | [Deep search technical image VLMs (@general subagent)](sessoes/witty-nebula.md) | general | $0.02 |  |
| 2026-06-17 | [Research DeepSeek embedding models (@general subagent)](sessoes/witty-planet.md) | general | $0.00 |  |
| 2026-06-16 | [Template anos 2000 Site do Pão](sessoes/proud-engine.md) | build | $0.07 |  |
| 2026-06-15 | [Research COPPE project article (@general subagent)](sessoes/clever-engine.md) | general | $0.00 |  |
| 2026-06-15 | [Register session in Notion (@session subagent)](sessoes/swift-cabin.md) | session | $0.01 |  |
| 2026-06-14 | [Registrar sessão no Notion (@session subagent)](sessoes/calm-garden.md) | session | $0.01 |  |
| 2026-06-11 | [Explore Notion DBs and local vault (@explore subagent)](sessoes/clever-planet.md) | explore | $0.01 |  |
| 2026-06-11 | [Converter checkboxes não marcados em tarefas](sessoes/glowing-comet.md) | plan | $0.00 |  |
| 2026-06-11 | [Assistente semanal e diário de tarefas](sessoes/glowing-engine.md) | build | $0.14 |  |
| 2026-06-11 | [Extract Notion tools from file (@explore subagent)](sessoes/hidden-comet.md) | explore | $0.00 |  |
| 2026-06-11 | [Rodar @update-guidelines (@update-guidelines subagent)](sessoes/lucky-comet.md) | update-g | $0.04 |  |
| 2026-06-11 | [New session - 2026-06-11T13:36:32.132Z](sessoes/mighty-garden.md) | plan | $0.00 |  |
| 2026-06-11 | [Projetos IA e ecossistema guidelines](sessoes/quick-star.md) | plan | $0.01 |  |
| 2026-06-10 | [Alterar código agente backup Notion](sessoes/quick-forest.md) | build | $1.19 |  |
| 2026-06-10 | [Guidelines globais no OpenCode](sessoes/shiny-comet.md) | build | $0.16 |  |
| 2026-06-10 | [Find Notion backup agents (@explore subagent)](sessoes/witty-meadow.md) | explore |  |  |
| 2026-06-04 | [Buscar sessão sobre database de rotinas (@explore subagent)](sessoes/happy-eagle.md) | explore |  |  |
| 2026-06-04 | [Sessão sobre database de rotinas](sessoes/lucky-circuit.md) | build | $0.01 |  |
| 2026-06-02 | [Research Mathpix alternatives (@general subagent)](sessoes/clever-cactus.md) | general |  |  |
| 2026-06-02 | [Search YouTube STEM tools (@general subagent)](sessoes/shiny-wizard.md) | general |  |  |
| 2026-06-02 | [Search GitHub STEM tool projects (@general subagent)](sessoes/swift-orchid.md) | general |  |  |
| 2026-06-02 | [Search Reddit STEM tool forums (@general subagent)](sessoes/tidy-river.md) | general |  |  |
| 2026-06-01 | [Log session to Notion (@session subagent)](sessoes/cosmic-meadow.md) | session |  |  |
| 2026-06-01 | [Log session to Notion (@session subagent)](sessoes/crisp-nebula.md) | session |  |  |
| 2026-06-01 | [New session - 2026-06-01T20:38:48.987Z](sessoes/curious-island.md) | build |  |  |
| 2026-06-01 | [New session - 2026-06-01T20:43:03.866Z](sessoes/hidden-pixel.md) | build |  |  |
| 2026-06-01 | [Test sync agent (@sync subagent)](sessoes/proud-eagle.md) | sync |  |  |
| 2026-06-01 | [Test session logging agent (@session subagent)](sessoes/silent-lagoon.md) | session |  |  |
| 2026-06-01 | [Test session logging (@session subagent)](sessoes/sunny-circuit.md) | session |  |  |
| 2026-05-31 | [New session - 2026-05-31T02:37:00.217Z](sessoes/witty-moon.md) | build |  |  |
