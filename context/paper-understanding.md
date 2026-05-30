# context/paper-understanding.md — Faithful Reconstruction

> **Role:** Neutral, charitable reconstruction of the paper. **No critique here.**
> Objections live in [stress-test.md](stress-test.md). This file is the ground
> truth that the critique points back at. Notation matches the paper exactly.

## Bibliographic record

- **Title:** *Thermodynamic Waste, Health Capital, and Long-Run Growth — A Thermo-Ecological Augmentation of the Solow Model*
- **Author:** Stuart Greenlee, M.A. (Economics), Independent Researcher
- **Date:** May 2026 · 23 pp. · single-author working paper
- **JEL:** O44 (growth & environment), Q56 (environment & development), E13, Q57 (ecological economics)
- **Acknowledgement of note:** the author states LLM tools were used for drafting/editing; all claims and errors are the author's.

## One-paragraph thesis

Production is a physical throughput process that unavoidably generates thermodynamic
waste (Second Law). Standard Solow ignores this. The paper bolts three coupled state
variables onto Solow — physical thermodynamic output **TO**, health capital **H**,
and natural capital **R** — and folds their effect into a single multiplicative
**thermo-ecological multiplier** Ω that scales the production function. Because Ω
multiplies output, it propagates through capital accumulation and lands in the steady
state with an **amplified** exponent 1/(1−α). When waste is positive and health is
below baseline, Ω < 1, so the economy converges to a permanently lower balanced growth
path — the **"thermodynamic growth trap"** — which is invisible in conventional GDP and
only visible in a damage-adjusted measure the paper calls **Thermo-GDP**. The model is
explicitly designed to nest standard Solow exactly when environmental costs are zero
(Ω = 1).

## The causal chain (the spine of the model)

```
Production  →  Physical TO (waste flows)  →  Shadow-priced damage D  →  Health effects (H↓)  →  feedback to Production
```

Two feedback arrows close the loop in Figure 1:
- **Left (orange):** more output can raise TO intensity (depends on tech & energy mix).
- **Right (green):** lower health reduces productivity and output, further eroding health.

## State variables & definitions

| Symbol | Name | Definition / units | Eq. |
|--------|------|--------------------|-----|
| **TO** = (E, P, M) | Physical thermodynamic output | Vector of **physical** waste flows: E = energy waste (J), P = pollution emissions (t CO₂e, PM₂.₅, NOₓ, SO₂…), M = material waste (t). *Explicitly NOT damage.* | (2) |
| **τ** | TO intensity | τ ≡ ‖TO‖ / (p₀·Y); dimensionless, bounded [0,1]. ‖TO‖ is a damage-equivalence-weighted norm (e.g. GWPs); p₀ is a fixed normalization price. "Production-side cleanliness," not inflated by cleanup spend. | (3) |
| **D** | Monetized damage | D = λ′·TO = λₑE + λₚP + λₘM, $/period. Shadow prices λ from social-cost literature. Health damage is a **subset** of D, not additive to it. | (4) |
| **X** | Per-capita exposure | X = κ·P / Pop. Depends on **physical** pollution P, not on monetized damage. | (5) |
| **H** | Health capital | Stock: productive capacity of population health (labor + cognition). | (6) |
| **R** | Natural capital | Renewable resource stock with logistic regeneration. | (10) |
| **Ω** | Thermo-ecological multiplier | Ω = ϕ(τ)·ζ(H)·θ(H)^(1−α); 0 < Ω ≤ 1 when damages positive. | (11) |

## The mechanism, equation by equation

**Production (4-factor, nests Cobb–Douglas):**
$$Y = A·K^α·L^β·U^u,\quad α+β+u=1 \tag{1}$$
U = useful exergy (primary exergy × conversion efficiency f). Justified by Ayres–Warr
(exergy resolves much of the Solow residual) and Santos et al. (exergy output
elasticities 0.29–0.46). **For the core model the paper drops to two factors**,
Y = A K^α (AL)^(1−α), treating exergy as embedded in TFP.

**Damage valuation anchors:** EPA 2023 SCC ≈ \$190/tCO₂ @ 2% discount; Rennert et al.
2022 ≈ \$185/tCO₂; methane ≈ \$1,600/tCH₄; N₂O ≈ \$5,400/tN₂O; PM₂.₅ via mortality/morbidity.

**Health dynamics:**
$$\dot H = η₀ + η₁h − δ_h H − χX \tag{6}$$
η₀ = baseline medical/sanitation progress; h = preventive health spend / Y; δ_h = natural
depreciation; χX = damage from exposure. Steady state H* = (η₀ + η₁h* − χX*)/δ_h.

**Health enters production through TWO channels:**
$$L^{eff} = L·θ(H),\quad A^{eff} = A·ζ(H) \tag{7}$$
θ(H) = (H/H̄)^b (labor quality); ζ(H) = (H/H̄)^m (TFP/cognition); b, m > 0; at H = H̄ both = 1.
The TFP channel ζ(H) is floated as a **testable contributing mechanism for the
productivity slowdown**: if pollution erodes cognition, *measured* TFP can fall even as
knowledge accumulates.

**Sustainability multiplier (axiomatic):**
$$ϕ(τ) = (1−τ)^ψ,\quad ψ>0 \tag{9}$$
Required axioms: (A1) ϕ(0)=1; (A2) strictly decreasing in τ; (A3) convex; (A4) ϕ→0 as
τ→ upper bound. (1−τ)^ψ is "the simplest" family satisfying all four. ψ tunes convexity
(ψ<1 gentle, =1 linear, >1 steep). **Qualitative results claimed robust to any
decreasing-convex ϕ with ϕ(0)=1.** ϕ depends only on τ (not restoration spend), which the
paper says fixes a "perverse-incentive" problem in an earlier formulation.

**Two separated sustainability indicators** (to avoid conflating production efficiency
with remediation): τ (production-side, lower=better) and **Net Ecological Position**
NEP = G(R) + C^restore − D (balance-sheet, >0 building natural capital). NEP is pitched
as analogous to World Bank Adjusted Net Savings.

**Natural capital:** dR/dt = G(R) − C, with G(R) = rR(1 − R/K) logistic; sustainable
extraction C ≤ G(R); for non-renewables (G≈0) Hotelling governs — the paper says it
*would* add marginal thermodynamic damage to user cost but explicitly **defers the
Hamiltonian derivation** (sign/form "beyond scope").

## Core Solow result

Modified production: Y = Ω·K^α(AL)^(1−α) with Ω = ϕ(τ)·ζ(H)·θ(H)^(1−α). Capital:
K̇ = sY − δK. Intensive form k ≡ K/(AL):
$$\dot k = s·Ω·k^α − (n+g+δ)·k \tag{14}$$
Steady state:
$$k^* = \left[\frac{sΩ^*}{n+g+δ}\right]^{1/(1−α)} \tag{16}$$
$$\boxed{\,y^* = (Ω^*)^{1/(1−α)}·\left[\frac{s}{n+g+δ}\right]^{α/(1−α)}\,} \tag{18}$$

**Central claim — amplification:** y* = (standard Solow output) × (Ω*)^(1/(1−α)). Since
0 < Ω ≤ 1 and 1/(1−α) > 1, a 10% fall in Ω cuts y* by **more** than 10% (≈14% at α=0.3,
since 1 − 0.9^(1/0.7) ≈ 0.14), because Ω also depresses equilibrium capital. The
elasticity ∂ln y*/∂ln Ω = 1/(1−α) (1.43 at α=0.3; 1.67 at α=0.4) — Proposition 4.

**Decomposition (Eq. 19):** Ω* = (1−τ*)^ψ · (H*/H̄)^m · (H*/H̄)^(b(1−α)) = three drags:
waste drag, cognitive (TFP) drag, labor drag. All = 1 in standard Solow → model nests
original.

**Comparative statics (Appendix B, signs unambiguous):** ∂k*/∂τ < 0; ∂k*/∂H > 0;
∂k*/∂ψ < 0 (for τ>0); ∂k*/∂Ω > 0.

**Convergence (Appendix B.3):** linearizing around k*, convergence rate
λᶜ = (1−α)(n+g+δ) — *identical to standard Solow*. The paper's gloss: the augmentation
changes **where** the economy converges (lower k*), not **how fast**. "The growth trap
is not about slow convergence, it is about converging to the wrong place."

**Health–output fixed point (Appendix B.4):** H* and Y* are mutually dependent
(H* depends on Y* via exposure; Y* depends on H* via Ω), giving an implicit fixed point.
Existence/uniqueness asserted under "χκτ small enough" that the damage slope < recovery
slope; claimed satisfied "under empirically plausible parameter values."

## The growth trap (headline policy message)

If Ω is **declining over time** (τ rising and/or H falling), the steady state itself
retreats — short-run GDP growth stays positive while sustainable capacity silently
erodes. **Invisible to GDP; visible only to Thermo-GDP.** Offered as *testable
contributing hypotheses* (not monocausal) for: (a) **secular stagnation** (rising τ /
health damage since ~1970s coinciding with the productivity slowdown); (b)
**convergence failure / poverty traps** (high-τ, low-H, depleted-R countries face
effective steady states far below the Solow prediction). The paper stresses **clean
growth** is possible and is the policy objective: drive τ→0 ⇒ Ω→1 ⇒ converge to standard
Solow *from below* (cites EU −50% GHG/GDP, 1990–2020).

## Thermo-GDP & accounting lineage

$$\text{Thermo-GDP} = \text{GDP} − D = \text{GDP} − λ′·TO \tag{21}$$
Framed as a Hicksian "green net product." Positioned as synthesizing / extending:
UN **SEEA-EA** (data architecture), World Bank **Adjusted Net Savings** (+ health
capital), UNEP **Inclusive Wealth** (flow counterparts to stocks), **GPI/ISEW**
(but with microfounded shadow prices instead of ad hoc adjustments). Claimed advantage:
the subtraction D uses the **same shadow prices** that enter the production function →
internal consistency between growth model and accounts.

## Planetary boundaries (Section 5)

Boundary transgressions enter as a welfare penalty Φ(R) = Σₙ ωₙ·max(0, R̄ₙ − Rₙ)² (Eq. 22);
ties to Rockström/Richardson (six of nine boundaries transgressed) and Raworth's Doughnut.
Presented as a pathway to a Ramsey-style optimization, not yet executed.

## Empirical strategy (Section 6) — five testable predictions

1. Lower τ ⇒ higher future TFP growth (controlling for standard determinants).
2. Sector PM₂.₅ exposure ⇒ lower labor productivity, stronger where cognitively intensive.
3. Thermo-GDP diverges from GDP most in resource-intensive economies; converges in green transitions.
4. Pollution reduction's growth effect **exceeds** narrowly-measured health cost savings (feedback amplifies abatement returns).
5. Convergence rates moderated by initial τ and H (high-τ/low-H converge slower).

**Anchor regression (§6.1):** panel
Δln(TFP)ᵢₜ = β₁τᵢ,ₜ₋₁ + β₂ln(Hᵢ,ₜ₋₁) + γ′Xᵢₜ + αᵢ + δₜ + εᵢₜ, predicting β₁<0, β₂>0.
Proxies: τ ← CO₂e/GDP (SEEA/IEA); H ← HALEs (WHO) or inverse satellite PM₂.₅; satellite
PM₂.₅ as instrument via atmospheric transport. Claims it is estimable with existing data.

## Extensions previewed (Section 7) — explicitly deferred to companion papers

- **7.1 Ramsey–Cass–Koopmans:** modified Euler (Eq. 23) makes the effective discount rate **endogenous** to environmental conditions ("closer to Stern than Nordhaus, but from model structure not ethics").
- **7.2 Hotelling:** extraction path modified by marginal thermodynamic damage cost; **full Hamiltonian deferred**.
- **7.3 DSGE:** TO shocks as negative TFP shocks (ϕ, ζ), labor-supply shocks (θ), cost-push (resource scarcity) ⇒ formal channel to stagflation.
- **7.4 Optimal carbon price path:** λ are equilibrium objects with a dynamic trajectory; **deferred**.

## Policy implications (Section 8)

Pigouvian pricing of TO at λ (carbon ≈ \$190/tCO₂; PM₂.₅ productivity co-benefit
≈ \$950–3,000/household/yr per µg/m³); adopt Thermo-GDP as complementary dashboard
(Stiglitz–Sen–Fitoussi); directed innovation subsidies to cut τ (Acemoglu et al. 2012);
health-inclusive CBA that counts the morbidity–productivity–TFP feedback, not just
avoided mortality.

## What the paper explicitly DOES NOT claim (§1.1) — scope guards

- No hard thermodynamic limit to near-term growth (efficiency/composition/innovation can cut τ).
- Not claiming pollution is the **dominant** driver of the slowdown — a *contributing, testable* mechanism.
- Does not replace macro; **augments** Solow (baseline ⇒ standard model exactly).
- Not anti-growth/anti-decoupling; clean growth is the objective.
- Not claiming GDP is useless; Thermo-GDP is a complement.

## Author-stated limitations (§10) — important for the critique

1. **Ω is reduced-form** — ϕ(τ)=(1−τ)^ψ is axiomatic, **not micro-founded** from optimizing firms/consumers; quantitative predictions hinge on ψ, which is uncalibrated ⇒ treat as qualitative/structural, not a forecasting engine.
2. **τ is not endogenized** — treated as slow-moving exogenous state; real τ responds to prices/regulation/innovation.
3. **Scalar TO aggregation** suppresses heterogeneity across waste streams (spatial/temporal/damage-pathway differences).
4. **Causal identification** of the health→macro-TFP channel is hard; micro estimates may not aggregate; instrument validity & GE feedbacks unresolved.
5. **No distributional effects** — representative-agent Solow cannot capture that waste/health/depletion fall on lower-income populations.

## Key equation cheat-sheet (Appendix A)

(1) Y=A·K^α·L^β·U^u · (2) TO=(E,P,M) · (3) τ=‖TO‖/(p₀Y) · (4) D=λ′TO · (5) X=κP/Pop ·
(6) Ḣ=η₀+η₁h−δ_hH−χX · (7) L^eff=Lθ(H), A^eff=Aζ(H) · (8) NEP=G(R)+C^rest−D ·
(9) ϕ(τ)=(1−τ)^ψ · (10) dR/dt=G(R)−C · (11) Y=Ω·K^α(AL)^(1−α), Ω=ϕ·ζ·θ^(1−α) ·
(14) k̇=sΩk^α−(n+g+δ)k · (16) k*=[sΩ*/(n+g+δ)]^(1/(1−α)) ·
(18) y*=(Ω*)^(1/(1−α))[s/(n+g+δ)]^(α/(1−α)) · (21) Thermo-GDP=GDP−λ′TO ·
(22) Φ(R)=Σωₙmax(0,R̄ₙ−Rₙ)².

## Reference backbone (for the source audit)

Georgescu-Roegen 1971; Ayres & Warr 2005/2009; Santos et al. 2018; Kümmel 1989;
Brockway et al. 2015 (rebound); Hotelling 1931; **Brock & Taylor 2010 (Green Solow)**;
Acemoglu et al. 2012; Ramsey 1928; **Nordhaus 2017 / Barrage & Nordhaus 2024 (DICE)**;
Stern 2006; EPA 2023 SCC; Rennert et al. 2022; IPCC AR6 WGIII 2022; OECD 2016;
Graff Zivin & Neidell 2012; Dechezleprêtre et al. 2025; Chen et al. 2018; SEEA-EA 2021;
Lawn 2003; World Bank 2023; Arrow et al. 2012; Stiglitz–Sen–Fitoussi 2009;
Rockström 2009 / Steffen 2015 / Richardson 2023; Raworth 2017; Solow 1956/1987;
Grossman & Krueger 1995; Hartwick 1977.
