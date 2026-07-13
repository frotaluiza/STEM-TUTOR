# Decisões e Timeline — Luc-Repport

**20 sessões** | **$8.30 custo total**
**200 decisões extraídas**
**8 ferramentas/tecnologias referenciadas**

## Decisões por Categoria

### Arquitetura (5)

- **Unificar t1.py e t2.py** em `run_pipeline.py`: a versão com CLI e suporte a dataset aumentado (t2.py) foi escolhida como base, descartando a versão hardcoded t1.py
- **Unificar t1.py e t2.py** em `run_pipeline.py`: a versão com CLI e suporte a dataset aumentado (t2.py) foi escolhida como base, descartando a versão hardcoded t1.py
- **Unificar t1.py e t2.py** em `run_pipeline.py`: a versão com CLI e suporte a dataset aumentado (t2.py) foi escolhida como base, descartando a versão hardcoded t1.py
- **Unificar t1.py e t2.py** em `run_pipeline.py`: a versão com CLI e suporte a dataset aumentado (t2.py) foi escolhida como base, descartando a versão hardcoded t1.py
- **Unificar t1.py e t2.py** em `run_pipeline.py`: a versão com CLI e suporte a dataset aumentado (t2.py) foi escolhida como base, descartando a versão hardcoded t1.py

### Modelo / LLM (5)

- **Mover toda definição de modelos Keras** para `models/keras_builders.py` e wrappers sklearn para `models/classical.py`, eliminando repetições entre t1, t2, t3 e gerando_imagens_hrnn
- **Mover toda definição de modelos Keras** para `models/keras_builders.py` e wrappers sklearn para `models/classical.py`, eliminando repetições entre t1, t2, t3 e gerando_imagens_hrnn
- **Mover toda definição de modelos Keras** para `models/keras_builders.py` e wrappers sklearn para `models/classical.py`, eliminando repetições entre t1, t2, t3 e gerando_imagens_hrnn
- **Mover toda definição de modelos Keras** para `models/keras_builders.py` e wrappers sklearn para `models/classical.py`, eliminando repetições entre t1, t2, t3 e gerando_imagens_hrnn
- **Mover toda definição de modelos Keras** para `models/keras_builders.py` e wrappers sklearn para `models/classical.py`, eliminando repetições entre t1, t2, t3 e gerando_imagens_hrnn

### Dados / KB (20)

- **AugmentedTrainRealTestGroupKFold** só ativa se a coluna `Origem_dados` existir e tiver valores sintéticos detectados; senão, cai em GroupKFold padrão
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- **AugmentedTrainRealTestGroupKFold** só ativa se a coluna `Origem_dados` existir e tiver valores sintéticos detectados; senão, cai em GroupKFold padrão
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- **AugmentedTrainRealTestGroupKFold** só ativa se a coluna `Origem_dados` existir e tiver valores sintéticos detectados; senão, cai em GroupKFold padrão
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- **AugmentedTrainRealTestGroupKFold** só ativa se a coluna `Origem_dados` existir e tiver valores sintéticos detectados; senão, cai em GroupKFold padrão
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
- É só ir no chat e perguntar sobre a tese que ele vai usar o RAG automaticamente
  *+5 mais...*

### Interface / UX (25)

- Revisar, organizar e modularizar todos os códigos do TCC (pastas CodFin) criando uma versão limpa e unificada em Codigo-revisado/, sem alterar os arquivos originais.
- **Nenhum arquivo original pode ser alterado** (CodFin/*.py, .csv, .json permanecem intocados)
- **Abdulrahim et al. (2026)** - "CFD-guided surrogate modeling and interaction analysis of AGMD" - Uses NN to approximate CFD results.
- **Abdulrahim et al. (2026)** - "CFD-guided surrogate modeling and interaction analysis of AGMD" - Uses NN to approximate CFD results.
- Revisar, organizar e modularizar todos os códigos do TCC (pastas CodFin) criando uma versão limpa e unificada em Codigo-revisado/, sem alterar os arquivos originais.
- **Nenhum arquivo original pode ser alterado** (CodFin/*.py, .csv, .json permanecem intocados)
- **Abdulrahim et al. (2026)** - "CFD-guided surrogate modeling and interaction analysis of AGMD" - Uses NN to approximate CFD results.
- Revisar, organizar e modularizar todos os códigos do TCC (pastas CodFin) criando uma versão limpa e unificada em Codigo-revisado/, sem alterar os arquivos originais.
- **Nenhum arquivo original pode ser alterado** (CodFin/*.py, .csv, .json permanecem intocados)
- **Abdulrahim et al. (2026)** - "CFD-guided surrogate modeling and interaction analysis of AGMD" - Uses NN to approximate CFD results.
- **Abdulrahim et al. (2026)** - "CFD-guided surrogate modeling and interaction analysis of AGMD" - Uses NN to approximate CFD results.
- Revisar, organizar e modularizar todos os códigos do TCC (pastas CodFin) criando uma versão limpa e unificada em Codigo-revisado/, sem alterar os arquivos originais.
- **Nenhum arquivo original pode ser alterado** (CodFin/*.py, .csv, .json permanecem intocados)
- **Abdulrahim et al. (2026)** - "CFD-guided surrogate modeling and interaction analysis of AGMD" - Uses NN to approximate CFD results.
- **Abdulrahim et al. (2026)** - "CFD-guided surrogate modeling and interaction analysis of AGMD" - Uses NN to approximate CFD results.
  *+10 mais...*

### Outros (145)

- **Manter baseline_best_params fixos** em `run_hrnn_only.py` (idêntico ao original t3.py) em vez de buscar dinamicamente os do Stage 1
- **Manter import relativo** com `sys.path.insert(0, ...)` nos scripts executáveis para não exigir instalação do pacote
- **Keras layers custom** (`SliceXPart`, `SliceYPhyPart`, `LucHybridLoss`) foram registradas com `@tf.keras.utils.register_keras_serializable(package="AGMD")` para permitir serialização
- **LucHybridLoss** espera `y_true_aug` com shape (n, 2m) — concat de true + physics, e `y_pred_2m` — concat de prediction duplicada: `[y_hat, y_hat]`
- **Score é RMSE negativo** (neg_mean_squared_error), sempre convertido para RMSE natural nas tabelas finais
- **3 variáveis de saída**: fluxo de permeado (J), T_alim_out, T_ref_out
- **GroupKFold com K=3** (um regime experimental por fold)
- **RMSE do fluxo** como métrica principal de seleção
- **Best subset** das 5 variáveis; **binning descartado** (sem ganho consistente)
- **Vencedor: ZohanResidual** (Ŷ = Y_físico + Ŷ_residual)
- **Requena et al. (2023)** - "Application of machine learning to characterize the permeate quality in pilot-scale V-AGMD" - This uses an NN for permeate quality, not for performance prediction with hybrid architectures.
- **Lisboa et al. (2024)** - "A reduced model for pilot-scale V-AGMD modules" - The 0D physical model.
- **~82 resultados** para V-AGMD (maioria modelagem física pura)
- **3 variáveis de saída**: fluxo de permeado (J), T_alim_out, T_ref_out
- **GroupKFold com K=3** (um regime experimental por fold)
  *+130 mais...*


## Timeline de Sessões

| Data | Título | Agente | Custo | Resumo |
|------|--------|--------|-------|--------|
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/clever-knight.md) | None | $0.38 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/curious-river.md) | None | $0.38 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/gentle-canyon.md) | None | $0.38 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/glowing-canyon.md) | None | $0.32 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/hidden-meadow.md) | None | $0.38 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/jolly-moon.md) | None | $0.32 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/jolly-star.md) | None | $0.38 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/lucky-moon.md) | None | $0.37 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/lucky-squid.md) | None | $0.37 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/mighty-mountain.md) | None | $0.38 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/quick-knight.md) | None | $0.38 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/quiet-lagoon.md) | None | $0.38 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/quiet-meadow.md) | None | $0.38 |  |
| 2026-07-01 | [Abrir Luc-Repport no Adobe (fork #1)](sessoes/witty-circuit.md) | None | $0.38 |  |
| 2026-06-28 | [Abrir Luc-Repport no Adobe](sessoes/shiny-island.md) | build | $0.44 |  |
| 2026-06-03 | [New session - 2026-05-30T20:18:30.225Z (fork #1)](sessoes/brave-meadow.md) | build | $0.60 |  |
| 2026-06-03 | [New session - 2026-05-30T20:18:30.225Z (fork #1)](sessoes/eager-otter.md) | build | $0.74 |  |
| 2026-06-03 | [New session - 2026-05-30T20:18:30.225Z (fork #1)](sessoes/gentle-otter.md) | None | $0.45 |  |
| 2026-06-03 | [New session - 2026-05-30T20:18:30.225Z (fork #1)](sessoes/hidden-nebula.md) | None | $0.45 |  |
| 2026-06-03 | [New session - 2026-05-30T20:18:30.225Z (fork #1)](sessoes/stellar-squid.md) | None | $0.45 |  |
