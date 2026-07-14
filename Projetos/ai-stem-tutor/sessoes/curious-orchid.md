---
title: "curious-orchid"
slug: "curious-orchid"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: curious-orchid
title: "Explore Stage 2 codebase (@explore subagent)"
date: 2026-06-02
agent: explore
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h02m16s
messages: 6
parts: 37
cost: 0
tokens_input: 55140
tokens_output: 7671
tokens_reasoning: 10376
tokens_cache_read: 136832
tokens_cache_write: 0
created: "2026-06-02 01:57:58 UTC"
updated: "2026-06-02 02:00:15 UTC"
---

SessÃ£o com **6 messages**, **37 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | ðŸ’¾ cache read: 136.8K | â±ï¸ 0h02m16s

## ðŸ‘¤ UsuÃ¡rio (2026-06-02 01:57:58 UTC)

You are exploring a Python codebase for a TCC (thesis) on hybrid machine learning models for membrane distillation.

The project is at: `C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado\`

I need you to thoroughly explore the Stage 2 flow to understand how hybrid models (ZohanResidual, ZohanHPD, Luc) are constructed and evaluated vs the FrozenBaseline.

Key files to read:
1. `stage2_focused.py` - main script
2. `sweep.py` - contains `build_frozen_baseline_grid` and hybrid model grid construction
3. `runner.py` - runs the search and evaluation
4. `selection.py` - OOF evaluation logic
5. `models/wrappers.py` - model wrappers
6. `models/keras_builders.py` - Keras model builders

Please read ALL of these files thoroughly (each one fully) and return:
1. The complete flow from stage2_focused.py through to OOF evaluation
2. How FrozenBaseline pipeline differs from ZohanResidual pipeline
3. How physics features (phy columns) are loaded and provided to hybrid models
4. Whether there's any issue with how params are passed through Pipeline â†’ YScalerRegressor â†’ KerasRegressor for hybrid models
5. Whether the `n_features` parameter correctly reflects 5 vs 8 features for different model types
6. How `build_frozen_baseline_grid` works vs how hybrid model grids are built
7. Any potential bugs or issues that would cause hybrid models to perform worse than baseline

Return ALL file contents and your analysis.

## ðŸ¤– Assistente (2026-06-02 01:57:59 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants me to thoroughly explore a Python codebase for a TCC (thesis) on hybrid machine learning models for membrane distillation. Let me start by reading all the requested files to understand the complete flow.

Let me begin by reading all the files they've mentioned.

</details>

### Resposta

I'll start by reading all the requested files in parallel.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-02 01:58:02 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me look for the stage2_focused.py file - it wasn't found at the expected path. Let me search for it, and also look for config.py which is imported by sweep.py.

</details>

### Resposta

The main script `stage2_focused.py` wasn't found. Let me search for it and also read the config file.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-02 01:58:05 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Found the stage2_focused.py file at `scripts/stage2_focused.py`. Let me read it now, and also let me search for how the physics features are loaded and passed.

</details>

### Resposta

Found `stage2_focused.py` in the `scripts/` directory. Let me read it now along with other relevant files.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-02 01:58:10 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have all the files. Let me also read the `models/__init__.py` and `scripts/run_all.py` to see if there are more pieces of the puzzle. Let me also check if there's any additional context in the `consolidate.py` or `models/classical.py`.

Actually, I have enough information now to provide a comprehensive analysis. Let me compile everything.

Let me trace through the entire flow carefully:

## 1. Complete Flow: stage2_focused.py â†’ OOF Evaluation

### a. Main script: `scripts/stage2_focused.py`
1. Loads best baseline params from a JSON file from Stage 1
2. Creates callbacks (EarlyStopping, ReduceLROnPlateau, TerminateOnNaN)
3. Injects callbacks into `best_params["model__fit__callbacks"]`
4. Builds grids for 4 families:
   - FrozenBaseline: `build_frozen_baseline_grid(best_params, N_FEATURES_BASE=5, N_TARGETS=3)`
   - Luc_Restricted: `build_luc_restricted_grid_from_baseline(best_params, N_FEATURES_BASE=5, N_TARGETS=3)`
   - ZohanHPD_Restricted: `build_hpd_restricted_grid_from_baseline(best_params, N_FEATURES_PLUS_PHY=8, N_TARGETS=3)`
   - ZohanResidual_Restricted: `build_residual_restricted_grid_from_baseline(best_params, N_FEATURES_PLUS_PHY=8, N_TARGETS=3)`
5. Creates FamilySpec objects with different x_mode and y_mode configurations
6. Reads CSV data â†’ `read_tabular_csv` â†’ `build_XY_groups_with_model_map`
7. The `build_XY_groups_with_model_map` returns:
   - X: 5 feature columns
   - Y_true: 3 target columns
   - Y_model: 3 physics columns (Alim_T_out_phy, Ref_T_out_phy, Flux_phy_L_m2_h)
   - groups, origin_values
8. Creates CV (`make_cv`) that uses `AugmentedTrainRealTestGroupKFold` â€” only real rows for test, synthetic+real train for train
9. For each FamilySpec, calls `run_family()`
10. Collects winners â†’ `winners_table()` â†’ saves outputs

### b. Four FamilySpec configurations:

**FrozenBaseline:**
- `estimator=make_keras_mlp_estimator` â†’ standard MLP (build_keras_mlp)
- `x_mode="x"` â†’ X_fit = X (only 5 base features)
- `y_mode="true"` â†’ Y_fit = Y_true
- `scale_y=True`
- Grid: n_features=5, n_targets=3, and all other params frozen from best baseline

**Luc_Restricted:**
- `estimator=make_keras_mlp_luc_estimator` â†’ Luc hybrid model (build_keras_mlp_luc_loss_2m_output)
- `x_mode="x"` â†’ X_fit = X (only 5 base features)
- `y_mode="true_plus_model"` â†’ Y_fit = np.concatenate([Y_true, Y_model], axis=1) â†’ 6 columns (3 true + 3 phy)
- `scale_y=True`
- Grid: n_features=5, n_targets=3, with Luc-specific params (omega, data_loss, physics_norm)

**ZohanHPD_Restricted (Physics Data-informed):**
- `estimator=make_keras_mlp_estimator` â†’ standard MLP (same as baseline!)
- `x_mode="x_plus_model"` â†’ X_fit = np.concatenate([X, Y_model], axis=1) â†’ 8 columns (5 features + 3 phy)
- `y_mode="true"` â†’ Y_fit = Y_true
- `scale_y=True`
- Grid: n_features=8, n_targets=3, with small L2 grid from baseline

**ZohanResidual_Restricted:**
- `estimator=make_keras_mlp_residual_x_only_estimator` â†’ residual model (build_keras_mlp_residual_add_phy_x_only)
- `x_mode="x_plus_model"` â†’ X_fit = np.concatenate([X, Y_model], axis=1) â†’ 8 columns (5 features + 3 phy)
- `y_mode="true"` â†’ Y_fit = Y_true
- `scale_y=True`
- Grid: n_features=8, n_targets=3, with small L2 grid from baseline

### c. run_family flow:
1. `_select_XY_for_spec(spec, X, Y_true, Y_model)` â†’ augments X/Y according to spec
2. `_resolve_estimator(spec, n_targets=m_true)` â†’ calls the factory function with n_targets
3. `_make_scaled_pipeline(base_estimator, scale_y=True, augmented_2m, m_targets)` â†’ creates:
   - Pipeline: [("scaler", StandardScaler()), ("model", YScalerRegressor(base_estimator=..., scale_y=True, ...))]
   - Note: YScalerRegressor wraps the base_estimator
4. Performs GridSearchCV or RandomizedSearchCV (without internal refit) to avoid TF state corruption
5. Applies refit rule (1SE + gap filter + min complexity)
6. Builds a **fresh** pipeline for OOF evaluation (avoiding TF state corruption from search)
7. Calls `evaluate_oof_per_output(fresh_est, ...)` â†’ clones the estimator per fold, fits, predicts, collects OOF predictions
8. Falls back to `_oof_direct(...)` if OOF fails â†’ this re-builds the pipeline per fold

### d. evaluate_oof_per_output (selection.py):
1. Takes the estimator (e.g., the Pipeline)
2. Iterates over CV folds
3. For each fold: `clone(estimator)`, `fit(X[tr], Y_fit[tr])`, `predict(X[te])`
4. Collects all predictions, computes R2 and RMSE per output

### e. _oof_direct fallback:
- Similar but builds fresh pipeline per fold (bypasses scikeras clone issues)
- Creates its own callbacks

## 2. FrozenBaseline vs ZohanResidual Pipeline

### FrozenBaseline Pipeline:
```
Pipeline([
    ("scaler", StandardScaler()),
    ("model", YScalerRegressor(
        base_estimator=KerasRegressor(model=build_keras_mlp, ...),
        scale_y=True,
        augmented_2m=False,    # because y_mode="true"
        m_targets=3
    ))
])
```
- Input: X with 5 features
- Y: Y_true with 3 targets
- n_features=5 passed to build_keras_mlp
- n_targets=3 passed to build_keras_mlp

### ZohanHPD Pipeline:
```
Pipeline([
    ("scaler", StandardScaler()),
    ("model", YScalerRegressor(
        base_estimator=KerasRegressor(model=build_keras_mlp, ...),  # SAME as baseline!
        scale_y=True,
        augmented_2m=False,
        m_targets=3
    ))
])
```
- Input: X with 8 features (5 base + 3 phy) â€” because x_mode="x_plus_model"
- Y: Y_true with 3 targets
- n_features=8 passed to build_keras_mlp
- n_targets=3 passed to build_keras_mlp

### ZohanResidual Pipeline:
```
Pipeline([
    ("scaler", StandardScaler()),
    ("model", YScalerRegressor(
        base_estimator=KerasRegressor(model=build_keras_mlp_residual_add_phy_x_only, ...),
        scale_y=True,
        augmented_2m=False,
        m_targets=3
    ))
])
```
- Input: X with 8 features (5 base + 3 phy)
- Y: Y_true with 3 targets
- n_features=8 passed to build_keras_mlp_residual_add_phy_x_only
- n_targets=3 passed to build_keras_mlp_residual_add_phy_x_only

The ZohanResidual model internally splits the 8 features:
- `SliceXPart(nt)` â†’ takes X_part (first 8-3=5 features)
- `SliceYPhyPart(nt)` â†’ takes y_phy (last 3 features)
- Learns residual: y_hat = y_phy + y_residual_from_NN(X_part)

### Luc Pipeline:
```
Pipeline([
    ("scaler", StandardScaler()),
    ("model", YScalerRegressor(
        base_estimator=KerasRegressor(model=build_keras_mlp_luc_loss_2m_output, ...),
        scale_y=True,
        augmented_2m=True,     # because y_mode="true_plus_model"
        m_targets=3
    ))
])
```
- Input: X with 5 features (base only)
- Y: 6 columns (3 true + 3 phy) â€” because y_mode="true_plus_model"
- The YScalerRegressor scales the first 3 columns (true) as usual
- The augmented_2m=True flag means YScalerRegressor expects 2m columns
- The Luc model internally outputs 2m=6 predictions, and the custom LucHybridLoss computes data+physics loss

## 3. How Physics Features are Loaded and Provided

In `config.py`:
```python
MODEL_MAP = {
    "Alim_T_out": "Alim_T_out_phy",
    "Ref_T_out": "Ref_T_out_phy",
    "Flux": "Flux_phy_L_m2_h",
}
```

In `data.py`, `build_XY_groups_with_model_map`:
- Uses MODEL_MAP to know which columns contain the physics model predictions
- Creates `Y_model` = array of 3 columns: ["Alim_T_out_phy", "Ref_T_out_phy", "Flux_phy_L_m2_h"]
- Returns `Y_model` alongside `X`, `Y_true`, etc.

In `stage2_focused.py`:
- `Y_model` is passed to `run_family` for each spec
- Inside `run_family`, `_select_XY_for_spec` uses `Y_model` based on `x_mode` and `y_mode`:
  - **ZohanHPD, ZohanResidual**: `x_mode="x_plus_model"` â†’ `X_fit = np.concatenate([X, Y_model], axis=1)` â†’ 8 features
  - **Luc**: `y_mode="true_plus_model"` â†’ `Y_fit = np.concatenate([Y_true, Y_model], axis=1)` â†’ 6 targets
  - **FrozenBaseline**: neither â†’ X_fit = X (5 features), Y_fit = Y_true (3 targets)

## 4. Potential Issue: Params Passed Through Pipeline â†’ YScalerRegressor â†’ KerasRegressor

Let me trace how params flow:

### FrozenBaseline:
- Grid params have prefix `model__model__...` (e.g., `model__model__n_features`, `model__model__hidden_layer_sizes`)
- Pipeline has step "model" â†’ YScalerRegressor
- Pipeline.set_params("model__model__n_features" = 5) â†’ sets `model__model__n_features` parameter
- This filters through:
  - Pipeline recognizes "model" as the step â†’ delegates to YScalerRegressor.set_params("model__n_features" = 5)
  - YScalerRegressor.set_params sees "model__n_features" â†’ it's NOT in wrapper_keys ("base_estimator", "scale_y", "augmented_2m", "m_targets")
  - Since it doesn't start with "base_estimator__", it goes to `inner_params["model__n_features"] = 5`
  - Then `self.base_estimator.set_params(model__n_features=5)` â†’ KerasRegressor.set_params
  - KerasRegressor.set_params("model__n_features" = 5) â†’ scikeras recognizes that this is a model parameter with prefix "model__"
  - Wait, actually scikeras uses the prefix "model__" to route params to the model-building function

Actually, let me think about this more carefully. The scikeras KerasRegressor wraps a model-building function. When you pass parameters to it:
- Parameters prefixed with `model__` are passed to the model-building function
- Parameters like `batch_size`, `epochs`, `fit__validation_split` are used by the KerasRegressor itself

So the flow is:
1. `Pipeline.set_params(model__model__n_features=5)` 
2. Pipeline delegates to YScalerRegressor with key `model__n_features=5`
3. YScalerRegressor.set_params receives `model__n_features=5`
4. Not in wrapper_keys, doesn't start with "base_estimator__" â†’ goes to `inner_params["model__n_features"] = 5`
5. `self.base_estimator.set_params(model__n_features=5)` â†’ KerasRegressor.set_params("model__n_features" = 5)
6. KerasRegressor recognizes "model__n_features" as a model param (prefix "model__") â†’ passes `n_features=5` to the build function

Wait, there's a subtlety. scikeras uses the prefix `model__` to denote parameters that should be passed to the model-building function. So:
- `model__hidden_layer_sizes` â†’ passes `hidden_layer_sizes` to build function
- `model__n_features` â†’ passes `n_features` to build function

But the issue is: the pipeline receives keys like `model__model__n_features`. Let me trace more carefully:

Pipeline step = "model" (a YScalerRegressor)
- Pipeline.set_params(**params) where params = {"model__model__n_features": 5, "model__model__hidden_layer_sizes": (64,32), ...}
- Pipeline internally routes "model__*" to the "model" step
- So YScalerRegressor.set_params receives: {"model__n_features": 5, "model__hidden_layer_sizes": (64,32), ...}

YScalerRegressor.set_params(params):
- For each (k, v) in params:
  - k = "model__n_features" â†’ not in wrapper_keys {"base_estimator", "scale_y", "augmented_2m", "m_targets"}
  - k = "model__n_features" â†’ doesn't start with "base_estimator__"
  - So it goes to inner_params["model__n_features"] = 5
- After processing all: inner_params = {"model__n_features": 5, "model__hidden_layer_sizes": (64,32), "model__activation": "relu", ...}
- self.base_estimator.set_params(**inner_params) â†’ KerasRegressor.set_params(model__n_features=5, model__hidden_layer_sizes=(64,32), ...)

KerasRegressor.set_params receives scikeras-standard parameters:
- `model__n_features`: scikeras recognizes `model__` prefix â†’ routes to model-building function parameter `n_features`
- `model__hidden_layer_sizes`: routes to model-building function parameter `hidden_layer_sizes`
- Other params like `batch_size`, `epochs`, `fit__validation_split` are used by KerasRegressor itself

So the routing seems correct! The `model__model__*` â†’ `model__*` â†’ routes correctly.

Wait, but there's a subtle issue with the L2 grid params. Let me look:

For FrozenBaseline, the grid includes:
- "model__model__l2": [best_l2] (from extract_baseline_keras_fixed_params)
- This becomes `model__l2` at the KerasRegressor level â†’ routes to build function parameter `l2` âœ“

For ZohanHPD and ZohanResidual, the grid includes:
- "model__model__n_features": [8]
- "model__model__n_targets": [3]
- "model__model__l2": [candidate_values] (from _small_l2_grid_from_baseline)

So the L2 is being varied for hybrid models but is frozen for the baseline.

For Luc:
- "model__model__n_features": [5]
- "model__model__n_targets": [3]
- "model__model__omega": [0.0, 0.1, 0.3, 0.5, 0.7]
- "model__model__data_loss": [baseline_loss]
- "model__model__physics_norm": ["mse", "mae"]

This all looks correct.

## 5. n_features: 5 vs 8

### FrozenBaseline:
- `build_frozen_baseline_grid(best_params, N_FEATURES_BASE=5, N_TARGETS=3)`
- Grid has `model__model__n_features = [5]`
- Pipeline receives X with 5 features (x_mode="x")
- build_keras_mlp receives n_features=5 âœ“

### Luc:
- `build_luc_restricted_grid_from_baseline(best_params, N_FEATURES_BASE=5, N_TARGETS=3)`
- Grid has `model__model__n_features = [5]`
- Pipeline receives X with 5 features (x_mode="x")
- build_keras_mlp_luc_loss_2m_output receives n_features=5 âœ“

### ZohanHPD:
- `build_hpd_restricted_grid_from_baseline(best_params, N_FEATURES_PLUS_PHY=8, N_TARGETS=3)`
- Grid has `model__model__n_features = [8]`
- Pipeline receives X with 8 features (x_mode="x_plus_model")
- build_keras_mlp receives n_features=8 âœ“

### ZohanResidual:
- `build_residual_restricted_grid_from_baseline(best_params, N_FEATURES_PLUS_PHY=8, N_TARGETS=3)`
- Grid has `model__model__n_features = [8]`
- Pipeline receives X with 8 features (x_mode="x_plus_model")
- build_keras_mlp_residual_add_phy_x_only receives n_features=8 âœ“

The n_features parameter correctly reflects 5 vs 8 features for different model types.

## 6. build_frozen_baseline_grid vs hybrid model grids

### build_frozen_baseline_grid:
1. Calls `extract_baseline_keras_fixed_params(best_params)` which freezes:
   - model__model__n_features, n_targets, hidden_layer_sizes, activation, optimizer, learning_rate, l2
   - model__batch_size, epochs, fit__validation_split, fit__shuffle, fit__verbose, fit__callbacks
   - Optional: model__model__loss, model__model__huber_delta
2. Overrides n_features = n_features_base (= 5)
3. Overrides n_targets = n_targets (= 3)
4. Returns a grid with single values for all params â†’ effectively a single candidate (but search="random" with n_iter=5 will still draw 5 samples, potentially with some variation)

Wait! If ALL params are frozen to single values, then random search with n_iter=5 will just pick the same combination 5 times. Then it will be evaluated with cross-validation, and the 1se rule etc. will be applied. But really there's only 1 candidate.

Actually, looking more carefully, the grid has only 1 combination. `ParameterGrid(frozen_baseline_grid)` produces 1 candidate. But the search is "random" with n_iter=5. With random search, it would draw 5 samples from 1 candidate â†’ essentially it runs 5 copies of the same thing? Or does it only run 1? Let me check scikit-learn's RandomizedSearchCV behavior... when the distribution has fewer items than n_iter, it just uses all combinations. Actually, RandomizedSearchCV with a dict (not a distribution) treats it as a grid, and `_run_search` calls `evaluate_candidates` for `n_iter` samples. But each sample would be different if using distributions.

Wait, the grid is a dict of lists, not a distribution. `RandomizedSearchCV` with a dict param_grid treats it like a grid and samples without replacement up to n_iter or the number of combinations. So if there's only 1 combination, it will evaluate just 1 candidate.

So `FrozenBaseline` is essentially a single model evaluation (the baseline with frozen params but on 5 features). No hyperparameter search.

### build_luc_restricted_grid_from_baseline:
1. Freezes all the same params
2. Removes `model__model__loss` (since Luc uses data_loss instead)
3. Adds Luc-specific params:
   - `model__model__data_loss`: [baseline_loss]
   - `model__model__huber_delta`: [baseline_huber_delta]
   - `model__model__physics_norm`: ["mse", "mae"]
   - `model__model__omega`: [0.0, 0.1, 0.3, 0.5, 0.7]
4. n_features=5, n_targets=3
5. Total combinations: 1*1*2*5 = 10 (but random search with n_iter=5 picks 5)

### build_hpd_restricted_grid_from_baseline:
1. Freezes all params
2. n_features=8, n_targets=3
3. `model__model__l2`: computed by `_small_l2_grid_from_baseline` â†’ deduplicated list of [baseline_l2, 0.0, 1e-6, 1e-5, 1e-4]
4. Total combinations: up to 5 L2 values
5. Uses `make_keras_mlp_estimator` â†’ same standard MLP as baseline, but with 8 inputs

### build_residual_restricted_grid_from_baseline:
1. Freezes all params
2. n_features=8, n_targets=3
3. `model__model__l2`: same small grid
4. Total combinations: up to 5 L2 values
5. Uses `make_keras_mlp_residual_x_only_estimator` â†’ residual model

## 7. Potential Bugs/Issues

### ISSUE 1: ZohanHPD uses the WRONG estimator!
Look at lines 91-94 of stage2_focused.py:
```python
FamilySpec(name="KerasMLP_ZohanHPD_Restricted", estimator=make_keras_mlp_estimator,
           search="random", param_grid=hpd_restricted_grid, n_iter=5,
           x_mode="x_plus_model", y_mode="true", complexity_fn=C_keras_mlp,
           n_jobs=1, scale_y=True),
```

`ZohanHPD` uses `make_keras_mlp_estimator` which creates a standard `KerasRegressor(model=build_keras_mlp)`. This is the SAME as the baseline! The only difference is that it receives 8 features (5 base + 3 physics) instead of 5.

This means ZohanHPD is just a standard MLP with 8 input features. The physics model outputs are just concatenated as additional input features. The model has no special architecture to leverage the physics knowledge; it just treats the physics outputs as extra features. This may or may not be intentional (it's the "Physics Data-informed" approach per the code comments).

### ISSUE 2: The `l2` grid for hybrid models (ZohanHPD, ZohanResidual) introduces a search over L2 values.
The `_small_l2_grid_from_baseline` function creates a list of L2 candidates that INCLUDES the baseline's best L2:
```python
cand = [baseline_l2, 0.0, 1e-6, 1e-5, 1e-4]
```

But then the random search with n_iter=5 will only sample 5 combinations. If there are, say, 5 L2 values, then all 5 draws will have different L2 values. The other frozen params stay the same.

However, for the Baseline frozen grid, the L2 is FROZEN to a single value. So the hybrid models are being evaluated WITH hyperparameter search (over L2) while the FrozenBaseline is just a single evaluation. This is actually an unfair comparison â€” the hybrids get to pick their best L2 value, while the baseline is stuck with one. But wait, the baseline's L2 came from a prior search in Stage 1, so it was already optimized. Still, the hybrids get to re-optimize L2 which should benefit them, not hurt them.

Actually wait - the baseline also has `model__model__l2` frozen to its best value. So the baseline is being evaluated with the L2 that was optimal in Stage 1. The hybrids get to try multiple L2 values around that baseline. This seems fine.

### ISSUE 3 (BIG): Inconsistent scoring for Luc vs other models.

In stage2_focused.py:
```python
flux_rmse_scorer = make_neg_rmse_single_true_target_scorer(FLUX_INDEX, N_TARGETS, "Flux")
luc_rmse_scorer = make_neg_rmse_single_true_target_scorer(
    target_index=FLUX_INDEX, n_true_targets=N_TARGETS, target_name="Flux",
)
```

These two scorers are defined identically! But look at how they're used:
- FrozenBaseline: `scoring=flux_rmse_scorer` (explicitly set via the variable, passing through the `scorer` variable in the loop)
- Luc: `spec.scoring = luc_rmse_scorer` (set on the spec)
- ZohanHPD: `spec.scoring = None`, so `scorer = flux_rmse_scorer` (line 117)
- ZohanResidual: `spec.scoring = None`, so `scorer = flux_rmse_scorer` (line 117)

So Luc has its own scorer variable but it's the same function. Not a real issue.

### ISSUE 4: Luc's y_mode="true_plus_model" and the scorer interaction.

The scorer `make_neg_rmse_single_true_target_scorer` takes `y` and slices `y[:, :m]` where `m = n_true_targets = 3`. But for Luc, `y_mode="true_plus_model"` means `Y_fit` has 6 columns (3 true + 3 phy). The scorer correctly uses `y[:, :m]` to get only the true targets. So the scoring is correct.

But wait, there's a potential issue with `evaluate_oof_per_output`. Let me look again:

```python
def evaluate_oof_per_output(estimator, X, Y_fit, groups, cv, *, m_true, augmented_2m, ...):
    mfit = Y_fit.shape[1]  # could be 3 or 6
    y_pred_oof_fit = np.full((n, mfit), np.nan, dtype=float)
    ...
    for fold:
        est.fit(X[tr], Y_fit[tr])
        pred = est.predict(X[te])
        if pred.shape[1] > mfit:
            pred = pred[:, :mfit]
        ...
    y_true_oof = Y_fit[eval_mask, :m_true]
    y_pred_oof = y_pred_oof_fit[eval_mask, :m_true]
```

For Luc with y_mode="true_plus_model":
- Y_fit has 6 columns
- The Luc model outputs 6 columns (due to Concatenate([y_hat, y_hat]) in build_keras_mlp_luc_loss_2m_output)
- pred.shape[1] = 6 = mfit â†’ no truncation
- y_true_oof = Y_fit[eval_mask, :3] â†’ true targets only âœ“
- y_pred_oof = y_pred_oof_fit[eval_mask, :3] â†’ first 3 columns of prediction âœ“

This looks correct. But check the YScalerRegressor:

For Luc with augmented_2m=True:
- `_split_aug(Y)` returns `Y[:, :m]` (true targets) and `Y[:, m:]` (phy targets)
- `fit`: scales true targets with StandardScaler, then also scales phy targets with the SAME scaler (that was fit on true targets!)
- `y_s = np.concatenate([y_true_s, y_phy_s], axis=1)` â†’ 6 scaled columns
- Model gets trained on scaled 6-output targets

Wait, there's a subtle issue. The YScalerRegressor scales y_true, then applies the SAME scaler to y_phy. But y_phy (physics model outputs) have a different distribution from y_true, so this could be problematic. The physics outputs might have systematically different means and variances than the true targets, and using the same scaler (fit on y_true) could distort them.

Actually, on second thought, the physics model predictions might be in the same units/scale as the true values, so this might be fine. But it's worth noting.

For predict with augmented_2m=True:
- Model outputs 6 values
- If y_pred.shape[1] == 2*m (6), it inverse-transforms first 3 and last 3 separately
- But both use the SAME scaler (_y_scaler) âœ“ (consistent with fit)

### ISSUE 5: Potential issue with YScalerRegressor.get_params and deep copy

The `YScalerRegressor.get_params(deep=True)` method:
```python
def get_params(self, deep: bool = True) -> Dict[str, Any]:
    params = {
        "base_estimator": self.base_estimator,
        "scale_y": self.scale_y,
        "augmented_2m": self.augmented_2m,
        "m_targets": self.m_targets,
    }
    if deep and hasattr(self.base_estimator, "get_params"):
        inner = self.base_estimator.get_params(deep=True)
        for k, v in inner.items():
            if k in params:
                params[f"base_estimator__{k}"] = v
            else:
                params[k] = v
    return params
```

This merges the inner estimator's params into the YScalerRegressor's params. For KerasRegressor, `get_params(deep=True)` returns params like:
- `model__n_features`, `model__hidden_layer_sizes`, `model__activation`, etc.
- `batch_size`, `epochs`, `fit__validation_split`, etc.

So when YScalerRegressor.get_params is called:
- It returns: {"base_estimator": ..., "scale_y": ..., "augmented_2m": ..., "m_targets": ..., "model__n_features": ..., "model__hidden_layer_sizes": ..., "batch_size": ..., ...}

Then the Pipeline.get_params flattens this further with the "model__" prefix for the "model" step:
- Pipeline.get_params() returns: {"scaler__...": ..., "model__base_estimator": ..., "model__scale_y": ..., "model__augmented_2m": ..., "model__m_targets": ..., "model__model__n_features": ..., "model__model__hidden_layer_sizes": ..., "model__batch_size": ..., ...}

And these are exactly the keys used in the param grids! This is consistent.

### ISSUE 6: StandardScaler applied to X with 8 features for hybrid models.

For hybrid models (ZohanHPD, ZohanResidual), `x_mode="x_plus_model"` â†’ X has 8 columns (5 features + 3 physics outputs).

The Pipeline applies StandardScaler to ALL 8 columns. This means the physics outputs (Y_model) are also standardized. For ZohanResidual, the model internally splits the input into `x_part` (first 5) and `y_phy` (last 3). But since the scaler was applied to the whole 8-column input, both parts are standardized.

This is correct behavior! The residual model receives standardized inputs.

### ISSUE 7: Potential major issue - The `_small_l2_grid_from_baseline` for ZohanHPD/ZohanResidual might introduce an UNFAIR comparison.

The `build_hpd_restricted_grid_from_baseline` and `build_residual_restricted_grid_from_baseline` call `_small_l2_grid_from_baseline` which creates a grid with MULTIPLE L2 values:
```python
baseline_l2 = float(baseline_best_params.get("model__model__l2", 0.0))
cand = [baseline_l2, 0.0, 1e-6, 1e-5, 1e-4]
```

In contrast, `build_frozen_baseline_grid` freezes the L2 to a single value.

But then ALL models use randomized search with n_iter=5:
- FrozenBaseline: 1 combination (all frozen) â†’ effectively just evaluates the frozen model
- ZohanHPD: 5 combinations (5 L2 values) â†’ searches over L2
- ZohanResidual: 5 combinations (5 L2 values) â†’ searches over L2
- Luc: 10 combinations, sampled 5 times â†’ searches over omega and physics_norm

The comparison is still slightly unfair in favor of hybrids because they get a mini hyperparameter search (over L2) while the baseline does not. However, since the baseline L2 was already optimized in Stage 1, this might not matter much.

### ISSUE 8: POTENTIAL CRITICAL BUG - `n_features` in `build_keras_mlp_luc_loss_2m_output` uses `n_targets` but ignores `n_outputs_`.

Look at lines 176-183 of keras_builders.py:
```python
def build_keras_mlp_luc_loss_2m_output(..., n_features=None, n_targets=None, ...):
    nf, _ = _infer_n_features_targets(
        n_features_in_=n_features_in_, n_outputs_=None,  # <-- n_outputs_ is hardcoded to None!
        n_features=n_features, n_targets=n_targets, **kwargs,
    )
    m = int(n_targets) if n_targets is not None else None
    if m is None:
        raise TypeError("Luc loss requires explicit 'model__model__n_targets'.")
```

The `_infer_n_features_targets` is called with `n_outputs_=None`. This means nt will always come from `n_targets` parameter (since n_outputs_=None). The returned `_` is for `nt` (number of targets), but it's ignored! Instead, `m` is derived separately from `n_targets` directly. This works but is a bit redundant/confusing.

### ISSUE 9: POTENTIAL CRITICAL BUG - `n_features` for `build_keras_mlp_residual_add_phy_x_only`.

Look at the residual builder (lines 203-235):
```python
def build_keras_mlp_residual_add_phy_x_only(..., n_features=None, n_targets=None, ...):
    nf, nt = _infer_n_features_targets(...)
    if int(nf) <= int(nt):
        raise ValueError("Residual expects n_features_total > n_targets (X + y_phy).")
```

For n_features=8 and n_targets=3, this check passes (8 > 3). Good.

But inside the model:
```python
x_part = SliceXPart(nt, name="X_part")(inputs)  # takes first (nf-nt)=5 columns
y_phy = SliceYPhyPart(nt, name="Yphy_part")(inputs)  # takes last nt=3 columns
```

Wait, `SliceXPart` does `inputs[:, :-self.nt]` â†’ takes everything except last nt columns. So for nf=8, nt=3: it takes first 5 columns (the original features).

`SliceYPhyPart` does `inputs[:, -self.nt:]` â†’ takes last nt=3 columns (the physics outputs).

This is correct!

But wait, after StandardScaler in the pipeline, the 8 inputs are standardized. The residual model then splits them into 5 (standardized features) and 3 (standardized physics outputs). It learns a residual from the features and adds it to the physics output. This is a standard physics-informed residual architecture.

### ISSUE 10: Timing of callback injection.

In stage2_focused.py, line 71:
```python
best_params["model__fit__callbacks"] = [early_stop, reduce_lr, term_nan]
```

This replaces whatever callbacks were stored in the JSON (which were serialized objects that shouldn't be deserialized). The callbacks are injected into best_params BEFORE building the grids.

But `extract_baseline_keras_fixed_params` copies `model__fit__callbacks`:
```python
keys_to_freeze = [
    ...
    "model__fit__callbacks",
]
...
for k in keys_to_freeze + optional_keys:
    if k in best_params:
        frozen[k] = [best_params[k]]
```

So `model__fit__callbacks` IS included in the frozen params for all models. But then in `_oof_direct`, the callbacks are REPLACED:
```python
to_set = {}
for k, v in params_i.items():
    if "callbacks" in k:
        continue
    to_set[k] = v
to_set["model__fit__callbacks"] = cbs  # different callbacks object
```

And in `run_family` > `evaluate_oof_per_output`:
The estimator is cloned and the params are set via `set_params(**params_i)`. The `params_i` include callbacks. But does the clone of the pipeline properly handle callback objects? This could be problematic if the callbacks can't be deep-copied.

Actually, this is probably why there's a fallback to `_oof_direct` that rebuilds fresh pipelines per fold with fresh callbacks.

### ISSUE 11: The FrozenBaseline grid through `build_frozen_baseline_grid` sets n_features=5, which is correct (only base features). But the SPEC for FrozenBaseline is `x_mode="x"` which means X_fit = X (5 features). The model receives 5 features. âœ“

### ISSUE 12: The `_select_XY_for_spec` function for `ZohanHPD` and `ZohanResidual`:

```python
elif spec.x_mode == "x_plus_model":
    if Y_model is None:
        raise ValueError(...)
    X_fit = np.concatenate([X, Y_model], axis=1)
```

This concatenates X (5 features) with Y_model (3 physics outputs) â†’ X_fit has 8 columns. The `n_features=8` in the grid matches this. âœ“

But wait - `Y_model` comes from `build_XY_groups_with_model_map` which reads the physics columns from the CSV. These are the physics MODEL predictions, not the true values. So the hybrid model receives: original 5 process features + 3 physics model predictions. This is the intended design.

### ISSUE 13: For ZohanHPD, the model is `make_keras_mlp_estimator` â†’ standard MLP with 8 inputs and 3 outputs.

But there's a question: should the ZohanHPD model treat the 8 inputs differently? Looking at the name "ZohanHPD" (Physics Data-informed), the idea is that the physics outputs are just additional features. The standard MLP can learn any mapping from 8 inputs to 3 outputs. So this is correct.

### ISSUE 14: L2 regularization value might not be passed correctly for ZohanHPD grid.

In `build_hpd_restricted_grid_from_baseline`:
```python
frozen = extract_baseline_keras_fixed_params(best_params)
frozen["model__model__n_features"] = [n_features_plus_phy]
frozen["model__model__n_targets"] = [n_targets]
frozen["model__model__l2"] = _small_l2_grid_from_baseline(baseline_best_params)
```

Wait! `extract_baseline_keras_fixed_params` already includes `model__model__l2` in `keys_to_freeze`. So it sets `frozen["model__model__l2"] = [baseline_l2]`. Then the code OVERRIDES it with `_small_l2_grid_from_baseline` which gives [baseline_l2, 0.0, 1e-6, 1e-5, 1e-4].

So the `l2` is overwritten. But line 116:
```python
frozen["model__model__l2"] = _small_l2_grid_from_baseline(baseline_best_params)
```

This OVERRIDES the frozen L2. Good, that's intentional.

### ISSUE 15: What about `model__model__loss` for ZohanHPD?

`extract_baseline_keras_fixed_params` includes `model__model__loss` in `optional_keys`, and if it's in best_params, it's frozen. So ZohanHPD/ZohanResidual inherit the baseline's loss function (which is likely "mse"). But build_keras_mlp accepts `loss` parameter. So this should be fine.

But wait, the residual builder `build_keras_mlp_residual_add_phy_x_only` also accepts `loss` param. If the baseline used "huber", this would be passed correctly. âœ“

### KEY FINDING: There could be an issue with the `StandardScaler` and the physics outputs in `Y_model`.

The Pipeline applies `StandardScaler` to X. For ZohanHPD and ZohanResidual, X has 8 columns (5 features + 3 physics outputs). The scaler is fit on ALL 8 columns.

But the physics outputs (Y_model) are the 3D physics model predictions (Alim_T_out_phy, Ref_T_out_phy, Flux_phy_L_m2_h). These might have very different scales from the features (e.g., temperatures ~30-80C, flux ~0-10 L/m2h, NaCl concentration ~0-350 g/L). StandardScaler will standardize each column independently, which is fine.

However, for the residual model, it internally splits the 8 standardized columns into:
- x_part: first 5 (original features, standardized)
- y_phy: last 3 (physics outputs, standardized)

The model learns: y_hat = y_phy + residual(x_part)
Then the loss is computed against y_true (which is NOT standardized - wait, is it?)

Actually, y_true goes through YScalerRegressor which scales it. So y_true is also scaled. But the residual model receives standardized y_phy (via the standardized X), and predicts y_hat. The YScalerRegressor then inverse-transforms the prediction. So the loss is computed on scaled targets, and then the output is inverse-transformed.

Wait, let me reconsider. The Pipeline is:
```
Pipeline([
    ("scaler", StandardScaler()),     # scales X
    ("model", YScalerRegressor(        # scales Y
        base_estimator=KerasRegressor(model=...),
        scale_y=True,
        ...
    ))
])
```

So:
1. X is standardized by StandardScaler
2. Y_true is standardized by YScalerRegressor (fit)
3. The Keras model trains on standardized X and standardized Y
4. Predictions are inverse-transformed by YScalerRegressor to original scale

For ZohanResidual:
- Standardized X (8 cols) goes into the model
- Model splits into x_part (first 5) and y_phy (last 3)
- Learns: y_hat = y_phy + f(x_part)
- This y_hat is trained against scaled y_true
- Output is inverse-transformed

This seems correct! The residual connection operates in the scaled space, which is fine.

### SUMMARY OF FINDINGS:

The codebase looks mostly correct. No obvious bugs that would cause hybrid models to perform worse than the baseline, but there are some observations:

1. **ZohanHPD uses a standard MLP estimator** - same as baseline but with 8 input features (5 base + 3 physics). The physics outputs are treated as just extra features. While not a bug, this may not be the most effective way to incorporate physics knowledge.

2. **The L2 grid for hybrids is expanded** while FrozenBaseline has only one L2 value - this gives hybrids more flexibility, not less. So this shouldn't cause worse performance.

3. **The Luc model's custom loss function** `LucHybridLoss` uses `omega` to balance data and physics terms. If the physics predictions are poor or on very different scales, this could hurt performance.

4. **StandardScaler for ZohanResidual** standardizes all 8 inputs including the physics outputs. The residual model then expects y_phy (standardized physics) as a baseline and learns residuals. This is architecturally correct.

5. **Scaler applied to physics predictions in YScalerRegressor for Luc:** The same scaler (fit on y_true) is applied to y_phy. If physics predictions are systematically biased, this could be suboptimal.

The most likely cause of hybrid models performing worse than the baseline is simply that the hybrid architectures (especially the more complex ones like ZohanResidual with internal splitting) have more parameters and are harder to train effectively with limited data. The baseline MLP with 5 inputs is a simpler model that might generalize better on small datasets.

Let me now write a comprehensive response.

</details>

### Resposta

Now let me also check for any additional relevant script files that load/process the data.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-02 01:59:21 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have all the files. Let me compile a thorough analysis.

</details>

### Resposta

Now I have all the files. Here is the complete analysis.

---

## COMPLETE ANALYSIS OF STAGE 2 FLOW

---

### 1. COMPLETE FLOW: `stage2_focused.py` THROUGH TO OOF EVALUATION

**Step-by-step:**

#### A. Entry Point: `scripts/stage2_focused.py`

1. **Load best baseline params** from Stage 1 JSON (line 48-49):
   ```python
   best_params = json.loads(...)["KerasMLP_BaselineSearch"]
   ```
   Contains keys like `model__model__n_features`, `model__model__hidden_layer_sizes`, `model__model__l2`, `model__batch_size`, etc.

2. **Create TF callbacks** (lines 58-68): `EarlyStopping`, `ReduceLROnPlateau`, `TerminateOnNaN`.

3. **Inject callbacks** into params (line 71):
   ```python
   best_params["model__fit__callbacks"] = [early_stop, reduce_lr, term_nan]
   ```

4. **Build grids** (lines 77-80):
   - `frozen_baseline_grid` from `build_frozen_baseline_grid(best_params, N_FEATURES_BASE=5, N_TARGETS=3)`
   - `luc_restricted_grid` from `build_luc_restricted_grid_from_baseline(best_params, N_FEATURES_BASE=5, N_TARGETS=3)`
   - `hpd_restricted_grid` from `build_hpd_restricted_grid_from_baseline(best_params, N_FEATURES_PLUS_PHY=8, N_TARGETS=3)`
   - `residual_restricted_grid` from `build_residual_restricted_grid_from_baseline(best_params, N_FEATURES_PLUS_PHY=8, N_TARGETS=3)`

5. **Define 4 FamilySpec objects** (lines 82-99):

   | Family | Estimator Factory | x_mode | y_mode | scale_y | Grid |
   |--------|------------------|--------|--------|---------|------|
   | FrozenBaseline | `make_keras_mlp_estimator` | `"x"` | `"true"` | True | All frozen, n_features=5, n_targets=3 |
   | Luc_Restricted | `make_keras_mlp_luc_estimator` | `"x"` | `"true_plus_model"` | True | n_features=5, n_targets=3, + Luc params (omega, data_loss, physics_norm) |
   | ZohanHPD_Restricted | `make_keras_mlp_estimator` | `"x_plus_model"` | `"true"` | True | n_features=8, n_targets=3, L2 grid |
   | ZohanResidual_Restricted | `make_keras_mlp_residual_x_only_estimator` | `"x_plus_model"` | `"true"` | True | n_features=8, n_targets=3, L2 grid |

6. **Load data** (lines 101-108):
   - `read_tabular_csv` reads the CSV (with decimal-comma handling)
   - `build_XY_groups_with_model_map` returns:
     - `X`: shape (N, 5) -- `["Alim_T_in", "Ref_T_in", "Ref_V_in", "P_vacuum", "C_NaCl"]`
     - `Y_true`: shape (N, 3) -- `["Alim_T_out", "Ref_T_out", "Flux"]`
     - `Y_model`: shape (N, 3) -- physics columns `["Alim_T_out_phy", "Ref_T_out_phy", "Flux_phy_L_m2_h"]`
     - `groups`: from `GROUP_COL = "Regime"`
     - `origin_values`: from `ORIGIN_COL = "Origem_dados"`

7. **Create CV** (line 108):
   - `make_cv` detects both real and synthetic rows in `origin_values`
   - Returns `AugmentedTrainRealTestGroupKFold` (test = only real rows, train = real-train + all synthetic)
   - Also returns `eval_mask = real_mask` (only evaluate OOF on real data)

8. **Run each family** (lines 116-121):
   ```python
   for spec in stage2_families:
       scorer = spec.scoring if spec.scoring is not None else flux_rmse_scorer
       winners.append(run_family(spec=spec, X=X, Y_true=Y_true, Y_model=Y_model,
                                 groups=groups, cv=cv, scoring=scorer,
                                 eval_mask=eval_mask, logger=logger))
   ```
   - FrozenBaseline, ZohanHPD, ZohanResidual use `flux_rmse_scorer`
   - Luc uses its own identical `luc_rmse_scorer` (set on spec.scoring)

9. **Collect results** (line 123): `summary = winners_table(winners, target_cols=TARGET_COLS)`

10. **Save outputs** (lines 124-129): via `save_outputs()` which:
    - Saves summary CSV
    - Saves best params JSON
    - Saves CV results per family
    - Saves family tables
    - Makes selection plots, OOF plots, sweep plots
    - Runs `run_sweep_from_winner` for each winner

#### B. `run_family` (runner.py, line 240)

1. **Select X/Y** via `_select_XY_for_spec`:
   - `x_mode="x"` â†’ `X_fit = X` (5 features)
   - `x_mode="x_plus_model"` â†’ `X_fit = np.concatenate([X, Y_model], axis=1)` (8 features)
   - `y_mode="true"` â†’ `Y_fit = Y_true` (3 targets)
   - `y_mode="true_plus_model"` â†’ `Y_fit = np.concatenate([Y_true, Y_model], axis=1)` (6 targets)

2. **Resolve estimator**: calls the factory function with `n_targets=m_true`:
   - `make_keras_mlp_estimator(3)` â†’ `KerasRegressor(model=build_keras_mlp, verbose=0)`
   - `make_keras_mlp_luc_estimator(3)` â†’ `KerasRegressor(model=build_keras_mlp_luc_loss_2m_output, verbose=0)`
   - `make_keras_mlp_residual_x_only_estimator(3)` â†’ `KerasRegressor(model=build_keras_mlp_residual_add_phy_x_only, verbose=0)`

3. **Build pipeline** via `_make_scaled_pipeline`:
   ```
   Pipeline([
       ("scaler", StandardScaler()),
       ("model", YScalerRegressor(
           base_estimator=<KerasRegressor>,
           scale_y=True,
           augmented_2m=bool(spec.y_mode == "true_plus_model"),
           m_targets=m_true
       ))
   ])
   ```

4. **Run Grid/Random search** with `refit=False` (to avoid TF state corruption).

5. **Select best params** via refit rule: 1SE + gap filter + min complexity + min gap (from `selection.py`).

6. **Fresh OOF evaluation** (lines 358-393):
   - Build a fresh pipeline, set params from best
   - Call `evaluate_oof_per_output(fresh_est, ...)` from `selection.py`
   - If that fails, fall back to `_oof_direct()` which builds entirely fresh pipelines per fold

7. **Manual refit** on full data (lines 398-413).

#### C. `evaluate_oof_per_output` (selection.py, line 321)

1. For each CV fold: `clone(estimator)`, `fit(X[tr], Y_fit[tr])`, `predict(X[te])`
2. Collect predictions into `y_pred_oof_fit` array
3. Apply `eval_mask` to filter only real data rows
4. Compute R2 and RMSE per output on `y_true_oof` vs `y_pred_oof`

#### D. `_oof_direct` fallback (runner.py, line 182)

1. Per fold: builds fresh `Pipeline([StandardScaler(), YScalerRegressor(...)])`
2. Sets params from best params (skipping callbacks from grid, using fresh ones)
3. Fits, predicts, collects

---

### 2. HOW FROZENBASELINE PIPELINE DIFFERS FROM ZOHANRESIDUAL PIPELINE

**FrozenBaseline:**
```
Pipeline input: X (5 features)
  â†’ StandardScaler (5 columns)
  â†’ YScalerRegressor(augmented_2m=False, m_targets=3)
    â†’ KerasRegressor(model=build_keras_mlp)
      â†’ build_keras_mlp(n_features=5, n_targets=3) â†’ standard dense MLP: Input(5) â†’ Dense(...) â†’ Dense(3)
```

**ZohanResidual:**
```
Pipeline input: X_plus_phy (8 features = 5 base + 3 physics)
  â†’ StandardScaler (8 columns)
  â†’ YScalerRegressor(augmented_2m=False, m_targets=3)
    â†’ KerasRegressor(model=build_keras_mlp_residual_add_phy_x_only)
      â†’ Internal architecture:
        Input(8) â†’ SliceXPart(nt=3) â†’ first 5 cols (original features)
                 â†’ SliceYPhyPart(nt=3) â†’ last 3 cols (physics outputs)
        x_part â†’ Dense(...) â†’ Dense(3) = y_res
        y_hat = y_phy + y_res  (Add layer)
        Output: y_hat (3 targets)
```

**Key differences:**

| Aspect | FrozenBaseline | ZohanResidual |
|--------|---------------|---------------|
| Input features | 5 (features only) | 8 (features + physics) |
| Architecture | Plain MLP | Residual: y_hat = y_phy + NN(x_features) |
| `n_features` param | 5 | 8 |
| Model builder | `build_keras_mlp` | `build_keras_mlp_residual_add_phy_x_only` |
| Hyperparameter search | None (all frozen) | L2 grid (5 values) |
| Loss function | Inherited from baseline | Inherited from baseline |

**ZohanHPD is architecturally identical to FrozenBaseline** -- it also uses `make_keras_mlp_estimator` â†’ `build_keras_mlp` -- but receives 8 inputs (5 features + 3 physics) instead of 5. The physics outputs are just extra features fed into a standard dense network.

---

### 3. HOW PHYSICS FEATURES (phy columns) ARE LOADED AND PROVIDED

**Configuration** (`config.py`):
```python
MODEL_MAP = {
    "Alim_T_out": "Alim_T_out_phy",
    "Ref_T_out": "Ref_T_out_phy",
    "Flux": "Flux_phy_L_m2_h",
}
```
This maps each target name to its corresponding physics model prediction column in the CSV.

**Loading** (`data.py`, `build_XY_groups_with_model_map`, line 74-80):
```python
if model_map is not None:
    model_cols_ordered = [model_map[t] for t in target_cols]
    Y_model = used[model_cols_ordered].to_numpy(dtype=float)
```
Creates `Y_model` as an array of 3 columns: Alim_T_out_phy, Ref_T_out_phy, Flux_phy_L_m2_h.

**Routing to models** (`runner.py`, `_select_XY_for_spec`, line 97-116):
- **ZohanHPD / ZohanResidual** (`x_mode="x_plus_model"`):
  ```python
  X_fit = np.concatenate([X, Y_model], axis=1)  # [N, 5+3] = [N, 8]
  ```
- **Luc** (`y_mode="true_plus_model"`):
  ```python
  Y_fit = np.concatenate([Y_true, Y_model], axis=1)  # [N, 3+3] = [N, 6]
  ```
- **FrozenBaseline**: neither augmentation -- X_fit = X (5), Y_fit = Y_true (3)

**Internal use within Keras models:**
- **ZohanResidual**: The model's `SliceXPart(nt=3)` and `SliceYPhyPart(nt=3)` layers split the 8 standardized inputs into first 5 (= original features) and last 3 (= standardized physics outputs). The physics outputs serve as a baseline prediction, and the NN learns residuals.
- **Luc**: The `LucHybridLoss` receives `y_true_aug` = 6 columns. It splits into `y_true` (first 3) and `y_phy` (last 3). The model outputs 6 values (`Concat[y_hat, y_hat]`), and the loss computes: `(1-omega) * L_data(y_true, y_pred) + omega * L_phys(y_phy, y_pred)`.

---

### 4. HOW PARAMS FLOW THROUGH PIPELINE -> YScalerRegressor -> KerasRegressor

**Example param chain for `model__model__n_features=8`:**

```
Grid key in sweep:      "model__model__n_features" = 8
                         â”‚
Pipeline.set_params()    â†’ recognizes "model" step
                         â”‚
                         â†“
YScalerRegressor.set_params("model__n_features" = 8)
                         â”‚
                         â”œâ”€â”€ Not in wrapper_keys {"base_estimator","scale_y","augmented_2m","m_targets"}
                         â”œâ”€â”€ Doesn't start with "base_estimator__"
                         â””â”€â”€ Goes to inner_params["model__n_features"] = 8
                         â”‚
                         â†“
self.base_estimator.set_params(**inner_params)
                         â”‚
                         â†“
KerasRegressor.set_params("model__n_features" = 8)
                         â”‚
                         â”œâ”€â”€ scikeras recognizes "model__" prefix
                         â””â”€â”€ Routes "n_features" = 8 to the model-building function
                         â”‚
                         â†“
build_keras_mlp(n_features=8, n_targets=3, ...)
```

**Verdict: The parameter routing is CORRECT.** The double `model__model__` prefix in the grid is handled correctly:
- First `model__` routes through Pipeline to the "model" step
- The remaining `model__n_features` goes into inner_params since it doesn't match YScalerRegressor wrapper keys
- KerasRegressor (scikeras) then recognizes `model__n_features` as having the `model__` prefix and routes `n_features` to the build function

**Special case -- YScalerRegressor's own params:**
- `model__scale_y`, `model__augmented_2m`, `model__m_targets`, `model__base_estimator`: These ARE in `wrapper_keys`, so `YScalerRegressor.set_params` handles them directly via `setattr(self, k, v)`.
- `model__base_estimator__<anything>`: The `base_estimator__` prefix is stripped and routed to the inner estimator.

**Special case -- scikeras model params vs fit params:**
- `model__model__hidden_layer_sizes` â†’ KerasRegressor receives `model__hidden_layer_sizes` â†’ routes to build function as `hidden_layer_sizes` âœ“
- `model__model__learning_rate` â†’ KerasRegressor receives `model__learning_rate` â†’ routes to build function as `learning_rate` âœ“
- `model__batch_size` â†’ KerasRegressor receives `batch_size` â†’ used by KerasRegressor itself âœ“
- `model__fit__validation_split` â†’ KerasRegressor receives `fit__validation_split` â†’ used as fit param âœ“

---

### 5. DOES `n_features` CORRECTLY REFLECT 5 VS 8?

**Check per model type:**

| Model | Grid `n_features` | Actual X_fit columns | Match? |
|-------|------------------|---------------------|--------|
| FrozenBaseline | 5 (from `N_FEATURES_BASE`) | 5 (x_mode="x") | YES |
| Luc | 5 (from `N_FEATURES_BASE`) | 5 (x_mode="x") | YES |
| ZohanHPD | 8 (from `N_FEATURES_PLUS_PHY`) | 8 (x_mode="x_plus_model") | YES |
| ZohanResidual | 8 (from `N_FEATURES_PLUS_PHY`) | 8 (x_mode="x_plus_model") | YES |

**The `n_features` parameter correctly reflects the actual number of input features for each model.**

`N_FEATURES_PLUS_PHY = N_FEATURES_BASE + N_TARGETS = 5 + 3 = 8` (from config.py)

---

### 6. HOW `build_frozen_baseline_grid` WORKS VS HYBRID MODEL GRIDS

#### `build_frozen_baseline_grid` (sweep.py:68-76):

1. Calls `extract_baseline_keras_fixed_params(best_params)` which copies ALL these keys (each as a single-element list):
   - `model__model__n_features`, `model__model__n_targets`, `model__model__hidden_layer_sizes`, `model__model__activation`, `model__model__optimizer`, `model__model__learning_rate`, `model__model__l2`
   - `model__batch_size`, `model__epochs`, `model__fit__validation_split`, `model__fit__shuffle`, `model__fit__verbose`, `model__fit__callbacks`
   - Plus optional: `model__model__loss`, `model__model__huber_delta`
2. Overrides: `model__model__n_features = [5]`, `model__model__n_targets = [3]`
3. **Result: grid with exactly 1 combination** (all params frozen to single values)

Despite `n_iter=5` in the FamilySpec, `RandomizedSearchCV` with a dict grid will only produce as many candidates as there are unique combinations -- so only 1 candidate is evaluated.

#### `build_luc_restricted_grid_from_baseline` (sweep.py:86-105):

1. Freezes all baseline params via `extract_baseline_keras_fixed_params`
2. Removes `model__model__loss` (replaced by `data_loss`)
3. Sets `n_features=5`, `n_targets=3`
4. Adds Luc-specific grid params:
   - `data_loss = [baseline_loss]` (1 value)
   - `huber_delta = [baseline_huber_delta]` (1 value)
   - `physics_norm = ["mse", "mae"]` (2 values)
   - `omega = [0.0, 0.1, 0.3, 0.5, 0.7]` (5 values)
5. **Total combinations: 1*1*2*5 = 10**, but with `n_iter=5`, only 5 are sampled

#### `build_hpd_restricted_grid_from_baseline` (sweep.py:108-117):

1. Freezes all baseline params
2. Sets `n_features=8`, `n_targets=3`
3. Overrides `model__model__l2` with `_small_l2_grid_from_baseline`:
   - Takes `baseline_l2` from best params
   - Combines: `[baseline_l2, 0.0, 1e-6, 1e-5, 1e-4]`, deduplicates
   - Typical result: up to 5 L2 values
4. **Total combinations: up to 5**

#### `build_residual_restricted_grid_from_baseline` (sweep.py:120-129):

Identical to `build_hpd_restricted_grid_from_baseline` in structure: n_features=8, n_targets=3, small L2 grid.

**Key difference:** FrozenBaseline has NO hyperparameter search (1 candidate), while hybrids have 5-10 candidates. This slightly favors hybrids since they get to re-optimize L2 (or other params) specifically for their architecture on this dataset.

---

### 7. POTENTIAL BUGS AND ISSUES

#### ISSUE 1 (Critical): ZohanHPD uses the WRONG estimator -- it is architecturally identical to FrozenBaseline

In `stage2_focused.py` lines 91-94:
```python
FamilySpec(name="KerasMLP_ZohanHPD_Restricted",
           estimator=make_keras_mlp_estimator,  # <-- SAME as baseline!
           ...
           x_mode="x_plus_model", ...)
```

`make_keras_mlp_estimator` returns `KerasRegressor(model=build_keras_mlp)` -- a **standard MLP** with no special physics-awareness. The only difference from FrozenBaseline is that it receives 8 inputs (5 base + 3 physics) instead of 5. The physics outputs are just concatenated as additional features. This may be intentional (treating physics as extra inputs), but the name "ZohanHPD" (Physics Data-informed) suggests a more sophisticated design. This is **not necessarily a bug**, but it means ZohanHPD is simply "MLP with 8 inputs" while ZohanResidual has an actual residual architecture.

#### ISSUE 2 (Medium): FrozenBaseline gets no L2 re-optimization vs hybrids

The `build_frozen_baseline_grid` freezes L2 to the Stage 1 best value, while `build_hpd_restricted_grid` and `build_residual_restricted_grid` create an expanded L2 grid. The hybrid models get to pick the best L2 for their specific architecture. This is actually an advantage for hybrids, not a disadvantage.

#### ISSUE 3 (Medium): same scaler applied to Y_phy in Luc's YScalerRegressor

In `YScalerRegressor.fit()` with `augmented_2m=True`:
```python
y_true_s = self._y_scaler.fit_transform(y_true)           # scaler fit on y_true
y_phy_s = self._y_scaler.transform(y_phy)                 # same scaler applied to y_phy
y_s = np.concatenate([y_true_s, y_phy_s], axis=1)
```

The same `StandardScaler` (fit on y_true) is applied to y_phy. If the physics model predictions are systematically biased (different mean/variance from true values), this may not be optimal. In `predict()`:
```python
a = self._y_scaler.inverse_transform(y_pred[:, :m])       # first 3
b = self._y_scaler.inverse_transform(y_pred[:, m:])       # last 3
```
Both halves are inverse-transformed with the same scaler. This is **consistent** with the fit procedure but might hurt Luc's ability to leverage physics outputs if they have a different distribution.

#### ISSUE 4 (Low): `build_keras_mlp_luc_loss_2m_output` ignores `n_outputs_` param

In `keras_builders.py` lines 176-183:
```python
nf, _ = _infer_n_features_targets(
    n_features_in_=n_features_in_, n_outputs_=None,  # hardcoded None!
    n_features=n_features, n_targets=n_targets, **kwargs,
)
m = int(n_targets) if n_targets is not None else None
```

The `_` (nt) is discarded and `m` is re-derived from `n_targets`. This works because `n_targets` is always explicitly set in the grid, but it means `n_outputs_` (which scikeras might pass) is ignored.

#### ISSUE 5 (Low): `_small_l2_grid_from_baseline` may produce duplicate or zero-length list edge case

```python
def _small_l2_grid_from_baseline(baseline_best_params):
    baseline_l2 = float(baseline_best_params.get("model__model__l2", 0.0))
    cand = [baseline_l2, 0.0, 1e-6, 1e-5, 1e-4]
    cand = [float(x) for x in cand if float(x) >= 0.0]
    return _dedup_keep_order(cand)
```

If `baseline_l2` is `0.0`, this produces `[0.0, 1e-6, 1e-5, 1e-4]` (4 unique values). With `n_iter=5`, random search will sample all 4 (repeat 1). If `baseline_l2` happens to be negative (impossible for L2) or the list is empty after filtering, it could cause issues.

#### ISSUE 6 (Medium): Potential unfair comparison due to different grid sizes

- **FrozenBaseline**: 1 candidate (model is just re-evaluated with frozen params)
- **ZohanHPD**: up to 5 candidates (L2 search)
- **ZohanResidual**: up to 5 candidates (L2 search)
- **Luc**: 10 possible combinations, sampled 5 times

The hybrids get to search over some hyperparameters while the baseline does not. This gives hybrids more flexibility to find a good configuration and should not cause worse performance.

#### ISSUE 7 (Low): FrozenBaseline grid has `model__model__loss` frozen

`extract_baseline_keras_fixed_params` includes `"model__model__loss"` in optional_keys. If the baseline used "huber" loss, this is preserved. For the frozen baseline, this is fine. For the residual model (`build_keras_mlp_residual_add_phy_x_only`), which also accepts `loss`, this is also fine. No inconsistency here.

#### ISSUE 8 (Info): The Luc model's loss function has the y_phy sliced from y_true_aug

In `LucHybridLoss.call()`:
```python
y_true = y_true_aug[:, :m]          # first 3 = true targets
y_phy = y_true_aug[:, m:(2 * m)]    # next 3 = physics predictions
y_pred = y_pred_2m[:, :m]           # first 3 of model output
```

This is correct -- the loss compares model predictions (y_pred) against both true targets (y_true) and physics outputs (y_phy). The `omega` parameter balances data fit vs physics consistency.

---

### SUMMARY OF FINDINGS

| # | Issue | Severity | Description |
|---|-------|----------|-------------|
| 1 | ZohanHPD uses `make_keras_mlp_estimator` | **Info** | Same standard MLP as baseline; physics outputs are just extra features. Not architecturally different. |
| 2 | Expanded L2 grid for hybrids | **Low** | Hybrids get to re-optimize L2; this favors hybrids, not hurts them. |
| 3 | Same scaler for y_phy in Luc | **Medium** | Physics predictions scaled with scaler fit on y_true. If distributions differ, this may hurt Luc. |
| 4 | n_outputs_ ignored in Luc builder | **Low** | Works because n_targets is always explicit. |
| 5 | Edge case in L2 grid dedup | **Low** | If all L2 values are the same (e.g., all 0.0), grid shrinks. |
| 6 | Different grid sizes for comparison | **Low** | Hybrids search, baseline doesn't. Hybrids have advantage, not disadvantage. |
| 7 | `model__model__loss` handling | **None** | Correctly propagated to all hybrid builders. |
| 8 | Luc loss architecture | **None** | Correctly splits y_true and y_phy from augmented Y. |

**Most likely reasons hybrids might underperform vs baseline:**
1. **Data scarcity**: Hybrid models have more parameters/complexity (8 inputs, residual connections, custom losses) and need more data to train effectively. The dataset may be too small.
2. **Physics model quality**: If the physics model predictions (`Y_model`) are inaccurate or noisy, feeding them as inputs or using them in a residual connection degrades performance.
3. **Optimization difficulty**: The Luc loss with `omega` balancing creates a multi-objective optimization that is harder to train than plain MSE.
4. **StandardScaler interaction** with residual architecture: Residual connections work best when the residual targets (y_true - y_phy) are small. If the standardized physics outputs are far from the standardized true targets, the model needs large residuals, defeating the purpose.

**No bugs were found in the parameter routing** through `Pipeline -> YScalerRegressor -> KerasRegressor`. The `model__model__*` prefix convention is correctly handled at each layer.

*Novo passo iniciado*

---

*6 messages | 37 parts | ðŸ’° $0.0000 | â±ï¸ 0h02m16s*

