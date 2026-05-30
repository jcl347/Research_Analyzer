# context/research-loop/iteration-log.md — The Auto-Research Experiment Log

> The Karpathy-style log of the loop ([framework.md](framework.md)): each row is a mutation
> ("edit"), what was run, the single comparable metric, and the keep/discard decision.
> The decisive event is **the red-team killing the converged idea on novelty + logic**, which
> redirected the loop to the surviving residual. Faithful — including the failures.

## Metric

`score = Novelty + Testability + EmpiricalSupport + DistinctnessFromEKC + PolicyRelevance`, each
0–10. The load-bearing axis is **DistinctnessFromEKC** (must escape "rich economies are cleaner
and more productive"). A mutation is **kept** only if it beats the incumbent total.

## Log

| # | Mutation ("edit") | Run / evidence | Outcome |
|---|-------------------|----------------|---------|
| 0 | **Seed:** ζ(H) cognitive-TFP drag, regime-conditional on (non-)decoupling | prior stress-test; baseline 30/50 | incumbent |
| A | (data run) does τ fall as Y rises? | OWID, 164 ctry, FE | **EKC gradient** — rich decouple, poor don't (the regime split is real) |
| B | (data run) regime × pollution → labor productivity | WB labprod × OWID, 157 ctry | **NULL** (t=0.87, wrong sign) |
| C | (data run) Thermo-GDP damage deficit → future growth | WB ANS, Barro 5-yr, 220 ctry | **NULL** (t=−0.19) |
| D | (data run) PM₂.₅ × service-share → productivity | WB PM₂.₅ × services, 216 ctry | **NULL** (t=1.0, wrong sign) |
| 1 | **Mutation:** "cognitive-MASKING reformulation" — the macro nulls are the *signature* of cognitive masking | red-team `wf_46fb5555` (5 agents) | **DISCARDED** — see below |
| 2 | **Mutation (survivor):** "cognitive capital is a *stock*, the evidence is a *flow*" — separate chronic stock-depreciation from the acute reversible flow | red-team residual + novelty scan | **KEPT** — the genuinely novel question |

## The decisive round (mutation #1 → #2)

**Mutation #1 ("masking reformulation")** scored high on policy/testability but the red-team drove
its **Novelty and DistinctnessFromEKC to near-zero**:
- **Novelty KILLED:** every pillar is published — Chang/Graff Zivin/Gross/Neidell; Ebenstein et al.
  (PNAS 2018); **Künn–Palacios–Pestel 2023** (the chess test I had proposed *already exists*);
  **De Ridder, Emissions-Adjusted TFP (2025)** (the masking/measurement-bias idea); OLG cognitive-
  depreciation models.
- **Logic WOUNDED:** "macro nulls confirm masking" is affirming the consequent — the repo itself
  concedes the nulls can't separate masked from absent. Net score **fell below the incumbent →
  discarded** as a *positive* claim (it survives only as a high-confidence **negative result**).

**Mutation #2** is the residual the red-team itself pointed to and the only piece that clears the
novelty bar: the **stock-vs-flow decomposition of the cognitive channel** (see
[novel-hypothesis.md](novel-hypothesis.md)). Stu's ζ(H) is a *stock* (it depreciates, with growth
consequences); all existing causal evidence is a reversible *flow*. Separating them — or showing
the effect is *entirely* flow (which would **falsify** Stu's mechanism) — is unaddressed in the
productivity/TFP literature and escapes the EKC null (longitudinal within-cohort identification).

## Converged state (what "high confidence" attaches to)

- **High confidence (tested):** the framework has **no macro footprint** beyond EKC/development
  (4 designs); the aggregate "growth trap" is **not identified**. *(This is the publishable kernel.)*
- **Medium-high confidence (validated as novel, untested):** the **stock-vs-flow** question is the
  genuine novel mutation; the mechanism itself is **unconfirmed** (needs cohort microdata).
- **Explicitly retracted:** any claim that the nulls *support* masking.

## Honest stopping condition

Further **macro** iteration cannot confirm the mechanism (it is micro by construction), so the loop
**stopped** at the point where the novel question is sharply stated, stress-test-survived for
novelty, and gated on a pre-registered cohort experiment that public macro data cannot run. The
two broader idea-generation runs (`wu74myokc` hill-climb, `wdk8efee0` team) were still executing at
write-time; their proposals will be appended to a `novel-approaches.md` if they add beyond the
stock-vs-flow residual.
