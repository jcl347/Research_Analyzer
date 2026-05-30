# context/hypothesis-tests.md — Testable Hypothesis Battery

> **Role:** Turn the paper's claims into a **pre-registerable, falsifiable empirical
> program**, designed against the stress-test's failure modes (especially **G12
> falsifiability** — the predictions are also implied by ordinary development/EKC). The
> neutral reading is [paper-understanding.md](paper-understanding.md); the critique is
> [stress-test.md](stress-test.md); the data + runnable code are
> [data-sources.md](data-sources.md) and [analysis/](analysis/).
>
> **Provenance:** produced by a 19-agent system (run `wf_a4624ef0`, ~968k tokens):
> 8 agents formalized one hypothesis each → a 4-agent **idea-sharing design panel**
> (identification-skeptic, data-feasibility-engineer, power/pre-registration-analyst,
> discriminating-test-designer) cross-critiqued all 8 → 6 agents pulled real data → 1
> assembled a starter dataset + analysis code. Every hypothesis names the **exact result
> that would reject it.**

## The one finding that reorganizes everything (panel consensus)

All four panelists independently converged on the same conclusion: **the macro
country-level τ→TFP coefficient is not salvageable** (the stress-test's G1 "τ has Y in
the denominator" and G3 "τ ≈ damage measure" are unbreakable at the country level), and
**the entire battery's discriminating power collapses onto a single object — the
*cognitive-intensity gradient* of the pollution response within a common
airshed/country-year.** That gradient is the empirical signature of the paper's one
genuinely novel claim, **ζ(H)** (pollution erodes cognition → measured TFP falls while
knowledge rises). 

**Implication for how to test the paper:** a bare `b1<0` in the §6.1 anchor regression is
**necessary but not sufficient** — an EKC-only world reproduces it. The paper's mechanism
is confirmed *only* if the pollution penalty is **larger in cognitively-intensive
sectors/tasks**, within saturated time×area fixed effects that purge the development
margin. The panel's shared recommendation: **freeze ONE pre-registered O*NET/PIAAC
cognitive-intensity index and use it identically across H1, H2, H4, H5, H6, H7**, so the
ζ(H) gradient is the battery-wide pre-specified estimand.

## Hypothesis battery at a glance

| ID | Tests | Discriminates EKC? | Feasibility | Panel verdict |
|----|-------|--------------------|-------------|---------------|
| **H7** cognitive-ζ | ζ(H): within-worker, reversible PM₂.₅ → cognitive-task error gradient | **Yes — cleanest** | high (needs microdata access) | **#1 across all 4 panelists** — the framework's decisive test |
| **H2** PM₂.₅-productivity | PM₂.₅ × sector cognitive-intensity → labor productivity | **Yes (interaction)** | high | Strong scalable labor-market discriminator |
| **H4** amplification | macro growth gain from abatement **>** BenMAP-valued health saving (ψ_total>1) | **Yes (the wedge)** | medium | Sharpest *macro* discriminator; quantifies P4 |
| **H6** anchor (§6.1) | `dln TFP = b1·τ + b2·lnH +…`; + sector cognitive interaction | macro layer **No**, micro layer yes | high | Macro = benchmark only; stake claim on γ_cog<0 |
| **H1** τ-TFP (P1) | causally-identified τ↓ → TFP↑, concentrated in cognitive sectors | only via the triple-diff | high | Demote macro main effect; keep sector triple-difference |
| **H5** convergence (P5) | high-τ/low-H converge slower | weakest (most EKC-exposed) | high | Reframe as *sector* convergence gap; not the rate-survival test |
| **H8** Ω-calibration | is the "growth trap" first-order? is τ exogenous to Y? | Leg (b) **opposes** EKC | high | Sharp, pre-destined to falsify the "large trap" rhetoric |
| **H3** Thermo-GDP (P3) | gap largest in throughput-heavy economies | Part A construction-true; Part B yes | high | Fold Part B into H4; Part A is a benchmark only |

## The hypotheses (each falsifiable)

### H7 — ζ(H), the decisive test · feasibility high · **run this first**
- **Claim:** acute, plausibly-exogenous PM₂.₅ transiently and *reversibly* degrades measured output per unit effort on **cognitive** tasks, holding the worker, knowledge, capital, and wage bill fixed; the decrement rises with task cognitive-intensity and is ~zero on physical-routine tasks at identical exposure.
- **H₀:** the PM₂.₅ × cognitive-intensity interaction = 0 (within worker/date/venue FE). **H₁:** interaction < 0.
- **Design:** within-worker + within-site + date FE; identify off day-to-day point-of-exposure PM₂.₅ deviations. Primary outcome = engine-verified per-decision error rate. Operationalizations: chess move quality vs Stockfish under time pressure (Künn-Palacios-Pestel ~30k moves), national-exam scores (Brazil ENEM, geocoded, millions of obs, public INEP microdata) merged to ACAG satellite PM₂.₅, and a co-located **cognitive-vs-physical task contrast in firm data** (Chang et al. 2019 call-center = cognitive arm; Chang et al. 2016 pear-packers = physical arm).
- **Falsifies if:** the interaction is statistically indistinguishable from 0 (95% CI contains 0) AND its point estimate < ⅓ of the chess benchmark, OR the effect is equal on physical and cognitive tasks.
- **Why it discriminates:** EKC is slow, between-unit, income-driven; a within-person, daily-frequency, fully-reversible cognitive gradient is something development *cannot* produce. **This design IS the framework's discriminating test.**

### H2 — PM₂.₅ × cognitive-intensity → labor productivity · feasibility high
- **Claim/H₁:** a 1 µg/m³ PM₂.₅ rise lowers productivity more in cognitively-intensive sectors (priors: −0.3% to −0.55%/µg/m³ main effect; Chang et al. 2019, Dechezleprêtre et al. 2025).
- **Design:** county×month FE absorb the entire airshed/EKC level; identify off the **within-airshed cross-sector cognitive gradient**. IV for local PM₂.₅: **thermal inversions** (Chang et al. 2019; Arceo-Gómez et al. 2016) and **wildfire smoke** (Borgschulte-Molitor-Zou 2024 — panel's preferred *primary* shock, weaker temperature coupling than inversions).
- **Falsifies if:** with MDE ≤0.1pp/µg/m³ on the interaction, β_int is not negative at 5%.
- **Panel fix:** lead with monitored microdata (call volume, piece-rate, software commits); QCEW county-month is robustness only (aggregation kills the interaction). Watch the **heat/co-pollutant confound** inside the interaction.

### H4 — amplification (P4), the macro discriminator · feasibility medium
- **Claim/H₁:** the total macro gain from an exogenous abatement shock **exceeds** the BenMAP-valued avoided mortality+morbidity of the same shock (ψ_total>1), with the excess running through **measured TFP** (the un-priced ζ(H) channel).
- **Design:** event-study DiD on a real natural experiment — Title IV scrubbers / coal retirements with **downwind-vs-upwind** exposure (Luechinger 2014), CAA-amendment nonattainment (Greenstone-List-Syverson), RGGI; Callaway-Sant'Anna for staggered adoption.
- **Falsifies if:** the upper bound of the 95% CI for ψ_total ≤ 1 (macro response fully explained by directly-priced health benefits).
- **Critical panel fixes:** (1) **Remove the GLS ~4.8% manufacturing-cost number from the falsification threshold — it is wrong-sign** (a compliance cost, not a health benefit) and would mislead the pre-registration; use only downwind/health-channel exposure. (2) Define the denominator as BenMAP avoided **mortality + clinically-valued morbidity ONLY** (explicitly excluding any productivity/cognition value), so the wedge is by construction the un-priced channel.

### H6 — the §6.1 anchor regression · feasibility high · **the workhorse benchmark**
- **Claim:** `dln(TFP)_it = b1·τ_{i,t−1} + b2·ln(H_{i,t−1}) + γ'X + a_i + d_t`; predicts b1<0, b2>0.
- **Three nested layers:** (1) macro FE anchor — *acknowledged non-causal*, reported as a benchmark; (2) a "simultaneity fix" instrumenting τ — **the panel judged this does NOT actually break G1/G3**; (3) **the make-or-break layer:** within-region inversion-IV-for-PM₂.₅ × industry cognitive-intensity (γ_cog), in an industry×region×year panel (US BEA-BLS + O*NET, or China ASIF).
- **Falsifies if:** the damage-weighted τ coefficient isn't negative net of an EKC polynomial + FE, **OR** γ_cog is indistinguishable from 0.
- **Data note:** use a **damage-weighted multi-pollutant** τ (EDGAR CO₂/CH₄/N₂O/PM₂.₅/SO₂/NOₓ × EPA-2023 shadow prices — with **SC-N₂O ≈ \$54,000/t, corrected from the paper's \$5,400**), not single-gas CO₂/GDP.

### H1 — P1 (τ↓ → future TFP↑) · feasibility high
- Same spine as H6. **Panel consensus: drop τ-as-country-treatment entirely** (uninstrumentable) and move identification onto the within-country-year **cross-sector cognitive triple-difference** (country-year + sector-year FE absorb all development). DiD around exogenous decarbonization/fuel-switch mandates (Callaway-Sant'Anna) is the more credible causal arm than the meteorological IV.
- **Falsifies the *distinct* claim** (not just P1) if, even with b1<0, the τ × sector-cognitive interaction is ≥0 and the measured-TFP-vs-R&D/patent decoupling doesn't appear — then it's observationally identical to development.

### H5 — P5 convergence · feasibility high · **most EKC-exposed**
- **Claim:** high-τ/low-H countries converge slower (γ_τ>0, γ_H<0) *after* flexibly conditioning on income.
- **Panel warning:** this is the **most G12-exposed** prediction (poor countries are dirty, unhealthy, and far from steady state), and the "survival after income interactions" falsifier is **structurally unwinnable** (collinearity + dynamic-panel/Nickell bias). **Reframe** to a *within-country sectoral* convergence test (do cognitive sectors in high-τ/low-H countries converge to the frontier slower?), and — per stress-test B.3/G10 — report it as **converging to a lower level**, not a slower rate.

### H8 — Ω calibration: is the "trap" real-sized? · feasibility high · **sharp** · ✅ **RUN — see [results.md](results.md)**
> **Executed result:** Leg (b) on the real OWID panel (164 countries) shows an **EKC gradient** — rich economies decouple (intensity −2.5%/yr, falling in 70% of country-years) so the trap **dissolves** for them (stress-test G2), while poor economies do **not** decouple (intensity flat, +0.04%/yr), so the trap premise **holds where the paper claimed a poverty trap** (P5). The naive `dln(τ)~dln(Y)` came out exactly `β−1` (mechanical, confirming G1/G2). Leg (a) calibration: the implied output gap is **magnitude-indeterminate** (3%→40%+, set by the unpinned p₀/ψ/health-elasticity) — which **corrected an over-claim in stress-test F4**.
- **Two legs.** (a) Calibrate `GAP = 1 − (Ω*)^(1/(1−α))` from real τ and H over published parameter bounds (α∈[0.3,0.4], **ψ∈[1,3]** — ψ<1 excluded since stress-test **G4** shows it violates the paper's own convexity axiom, SCC \$185–190); Monte-Carlo the CDF and report the share of country-years with GAP≥10%, **as an explicit function of the unidentified normalization price p₀**. (b) Estimate within-country `d ln τ / d ln Y`.
- **Falsifies the "large trap" rhetoric if:** median GAP ≤5% for high-τ economies at p₀ set so mean τ≈0.05; **and** the trap "dissolves" if `d ln τ/d ln Y < 0` (EKC).
- **Why it's a clean EKC contrast:** leg (b) **pits EKC against the trap directly** — EKC predicts τ falls as Y rises (trap dissolves), the paper needs τ roughly invariant. **Panel fix:** instrument Y-growth (Bartik export-demand) so the elasticity isn't the mechanical Y-in-denominator artifact (G1/G2).

### H3 — P3 Thermo-GDP divergence · feasibility high · **mostly a benchmark**
- Part A (gap = D/GDP larger where D larger) is **construction-true** — conceded, not evidence. The only falsifiable content is **Part B** (green transitions → faster *subsequent* GDP), which has a **fatal pre-trends/mean-reversion confound**; the panel recommends **folding Part B into H4** (same amplification wedge) and going subnational (US states under RGGI/coal retirements) to lift episode count.

## Panel synthesis — the cross-cutting recommendations

- **Identification-skeptic:** adopt ONE frozen cognitive-intensity index; the macro τ coefficient is unsalvageable (G1/G3); top credibly-identifiable = **H7 > H2 > H6(layer-3)**.
- **Data-feasibility-engineer:** build ONE shared `ISO3×year` master panel (PWT ⋈ EDGAR ⋈ WHO-HALE ⋈ WDI) reused across H1/H5/H6/H8; most runnable-now = **H8(leg b) > H6(macro) > H5**; H7 is an *access-to-microdata* task (lead with Brazil ENEM, public).
- **Power/pre-registration-analyst:** **freeze-and-placebo** the cognitive channel as the single shared "discrimination certificate"; best-powered = **H7 > H2 > H6**; flagged H4's wrong-sign GLS anchor and H5's underpowered triple-interaction.
- **Discriminating-test-designer:** every hypothesis must pass one shared protocol — purge the EKC margin with within-unit + high-frequency + saturated time×area FE; cleanest separations = **H7 > H4 > H2**.

## Recommended execution order (cheapest-decisive first)

1. **H8 leg (b)** — a 2-line FE regression of `dln τ` on `dln Y` (PWT × OWID, fully public). Sharpest EKC-vs-trap discriminator; runnable today. *(If τ falls with income, the trap dissolves — a fast, high-information result.)*
2. **H6 macro anchor** — the paper's literal §6.1 regression on the shared global panel (benchmark; expect b1<0 but **non-discriminating**).
3. **H8 leg (a)** — calibrate the GAP CDF vs p₀ (is the "trap" first- or second-order?).
4. **H7 / H2 cognitive gradient** — the decisive tests; require microdata access (Brazil ENEM public spine first, then chess + firm cognitive-vs-physical arms).
5. **H4 amplification** — the macro wedge, on Title-IV/CAA natural experiments.

## Pre-analysis plan (the commitments that make this credible)

1. **Freeze** the O*NET/PIAAC cognitive-intensity index and the damage-weight vector (EPA-2023 SCC, corrected SC-N₂O) before seeing any outcome.
2. **Pre-register** H7's within-site cognitive-vs-physical contrast and H6-layer-3's γ_cog as the *primary confirmatory estimands*; everything macro is benchmark-only.
3. **Placebo:** simulate EKC-only data (thermo mechanism off, rich-get-cleaner imposed); confirm it reproduces b1<0 but **not** γ_cog<0. If the placebo also yields γ_cog<0, the test fails to discriminate.
4. **Multiple-testing** correction across the battery; report Kleibergen-Paap weak-IV F and Anderson-Rubin CIs for every IV.
5. **Honor the stress-test caveats in every spec:** G1 (τ endogenous via Y), G11 (HALE/inverse-PM₂.₅ are bad controls — downstream of the treatment), F10 (PM₂.₅ is an invalid instrument for H if it reaches TFP via τ).

## What a clean result looks like

- **Supports the paper** iff: γ_cog<0 (pollution hits cognitive work harder) survives saturated FE *and* income controls, the H7 within-worker reversible decrement appears, ψ_total>1 runs through measured TFP, **and** τ is roughly Y-invariant (H8b).
- **Refutes the distinct mechanism** (leaving only ordinary development/EKC) iff: γ_cog≈0, the macro b1<0 is entirely absorbed by an income polynomial, ψ_total≤1, and `d ln τ/d ln Y<0`.
