# context/results.md — Executed Empirical Results

> **Role:** real, executed analysis (not a plan). Faithful reporting: this evidence
> **supports some** of the paper's claims, **undercuts others**, and **corrects an
> over-claim in my own [stress-test.md](stress-test.md) (F4)**. Test specs are in
> [hypothesis-tests.md](hypothesis-tests.md); data access in
> [data-sources.md](data-sources.md).
>
> **Run environment (honest):** Python 3.14.5 with **only numpy** available
> (pandas/statsmodels/scipy missing; 3.14 wheels unavailable). The two-way fixed-effects
> estimator and cluster-robust SEs were therefore **implemented by hand in numpy**
> (alternating-projection within-transformation; cluster-by-country sandwich). Reproducible
> script: [analysis/decoupling_h8.py](analysis/decoupling_h8.py). Data: OWID `owid-co2-data.csv`
> (Global Carbon Budget + Maddison), downloaded live, 164 countries. **τ here = CO₂/GDP
> only** (territorial), a proxy for the model's full ‖TO‖.

## What was run

| Test | Status | Why it was the right first target |
|------|--------|------------------------------------|
| **H8 leg (b)** — does τ fall as Y rises? | ✅ **RUN** | Cheapest decisive EKC-vs-trap discriminator; fully public data |
| **H8 leg (a)** — is the implied "trap" first- or second-order? | ✅ **RUN** (calibration) | Settles the F4 magnitude dispute |
| H6 anchor (τ,H → TFP) | ⛔ not run | Needs PWT TFP (`.xlsx`/`.dta`); blocked by missing pandas/openpyxl on Py 3.14 |
| H7/H2 cognitive gradient | ⛔ not run | Requires microdata access (Brazil ENEM, chess, firm panels) |

## Identification caveat, confirmed empirically

The naive H8b regression `dln(τ) ~ dln(Y)` is **mechanically `β_emissions − 1`** because
τ = CO₂/GDP puts GDP on both sides (stress-test **G1/G2**). Verified in the data: the naive
coefficient came out **−0.68 = β−1** exactly. So the naive test is **uninformative** — the
real estimand is the **emissions–output elasticity β** from `dln(CO₂) ~ dln(GDP)` (which
does *not* have GDP on both sides), plus the descriptive intensity trend. This is exactly
what the design panel's identification-skeptic warned.

## H8b results — emissions–output elasticity β and intensity trend (two-way FE, cluster-by-country)

| Window | N | β (emissions) | rel. decoupling (β<1)? | mean `dln(τ)` | share country-yrs τ **falling** |
|--------|---|---------------|------------------------|---------------|----------------------------------|
| Full 1821+ | 14,268 | 0.31 (.14) | yes | **+1.12%/yr** | 51.6% |
| 1971+ | 8,143 | 0.26 (.21) | yes | −0.73%/yr | 57.8% |
| 1990+ | 5,244 | 0.17 (.31) | yes | −1.22%/yr | 60.9% |
| 2000+ | 3,608 | 0.54 (.08) | yes | −1.32%/yr | 61.9% |
| **1990+ RICH half** | 2,621 | −0.23 (.51)¹ | yes | **−2.49%/yr** | **70.4%** |
| **1990+ POOR half** | 2,623 | 0.55 (.11) | yes | **+0.04%/yr** | 51.5% |

*(SE in parentheses. ¹ Rich-half β point estimate is absolute decoupling but is imprecise (SE .51); the robust statement for the rich half is the descriptive trend −2.49%/yr / 70% falling.)*

**The headline pattern is a textbook Environmental Kuznets Curve gradient:** rich economies
**decouple** (intensity falling ~2.5%/yr, falling in 70% of country-years); poor economies
**do not** (intensity flat at +0.04%/yr, a coin-flip 51.5%). Over the full historical panel
intensity actually **rose** (+1.1%/yr) — there is no universal automatic decoupling.

### What H8b means for the paper (faithful, two-sided)

- **Undercuts the secular-stagnation-in-advanced-economies framing.** For rich countries τ
  falls robustly with income, so Ω → 1 and **the "thermodynamic growth trap" dissolves along
  the balanced growth path** — exactly the mechanism stress-test **G2** described. The paper's
  premise that τ is a "slow exogenous state" is **false for advanced economies.**
- **Supports the convergence-failure / environmental-poverty-trap prediction (P5, §3.6).**
  For poor countries τ is *flat* — it does **not** decouple — so the waste drag persists and
  the trap premise is **most tenable exactly where the paper claimed a poverty trap.** This is
  genuine supporting evidence for one of the paper's two headline hypotheses.
- **Net:** the framework is **misapplied to rich economies but defensible for poor ones** — a
  refinement the paper does not draw but the data support. (Caveat: rich-country territorial
  decoupling partly reflects **offshoring** of dirty production to poor countries; consumption-
  based τ would show weaker rich-country decoupling and strengthen this caveat.)

## H8a results — is the implied "trap" first- or second-order? (calibration)

Implied steady-state output gap `1 − (Ω*)^(1/(1−α))` from the **waste drag** alone (α=0.3):

| τ | ψ=1 | ψ=2 | ψ=3 |
|---|-----|-----|-----|
| 0.02 | 2.8% | 5.6% | 8.3% |
| 0.05 | **7.1%** | 13.6% | 19.7% |
| 0.10 | 14.0% | 26.0% | 36.3% |
| 0.20 | 27.3% | 47.1% | 61.6% |
| 0.30 | 39.9% | 63.9% | 78.3% |

**Health drag** alone, representative `H/H̄ = 58/74 = 0.784` (high-pollution HALE vs
pollution-free): combined elasticity 0.5 → **16%**, 1.0 → **29%**, 1.5 → **41%**.

### ⚠ This corrects my own stress-test (F4)

stress-test **F4** asserted the effect is *"almost certainly second-order … Ω ≈ 0.85–1.0."*
**The calibration shows that was an over-claim.** Even at the stress-test's *own* representative
τ=0.05 with ψ=1, the waste-drag gap is **7%** (not <5%), and the **health-drag channel can be
16–41%** for a country with a realistic HALE deficit. The honest conclusion (matching the
verification workflow's "weakened" verdict on F4): **the magnitude is genuinely indeterminate**
— anywhere from ~3% to >40% depending on the **unidentified normalization price p₀** (which sets
τ; stress-test **G3**), the **uncalibrated convexity ψ**, and the **health-elasticity**. So:
the paper's dramatic rhetoric is *unsupported by conservative parameters* but **not refuted** —
and under moderately aggressive (still defensible) parameters the trap **is** first-order. F4 is
hereby downgraded from "second-order" to **"magnitude indeterminate; pivots entirely on the
unidentified p₀/ψ/health-elasticity."**

## Net verdict on H8 (the only family executed)

| Leg | Result | Bears on |
|-----|--------|----------|
| H8b (rich) | τ decouples (−2.5%/yr) | **Against** the trap for advanced economies (G2) |
| H8b (poor) | τ flat (+0.04%/yr) | **For** convergence-failure/poverty-trap (P5) |
| H8b (naive) | = β−1 mechanically | Confirms G1/G2 — naive test uninformative |
| H8a | gap = 3%→40%+, set by unpinned p₀/ψ/health | Magnitude indeterminate; **corrects F4** |

## Honest limitations of what was run

1. **τ = CO₂/GDP only** (territorial), not the model's full damage-weighted ‖TO‖; consumption-based emissions would weaken rich-country decoupling.
2. **Reduced-form / descriptive**, not causal — no instrument for Y-growth (the panel wanted a Bartik export-demand IV; not implemented). This is the H8b *descriptive-elasticity* leg, appropriately labeled.
3. **Income split is a crude median split** on mean GDP-per-capita; not a formal interaction with inference.
4. **H6 (the §6.1 anchor on TFP) was not run** — it needs PWT TFP, blocked by the Py-3.14/no-pandas environment. To run it: `pip install pandas pyreadstat` (or read `pwt100.dta`), then [analysis/anchor_regression.py](analysis/anchor_regression.py).
5. **The decisive tests (H7/H2 cognitive gradient) remain unrun** — they need microdata access and are where the framework actually stands or falls (per the panel consensus).

## Bottom line

Real data, honestly run, **split the paper down the middle**: its trap mechanism **dissolves
for rich economies** (they decouple — undercutting the secular-stagnation framing and confirming
stress-test G2) but **persists for poor economies** (they don't decouple — supporting the
paper's own convergence-failure prediction). And the calibration shows the trap's **magnitude
is not pinned down by anything in the model** — correcting my earlier "second-order" claim. The
verdict the framework actually earns is **conditional**: a real but parameter-sensitive drag that
matters most for non-decoupling developing economies, not the universal "thermodynamic growth
trap" the abstract advertises.
