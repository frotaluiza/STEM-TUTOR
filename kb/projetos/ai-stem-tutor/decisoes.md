# Decisões e Timeline — AI STEM Tutor — DeepTutor

**63 sessões** | **$10.05 custo total**
**238 decisões extraídas**
**33 ferramentas/tecnologias referenciadas**

## Decisões por Categoria

### Arquitetura (12)

- **Concept Extraction:** Use the existing LlamaIndex RAG pipeline + LLM to extract key concepts and relationships
- **Prompt-to-Comic**, **ComicForge**, **MythGen** — open source, LLM + imagem, pipeline completo
- **ComicMath (Khetan 2026)** — o pipeline mais próximo da nossa abordagem
- **Componentes**: `ModuleMap` e `ConceptGraph` de `@/components/learning/`
- O `RAGService` (em `deeptutor/services/rag/service.py`) orquestra qual pipeline usar baseado no provider escolhido
- **Titulo Resumido**: "Arquitetura AI STEM Tutor" (3 words, descriptive)
- **Resumo (curto)**: "Design da arquitetura do AI STEM Tutor (fork DeepTutor): Provider LLM Híbrido, Sistema de Contexto entre sessões e Timeline Visual + Roadmap."
- Ex: "Implementar pipeline RAG — Conversando com Trabalhos Longos"
- **Resumo (curto)**: "Planejamento e implementação do NoteBlocks (editor de blocos estilo Notion) no DeepTutor com terminal, sync Notion e arquitetura completa."
- **Arquitetura AI STEM Tutor** — Concluído (11/07)
- **Resumo (curto):** `Criação do subprojeto "Caminhos do xadrez" no DeepTutor: capability+agent com pipeline multi-estágio e tabuleiro interativo.`
- **Título Resumido**: "Comic Engine — Pesquisa + Pipeline Sadiku"

### Ferramentas / Stack (47)

- deeptutor/api/routers/project_state.py (###)
- **Relação Projeto 1**: A associação com AI STEM Tutor pode não ter sido efetivada via Notion API — verificar manualmente se a relação está correta na página da sessão
- **Depende de:** OpenAI, Anthropic, Cohere (APIs pagas)
- `deeptutor/` -- Backend Python (FastAPI) com motor agentico
- LLM Provider: DeepSeek (modelo `deepseek-chat`, base_url `https://api.deepseek.com`)
- "Gerar share URL (opencode serve + API)"
- Custom `deeptutor/api/routers/project_state.py` had broken import — was importing `get_runtime_settings` (doesn't exist), fixed to `get_runtime_settings_service`.
- Server now listening on port 8001, API returns sessions with existing conversations (13 sessions, 42 messages).
- They use opencode which is powered by an LLM API
- GitHub Copilot: has a monthly fee but not a general API
- For OpenAI-compatible API (which DeepTutor needs), most services are pay-per-token
- Base URL: https://api.deepseek.com
- API key: sk-6c4b96cd265f40eb94b983049bf07add
- LLM provider / base URL / API key / model
- LLM provider: openai (since DeepSeek uses OpenAI-compatible API)
  *+32 mais...*

### Modelo / LLM (3)

- **Notas:** Plataforma de aprendizado progressivo. RAG de livros didáticos → repositórios markdown. Tutor LLM que acompanha o usuário com ferramentas (Wolfram, simulações, code exec). Progressão visual: Obsidian-like nodes → mundo virtual. Junção AI STEM Tutor + Mar da Elétrica.
- Basta adicionar: se user tem tier Pro, libera modelos do pool; se BYOK, permite criar profile próprio
- **Modelos SD:** (bold as paragraph)

### Dados / KB (17)

- **PDF/Content Map**: When student uploads a PDF (to KB), generate a concept mind map showing related concepts as visual nodes (like Obsidian graph view), showing the essence of the content
- **Reassuring messages**: The user wants to hand-write custom initial messages like "Tá tudo bem, esse livro é intimidador mas ele é digerível..."
- **Trigger:** After PDF is uploaded & ingested into a KB
- "Adicionar provedor RAG para opencode/DeepTutor"
- **Docling** (IBM, MIT) como backbone de extração - ele já faz PDF → Markdown com estrutura preservada (tabelas, fórmulas, headers, captions, equações)
- **Incorporação:** `pip install docling` → converter PDF → exportar Markdown → chunk → embedding → KB
- Implementar KB _project_context auto-sync (Notion → DeepTutor)
- **LightRAG server**: delega consultas para servidor externo
- **Admin-assigned**: KBs compartilhadas por admin em multi-usuario
- **Notion Page URL:** [KB memphis-references — Ingest 12 DeepTutor PDFs](https://www.notion.so/KB-memphis-references-Ingest-12-DeepTutor-PDFs-39b191ce57f981549625e87532fb4800)
- **Decisões** with date-stamped entry about KB creation
- **Nova tarefa** na database Tarefas da Semana
- "Pode criar uma database chamada artigos"
- "Adicionar provedor RAG para opencode/DeepTutor"
- **Ferramentas open-source:** (bold as paragraph)
  *+2 mais...*

### Interface / UX (22)

- **Visualization:**
- **Frontend Component:** New `ConceptMapViewer.tsx` component + "Mind Map" tab in KB detail view
- **Batch 2** (18 blocos): Arquivos Modificados, MCP Servers Ativos, KB Memphis References
- **Batch 3** (25 blocos): Project Mind Map, Cross-Reference table, Próximos Passos, Arquivos Locais
- **Why for DeepTutor:** Converte livros-texto (Sadiku, etc.) em Markdown estruturado com tabelas, fórmulas, hierarquia de capítulos. Perfeito pro seu objetivo de "transformar livro em Notebook Markdown". Já tem chunker nativo (HierarchicalChunker, HybridChunker). Integra com LangChain/LlamaIndex. Roda 100% local.
- "Daria pra implementar um tutor literalmente \"em cima\" de arquivos" - tutor/AI STEM tutor related
- Implementar Roadmap backend + frontend (kanban de features)
- **Arquivos / Referências** listing DeepTutor and PDF details
- **Arquivos Locais** section with slug, session ID, and share URL
- **Escolha**: Implementar como nova surface no menu lateral (`/noteblocks`), sem substituir o chat existente
- Resumo (curto): "Planejamento e implementação do NoteBlocks: models, storage, router, testes, Notion sync, terminal WebSocket, e editor frontend no DeepTutor."
- Resumo (curto): {"rich_text": [{"text": {"content": "Planejamento e implementação do NoteBlocks: models, storage, router, testes, Notion sync, terminal WebSocket, e editor frontend no DeepTutor."}}]}
- **UI controls**: A "Fit" button to auto-zoom, a legend showing node color types
- **Toggle**: No built-in toggle -- it loads immediately on mount
- **Custom node components**:
  *+7 mais...*

### Outros (137)

- **Lesson Map**: When student starts a lesson (theory or exercises mode), the tutor understands the module context and creates a map that shows how the content is digestible/modularized
- **Platform philosophy**: Messages that modularize content, reduce intimidation
- **Trigger:** When student starts a lesson (selects theory/exercises mode)
- **Context:** Tutor reads the module's knowledge graph and current student progress
- **Batch 1** (24 blocos): Contexto, Decisões (Engine de parsing, Sci-Hub, Mermaid, 3 bugs)
- **Share URL**: Não foi gerado para esta sessão (nenhum share ativo no SQLite)
- **Projeto Vinculado nas tarefas**: As relações com o projeto precisam de verificação manual
- Created DeepTutor skill "pinn-executor" for automatic PINN implementation from papers
- Implemented and verified Burgers equation PINN using DeepXDE + PyTorch (Adam + L-BFGS, loss 0.0000034)
- Planned reimplementation of TCC models with hyperparameter optimization
- Created DeepTutor skill "pinn-executor" for automatic PINN implementation from papers
- Implemented and verified Burgers equation PINN using DeepXDE + PyTorch (Adam + L-BFGS, loss 0.0000034)
- Planned reimplementation of TCC models with hyperparameter optimization
- Created DeepTutor skill "pinn-executor" for automatic PINN implementation from papers
- Implemented and verified Burgers equation PINN using DeepXDE + PyTorch (Adam + L-BFGS, loss 0.0000034)
  *+122 mais...*


## Timeline de Sessões

| Data | Título | Agente | Custo | Resumo |
|------|--------|--------|-------|--------|
| 2026-07-13 | [Find nav items and page patterns (@explore subagent)](sessoes/cosmic-island.md) | explore | $0.01 |  |
| 2026-07-12 | [Explore opencode note setup (@explore subagent)](sessoes/calm-island.md) | explore |  |  |
| 2026-07-12 | [Register session in Notion (@session subagent)](sessoes/calm-nebula.md) | session | $0.01 |  |
| 2026-07-12 | [Documentar testes no Notion (@general subagent)](sessoes/calm-pixel.md) | general | $0.03 |  |
| 2026-07-12 | [Registrar sessão no Notion (@session subagent)](sessoes/clever-moon.md) | session | $0.03 |  |
| 2026-07-12 | [Sync session to Notion (@general subagent)](sessoes/crisp-river.md) | general | $0.02 |  |
| 2026-07-12 | [New session - 2026-07-12T00:04:56.367Z](sessoes/curious-forest.md) | build | $0.06 |  |
| 2026-07-12 | [Documentar teste no Notion (@general subagent)](sessoes/eager-cabin.md) | general | $0.03 |  |
| 2026-07-12 | [Rodar front e back do Deep Tutor](sessoes/glowing-mountain.md) | build | $0.01 |  |
| 2026-07-12 | [Register session in Notion (@general subagent)](sessoes/glowing-wizard.md) | general | $0.01 |  |
| 2026-07-12 | [Run @session to push live doc (@session subagent)](sessoes/glowing-wolf.md) | session |  |  |
| 2026-07-12 | [Post test report to Notion (@general subagent)](sessoes/hidden-circuit.md) | general | $0.02 |  |
| 2026-07-12 | [Explore DeepTutor test structure (@explore subagent)](sessoes/hidden-garden.md) | explore |  |  |
| 2026-07-12 | [Rodar @session para esta sessão (@session subagent)](sessoes/jolly-engine.md) | session | $0.01 |  |
| 2026-07-12 | [@session final para esta sessão (@session subagent)](sessoes/lucky-engine.md) | session | $0.02 |  |
| 2026-07-12 | [Explore DeepTutor test setup (@explore subagent)](sessoes/lucky-mountain.md) | explore | $0.01 |  |
| 2026-07-12 | [Research Sci-Hub MCP (@explore subagent)](sessoes/neon-moon.md) | explore | $0.01 |  |
| 2026-07-12 | [Explore project-manager code (@explore subagent)](sessoes/nimble-forest.md) | explore | $0.02 |  |
| 2026-07-12 | [NoteBlocks - Implementacao completa + Roadmap Memphis](sessoes/playful-forest.md) | build | $1.55 |  |
| 2026-07-12 | [Explore DeepTutor frontend nav (@explore subagent)](sessoes/playful-rocket.md) | explore | $0.01 |  |
| 2026-07-12 | [Explore mind-map-module changes (@explore subagent)](sessoes/quick-panda.md) | explore |  |  |
| 2026-07-12 | [Nova entrada no STEM TUTOR](sessoes/quiet-pixel.md) | build | $0.10 |  |
| 2026-07-12 | [Registrar sessão no Notion (@session subagent)](sessoes/shiny-cabin.md) | session | $0.02 |  |
| 2026-07-12 | [Explore Deeptutor project (@explore subagent)](sessoes/shiny-eagle.md) | explore |  |  |
| 2026-07-12 | [Notion Projetos 2026 page ID lookup](sessoes/shiny-tiger.md) | plan | $0.01 |  |
| 2026-07-12 | [Explore DeepTutor KB/navigation (@explore subagent)](sessoes/stellar-meadow.md) | explore | $0.03 |  |
| 2026-07-12 | [Explore HKU codebase structure (@explore subagent)](sessoes/sunny-cactus.md) | explore |  |  |
| 2026-07-12 | [Survey all projects in sessions (@explore subagent)](sessoes/sunny-moon.md) | explore | $0.01 |  |
| 2026-07-12 | [Documentar ciclo de testes no Notion (@general subagent)](sessoes/swift-nebula.md) | general | $0.03 |  |
| 2026-07-12 | [@session para playful-forest (@session subagent)](sessoes/swift-tiger.md) | session | $0.01 |  |
| 2026-07-12 | [Testar @session START flow (@session subagent)](sessoes/witty-cabin.md) | session | $0.00 |  |
| 2026-07-12 | [Integração OpenCode STEM TUTOR](sessoes/witty-wizard.md) | build | $0.24 |  |
| 2026-07-11 | [New session - 2026-07-11T15:06:05.342Z](sessoes/calm-canyon.md) | build | $1.10 |  |
| 2026-07-11 | [DeepTutor KB API + Learning Space (@explore subagent)](sessoes/happy-engine.md) | explore |  |  |
| 2026-07-11 | [Explore LLM service layer (@explore subagent)](sessoes/hidden-river.md) | explore |  |  |
| 2026-07-11 | [Register session in Notion (@session subagent)](sessoes/hidden-sailor.md) | session |  |  |
| 2026-07-11 | [Register session in Notion (@session subagent)](sessoes/kind-harbor.md) | session |  |  |
| 2026-07-11 | [New session - 2026-07-11T20:59:17.530Z](sessoes/playful-mountain.md) | build | $0.71 |  |
| 2026-07-11 | [Explore STEM TUTOR project (@explore subagent)](sessoes/playful-wolf.md) | explore |  |  |
| 2026-07-11 | [New session - 2026-07-11T20:45:32.087Z](sessoes/shiny-wolf.md) | plan | $0.42 |  |
| 2026-07-11 | [Explore DeepTutor codebase (@explore subagent)](sessoes/swift-canyon.md) | explore |  |  |
| 2026-07-08 | [Explore tutor stem project (@explore subagent)](sessoes/hidden-orchid.md) | explore |  |  |
| 2026-07-02 | [Registrar sessão no Notion (@session subagent)](sessoes/silent-moon.md) | session | $0.01 |  |
| 2026-07-01 | [Explore web frontend viewers (@explore subagent)](sessoes/clever-lagoon.md) | explore | $0.02 |  |
| 2026-07-01 | [Explore DeepTutor project (@explore subagent)](sessoes/eager-squid.md) | explore | $0.01 |  |
| 2026-07-01 | [Novo projeto Caminhos do Xadrez](sessoes/glowing-panda.md) | build | $0.04 |  |
| 2026-07-01 | [RAG primeiros capítulos tese Ingrid no DeepTutor](sessoes/lucky-island.md) | build | $2.33 |  |
| 2026-07-01 | [Explore TUTOR project structure (@explore subagent)](sessoes/nimble-garden.md) | explore | $0.01 |  |
| 2026-06-25 | [Tarefa testes IA retroativos Deep Tutor](sessoes/swift-planet.md) | plan | $0.01 |  |
| 2026-06-21 | [Últimas entradas deeptutor no Notion](sessoes/cosmic-rocket.md) | build | $2.58 |  |
| 2026-06-17 | [DeepTutor KB and RAG analysis (@explore subagent)](sessoes/misty-canyon.md) | explore | $0.02 |  |
| 2026-06-17 | [Explore DeepTutor codebase (@explore subagent)](sessoes/misty-comet.md) | explore | $0.02 |  |
| 2026-06-17 | [Register session in Notion (@session subagent)](sessoes/witty-rocket.md) | session | $0.02 |  |
| 2026-06-16 | [Explore STEM TUTOR project (@explore subagent)](sessoes/crisp-canyon.md) | explore | $0.01 |  |
| 2026-06-16 | [Register session in Notion (@session subagent)](sessoes/crisp-planet.md) | session | $0.02 |  |
| 2026-06-16 | [STEM TUTOR: engenharia elétrica em quadrinhos](sessoes/gentle-engine.md) | build | $0.20 |  |
| 2026-06-16 | [Failed to fetch no deeptutor](sessoes/shiny-nebula.md) | build | $0.03 |  |
| 2026-06-16 | [Explore DeepTutor web codebase (@explore subagent)](sessoes/witty-lagoon.md) | explore | $0.01 |  |
| 2026-06-15 | [Register session in Notion (@session subagent)](sessoes/cosmic-cabin.md) | session | $0.01 |  |
| 2026-06-15 | [Add voice input to DeepTutor (@explore subagent)](sessoes/cosmic-falcon.md) | explore | $0.01 |  |
| 2026-06-15 | [Chat para instalação DeepTutor](sessoes/eager-nebula.md) | build | $0.14 |  |
| 2026-06-15 | [Explore chat message flow (@explore subagent)](sessoes/happy-mountain.md) | explore | $0.02 |  |
| 2026-06-02 | [Find leitura individual files (@explore subagent)](sessoes/nimble-falcon.md) | explore |  |  |
