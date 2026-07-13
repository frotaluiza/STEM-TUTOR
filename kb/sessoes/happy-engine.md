---
slug: happy-engine
title: "DeepTutor KB API + Learning Space (@explore subagent)"
date: 2026-07-11
agent: explore
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h01m25s
messages: 11
parts: 80
cost: 0
tokens_input: 84381
tokens_output: 7069
tokens_reasoning: 528
tokens_cache_read: 526208
tokens_cache_write: 0
created: "2026-07-11 22:02:17 UTC"
updated: "2026-07-11 22:03:43 UTC"
---

Sessão com **11 messages**, **80 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | 💾 cache read: 526.2K | ⏱️ 0h01m25s

## 👤 Usuário (2026-07-11 22:02:17 UTC)

Explore the DeepTutor codebase at C:\Users\frota\Documents\Projetos\AI TUTOR\ to understand:

1. Knowledge Base API: Read deeptutor/api/ - list all files, then read the knowledge router(s) if they exist. I need to see how KBs are created, updated, and queried via REST API.

2. Learning Space: Read web/app/space/ directory recursively. Look at how the Learning Space pages are structured (React components). I need to understand the frontend architecture - is it a single page? Multiple routes? What components exist?

3. Capabilities: Look at deeptutor/capabilities/ README or __init__.py to understand how capabilities work and if there's a "project" or "roadmap" capability.

4. Knowledge ingestion: Check deeptutor/knowledge/ - look for any ingestion pipeline (ingest_textbook.py calls something in the backend).

5. Learning Space frontend: Read web/app/space/learning/page.tsx to see the main learning page structure.

Return the full content of the knowledge API router, the learning space page structure, and any relevant knowledge ingestion code.

## 🤖 Assistente (2026-07-11 22:02:17 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to explore a DeepTutor codebase thoroughly. Let me start by understanding the directory structure and then dive into the specific areas they've asked about.

Let me begin with multiple parallel searches to be efficient.

</details>

### Resposta

I'll start by exploring the directory structure broadly, then dive into each specific area.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 22:02:21 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The glob for web/app/space/ didn't find files or had an error. Let me try with a different path approach.

</details>

### Resposta

Let me now read the key files in parallel. The glob for `web/app/space` failed - let me check what's in the `web/` directory first.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 22:02:25 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The glob for `web/app/space` failed. Let me check if there's a `space` directory under `web/` or `web/app/`. Looking at the web directory, there's `app/` and `components/`. Let me look at those.

</details>

### Resposta

Now let me read the rest of the knowledge.py file (it was truncated) and explore the web frontend structure:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 22:02:30 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have the knowledge.py file (truncated at line 2635) and the full web/app directory listing. I see there is a `space` directory at `(utility)/space/`. Let me read the relevant files:

1. The rest of knowledge.py (from line 2636)
2. The space page files: `(utility)/space/page.tsx`, `(utility)/space/layout.tsx`, `(utility)/space/learning/page.tsx`
3. The capabilities registry/protocol files
4. Check for any `ingest_textbook.py` file in the knowledge directory

Let me also check the remaining portion of knowledge.py and the space pages.

</details>

### Resposta

Now let me read the remaining knowledge.py, the space/learning page, and other key files:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 22:02:37 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me also look at:
1. The SpaceMain component and SpaceDashboard component
2. The capabilities registry to understand how capabilities are registered
3. Look for any "project" or "roadmap" capability
4. Check if there's an ingest_textbook.py or similar file in the project

</details>

### Resposta

Let me now look at the SpaceMain/SpaceDashboard components and the capabilities registry:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 22:02:41 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the SpaceMain and SpaceDashboard components, and the ingest_textbook.py script.

</details>

### Resposta

Let me read the key components and the ingestion script:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 22:02:45 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me also check the web/app/(workspace)/home page to understand the main chat routing, and also look at the web/app/(utility)/space/chat-history, skills, questions, notebooks, personas pages to complete the picture of the Learning Space.

</details>

### Resposta

Let me check the remaining space sub-pages and the workspace layout to complete the architecture picture:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 22:02:52 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive understanding of the DeepTutor codebase. Let me compile all the findings into a thorough report. Let me also check if there are any "project" or "roadmap" related capabilities.

</details>

### Resposta

Let me check one more thing -- the capabilities settings router and any "project" references:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 22:02:57 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive understanding of the DeepTutor codebase. Let me compile the report. Let me also quickly check the workspace home page to understand the main chat interface for completeness, since it's part of the overall frontend architecture.

</details>

### Resposta

Let me read the main workspace home page (chat interface) to complete the frontend picture:

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 22:03:02 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive understanding of the DeepTutor codebase. Let me compile the full report covering all 5 areas requested by the user.

</details>

### Resposta

Aqui esta o relatorio completo com todas as descobertas sobre o codigo-fonte do DeepTutor.

---

## 1. Knowledge Base API Router

**Arquivo:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\api\routers\knowledge.py` (2761 linhas)

Este e o roteador REST mais complexo da aplicacao, montado em `/api/v1/knowledge`. Ele gerencia todo o ciclo de vida das bases de conhecimento (KBs).

### Rotas da API REST

| Metodo | Rota | Funcao |
|--------|------|--------|
| `GET` | `/health` | Health check do subsistema de KB |
| `GET` | `/rag-providers` | Lista provedores RAG disponiveis (llamaindex, pageindex, graphrag, lightrag) |
| `PUT` | `/rag-providers/{provider}/mode` | Define o modo de recuperacao padrao de um engine |
| `GET` | `/rag-pipelines/{provider}/config` | Le configuracoes do pipeline (API key, knobs) |
| `PUT` | `/rag-pipelines/{provider}/config` | Atualiza configuracoes do pipeline |
| `GET` | `/rag-pipelines/{provider}/preflight` | Verifica se o provider pode rodar no ambiente atual |
| `GET` | `/rag-pipelines/model-options` | Lista modelos (llm/embedding) disponiveis |
| `PUT` | `/rag-pipelines/active-model` | Alterna o modelo ativo globalmente |
| `GET` | `/supported-file-types` | Politica de upload (extensoes, tamanho maximo) |
| `GET` | `/configs` | Todas as configs de KB |
| `POST` | `/configs/sync` | Sincroniza configs dos arquivos metadata.json |
| `GET` | `/{kb_name}/config` | Config de uma KB especifica |
| `PUT` | `/{kb_name}/config` | Atualiza config de uma KB (ex: trocar rag_provider) |
| `GET` | `/list` | Lista todas as KBs visiveis (com info detalhada, status, estatisticas) |
| `GET` | `/default` | Retorna a KB padrao |
| `PUT` | `/default/{kb_name}` | Define a KB padrao |
| `POST` | `/create` | **Cria uma nova KB** (multipart: nome + arquivos + provedor) |
| `GET` | `/{kb_name}` | Detalhes de uma KB especifica |
| `DELETE` | `/{kb_name}` | **Deleta uma KB** |
| `POST` | `/{kb_name}/upload` | **Upload de arquivos** para uma KB existente (processamento em background) |
| `POST` | `/{kb_name}/reindex` | **Re-indexa** uma KB (versiona por configuracao de embedding) |
| `POST` | `/{kb_name}/retry` | **Retry** de uma KB que falhou |
| `GET` | `/{kb_name}/files` | Lista arquivos raw de uma KB |
| `GET` | `/{kb_name}/files/{filename}` | Download/preview de arquivo raw |
| `DELETE` | `/{kb_name}/files/{filename}` | Deleta arquivo raw |
| `GET` | `/{kb_name}/file-preview-text/{filename}` | Texto extraido para preview |
| `POST` | `/{kb_name}/folders` | Cria pasta organizacional em raw/ |
| `POST` | `/{kb_name}/files/move` | Move arquivo/pasta entre pastas |
| `POST` | `/{kb_name}/link-folder` | Vincula pasta local a KB |
| `GET` | `/{kb_name}/linked-folders` | Lista pastas vinculadas |
| `DELETE` | `/{kb_name}/linked-folders/{folder_id}` | Desvincula pasta |
| `POST` | `/{kb_name}/sync-folder/{folder_id}` | Sincroniza pasta vinculada |
| `GET` | `/{kb_name}/progress` | Progresso da inicializacao |
| `POST` | `/{kb_name}/progress/clear` | Limpa progresso travado |
| `WS` | `/{kb_name}/progress/ws` | WebSocket de progresso em tempo real |
| `GET` | `/tasks/{task_id}/stream` | SSE de logs de tarefa |
| `POST` | `/connect-obsidian` | Conecta vault Obsidian como KB |
| `POST` | `/probe-folder` | Inspeciona pasta antes de vincular |
| `POST` | `/connect-folder` | Monta indice existente como KB read-only |
| `POST` | `/probe-lightrag-server` | Testa conexao com servidor LightRAG |
| `POST` | `/connect-lightrag-server` | Conecta servidor LightRAG externo |

### Criacao de KB (POST /create)

O fluxo e:
1. Valida nome, provedor e arquivos
2. Registra KB em `kb_config.json` com status `initializing`
3. Cria `KnowledgeBaseInitializer` que monta a estrutura de diretorios
4. Salva arquivos em `<kb>/raw/`
5. Dispara `run_initialization_task` em background que chama `initializer.process_documents()`
6. O background task usa `RAGService.initialize()` para indexar pelo provider escolhido
7. Atualiza status para `ready` ou `error`

### Upload de arquivos (POST /{kb_name}/upload)

1. Valida provedor contra o binding da KB
2. Salva arquivos em `<kb>/raw/` (com suporte a pastas organizacionais)
3. Dispara `run_upload_processing_task` em background
4. Usa `DocumentAdder.add_documents()` + `process_new_documents()` para indexar incrementalmente
5. Deduplica por hash SHA-256 do conteudo

### Arquitetura de Conexao de KBs

O roteador suporta **5 tipos de KB**:
- **Local** (padrao): cria diretorio em `data/knowledge_bases/`
- **Obsidian vault**: ponteiro read-only para vault do Obsidian
- **Linked folder**: monta indice existente de outro engine
- **LightRAG server**: delega consultas para servidor externo
- **Admin-assigned**: KBs compartilhadas por admin em multi-usuario

---

## 2. Learning Space (Frontend)

### Arquitetura Geral

O frontend e uma aplicacao **Next.js** com roteamento baseado em sistema de arquivos (App Router). Ha **4 grupos de layout**:

```
web/app/
  globals.css
  layout.tsx                    # Layout raiz (html, body, providers)
  (auth)/                       # layout.tsx + login + register
  (admin)/                      # layout.tsx (admin)
  (utility)/                    # layout.tsx + todas as paginas "utilitarias"
    space/                      # *** LEARNING SPACE ***
      layout.tsx                # Usa SpaceMain como wrapper
      page.tsx                  # SpaceDashboard (hub central)
      learning/page.tsx         # Mastery Path
      chat-history/page.tsx     # Historico de conversas
      notebooks/page.tsx        # Notebooks
      questions/page.tsx        # Banco de questoes
      skills/page.tsx           # Skills
      personas/page.tsx         # Personas
    knowledge/page.tsx
    settings/...                # ~15 paginas de configuracao
    memory/...                  # Memoria L1, L2, L3
    notebook/page.tsx
    profile/page.tsx
    agents/page.tsx
  (workspace)/                  # layout com sidebar + UnifiedChatProvider
    layout.tsx                  # CapabilityAccessProvider + UnifiedChatProvider + WorkspaceSidebar
    page.tsx                    # Redireciona para /home
    home/[[...sessionId]]/page.tsx  # Chat principal (2190 linhas)
    book/...                    # Reader de livros
    partners/...                # Gerenciamento de partners
    co-writer/...               # Co-Writer
    playground/page.tsx        # Playground
```

### Componentes do Learning Space

**`SpaceMain.tsx`** (`web/components/space/SpaceMain.tsx`):
- Layout wrapper que decide entre layout **full-bleed** (para `/space/learning`) ou layout **centralizado com max-w-5xl** (para as demais secoes)
- Exibe um link "Voltar ao Learning Space" quando em sub-paginas
- Usa o padrao **hub-and-spoke**: o dashboard (`/space`) e o unico navegador; secoes nao tem navegacao lateral propria

**`SpaceDashboard.tsx`** (`web/components/space/SpaceDashboard.tsx`):
- Pagina inicial do Learning Space (`/space`)
- Exibe cards em 2 grupos:
  1. **Conversations & Materials**: Chat History, Notebooks, Question Bank
  2. **Personalization**: Mastery Path, Personas, Skills
- Cada card mostra contagem ao vivo (chamadas paralelas independentes)
- i18n completo (zh/en)

### Estrutura de Componentes do Space

```
web/components/space/
  SpaceMain.tsx              # Layout wrapper
  SpaceDashboard.tsx         # Hub central
  SpaceSectionHeader.tsx     # Cabecalho de secao reutilizavel
  SkillsSection.tsx          # Secao de Skills
  ScopePicker.tsx            # Seletor de escopo
  ScopeEditorModal.tsx       # Modal de edicao de escopo
  QuestionBankSection.tsx    # Banco de questoes
  PersonasSection.tsx        # Personas
  NotebooksSection.tsx       # Notebooks (criar, listar, deletar)
  MyAgentsSection.tsx        # Agentes do usuario
  ChatHistorySection.tsx     # Historico de conversas
  ImportWizard.tsx           # Assistente de importacao
  EduHubImportModal.tsx      # Modal de importacao do EduHub
```

### Pagina de Aprendizado (Mastery Path) - `/space/learning`

O arquivo `web/app/(utility)/space/learning/page.tsx` (272 linhas):

- **Layout**: Sidebar de 256px a esquerda com lista de paths + area de detalhe a direita
- **Funcionalidades**:
  - Lista todas as "mastery paths" do usuario com nome, contagem de KP e % medio de proficiencia
  - Seleciona um path para ver detalhes
  - Dois modos de visualizacao: **Lista** (`ModuleMap`) e **Grafo** (`ConceptGraph`)
  - Botoes para continuar, resetar progresso e deletar path
  - Botao "New (in Chat)" que navega para `/home` para iniciar novo path via chat
- **APIs usadas**: `fetchAllProgress()`, `fetchMasteryMap()`, `deleteProgress()`, `redoProgress()` de `@/lib/learning-api`
- **Componentes**: `ModuleMap` e `ConceptGraph` de `@/components/learning/`

---

## 3. Capabilities System

### Estrutura

**Arquivo:** `deeptutor/capabilities/__init__.py`

Expoe: `KnowledgeCapability`, `LoopCapability`, `PromptBlock`, `active_loop_capabilities()`, `any_exclusive_capability_active()`, `capability_tool_owners()`

### Registry (`deeptutor/capabilities/registry.py`)

5 capacidades de loop sao registradas:

| Capacidade | Classe | Owned Tools | Tipo |
|-----------|--------|-------------|------|
| `mastery_path` | `MasteryLoopCapability` | Ferramentas de mastery | Loop augment |
| `deep_solve` | `SolveLoopCapability` | Ferramentas de resolucao | Loop augment |
| `obsidian` | `ObsidianCapability` | Ferramentas do Obsidian | Knowledge (exclusivo) |
| `subagent` | `SubagentCapability` | Ferramentas de subagente | Knowledge (exclusivo) |
| `explore_context` | `ExploreContextCapability` | Ferramentas de contexto | Loop augment |

**Nao ha** uma capacidade "project" ou "roadmap". O sistema de capacidades e estritamente sobre modos de interacao do chat: `chat` (padrao), `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `mastery_path` (loop), `obsidian`, `subagent`, `explore_context`.

### Protocolo (`deeptutor/capabilities/protocol.py`)

Duas categorias:
- **`LoopCapability`**: Augmenta o chat padrao com tools proprias. O chat continua rodando normalmente.
- **`KnowledgeCapability`**: Substitui o tool surface inteiro (tools exclusivas). Usado por Obsidian e Subagent.

---

## 4. Knowledge Ingestion Pipeline

### Arquivo principal: `deeptutor/knowledge/`

| Arquivo | Funcao |
|---------|--------|
| `__init__.py` | Lazy-loads `DocumentAdder`, `KnowledgeBaseInitializer`, `KnowledgeBaseManager` |
| `manager.py` | `KnowledgeBaseManager` - gerencia config, lista/deleta KBs, linked folders |
| `initializer.py` | `KnowledgeBaseInitializer` - cria estrutura de diretorios e processa documentos |
| `add_documents.py` | `DocumentAdder` - adicao incremental com dedup por hash SHA-256 |
| `kb_types.py` | Tipos de KB: local, linked, obsidian, lightrag_server, subagent |
| `naming.py` | Validacao de nomes de KB |
| `progress_tracker.py` | `ProgressTracker` - rastreia estado de inicializacao |

### Script de Ingestao de Livro Didatico

**Arquivo:** `C:\Users\frota\Documents\Projetos\AI TUTOR\scripts\ingest_textbook.py` (499 linhas)

Fluxo completo:
1. Abre PDF com `fitz` (PyMuPDF)
2. Detecta capitulos por OCR de "Chapter N" no texto
3. Extrai paginas como Markdown com imagens (full-page renders a 72 DPI)
4. Detecta secoes (`1.1`, `1.2`, etc.) e exercicios ("Review Questions", "Problems")
5. Gera estrutura de arquivos:
   ```
   data/modules/{kb_name}/
     textbook.md         # Livro completo
     meta.json           # Metadata
     chapters/ch{nn}.md  # Por capitulo
     sections/ch{nn}_{sec}.md  # Por secao
     exercises/ch{nn}-{type}.md  # Exercicios
     figures/pg{nnnn}.png  # Imagens das paginas
     raw_text/           # Backup pre-formatacao
   ```
6. **Registra como KB** chamando `KnowledgeBaseInitializer`:
   - Cria diretorio da KB em `data/knowledge_bases/`
   - Copia `textbook.md` e `meta.json` para `raw/`
   - Copia figuras para diretorio `figures/` da KB
   - Chama `process_documents()` para indexar via RAG provider
7. Formata Markdown chamando `scripts/format_textbook.py`

### Pipeline RAG (`deeptutor/services/rag/`)

A ingestion final e feita pelos pipelines RAG:
- `deeptutor/services/rag/pipelines/llamaindex/ingestion.py` - Indexacao LlamaIndex
- `deeptutor/services/rag/pipelines/graphrag/ingestion.py` - Indexacao GraphRAG
- O `RAGService` (em `deeptutor/services/rag/service.py`) orquestra qual pipeline usar baseado no provider escolhido

---

## 5. Mastering Path Page (Learning Space Frontend)

### Pagina: `web/app/(utility)/space/learning/page.tsx` (272 linhas)

```tsx
export default function MasteryPathPage() {
  // Estados: paths[], selected, detail, loadingList, loadingDetail, viewMode
  // viewMode: "list" | "graph"
  
  // Render:
  //   <aside> (sidebar 256px):
  //     - Header "Mastery Path"
  //     - Lista de paths clicaveis (nome + % mastery + contagem KP)
  //     - Botao "New (in Chat)"
  //   <section> (area principal):
  //     - Se loading: spinner
  //     - Se sem selecao: mensagem instrutiva
  //     - Se com detalhe:
  //       - Toggle viewMode (List | Graph)
  //       - Botoes: Reset progress, Delete
  //       - ModuleMap (viewMode=list) ou ConceptGraph (viewMode=graph)
```

### Componentes usados:

1. **`ModuleMap`** (`@/components/learning/ModuleMap`): Visualizacao em lista dos modulos/pontos de conhecimento, com botoes "Continue" por path
2. **`ConceptGraph`** (`@/components/learning/ConceptGraph`): Visualizacao em grafo dos知识 pontos, com `onNodeClick` que navega para `/home/{sessionId}?kp={kpId}`

### APIs:

- **`fetchAllProgress()`** (`@/lib/learning-api`): GET para `/api/v1/learning/progress/all`? - retorna `{ summaries: ProgressSummary[] }`
- **`fetchMasteryMap(bookId)`**: GET para `/api/v1/learning/progress/{id}/map` - retorna `MasteryMapResult` com modulos, KP, status de mastery
- **`deleteProgress(bookId)`**: DELETE `/api/v1/learning/progress/{id}`
- **`redoProgress(bookId)`**: POST `/api/v1/learning/progress/{id}/redo`

### Backend correspondente:

**`deeptutor/api/routers/mastery_path.py`** (montado em `/api/v1/learning`):
- Usa `LearningService` + `LearningStore` para persistencia
- Modelos: `LearningModule`, `KnowledgePoint`, `KnowledgeType`, `LearningStage`
- Politica de mastery definida em `deeptutor/learning/policy`
- A tutoria em si roda no loop de chat do agente (modo "Mastery Path")

*Novo passo iniciado*

---

*11 messages | 80 parts | 💰 $0.0000 | ⏱️ 0h01m25s*
