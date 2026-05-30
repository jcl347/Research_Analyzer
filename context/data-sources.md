# context/data-sources.md — Verified Data Inventory + Starter Dataset

> **Role:** the real, accessible data behind [hypothesis-tests.md](hypothesis-tests.md).
> Access paths and variable codes were **verified live** by data-acquisition agents
> (run `wf_a4624ef0`); anchor values are tagged `verified` only where an agent actually
> retrieved them this session. **Nothing is imputed** — every unretrieved cell is blank.
> Runnable analysis code: [analysis/anchor_regression.R](analysis/anchor_regression.R)
> and [analysis/anchor_regression.py](analysis/anchor_regression.py).
>
> **Integrity rule for this file:** the anchor values are a handful of *verified* points
> to seed and sanity-check a real download — **not** an analysis dataset. Do not run
> inference on them (see "Data-integrity hazards" below).

## Master panel design

Build ONE shared panel keyed on **`ISO3 × year`**: PWT (TFP, hc, real GDP) ⟕ OWID/EDGAR
(τ) ⟕ WDI PM₂.₅ ⟕ WHO HALE (H) ⟕ WDI macro (controls). Reused across H1, H5, H6, H8.

## The six sources

### 1. TFP — Penn World Table 10.01 (GGDC)
- **Access:** `https://www.rug.nl/ggdc/docs/pwt100.xlsx` (Excel, sheet `Data`) or `pwt100.dta`. *(The "10.01" patch is served under `pwt100` filenames. Note: **PWT 11.0** released 2025-10-07 — 185 countries, 1950-2023 — is now newest.)*
- **Key vars:** `rtfpna` = TFP at constant national prices (2017=1) — the LHS for `dln(TFP)`; `rwtfpna` (welfare-relevant TFP, robustness); `rgdpna`, `hc` (human capital), `labsh`, `emp`, `pop`. Cross-country TFP *levels* use `ctfp`/`cwtfp` (not `rtfpna`).
- **Coverage / key:** 183 countries × 1950-2019; `countrycode` (ISO3) × `year`.
- **Verified anchors:** USA `rtfpna` 2019 = **1.0169**, DEU = 0.9907, CHN = 0.9668, IND = 1.0201 (2017 base = 1.000); USA `hc` = 3.749, CHN `hc` = 2.699, IND `hc` = 2.171; USA `labsh` = 0.597.
- **⚠ Caveat:** `rtfpna` = 1.000 in 2017 *within each country* → its level is meaningless across countries; **only `dln(rtfpna)` is valid as the §6.1 LHS.**

### 2. τ proxy — CO₂ intensity (Our World in Data, primary)
- **Access:** `https://ourworldindata.org/grapher/co2-intensity.csv?v=1&csvType=full&useColumnShortNames=true` (column `emissions_total_per_gdp`). Secondary cross-check: World Bank `EN.GHG.CO2.RT.GDP.PP.KD`.
- **Units / coverage / key:** kg CO₂ per international-\$ (2011 PPP); ~200 countries, annual 1820-2022 (latest 2022); `Code` (ISO3) × `year`.
- **Verified anchors (2022):** USA **0.295**, CHN 0.434, IND 0.196, DEU 0.180, SWE 0.086, RUS 0.358, BRA 0.151, QAT 3.014 (outlier); (2023) USA 0.185, CHN 0.407.
- **⚠ Caveat:** CO₂-only, territorial, excludes land-use change. For the model's full `‖TO‖`, rebuild a **damage-weighted multi-pollutant** intensity from EDGAR (CO₂/CH₄/N₂O/PM₂.₅/SO₂/NOₓ) × SCC weights. **And τ has Y in its denominator → endogenous (stress-test G1/G3).**

### 3. PM₂.₅ exposure — World Bank WDI `EN.ATM.PM25.MC.M3`
- **Access:** `https://api.worldbank.org/v2/country/all/indicator/EN.ATM.PM25.MC.M3?format=json&date=2010:2020`. (Compiled from IHME GBD 2023; upstream surface = van Donkelaar/ACAG satellite + monitors.)
- **Units / coverage / key:** µg/m³ population-weighted mean annual; ~190 countries, 1990/95/2000/05 + annual 2010-2020; ISO3 × year.
- **Verified anchors (2020):** USA **7.81**, CHN 34.81, IND 48.39, DEU 10.29, BRA 12.18, NGA 56.53, ZAF 23.75, JPN 12.84, GBR 9.91; World 31.32.

### 4. H proxy — WHO HALE (`WHOSIS_000002`)
- **Access:** GHO OData (no key): `https://ghoapi.azureedge.net/api/WHOSIS_000002` (filter `Dim1 eq 'SEX_BTSX'`, `SpatialDim`=ISO3, `TimeDim`=year).
- **Units / coverage / key:** years of healthy life expectancy at birth; ~190 states, 2000-2021 (latest 2021); `SpatialDim` (ISO3) × `TimeDim`.
- **Verified anchors (2021):** JPN **73.40**, CHE 71.15, DEU 68.93, CHN 68.58, USA 63.91, BRA 61.83, IND 58.15, NGA 54.95; global ≈ 63.7.
- **⚠ Caveat:** HALE is **downstream of pollution** → a *bad control* on the RHS (stress-test G11); report the anchor with and without it.

### 5. Macro controls — World Bank WDI
- **Access:** `https://api.worldbank.org/v2/country/{ISO3;…}/indicator/{CODE}?date=YYYY:YYYY&format=json&per_page=20000` (no key).
- **Key vars:** GDP pc `NY.GDP.PCAP.KD` (const 2015 \$); savings `NY.GNS.ICTR.ZS`; pop growth `SP.POP.GROW`.
- **Verified anchors (2022):** GDP pc — USA \$63,886, DEU \$44,817, CHN \$11,831, BRA \$9,032, NGA \$2,254, IND \$2,098; savings — CHN 44.8%, IND 29.8%, USA 18.7%; NGA pop growth 2.09%.

### 6. Damage shadow prices + material (M) — EPA / Rennert / UNEP-IRP
- **Access:** EPA 2023 SC-GHG report `https://www.epa.gov/system/files/documents/2023-12/epa_scghg_2023_report_final.pdf` (Table ES.1); material footprint via OWID (UNEP-IRP Global Material Flows).
- **Verified anchors:** **SC-CO₂ = \$190/t** (2020 emissions, 2% rate; \$120 @2.5%, \$340 @1.5%; rising to \$230 in 2030, \$308 in 2050); **SC-CH₄ ≈ \$1,600/t**; **SC-N₂O ≈ \$54,000/t** *(corrects the paper's erroneous \$5,400 — see [source-map.md](source-map.md))*; Rennert et al. 2022 SC-CO₂ = \$185 (5-95%: \$44-413). DMC/capita 2023: USA 25.0 t, CHN 25.1 t, IND 6.0 t.

## Assembled starter table (verified cells only)

| ISO3 | CO₂ int. (OWID '22) | PM₂.₅ ('20) | HALE ('21) | GDP pc ('22) | `rtfpna` ('19) |
|------|---------------------|-------------|------------|--------------|----------------|
| USA | 0.295 | 7.81 | 63.91 | 63,886 | 1.0169 |
| CHN | 0.434 | 34.81 | 68.58 | 11,831 | 0.9668 |
| IND | 0.196 | 48.39 | 58.15 | 2,098 | 1.0201 |
| DEU | 0.180 | 10.29 | 68.93 | 44,817 | 0.9907 |
| BRA | 0.151 | 12.18 | 61.83 | 9,032 | — |
| NGA | — | 56.53 | 54.95 | 2,254 | — |
| JPN | — | 12.84 | 73.40 | — | — |
| SWE / QAT / RUS | 0.086 / 3.014 / 0.358 | — | — | — | — |
| GBR / ZAF / CHE | — | 9.91 / 23.75 / — | — / — / 71.15 | — | — |

*(Blank = not retrieved this session, **not** imputed. ~5-6 countries are fully overlapping.)*

## Illustrative cross-section (n=5-6 — NOT inference; reads as the EKC confound)

- **PM₂.₅ vs ln(GDP pc):** strong **negative**, Pearson r = **−0.85** (n=5). Richer → cleaner air. ⚠ **This is *exactly* the EKC/development pattern (stress-test G12)** — it does *not* support the thermo mechanism; it is the confound the battery must purge.
- **HALE vs ln(GDP pc):** positive, r = +0.67 — the `b2>0` direction, but confounded with development and HALE is mechanically downstream (G11).
- **CO₂ intensity vs ln(GDP pc):** weak/null, r = **+0.16** (n=5). Informative: τ is **not** a simple monotone function of income (China high-τ/mid-income, USA mid-τ/high-income) — relevant to whether τ is a slow exogenous state (H8b).
- **P5/convergence:** **not testable** from a cross-section — needs the time-differenced panel with country+year FE.

## Data-integrity hazards (bar inference until a real download)

1. **`rtfpna` is a within-country index** (=1 in 2017 everywhere) → cross-country levels are meaningless; only `dln(rtfpna)` is valid.
2. **τ = emissions/GDP has Y in the denominator** (G1/G2) → mechanically endogenous; lagging does not fix it.
3. **HALE / inverse-PM₂.₅ are downstream of pollution** (G11) → bad controls; the PM₂.₅ instrument for H is invalid (F10).
4. **The cross-section IS the EKC pattern** (G12) → any cross-sectional "result" is indistinguishable from ordinary development; only the within-unit cognitive-gradient designs (H7/H2/H6-layer-3) discriminate.

## Runnable analysis code

- **[analysis/anchor_regression.R](analysis/anchor_regression.R)** — `fixest`/`data.table`: loads the 5 named datasets, builds the `ISO3×year` panel, runs the §6.1 anchor (`dln_tfp ~ tau_l1 + lnH_l1 + lngdp_l1 + s + n | iso3 + year`, clustered), the **EKC development horse-race** (adds `ln GDPpc + its square`), and the **sector cognitive-intensity test** (`pm25_l1 : cog_intensity`), with the G1/G11/F10 caveats inline.
- **[analysis/anchor_regression.py](analysis/anchor_regression.py)** — `pandas`/`linearmodels`/`statsmodels` equivalent.
- *Agent-generated starter code — review before running; supply the downloaded CSVs named in each header.*

## Honest status

This is a **verified data-access map + a seeded starter table + runnable code**, not a
completed estimation. The decisive tests (H7/H2 cognitive gradient) require **microdata
access** (Brazil ENEM is the public spine; chess and firm cognitive-vs-physical panels
follow). The fastest real result available now is **H8 leg (b)** — regress `dln τ` on
`dln Y` with country+year FE on the public PWT × OWID panel; it directly pits the EKC
("τ falls with income → trap dissolves") against the paper ("τ ≈ Y-invariant").
