---
slug: curious-nebula
title: "Find CV metrics in TCC code (@explore subagent)"
date: 2026-07-07
agent: explore
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h01m49s
messages: 13
parts: 94
cost: 0
tokens_input: 96385
tokens_output: 9962
tokens_reasoning: 811
tokens_cache_read: 651648
tokens_cache_write: 0
created: "2026-07-07 17:49:09 UTC"
updated: "2026-07-07 17:50:58 UTC"
---

Sessão com **13 messages**, **94 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | 💾 cache read: 651.6K | ⏱️ 0h01m49s

## 👤 Usuário (2026-07-07 17:49:09 UTC)

Search the directory C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado for any code that performs GroupKFold cross-validation and computes metrics per fold. I need to find:
1. Where GroupKFold or KFold cross-validation is used
2. What metrics are computed per fold (RMSE, R², MAE, etc.)
3. Whether any metric captures the variability/dispersion between folds (like std of RMSE across folds, or similar)
4. Any output logs or CSV files that show per-fold results

Look in all Python scripts, notebooks, and any output files. Search for patterns like "cv", "cross_val", "GroupKFold", "fold", "std", "variability", "score" in .py, .ipynb, .csv, .log files. Be very thorough - check all subdirectories.

## 🤖 Assistente (2026-07-07 17:49:09 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants me to thoroughly search a directory for code related to GroupKFold cross-validation and metrics computation. Let me start by exploring the directory structure and then searching for the relevant patterns.

</details>

### Resposta

I'll start by exploring the directory structure and searching for relevant patterns in parallel.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:49:13 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good, I have a comprehensive view of the directory structure. Now let me search for the key patterns. The main file that likely contains GroupKFold logic is `cv.py` - let me start reading it, and also search for GroupKFold, KFold, cross_val, and fold-related patterns across all Python files and logs.

</details>

### Resposta

Now let me search for the key patterns across all relevant files.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:49:19 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I've found extensive results. Now I need to read the key files more deeply to understand what metrics are computed per fold and whether any captures variability/dispersion between folds. Let me read the main files that do the actual cross-validation work:

1. `runner.py` - the main OOF evaluation
2. `scripts/auto_optimize_mlp.py` - has mean_rmse, std_rmse
3. `scripts/hibridos_cv_completo.py` - has fold_metrics with rmse and r2
4. `scripts/debug_oof_fold.py` - has fold-level rmse
5. `scripts/multi_output_otimizado.py` - has std_rmse
6. `scripts/rodar_agente_tcc.py` - has mean_rmse and std_rmse
7. `scripts/refit_all_stages.py`, `scripts/refit_stage0.py`, `scripts/refit_stage2.py` - these do refitting with CV
8. The results CSV files
9. The pipeline logs

Let me read the critical files to understand the full picture.

</details>

### Resposta

Let me now read the key source files in detail to understand the exact per-fold metric computation.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:49:26 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

I have good detail on the main files. Now let me also look at:
1. `selection.py` - for `evaluate_oof_per_output` function
2. The refit scripts for per-fold metrics
3. The pipeline log to see actual metric values
4. The csv files for table output
5. The `rodar_agente_tcc.py` which has fold_test_rmse.std
6. Other logs showing per-fold results

Let me continue reading more files.

</details>

### Resposta

Now let me read the key evaluation function and remaining important files.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:49:31 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the `evaluate_oof_per_output` function in `selection.py` and also look at the log files to see actual metric outputs, and the CSV files.

</details>

### Resposta

Let me now read the `evaluate_oof_per_output` function and some log/CSV files for actual metric values.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:49:36 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me look deeper into the log files to see actual per-fold RMSE values, and look at results directories for CSV files, and also look at some more scripts that compute fold-level variability like the `computar_dps_reais.py` and `diagnostico_sklearn_vs_keras.py`.

Let me also check the pipeline log as it's too large, but I can grep for specific patterns in it.

</details>

### Resposta

Let me now search the log files for actual per-fold metric values and check additional scripts.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:49:43 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me check the remaining key files. Let me also look at `sweep.py`, `selection.py` for how it handles per-fold metrics from sklearn's `cv_results_`, and some of the result CSV files.

</details>

### Resposta

Let me check the remaining important files and result directories for per-fold outputs.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:49:47 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The CSV files in tcc/ are empty (single line). Let me check the other CSV files and look at what's inside the results directories. Let me also check some key scripts that explicitly report per-fold std deviation.

Let me also look at the generate_overlays_oof.py which shows per-fold RMSE output.

</details>

### Resposta

Let me check additional scripts for per-fold metric output and result directories.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:49:52 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me check the remaining log files for per-fold RMSE values and also check if there are any JSON result files that capture fold-level variability.

</details>

### Resposta

Let me check the remaining logs and search for JSON result files with per-fold data.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:49:58 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me look at the `run_stage2_hibridos.py` script to see its fold-level metrics and how it stores them, as it seems to be one of the most comprehensive ones.

</details>

### Resposta

Let me read the key comprehensive scripts that compute std across folds.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:50:04 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a very comprehensive picture. Let me compile all findings. Let me also quickly look at the JSON result files if they contain per-fold data.

</details>

### Resposta

Let me do a final check for JSON files containing per-fold data.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-07 17:50:09 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a thorough understanding of all the code. Let me compile the comprehensive findings.

</details>

### Resposta

Here is a comprehensive report of all findings.

---

## Complete Analysis of GroupKFold Cross-Validation & Per-Fold Metrics

### 1. WHERE GroupKFold / KFold Is Used

**Central CV Definition:** `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\cv.py`

This file is the **core CV module** and defines 3 strategies:

| Strategy | Function/Class | When Used |
|---|---|---|
| **GroupKFold** | `GroupKFold(n_splits=...)` (line 104 / 122) | When `origin_values` has no real+synth split, or when only groups >=2 unique vals |
| **KFold** | `KFold(n_splits=..., shuffle=True, random_state=42)` (line 126) | When no group column detected (fallback) |
| **Custom: `AugmentedTrainRealTestGroupKFold`** | Custom class (line 47) | When both real and synthetic rows exist in `Origem_dados`; wraps an inner `GroupKFold` (line 76) but forces test sets to contain ONLY real rows |

**Files that import GroupKFold directly (standalone scripts):**

- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\auto_optimize_mlp.py` (line 17)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\analisar_gap.py` (line 7)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\computar_dps_reais.py` (line 8)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\debug_oof_fold.py` (line 21)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\diagnostico_sklearn_vs_keras.py` (line 13)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\ensamble_multiobjective.py` (line 13)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\estrategia_hibrida.py` (line 13)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\estrategia_hibrida_v2.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\fase2_corrigido.py` (line 12)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\fase2_hibridos.py` (line 14)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\generate_overlays_oof.py` (line 15)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_curvas_aprendizado.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_imagens_3targets.py` (line 14)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_imagens_finais.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_oof_vencedores.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_overlays_e_sweeps.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_overlays_vencedores.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_surrogate.py` (line 8)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_sweeps_com_treino_valid.py` (line 13)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_todas_imagens.py` (line 13)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_cv_completo.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_oor_completo.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_oor_v2.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_scikeras_oof.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\hibridos_single_output.py` (line 14)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\keras_flux_final.py` (line 12)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\keras_mlp_puro_flux.py` (line 13)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\keras_single_temps.py` (line 13)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\luc_sweep_independente.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\mlp_nativo_ols.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\multi_output_otimizado.py` (line 11)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\otimizar_baseline_e_hibridos.py` (line 13)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\otimizar_vs_classicos.py` (line 11)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\per_output_gridsearch.py` (line 11)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\pinn_only_test.py` (line 12)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\pipeline_final.py` (line 10)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_all_stages.py` (line 18)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_all_winners.py` (line 20)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_stage0.py` (line 19)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\refit_stage2.py` (line 16)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\rodar_agente_tcc.py` (line 111)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_luc_target.py` (line 61)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_oof_keras.py` (line 43)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage2_hibridos.py` (line 247)
- `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\runner.py` (line 7)

**Most GroupKFold instances use `n_splits=3`** (174 samples, ~139 train, ~35 test across folds). Some scripts use `n_splits=10` (`gerar_surrogate.py`).

---

### 2. WHAT Metrics Are Computed Per Fold

The **primary metrics** computed per fold are:

| Metric | Symbol | Functions Used | Files |
|---|---|---|---|
| **RMSE** (Root Mean Squared Error) | `rmse` | `sklearn.metrics.mean_squared_error` + `np.sqrt` | Nearly every script |
| **R²** (Coefficient of Determination) | `r2` | `sklearn.metrics.r2_score` | `selection.py`, `runner.py`, `hibridos_cv_completo.py`, `refit_*.py`, `multi_output_otimizado.py`, `pinn_only_test.py` |
| **MAE** (Mean Absolute Error) | -- | Not used in per-fold context | -- |

**Target columns** (3 outputs):
- `Alim_T_out` (index 0) -- inlet temperature
- `Ref_T_out` (index 1) -- outlet temperature
- `Flux` (index 2) -- permeate flux (primary target of interest)

**How per-fold RMSE is computed:**

```python
# Typical per-fold pattern (e.g., auto_optimize_mlp.py:74):
rmse_flux = float(np.sqrt(mean_squared_error(Y_true[te, 2], y_pred[:, 2])))
fold_scores.append(rmse_flux)
```

**For multi-output (all 3 targets):**

```python
# hibridos_cv_completo.py:92-94:
rmse = np.sqrt(mean_squared_error(Y_true[te], yp, multioutput='raw_values'))  # [alim, ref, flux]
r2 = r2_score(Y_true[te], yp, multioutput='raw_values')
fold_metrics.append({"rmse": rmse, "r2": r2})
```

---

### 3. WHETHER ANY Metric Captures Variability/Dispersion Between Folds

**YES, several scripts compute std across folds.** Here is the complete list:

#### A. Scripts that compute `np.std()` of per-fold RMSE:

1. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\auto_optimize_mlp.py`** (lines 77-78):
   ```python
   mean_rmse = float(np.mean(fold_scores))
   std_rmse = float(np.std(fold_scores))
   ```
   Reports `RMSE inicial: {rmse:.4f} +- {std:.4f}` and stores `std` per candidate.

2. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\diagnostico_sklearn_vs_keras.py`** (lines 62, 76):
   ```python
   return float(np.mean(fold_flux)), float(np.std(fold_flux))
   ```

3. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\keras_mlp_puro_flux.py`** (lines 95-96):
   ```python
   cv = float(np.mean(fold_flux))
   std = float(np.std(fold_flux))
   ```

4. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\multi_output_otimizado.py`** (lines 113-114):
   ```python
   mean_rmse = fold_metrics.mean(axis=0)
   std_rmse = fold_metrics.std(axis=0)
   ```
   Stores per-target std: `std_alim`, `std_ref`, `std_flux`.

5. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\computar_dps_reais.py`** (lines 93, 112-113):
   ```python
   print(f"  {t}: {[round(x,4) for x in arr]}  mean={arr.mean():.4f}  std={arr.std():.4f}")
   ```
   And uses the **real empirical std across folds** (not pooled) for the **1-SE rule between models**.

6. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\rodar_agente_tcc.py`** (lines 168-169):
   ```python
   mean_rmse = fold_test_rmse.mean(axis=0)
   std_rmse = fold_test_rmse.std(axis=0)
   ```
   Also stores per-fold RMSE values:
   ```python
   "fold_rmse_flux": [float(x) for x in fold_test_rmse[:, 2]]
   ```

7. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage2_hibridos.py`** (lines 303-306):
   ```python
   fold_flux_rmse = np.array(fold_flux_rmse)
   cv_results["mean_test_rmse"].append(float(fold_flux_rmse.mean()))
   cv_results["std_test_rmse"].append(float(fold_flux_rmse.std()))
   cv_results["fold_rmse_list"].append([float(x) for x in fold_flux_rmse])
   ```
   **This is the most complete storage** -- it saves the full per-fold list alongside mean and std.

#### B. Sklearn's built-in `std_test_score` from `cv_results_`:

The main pipeline infrastructure (`runner.py`, `selection.py`) uses `GridSearchCV` / `RandomizedSearchCV` which **automatically** computes `std_test_score` and `mean_test_score` across CV folds.

- **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\selection.py`** (line 21):
  ```python
  def lower_bound_1se(cv_results):
      best_idx = int(np.argmax(cv_results["mean_test_score"]))
      return float(cv_results["mean_test_score"][best_idx] - cv_results["std_test_score"][best_idx])
  ```
  This implements the **1-SE rule** using the CV std across folds.

- **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\runner.py`** (lines 158, 364-367):
  ```python
  df["std_rmse_cv_Flux"] = df["std_test_score"].astype(float)
  # ...
  mean_test = float(cvres["mean_test_score"][i])
  std_test = float(cvres["std_test_score"][i])
  ```

- **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\runner.py`** (line 462):
  ```python
  thr_1se = float(cvres["mean_test_score"][best_idx] - cvres["std_test_score"][best_idx])
  ```

#### C. IMPORTANT CAVEAT on std_test_score semantics:

Sklearn's `std_test_score` in `cv_results_` uses **population std** (`ddof=0`) by default, i.e., `np.std(scores)`. This is a pooled std across all 3 CV folds for each hyperparameter combination. It captures **dispersion across folds**, but with only 3 folds, the uncertainty is large.

The `computar_dps_reais.py` script (item 5 above) explicitly uses `arr.std()` for each target's 3 fold values to apply the **1-SE rule across models** for model selection, which is a more transparent approach.

---

### 4. OUTPUT LOGS AND FILES SHOWING PER-FOLD RESULTS

#### Log files:

| File | Contents |
|---|---|
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\pipeline_run.log` | Main pipeline output. Shows per-fold fit/predict sizes ("Eval OOF fold 1: fit on 102, predict on 72") but does NOT print per-fold RMSE values. Shows `best_score=-0.082120` (neg RMSE for Flux) and `OOF succeeded`. |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\stage2_only_run.log` | Stage 2 hybrid run. Same pattern: shows fold sizes and `best_score` (neg RMSE) but not per-fold RMSE. Also shows sweep data with RMSE comparisons. |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\pipeline_v2.log` | Another pipeline variant log. |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\pipeline_full.log` | Full pipeline log. |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\pipeline_tf.log` | TensorFlow pipeline log. |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\stage0.log` | Stage 0 log (mostly empty). |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\stage1.log` | Stage 1 log (empty file). |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\stage1_v2.log` | Stage 1 v2 log. |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\stage1_alim_full.log` | Alim target focused log. |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\stage1_alim_vbs.log` | Alim target verbose log. |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\stage2_only_run.log` | Stage 2 only run (detailed). |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\run_all_v2.log` | Run-all v2 log. |

**Key observation about logs:** The main pipeline logs do **NOT** print per-fold RMSE values. They only log fold sizes ("fit on 102, predict on 72") and the aggregated `best_score` (which is the mean test score across folds). To see per-fold RMSE values, you must run the specific debug/evaluation scripts.

#### Debug scripts that DO print per-fold RMSE:

1. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\debug_oof_fold.py`** (line 61):
   ```python
   print(f'Fold {fold}, output {k}: RMSE = {rmse:.4f}', flush=True)
   ```

2. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\computar_dps_reais.py`** (line 93):
   ```python
   print(f"  {t}: {[round(x,4) for x in arr]}  mean={arr.mean():.4f}  std={arr.std():.4f}")
   ```

3. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\generate_overlays_oof.py`** (line 126):
   ```python
   print(f"  Fold {fold_idx+1}/{N_SPLITS}: train={len(train_idx)} test={len(test_idx)} rmse={...:.4f}")
   ```

4. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\gerar_surrogate.py`** (line 126):
   ```python
   print(f"  Fold {fold+1}: Flux={rmse[2]:.4f} Alim={rmse[0]:.4f} Ref={rmse[1]:.4f}")
   ```

5. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\rodar_agente_tcc.py`** (lines 180-181):
   ```python
   print(f"  [{i+1:3d}/{N_ITER}] {str(hls):<18} act={act:<5} lr={lr:.0e} l2={l2:.0e} "
         f"Flux_RMSE={mean_rmse[2]:.4f}±{std_rmse[2]:.4f}")
   ```

6. **`C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\scripts\run_stage2_hibridos.py`** (line 309):
   ```python
   print(f"  {str(params):<35} Flux_RMSE={fold_flux_rmse.mean():.4f}±{fold_flux_rmse.std():.4f}")
   ```

#### CSV / output files:

| File | Contents |
|---|---|
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\tcc\Textual\Imagens\chap06\model_selection\tabela_stage0.csv` | Empty file (1 line, no data) |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\tcc\Textual\Imagens\chap06\model_selection\tabela_stage1.csv` | Empty file (1 line, no data) |
| `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\tcc\Textual\Imagens\chap06\model_selection\tabela_stage2.csv` | Empty file (1 line, no data) |
| No JSON files with `fold_rmse` or `std_test` were found in the codebase; these would be generated at runtime by the scripts. |

---

### SUMMARY TABLE

| Question | Answer |
|---|---|
| **1. Where is GroupKFold used?** | Central definition in `cv.py` (lines 3, 76, 104, 122). Used in **50+ Python files** throughout the codebase. Almost always `n_splits=3`. Custom `AugmentedTrainRealTestGroupKFold` wrapper used when data has real+synthetic origin split. |
| **2. What metrics per fold?** | **RMSE** (always), **R²** (most scripts), computed per target (Alim_T_out, Ref_T_out, Flux). MAE is not used. Metrics computed via `sklearn.metrics.mean_squared_error` + `np.sqrt` for RMSE, `sklearn.metrics.r2_score` for R², typically with `multioutput='raw_values'` to get per-target arrays. |
| **3. Variability between folds?** | **YES**. Several scripts compute `np.std(fold_scores)` across the 3 folds: `auto_optimize_mlp.py`, `diagnostico_sklearn_vs_keras.py`, `keras_mlp_puro_flux.py`, `multi_output_otimizado.py`, `computar_dps_reais.py`, `rodar_agente_tcc.py`, `run_stage2_hibridos.py`. Additionally, sklearn's GridSearchCV/RandomizedSearchCV internally computes `std_test_score` (population std, ddof=0) across CV folds, used by the 1-SE selection rule in `selection.py` (line 21) and `runner.py` (line 462). The `computar_dps_reais.py` script is the most explicit about using fold-to-fold std for 1-SE model selection. |
| **4. Per-fold output files?** | No CSV/JSON files containing per-fold values persist on disk in the codebase directory (the three CSV files in `tcc/Textual/...` are empty). Per-fold RMSE values are printed to stdout by debug scripts (`debug_oof_fold.py`, `computar_dps_reais.py`, `generate_overlays_oof.py`, `gerar_surrogate.py`, `rodar_agente_tcc.py`, `run_stage2_hibridos.py`). The `rodar_agente_tcc.py` stores `fold_rmse_flux` in memory but does not persist it. The `run_stage2_hibridos.py` builds a `cv_results` dict with `fold_rmse_list` (all 3 values) but does not export it to a file. Log files show fold sizes and aggregated best scores, but not per-fold RMSE values. |

*Novo passo iniciado*

---

*13 messages | 94 parts | 💰 $0.0000 | ⏱️ 0h01m49s*
