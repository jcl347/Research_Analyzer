# CLAUDE.md — Research_Analyzer

## Purpose of this repository

`Research_Analyzer` is a workspace for **adversarially reading and stress-testing
research papers**. The unit of work is a single paper (currently a PDF in the repo
root). The deliverable for each paper is a set of structured `context/*.md` files
that (a) faithfully reconstruct what the paper claims and (b) pressure-test those
claims against economic theory, internal consistency, and the empirical record.

The goal is **not** to summarize approvingly. It is to find where the paper is
strong, where it is overstated, where it is internally inconsistent, and where its
central claims would survive or break under scrutiny.

## How Claude should operate in this repo

When asked to analyze the paper, read these context files first and keep them in
sync. Each file has one job. **Do not collapse them into one document** — the
separation is the point: a faithful reading must exist independently of the
critique so the critique can be checked against it.

### Context files (the "dictated" context)

| File | Role | When to read | When to update |
|------|------|--------------|----------------|
| [context/paper-understanding.md](context/paper-understanding.md) | Faithful, neutral reconstruction of the paper: claims, equations, mechanism, scope, what it explicitly disclaims. No critique here. | First, always. It is the ground truth the critique references. | When the source paper changes or a misreading is found. |
| [context/stress-test.md](context/stress-test.md) | The adversarial analysis: failure modes, internal inconsistencies, overstated novelty, weak identification, robustness checks. Each finding cites the specific equation/section it attacks. | After the understanding file. This is the primary deliverable. | Whenever a new angle of attack is found or a finding is verified/refuted. |
| [context/source-map.md](context/source-map.md) | Citation audit: does each external claim (SCC numbers, OECD/IPCC figures, cited elasticities) actually say what the paper says it says? | When verifying the paper's empirical anchors. | When a citation is checked against the literature. |
| [context/paper-fulltext.txt](context/paper-fulltext.txt) | Machine-readable plaintext of the source PDF (extracted via `pdftotext`). Use this to `grep` the paper directly — `pdftoppm`/image rendering is broken on this machine, so the PDF tooling can't render pages. | When you need to quote or locate exact wording in the source. | Only if the source PDF is replaced. |
| [context/hypothesis-tests.md](context/hypothesis-tests.md) | The **testable empirical program**: 8 falsifiable hypothesis specs (H1–H8) derived from the paper's predictions + the unique ζ(H) claim, each with H₀/H₁, identification, and the exact result that rejects it; plus the idea-sharing design-panel synthesis and a pre-analysis plan. Built to survive the stress-test's G12 falsifiability gap. | When designing or running empirical tests of the paper. | When a test is run, a design is refined, or a result comes in. |
| [context/data-sources.md](context/data-sources.md) | Verified data inventory (PWT, OWID/WB CO₂ intensity, WB PM₂.₅, WHO HALE, WDI, EPA SCC) with exact access paths, variable codes, coverage, and *only-sourced* anchor values; the assembled starter table; and the data-integrity hazards. | When acquiring/merging data for a test. | When a source is added or a value verified. |
| [context/results.md](context/results.md) | **Executed** empirical results (real OWID data, FE regressions run in pure numpy): the H8 EKC-vs-trap test and the Ω-gap calibration, reported faithfully (supports the poverty-trap claim, undercuts the advanced-economy trap, and **corrects an over-claim in stress-test F4**). | When citing what the data actually show. | When a new test is executed. |
| [context/analysis/](context/analysis/) | Runnable code — `decoupling_h8.py` (**executed** this session) plus `anchor_regression.R`/`.py` (starter; needs PWT TFP). | When executing or reproducing a test. | When the analysis is run or revised. |
| [context/research-loop/](context/research-loop/) | The **iterative auto-research loop** (Karpathy-style): `framework.md` (design), `data-finetune.md` (4 executed macro probes — 1 EKC confirm + 3 nulls), `iteration-log.md` (the mutate→score→keep/discard trail incl. the red-team killing the first idea), `novel-hypothesis.md` (the converged, stress-test-survived novel mutation). Plus executed scripts (`regime_productivity_test.py`, `thermo_deficit_test.py`). | When evolving/testing a novel mutation of the paper. | When a loop round runs or a probe executes. |

> When new papers are added, mirror this structure: one `paper-understanding`,
> one `stress-test`, one `source-map` per paper (namespace by a short slug if
> more than one paper lives here, e.g. `context/<slug>/stress-test.md`).

## Working rules

1. **Separate reconstruction from critique.** Never let an objection leak into
   `paper-understanding.md`. Never restate the paper uncritically in
   `stress-test.md` — every paragraph there should be doing adversarial work.
2. **Cite the target.** Every stress-test finding names the equation number,
   section, or page it attacks (e.g. "Eq. 18", "§3.4", "Appendix B.3"). A critique
   that can't point at a line in the paper is a vibe, not a finding.
3. **Severity-rank findings.** Tag each as **Fatal / Serious / Minor / Framing**
   so the reader knows what actually threatens the thesis vs. what is presentational.
4. **Steelman before you break.** State the strongest version of the paper's claim,
   then attack that — not a weaker paraphrase.
5. **Distinguish "wrong" from "unsupported" from "overstated."** A reduced-form
   model that admits it is reduced-form is not "wrong"; it may still overclaim
   novelty or bury a units problem. Keep these categories distinct.
6. **Use the model's own notation** (Ω, τ, ϕ, ζ, θ, H, TO) so findings are
   checkable against the paper without a translation layer.

## The paper currently under analysis

**"Thermodynamic Waste, Health Capital, and Long-Run Growth: A Thermo-Ecological
Augmentation of the Solow Model"** — Stuart Greenlee (May 2026), 23 pp.

One-line thesis: augment Solow with a multiplicative *thermo-ecological multiplier*
Ω = ϕ(τ)·ζ(H)·θ(H)^(1−α) ≤ 1 that lowers the steady state by an *amplified* factor
(Ω*)^(1/(1−α)), producing a "thermodynamic growth trap" invisible to conventional GDP.

**Primary question for this analysis: are the ideas novel, and do they hold up?**
Current verdict (see [context/stress-test.md](context/stress-test.md), **verified by a
16-agent adversarial workflow**): **~3/10 novel on the mathematics, ~6/10 on the synthesis.**
The "amplification" `(Ω*)^(1/(1−α))` is the generic Solow/Mankiw–Romer–Weil level effect
(web-verified), and DICE already multiplies output by a damage factor `1 − 0.00236·T²`
(web-verified) — so "amplification absent from DICE" fails, though it *does* survive against
Green Solow (which has no production-side damage multiplier). One genuinely sharp testable
idea survives: ζ(H) implying *measured* TFP can fall while knowledge rises.

The verification both **corrected my own critique** (F6 *refuted* — the health loop is
provably self-correcting; F2–F5 *weakened*) and surfaced a **flagship structural issue I
missed: G1** — because `τ = ‖TO‖/(p₀·Y)` has output in the denominator, Ω is endogenous to Y,
so the "closed-form" steady state Eq. (18) is actually implicit and Prop. 4's elasticity is a
mislabeled partial derivative. **No fatal errors, but G1 is borderline.** Two citation errors
are confirmed: SC-N₂O (~\$54k, not \$5.4k) and the IPCC WGIII↔WGII/Burke–Hsiang–Miguel
mis-attribution.

**Executed empirical test (see [context/results.md](context/results.md)):** real OWID data
splits the paper down the middle — the "thermodynamic growth trap" **dissolves for rich
economies** (they decouple: intensity −2.5%/yr) but **persists for poor economies** (flat
intensity), so the framework is misapplied to advanced economies yet **supports the paper's own
convergence-failure / poverty-trap prediction**. The Ω-gap calibration is magnitude-indeterminate
(3%→40%+), which **corrected an over-claim in stress-test F4**.

See [context/paper-understanding.md](context/paper-understanding.md) for the full neutral
reconstruction, [context/stress-test.md](context/stress-test.md) for the critique +
novelty verdict, and [context/source-map.md](context/source-map.md) for the citation audit.
