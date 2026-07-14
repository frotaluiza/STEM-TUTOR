# Sessão de Aprendizado em NoteBlocks

## Contexto

Branch: `feature/session-from-module`
Data: 2026-07-14
Sessão: (slug da sessão atual)

## Problema

Hoje, uma sessão de aprendizado no Mastery Path acontece **dentro do chat** (`/home/{sessionId}` com capability `mastery_path`). O aluno conversa com o tutor num formato scrollável de mensagens. Isso tem limitações:

1. **Não promove autonomia** — o aluno é passivo, só responde perguntas
2. **Não gera artefato** — a conversa desaparece no histórico
3. **Não integra escrita** — o aluno não constrói seus próprios materiais de estudo
4. **Diálogo linear** — não dá para organizar, arrastar, editar o que foi produzido

## Visão

Uma **sessão de aprendizado** ocorre dentro de um **NoteBlocks** especialmente formatado para estudo, com:

- **Chat sidebar** com o tutor (diálogo contínuo, guiado por EMT)
- **Documento principal** onde o aluno escreve sua própria interpretação
- **Drag-and-drop** de blocos da conversa → anotação
- **Exercícios na página** (resumo, paráfrase, múltipla escolha)
- **Tutor avalia respostas** escritas e guia o aluno
- **Abas**: Nota + Chat + Explorer (arquivos gerados)

## Fundamentação Teórica (Papers Memphis)

### 5-Step Tutoring Frame (AutoTutor)

| Passo | Original (AutoTutor) | Adaptado p/ NoteBlocks |
|-------|---------------------|------------------------|
| 1. Tutor question | Tutor propõe questão profunda | Bloco `@ask` ou prompt no chat |
| 2. Learner response | Aluno responde em texto curto | Aluno escreve bloco de texto/anotação |
| 3. Short feedback | "Sim", "Quase", "Não" | Tutor avalia e colore o bloco |
| 4. Collaborative improvement | Bombeamento → dica → prompt → asserção | Tutor sugere adições/blocos complementares |
| 5. Check understanding | "Resuma o que aprendeu" | Aluno escreve resumo no NoteBlock |

### EMT Dialogue (Expectation-Misconception Tailored)

O tutor tem **expectativas** (o que uma boa resposta contém) e **misconceptions** (erros comuns):

1. **Bombeamento (Pump)**: "Me fale mais sobre..." — expandir
2. **Dica (Hint)**: "Pense na relação entre X e Y" — direcionar
3. **Prompt**: "Qual termo específico descreve ___?" — preencher lacuna
4. **Asserção**: "Na verdade, o correto é..." — corrigir

Já implementado em `dialogue_engine.py` (Runner do Conhecimento). Adaptar para NoteBlocks.

### Macro e Micro Adaptividade

- **Macro** (outer loop): Qual módulo/KP trabalhar hoje → decidido pelo `next_objective()` do `learning.policy`
- **Micro** (inner loop): Como escalar o suporte → EMT dialogue moves dentro da sessão

### Content > Medium

> "It is the semantic, conceptual content in the conversation that predicts learning, not the medium of communication" (Graesser et al., 2014)

O meio (chat, noteblock, voz) importa menos que o conteúdo. Mas o **formato NoteBlocks** permite que o aluno construa active learning (escrever > ler), que tem efeito comprovado.

## Arquitetura Proposta

### Layout da Página

```
┌──────────────────────────────────────────────────────────┐
│  Abas: [📝 Nota] [💬 Chat com Tutor] [📁 Explorer]       │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────── Nota (principal) ──────────────────────┐  │
│  │                                                     │  │
│  │  ▶ Módulo: Derivadas (1/5) — 45% mastered          │  │
│  │                                                     │  │
│  │  ┌────────────────────────────────────────────┐     │  │
│  │  │  @ask: O que é uma derivada?               │     │  │
│  │  └────────────────────────────────────────────┘     │  │
│  │                                                     │  │
│  │  ┌────────────────────────────────────────────┐     │  │
│  │  │ [👤 Aluno]                                 │     │  │
│  │  │ Uma derivada representa a taxa de...       │     │  │
│  │  │ A derivada de f(x)=x² é 2x porque...      │     │  │
│  │  └────────────────────────────────────────────┘     │  │
│  │                                                     │  │
│  │  ┌────────────────────────────────────────────┐     │  │
│  │  │ [🎓 Tutor] ✅ Quase lá! Você mencionou     │     │  │
│  │  │ a taxa de variação, mas faltou dizer que   │     │  │
│  │  │ ela é INSTANTÂNEA. Adicione isso: "taxa    │     │  │
│  │  │ de variação instantânea de f em relação    │     │  │
│  │  │ a x".                                       │     │  │
│  │  └────────────────────────────────────────────┘     │  │
│  │                                                     │  │
│  │  [➕ Adicionar bloco: Texto | @ask | Imagem | MD ]  │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                           │
├──────────────────────────────────────────────────────────┤
│  [📌 Pending: adicionar "instantânea" ao texto]          │
│  [📌 Próximo: exercício prático de derivada]             │
└──────────────────────────────────────────────────────────┘
```

### Aba Chat (Sidebar ou Aba Separada)

```
┌──────────────────── Chat ────────────────────┐
│                                               │
│  Tutor: Vamos estudar derivadas. O que você   │
│  já sabe sobre o assunto?                     │
│                                               │
│  ┌────────────────────────────────────┐       │
│  │ Aluno: Sei que é a inclinação da   │       │
│  │ reta tangente                      │       │
│  └────────────────────────────────────┘       │
│                                               │
│  Tutor: Isso! Quer dizer que a derivada       │
│  mede...? [complete]                         │
│                                               │
│  ┌────────────────────────────────────┐       │
│  │ Aluno: a taxa de variação          │       │
│  └────────────────────────────────────┘       │
│                                               │
│  ┌────────────────────────────────────┐       │
│  │  🎯 Puxe este bloco para a Nota    │ ←──  │
│  │  "Derivada = taxa de variação      │       │
│  │   instantânea"                     │       │
│  └────────────────────────────────────┘       │
│                                               │
│  ┌───────┐                                    │
│  │ 🖱️   │  Arraste blocos do chat para       │
│  │ arrasta│  dentro da anotação               │
│  └───────┘                                    │
└───────────────────────────────────────────────┘
```

### Aba Explorer

```
┌──────────────── Explorer ───────────────────┐
│                                               │
│  📁 outputs/                                  │
│    ├── 📄 grafico-derivada.png    [Arrastar]  │
│    ├── 📊 tabela-limites.csv      [Arrastar]  │
│    └── 🤖 codigo-newton.py        [Arrastar]  │
│                                               │
│  📁 data/noteblocks/attachments/              │
│    ├── 🖼️ diagrama.jpg            [Arrastar]  │
│    └── 📕 capitulo-3.pdf          [Arrastar]  │
│                                               │
│  ⏳ Monitorando: outputs/, downloads/         │
└───────────────────────────────────────────────┘
```

### Fluxo de Dados

```
1. Usuário clica "Estudar Módulo" no ModuleMap
   ↓
2. Cria NoteBlocks note com:
   - module_id, path_id, session_id
   - Blocks iniciais: título, @ask do primeiro KP
   ↓
3. Abre /noteblocks?noteId=X&mode=session
   ↓
4. Tutor conecta via WebSocket dedicado
   - Cada turno: tutor fala → aluno escreve/edita → tutor avalia
   - Blocos do chat são arrastáveis para o documento
   ↓
5. Exercícios:
   - Bloco @ask que o tutor avalia
   - Bloco "resumo" ao final de cada KP
   - Bloco "reflexão" ao final do módulo
   ↓
6. Ao concluir módulo:
   - Atualiza mastery path progress via API
   - Gera resumo no NoteBlocks
   - Sugere próximo módulo
```

### Integração com NoteBlocks Atual

**Blocos existentes que já servem:**
- `text` — aluno escreve anotação
- `heading` — organizar seções
- `markdown` — formatação rica
- `ask` — já existe como "@ask: pergunta para o agente"
- `question` — múltipla escolha com avaliação
- `command/output` — terminal integrado
- `attachment` — arquivos anexados

**Novos blocos necessários:**
- `chat` — bloco de citação da conversa (arrastado do chat), com `origin: "tutor"` ou `"opencode"`
- `exercise` — exercício com avaliação do tutor embutida
- `summary` — bloco especial de resumo (trackeado pelo progresso)

**Novo tipo de origem:**
- `chat` — bloco originado do chat sidebar (vs `tutor` que veio de tool call direta)

### Drag-and-Drop (Fora do Editor)

O NoteBlocks já tem DnD interno (reordenar blocos). Precisa adicionar:

1. **Chat → Nota**: Blocos no chat têm `draggable="true"`. Ao soltar no editor, cria um bloco com `origin: "chat"`, `meta: { source_turn_id }`.

2. **Explorer → Nota**: Arquivos na aba Explorer são arrastáveis. Ao soltar:
   - Imagens → `type: "attachment"` + upload automático
   - Texto/MD → `type: "markdown"` com conteúdo
   - PDF → `type: "attachment"`

3. **Indicador visual**: Linha roxa de drop (já existe no reordenamento)

### Diálogo Tutor → NoteBlocks

O tutor não precisa existir **dentro** do NoteBlocks. Ele pode:

**Opção A — Chat Sidebar (recomendado):**
- Aba dedicada ao chat com o tutor
- Blocos do chat são **citáveis** por drag para o NoteBlocks
- O chat usa a mesma infra de WebSocket `unified_ws`
- O NoteBlocks fica sempre visível ao lado

**Opção B — Tutor como bloco:**
- Cada interação do tutor vira um bloco no NoteBlocks
- Aluno responde editando/adicionando blocos
- Perde a continuidade do diálogo

**Opção C — Misto:**
- Chat sidebar para diálogo contínuo
- Blocos `@ask` no NoteBlocks para exercícios assíncronos
- Melhor dos dois mundos

Recomendação: **Opção A** com possibilidade de arrastar blocos do chat para o NoteBlocks.

## Próximos Passos (Implementação)

### Fase 1 — Infraestrutura de Sessão
1. [ ] `next_objective()` aceitar `module_id` opcional (policy.py)
2. [ ] `start_session_at_module()` no LearningService
3. [ ] Mastery capability propagar `module_id` do contexto
4. [ ] Rota `/api/v1/learning/progress/{book_id}/start-module-session`

### Fase 2 — NoteBlocks Modo Sessão
5. [ ] Criar `NoteBlocksSession` view (wrapper do NoteBlocks + chat sidebar)
6. [ ] WebSocket dedicado para sessão tutor-nota
7. [ ] Blocos de citação do chat (`origin: "chat"`)
8. [ ] Drag-and-drop do chat → nota

### Fase 3 — Pedagogia EMT em NoteBlocks
9. [ ] Adaptar `dialogue_engine.py` para NoteBlocks (pump→hint→prompt→assert)
10. [ ] Sistema de expectativas por KP
11. [ ] Avaliação de blocos escritos pelo aluno
12. [ ] Ciclo: tutor pergunta → aluno escreve → tutor avalia → aluno revisa

### Fase 4 — Explorer + Arquivos
13. [ ] Aba Explorer com FileSystemWatcher
14. [ ] Drag de arquivos externos → nota
15. [ ] Upload automático com preview

### Fase 5 — Gamificação e Revisão
16. [ ] Runner do Conhecimento integrado ao NoteBlocks
17. [ ] BKT tracking por skill na sessão
18. [ ] Spaced repetition links para revisão

## Decisões de Design

| Decisão | Escolha | Rationale |
|---------|---------|-----------|
| Chat sidebar vs inline | Sidebar (aba) | Preserva continuidade do diálogo; nota fica sempre visível |
| DnD library | HTML5 nativo (já usado) | Sem dependência extra; funciona com WebSocket |
| Blocos do chat | Citação com `origin:chat` | Rastreável; mantém metadados da conversa |
| Avaliação escrita | Tutor avalia blocos de texto | Mesmo mecanismo do EMT dialogue engine |
| Persistência | NoteBlocks atual (YAML+MD) | Já funciona; compatível com Notion sync |
| Estado da sessão | LearningProgress JSON | Já existe; compartilhado com mastery_path |

## Referências

- Graesser et al. (2018). ElectronixTutor. *IJSTEMEd*.
- Nye, Graesser & Hu (2014). AutoTutor Family Review. *IJAIED*.
- Graesser, Forsyth & Lehman (2017). Two Heads. *TCR*.
- Rus et al. (2014). DeepTutor at Scale. *LS*.
- Cai et al. (2014). Instructional Strategies Trialogue. *ARL*.
- Brawner & Graesser (2014). Natural Language Tutoring. *ARL*.
- Chi & Wylie (2014). ICAP Framework. *Educ Psychologist*.
