# Decisões e Timeline — TCC — Ingrid (MD/Desalination)

**52 sessões** | **$5.97 custo total**
**125 decisões extraídas**
**26 ferramentas/tecnologias referenciadas**

## Decisões por Categoria

### Arquitetura (9)

- **ÊNFASE EM PROJETOS IA**: Three phases - Pesquisa, Arquitetura, Implementação
- Fase 3 — **Implementação**: codar seguindo a arquitetura definida.
- Fase 3 — **Implementação**: codar seguindo a arquitetura definida.
- **Feed-forward**: regras de arquitetura via `AGENTS.md` / `SKILL.md`
- Implementação de 4 arquiteturas híbridas
- **block** (cinza 10%): nos principais do pipeline
- 4 arquiteturas híbridas implementadas
- Implementação e comparação de 4 arquiteturas híbridas
- **Unificar t1.py e t2.py** em `run_pipeline.py`: a versão com CLI e suporte a dataset aumentado (t2.py) foi escolhida como base, descartando a versão hardcoded t1.py

### Ferramentas / Stack (1)

- But I'm not sure the Notion API supports creating linked database views programmatically

### Modelo / LLM (11)

- **Model-constrained learning** (aprendizado com restrição de modelo físico)
- **Stage 0**: RMSE comparando modelos clássicos (OLS, Ridge, Lasso, Árvores, MLP sklearn, etc.)
- **Motivação:** modelo preditivo confiável permite:
- **Critério de seleção (1-SE):** 1º: melhor RMSE_CV no fluxo; 2º: modelos dentro de 1 desvio padrão do melhor; 3º: menor complexidade entre eles
- **Critério 1-SE:** seleciona-se o modelo mais simples dentro de 1 desvio padrão do melhor — vence a baseline Alim
- **`\subsection{Objetivos especificos}`**: 6 itens: estruturar base, avaliar modelo 0D, comparar familias de modelos, aplicar validacao cruzada por grupos, selecionar modelo por criterios de desempenho/generalizacao/complexidade, analisar incorporacao de informacao fisica.
- **`\subsection{Abordagens de modelagem fisica em destilacao por membranas}`** — Modelos distribuidos (Alsaadi2013, 1D), modelos CFD 2D (Ansari2022), modelos reduzidos 0D (Lisboa2024). Compromisso entre fidelidade fisica, custo computacional e aplicabilidade pratica.
- **`\subsection{Modelos orientados por dados}`** — Redes neurais (ANN_AGMD, ANN_VMD_Fouling), planejamento experimental, regressao e metodologia de superficie de resposta. Limitacao: generalizacao restrita a faixa de treinamento.
- **`\subsection{Abordagens hibridas}`** — Physics-Informed Neural Networks (PINNs), modelos residuais (Zhou2024, Zheng2021). Combinacao de conhecimento fisico como restricao/referencia.
- **`\subsection{Modelagem do Transporte de Massa}`** — Modelo Dusty Gas (difusao molecular + Knudsen). Equacoes: fluxo molar N_w, fluxo massico j_w, coeficiente B_eq, atividade da agua a_w. Linearizacao para pequenas diferencas de pressao.
- **Mover toda definição de modelos Keras** para `models/keras_builders.py` e wrappers sklearn para `models/classical.py`, eliminando repetições entre t1, t2, t3 e gerando_imagens_hrnn

### Dados / KB (9)

- **Projeto** (relation) - Projeto vinculado (database_id: 9172be34-0056-4f38-aa2a-093339bb5790)
- **Otimizador**: tentar `SGD` com momentum (às vezes generaliza melhor que Adam em dados pequenos) ou **Adam com learning rate mais baixo** (ex: `1e-4` a `1e-5`)
- **Objetivo geral:** avaliar modelagem baseada em dados e híbrida para predizer desempenho V-AGMD
- **`\subsection{Objetivo geral}`**: Avaliar modelagem baseada em dados e hibrida para predicao de desempenho V-AGMD (fluxo de permeado, temperaturas de saida).
- **AugmentedTrainRealTestGroupKFold** só ativa se a coluna `Origem_dados` existir e tiver valores sintéticos detectados; senão, cai em GroupKFold padrão
- **Slides do TCC**: `C:\Users\frota\OneDrive\Documentos\TCC\Slides-TCC-`
- **Slides (via projeto slidegen)**: `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\slides_repo`
- **TCC (documento)**: várias versões (`Codigo-revisado`, `TCC_editado`)
- **OOF RMSE** (predições out-of-fold sobre os dados de treino+val)

### Interface / UX (11)

- **Workflow Padrão**: Plan mode → Build mode
- **Refactor**: melhorar qualidade com a suite como rede de proteção
- Editar os dois slides de contribuições (`presentationTCC.tex` e `5_conclusoes.tex`) para adicionar bullets/ênfase no contexto da dessalinização.
- **Contribuições do trabalho:**
- **Contribuições:**
- **`\subsection{Sintese e lacunas}`** — L iteratura usa divisoes simples (70/15/15, 80/20) aleatorias, raramente validacao cruzada, selecao heuristic a de hiperparametros, pouca analise de extrapolacao. Este trabalho contribui com validacao rigorosa + informacao fisica.
- **`\subsection{Modelagem do Transporte de Calor}`** — Rede de resistencias termicas: convecao (R_f, R_c), conducao (R_m membrana, R_g air gap), calor latente (q_v = j_w * h_lv). Resistencia equivalente R_eq, fluxo termico q'' = (T_f - T_c)/R_eq.
- **Slides**: `41901fd` em `github.com/frotaluiza/Slides-TCC-`
- **Tese**: `57115be` em `github.com/frotaluiza/TCC---Distila-o-de-Membranas`
- Revisar, organizar e modularizar todos os códigos do TCC (pastas CodFin) criando uma versão limpa e unificada em Codigo-revisado/, sem alterar os arquivos originais.
- **Nenhum arquivo original pode ser alterado** (CodFin/*.py, .csv, .json permanecem intocados)

### Outros (84)

- **Red**: escrever teste que falha (proibido implementar)
- **Green**: código mínimo para passar (proibido modificar o teste)
- **S**cenario → **T**race → **A**ssess → **R**efine
- **Feedback**: hooks determinísticos (`PreToolUse` para travar diretórios de teste)
- **Li2025PINN** — Li & Li — *PINNs para modelagem e diagnóstico de degradação em membranas RO* (DWT, 2025)
- **Helali2025PINN** — Helali et al. — *PINNs para monitoramento de desempenho em SWRO* (Water, 2025)
- "Zohan" is a model architecture name used in the thesis (ZohanResidual, ZohanHPD, ZohanHRNN, etc.) - it's not an author name. These are model architectures implemented by the user.
- **brave-meadow.md** (869 lines) - extensive 0D model discussions, but it's from June 3-11 based on its content
- **argumentacao_pinn_tcc.md** (784 lines) - about PINN replacing 0D model, dated June 11
- `swift-knight` - "Implementação de PINNs a partir de artigos" (more about replicating in DeepTutor)
- `swift-knight` - "Implementação de PINNs a partir de artigos" - 2026-06-22 (but the doc says 2026-06-15)
- The `swift-knight` session was about implementing PINNs in DeepTutor
- `Codigo-revisado/scripts/testar_surrogate.py` — testa o surrogate vs colunas phy + implementa PINN híbrida
- **Surrogate-regularized MLP** (ou *physics-regularized NN*)
- *Knowledge distillation* de um simulador físico
  *+69 mais...*


## Timeline de Sessões

| Data | Título | Agente | Custo | Resumo |
|------|--------|--------|-------|--------|
| 2026-07-12 | [Find Zotero and TCC PDFs (@explore subagent)](sessoes/glowing-squid.md) | explore | $0.01 |  |
| 2026-07-12 | [Leitura artigos TCC via scihub MCP](sessoes/jolly-falcon.md) | build | $0.38 |  |
| 2026-07-12 | [Find TCC repo and bib files (@explore subagent)](sessoes/lucky-panda.md) | explore | $0.02 |  |
| 2026-07-12 | [TCC project state check (@explore subagent)](sessoes/misty-rocket.md) | explore | $0.01 |  |
| 2026-07-11 | [Read Ingrid thesis lit review structure (@explore subagent)](sessoes/calm-rocket.md) | explore |  |  |
| 2026-07-11 | [Search flux importance SEC GOR papers (@explore subagent)](sessoes/eager-falcon.md) | explore |  |  |
| 2026-07-11 | [Search flow rate and hydraulic pressure in MD (@explore suba](sessoes/glowing-meadow.md) | explore |  |  |
| 2026-07-11 | [Search VMD vs V-AGMD difference (@explore subagent)](sessoes/glowing-pixel.md) | explore |  |  |
| 2026-07-11 | [Search flux importance in user's papers (@explore subagent)](sessoes/happy-otter.md) | explore |  |  |
| 2026-07-11 | [Search MD configurations tradeoffs (@explore subagent)](sessoes/playful-comet.md) | explore |  |  |
| 2026-07-11 | [Search MD vapor pressure sources (@explore subagent)](sessoes/playful-planet.md) | explore |  |  |
| 2026-07-11 | [Search PDFs for MD context (@explore subagent)](sessoes/proud-wizard.md) | explore |  |  |
| 2026-07-11 | [Search existing papers for flux importance (@explore subagen](sessoes/swift-wizard.md) | explore |  |  |
| 2026-07-08 | [Find TCC code files (@explore subagent)](sessoes/crisp-rocket.md) | explore |  |  |
| 2026-07-08 | [Explore TCC slides directory (@explore subagent)](sessoes/witty-orchid.md) | explore |  |  |
| 2026-07-07 | [Find MD review papers in TCC folders (@explore subagent)](sessoes/crisp-meadow.md) | explore |  |  |
| 2026-07-07 | [Find CV metrics in TCC code (@explore subagent)](sessoes/curious-nebula.md) | explore |  |  |
| 2026-07-06 | [Find overlay plot scripts (@explore subagent)](sessoes/glowing-planet.md) | explore | $0.01 |  |
| 2026-07-02 | [Find per-target best params (@explore subagent)](sessoes/kind-knight.md) | explore | $0.02 |  |
| 2026-07-01 | [Find results data files (@explore subagent)](sessoes/calm-orchid.md) | explore | $0.02 |  |
| 2026-07-01 | [Find TCC slides repo and desalination branches slide (@explo](sessoes/cosmic-moon.md) | explore | $0.01 |  |
| 2026-07-01 | [Explore TCC project structure (@explore subagent)](sessoes/misty-tiger.md) | explore | $0.02 |  |
| 2026-07-01 | [Explore slides and fluxogram (@explore subagent)](sessoes/neon-tiger.md) | explore | $0.01 |  |
| 2026-07-01 | [Rodada que gerou dados do TCC](sessoes/sunny-forest.md) | build | $1.68 |  |
| 2026-06-30 | [Surrogate do modelo 0D](sessoes/gentle-forest.md) | build | $0.06 |  |
| 2026-06-30 | [Read all TCC chapters (@explore subagent)](sessoes/playful-meadow.md) | explore | $0.02 |  |
| 2026-06-27 | [Extract all slide details (@explore subagent)](sessoes/playful-lagoon.md) | explore | $0.01 |  |
| 2026-06-26 | [Explore TCC and slides structure (@explore subagent)](sessoes/quick-engine.md) | explore | $0.01 |  |
| 2026-06-26 | [Acessar repositório de slides e TCC](sessoes/sunny-eagle.md) | build | $0.48 |  |
| 2026-06-25 | [Adicionar testes opencode framework IA](sessoes/clever-otter.md) | build | $0.07 |  |
| 2026-06-22 | [Entrada logs opencode e live doc TCC](sessoes/eager-forest.md) | build | $0.11 |  |
| 2026-06-21 | [Find C_NaCl unit in model 0D (@explore subagent)](sessoes/glowing-rocket.md) | explore | $0.01 |  |
| 2026-06-15 | [Logs automáticos para contribuições no TCC](sessoes/lucky-nebula.md) | build | $0.08 |  |
| 2026-06-15 | [Find Luc appendix images (@explore subagent)](sessoes/nimble-sailor.md) | explore | $0.02 |  |
| 2026-06-12 | [Vender melhor o peixe do TCC](sessoes/quick-lagoon.md) | build | $1.56 |  |
| 2026-06-11 | [Contexto dashboard 2026](sessoes/neon-planet.md) | plan | $0.00 |  |
| 2026-06-11 | [Chat do projeto TCC](sessoes/neon-rocket.md) | build | $0.39 |  |
| 2026-06-08 | [Organizar reunião TCC: código e slides](sessoes/happy-nebula.md) | build | $0.35 |  |
| 2026-06-04 | [Como acessar todas as seções](sessoes/cosmic-panda.md) | build | $0.01 |  |
| 2026-06-04 | [Abrir sessões do opencode.db](sessoes/playful-canyon.md) | build | $0.01 |  |
| 2026-06-03 | [Sessões perdidas do TCC](sessoes/curious-harbor.md) | build | $0.05 |  |
| 2026-06-03 | [Criar sessão opencode com dados de sessão anterior](sessoes/curious-lagoon.md) | build | $0.00 |  |
| 2026-06-02 | [Explore Stage 2 codebase (@explore subagent)](sessoes/curious-orchid.md) | explore |  |  |
| 2026-06-01 | [Extract per-output RMSE (@explore subagent)](sessoes/brave-panda.md) | explore |  |  |
| 2026-05-31 | [List all output files (@explore subagent)](sessoes/jolly-comet.md) | explore |  |  |
| 2026-05-31 | [Investigate original outputs (@explore subagent)](sessoes/mighty-wizard.md) | explore |  |  |
| 2026-05-31 | [Find 0D comparison script (@explore subagent)](sessoes/misty-sailor.md) | explore |  |  |
| 2026-05-31 | [Find opencode session files (@explore subagent)](sessoes/stellar-pixel.md) | explore |  |  |
| 2026-05-30 | [New session - 2026-05-30T20:18:30.225Z](sessoes/quick-tiger.md) | build | $0.53 |  |
| 2026-05-29 | [Find fluxograma, espacos busca, HPD, scatter files (@explore](sessoes/clever-island.md) | explore |  |  |
| 2026-05-29 | [Analyze template image styles (@explore subagent)](sessoes/nimble-meadow.md) | explore |  |  |
| 2026-05-29 | [Analyze corrections plan (@explore subagent)](sessoes/quiet-harbor.md) | explore |  |  |
