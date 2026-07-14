# Project Orchestrator — Arquitetura

**Projeto:** Mar da Elétrica: AI STEM Tutor
**Data:** 2026-07-14
**Versão:** 1.0.0
**Perfil:** Frota

---

## 1. Visão Geral

O **Project Orchestrator** é o sistema central de gerenciamento de project-spaces.
Ele unifica o versionamento de decisões, código, fontes e metadados de todos os
projetos do perfil Frota em um único repositório GitHub versionado, com sync
bidirecional para o Notion.

### Princípios

| Princípio | Descrição |
|-----------|-----------|
| **Source of truth local** | O repositório `Projetos/` é a fonte única e verdadeira |
| **Versionamento nativo** | Git como mecanismo de histórico, branch e merge |
| **Rastreabilidade total** | Toda decisão é registrada com contexto, origem e timestamp |
| **Sync bidirecional** | GitHub ↔ Notion via Actions; local ↔ GitHub via git |
| **Perfil como identidade** | "Frota" autentica e autoriza acesso ao ecossistema |

---

## 2. Arquitetura de Sistemas

```
┌──────────────────────────────────────────────────────────────────────┐
│                      MÁQUINA LOCAL (Windows)                         │
│                                                                      │
│  ┌──────────────┐  ┌──────────────────┐  ┌────────────────────────┐ │
│  │   opencode    │  │  watch-project-  │  │  API REST              │ │
│  │   (sessão)    │  │  state.ps1       │  │  localhost:8080        │ │
│  │   edita .md   │──│  watcher +       │  │  (FastAPI)             │ │
│  │   .yaml       │  │  auto-commit     │  │  serve projetos/       │ │
│  └──────────────┘  └────────┬─────────┘  └────────────────────────┘ │
│                             │                                        │
│                    ┌────────▼─────────┐                               │
│                    │  git commit      │                               │
│                    │  branch:         │                               │
│                    │  sessao/{slug}   │                               │
│                    └────────┬─────────┘                               │
└─────────────────────────────┼────────────────────────────────────────┘
                              │ git push (no merge)
                              ▼
┌──────────────────────────────────────────────────────────────────────┐
│                      GITHUB (frotaluiza/STEM-TUTOR)                   │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  main (branch estável)                                        │   │
│  │  ├── Projetos/ai-stem-tutor/                                 │   │
│  │  ├── Projetos/tcc/                                           │   │
│  │  ├── Projetos/curso-bateria/                                 │   │
│  │  └── Projetos/pc-windows/                                    │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                              │                                        │
│              ┌───────────────┴────────────────┐                      │
│              ▼                                ▼                      │
│  ┌──────────────────────┐    ┌──────────────────────────┐            │
│  │  GitHub Action        │    │  GitHub Action            │           │
│  │  push (commit →       │    │  pull (schedule 15min)    │           │
│  │  Notion)              │    │  Notion → commit)         │           │
│  └──────────┬───────────┘    └───────────┬──────────────┘            │
└─────────────┼────────────────────────────┼───────────────────────────┘
              ▼                            ▼
┌──────────────────────────────────────────────────────────────────────┐
│                              NOTION                                   │
│                                                                      │
│  Databases: Projetos, Sessões, Fontes, Tarefas, Rotinas, ...        │
│  → Entradas manuais são puxadas pelo GitHub Action pull              │
│  → Entradas do opencode/GitHub são empurradas pelo push              │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 3. Estrutura do Repositório

```
STEM-TUTOR/                          ← repositório GitHub
├── Projetos/                        ← raiz dos project-spaces
│   ├── perfis/
│   │   └── frota.yaml               ← perfil do usuário
│   │
│   ├── ai-stem-tutor/               ← projeto IA
│   │   ├── project-state.yaml       ← estado, objetivo, caminho, decisões
│   │   ├── fontes/                  ← vídeos, leituras, artigos, anotações
│   │   ├── arquitetura/             ← decisões arquiteturais + docs
│   │   ├── tarefas/                 ← tasks do projeto
│   │   ├── rotinas/                 ← agendador de eventos
│   │   ├── frameworks/              ← frameworks usadas
│   │   ├── ferramentas/             ← ferramentas conectadas
│   │   ├── docs/                    ← NoteBlocks
│   │   ├── sessoes/                 ← sessões opencode
│   │   ├── conversas/               ← conversas Notion
│   │   └── relatorios/
│   │       ├── testes/              ← relatórios de testes
│   │       └── diarios/             ← resumos diários automáticos
│   │
│   ├── tcc/                         ← projeto acadêmico (mesma estrutura)
│   ├── curso-bateria/               ← projeto música
│   ├── pc-windows/                  ← projeto pessoal
│   └── conflitos/                   ← divergências local × Notion
│
├── scripts/
│   ├── api/                         ← API REST FastAPI
│   │   ├── main.py
│   │   ├── routers/
│   │   │   ├── projects.py
│   │   │   ├── sessions.py
│   │   │   ├── readings.py
│   │   │   ├── tasks.py
│   │   │   └── daily_reports.py
│   │   └── models/
│   ├── kb/                          ← scripts de sync
│   │   ├── watch-project-state.ps1  ← watcher + branch automática
│   │   ├── init-environment.ps1     ← setup de ambiente
│   │   ├── start-api.ps1            ← inicia a API REST
│   │   ├── install-api-autostart.ps1← auto-início no login
│   │   ├── gh-sync-notion.py        ← push GitHub → Notion
│   │   ├── notion-pull.py           ← pull Notion → GitHub
│   │   └── reconcile.py             ← sync inicial
│   └── api/requirements.txt
│
├── .github/workflows/
│   └── sync-notion.yml              ← GitHub Actions bidirecional
│
├── .opencode/skills/
│   └── project-orchestrator/        ← skill carregada em toda sessão
│       ├── skill.json
│       └── instructions.md
│
└── web/                             ← DeepTutor frontend
    ├── lib/projects-api.ts          ← cliente da API de projetos
    ├── lib/proxy-policy.ts          ← rota de proxy /orchestrator/
    ├── proxy.ts                     ← middleware Next.js
    └── app/(workspace)/projects/    ← páginas de projetos
```

---

## 4. Schema do project-state.yaml

```yaml
projeto: "Nome do Projeto"
slug: nome-do-projeto
perfil: Frota
area: "IA | Academico | Musica | Pessoal"
status: "Ideia | Planejar | Em andamento | Concluído"
objetivo: "Descrição do objetivo principal"
repositorio_codigo: "owner/repo"  # opcional, para projetos com código

# Fases do projeto (mastery path)
caminho:
  - fase: "Pesquisa"
    descricao: "Referências, artigos, papers"
    fontes: []
  - fase: "Arquitetura"
    descricao: "Decisões técnicas documentadas"
  - fase: "Implementação"
    descricao: "Codificação"

# Decisões acumuladas (rastreáveis)
decisoes_acumuladas:
  - contexto: "Problema ou necessidade"
    escolha: "Decisão tomada"
    stack: "Tecnologias envolvidas"
    data: 2026-07-14
    origem: "opencode | notion | manual"

# Próximos passos
proximos_passos:
  - descricao: "Ação a realizar"
    prioridade: "alta | media | baixa"
    prazo: 2026-07-20

# Contagem de fontes
fontes:
  videos: 12
  leituras: 8
  artigos: 5

ultima_atualizacao: 2026-07-14
```

---

## 5. Ciclo de Vida de uma Sessão

### Início
1. Usuário inicia sessão no opencode
2. Skill `project-orchestrator` é carregada automaticamente
3. `@init-environment` verifica git, API, dependências
4. Watcher cria branch `sessao/{slug}` a partir de `main`

### Durante
1. LLM altera arquivos do project-space conforme decisões
2. Cada alteração relevante inclui `## Decisões` no live doc
3. Watcher detecta mudanças via FileSystemWatcher
4. Debounce de 5s → `git commit` automático na branch da sessão
5. Mensagem de commit: `auto: {n} alteração(ões) em {branch}`

### Final
1. `@end-session` ou watcher detecta fim da sessão
2. Commit final na branch de sessão
3. `git checkout main`
4. `git merge sessao/{slug} --no-edit`
5. `git push origin main`
6. GitHub Action `sync-notion.yml` → push para Notion

### Pull do Notion
1. GitHub Action schedule (a cada 15 min) ou webhook
2. `notion-pull.py` consulta DB Sessões por entradas novas/editadas
3. Se encontrou: download como .md em `Projetos/{slug}/sessoes/`
4. Se conflito com .md local → salva em `Projetos/conflitos/`
5. `git add + commit + push` em main
6. Usuário dá `git pull` na máquina local

---

## 6. Databases do Sistema (Notion ↔ Local)

| Database Notion | Diretório Local | Descrição |
|----------------|-----------------|-----------|
| Projetos (2026) | `Projetos/{slug}/project-state.yaml` | Catálogo de projetos |
| Sessões opencode | `Projetos/{slug}/sessoes/` | Log de sessões |
| Fontes Projetos | `Projetos/{slug}/fontes/` | Vídeos, leituras, artigos, anotações (unificada) |
| Tarefas da Semana | `Projetos/{slug}/tarefas/` | Tasks por projeto |
| Rotinas | `Projetos/{slug}/rotinas/` | Agendador de eventos |
| Frameworks | `Projetos/{slug}/frameworks/` | Frameworks implementadas |
| Ferramentas | `Projetos/{slug}/ferramentas/` | Barra de ferramentas personalizável |
| Documentação (NoteBlocks) | `Projetos/{slug}/docs/` | Notebooks armazenados |
| Conversas Notion | `Projetos/{slug}/conversas/` | Logs de conversas do Notion |
| Relatórios de Testes | `Projetos/{slug}/relatorios/testes/` | Resultados de testes |
| Relatório Diário | `Projetos/{slug}/relatorios/diarios/` | Resumo automático diário |
| Arquitetura | `Projetos/{slug}/arquitetura/` | Decisões + docs arquiteturais |

---

## 7. Formato de Decisões Rastreáveis

Toda sessão do opencode DEVE estruturar as decisões no live doc no formato:

```markdown
## Decisões

### YYYY-MM-DD HH:MM — Título da Decisão
- **Contexto**: Problema ou necessidade identificada
- **Alternativas**: (opcional) O que foi considerado
- **Escolha**: Decisão tomada
- **Stack**: (opcional) Tecnologias envolvidas
- **Origem**: opencode | notion | manual
- **Arquivos**: (opcional) Caminhos dos arquivos alterados
```

Estas decisões são:
1. Registradas no `project-state.yaml` → `decisoes_acumuladas`
2. Visíveis no DeepTutor via API REST
3. Rastreáveis pelo Project Manager
4. Associadas à sessão e ao projeto

---

## 8. API REST — Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/health` | Status da API |
| GET | `/api/v1/profile` | Perfil Frota |
| GET | `/api/v1/projects` | Lista todos os projetos |
| GET | `/api/v1/projects/{slug}` | Detalhes + fontes de um projeto |
| GET | `/api/v1/projects/{slug}/state` | project-state.yaml |
| GET | `/api/v1/projects/{slug}/{database}` | Tabela específica (fontes, tarefas, etc.) |
| GET | `/api/v1/sessions?projeto=slug` | Sessões do projeto |
| GET | `/api/v1/readings?projeto=slug` | Leituras/fontes |
| GET | `/api/v1/tasks?projeto=slug` | Tarefas |
| GET | `/api/v1/reports/daily?projeto=slug` | Relatórios diários |

Proxy no frontend: `/orchestrator/api/v1/*` → `http://localhost:8080/api/v1/*`

---

## 9. Perfil Frota

```yaml
perfil: Frota
usuario: LuizaF
github: frotaluiza
projetos:
  - slug: ai-stem-tutor
    repositorio_codigo: frotaluiza/STEM-TUTOR
  - slug: tcc
    repositorio_codigo: frotaluiza/TCC---Distila-o-de-Membranas
  - slug: curso-bateria
  - slug: pc-windows
```

O perfil é:
- Gerenciado pelo DeepTutor (autenticação)
- Definido em `Projetos/perfis/frota.yaml`
- A referência para todos os project-spaces
- Fora dele, nenhum projeto é acessível

---

## 10. Relatório Diário Automático

Task em background (Watcher) que ao final do dia:
1. Coleta alterações no `project-state.yaml` das últimas 24h
2. Associa conversas do opencode e entradas do Notion às decisões
3. Gera resumo em `Projetos/{slug}/relatorios/diarios/YYYY-MM-DD.md`
4. Formato:
   ```markdown
   # Relatório Diário — YYYY-MM-DD
   **Projeto:** {nome}
   
   ## Alterações
   - Decisões: {n} novas
   - Tarefas: {n} concluídas, {n} pendentes
   - Sessões: {n} sessões do opencode
   - Fontes: {n} novas adicionadas
   
   ## Detalhes
   - {decisão 1} (via opencode)
   - {decisão 2} (via Notion)
   
   ## Origem das alterações
   - opencode: {n}
   - Notion: {n}
   - Manual: {n}
   ```

---

## 11. Auto-Start da API

A API REST é iniciada automaticamente no login do Windows via Task Scheduler:

```
Tarefa: ProjectOrchestratorAPI
Evento: At logon do usuário
Comando: powershell -NoProfile -WindowStyle Hidden -File start-api.ps1 -Background
Porta: 8080
```

Comandos:
```powershell
# Instalar auto-start
.\scripts\kb\install-api-autostart.ps1

# Remover auto-start
.\scripts\kb\install-api-autostart.ps1 -Remove

# Iniciar manualmente
.\scripts\kb\start-api.ps1
.\scripts\kb\start-api.ps1 -Background
```

---

*Artefato gerado em 2026-07-14 pelo Project Orchestrator — Perfil Frota*
