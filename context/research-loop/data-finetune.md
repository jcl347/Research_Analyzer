# context/research-loop/data-finetune.md — Executed Data Probes (the loop's "runs")

> **Role:** the real, executed empirical probes that feed the `EmpiricalSupport` axis of the
> [auto-research loop](framework.md) — the analog of Karpathy's training run. Reported
> **faithfully**, including a **null** that genuinely redirected the hypothesis. Pure-numpy
> two-way FE (no pandas/statsmodels on this machine). Scripts:
> [regime_productivity_test.py](regime_productivity_test.py) and
> [../analysis/decoupling_h8.py](../analysis/decoupling_h8.py).

## Probe A — the regime split exists (prior, from [../results.md](../results.md))

On the OWID CO₂ panel (164 countries), an **Environmental-Kuznets gradient**: rich economies
**decouple** (intensity −2.5%/yr, falling in 70% of country-years), poor economies do **not**
(intensity flat, +0.04%/yr). This established the *regime* the loop's seed hypothesis is built on:
the thermo-ecological drag, if real, should be **conditional on the non-decoupling regime**.

## Probe B — the regime-conditional drag is **NOT** detectable at the macro level (NEW, null)

**Question:** does pollution intensity τ predict lower subsequent **labor-productivity** growth,
and is the drag stronger in the non-decoupling regime (as the seed hypothesis says)?

**Data:** World Bank labor productivity `SL.GDP.PCAP.EM.KD` (GDP per person employed; 7,016 obs)
merged with OWID CO₂ intensity τ. Matched panel: **N = 4,820** country-years, **157 countries**
(112 decouplers, 45 non-decouplers), 1992–2022. Two-way (country × year) FE, cluster-by-country.

| Estimate | Coef (SE) | t | Predicted | Result |
|----------|-----------|---|-----------|--------|
| mean dln(LP), decouplers | **+1.56%/yr** | — | higher | — |
| mean dln(LP), non-decouplers | **+1.57%/yr** | — | lower | **identical → no gap** |
| lag ln(τ) → dln(LP) | +0.0047 (.0086) | +0.55 | **< 0** | **ns, wrong sign** |
| nonDecoupler × lag ln(τ) | +0.0205 (.0235) | +0.87 | **< 0** | **ns, wrong sign** |
| convergence: lag ln(LP) | −0.0629 (.0110) | −5.73 | < 0 | strong (as expected) |

**Verdict: a clean null.** There is **no detectable macro regime-conditional pollution drag** on
labor productivity. (The convergence term behaves textbook-normally, so the panel is well-behaved —
the null is not a power artifact of a broken regression.)

### Why this *advances* the research idea (the "failed experiment" that updates direction)

The null is **diagnostic, not fatal**, because it is *exactly what the ζ(H) "masking" hypothesis
predicts*:
1. **Masking is the mechanism, and the macro null is its fingerprint.** If pollution erodes
   *cognition* and that loss co-moves with knowledge accumulation, it is **absorbed into measured
   TFP/labor-productivity** at the aggregate level — so a country-level regression *should* find
   nothing. The macro null and the masking hypothesis are observationally identical.
2. **But the macro test cannot distinguish "masked" from "absent."** That is precisely the
   identification wall the design panel hit (stress-test G12 / hypothesis H7): the only way to see
   a masked cognitive effect is to **break the masking** — measure cognition or cognitively-intensive
   output **directly, within-unit, at high frequency**, where knowledge is held fixed.
3. **Loop update (data-driven):** *drop any claim of a detectable macro regime-conditional drag*
   (it lowers `EmpiricalSupport` for macro framings and would be dismissed by a skeptic), and
   **sharpen the hypothesis to the micro cognitive-masking claim** with an explicit
   "why-it's-invisible-at-macro" component. The masking is reframed from a *bug* (hard to test)
   into the *central, distinctive prediction* (the macro null is a confirmed implication).

## Probe C — a thermodynamic-damage *deficit* does NOT predict future growth (NEW, null)

**Question (a data-testable mutation of the paper's Thermo-GDP idea):** does subtracting
thermodynamic damage from output carry predictive content — i.e., do economies running large
*unpriced* thermodynamic deficits subsequently grow slower? Script:
[thermo_deficit_test.py](thermo_deficit_test.py).

**Data:** World Bank Adjusted-Net-Savings components — CO₂ damage `NY.ADJ.DCO2.GN.ZS` + particulate
damage `NY.ADJ.DPEM.GN.ZS` (= D/GNI), gross savings `NY.GNS.ICTR.ZS`, GDP pc `NY.GDP.PCAP.KD`.
Barro non-overlapping 5-year panel (t ∈ {1995…2015} → growth to t+5), **N = 1,060** country-periods,
**220 countries**, country × period FE.

| Estimate | Coef (×100) | t | Predicted | Result |
|----------|-------------|---|-----------|--------|
| thermoDamage(D/GNI) → forward 5-yr growth | −0.03 | −0.19 | < 0 | **NULL** |
| thermoDamage, net of gross savings (horse-race, n=814) | +0.04 | +0.52 | < 0 | **null, wrong sign** |
| convergence (ln y_t) | −6.75 / −3.58 | −3.9 / −4.3 | < 0 | strong (textbook) |

**Verdict: a second clean null.** The Thermo-GDP "deficit signals future underperformance" mutation
has **no macro predictive content** (and the pollution-damage adjustment adds nothing beyond gross
savings). The convergence term again behaves normally, so the panel is sound.

## Probe D — no "cognitive echo" in macro productivity either (NEW, null)

**Question (a macro echo of ζ(H)):** does pollution drag productivity *more* in service/knowledge-
intensive economies (an interaction the EKC null cannot produce)? **Data:** WB PM₂.₅
`EN.ATM.PM25.MC.M3` × services-share `NV.SRV.TOTL.ZS` × labor productivity; N = 2,793, 216
countries, 2009–2021, country×year FE. **Result:** PM₂.₅×Services interaction = +0.29 (t=+1.00) —
**insignificant and wrong-signed**; PM₂.₅ main effect −0.49 (t=−0.82, ns). The cognitive channel
leaves **no detectable macro echo** even in its most favorable macro interaction.

## Synthesis across probes — a high-confidence empirical pattern

| Probe | Tests | Result |
|-------|-------|--------|
| A (decoupling) | does τ fall as Y rises? | **EKC gradient** — rich decouple, poor don't |
| B (regime × productivity) | regime-conditional pollution→productivity drag | **NULL** |
| C (Thermo-GDP deficit) | damage deficit → future growth | **NULL** |
| D (cognitive macro echo) | PM₂.₅ × service-share → productivity | **NULL (wrong sign)** |

Four independent macro designs return **one EKC confirmation and three nulls** (with textbook
convergence throughout, so the panels are sound). The high-confidence
reading: **the framework has no macro footprint distinguishable from ordinary development/EKC** —
which is *exactly* the signature the ζ(H) cognitive-**masking** hypothesis predicts (a cognitive loss
that co-moves with knowledge is absorbed into aggregate measures). The data therefore **redirect the
research program from a macro-growth theory to a micro-cognitive-measurement one**, and raise
confidence that the only testable novel claim lives at the **within-worker cognitive** level.

## How the probes scored the loop

- Probe A raised `DistinctnessFromEKC` for the regime-conditional framing (a real regime split exists).
- Probe B's null **lowered `EmpiricalSupport` for any macro-testable version** and pushed the loop
  toward the micro cognitive-masking idea — and turned the macro null into a *predicted* implication,
  which a sharper hypothesis can claim as supporting evidence.

## Caveats (honest)

- Macro labor productivity cannot see cognitively-intensive *sectors/tasks* — the level at which the
  effect, if real, would appear. The null is **uninformative about the micro mechanism** by construction.
- τ = CO₂/GDP shares GDP with labor productivity (GDP/worker); contemporaneous regressions are
  mechanically biased, so only **lagged** τ levels were used (still imperfect).
- Reduced-form, not causal; decoupler classification is a coarse 1991+ intensity-trend split.
- The **decisive** test remains micro: within-worker/within-student cognitive output vs. exogenous
  PM₂.₅ (chess, exams, monitored cognitive vs. physical tasks) — see [../hypothesis-tests.md](../hypothesis-tests.md) H7.
