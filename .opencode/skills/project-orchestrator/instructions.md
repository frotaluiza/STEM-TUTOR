# Project Orchestrator — Instruções

## Arquitetura

```
GitHub: frotaluiza/Projetos/        ← repositório único de project-spaces
├── perfis/
│   └── frota.yaml                   ← perfil do usuário
├── {projeto-slug}/
│   ├── project-state.yaml           ← estado do projeto
│   ├── fontes/                      ← vídeos, leituras, artigos, anotações
│   ├── arquitetura/                 ← decisões arquiteturais
│   ├── tarefas/                     ← tasks do projeto
│   ├── rotinas/                     ← agendador de eventos
│   ├── frameworks/                  ← frameworks usadas
│   ├── ferramentas/                 ← ferramentas conectadas
│   ├── docs/                        ← NoteBlocks
│   ├── sessoes/                     ← sessões opencode
│   ├── conversas/                   ← conversas Notion
│   └── relatorios/
│       ├── testes/
│       └── diarios/
├── scripts/kb/                      ← scripts compartilhados
├── .github/workflows/
│   └── sync-notion.yml
└── .opencode/skills/
    └── project-orchestrator/
```

## Gestão de Branches

### Ao iniciar sessão:
1. Verificar branch atual
2. Se for main: criar branch `sessao/{slug}` a partir de main
3. Se já estiver em branch de sessão: continuar nela

### Ao alterar project-state:
- Commitar na branch da sessão
- Mensagem: `project-state: {descrição resumida}`

### Ao alterar código do projeto:
- Se o projeto tem repo de código (ex: deeptutor/):
  - **Criar duas branches:**
    1. `ps/{feature}` no project-space (a partir de `sessao/{slug}`)
    2. `feature/{feature}` no repo de código
  - Atualizar `project-state.yaml`: `branch_codigo: "feature/{feature}"`
  - Trabalhar em ambas simultaneamente
  - Mergear quando pronto: `feature/` → `main` (código) + `ps/` → `sessao/` (project-space)

### Hierarquia completa de branches:
```
main
  └── sessao/{slug}            ← criada no início da sessão
       └── ps/{feature}        ← criada quando decide implementar código
                                   ↑
                              feature/{feature}  ← repo de código
```

### Ao finalizar sessão:
1. **Atualizar project-state.yaml** com:
   - branch atual da sessão
   - últimas decisões tomadas
   - status atualizado
   - última atualização (timestamp)
2. Commit final na branch com msg: `sessao: {slug} — {n} decisões`
3. Checkout main
4. Merge da branch de sessão
5. Push

## Sincronização Obrigatória do Project State

Toda sessão DEVE garantir que o `project-state.yaml` reflita o estado atual:

| Campo | Como atualizar |
|-------|----------------|
| `status` | Se houve avanço significativo, mudar para "Em andamento" |
| `branch_atual` | Slug da branch da sessão (`sessao/{slug}`) |
| `ultima_sessao` | Slug, título e data da sessão atual |
| `decisoes_acumuladas` | Adicionar decisões tomadas durante a sessão |
| `proximos_passos` | Atualizar com base no que ficou pendente |
| `fontes.{videos, leituras, artigos}` | Incrementar se novas fontes foram adicionadas |
| `ultima_atualizacao` | Data ISO atual |

### Regra: project-state sempre espelha a branch

Se a sessão criou uma branch nova (`sessao/{slug}`), o project-state DEVE conter:
```yaml
branch_atual: "sessao/calm-canyon"
ultima_sessao:
  slug: calm-canyon
  titulo: "Implementar feature X"
  data: 2026-07-14
```

Isso garante que o Project Manager (PM) no DeepTutor veja sempre a branch correta.

## Formatos

### project-state.yaml
```yaml
projeto: "Nome do Projeto"
slug: nome-do-projeto
perfil: Frota
objetivo: "Descrição do objetivo"
status: "Ideia | Planejar | Em andamento | Concluído"
repositorio_codigo: "owner/repo"  # opcional
caminho:
  - fase: "Fase 1"
    descricao: "..."
    fontes: []
ultima_atualizacao: 2026-07-14
```

### Fontes (fontes/ diretório)
Cada fonte é um .md com frontmatter:
```yaml
---
tipo: video | leitura | artigo | anotacao | referencia
titulo: "..."
url: "..."
projeto: nome-do-projeto
tags: []
data: 2026-07-14
---
```

## Comandos Rápidos

- `@init-environment` — Verifica git, Notion API, dependências
- `@start-session` — Cria branch de sessão, prepara ambiente
- `@end-session` — Merge da branch, push, sync
- `@sync-notion` — Sincroniza alterações locais → Notion
- `@pull-notion` — Puxa alterações do Notion → local
- `@generate-report` — Gera resumo diário do projeto

## Formato de Decisões Rastreáveis (Live Doc)

Toda sessão DEVE incluir uma seção `## Decisões` no live doc. Cada decisão no formato:

```markdown
## Decisões

### YYYY-MM-DD HH:MM — Título da Decisão
- **Contexto**: Problema ou necessidade
- **Alternativas**: O que foi considerado
- **Escolha**: Decisão tomada
- **Stack**: Tecnologias envolvidas
- **Origem**: opencode
- **Arquivos**: Caminhos dos arquivos alterados
```

### Estrutura obrigatória do live doc

```markdown
## Contexto
Projeto: {Nome do Projeto}
Sessão: {slug}
Objetivo: {objetivo da sessão}

## Decisões
{formato padronizado acima}

## Arquivos Modificados
- {caminho} (criação/modificação)

## Próximos Passos
- {ação pendente}
```

### Live Doc vs Artefato

- **Live doc**: registro temporário da sessão (`docs/{slug}.md`)
- **Artefato**: documento persistente no repositório (`Projetos/{slug}/arquitetura/`)

**Sempre perguntar ao usuário após uma ação relevante se ele quer gerar um artefato.**

## Perfil Frota

O perfil "Frota" dá acesso ao repositório Projetos/.
- Usuário: LuizaF
- GitHub: frotaluiza
- Perfil definido em: `perfis/frota.yaml`
