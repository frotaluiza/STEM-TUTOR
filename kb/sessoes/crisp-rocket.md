---
slug: crisp-rocket
title: "Find TCC code files (@explore subagent)"
date: 2026-07-08
agent: explore
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h01m16s
messages: 6
parts: 66
cost: 0
tokens_input: 70551
tokens_output: 9505
tokens_reasoning: 334
tokens_cache_read: 130688
tokens_cache_write: 0
created: "2026-07-08 21:25:47 UTC"
updated: "2026-07-08 21:27:03 UTC"
---

Sessão com **6 messages**, **66 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | 💾 cache read: 130.7K | ⏱️ 0h01m16s

## 👤 Usuário (2026-07-08 21:25:47 UTC)

Find ALL Python scripts and code files related to the TCC project. Search in:
1. C:\Users\frota\OneDrive\Documentos\TCC\Codigos\
2. C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\tcc\
3. C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\slides_repo\

Return the full paths of all Python (.py), R (.r, .Rmd), and Jupyter notebook (.ipynb) files found. Also look for any files with "metric" or "model" or "familia" in the name.

## 🤖 Assistente (2026-07-08 21:25:47 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to find all Python scripts and code files related to the TCC project across three directories. Let me search broadly using glob patterns for various file types.

</details>

### Resposta

I'll search all three directories in parallel for the requested file types.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-08 21:25:56 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The results are quite extensive and the Python results were truncated. Let me also search specifically within the non-venv directories to get a cleaner picture. Let me also search the other two directories more carefully, and look for files with specific names.

Let me do additional targeted searches to get the full list without venv noise.

</details>

### Resposta

The results were truncated for Python files. Let me refine the searches, excluding the virtual environment (`venv`) to focus on project code, and also check the remaining directories more carefully.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-08 21:26:05 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The results are still truncated for the Codigo-revisado and scripts_hibrido directories. Let me get the complete list for those directories by being more specific, and also check the remaining files I haven't fully listed yet. Let me also look at the remaining `.py` files in `Codigo-revisado\scripts` that got truncated.

Let me also look at the `scripts_hibrido` directory (excluding venv) and any other top-level directories I might have missed.

</details>

### Resposta

Let me get the complete file lists for the directories that were truncated.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-08 21:26:21 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive picture. Let me also check the `tcc_repo` directory for any Python files, and also look at the `vagmd0Dmodel-main` directory.

</details>

### Resposta

Let me also check the remaining subdirectories and ensure no files were missed.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-08 21:26:28 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive picture. Let me summarize the findings for the user. Note that "tcc_repo" and "vagmd0Dmodel-main" don't have Python files - tcc_repo is a LaTeX thesis project and vagmd0Dmodel-main is a C project.

Also, directories 2 and 3 (the "SLIDES POLI" ones) had no Python files at all.

Let me compile the complete, clean results.

</details>

### Resposta

Here is the complete report of all TCC-related code files found across the three directories.

---

## Directory 1: `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\`

### Python scripts (root level)
1. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\t3.py`

### Python -- `CodFin\`
2. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\t1.py`
3. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\t2.py`
4. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\t3.py`
5. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\cabecalho.py`
6. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\script_organizador.py`
7. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\consolidar_resultados.py`
8. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\gerando_imagens_hrnn.py`
9. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\results_hrnn_only_dados_att_com_var_com_phy_20260311_132909\gerando_imagens.py`
10. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\stage1-stage0\gerando_imagens.py`

### Python -- `Codigo-revisado\` (core modules)
11. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\config.py`
12. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\data.py`
13. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\cv.py`
14. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\consolidate.py`
15. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\file_io.py`
16. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\plots.py`
17. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\runner.py`
18. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\selection.py`
19. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\sweep.py`

### Python -- `Codigo-revisado\models\`
20. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\models\__init__.py`
21. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\models\wrappers.py`
22. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\models\per_output_mlp.py`
23. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\models\keras_builders.py`

### Python -- `Codigo-revisado\scripts\` (all scripts)
24. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\_check_best.py`
25. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\_check_r2.py`
26. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\_read_results.py`
27. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\_show_stage0.py`
28. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\analisar_complexidade_universal.py`
29. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\analisar_gap.py`
30. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\analise_1se_final.py`
31. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\auto_optimize_mlp.py`
32. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\calcular_vencedores.py`
33. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\check_gap.py`
34. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\computar_dps_reais.py`
35. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\debug_oof_fold.py`
36. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\diagnostico_sklearn_vs_keras.py`
37. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\ensamble_multiobjective.py`
38. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\estrategia_hibrida.py`
39. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\estrategia_hibrida_v2.py`
40. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\fase2_corrigido.py`
41. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\fase2_hibridos.py`
42. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gen_latex_table.py`
43. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gen_tables.py`
44. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gen_tables_final.py`
45. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\generate_oof_winner.py`
46. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\generate_overlays.py`
47. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\generate_overlays_oof.py`
48. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_curvas_aprendizado.py`
49. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_imagens.py`
50. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_imagens_3targets.py`
51. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_imagens_finais.py`
52. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_oof_vencedores.py`
53. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_overlays_e_sweeps.py`
54. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_overlays_vencedores.py`
55. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_surrogate.py`
56. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_sweeps_com_treino_valid.py`
57. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_tabelas_tcc.py`
58. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_todas_imagens.py`
59. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_todas_imagens_v2.py`
60. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_cv_completo.py`
61. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_oor_completo.py`
62. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_oor_v2.py`
63. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_scikeras_oof.py`
64. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_single_output.py`
65. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\keras_flux_final.py`
66. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\keras_mlp_puro_flux.py`
67. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\keras_single_temps.py`
68. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\luc_sweep_independente.py`
69. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\mlp_nativo_ols.py`
70. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\multi_output_otimizado.py`
71. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\oof_all_models.py`
72. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\otimizar_baseline_e_hibridos.py`
73. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\otimizar_vs_classicos.py`
74. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\per_output_gridsearch.py`
75. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\pinn_only_test.py`
76. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\pipeline_final.py`
77. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_all_stages.py`
78. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_all_winners.py`
79. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_stage0.py`
80. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_stage2.py`
81. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\regenerate_plots.py`
82. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\rodar_agente_tcc.py`
83. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\rodar_hibridos_backbone.py`
84. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_agente_final.py`
85. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_agent_cv_final.py`
86. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_agent_multiobjective.py`
87. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_all.py`
88. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_all_multitarget.py`
89. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_com_params_tcc.py`
90. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_flux_baseline.py`
91. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_full_pipeline.py`
92. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_hrnn_only.py`
93. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_luc_flux.py`
94. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_luc_target.py`
95. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_oof_keras.py`
96. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_organizer.py`
97. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_original_pipeline.py`
98. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_pipeline.py`
99. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage0.py`
100. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage0_completo.py`
101. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage0_final.py`
102. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage0_rapido.py`
103. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage1.py`
104. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage1_checkpoint.py`
105. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage1_completo.py`
106. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage1_for_target.py`
107. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage1_manual.py`
108. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage1_puro.py`
109. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage1_sequencial.py`
110. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage2_hibridos.py`
111. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage2_multitarget.py`
112. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage2_puro.py`
113. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_strategy.py`
114. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_tf_pipeline.py`
115. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\selecao_1se_entre_familias.py`
116. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\show_table.py`
117. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\stage1_focused.py`
118. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\stage2_agent.py`
119. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\stage2_focused.py`
120. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\test_all_scikeras.py`
121. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\test_keras_equal_mlpsk.py`
122. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\test_keras_vs_sklearn.py`
123. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\test_pinn_surrogates.py`
124. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\test_scikeras.py`
125. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\test_sklearn_mlp.py`
126. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\test_sklearn_tcc.py`
127. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\testar_surrogate.py`

### Python -- `Codigo-revisado\scripts\results\`
128. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\results\_show_all.py`
129. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\results\_show_results.py`

### Python -- `scripts_hibrido\` (project code, excluding `venv`)
130. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\scripts_hibrido\debug.py`
131. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\scripts_hibrido\res1.py`

### R scripts -- `R\`
132. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\R\teste.R`
133. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\R\refazendo_aug.R`
134. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\R\com_regime_e_rede_neural.R`
135. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\R\com_regime.R`
136. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\R\comparando_com_sem_aug.R`

### Jupyter Notebooks -- `Regressao Linear\`
137. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Regressao Linear\Regressao_OLS_basica_80_20_.ipynb`
138. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Regressao Linear\comparando_regressoes_sem_mudanca_para_categorico.ipynb`

### Files matching "familia" in name
139. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\selecao_1se_entre_familias.py`

### Files matching "metric" or "model" (project code only, not `venv`)
The search found these within the project code:
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\oof_all_models.py` (contains "models" in name)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\models\` (entire `models/` module listed above)
- Data files like `oof_rmse_all_models.csv` and `agmd_0d_metrics.json` (output/result files)

---

## Directory 2: `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\tcc\`
**No Python, R, Rmd, or ipynb files found.** This directory contains only image assets (PNGs).

---

## Directory 3: `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\slides_repo\`
**No Python, R, Rmd, or ipynb files found.** This directory contains only image assets (PNGs).

---

## Other TCC subdirectories (no Python found):
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\tcc_repo\` -- LaTeX thesis project (`.tex`, `.bib`, `.cls`, images)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\vagmd0Dmodel-main\` -- C language project (`.c`, `.h` files)

---

## Summary

| Language | Count | Notes |
|---|---|---|
| **Python (.py)** | **131 files** | All project-level code (excluding `venv` library files) |
| **R (.R)** | **5 files** | All in `Codigos\R\` |
| **Rmd (.Rmd)** | **0 files** | None found |
| **Jupyter (.ipynb)** | **2 files** | Both in `Codigos\Regressao Linear\` |
| **"familia" in name** | **1 file** | `selecao_1se_entre_familias.py` |
| **"model" in name** | **Module + scripts** | `models/` package (4 files) + `oof_all_models.py` |
| **"metric" in name** | **0 files** | Only output CSVs/JSONs |

The vast majority of the TCC computational code lives in `Codigo-revisado/` (core modules + 106 scripts), with additional legacy/experimental code in `CodFin/`, `scripts_hibrido/`, and `R/`. Directories 2 and 3 (slides-related) contain only images, no code files.

*Novo passo iniciado*

---

*6 messages | 66 parts | 💰 $0.0000 | ⏱️ 0h01m16s*
