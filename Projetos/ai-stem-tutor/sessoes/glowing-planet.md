---
title: "glowing-planet"
slug: "glowing-planet"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: glowing-planet
title: "Find overlay plot scripts (@explore subagent)"
date: 2026-07-06
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h01m55s
messages: 13
parts: 86
cost: 0.013493
tokens_input: 66740
tokens_output: 6286
tokens_reasoning: 3336
tokens_cache_read: 519680
tokens_cache_write: 0
created: "2026-07-06 23:00:42 UTC"
updated: "2026-07-06 23:02:38 UTC"
---

SessÃ£o com **13 messages**, **86 parts**, agente **explore**, modelo **deepseek-v4-flash** | ðŸ’° $0.0135 | ðŸ’¾ cache read: 519.7K | â±ï¸ 0h01m55s

## ðŸ‘¤ UsuÃ¡rio (2026-07-06 23:00:42 UTC)

Search thoroughly in C:\Users\frota\OneDrive\Documentos\TCC for Python scripts (*.py) that generate overlay plots (predicted vs experimental) for hold-out. Look for files containing "overlay", "holdout", "hold-out", "predito", "experimental", "scatter" in their content or filename. Also search in C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI if needed. Return the full paths of all relevant scripts and a brief description of what each does.

## ðŸ¤– Assistente (2026-07-06 23:00:42 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants me to search thoroughly for Python scripts that generate overlay plots (predicted vs experimental) for hold-out in specific directories. Let me start by searching in multiple ways:

1. Glob for *.py files in the TCC directory
2. Search for content patterns in those files
3. Also check the SLIDES POLI directory

Let me do multiple searches in parallel.

</details>

### Resposta

I will conduct a thorough search across both directories. Let me start with multiple parallel searches.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:01 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The search found many results. Let me now focus on the non-virtual-env Python scripts that are most relevant. Let me look at the specific key files:

1. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\t3.py` - Has overlay functions
2. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\regenerate_plots.py` - Has overlay references
3. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_todas_imagens_v2.py` - Has overlay
4. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_todas_imagens.py` - Has overlay
5. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_overlays_vencedores.py` - Overlays
6. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_overlays_e_sweeps.py` - Overlays
7. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_imagens_finais.py` - Overlays
8. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\generate_overlays_oof.py` - Overlays
9. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\generate_overlays.py` - Overlays
10. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\plots.py` - Core plotting functions
11. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\file_io.py` - Has overlay functions
12. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\gerando_imagens_hrnn.py` - Might have overlay
13. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\results_hrnn_only_dados_att_com_var_com_phy_20260311_132909\gerando_imagens.py` - Might have overlay
14. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\stage1-stage0\gerando_imagens.py` - Might have overlay

Let me also search for "predito", "experimental", "scatter" in these Python files.

</details>

### Resposta

Good, I have initial results. Let me now search for additional keyword patterns and read the most relevant files to understand their purposes.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:09 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me read the most relevant files to understand their purpose in detail. The key scripts are in:

1. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\` - This seems to be the main working codebase
2. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\` - Earlier version

Key scripts to analyze:
- `scripts\generate_overlays.py` - Generates overlay plots
- `scripts\generate_overlays_oof.py` - OOF-based overlay plots
- `scripts\gerar_overlays_vencedores.py` - Overlays with winners
- `scripts\gerar_overlays_e_sweeps.py` - Overlays and sweeps
- `scripts\gerar_imagens_finais.py` - Final images including overlays
- `scripts\gerar_todas_imagens.py` - All images including overlays
- `scripts\gerar_todas_imagens_v2.py` - All images v2 including overlays
- `scripts\regenerate_plots.py` - Regenerates plots from overlay data
- `plots.py` - Core plotting functions
- `file_io.py` - Core file I/O with overlay functions
- `CodFin\t3.py` - Has overlay functions

Let me read the most significant ones.

</details>

### Resposta

Now let me read the key scripts to understand their purpose and identify which ones specifically generate hold-out overlay plots.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:15 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me also read the remaining key scripts: `gerar_imagens_finais.py`, `gerar_todas_imagens.py`, `gerar_todas_imagens_v2.py`, `regenerate_plots.py`, `plots.py` (the relevant sections), and `file_io.py` (the relevant sections). Also the CodFin\t3.py.

</details>

### Resposta

Let me read the remaining key scripts:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:20 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me also read the core plotting functions in `plots.py` (the overlay-related sections) and `file_io.py`. Also read `CodFin\t3.py` for its overlay functions.

</details>

### Resposta

Let me now read the core plotting and file_io modules, plus the CodFin t3.py overlay functions:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:25 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me also check the other generator scripts in the CodFin directory and a few more in the scripts_hibrido directory. Let me also check the gerando_imagens scripts under CodFin and stage1-stage0.

</details>

### Resposta

Let me check the remaining generator scripts in the CodFin directory:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:30 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a comprehensive understanding of the codebase. Let me also check the `refit_all_winners.py` and `refit_stage2.py` scripts since they mention hold-out, and check if they also generate overlay plots.

</details>

### Resposta

Let me check the refit scripts that mention hold-out:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:35 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a very comprehensive view of the codebase. Let me also check the refit scripts more carefully since they mention hold-out to confirm they do overlay plots.

The `refit_all_winners.py` and `refit_stage2.py` mention hold-out but don't seem to generate overlay plots themselves. They are about refitting models with the hold-out split.

Now let me also look at `gerando_imagens.py` under the `results_hrnn_only...` folder to see if it has overlay functions.

Let me also check the CodFin\t3.py file for its main/runner section that calls the overlay functions.

</details>

### Resposta

Let me check the remaining CodFin scripts and look for any additional overlay-related code:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:40 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Good. The `gerando_imagens.py` under `results_hrnn_only` is just an image organizer/consolidator, not an overlay plot generator.

Now let me also quickly check the `CodFin\t1.py` and `CodFin\t2.py` for overlay-related functions.

</details>

### Resposta

Let me check the remaining CodFin/t*.py files briefly and look for any scripts I might have missed:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:45 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The t1.py and t2.py don't have dedicated overlay functions, only the bare scatter plots (OOF pred vs true). The overlay-specific code is concentrated in:

1. `CodFin\t3.py` - Contains `plot_oof_vs_phy_overlay_per_target`, `plot_oof_vs_phy_overlay_panel`, `save_overlay_comparison_table` functions. Also has a runner that calls these functions.

2. `Codigo-revisado\plots.py` - Contains `plot_oof_vs_phy_overlay_per_target` and `plot_oof_vs_phy_overlay_panel` - the core plotting functions for overlays.

3. `Codigo-revisado\file_io.py` - Contains `save_overlay_comparison_table` and also calls the overlay functions in its `save_outputs` function.

4. `Codigo-revisado\scripts\generate_overlays.py` - Script that generates 0D vs winner overlay plots using full-data fit.

5. `Codigo-revisado\scripts\generate_overlays_oof.py` - Script that generates OOF-based 0D vs winner overlay plots using CV folds.

6. `Codigo-revisado\scripts\regenerate_plots.py` - Script that regenerates overlay plots from saved CSV overlay files.

7. `Codigo-revisado\scripts\gerar_overlays_vencedores.py` - Generates overlay scatter plots with the absolute winner per target (scatter plot with predicted vs experimental).

8. `Codigo-revisado\scripts\gerar_overlays_e_sweeps.py` - Generates overlay plots with vertical error bars (yerr) plus L2/LR sweeps.

9. `Codigo-revisado\scripts\gerar_imagens_finais.py` - Regenerates overlay + OOF + sweep + best_per_family plots for final winners.

10. `Codigo-revisado\scripts\gerar_todas_imagens.py` - Generates all images: overlay (line plots), OOF, learning curve, sweep, best_per_family.

11. `Codigo-revisado\scripts\gerar_todas_imagens_v2.py` - Generates consolidated images including overlay plots with synthetic data for visualization purposes.

Now, the user specifically asked for scripts that generate "overlay plots (predicted vs experimental) for hold-out." 

Looking at the "hold-out" references:
- `refit_all_winners.py` - "TEST = hold-out 35 amostras" - but this doesn't generate overlay plots
- `refit_stage2.py` - "Test = hold-out 20% (35 amostras, nunca vistas)" - but this doesn't generate overlay plots either
- `refit_stage0.py` - "Runner â€” cada fold faz CV + Test no hold-out 20%" - doesn't generate overlay plots
- `calcular_vencedores.py` - "Usa Test RMSE (hold-out 20%) como metrica principal" - doesn't generate overlay plots

None of the overlay scripts explicitly reference "hold-out" in their code. However, the overlay plots DO compare predicted vs experimental values - they just use OOF (out-of-fold) predictions rather than hold-out test predictions. The OOF predictions come from the cross-validation process.

Wait, let me look more closely at:

1. `gerar_overlays_vencedores.py` - Uses GroupKFold cross-validation, so its predictions are OOF (from CV folds), not strictly hold-out. But the scatter plots compare predicted vs experimental.

2. `gerar_overlays_e_sweeps.py` - Same OOF approach.

3. `gerar_imagens_finais.py` - Same OOF approach.

4. `generate_overlays.py` - Uses full-data fit (not hold-out, not OOF - it fits on ALL data and predicts on ALL data).

5. `generate_overlays_oof.py` - Uses OOF (CV folds).

6. `gerar_todas_imagens.py` - Uses OOF.

The hold-out specifically appears in `refit_all_winners.py` which does a proper 80/20 hold-out split. Let me check whether it generates overlay plots.

Looking again at `refit_all_winners.py`:
- It does `train_test_split` with test_size=0.2 stratified by groups
- It has a "hold-out 35 amostras"
- But I didn't see any overlay plotting code in it

Let me check the full content of refit_all_winners.py to be sure.

</details>

### Resposta

Let me check the refit_all_winners.py for any overlay plotting and also check if there's any direct hold-out overlay script:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:01:57 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a complete picture. Let me summarize my findings.

The user asked to search for Python scripts that generate overlay plots (predicted vs experimental) for hold-out. Let me be precise about what I found:

### Scripts that DIRECTLY generate overlay plots (predicted vs experimental):

**Core plotting modules (libraries, not standalone scripts):**
1. `Codigo-revisado/plots.py` - Contains `plot_oof_vs_phy_overlay_per_target()` and `plot_oof_vs_phy_overlay_panel()` - core scatter plot functions that show predicted vs experimental with RMSE.
2. `Codigo-revisado/file_io.py` - Contains `save_overlay_comparison_table()` and `save_outputs()` which orchestrates overlay generation.
3. `CodFin/t3.py` - Contains the original versions of the same overlay functions.

**Standalone scripts that GENERATE overlay plots:**
4. `Codigo-revisado/scripts/generate_overlays.py` - Full-data fit overlay plots (0D vs winner).
5. `Codigo-revisado/scripts/generate_overlays_oof.py` - OOF-based overlay plots.
6. `Codigo-revisado/scripts/regenerate_plots.py` - Regenerates overlay plots from saved CSV overlay data.
7. `Codigo-revisado/scripts/gerar_overlays_vencedores.py` - Scatter overlay plots (predito vs experimental) for absolute winners.
8. `Codigo-revisado/scripts/gerar_overlays_e_sweeps.py` - Overlay plots with error bars + sweeps.
9. `Codigo-revisado/scripts/gerar_imagens_finais.py` - Final overlay plots with yerr.
10. `Codigo-revisado/scripts/gerar_todas_imagens.py` - Line overlay plots (experimental + 0D + hybrid).
11. `Codigo-revisado/scripts/gerar_todas_imagens_v2.py` - Consolidated overlay plots (using synthetic data).

### Regarding "hold-out":
- The `refit_all_winners.py` and `refit_stage2.py` scripts mention hold-out (20% test split with 35 hold-out samples), but they do NOT generate overlay plots. They compute metrics (RMSE/R2) on the hold-out set.
- The overlay scripts use OOF (out-of-fold) predictions from GroupKFold CV, not a dedicated hold-out set. However, the predictions used in the scatter overlays ARE predictions on unseen data during CV (each fold's test data).
- `generate_overlays.py` uses full-data fit (NOT hold-out).

Wait, let me reconsider. The user specifically asked for "hold-out" overlay plots. Let me look more carefully...

In `gerar_overlays_vencedores.py`, they use `GroupKFold(3)` - each point is predicted when it's OUT-OF-FOLD. The scatter plot shows these OOF predictions vs experimental values. This IS a form of hold-out (each point was held out during its fold's training).

In `gerar_overlays_e_sweeps.py` - same, uses GroupKFold CV.

In `gerar_imagens_finais.py` - same, uses GroupKFold CV.

In `generate_overlays.py` - uses full-data fit, so NOT hold-out.

In `generate_overlays_oof.py` - uses GroupKFold CV, so OOF (which is a type of cross-validated hold-out).

Actually, I should also note that `refit_stage2.py` and `refit_all_winners.py` explicitly do a 80/20 hold-out split, but they don't generate overlay plots (they compute metrics).

Let me be comprehensive in my report, distinguishing between:
1. Scripts that generate overlay plots (regardless of whether they use hold-out or OOF)
2. The hold-out benchmark scripts (which compute metrics but don't plot overlays)

Let me compile the final answer.

</details>

### Resposta

Now I have a comprehensive view. Let me verify the SLIDES POLI directory has no relevant scripts:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-06 23:02:10 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Good - the SLIDES POLI directory has no relevant overlay/hold-out Python scripts. Only a tangential mention of "experimental" in the mock_backend.

Now let me compile the complete results.

</details>

### Resposta

Here is the complete and thorough report.

---

## Search Results: Overlay Plot Scripts (Predicted vs Experimental)

### Location 1: `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\` (primary codebase)

---

### A. Core Library Modules (contain the plot functions used by all scripts)

**1. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\plots.py`**
- Contains `plot_oof_vs_phy_overlay_per_target()` (line 384) and `plot_oof_vs_phy_overlay_panel()` (line 454).
- These are the **central overlay plotting functions**. They produce scatter plots of predicted vs experimental values for each target (Alim_T_out, Ref_T_out, Flux), comparing the 0D physical model against the hybrid model (HRNN/OOF). Includes RMSE, R-squared, y=x line, +/-RMSE shaded region, and experimental error bars.
- Used by all overlay generator scripts below.

**2. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\file_io.py`**
- Contains `save_overlay_comparison_table()` (line 70) which dumps the (experimental, 0D-physics, hybrid-OOF) triple to a CSV file.
- Contains `save_outputs()` (line 90) which orchestrates the full pipeline: training, OOF prediction, overlay generation per family, panel plots, and CSV export. This is the main integration point between training and plotting.

---

### B. Standalone Scripts that Generate Overlay Plots

**3. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\generate_overlays.py`**
- **Purpose:** Generates overlay plots using **full-data fit** (not hold-out; fits on all data, predicts on all data). Compares the 0D physical model vs. the winning HRNN model and vs. the Residual model.
- **Output:** Saves per-target overlay scatter plots + panel plot + comparison CSV into `results_*/overlay_0d_vs_winner/`.
- Uses `plot_oof_vs_phy_overlay_per_target()` and `plot_oof_vs_phy_overlay_panel()` from `plots.py`.

**4. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\generate_overlays_oof.py`**
- **Purpose:** Generates overlay plots using **OOF (out-of-fold)** predictions from 3-fold GroupKFold CV. Refits the FrozenBaseline (0D) and HRNN (winner) models on each fold's training data and predicts on the held-out fold. This is a **cross-validated hold-out** approach.
- **Output:** Saves per-target OOF overlay scatter plots + panel plot + comparison CSV into `results_*/overlay_oof_vs_0d/`.
- Uses the same core plot functions from `plots.py`.

**5. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\regenerate_plots.py`**
- **Purpose:** Reads previously saved `_overlay_points_*.csv` files and **re-generates** overlay plots, OOF predicted-vs-true plots, and winner RMSE bar charts from the cached data.
- **Output:** Re-generates per-target overlay + panel + RMSE plots into the same output directory.
- Command-line argument: accepts an output directory path (defaults to a Stage 2 results folder).

**6. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_overlays_vencedores.py`**
- **Purpose:** Generates **scatter overlay plots (Predito x Experimental)** for the absolute winner per target using 3-fold GroupKFold CV (OOF). Each target uses its best model: ZohanResidual (for Alim_T_out), OLS (for Ref_T_out), ZohanHPD (for Flux).
- **Output:** Saves files like `overlay_ZohanResidual_Alim_T_out_n.png`, `overlay_OLS_Ref_T_out_n.png`, `overlay_ZohanHPD_Flux_n.png` into `tcc/Textual/Imagens/chap06/`.
- Axis labels: X-label = "Predito", Y-label = "Experimental".

**7. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_overlays_e_sweeps.py`**
- **Purpose:** Regenerates overlay plots **with vertical error bars (yerr)** plus L2 and learning rate sweeps. Uses 3-fold GroupKFold CV (OOF) for ZohanResidual (Alim), OLS (Ref), and ZohanHPD (Flux).
- **Output:** Saves overlay plots like `overlay_ZohanResidual_Alim_T_out_n.png`, plus sweep plots into `chap06/model_selection/`.
- Uses `ax.errorbar()` for experimental uncertainty and `ax.scatter()` for predicted vs experimental points. Labels: "Predito" / "Experimental".

**8. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_imagens_finais.py`**
- **Purpose:** Regenerates final overlay plots (with yerr), OOF, sweep, and best-per-family bar charts. Uses 3-fold GroupKFold CV (OOF) for the final winners: ZohanResidual, ZohanHRNN.
- **Output:** Overlay files like `overlay_ZohanResidual_Alim_T_out_n.png`, `overlay_ZohanHRNN_Ref_T_out_n.png` into `chap06/`.
- Same axis labels ("Predito" / "Experimental") and error-bar style.

**9. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_todas_imagens.py`**
- **Purpose:** Generates **all** TCC chapter images including **line overlay plots** (NOT scatter). Shows Experimental, Modelo 0D, and ZohanResidual predictions as connected line plots over sorted indices. Also generates OOF scatter plots, learning curves, sweeps, and best-per-family.
- **Output:** `overlay_ZohanResidual_Alim_T_out.png`, `overlay_panel_ZohanResidual.png`, `oof_KerasMLP_ZohanResidual_Restricted_*.png`, all into `chap06/`.

**10. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_todas_imagens_v2.py`**
- **Purpose:** Generates consolidated chapter images including **line overlay plots** (using synthetic/demo data for visualization) and OOF scatter plots. Uses pre-consolidated RMSE values.
- **Output:** `overlay_ZohanResidual_Alim_T_out.png`, `overlay_panel_ZohanResidual.png`, `oof_KerasMLP_ZohanResidual_Restricted_*.png`.

---

### Location 2: `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\` (earlier version codebase)

**11. `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\CodFin\t3.py`**
- **Purpose:** The **original** monolithic training + plotting script. Contains the original definitions of `plot_oof_vs_phy_overlay_per_target()` (line 1028), `plot_oof_vs_phy_overlay_panel()` (line 1100), and `save_overlay_comparison_table()` (line 1159). Also has a full `save_outputs()` runner (line 1360+) that generates overlay plots per family during model selection.
- **Output:** Per-family overlay plots + panel + CSV points.
- Uses scatter plots with "Experimental" on x-axis and "Predito" on y-axis (note: the newer `Codigo-revisado/plots.py` swaps these axes).

---

### Hold-Out Specific Scripts (metric computation, NOT overlay plotting)

These scripts explicitly use a **hold-out 20% split** but do **not** generate overlay plots. They are listed for completeness:

- **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_all_winners.py`** -- Refits all 14 models with an 80/20 stratified hold-out split. Computes CV, OOF, and TEST (hold-out) RMSE/R2 metrics. No overlay plots.
- **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_stage2.py`** -- Refits Stage 2 hybrid models with hold-out 20%. Prints metrics only.
- **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_stage0.py`** -- Refits Stage 0 classical models with hold-out 20%.
- **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\calcular_vencedores.py`** -- Uses Test RMSE (hold-out 20%) to rank winners.

---

### Location 3: `C:\Users\frota\OneDrive\Documentos\Projetos\SLIDES POLI\`

- **No relevant scripts found.** The slidegen package is a LaTeX slide generator and does not contain any overlay/hold-out plot code. The only tangential mention of "experimental" is a string in `mock_backend.py`.

---

## Summary Table (Most Relevant Scripts)

| # | Full Path | Overlay Type | Hold-Out? | Key Functions |
|---|-----------|-------------|-----------|---------------|
| 1 | `...\Codigo-revisado\plots.py` | Scatter (pred vs exp) | No (library) | `plot_oof_vs_phy_overlay_per_target`, `plot_oof_vs_phy_overlay_panel` |
| 2 | `...\Codigo-revisado\file_io.py` | Orchestrator | No (library) | `save_overlay_comparison_table`, `save_outputs` (calls plot funcs) |
| 3 | `...\Codigo-revisado\scripts\generate_overlays.py` | Scatter overlay | Full-data (not hold-out) | HRNN vs 0D, Residual vs 0D |
| 4 | `...\Codigo-revisado\scripts\generate_overlays_oof.py` | Scatter overlay | **OOF (CV hold-out)** | HRNN OOF vs 0D |
| 5 | `...\Codigo-revisado\scripts\regenerate_plots.py` | Scatter overlay | Re-generates from CSV | Reads overlay CSV, re-plots |
| 6 | `...\Codigo-revisado\scripts\gerar_overlays_vencedores.py` | Scatter (Predito x Experimental) | **OOF (CV)** | 3 winners, 3 targets |
| 7 | `...\Codigo-revisado\scripts\gerar_overlays_e_sweeps.py` | Scatter + yerr | **OOF (CV)** | Includes L2/LR sweeps |
| 8 | `...\Codigo-revisado\scripts\gerar_imagens_finais.py` | Scatter + yerr | **OOF (CV)** | Final winners |
| 9 | `...\Codigo-revisado\scripts\gerar_todas_imagens.py` | Line overlay + OOF scatter | **OOF (CV)** | All chapter images |
| 10 | `...\Codigo-revisado\scripts\gerar_todas_imagens_v2.py` | Line overlay (synthetic) | No (demo) | Consolidated chapter images |
| 11 | `...\CodFin\t3.py` | Scatter overlay | OOF (CV) | Original definitions + runner |

The scripts most directly matching "overlay plots (predicted vs experimental) for hold-out" are **#4 (`generate_overlays_oof.py`)** -- which uses explicit OOF (CV hold-out) predictions -- and **#6, #7, #8** (`gerar_overlays_vencedores.py`, `gerar_overlays_e_sweeps.py`, `gerar_imagens_finais.py`) -- which all use 3-fold GroupKFold OOF and label axes as "Predito" and "Experimental".

*Novo passo iniciado*

---

*13 messages | 86 parts | ðŸ’° $0.0135 | â±ï¸ 0h01m55s*

