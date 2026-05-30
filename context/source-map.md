# context/source-map.md — Citation & Empirical-Anchor Audit

> **Role:** Does each external claim say what the paper says it says? Verdicts are from
> Claude's training knowledge (cutoff Jan 2026); items tagged **[verify]** should be
> confirmed against the primary source before being relied on. Attacks on the *model*
> live in [stress-test.md](stress-test.md); this file only checks the *citations*.

## Headline numbers

| Claim in paper | Cited as | Assessment | Action |
|----------------|----------|-----------|--------|
| Outdoor air pollution could cut global GDP ~**1% by 2060** | [2] OECD 2016, *Economic Consequences of Outdoor Air Pollution* | **Accurate.** OECD 2016 projected market GDP losses ~1% of GDP by 2060 (labor productivity + health spend + crop yields), with much larger *welfare* costs. Paper uses the market-GDP figure correctly. | OK |
| Unmitigated warming could cut output **10–23% by 2100** | [3] IPCC 2022, **WGIII (Mitigation)** | **CONFIRMED inaccurate (web-verified).** WGIII is *Mitigation* (emissions/abatement pathways), not damages — that is WGII (*Impacts*). The 23% figure is the signature result of **Burke, Hsiang & Miguel 2015 (Nature 527:235)**, not an IPCC product; WGII itself *declined* to endorse a single headline aggregate-loss number (offered only ~2–15% of GDP qualitative guidance for 2.1–3.5°C). The clean "10–23%" bracket is a synthesis of the damages literature, mis-attributed to the wrong working group. | **Re-cite to Burke–Hsiang–Miguel 2015 (+ optionally WGII Ch. 16); reserve WGIII for mitigation-cost claims.** |
| Useful exergy explains a far larger growth share, narrowing the Solow residual | [4,5] Ayres & Warr 2005/2009 | **Accurate** characterization of Ayres–Warr's thermoeconomics. | OK |
| Exergy output elasticities **0.29–0.46** across countries | [7] Santos et al. 2018, *Ecological Economics* 148 | **Plausible/accurate**; consistent with that paper's cross-country exergy production-function estimates. (Note: these large elasticities are in tension with the paper's later 2-factor reduction — see stress-test F8, a *modeling* issue, not a citation issue.) | OK |
| EPA 2023 central SCC **~\$190/tCO₂ @ 2%** | [9] EPA 2023, *Report on the SC-GHG* | **Accurate.** EPA's Nov-2023 final SC-CO₂ ≈ \$190 (2020\$) at the 2% near-term Ramsey rate. | OK |
| Rennert et al. **~\$185/tCO₂** | [10] Rennert et al. 2022, *Nature* 610 | **Accurate.** Central SC-CO₂ ≈ \$185/t. | OK |
| Methane **~\$1,600/tCH₄** | [9] EPA 2023 | **Plausible/accurate** for EPA 2023 SC-CH₄ at 2% (near-term). | OK |
| Nitrous oxide **~\$5,400/tN₂O** | [9] EPA 2023 | **CONFIRMED inaccurate (web-verified, ~10× too low).** EPA 2023 (Report on the SC-GHG, Table ES.1) central SC-N₂O for 2020 emissions at 2% ≈ **\$54,000/tN₂O** (corroborated by RFF's summary of the EPA table). \$54k sits coherently beside the same-rate SC-CO₂ \$190 and SC-CH₄ \$1,600; \$5,400 (near the CH₄ value) is implausible given N₂O's ~300× GWP and long lifetime — a dropped-digit transcription error. *(One web auto-summary returned "\$5,400" citing no source — treated as a summarizer artifact.)* | **Fix to ~\$54,000/tN₂O.** |
| PM₂.₅: **1 µg/m³ ↑ ⇒ ~0.55%** labor-productivity ↓ | [12] Dechezleprêtre et al. 2025, OECD STI Policy Papers | **Plausible** and in line with that literature's magnitudes. Paper calls it "European firm-level studies"; [12] is an OECD paper drawing on European data — fair. | OK |
| PM₂.₅ productivity co-benefit **\$950–3,000/household/yr per µg/m³** | [12] | **[verify]** — magnitude is plausible but I can't confirm the exact band from memory. | **[verify]** |
| EU cut **GHG per unit GDP ~50%, 1990–2020** | (no ref; §3.6) | **Plausible/accurate.** EU GHG-intensity of GDP fell roughly by half (emissions ~−30% while real GDP grew ~+60%). | OK |
| **Six of nine** planetary boundaries transgressed | [24,25] Steffen 2015 / Richardson et al. 2023, *Sci. Advances* | **Accurate.** Richardson et al. 2023 report six of nine transgressed. | OK |
| Graff Zivin–Neidell: ozone ↓ agricultural-worker productivity | [11] 2012, *AER* 102(7) | **Accurate.** Landmark study (California farm/fruit pickers; ozone causally lowers output). | OK |

## Framework/model citations (used to position the contribution)

| Anchor | Cited as | Assessment |
|--------|----------|-----------|
| **Green Solow** | [15] Brock & Taylor 2010, *J. Econ. Growth* 15(2):127–153 | **Correct citation.** Relevant: Green Solow already ties emissions to output and yields EKC + emissions convergence — directly bears on novelty claim #2/#3 (stress-test §A, F1). |
| **DICE** | [18] Nordhaus 2017 PNAS; [30] Barrage & Nordhaus 2024 PNAS (DICE-2023R) | **Correct — and structurally decisive (C3 web-verified against DICE-2016R source).** DICE net output = `gross × (1 − 0.00236·T²)` (older vintages used `1/(1+0.00236·T²)`) — i.e. damages are *already* a multiplicative production-side factor, exactly the role Ω plays, and in a Ramsey model with endogenous capital so the "amplification" propagates into the capital stock numerically. **Directly undercuts** novelty claims #2/#3 (stress-test §A, F1). |
| Directed technical change | [16] Acemoglu, Aghion, Bursztyn, Hemous 2012, *AER* 102(1) | Correct; supports the §8.3 clean-innovation-subsidy policy. |
| Georgescu-Roegen entropy/economics | [1] 1971, Harvard UP | Correct; foundational for the dissipative-structure framing (which stress-test F8 argues is decorative in the math). |
| Rebound | [28] Brockway et al. 2015, *Energies* | Correct — and notably **self-undercutting**: rebound is cited but never incorporated, weakening the "drive τ→0" optimism (stress-test F8). |
| EKC | [33] Grossman & Krueger 1995, *QJE* 110(2) | Correct — and **self-undercutting** for §6.1: EKC implies the proposed β₁<0 can arise from development alone (stress-test F10). |
| Green accounting lineage | [19] SEEA-EA 2021; [20] Lawn 2003 (GPI/ISEW); [21] World Bank 2023; [22] Arrow et al. 2012 (Inclusive Wealth); [27] Stiglitz–Sen–Fitoussi 2009 | Correct citations. They also establish that Thermo-GDP = GDP − D is *within* this tradition (novelty claim #4, stress-test §A). |
| Hotelling / Ramsey / Solow / Hartwick | [14] 1931; [17] 1928; [31] 1956; [34] 1977 | Correct canonical citations. |

## Literature the *stress-test* invokes that the paper omits (relevant counter-citations)

These are not in the paper but are load-bearing for the critique:

- **Mankiw, Romer & Weil 1992, *QJE*** — the augmented-Solow level-effect M^(1/(1−α)); shows the "amplification" is generic (F1). **C4 web-verified:** y* is homogeneous of degree 1/(1−α) in any Hicks-neutral multiplier (=1.4286 at α=0.3, 1.667 at α=0.4); the paper's own numerics (1−0.9^(1/0.7)≈0.14) check out — only the "not present in Green Solow/DICE" framing is wrong.
- **Weil 2007, *QJE*, "Accounting for the effect of health on economic growth"** — prior health-augmented growth accounting (novelty claim #1).
- **Grossman 1972** — original health-capital concept (novelty claim #1).
- **Nordhaus & Tobin 1972 (Measure of Economic Welfare)** — origin of "GDP omits environmental damage" (F11).
- **Weitzman (green NNP)** — output-minus-shadow-priced-damage is the definition of green net product (novelty claim #4).
- **Burke, Hsiang & Miguel 2015, *Nature*** — likely true source of the "10–23% by 2100" figure mis-attributed to IPCC WGIII.

## Net citation verdict (post-verification)

The paper's citations are **mostly accurate and appropriate** — it is well-read and cites the
right canonical works (OECD 1%, EPA SC-CO₂ \$190 / SC-CH₄ \$1,600, six-of-nine boundaries, and
the MRW/DICE structural facts all **web-verified accurate**). Two concrete errors are now
**confirmed** and should be fixed: **(1)** SC-N₂O is ~**\$54,000/tN₂O**, not the paper's
\$5,400 (~10× too low); **(2)** the 10–23%-by-2100 damages figure is **Burke–Hsiang–Miguel
2015 / IPCC WGII**, mis-attributed to WGIII (Mitigation). One item remains open: the PM₂.₅
co-benefit band \$950–3,000 **[verify]**.

The deeper problem is not miscitation but **under-citation of the works that pre-empt the
novelty claims**: Green Solow and DICE are cited but their structural relationship to Ω is not
acknowledged (and C3 confirms DICE already has the multiplicative damage factor), while MRW,
Weil, and Nordhaus–Tobin are absent. See [stress-test.md](stress-test.md) §A.
