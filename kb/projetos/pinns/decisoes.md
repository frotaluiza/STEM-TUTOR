# Decisões e Timeline — PINNs

**5 sessões** | **$6.87 custo total**
**20 decisões extraídas**
**27 ferramentas/tecnologias referenciadas**

## Decisões por Categoria

### Arquitetura (6)

- **Contexto:** Implementação de agente PINN no DeepTutor, Burgers equation (DeepXDE + PyTorch), replicação de 4 arquiteturas híbridas do TCC V-AGMD.
- **Decisões:** Uso de `scikeras` + Pipeline + YScalerRegressor (como no TCC original); sweep conjunto L2+ω+physics_norm para Luc.
- **Resultados:** Todas as 4 arquiteturas bateram os RMSE do TCC:
- **Pipeline padrão**: scikeras + YScalerRegressor + Pipeline(StandardScaler)
- **4 arquiteturas híbridas**: ZohanResidual, ZohanHRNN, ZohanHPD, Luc
- **Problema**: O modelo atual (deepseek-v4-flash) não tem visão. Precisamos de um serviço externo.

### Ferramentas / Stack (1)

- TabTransformer++ - residual stacking

### Dados / KB (1)

- Implementar loss function com os dados

### Outros (12)

- **Próximos passos:** Papers with Code para PINN, varrer Zotero, aplicar SkillOpt.
- **Projetos vinculados:** 3 - AI STEM Tutor, 4 - Agente PINN Híbrido.
- **Otimização per-output**: Alim_T_out prefere logistic+alpha alto; Flux prefere relu+alpha baixo
- **Grid restrito**: L2 ao redor da baseline, sweep conjunto L2+ω para Luc
- Pro: Easy to implement (just change the target index in the scorer)
- **Opções**:
- That implements PINN to approximate a function
- **INC** (Implicit Neural Correction): github.com/tum-pbs/INC - Hybrid NN + PDE solver
- **HyResPINNs**: Hybrid Residual Networks for adaptive Neural/RBF
- **PASSC**: FEM + PINN correction for convection-dominated transport
- **HyPINO**: Multi-physics neural operator with residual refinement
- **PASSC**: FEM + PINN correction


## Timeline de Sessões

| Data | Título | Agente | Custo | Resumo |
|------|--------|--------|-------|--------|
| 2026-06-17 | [Search PINNs MD papers (@general subagent)](sessoes/gentle-nebula.md) | general | $0.01 |  |
| 2026-06-17 | [Acessar live doc da sessão PINNs](sessoes/hidden-moon.md) | plan | $4.27 |  |
| 2026-06-17 | [Search PINNs in MD papers (@general subagent)](sessoes/stellar-nebula.md) | general | $0.00 |  |
| 2026-06-17 | [Search PINNs AGMD Consensus (@general subagent)](sessoes/tidy-mountain.md) | general | $0.01 |  |
| 2026-06-14 | [Implementação de PINNs a partir de artigos](sessoes/swift-knight.md) | build | $2.58 |  |
