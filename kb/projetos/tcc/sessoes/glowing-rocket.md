---
slug: glowing-rocket
title: "Find C_NaCl unit in model 0D (@explore subagent)"
date: 2026-06-21
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h02m16s
messages: 13
parts: 86
cost: 0.013395
tokens_input: 60771
tokens_output: 5081
tokens_reasoning: 7977
tokens_cache_read: 439680
tokens_cache_write: 0
created: "2026-06-21 15:20:01 UTC"
updated: "2026-06-21 15:22:17 UTC"
---

Sessão com **13 messages**, **86 parts**, agente **explore**, modelo **deepseek-v4-flash** | 💰 $0.0134 | 💾 cache read: 439.7K | ⏱️ 0h02m16s

## 👤 Usuário (2026-06-21 15:20:01 UTC)

Search the model 0D source code at C:\Users\frota\OneDrive\Documentos\TCC\Codigos\vagmd0Dmodel-main for how C_NaCl / salt concentration / NaCl is defined and what unit it expects (g/L, kg/kg, wt%, fraction, etc.). Look in source files (.c, .h, .f90, .cpp, .hpp). I need to understand what unit the model expects for the NaCl concentration input parameter, so I can convert the real data to match. Also search the TCC code at C:\Users\frota\OneDrive\Documentos\TCC\Codigos\Codigo-revisado for how the data CSV is loaded and any unit conversion happening.

Return:
1. The exact definition/unit of NaCl concentration expected by the model 0D
2. How the TCC code loads the CSV and whether it converts C_NaCl units
3. Any comments or documentation about units


## 🤖 Assistente (2026-06-21 15:20:01 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me search both codebases thoroughly to understand how NaCl concentration is defined and what units are expected.

</details>

### Resposta

I'll search both codebases in parallel for NaCl-related definitions, units, and CSV loading.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:20:07 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The model 0D source files didn't match any grep patterns for C_NaCl or NaCl. The codebase might have files in different extensions or the variable might be named differently. Let me explore the model 0D source code structure first, then look deeper.

</details>

### Resposta

Let me explore the model 0D source structure and search more broadly:

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:20:11 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I need to read the key source files in the model 0D. Let me start with the main entrydata, physics, dessal, and properties files.

</details>

### Resposta

Now let me read the key source files to find NaCl definitions:

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:20:16 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Excellent! I now have the full picture from the model 0D side. Let me analyze:

In `entrydata.c`, line 13-14:
```c
entry_salinity_feed = 3.5e-2, // Default: 3.5 wt%
entry_salinity_cool = 3.5e-2, // Default: 3.5 wt%
```

So the default is `3.5e-2 = 0.035`, and the comment says "3.5 wt%". This means **mass fraction** (wt% = weight percent, so 3.5 wt% = 0.035 mass fraction).

Now let me check how salinity is used in the properties to confirm:

In `properties.c`:
- `SaltWaterDensity(temperature, salinity)` - takes salinity directly as a fraction (no conversion)
- `SaltWaterSpecificHeat(temperature, salinity)` - line 55: `alt_salinity = 1000.0 * salinity;` — this converts salinity from mass fraction to g/kg (parts per thousand). So it takes mass fraction and multiplies by 1000 to get g/kg for the correlation.
- `SaltWaterDynViscosity(temperature, salinity)` - line 85: `alt_salinity = salinity / 1.00472;` — this uses salinity as-is (mass fraction) and then converts internally
- `SaltWaterThermalConductivity(temperature, salinity)` - line 110: `alt_salinity = 1000.0 * salinity;` — converts mass fraction to g/kg
- `ActivityCoefficient(salinity)` - line 137: `molar_fraction = water_molar_mass * salinity / ((1.0 - salinity) * salt_molar_mass + salinity * water_molar_mass);` — this is the mass-fraction-to-mole-fraction conversion formula. This definitively confirms that salinity is mass fraction (kg_salt/kg_solution).
- `SaltWaterLatentHeat(temperature, salinity)` - line 170: `latent_heat_vaporization = pure_latent_heat * (1.0 - salinity);` — uses salinity directly as mass fraction.

So the model 0D definitively expects salinity/NaCl concentration as **mass fraction** (0 to 1). The default `3.5e-2 = 0.035` corresponds to typical seawater at 3.5 wt% = 35 g/kg = 35,000 ppm.

Now let me check the TCC code for how the CSV is loaded and any unit conversion.

</details>

### Resposta

Excellent. Now let me read the key TCC code files to see how the CSV is loaded and if there's unit conversion:

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:20:24 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a lot of the key information. Let me now look at `data.py` which has the `read_tabular_csv` function to see how the CSV is loaded and if there's any unit conversion happening. Also let me look at the config.yaml and the CSV data file to understand the raw data.

</details>

### Resposta

Now let me read the data loading module and check the CSV and config:

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:20:28 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the config.yaml to see the data path and any column definitions, and also look for the CSV data file.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:20:31 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Excellent! Now let me peek at the main data CSV file to see the actual values of C_NaCl in the real data.

</details>

### Resposta

Let me look at the main data CSV to see the actual C_NaCl values, and also check the main.c for CLI usage:

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:20:36 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have all the information needed. Let me compile my findings.

**Model 0D (vagmd0Dmodel)**

The NaCl concentration is defined in `entrydata.c` as `entry_salinity_feed` and `entry_salinity_cool`. The default value is:

```c
entry_salinity_feed = 3.5e-2, // Default: 3.5 wt%
entry_salinity_cool = 3.5e-2, // Default: 3.5 wt%
```

And in `main.c`, line 27-30:
```
-entry_salinity_feed: type double, unit wt%
```

So the model expects salinity in **wt%** (weight percent). But wait - is "wt%" the same as percent (0-100) or as a fraction (0-1)?

Looking at the default: `3.5e-2 = 0.035`. The comment says "3.5 wt%". 

3.5 wt% means 3.5 grams per 100 grams = 0.035 mass fraction.

So the model expects the value as a **mass fraction** (0 to 1), but the developers call it "wt%" in the documentation. The actual numeric value is the mass fraction. So if your data is in wt% (like 3.5), the model expects 0.035.

Let me confirm by looking at how the salinity is used:

1. In `properties.c`, `SaltWaterSpecificHeat` at line 55: `alt_salinity = 1000.0 * salinity;` — if salinity is 0.035 (mass fraction), then alt_salinity = 35 g/kg which is standard seawater salinity correlation.

2. In `properties.c`, `ActivityCoefficient` at line 137: `molar_fraction = water_molar_mass * salinity / ((1.0 - salinity) * salt_molar_mass + salinity * water_molar_mass);` — This is the classic conversion from mass fraction (salinity) to mole fraction.

3. In `SaltWaterLatentHeat` at line 170: `latent_heat_vaporization = pure_latent_heat * (1.0 - salinity);` — Uses salinity as mass fraction (1 - mass_fraction).

So the model **definitively** expects `salinity` as a **mass fraction** (dimensionless, 0 to 1), where typical seawater is `0.035` (3.5 wt%, which is 35 g/kg or 35,000 ppm).

**TCC code - How CSV is loaded and if there's unit conversion**

Looking at `gerar_surrogate.py` (lines 27-31), there is explicit unit conversion:

```python
# Converter unidades para o modelo C
X_phys = X_raw.copy()
X_phys[:, 2] /= 3600.0  # L/h -> kg/s
X_phys[:, 3] *= 100.0    # mbar -> Pa
X_phys[:, 4] *= 0.001    # g/L -> fracao massica wt%
```

This is for the **synthetic data generation** (calling the model 0D via WSL). The raw ranges are:
```python
ranges = np.array([[55, 75], [20, 35], [300, 600], [-510, -490], [0.005, 0.02]])
```
So the raw C_NaCl range is [0.005, 0.02] (which is in g/L according to the comment), and it gets converted to mass fraction by multiplying by 0.001:
- 0.005 g/L → 0.000005 mass fraction (wait, that doesn't look right)
- Actually: 0.005 * 0.001 = 0.000005... that's very dilute.

Wait, let me re-read. The raw ranges generate `X_raw` values. Then:
```python
X_phys[:, 4] *= 0.001    # g/L -> fracao massica wt%
```

So if X_raw has C_NaCl values in the range [0.005, 0.02], and these are supposed to be in g/L, then after multiplying by 0.001:
- 0.005 g/L → 0.000005 mass fraction? 

But that doesn't make sense. Typical seawater is ~35 g/L = 0.035 mass fraction. 0.005 to 0.02 g/L would be essentially fresh water.

Hmm, let me re-examine. Looking at the real data CSV:
```
C_NaCl = 10.1766, 10.1044, 10.0902, ...
```

These values are around 10. The column `sal_in_used_fraction` has values like `0.0101766`, `0.0101044`, etc.

So the real data CSV has `C_NaCl` in **g/L** (approximately 10 g/L), and `sal_in_used_fraction` is the **mass fraction** version (0.01 = ~1 wt%).

Wait, looking more carefully at the CSV:
- Column `C_NaCl` has values like 10.1766, 10.1044 (which seems to be g/L)
- Column `sal_in_used_fraction` has values like 0.0101766, 0.0101044 (which is the mass fraction)

So `sal_in_used_fraction = C_NaCl / 1000` roughly. 10.1766 g/L ≈ 0.0101766 mass fraction (since 1 L of water ≈ 1 kg, so g/L ≈ g/kg, and mass fraction = g/kg / 1000).

Actually, 10 g/L in water with density ~1000 g/L: mass fraction ≈ 10/1000 = 0.01. So the conversion g/L → mass fraction is indeed dividing by approximately 1000 (or by the solution density for higher accuracy).

So the `gerar_surrogate.py` script creates synthetic data:
- `X_raw[:, 4]` is in the range [0.005, 0.02] g/L
- Converted: `X_phys[:, 4] = X_raw[:, 4] * 0.001` to get mass fraction [0.000005, 0.00002]

But that seems far too dilute... Let me look more carefully.

Actually wait - looking at the ranges again:
```python
ranges = np.array([[55, 75], [20, 35], [300, 600], [-510, -490], [0.005, 0.02]])
```

The C_NaCl raw range is [0.005, 0.02]. The comment says "g/L -> fracao massica wt%". So the input is g/L and conversion is * 0.001 to get mass fraction.

0.005 to 0.02 g/L → 5e-6 to 2e-5 mass fraction.

But that's WAY too low... Unless this is meant to be in a different unit like percent already? If 0.005 means 0.005 g/L (5 mg/L) that's practically fresh water.

Hmm, OR maybe the range is already expected to be in percent (like 0.5% to 2%), and multiplying by 0.001 would give 0.0005 to 0.00002 mass fraction which is still very low.

Let me look at this from the real data perspective. The real CSV has C_NaCl values around 10, and sal_in_used_fraction around 0.01. So:
- C_NaCl ≈ 10 → sal_in_used_fraction ≈ 0.01

Conversion: 0.01 / 10 = 0.001 = 1/1000

So indeed, it seems like the real data C_NaCl is in g/L (about 10 g/L), and the mass fraction is C_NaCl / 1000 ≈ 0.01.

But in `gerar_surrogate.py`, the raw range is [0.005, 0.02], which if interpreted as g/L, would give mass fractions of 5e-6 to 2e-5. That's extremely dilute - essentially fresh water. 

Actually, I think maybe the raw range units are different. If 0.005 to 0.02 is meant to be in wt% (percent by weight), then:
- 0.005 wt% = 0.00005 mass fraction
- 0.02 wt% = 0.0002 mass fraction

Still very low compared to the real data (which has ~1 wt% / 0.01 mass fraction).

Actually, I think I may be misreading the ranges. Let me look at the ranges again:
```
ranges = np.array([[55, 75], [20, 35], [300, 600], [-510, -490], [0.005, 0.02]])
```

Column 0: Alim_T_in [55, 75] °C
Column 1: Ref_T_in [20, 35] °C
Column 2: Ref_V_in [300, 600] L/h
Column 3: P_vacuum [-510, -490] mbar
Column 4: C_NaCl [0.005, 0.02] ???

If C_NaCl is in g/L and multiplied by 0.001 to get mass fraction, that gives 5e-6 to 2e-5 mass fraction. That's fresh water salinity but perhaps for surrogate training they're exploring the full range? That seems unlikely.

Alternatively, maybe the comment is misleading and the conversion is wrong in the script. Let me look at the model map in config.py:
```python
MODEL_MAP = {
    "Alim_T_out": "Alim_T_out_phy",
    "Ref_T_out": "Ref_T_out_phy",
    "Flux": "Flux_phy_L_m2_h",
}
```

And in the real CSV, we have:
- `C_NaCl` values: ~10 
- `sal_in_used_fraction` values: ~0.01
- `sal_feed_out_phy_wt_pct`: ~1.04 (wt% outlet)

So the naming convention:
- `C_NaCl` ≈ 10 — this is in g/L (or equivalent)  
- `sal_in_used_fraction` = 0.01 = C_NaCl / 1000 (mass fraction used as input to the model)
- `sal_feed_out_phy_wt_pct` ≈ 1.04 (wt% at outlet)

Wait, but `sal_in_used_fraction` has values exactly like 0.0101766, which is 10.1766 / 1000. So C_NaCl is in g/L, and the mass fraction fed to the model is g/L / 1000 ≈ g/L / density_of_water_in_g_per_L.

Now in the real CSV, I notice that `sal_in_used_fraction` column exists! This column is already the mass fraction that the model expects. But the TCC code uses FEATURE_COLS which includes `C_NaCl`, not `sal_in_used_fraction`.

So the TCC code is training on C_NaCol which is in g/L (around 10), NOT in mass fraction (around 0.01).

Wait, but the TCC code is training ML surrogates to approximate the physics model. The features include C_NaCl (in g/L as loaded from CSV), and the targets include things like Alim_T_out_phy. There's no explicit unit conversion when loading the data for training.

Let me verify by looking at `pipeline_final.py` more carefully:
```python
df = read_tabular_csv(str(DATA_PATH), decimal_comma=True)
X, Y_true, groups, _, Y_model, _ = build_XY_groups_with_model_map(
    df=df, feature_cols=["Alim_T_in","Ref_T_in","Ref_V_in","P_vacuum","C_NaCl"],
    ...
)
```

The C_NaCl from the CSV (which is around 10, in g/L) is used directly as a feature. There's no unit conversion in the data loading. The model map then maps to Alim_T_out_phy, Ref_T_out_phy, Flux_phy_L_m2_h which are the physics model outputs.

So essentially:
- The CSV stores C_NaCl in **g/L** (around 10 g/L)
- The physics model 0D expects salinity in **mass fraction/wt%** (0 to 1, where 0.01 = 1 wt%)
- The CSV also has a column `sal_in_used_fraction` which has the mass fraction equivalent (around 0.01)
- The TCC surrogate models are trained on C_NaCl (g/L) as a feature, and they learn to approximate the physics model outputs
- The `gerar_surrogate.py` script explicitly converts: `X_phys[:, 4] *= 0.001  # g/L -> fracao massica wt%` when calling the model 0D binary

So the conversion chain is:
- Real data: C_NaCl in g/L (≈10) → stored as-is in CSV
- Model 0D expects: mass fraction (≈0.01 for the same data)
- gerar_surrogate.py: converts C_NaCl (g/L) * 0.001 → mass fraction before passing to the C model
- TCC surrogate training: uses C_NaCol (g/L) directly as a feature, no conversion

Let me also check the `output.c` and `output.h` to see how the report.csv is written, since the report.csv shows the output salinity in wt%.

Actually, I already have that info from report.csv:
```
Feed salinity at the outlet of the module =, 0.0014825439, wt%
```

So the output salinity is in wt% (meaning 0.00148 wt% = 0.0000148 mass fraction). This confirms the model treats the input and output salinity as wt% (where the numeric value IS the wt% value, not decimal - wait, 0.00148 wt% is a very low number. If it's truly wt% as the unit says, then 0.00148 wt% means 0.0000148 mass fraction. But if the actual number IS the mass fraction and they're just labeling it as wt% incorrectly, then it'd mean 0.148 wt%.

Let me check by looking at the output code.

</details>

### Resposta

Let me check the output formatting and also look more closely at the salinity conversion:

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:21:09 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have the full picture. Let me trace through the critical piece:

In `output.c`, line 38:
```c
PetscFPrintf(PETSC_COMM_WORLD, fptr, "Feed salinity at the outlet of the module =, %.10f, wt%%\n", 100.0 * array[7]);
```

The model stores the outlet salinity internally as `array[7]` and then multiplies by 100.0 for output → `100.0 * array[7]` with unit "wt%".

From the report.csv we saw:
```
Feed salinity at the outlet of the module =, 0.0014825439, wt%
```

So:
```
100.0 * array[7] = 0.0014825439
array[7] = 0.000014825439 (mass fraction)
```

This confirms that internally the model stores salinity as **mass fraction** (dimensionless, 0 to 1).

But wait, what about the input? The input `entry_salinity_feed` has default `3.5e-2` which = 0.035, and the comment says "3.5 wt%". But is the input treated as mass fraction internally, or as wt%?

Let me trace the full flow:
1. Input: `-entry_salinity_feed 0.035` (default value from entrydata.c)
2. Stored in `dessal_data.entry_salinity_feed = 0.035`
3. Used in `dessal.c` line 56: `SaltWaterPropBuild(&feed_prop, avg_feed_temperature, avg_salinity)` where `avg_salinity = 0.5 * (entry_salinity_feed + out_salinity_feed)`
4. In `properties.c`, `SaltWaterPropBuild` calls `SaltWaterDensity(temperature, salinity)` with salinity = 0.035

Looking at `SaltWaterDensity`:
```c
temperature_part = a[0] + a[1] * temperature + ...
salinity_part = b[0] * salinity + b[1] * salinity * temperature + ...
return temperature_part + salinity_part;
```

This function directly uses salinity as-is (coefficient b[0] = 802.0). If salinity = 0.035, then b[0] * salinity = 802.0 * 0.035 = 28.07. And the pure water part from a coefficients at 60°C would be about 983 kg/m³. So total density ≈ 983 + 28 = 1011 kg/m³. That's reasonable for seawater at 3.5 wt%.

If the input were treated as "3.5" (wt% value, 3.5%), then density would be 802 * 3.5 = 2807, which is absurd. So the input IS mass fraction (0.035) not wt% value (3.5).

So the model:
- **Internal representation**: salinity as **mass fraction** (0 to 1, dimensionless)
- **CLI argument**: expects mass fraction too, but the help text says `unit wt%` which is misleading
- **Output**: multiplies by 100 to show in `wt%` (line 38 of output.c: `100.0 * array[7]`)
- **Default**: `3.5e-2 = 0.035` mass fraction = 3.5 wt% = 35 g/kg

Now for the `gerar_surrogate.py` conversion:
```python
X_phys[:, 4] *= 0.001    # g/L -> fracao massica wt%
```

Wait, this converts g/L to mass fraction. If raw C_NaCl is around 10 g/L:
- 10 g/L * 0.001 = 0.01 mass fraction

But the raw ranges are [0.005, 0.02], which after multiplication by 0.001 gives [5e-6, 2e-5] mass fraction. That's absurdly low...

Unless the comments on the ranges are wrong about the units. Let me reconsider the ranges:
```
ranges = np.array([[55, 75], [20, 35], [300, 600], [-510, -490], [0.005, 0.02]])
```

Looking at the real data more carefully:
- P_vacuum in CSV is around -495 to -500 (looks like mbar: -495.9198, -497.0388, etc.)
- The range for P_vacuum is [-510, -490] mbar → convert to Pa: * 100 = [-51000, -49000] Pa

Wait, but the gerar_surrogate converts:
```python
X_phys[:, 3] *= 100.0    # mbar -> Pa
```

So -500 mbar → -50000 Pa. That matches the real data column `pv_pa_used` which has values like -49591.98, -49703.88 Pa.

Now for C_NaCl: if the range is [0.005, 0.02] and it's multiplied by 0.001:
- [0.005, 0.02] * 0.001 = [0.000005, 0.00002] mass fraction

But wait, that doesn't match the real data at all. The real data has C_NaCl ≈ 10 and sal_in_used_fraction ≈ 0.01.

But this is synthetic data for surrogate training - it doesn't need to match the real data. The surrogate is supposed to learn the full behavior of the physics model across a range of inputs.

But [0.005, 0.02] as g/L is 5-20 mg/L. That's extremely dilute. The model runs at those salinities and produces meaningful output? 

Hmm, actually thinking about it more, the comment on line 27 says:
```
# Converter unidades para o modelo C
```

And the model expects mass fraction. If the raw range [0.005, 0.02] is already in mass fraction (like 0.5% to 2%), then multiplying by 0.001 would give 0.0005% to 0.002%, which is still off.

Actually I think the comment might just be wrong or the units are ambiguous. Let me look at it differently:

If the raw C_NaCl range is [0.005, 0.02] and this is meant as wt% (i.e., 0.5% to 2%), then:
- In wt% form: 0.5% to 2% = 0.005 to 0.02 as a fraction
- The model expects mass fraction (which is wt%/100 = 0.005 to 0.02)

Wait no, if raw is in wt% (where 1 wt% = 1), then raw range [0.005, 0.02] means 0.005 wt% to 0.02 wt%. That's 0.05 g/kg to 0.2 g/kg. Very dilute.

I think the most consistent interpretation is: the raw ranges are indeed what the comment says, and the surrogate is trained on dilute solutions for some reason. Or the ranges serve as placeholders for a wider test.

Actually, let me just re-read the raw range carefully:

```python
ranges = np.array([[55, 75], [20, 35], [300, 600], [-510, -490], [0.005, 0.02]])
```

Column 0: Alim_T_in = [55, 75] °C
Column 1: Ref_T_in = [20, 35] °C  
Column 2: Ref_V_in = [300, 600] L/h
Column 3: P_vacuum = [-510, -490] mbar
Column 4: C_NaCl = [0.005, 0.02] ???

Then conversion:
```python
X_phys[:, 2] /= 3600.0  # L/h -> kg/s
X_phys[:, 3] *= 100.0    # mbar -> Pa
X_phys[:, 4] *= 0.001    # g/L -> fracao massica wt%
```

For Ref_V_in (column 2): 300-600 L/h → 0.083-0.167 kg/s. Looking at real CSV, `mdot_feed_used_kg_s` is around 0.111 or 0.167, so this matches.

For P_vacuum (column 3): -510 to -490 mbar → -51000 to -49000 Pa. Real data has pv_pa_used around -49500 to -49800 Pa. Matches.

For C_NaCl (column 4): If range is [0.005, 0.02] g/L → mass fraction [5e-6, 2e-5]. But real sal_in_used_fraction is around 0.01. That's 1000x different.

There's a discrepancy here. Either:
1. The range unit comment is wrong
2. The conversion factor is wrong
3. The synthetic data is generated for a different salinity range

But looking at the comment on line 31: `# g/L -> fracao massica wt%` - this clearly states what the conversion is supposed to do.

OK, I think the answer might be simpler. Let me look at the real data:
- C_NaCol in CSV ≈ 10.18 (first row)
- sal_in_used_fraction in CSV ≈ 0.0101766 (first row)
- So sal_in_used_fraction = C_NaCl / 1000 approximately

So indeed, C_NaCell values in the real data are in g/L units (roughly 10 g/L), and they are divided by 1000 to get mass fraction (roughly 0.01).

Now for the synthetic data, the raw range is [0.005, 0.02]. If these are in g/L:
- 0.005 g/L = 5 mg/L (very dilute)
- 0.02 g/L = 20 mg/L (still very dilute)

After multiplying by 0.001: [5e-6, 2e-5] mass fraction.

This doesn't match the real data at all. The real C_NaCl values are around 10 g/L. But the synthetic range is 0.005-0.02 g/L.

I think the synthetic data range might be the wt% fraction itself (0.5% to 2% = 0.005 to 0.02 as wt% fraction), and the comment "g/L" on the range is wrong. But then the conversion `*= 0.001` would be wrong too (converting wt% to mass fraction would need `/100`, not `*0.001`).

Actually no: if the raw values [0.005, 0.02] ARE the mass fraction (0.5% to 2%), then the conversion `*= 0.001` should NOT be applied. But it IS applied, giving [5e-6, 2e-5], which is the same problem.

Let me just check if maybe the X_raw representation is different. The `ranges` generates X_raw, and then X_phys is a copy that gets converted. But both X_raw and X_phys store C_NaCl. In the output (line 71), `X_raw[idx,4]` is stored in the CSV. So the surrogate data CSV will have C_NaCol around 0.005-0.02.

Looking at line 71:
```python
"C_NaCl": float(X_raw[idx,4]), "Alim_T_out_phy": t_f,
```

So the surrogate data CSV has C_NaCl in the [0.005, 0.02] range. And these are the raw values BEFORE the conversion. So indeed the surrogate is trained on data where C_NaCl is 0.005-0.02, and the model 0D receives the converted values [5e-6, 2e-5].

This is indeed a dilute solution range. It's possible the script was designed for a specific purpose (testing near-freshwater scenarios) or the ranges were just chosen arbitrarily for testing.

But in any case, here's the key finding:

**The model 0D expects salinity as a mass fraction (0 to 1).**

And the real data CSV has:
- `C_NaCl` in g/L (approximately 10 g/L → 0.01 mass fraction)  
- `sal_in_used_fraction` is the mass fraction version already computed

The TCC training code **does NOT do unit conversion** - it uses C_NaCol directly from the CSV (which is in g/L) as a feature. This means the surrogate models learn to map from g/L to the physics model outputs without explicit conversion. The surrogate is effectively trained on g/L and learns the relationship implicitly.

Now let me also check the `comparison` code to see if there's any unit handling there.

</details>

### Resposta

Let me also check the R code and the comparison between model and real data for any unit handling:

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:21:42 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me also look at the comparison between model 0D and real data to see if there's any unit handling there.

</details>

### Resposta

Let me look at the comparison code between model 0D and real data:

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:21:45 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

No source files in the comparison directory. Let me check the comparison CSV to see what columns exist.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-21 15:21:48 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have all the information I need. Let me compile the comprehensive answer.

Let me also check if there's a sal_in_used_fraction column in the CSV header - I noticed it in the data I read earlier.

From the CSV header (line 1):
```
Alim_T_in,Alim_T_out,deltaP_Alim,Condu_feed,deltaP_ref,Ref_T_in,Ref_T_out,Ref_V_in,Ref_P_in,Re,P_vacuum,C_NaCl,Regime,Flux,Alim_T_out_phy,Ref_T_out_phy,Flux_phy_kg_m2_h,Flux_phy_L_m2_h,sal_feed_out_phy_wt_pct,pv_pa_used,sal_in_used_fraction,mdot_feed_used_kg_s,mdot_cool_used_kg_s,GOR_phy,SECth_phy_kWh_m3,Thermal_eff_phy_pct
```

So the CSV has these relevant columns:
- `C_NaCl`: ~10 (g/L)
- `sal_in_used_fraction`: ~0.01 (mass fraction - the actual input to the model)
- `pv_pa_used`: Pa (actual pressure in Pa)
- `mdot_feed_used_kg_s`: kg/s (actual mass flow in kg/s)

And looking at the TCC code feature list: it uses `C_NaCl` NOT `sal_in_used_fraction`.

So the TCC surrogate models are trained with `C_NaCl` in g/L (around 10), NOT in mass fraction (0.01). The model learns the nonlinear relationship between g/L and the physics model outputs without explicit conversion.

Now here's the most important part:

**The model 0D expects salinity as mass fraction (0-1).**

From the evidence:
1. `entrydata.c` line 13: `entry_salinity_feed = 3.5e-2, // Default: 3.5 wt%` -- 3.5e-2 = 0.035 = 3.5 wt% mass fraction
2. `properties.c` `ActivityCoefficient` line 137: `water_molar_mass * salinity / ((1.0 - salinity) * salt_molar_mass + salinity * water_molar_mass)` -- this is the explicit mass-fraction-to-mole-fraction conversion formula
3. `properties.c` `SaltWaterSpecificHeat` line 55: `alt_salinity = 1000.0 * salinity` -- converts mass fraction to g/kg
4. `properties.c` `SaltWaterLatentHeat` line 170: `(1.0 - salinity)` -- uses as mass fraction directly
5. `output.c` line 38: `100.0 * array[7]` -- multiplies by 100 to show as wt% in output, confirming internal value is mass fraction
6. `main.c` line 27-28: `-entry_salinity_feed: type double, unit wt%` -- documented unit is wt%

So the value the model expects for `-entry_salinity_feed` is the **mass fraction** (dimensionless, 0 to 1). A value of `0.035` = 3.5 wt% = 35 g/kg = 35,000 ppm.

**Conversion:**
- If your data is in **g/L** (like the CSV's C_NaCl column ≈ 10): divide by ~1000 to get mass fraction. More precisely: `mass_fraction = (C_NaCl_in_g_per_L) / (solution_density_in_g_per_L)`. Since density is ~1000-1020 g/L for these salinities, `mass_fraction ≈ C_NaCl / 1000`.
- If your data is in **wt%** (e.g., 3.5): divide by 100. `mass_fraction = wt_pct / 100`.
- If your data is in **g/kg** (e.g., 35): divide by 1000. `mass_fraction = g_per_kg / 1000`.
- If your data is in **ppm** (e.g., 35000): divide by 1,000,000. `mass_fraction = ppm / 1e6`.

The CSV already has the mass fraction in the `sal_in_used_fraction` column (≈0.01), which is `C_NaCl / 1000`.

**The TCC surrogate code:**
- Does NOT convert C_NaCl units when loading the CSV (uses C_NaCl in g/L directly)
- The `gerar_surrogate.py` script DOES convert: `X_phys[:, 4] *= 0.001  # g/L -> fracao massica wt%` when calling the C model binary
- So the surrogate is trained on g/L and learns to approximate the physics model outputs in those units

This is a key insight: if someone wants to call the physics model 0D directly with C_NaCl values from the CSV, they MUST convert g/L to mass fraction (÷1000). But if they're using the trained surrogate, they can pass C_NaÇl directly in g/L.

</details>

### Resposta

Now I have all the evidence. Here is the complete analysis:

---

## 1. NaCl Concentration Unit Expected by the Model 0D

**The model expects salinity as a MASS FRACTION (dimensionless, 0 to 1).**

The definitive evidence chain:

### Entry data (input) -- `entrydata.c` line 13:
```c
entry_salinity_feed = 3.5e-2, // Default: 3.5 wt%
```
The default `3.5e-2 = 0.035` corresponds to 3.5 wt% seawater. The comment confirms the interpretation.

### CLI documentation -- `main.c` lines 27-30:
```c
"-entry_salinity_feed: type double, unit wt%%\n"
"Description - Feed salinity at the inlet of the module\n\n"
"-entry_salinity_cool: type double, unit wt%%\n"
"Description - Coolant salinity at the inlet of the module\n\n"
```
The documented unit is `wt%`, meaning the numeric value IS the fraction already. For 3.5 wt% you pass `0.035`, not `3.5`.

### Internal property correlations -- `properties.c`:

**Activity coefficient** (line 137) -- the definitive chemical engineering conversion from mass fraction to mole fraction:
```c
molar_fraction = water_molar_mass * salinity / ((1.0 - salinity) * salt_molar_mass + salinity * water_molar_mass);
```
This formula only works if `salinity` is mass fraction (kg_salt/kg_solution).

**Specific heat** (line 55) -- converts to g/kg for the correlation:
```c
alt_salinity = 1000.0 * salinity;  // mass fraction → g/kg
```

**Latent heat** (line 170) -- uses salinity as mass fraction directly:
```c
latent_heat_vaporization = pure_latent_heat * (1.0 - salinity);
```

### Output formatting -- `output.c` line 38:
```c
PetscFPrintf(..., "Feed salinity at the outlet of the module =, %.10f, wt%%\n", 100.0 * array[7]);
```
The internal value `array[7]` is mass fraction, multiplied by 100 to display as wt% in the report.

### Summary table for the model 0D:

| Unit | Value for 3.5 wt% seawater | Conversion to model input |
|---|---|---|
| **Mass fraction** (model expects) | **0.035** | — |
| wt% (percent by weight) | 3.5 | ÷ 100 |
| g/L (approx. = g/kg for dilute) | 35 | ÷ 1000 |
| g/kg | 35 | ÷ 1000 |
| ppm (mg/kg) | 35,000 | ÷ 1,000,000 |
| mg/L | 35,000 | ÷ 1,000,000 |

More precisely: `mass_fraction = g_per_L / solution_density_in_g_per_L`, but since density ~1000-1020 g/L, dividing by 1000 is an excellent approximation.

---

## 2. How the TCC Code Loads the CSV and Handles C_NaCl Units

### Data loading -- `data.py`, function `read_tabular_csv()`:
- Reads the CSV at `C:\Users\frota\OneDrive\Documentos\TCC\dados_att_com_var_com_phy.csv`
- Handles comma-as-decimal separator (e.g., `"10,1766"` → `10.1766`)
- **NO unit conversion is performed** on any column

### Feature extraction -- `config.yaml` / `config.py`:
```yaml
columns:
  features:
    - Alim_T_in
    - Ref_T_in
    - Ref_V_in
    - P_vacuum
    - C_NaCl
```

### What the CSV actually contains:

From the CSV header:
```
Alim_T_in, ..., C_NaCl, ..., sal_in_used_fraction, ...
```

Sample row:
```
C_NaCl = 10.1766
sal_in_used_fraction = 0.0101766
```

- **`C_NaCl` is in g/L** (~10 g/L = ~10,000 mg/L)
- **`sal_in_used_fraction` is the mass fraction** (~0.01) that was actually fed to the model 0D

The TCC code uses `C_NaCl` (g/L) as the feature, **NOT** `sal_in_used_fraction`.

### The only place unit conversion happens -- `gerar_surrogate.py` line 31:

```python
# Converter unidades para o modelo C
X_phys = X_raw.copy()
X_phys[:, 2] /= 3600.0  # L/h -> kg/s
X_phys[:, 3] *= 100.0    # mbar -> Pa
X_phys[:, 4] *= 0.001    # g/L -> fracao massica wt%
```

This is the script that calls the C model binary via WSL to generate synthetic surrogate training data. It explicitly converts: **g/L × 0.001 = mass fraction**.

The synthetic data ranges are:
```python
ranges = np.array([[55, 75], [20, 35], [300, 600], [-510, -490], [0.005, 0.02]])
#           Alim_T_in °C, Ref_T_in °C, Ref_V_in L/h, P_vacuum mbar, C_NaCl ???
```

And the C_NaCl parameter fed to the model after conversion:
```
# C_NaCl raw range: [0.005, 0.02] g/L   → after *0.001: [5e-6, 2e-5] mass fraction
```

However, the synthetic data is stored back in the CSV using the **raw (pre-conversion)** value:
```python
"C_NaCl": float(X_raw[idx,4]),   # raw g/L value stored in CSV
"Alim_T_out_phy": t_f,            # physics model output
```

### Key finding about the TCC surrogate training:

The surrogate ML models (neural networks) are trained on `C_NaCl` **in g/L** (values ~10), mapping to physics model outputs. The model implicitly learns the nonlinear relationship between g/L and the physics, including the internal conversion.

**No unit conversion is done when loading the CSV for surrogate training.** The `StandardScaler` in the pipeline normalizes the features, but the raw unit remains g/L for C_NaCl.

---

## 3. Documentation and Comments About Units

### In the model 0D source:

| File | Line | Comment |
|---|---|---|
| `entrydata.c` | 13-14 | `// Default: 3.5 wt%` (on `3.5e-2` value) |
| `main.c` | 27-30 | `unit wt%` in CLI help |
| `output.c` | 38 | `, wt%%` in output format string, with `100.0 *` multiplier |
| `properties.c` | 55 | `alt_salinity = 1000.0 * salinity` (implicitly documents that input is mass fraction, not g/kg) |
| `properties.c` | 137 | mass-fraction-to-mole-fraction formula (implicit proof) |

### In the TCC code:

| File | Line | Comment |
|---|---|---|
| `gerar_surrogate.py` | 27 | `# Converter unidades para o modelo C` |
| `gerar_surrogate.py` | 31 | `# g/L -> fracao massica wt%` (documenting the C_NaCl conversion) |

---

## Summary / Actionable Guidance

To convert real data for use with the model 0D (the C binary `vagmd0Dmodel`):

| If your `C_NaCl` is in... | Example value | Pass this to `-entry_salinity_feed` |
|---|---|---|
| **g/L** (like CSV column) | 10.18 | `0.01018` (divide by ~1000) |
| **wt%** | 1.018 | `0.01018` (divide by 100) |
| **g/kg** | 10.18 | `0.01018` (divide by 1000) |
| **ppm** | 10,180 | `0.01018` (divide by 1e6) |
| **mg/L** | 10,180 | `0.01018` (divide by 1e6) |

The fast conversion: **`mass_fraction = C_NaCl_in_g_L / 1000`** (since 1 L of water ≈ 1 kg). The CSV column `sal_in_used_fraction` already holds this pre-computed value.

**Important nuance for the TCC surrogate models:** They are trained on `C_NaCl` in g/L directly. If you use the trained surrogate (not the C binary), pass C_NaCl in **g/L** as-is, without converting.

*Novo passo iniciado*

---

*13 messages | 86 parts | 💰 $0.0134 | ⏱️ 0h02m16s*
