---
slug: gentle-nebula
title: "Search PINNs MD papers (@general subagent)"
date: 2026-06-17
agent: general
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h01m54s
messages: 11
parts: 42
cost: 0.012347
tokens_input: 64294
tokens_output: 4843
tokens_reasoning: 3661
tokens_cache_read: 344704
tokens_cache_write: 0
created: "2026-06-17 22:08:49 UTC"
updated: "2026-06-17 22:10:44 UTC"
---

Sessão com **11 messages**, **42 parts**, agente **general**, modelo **deepseek-v4-flash** | 💰 $0.0123 | 💾 cache read: 344.7K | ⏱️ 0h01m54s

## 👤 Usuário (2026-06-17 22:08:49 UTC)

Pesquise na web artigos acadêmicos sobre Physics-Informed Neural Networks (PINNs) aplicadas a Membrane Distillation (MD) ou dessalinização.

Use os termos de busca:
1. "Physics-Informed Neural Networks" + "membrane distillation"
2. "PINNs" + "membrane distillation" 
3. "physics-informed machine learning" + "desalination"
4. "physics-guided neural network" + "membrane"

Para cada artigo encontrado, forneça:
- Título completo
- Autores e ano
- Periódico
- Breve descrição
- Como se relaciona com destilação por membranas

Procure artigos de 2020 a 2026. Retorne no mínimo 5 artigos (além do Andrés-Mañas que já conhecemos).

## 🤖 Assistente (2026-06-17 22:08:49 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to search for academic articles about Physics-Informed Neural Networks (PINNs) applied to Membrane Distillation (MD) or desalination. Let me search the web using the specified terms.

Let me use the composio tools for web searching since I have access to a web search tool there.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 22:08:55 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I'll use the COMPOSIO_SEARCH_SCHOLAR tool to search for academic papers with the four query combinations, and also COMPOSIO_SEARCH_WEB for broader coverage. Let me run all searches in parallel.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 22:09:03 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I got a lot of results. Let me process the saved file to extract all the articles properly, deduplicate them, and organize them. The data is in /mnt/files/mex/herd.json. Let me use the remote workbench to parse and organize the results.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 22:09:12 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive list of articles. Let me fetch more details for the most relevant ones - the ones directly related to PINNs + membrane distillation or desalination. Let me also get the remaining pages of results for the most targeted query (search 1 and 2) to find more relevant articles.

Let me identify the most relevant articles from the results so far:

**Directly related to PINNs + MD/Desalination:**

1. **Shirzadi et al. (2024)** - "Novel physics-informed optimization framework for complex multi-physics problems: Implementation for a sweeping gas membrane distillation module" - Chemical Engineering Journal. **Directly applies PIPO (related to PINNs) to SGMD.** 13 citations.

2. **Shahouni & Abrofarakh (2026)** - "...learning framework with blockchain for dynamic optimization of flux, fouling and heavy metal rejection in metal foam-enhanced direct contact membrane distillation..." - Engineering Applications of AI. **FO-PINNs applied to DCMD.** 1 citation.

3. **V Arya, A Agarwal, C Bakli (2026)** - "Physics-informed machine learning for electroosmotic flow in graphene nanochannels: Towards next-generation desalination membranes" - Desalination. **PINN model for desalination membranes.** 2 citations.

4. **S Garakani, JW Chew (2025)** - "Development of physics-informed machine-learning models to enhance understanding and prediction of membrane fouling" - Journal of Membrane Science. **Physics-informed ML for membrane fouling.** 21 citations.

5. **S Garakani, M Hassanabadi, JW Chew (2026)** - "A physics-informed neural network for interpretable membrane-fouling prediction with adaptive transitions between fouling mechanisms" - Separation and Purification Technology. **PINN for membrane fouling.** 1 citation.

6. **S Helali et al. (2025)** - "Harnessing physics-informed neural networks for performance monitoring in SWRO desalination" - Water (MDPI). **PINNs for SWRO desalination.** 5 citations.

7. **G Fu et al. (2025)** - "Physics-informed neural network-based prediction of permeation performance in reverse osmosis membrane elements" - Environmental Science: Water Research & Technology (RSC). **PINNs for RO membrane fouling prediction.** 2 citations.

8. **Y Chen et al. (2024)** - "Transfer learning and pretraining enhanced physics-informed machine learning for closed-circuit reverse osmosis modeling" - Desalination. **Physics-informed ML for RO.** 14 citations.

9. **M Li, J Li (2025)** - "Physics-informed neural networks for modeling and diagnosing degradation in reverse osmosis membranes" - Desalination and Water Treatment. **PINNs for RO membranes.** 4 citations.

10. **H Gao et al. (2025)** - "Wrinkle-Free Membrane Design Based on Physics-Informed Neural Network" - International Journal of Applied Mechanics. **PINN for membrane design (structural, not MD).** 1 citation.

11. **R Türker Karalı** - "Tuzlu su desalinasyonunda yapay zeka kullanımı" (Use of artificial intelligence in seawater desalination) - Masters thesis, ITU. **PINNs for desalination.**

Let me now do a second round of searches to see if I missed anything, particularly focusing on the most targeted search terms. Let me also look at the next pages for the most specific searches.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 22:09:26 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now look at the most relevant articles in detail. I found a very interesting reference in the last search:

From search 4 (index 3): In the snippet of the Peralez & Nadri (2024) paper:
"A deep-learning-based observer for state estimation of direct contact membrane distillation"

This seems very relevant! Let me fetch more details for the most important articles. Let me also look up the "Andrés-Mañas" article the user mentioned.

Key articles directly relevant to PINNs + MD:

1. **Shirzadi et al. (2024)** - "Novel physics-informed optimization framework for complex multi-physics problems: Implementation for a sweeping gas membrane distillation module" - Chemical Engineering Journal. **Directly applies PIPO (Physics-Informed Physics-Optimized) framework to SGMD.**

2. **Shahouni & Abrofarakh (2026)** - "Fractional-order physics-informed neural network (FO-PINN) deep learning framework with blockchain for dynamic optimization of flux, fouling and heavy metal rejection in metal foam-enhanced direct contact membrane distillation" - Engineering Applications of Artificial Intelligence. **Directly applies FO-PINNs to DCMD.**

3. **Shirzadi et al. (probably the same group as Shirzadi above)** - There's another one: "Physics-informed neural networks for membrane fouling" related papers.

4. **Helali et al. (2025)** - "Harnessing physics-informed neural networks for performance monitoring in SWRO desalination" - Water (MDPI). **PINNs for seawater RO desalination performance monitoring.**

5. **V Arya et al. (2026)** - "Physics-informed machine learning for electroosmotic flow in graphene nanochannels: Towards next-generation desalination membranes" - Desalination. **PINN model for desalination membranes at nano-scale.**

6. **Garakani & Chew (2025)** - "Development of physics-informed machine-learning models to enhance understanding and prediction of membrane fouling" - Journal of Membrane Science.

7. **Garakani, Hassanabadi & Chew (2026)** - "A physics-informed neural network for interpretable membrane-fouling prediction with adaptive transitions between fouling mechanisms" - Separation and Purification Technology.

8. **Y Chen et al. (2024)** - "Transfer learning and pretraining enhanced physics-informed machine learning for closed-circuit reverse osmosis modeling" - Desalination.

9. **G Fu et al. (2025)** - "Physics-informed neural network-based prediction of permeation performance in reverse osmosis membrane elements" - Environmental Science: Water Research & Technology.

10. **M Li, J Li (2025)** - "Physics-informed neural networks for modeling and diagnosing degradation in reverse osmosis membranes" - Desalination and Water Treatment.

11. **L Liu, J Luo, Y Heng (2025)** - "Fast solution of 3D transport processes using a physics-informed neural network with embedded transfer learning" - Separation and Purification Technology. (about UPMs - ultrapermeable membranes for water treatment/desalination)

12. **Türker Karalı** - "Tuzlu su desalinasyonunda yapay zeka kullanımı" (Use of AI in seawater desalination) - Master's thesis at ITU. **Mentions PINNs for desalination.**

13. **Rahman & Hazra (2024)** - "Advancing computational fluid dynamics through machine learning: a review" - **Mentions PINNs in MD.**

Let me also fetch the Andrés-Mañas paper the user knows about, to make sure I don't duplicate it. Let me search for it.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 22:09:35 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me fetch the Andrés-Mañas paper to check, and also fetch details of the key articles I found.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 22:09:42 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me search for the Andrés-Mañas paper specifically to identify it, and also fetch the key article pages for more details.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 22:09:56 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The Sciencedirect pages timed out (paywall). That's fine - I have enough information from the snippets to compile the results. The Andrés-Mañas search returned a 2026 paper by Ghim et al. about "Key Considerations in Developing Photothermal Membrane Distillation" which mentions physics-informed ML but it's not by Andrés-Mañas.

The user said "além do Andrés-Mañas que já conhecemos" - meaning they already know one paper by Andrés-Mañas. Let me look for it more specifically.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 22:10:02 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I see now - the user mentioned that they already know the Andrés-Mañas papers. The relevant one from Andrés-Mañas et al. that uses machine learning (not necessarily PINNs) is:

- **Requena, Andrés-Mañas, Gil, Zaragoza (2023)** - "Application of machine learning to characterize the permeate quality in pilot-scale vacuum-assisted air gap membrane distillation operation" - Membranes (MDPI). This uses ANN for MD, not PINNs specifically though.

Now let me compile my final response with the most relevant articles. I have enough data. Let me organize the best 10+ articles that are specifically about PINNs + MD or desalination.

Here's my curated list:

### Directly on PINNs + Membrane Distillation:

1. **Shirzadi et al. (2024)** - "Novel physics-informed optimization framework for complex multi-physics problems: Implementation for a sweeping gas membrane distillation module" - Chemical Engineering Journal
   - Authors: M Shirzadi, Z Li, T Yoshioka, H Matsuyama
   - Citations: 13
   - Directly applies PIPO (Physics-Informed Physics-Optimized) to SGMD. The framework differs from standard PINNs but incorporates physics knowledge into optimization. **Relação direta com MD.**

2. **Shahouni & Abrofarakh (2026)** - "Fractional-order physics-informed neural network deep learning framework with blockchain for dynamic optimization of flux, fouling and heavy metal rejection in metal foam-enhanced direct contact membrane distillation" - Engineering Applications of Artificial Intelligence
   - Authors: R Shahouni, M Abrofarakh
   - Citations: 1
   - Directly applies FO-PINNs to DCMD optimization. **Relação direta com DCMD.**

### PINNs for Membrane Processes (RO, Fouling):

3. **Garakani & Chew (2025)** - "Development of physics-informed machine-learning models to enhance understanding and prediction of membrane fouling" - Journal of Membrane Science
   - Authors: SS Garakani, JW Chew
   - Citations: 21
   - Uses physics-informed ML for membrane fouling prediction. Aplicável a MD porque fouling é crítico em MD.

4. **Garakani, Hassanabadi & Chew (2026)** - "A physics-informed neural network for interpretable membrane-fouling prediction with adaptive transitions between fouling mechanisms" - Separation and Purification Technology
   - Authors: SS Garakani, M Hassanabadi, JW Chew
   - Citations: 1
   - PINN for membrane fouling. Mesma lógica: fouling prediction é transferível para MD.

5. **Fu et al. (2025)** - "Physics-informed neural network-based prediction of permeation performance in reverse osmosis membrane elements" - Environmental Science: Water Research & Technology (RSC)
   - Authors: G Fu, S Yuan, Y Li, B Sheng, Y Cen
   - Citations: 2
   - PINN para prever desempenho de membranas RO. Abordagem PINN para permeação é transferível para MD.

6. **M Li, J Li (2025)** - "Physics-informed neural networks for modeling and diagnosing degradation in reverse osmosis membranes" - Desalination and Water Treatment
   - Authors: M Li, J Li
   - Citations: 4
   - PINNs for RO membrane degradation. Metodologia PINN pode ser aplicada a MD.

### PINNs for Desalination:

7. **Helali et al. (2025)** - "Harnessing physics-informed neural networks for performance monitoring in SWRO desalination" - Water (MDPI)
   - Authors: S Helali, S Albalawi, N Bel Hadj Ali
   - Citations: 5
   - PINNs for SWRO performance monitoring. Metodologia aplicável a MD.

8. **V Arya, A Agarwal, C Bakli (2026)** - "Physics-informed machine learning for electroosmotic flow in graphene nanochannels: Towards next-generation desalination membranes" - Desalination
   - Authors: V Arya, A Agarwal, C Bakli
   - Citations: 2
   - PINN model for electroosmotic flow in nanochannel desalination membranes. **Relação com membranas de dessalinização.**

9. **Chen et al. (2024)** - "Transfer learning and pretraining enhanced physics-informed machine learning for closed-circuit reverse osmosis modeling" - Desalination
   - Authors: Y Chen, Z Wu, B Zhang, J Ren, C He, Q Chen
   - Citations: 14
   - Physics-informed ML for CCRO modeling. Abordagem híbrida transferível para MD.

### Related Reviews and Broader Context:

10. **Rahman & Hazra (2024)** - "Advancing computational fluid dynamics through machine learning: a review of data-driven innovations and applications" - (researchgate)
    - Authors: MS Rahman, S Hazra
    - Citations: 35
    - Review que menciona PINNs aplicados a MD. Revisão geral que conecta PINNs com CFD em MD.

11. **Liu, Luo & Heng (2025)** - "Fast solution of 3D transport processes using a physics-informed neural network with embedded transfer learning" - Separation and Purification Technology
    - Authors: L Liu, J Luo, Y Heng
    - Citations: 11
    - PINN for 3D transport in ultrapermeable membranes for desalination. **Relação com membranas de dessalinização.**

12. **Ghim et al. (2026)** - "Key Considerations in Developing Photothermal Membrane Distillation" - ACS ES&T Engineering
    - Authors: D Ghim, H Kim, X Wu, S Cao, PI Chou
    - Cita: menciona necessidade de desenvolver PINNs para MD. Aborda desenvolvimento de PINNs para fototermal MD.

13. **Peralez & Nadri (2024)** - "Deep model-free KKL observer: A switching approach" - Proceedings of Machine Learning Research
    - Authors: J Peralez, M Nadri
    - Citations: 9
    - Mentions "A deep-learning-based observer for state estimation of direct contact membrane distillation" as related work.

Let me also check for the Peralez paper snippet more carefully - it mentions "A deep-learning-based observer for state estimation of direct contact membrane distillation" which is a separate reference in their paper. Let me look for the actual DCMD observer paper.

Actually, let me also fetch one more round to find the KKL observer DCMD paper and check some more relevant results.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-17 22:10:19 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Excellent! I now have a very comprehensive set of results. Let me compile a clean, organized response with the best articles. I'll organize them into tiers of relevance.

Key additional articles found:

From search 1 (index 0):
- Wang, Marani & Kirati (2022): "A deep-learning-based observer for state estimation of direct contact membrane distillation system" - This is a deep learning + DCMD paper, not exactly PINN but related.

From search 2 (index 1):
- Alves, Weschenfelder & Cechinel (2026): "Physics-informed machine learning for cross-study prediction of oil–water membrane fouling" - Scientific Reports. Physics-informed ML for membrane fouling.
- Ghim et al. (2026): "Key Considerations in Developing Photothermal Membrane Distillation" - ACS ES&T Engineering. Explicitly calls for physics-informed ML frameworks for MD.
- Do & Do (2026): "Enhanced Temporal Convolutional Network Based Approach for Degradation Prediction of Reverse Osmosis Systems" - mentions future work with PINNs for RO and MD.

From search 3 (index 2):
- Liu, Luo & Heng (2025): "Fast solution of 3D transport processes using a physics-informed neural network with embedded transfer learning" - Separation and Purification Technology. PINN for UPM module optimization (desalination membranes).
- Merdasi et al. (2023): "Physics Informed Neural Network application on mixing and heat transfer in combined electroosmotic-pressure driven flow" - Related to fluid/heat transfer that applies to MD.
- Manavi, Fattahi & Becker (2024): "A parameterized physics-informed machine learning approach for solving heat and mass transfer equations in the drying process" - Heat & mass transfer PINN approach, transferable to MD.

Let me now pick the best articles and compose a response.

</details>

### Resposta

Aqui estão os artigos mais relevantes encontrados (excluindo Andrés-Mañas):

---

## 🔴 Nível 1 — Aplicação Direta de PINNs em Membrane Distillation

**1. Shirzadi, M., Li, Z., Yoshioka, T. & Matsuyama, H. (2024)**
- **Título:** "Novel physics-informed optimization framework for complex multi-physics problems: Implementation for a sweeping gas membrane distillation module"
- **Periódico:** *Chemical Engineering Journal*
- **Citações:** 13
- **Descrição:** Propõe o framework PIPO (Physics-Informed Physics-Optimized), distinto de PINNs tradicionais, que incorpora equações físicas diretamente no processo de otimização. Implementado para um módulo de sweeping gas membrane distillation (SGMD).
- **Relação com MD:** **Direta** — otimização física-informada de SGMD.

**2. Shahouni, R. & Abrofarakh, M. (2026)**
- **Título:** "Fractional-order physics-informed neural network deep learning framework with blockchain for dynamic optimization of flux, fouling and heavy metal rejection in metal foam-enhanced direct contact membrane distillation"
- **Periódico:** *Engineering Applications of Artificial Intelligence*
- **Citações:** 1
- **Descrição:** Desenvolve FO-PINNs (Fractional-Order PINNs) para modelagem substituta de DCMD, combinando com Reinforcement Learning para otimização dinâmica de fluxo, fouling e rejeição de metais pesados.
- **Relação com MD:** **Direta** — FO-PINNs aplicados a DCMD com validação CFD.

**3. Abrofarakh, M., Moghadam, H. & Abdulrahim, H.K. (2024)**
- **Título:** "Investigation of direct contact membrane distillation (DCMD) performance using CFD and machine learning approaches"
- **Periódico:** *Chemosphere*
- **Citações:** 31
- **Descrição:** Usa CFD + ML para investigar desempenho de DCMD. Base para o artigo de 2026 com FO-PINNs.
- **Relação com MD:** **Direta** — antecede a abordagem PINN em DCMD.

---

## 🟠 Nível 2 — PINNs Aplicadas a Processos de Membrana (RO, Fouling) — Transferível para MD

**4. Garakani, S.S. & Chew, J.W. (2025)**
- **Título:** "Development of physics-informed machine-learning models to enhance understanding and prediction of membrane fouling"
- **Periódico:** *Journal of Membrane Science*
- **Citações:** 21
- **Descrição:** Modelos PINN que incorporam equações físicas de fouling em membranas, usando pesos dinâmicos para loss function. Demonstra que PINN generaliza melhor que modelos puramente data-driven com dados reduzidos.
- **Relação com MD:** Fouling é o principal desafio operacional em MD — a metodologia é diretamente aplicável.

**5. Garakani, S.S., Hassanabadi, M. & Chew, J.W. (2026)**
- **Título:** "A physics-informed neural network for interpretable membrane-fouling prediction with adaptive transitions between fouling mechanisms"
- **Periódico:** *Separation and Purification Technology*
- **Citações:** 1
- **Descrição:** PINN interpretável que modela transições adaptativas entre mecanismos de fouling (bloqueio completo, intermediário, etc.).
- **Relação com MD:** Transições de fouling são críticas em MD, especialmente com águas residuais.

**6. Fu, G., Yuan, S., Li, Y., Sheng, B. & Cen, Y. (2025)**
- **Título:** "Physics-informed neural network-based prediction of permeation performance in reverse osmosis membrane elements"
- **Periódico:** *Environmental Science: Water Research & Technology* (RSC)
- **Citações:** 2
- **Descrição:** PINN para prever desempenho de permeação em membranas RO, incorporando equações de transferência de massa na loss function. Supera BPNN, LSTM e DBN.
- **Relação com MD:** PINN para permeação em membranas é conceito idêntico ao necessário para modelagem de fluxo em MD.

**7. Liu, L., Luo, J. & Heng, Y. (2025)**
- **Título:** "Fast solution of 3D transport processes using a physics-informed neural network with embedded transfer learning"
- **Periódico:** *Separation and Purification Technology*
- **Citações:** 11
- **Descrição:** PINN com transfer learning (PINN-TL) para solução rápida de transporte 3D em ultrapermeable membranes (UPMs) para dessalinização.
- **Relação com MD:** Transporte 3D em módulos de membrana — aplicável a simulação de MD.

**8. Li, M. & Li, J. (2025)**
- **Título:** "Physics-informed neural networks for modeling and diagnosing degradation in reverse osmosis membranes"
- **Periódico:** *Desalination and Water Treatment*
- **Citações:** 4
- **Descrição:** PINNs para modelar e diagnosticar degradação de membranas RO ao longo do tempo.
- **Relação com MD:** Degradação de membranas é igualmente relevante para MD de longa operação.

---

## 🟡 Nível 3 — PINNs Aplicadas a Dessalinização (Contexto Geral)

**9. Chen, Y., Wu, Z., Zhang, B., Ren, J., He, C. & Chen, Q. (2024)**
- **Título:** "Transfer learning and pretraining enhanced physics-informed machine learning for closed-circuit reverse osmosis modeling"
- **Periódico:** *Desalination*
- **Citações:** 14
- **Descrição:** ML physics-informed com transfer learning + pretraining para modelagem de CCRO (closed-circuit RO), processo batch de dessalinização.
- **Relação com MD:** Abordagem híbrida TL + PINN pode ser transferida para MD batch/contínuo.

**10. Helali, S., Albalawi, S. & Bel Hadj Ali, N. (2025)**
- **Título:** "Harnessing physics-informed neural networks for performance monitoring in SWRO desalination"
- **Periódico:** *Water* (MDPI)
- **Citações:** 5
- **Descrição:** PINNs para monitoramento de desempenho em dessalinização por osmose reversa de água do mar (SWRO).
- **Relação com MD:** Framework de monitoramento PINN aplicável a plantas de MD.

**11. Arya, V., Agarwal, A. & Bakli, C. (2026)**
- **Título:** "Physics-informed machine learning for electroosmotic flow in graphene nanochannels: Towards next-generation desalination membranes"
- **Periódico:** *Desalination*
- **Citações:** 2
- **Descrição:** Modelo PINN para fluxo eletrosmótico em nanocanais de grafeno para membranas de dessalinização de próxima geração.
- **Relação com MD:** Fundamentos de transporte em nanoescala relevantes para membranas MD.

---

## 🟢 Nível 4 — Menções/Reviews que Conectam PINNs e MD

**12. Wang, Y., Marani, Y. & Kirati, T.M.L. (2022)**
- **Título:** "A deep-learning-based observer for state estimation of direct contact membrane distillation system modeled by differential algebraic equations"
- **Periódico:** *IEEE Conference (CDC)*
- **Citações:** 2
- **Descrição:** Deep learning observer para estimativa de estado em DCMD modelado por DAEs. Usa KKL observer com deep learning — precursor conceitual de PINNs para MD.
- **Relação com MD:** **Direta** — estimativa de estados em DCMD.

**13. Ghim, D., Kim, H., Wu, X., Cao, S. & Chou, P.I. (2026)**
- **Título:** "Key Considerations in Developing Photothermal Membrane Distillation"
- **Periódico:** *ACS ES&T Engineering*
- **Descrição:** Review que enfatiza a necessidade de desenvolver **physics-informed ML frameworks** que integrem princípios de heat and mass transfer para fototermal MD.
- **Relação com MD:** **Direta** — advocacy explícita por PINNs em MD.

**14. Rahman, M.S. & Hazra, S. (2024)**
- **Título:** "Advancing computational fluid dynamics through machine learning: a review of data-driven innovations and applications"
- **Periódico:** *ResearchGate / preprint*
- **Citações:** 35
- **Descrição:** Review abrangente sobre CFD + ML. Menciona explicitamente PINNs aplicados em membrane distillation processes.
- **Relação com MD:** Seção dedicada a CFD em MD com PINNs.

**15. Do, T.H. & Do, P. (2026)**
- **Título:** "Enhanced Temporal Convolutional Network Based Approach for Degradation Prediction of Reverse Osmosis Systems"
- **Periódico:** *International Journal of Mathematics, Engineering and Management Sciences*
- **Descrição:** Propõe como trabalho futuro desenvolver modelos baseados em **Physics-Informed Machine Learning** para fluxo em RO e MD.
- **Relação com MD:** Explicitamente planeja estender para MD.

---

## 📊 Mapa da Literatura

```
                        PINNs + MD
                     ┌─────────────────┐
                     │  Shirzadi (2024) │ ← PIPO para SGMD
                     │  Shahouni (2026) │ ← FO-PINNs para DCMD
                     │  Wang (2022)     │ ← Deep learning observer DCMD
                     │  Ghim (2026)     │ ← Advocacy PINNs p/ fototermal MD
                     └────────┬────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
    PINNs + Membranas   PINNs + Fouling   PINNs + Desalinação
    ┌──────────────┐  ┌───────────────┐  ┌─────────────────┐
    │ Fu (2025)    │  │Garakani (2025)│  │ Chen (2024)     │
    │ Liu (2025)   │  │Garakani (2026)│  │ Helali (2025)   │
    │ Li (2025)    │  │Alves (2026)   │  │ Arya (2026)     │
    └──────────────┘  └───────────────┘  └─────────────────┘
```

O gap principal: **apenas 2 artigos** (Shirzadi 2024 e Shahouni 2026) aplicam PINNs diretamente em MD. Os demais são transferíveis por similaridade de processo (fouling, permeação, transporte em membranas).

*Novo passo iniciado*

---

*11 messages | 42 parts | 💰 $0.0123 | ⏱️ 0h01m54s*
