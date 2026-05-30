# context/research-loop/novel-hypothesis.md — Converged Novel Mutation (post red-team)

> **Status:** converged through the [auto-research loop](framework.md) → four executed data
> probes ([data-finetune.md](data-finetune.md)) → a **team red-team that killed the first
> version** ([stress-test](#red-team-outcome), run `wf_46fb5555`). This file states only what
> **survives** that adversarial pass. Initial analysis in [../](../) is unchanged.
>
> **Two-line honesty header (the red-team's non-negotiable demand):** the macro nulls are
> **motivation only — necessary-but-not-sufficient.** A macro null is produced by masking, by
> *no effect at all*, by τ=CO₂/GDP mismeasurement, and by low power alike; it carries **zero**
> confirmatory weight. Nothing here claims the cognitive mechanism is confirmed.

## What the loop killed (and why that's the loop working)

The loop first converged on a **"cognitive-masking reformulation"** (pollution erodes cognition →
masked in aggregate TFP → the macro nulls are its *signature*). The red-team **killed it** on two
grounds:
1. **Logic (wounded→killed):** reading the nulls as the masking signature is **affirming the
   consequent**. The repo's own files already concede this ([data-finetune.md](data-finetune.md):
   "the macro test cannot distinguish 'masked' from 'absent'"; [stress-test.md](../stress-test.md)
   G12: "no measurement discriminates the mechanism"). Four designs returning the same null are
   four measurements of one unidentified object, not four independent tests.
2. **Novelty (KILLED):** every pillar is already published — pollution→cognition→measured
   productivity (Chang, Graff Zivin, Gross & Neidell; **Ebenstein et al., PNAS 2018**); the
   within-worker exogenous-PM₂.₅ cognitive test (**Künn, Palacios & Pestel 2023**, ~30k chess
   moves — *already executed*, so it is **prior work, not a "future decisive test"**); the
   TFP-measurement-bias / masking idea (**De Ridder, *Emissions-Adjusted TFP*, 2025**;
   green-TFP/green-accounting); cognitive human-capital depreciation distinct from mortality (OLG
   pollution-growth models). The masking reframe is a relabeling of the known TFP-vs-human-capital
   non-identification in development accounting.

## What survives — the genuinely novel mutation

The red-team's own "only potentially-novel residual" points to a sharp, real gap:

> ### "Cognitive capital is a *stock*, but the entire evidence base is a *flow*."
>
> Stu's ζ(H) makes **H a stock** — cognitive capital that accumulates and **depreciates**, with
> *permanent* growth consequences (that is the whole point of putting it in a Solow multiplier).
> But **every** causal estimate in the literature (Künn chess, Chang call-centers, Graff Zivin
> pear-packers, Ebenstein) identifies a **transient, reversible flow**: you breathe dirty air
> today, you err more today, you **recover when the air clears**. A reversible daily tax **cannot
> generate Stu's mechanism** — it does not lower the long-run cognitive *stock*. **No one has
> separated the chronic stock-depreciation channel from the acute reversible flow in the
> productivity/TFP context.**

**The novel research question (a genuine mutation of Stu's paper, not a new topic):**
*Is there a cognitive-capital **stock-depreciation** effect of chronic pollution exposure — a
persistent, slow-to-reverse downward shift in productive cognition — net of the acute reversible
flow?*
- **If yes:** Stu's growth mechanism has its missing foundation, and one can finally calibrate the
  *stock* depreciation rate δ_cog that his Ω-multiplier silently assumes.
- **If the effect is entirely flow:** Stu's model is **misspecified at its core** — a
  stock-depreciation growth theory built on flow-based evidence — a sharp, novel, *falsifying*
  critique of the framework.

Either outcome is a publishable contribution, and **neither is in the cited prior work**: the
epidemiology of chronic PM₂.₅ → cognitive decline (dementia; prenatal/childhood) exists but is
**not framed as productivity-relevant cognitive-capital depreciation** and **not decomposed
against the acute flow** in an economics/TFP setting. The **stock-vs-flow decomposition in the
productivity context is the white space.**

### Why it escapes the EKC null (distinctness)

A chronic within-cohort *accumulation* effect on cognition is not "rich economies are cleaner."
It is identified from **longitudinal exposure history**, not cross-country income levels, and the
acute-flow control + EKC-only placebo are built into the design below.

## The decisive (pre-registered, currently UNRUN) test

Per the red-team, the standard within-day design is **not** decisive (it re-identifies the
published *flow*). The novelty-bearing design must:
1. **Chronic-exposure cohort** isolating persistent cognitive deficits **net of acute episodes**
   (stock, not reversible flow) — e.g., long-run residential PM₂.₅ history linked to repeated
   engine-verified cognitive performance, controlling for same-day exposure.
2. **Co-located within-firm cognitive-vs-physical task panel** (not a cross-study
   call-center-vs-pear-packer comparison), PM₂.₅ orthogonalized to heat and co-pollutants.
3. A **pre-specified symmetric effect-size band** (replacing the near-untrippable
   CI-contains-zero ∧ point-estimate < ⅓-benchmark falsifier).
4. An **EKC-only placebo**: simulate development-driven data with the channel off; confirm it does
   **not** reproduce the chronic effect.

**Confirms** the mutation iff the chronic (stock) deficit is non-zero **net of** the acute flow and
the placebo is clean. **Refutes** (and falsifies Stu's stock mechanism) iff the effect is entirely
acute/reversible.

## Confidence (calibrated, per the verdict)

| Claim | Confidence | Basis |
|-------|-----------|-------|
| The framework has **no macro footprint** beyond EKC/development | **High** | 4 independent designs, textbook convergence intact |
| The aggregate "thermodynamic growth trap" is **not identified** and should be withdrawn/qualified | **High** | follows from the above + F1/G1 |
| The **stock-vs-flow gap** is real and unaddressed in the productivity literature | **Medium-High** | red-team novelty scan; the cited evidence is all flow |
| The cognitive **stock-depreciation mechanism is real** | **Untested** | needs cohort microdata; not reachable with public macro data |

**Net:** this is an **honest negative-result-plus-novel-hypothesis note** — a measurement /
identification contribution — **not** a confirmed positive discovery. The macro nulls explain *why
prior macro work found nothing*; the novel, testable, EKC-proof question is the **stock-vs-flow
decomposition of the cognitive channel.**

<a name="red-team-outcome"></a>
## Red-team outcome (run `wf_46fb5555`, 5 agents)

| Angle | Verdict |
|-------|---------|
| nulls-don't-prove-masking | **WOUNDED** — affirming the consequent; nulls are non-informative between masking/no-effect |
| prior-work | **KILLED** — all pillars published (Chang/GZ/Neidell, Ebenstein 2018, Künn 2023, De Ridder 2025, OLG models) |
| falsifiability-and-power | **WOUNDED** — no MDE computed; nulls may be underpowered, not clean |
| is-it-just-EKC-relabeled | **WOUNDED** — masking relabels the EKC null; decisive micro test already exists |
| **Final verdict** | A **negative-result + measurement-note**, confidence **high for the negative result**, **not** a novel positive theory — *unless* recast to the **stock-vs-flow** residual above. |

*Required edits the red-team imposed (all applied here): strip every word where nulls "confirm/
support/are the signature of" masking; cite the prior work as prior; demote masking to motivation;
flag that MDEs are not computed so "null" means "uninformative," not "absent."*
