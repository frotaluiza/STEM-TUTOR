# Memphis Papers Analysis — Gaps vs DeepTutor HKU

## Metodologia
- Queries RAG contra a KB `memphis-references` (17 documentos)
- Web search por implementacoes open-source
- Cross-reference com o codigo HKU DeepTutor

---

## 1. Expectation/Misconception Tailoring (EMT)

### Como funciona no AutoTutor
AutoTutor mantem listas de **expectativas** (respostas ideais esperadas) e **misconceptions** (erros comuns) para cada tarefa. Conforme o aluno responde, o sistema compara as contribuicoes usando pattern-matching e avaliacao semantica, entao gera hints, pumps e prompts para guiar o aluno a cobrir todas as expectativas enquanto corrige misconceptions. O processo dura de 30 a 100 turnos ate que todas as expectativas sejam cobertas.

### Gap no DeepTutor HKU
HKU usa LLM generico sem estrutura de EMT. O LLM decide livremente como responder, sem matching contra expectativas pre-definidas.

### Open Source Disponivel
- **GnuTutor** (C#, Andrew Olney/U Memphis) — implementacao original do AutoTutor, usa state table para processar input do aluno
- **GuruTutor** (GitHub: aolney/GuruTutor) — redesign do GnuTutor + sistema Guru

### Impacto x Esforco
- **Impacto**: Alto — personalizacao real baseada em conhecimento do aluno
- **Esforco**: Alto — requer definir expectativas/misconceptions por topico, ou usar LLM para gera-las automaticamente
- **Prioridade**: Media (futuro)

---

## 2. Dialogue Move Engine (Hint → Pump → Prompt → Expectation → Summary)

### Como funciona no AutoTutor
O motor comeca com uma Main Question, entao cicla:
1. **Hint** — pergunta leading que guia o aluno a uma ideia-chave
2. **Prompt** — pede uma palavra/frase especifica da ideia
3. **Pump** — "Algo mais?" incentiva elaboracao
4. **Expectation** — quando o aluno cobre a expectativa, o tutor reconhece
5. **Summary** — consolidacao da resposta correta

### Gap no DeepTutor HKU
HKU nao tem estrutura de dialogue moves. O LLM gera respostas livres sem sequencia pedagogica.

### Open Source Disponivel
Mesmo que EMT: GnuTutor e GuruTutor implementam o motor de dialogue moves.

### Impacto x Esforco
- **Impacto**: Alto — qualidade pedagogica comprovada por decadas de pesquisa
- **Esforco**: Medio — implementar o state machine de moves e possivel, mas o conteudo (hints/prompts) precisa ser gerado por LLM ou pre-definido
- **Prioridade**: Alta — implementar como camada sobre o LLM atual

---

## 3. Trialog (3-Agent Architecture)

### Como funciona no AutoTutor
Trialog envolve 3 agentes:
- **Tutor** — guia a conversa e avalia
- **Peer Student** — aprendiz artificial que comete erros para o aluno humano corrigir
- **Mentor** — fornece suporte quando necessario

O aluno humano interage com os agentes, ensinando o peer e sendo avaliado pelo tutor.

### Gap no DeepTutor HKU
HKU so tem 1:1 tutor-aluno. Nao ha peer agent ou mentor agent.

### Open Source Disponivel
- **Ruffle&Riley** (GitHub: rschmucker/ruffle-and-riley) — trialog onde humano ensina student agent (Ruffle) com suporte de professor agent (Riley)
- **ASTRA** (GitHub: solex2006/astra-social-tutor) — multi-agent com Pedagogical Tutor Agent + Collaborative Group Agent

### Impacto x Esforco
- **Impacto**: Medio — util para aprendizado colaborativo e ensino entre pares
- **Esforco**: Alto — requer arquitetura multi-agente, gerenciamento de estados paralelos
- **Prioridade**: Baixa (futuro distante)

---

## 4. BKT/IRT — Bayesian Student Model

### Como funciona no Memphis
- **BKT** (Bayesian Knowledge Tracing): modelo probabilistico que estima se o aluno sabe um conceito com base em acertos/erros, considerando guess (chute) e slip (erro por descuido)
- **IRT** (Item Response Theory): modela a proficiencia do aluno e a dificuldade de cada questao em uma escala comum

### Implementacao no HKU
HKU usa scoring deterministico (recency-weighted 0.5-1.0) com JSON persistence. Nao ha modelo probabilistico.

### Open Source Disponivel
- **pyBKT** (Python, MIT) — biblioteca completa de BKT com variantes (individual student priors, item-specific guess/slip)
- **StanBKT** — usa inferencia Bayesiana via Stan com incerteza quantificada
- **OATutor** (GitHub: micadibugit/OATutor) — sistema adaptativo com BKT integrado em ReactJS

### Impacto x Esforco
- **Impacto**: Alto — BKT permite estimar mastery com incerteza, essencial para personalizacao
- **Esforco**: Baixo — pyBKT é pip installavel, so integrar ao pipeline de mastery
- **Prioridade**: **Alta** — implementacao rapida com pyBKT

---

## 5. Student Leveling (Onboarding)

### Como funciona
Nye et al. 2014 descreve avaliacao inicial para calibrar conhecimento do aluno antes da sessao. Determina ponto de partida, ritmo e profundidade das explicacoes.

### Implementado no NoteBlocks
✅ **Fase 3.5 implementada**: modal de nivelamento com 4 niveis + descricao personalizada.
O nivel é salvo no Note (campo `level`) e enviado ao agente como contexto.

### Proximo passo
Usar o nivel para selecionar automaticamente o ponto de partida no curriculum do DeepTutor.

---

## Relatorio de Viabilidade — Priorizacao

| Item | Impacto | Esforco | Prioridade |
|------|---------|---------|------------|
| **Dialogue Move Engine** (Hint→Pump→Prompt→Summary) | Alto | Medio | **Alta** |
| **BKT/IRT Student Model** (pyBKT integration) | Alto | Baixo | **Alta** |
| **EMT — Expectation/Misconception Tailoring** | Alto | Alto | Media |
| **Student Leveling** (ja implementado) | Alto | Baixo | ✅ Feito |
| **Trialog (3-agent)** | Medio | Alto | Baixa |

---

## 6. Estrategia de Sequenciamento — Escada Logica (Logical Ladder)

### Como o AutoTutor ordena as expectativas

A ordenacao das expectativas na "escada logica" do AutoTutor segue:

1. **Relacoes de pre-requisito** — expectativas fundamentais ou logicamente anteriores vem primeiro
2. **Progressao natural do raciocinio** — nao baseado em dificuldade, mas na sequencia ideal de resolucao do problema
3. **Script pre-definido** — cada problema tem um curriculum script onde as expectativas sao sequenciadas conforme o caminho ideal de solucao
4. **Cobertura sistematica** — o tutor cobre cada expectativa por vez (hints → prompts → assertions) antes de avancar

### A escada de moves (do mais aberto ao mais especifico)

```
Nivel 1 — PUMP       "Me fale mais sobre isso"
Nivel 2 — HINT       "Pense sobre a relacao entre X e Y"
Nivel 3 — PROMPT     "Qual o valor de X quando Y = 0?"
Nivel 4 — ASSERTION  "Entao a resposta e: ..." (correcao)
Nivel 5 — SUMMARY    "Recapitulando: ..." (fecho)
```

### Aplicacao no Runner do Conhecimento

| Escada Memphis | Runner Game |
|----------------|-------------|
| Pump | Frase aparece INTACTA — aluno so pula e le |
| Hint | Frase aparece com **parte em destaque/sublinhado** guiando o olhar |
| Prompt | Frase aparece **incompleta** — aluno preenche mentalmente ao pular |
| Assertion | Apos colisao — tutor mostra a frase corrigida |
| Summary | **Pop-up de pergunta** no final da corrida — testa se absorveu |
| Retorno apos erro | Frases seguintes sao REORDENADAS: volta ao pre-requisito anterior e sobe de novo |

### Estrutura da Sessao

```
Main Question → Expectation 1 → Expectation 2 → ... → Expectation N
                    │                │                    │
              Pump→Hint→Prompt  Pump→Hint→Prompt    Pump→Hint→Prompt
              (se erro: assertion + retorno ao topo da escada)
```

### Recomendacao Imediata (atualizada)
1. **BKT/IRT** — integrar pyBKT ao pipeline de mastery do DeepTutor (substituir scoring deterministico)
2. **Dialogue Move Engine** — criar camada de state machine entre o prompt do usuario e o LLM, forçando sequencia Hint→Prompt→Pump→Summary
3. **Runner Logical Ladder** — as frases no Runner seguem a ordem de pre-requisitos: fundamentos primeiro, avancados depois. Apos erro, volta ao pre-requisito anterior.

### Open Source para Aproveitar
- `pip install pybkt` → integracao direta
- `github.com/aolney/GuruTutor` → referencia para dialogue moves
- `github.com/rschmucker/ruffle-and-riley` → referencia para trialog
