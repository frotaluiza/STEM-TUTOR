---
slug: swift-canyon
title: "Explore DeepTutor codebase (@explore subagent)"
date: 2026-07-11
agent: explore
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h02m46s
messages: 18
parts: 136
cost: 0
tokens_input: 67872
tokens_output: 7764
tokens_reasoning: 1010
tokens_cache_read: 832256
tokens_cache_write: 0
created: "2026-07-11 21:14:51 UTC"
updated: "2026-07-11 21:17:38 UTC"
---

Sessão com **18 messages**, **136 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | 💾 cache read: 832.3K | ⏱️ 0h02m46s

## 👤 Usuário (2026-07-11 21:14:51 UTC)

Explore the user's codebase looking for any files related to "deeptutor", "deep-tutor", "tutor", or similar. Search in C:\Users\frota\ and subdirectories. Look for:
1. Any project structure, configs, package.json, etc.
2. Any backend code (Python, Node.js, etc.)
3. Any frontend code
4. Any .env, config files with API keys or model configs
5. Any README or documentation

Also check the Notion for any project called "DeepTutor" or "AI STEM Tutor" in the Projetos database.

Return everything you find about the project structure, tech stack, and current status.

## 🤖 Assistente (2026-07-11 21:14:52 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to explore their codebase for anything related to "deeptutor", "deep-tutor", "tutor", etc. They also want me to check Notion for a project called "DeepTutor" or "AI STEM Tutor". Let me start with multiple parallel searches.

</details>

### Resposta

I'll start by searching across multiple dimensions in parallel: file patterns, content searches, and directory exploration.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:15:48 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I found several relevant directories and files. Let me dig deeper into the most important ones:

1. `C:\Users\frota\Documents\Projetos\AI TUTOR\` - This seems to be the main project directory
2. `C:\Users\frota\data\user\logs\deeptutor.jsonl` - Logs
3. `C:\Users\frota\OneDrive\Documentos\Obsidian Vault\2026\3 - AI STEM Tutor\` - Obsidian vault notes
4. `C:\Users\frota\OneDrive\Documentos\Obsidian Vault\2026\_notion\Projetos\3 - AI STEM Tutor.md` - Notion synced project
5. `C:\Users\frota\OneDrive\Documentos\Obsidian Vault\Leituras\_notion\DeepTutor- Towards Agentic Personalized Tutoring (arXiv-2604.26962).md` - Reading note
6. Various task notes about DeepTutor

Let me explore these directories and read the key files.

</details>

### Resposta

Good, I found several key locations. Let me dig deeper into the main project directory and the Obsidian vault notes.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:15:54 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Great! The main project is at `C:\Users\frota\Documents\Projetos\AI TUTOR`. Let me explore it further - read the key configuration files, the README, pyproject.toml, etc.

</details>

### Resposta

Excellent! Found the main project at `C:\Users\frota\Documents\Projetos\AI TUTOR`. Let me read the key configuration files.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:15:59 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a good picture of the DeepTutor project. Let me explore the project structure deeper - the backend and frontend code directories.

</details>

### Resposta

Let me explore the backend and frontend code directories, plus additional key files.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:05 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me get more details about the project: the web frontend package.json, the modifications doc, the data/user directory (which would have settings), and any customizations.

</details>

### Resposta

Let me get more details on the web frontend config, modifications doc, and settings.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:10 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me also check the web .env.local, the settings directory, and the git status to understand the current state of the fork.

</details>

### Resposta

Let me get the local env file, settings, and git status.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:15 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me also check the settings files and see if there are any modified frontend files for voice features.

</details>

### Resposta

Let me check the model catalog config and the modified files for voice features, plus any other custom code.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:21 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me look for the useTextToSpeech hook and the speech recognition types since they were mentioned in the modifications doc.

</details>

### Resposta

Let me find the custom hooks and types files mentioned in the modifications doc.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:26 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me check the hooks directory to find the useTextToSpeech and other hooks. Also check for the CropPlaceholder and NotebookEditor.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:31 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

So we have the hooks: `useVoiceAutoplay.ts` and `useVoiceRecorder.ts`. The modifications doc mentions `useTextToSpeech.ts` but there isn't one - maybe the naming changed. Let me read these voice-related hooks and also check the ingest script and the types directory. Let me also check if there's a `crop-tool.html` file.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:36 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me also look at the other Obsidian notes related to the project to get the full picture. Let me also check the AGENTS.md in the project dir, and examine the GitHub remote URL.

</details>

### Resposta

Let me get the final pieces - the Git remote and the other Obsidian notes.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:43 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me also look at the task notes in Obsidian for more context about what's been done.

</details>

### Resposta

Let me read the key task notes to understand project status.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:47 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive picture. Let me also check the modified ChatComposer and AssistantResponse to see the custom voice code.

</details>

### Resposta

Let me read the modified ChatComposer and AssistantResponse to check for customizations, and also get the current branch status and modified files list.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:52 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive understanding. Let me compile the full report.

The summary of what I found:

**Project: DeepTutor (forked as "AI STEM Tutor" / "stem-tutor")**

**Location:** `C:\Users\frota\Documents\Projetos\AI TUTOR\`

**No notion query yet** - I need to check the Notion! Let me do that.

</details>

### Resposta

Now let me check the Notion for the project status via the API.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:16:58 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The AGENTS.md mentions we should consult the Notion for project status. Let me look for any Notion-related Python scripts or config files for the API connectivity.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:17:02 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I can't directly query the Notion API without the proper credentials and setup. But from the Obsidian vault (which is synced from Notion), I already have the project information:

- The project "3 - AI STEM Tutor" in the Obsidian vault (synced via Notion) has status "Planejar" and priority "Alta" in the "IA" area.

Let me also check if there are any Notion integration scripts in the project.

</details>

### Resposta

Let me check if there are any Notion-related scripts or tools in the project folder.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-11 21:17:07 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I now have a comprehensive picture of the entire DeepTutor / AI STEM Tutor project. Let me compile the final report.

From the Obsidian vault (synced from Notion), I can see:
- Project "3 - AI STEM Tutor" in Notion: status=Planejar, area=IA, prioridade=Alta
- The DeepTutor paper reading is marked as "Planejada" with priority "Alta"
- Multiple tasks exist in the task database related to DeepTutor

Let me now compile everything into a comprehensive report.

</details>

### Resposta

Agora tenho um panorama completo. Aqui está o relatório consolidado.

---

## Relatorio Completo: DeepTutor / AI STEM Tutor

---

### 1. LOCALIZACAO DO PROJETO

**Diretorio principal (fork local):**
`C:\Users\frota\Documents\Projetos\AI TUTOR\`

**Repo upstream (forked from):**
`https://github.com/HKUDS/DeepTutor.git`

**Branch ativa atualmente:** `feature/mind-map-module`

**Branches locais existentes:**
- `feature/crop-tool-inline`
- `feature/equation-formatting`
- `feature/mind-map-module` (atual)
- `main`
- `stem-tutor` (branch principal com as customizacoes do AI STEM Tutor)

---

### 2. ESTRUTURA DO PROJETO

```
AI TUTOR/
├── deeptutor/              # Backend Python (package principal)
│   ├── __init__.py, __main__.py, __version__.py
│   ├── agents/             # Agentes de chat e capacidades
│   ├── api/                # FastAPI routers (unified_ws, knowledge, notebook, system...)
│   ├── app/                # DeepTutorApp facade (SDK Python)
│   ├── book/               # Book Engine
│   ├── capabilities/       # Capacidades: chat, solve, question, research, visualize, mastery
│   ├── co_writer/          # Co-Writer workspace
│   ├── config/             # Config management
│   ├── core/               # Core runtime: orchestrator, stream, tool/capability protocols
│   ├── events/
│   ├── i18n/               # Internacionalizacao
│   ├── knowledge/          # RAG, knowledge bases, LlamaIndex, GraphRAG, LightRAG...
│   ├── learning/           # Learning Space
│   ├── logging/
│   ├── loop_plugins/       # Plugin framework para loops
│   ├── multi_user/         # Deploy multi-usuario
│   ├── partners/           # Sistema de parceiros (antigo TutorBot)
│   ├── runtime/            # Orchestrator, registry, launcher, bootstrap
│   ├── services/           # LLM, parsing, sandbox, etc.
│   ├── skills/             # Sistema de skills
│   ├── tools/              # Ferramentas: rag, web_search, paper_search, brainstorm, exec...
│   └── utils/
├── deeptutor_cli/          # CLI entry point (Typer)
├── deeptutor_web/          # Frontend build assets
├── web/                    # Frontend Next.js 16 (TypeScript, React 19, Tailwind)
│   ├── app/                # Next.js App Router pages
│   ├── components/         # Componentes React
│   │   ├── chat/home/ChatComposer.tsx   (MODIFICADO - voice input)
│   │   ├── common/AssistantResponse.tsx (MODIFICADO - TTS nas respostas)
│   │   └── knowledge/      # CropModal, MarkdownWithCrops, KbFilePreview...
│   ├── hooks/              # useVoiceAutoplay, useVoiceRecorder, etc.
│   ├── lib/
│   ├── types/
│   ├── locales/            # Traducoes i18n
│   ├── package.json
│   └── next.config.js
├── data/                   # Dados de runtime (gitignored)
│   ├── user/
│   │   └── settings/       # model_catalog.json, system.json, auth.json, agents.yaml...
│   ├── modules/sadiku/     # Livro "Fundamentals of Electric Circuits" (Sadiku) ingerido
│   ├── knowledge_bases/    # KBs criadas no DeepTutor
│   ├── partners/           # Workspaces de parceiros
│   └── memory/             # Memoria L1/L2/L3
├── tests/                  # Testes pytest
├── scripts/                # Scripts utilitarios
│   ├── ingest_textbook.py  # Pipeline de ingesao de livros didaticos
│   ├── format_textbook.py
│   └── ...
├── docs/
│   └── modificacoes-stem-tutor.md  # DOCUMENTACAO DAS MODIFICACOES
├── assets/                 # Imagens, logos, READMEs traduzidos
├── pyproject.toml          # Configuracao Python
├── requirements.txt
├── .env.example
├── AGENTS.md               # Guia de arquitetura para agentes LLM
├── SKILL.md                # Skill do DeepTutor para outros agentes
├── Dockerfile, compose.yaml, docker-compose.yml
├── LICENSE (Apache 2.0)
├── README.md
└── CONTRIBUTING.md
```

---

### 3. TECH STACK

| Camada | Tecnologia |
|---|---|
| **Backend** | Python 3.11+ / 3.12 (FastAPI, Uvicorn, WebSockets) |
| **Frontend** | Next.js 16.2.3, React 19, TypeScript 5, Tailwind CSS 3.4 |
| **LLM Provider** | DeepSeek Chat (`deepseek-chat`, API compativel OpenAI) |
| **Embeddings** | Ollama local (`nomic-embed-text`, 768d) |
| **RAG** | LlamaIndex 0.14+ (default), GraphRAG, LightRAG, PageIndex, Obsidian link |
| **Vector Store** | FAISS (cpu), fallback SimpleVectorStore |
| **CLI** | Typer, Rich, Prompt Toolkit |
| **SDK LLM** | OpenAI SDK nativo, Anthropic SDK, Dashscope, Perplexity |
| **Banco** | SQLite (chat_history.db), PocketBase opcional (auth/multi-user) |
| **Container** | Docker / Podman (rootless, read-only rootfs) |
| **Code Quality** | Ruff, Black, MyPy, Bandit, Pytest, Pre-commit |
| **CI/CD** | GitHub Actions (upstream) |

---

### 4. MODIFICACOES DO FORK "STEM TUTOR"

Documentadas em `C:\Users\frota\Documents\Projetos\AI TUTOR\docs\modificacoes-stem-tutor.md`

#### 4a. Voice Input (Entrada por Voz)
- **Arquivos modificados:**
  - `web/components/chat/home/ChatComposer.tsx` — Botao toggle voice mode + auto-send por silencio (1.2s)
  - `web/components/common/AssistantResponse.tsx` — TTS via `speechSynthesis` ao final do streaming
- **Hooks criados:**
  - `web/hooks/useVoiceRecorder.ts` — Gravacao por microfone (MediaRecorder) + transcricao via backend (`/api/v1/voice/stt`)
  - `web/hooks/useVoiceAutoplay.ts` — Auto-play de TTS com persistencia em localStorage e settings

#### 4b. Crop Tool + Notebook Editor (Junho 2026)
- **Branch:** `feature/crop-tool-inline` (mergeado em `stem-tutor`)
- **Backend:** Endpoints `POST /api/v1/knowledge/{kb}/crop` e `/crop-save` para recorte de PDF + `POST /api/v1/notebook/chat` para chat inline
- **Frontend:** CropModal, MarkdownWithCrops, NotebookEditor (split-pane markdown + chat)
- **Script de ingestao:** `scripts/ingest_textbook.py` — pipeline completo PDF -> markdown estruturado (18 capitulos, 339 secoes, 20 listas de exercicios, 1022 paginas renderizadas)
- **Livro ja ingerido:** Sadiku, "Fundamentals of Electric Circuits" (4a e 7a edicoes) em `data/modules/sadiku/`

#### 4c. Skills Instaladas do ClawHub
- `tutor` v1.0.0
- `study-tutor` v1.0.2
- `tutor-ai` v1.0.0

---

### 5. CONFIGURACAO ATIVA

**Model Catalog** (`data/user/settings/model_catalog.json`):
```json
LLM: DeepSeek (api.deepseek.com, modelo deepseek-chat, 65k tokens)
Embedding: Ollama local (localhost:11434, nomic-embed-text, 768d)
Search: nenhum configurado
```

**System** (`data/user/settings/system.json`):
```json
backend_port: 8001
frontend_port: 3782
sandbox_allow_subprocess: true
auth: disabled
```

**Frontend env** (`web/.env.local`):
```
NEXT_PUBLIC_API_BASE=http://localhost:8001
NEXT_PUBLIC_AUTH_ENABLED=false
```

**Ambiente:**
- Python 3.12.12 (venv em `.venv`)
- Node.js 24.15.0
- API Key DeepSeek exposta em `model_catalog.json` (sk-6c4b...)

---

### 6. STATUS NO NOTION (via Obsidian sync)

**Projeto:** "3 - AI STEM Tutor"
| Campo | Valor |
|---|---|
| Database ID | `9172be34-0056-4f38-aa2a-093339bb5790` |
| Notion ID | `eb257164-7a4f-4424-acbe-10995d8fc4f8` |
| Status | **Planejar** |
| Area | **IA** (laranja, prioritaria) |
| Prioridade | **Alta** |
| Ordem | 1 |
| Notas | "Precisa vir antes para suportar escaneamento/livros e prototipos de tutor." |

**Leitura vinculada:** "DeepTutor: Towards Agentic Personalized Tutoring" (arXiv:2604.26962)
| Campo | Valor |
|---|---|
| Status | **Planejada** |
| Prioridade | Alta |
| Tipo | Artigo |
| Tags | Organizacao |

**Tarefas relacionadas (todas "A fazer", prioridade Alta):**
1. Fork do DeepTutor + esbocar arquitetura do STEM Tutor
2. Fazer DeepTutor funcionar no terminal (CLI)
3. Madrugada: testar DeepTutor + prototipo de ferramenta "paper -> architecture -> code"
4. Corrigir modo de conversa continua do DeepTutor
5. Adicionar provedor RAG para opencode-DeepTutor
6. Caminhos do xadrez — Capability+Agent no DeepTutor
7. Pesquisar frameworks de didatica para guiar o comportamento do AI STEM Tutor
8. Comecar a montar o pitch do AI STEM Tutor

---

### 7. RESUMO EXECUTIVO

**O projeto e um fork local do DeepTutor** (HKUDS/DeepTutor, Apache 2.0), um workspace de aprendizado agente-nativo com ~200k+ linhas de codigo, que integra tutoria, resolucao de problemas, geracao de quizzes, pesquisa, visualizacao e praticas de mastery em um unico sistema extensivel.

**Ja foi feito:**
- Fork completo com branch `stem-tutor` criada
- Customizacoes de voz funcionais (voice input + TTS nas respostas)
- Crop Tool + Notebook Editor para recorte de figuras de PDF e edicao markdown com chat inline
- Pipeline de ingestao de livros didaticos (Sadiku ja ingerido: 18 capitulos, 339 secoes)
- 3 skills educacionais instaladas do ClawHub (tutor, study-tutor, tutor-ai)
- Configurado com DeepSeek (API key ativa) + Ollama local para embeddings
- AGENTS.md personalizado com diretrizes pedagogicas para o STEM Tutor

**Nao foi feito / pendente (planejado):**
- O projeto ainda esta em status **"Planejar"** no Notion
- Nenhum deploy em producao
- Testes de integracao com o opencode nao concluidos
- Modo de conversa continua do CLI ainda nao testado/corrigido
- Provedor RAG para opencode-DeepTutor nao implementado
- Framework didatico para guiar o comportamento do tutor nao definido
- Pitch do projeto nao iniciado
- Branch atual (`feature/mind-map-module`) tem modificacoes nao commitadas em `AGENTS.md`, `agentic_chat.yaml` e `space/learning/page.tsx`

*Novo passo iniciado*

---

*18 messages | 136 parts | 💰 $0.0000 | ⏱️ 0h02m46s*
