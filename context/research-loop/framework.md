# context/research-loop/framework.md — The Auto-Research Orchestration Loop

> **Role:** the design of the iterative, multi-agent hypothesis-development loop used to
> evolve a *novel* research idea out of the analysis in [../](../). Modeled on Andrej
> Karpathy's **autoresearch** (github.com/karpathy/autoresearch). All initial analysis is
> **kept intact**; this loop is purely additive and lives under `context/research-loop/`.

## What Karpathy's autoresearch does (the template)

A minimal autonomous-optimization cycle:

> **edit one artifact → run for a fixed budget → measure one comparable metric → keep or discard → repeat**

- The agent modifies **a single file** (`train.py`); the human only writes `program.md` (the brief).
- Each experiment has a **fixed time budget** (≈5 min) so ~100 iterations run overnight.
- A **single, fair metric** (`val_bpb`, vocabulary-independent) makes every change comparable.
- The agent **keeps or discards** each change based on the metric — greedy hill-climbing — and
  leaves a **log** of experiments. "You wake up to a log and (hopefully) a better model."

## The adaptation here (hypothesis-as-artifact)

We keep the control flow and swap the artifact and metric: the **hypothesis statement** is the
single artifact; each "run" is a novelty-check + test-design + (real) data probe; the metric is a
fixed composite score. One concrete **mutation** per iteration, kept only if it beats the incumbent.

| Karpathy autoresearch | This loop |
|-----------------------|-----------|
| Artifact = `train.py` (one file) | Artifact = **the hypothesis statement** (one paragraph) |
| `program.md` (human brief) | The **research brief** (goal + the two grounding findings: ζ(H) + the EKC regime split) |
| Edit `train.py` | **Mutate**: one concrete improving change to the incumbent (an "Ideator" agent) |
| Train 5 min | **Run**: novelty-check (web) + decisive-test design (+ a real data probe by the main loop) |
| Measure `val_bpb` | **Measure**: composite score = Novelty + Testability + EmpiricalSupport + DistinctnessFromEKC + PolicyRelevance (each 0–10; total 0–50) |
| Keep/discard on metric | **Keep/discard** vs incumbent total (greedy hill-climb) |
| Experiment log | **Iteration log** ([iteration-log.md](iteration-log.md)) + memory passed forward to avoid repeats |

### The single fair metric (analog of `val_bpb`)

`total = Novelty + Testability + EmpiricalSupport + DistinctnessFromEKC + PolicyRelevance`,
each 0–10, graded harshly. The **DistinctnessFromEKC** dimension is the load-bearing one: it
forces every candidate past the skeptic's null ("rich economies are just cleaner *and* more
productive"), which is exactly the falsifiability gap (G12) that sank the original paper's
broad predictions. An idea only scores high if a skeptical economist **could not** reproduce
its key prediction from ordinary development.

## Control flow (deterministic loop, model-driven steps)

Implemented as a `Workflow` (deterministic for-loop; agents do the creative work):

```
incumbent ← seed hypothesis (the ζ(H) regime-conditional cognitive-TFP drag), baseline score 30/50
memory ← []
for k in 1..K:                              # K=5 here; Karpathy runs ~100
    candidate ← Ideator(incumbent, memory)  # ONE concrete mutation (the "edit")
    novelty   ← NoveltyChecker(candidate)   # web search vs literature (the "run")
    design    ← TestDesigner(candidate)     # decisive falsifiable test + data
    score     ← Reviewer(candidate, novelty, design, incumbent)   # the metric
    keep ← score.total > incumbent.score.total                    # keep/discard
    if keep: incumbent ← candidate(+design+score)
    memory.push({mutation, total, kept})    # log; do-not-repeat
return incumbent, memory                     # converged idea + experiment log
```

### Roles (agents)

- **Ideator** — proposes one improving mutation, forbidden from repeating logged mutations.
- **Novelty checker** — web-searches the literature; returns closest prior work + what is genuinely new.
- **Test designer** — the single most decisive feasible test, with an exact falsifier.
- **Reviewer** — the harsh grader producing the comparable composite score.
- **(Main loop / human-in-the-loop)** — supplies the brief, and **executes real data probes** between iterations to feed `EmpiricalSupport` with actual coefficients (see [data-finetune.md](data-finetune.md)).

## Design principles carried over

1. **One change at a time** — keeps each step reviewable and the metric attributable (Karpathy's scope constraint).
2. **One comparable metric** — no moving goalposts; greedy hill-climbing on the total.
3. **Bounded budget per step** — one novelty-check + one test design + one data probe (not an open-ended search).
4. **Memory / log** — every mutation recorded with its score and keep/discard, so the loop doesn't cycle.
5. **Human sets the brief, not the moves** — the brief fixes the goal and the grounding evidence; the agents evolve the idea.

## Differences from the original (and why)

- **Real metric, not a proxy:** unlike `val_bpb`, our score is partly subjective (a reviewer LLM),
  so we anchor `EmpiricalSupport` with **executed** data probes (real regression coefficients), not
  vibes — the main loop runs a fresh test each round and feeds the result back.
- **Fewer iterations, deeper steps:** K=5 (not ~100), because each "run" is a literature check + a
  designed experiment rather than a 5-minute training job.
- **Adversarial grading:** the DistinctnessFromEKC axis is an explicit adversary, mirroring the
  stress-test discipline used on the original paper.

## Outputs

- [iteration-log.md](iteration-log.md) — the per-iteration mutate/score/decide trace (the "experiment log").
- [novel-hypothesis.md](novel-hypothesis.md) — the converged novel research idea + its decisive test.
- [data-finetune.md](data-finetune.md) — the real data probe(s) that fine-tuned the idea.
