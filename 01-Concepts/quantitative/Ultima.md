---
aliases: [ultima, DvolgaDvol, dVolga/dVol, third order vega, vol convexity of convexity]
tags:
  - "#quant"
date-added: "2026-05-23"
---

# Ultima

## Definition

Ultima is the rate at which [[Volga]] changes as implied volatility changes. Volga is the convexity of the option price in vol space (how price curves with respect to vol). Ultima tells you how that convexity itself curves. Ultima = d(Volga) / d(σ) = d³(Option price) / d(σ)³.

Ultima is the deepest vol greek a practitioner is likely to encounter without writing custom code. It captures the asymmetry of volga across vol levels: at low vol, volga grows rapidly with vol; at high vol, volga decreases. Ultima describes that transition.

Three domains where ultima matters: deep OTM option pricing during severe vol regime changes, exotic option pricing in stochastic vol models, and tail risk hedging strategies dependent on vol convexity of convexity.

For nearly all retail and most institutional traders, ultima sits below the threshold of conscious management. Included for completeness because it occasionally explains anomalous deep OTM book behavior in crises.

## Why it matters (commodities and FX)

Ultima rarely matters in normal markets. It matters in three specific situations:

- **Crisis tail hedging.** Funds holding deep OTM options as crash protection ([[VIX]] calls struck at 50+, deep OTM SPX puts, deep OTM commodity wings) see volga itself change with vol. When VVIX rises sharply, volga on these wings grows nonlinearly via ultima, making the position more reactive to subsequent vol moves. Hedge funds pricing these positions with constant volga underestimate crisis gains.
- **Exotic option books in stochastic vol regimes.** Barrier options, autocallables, and lookbacks have ultima exposure baked into stochastic vol pricing. When the underlying [[Vol of Vol]] regime shifts (2008, March 2020, August 2024), ultima drives part of the systematic repricing.
- **Commodity wing repricing.** Deep OTM [[Henry Hub Natural Gas]] options struck at $10+ during normal regimes have trivial ultima. During a polar vortex vol explosion, volga on these wings grows via ultima faster than first order analysis predicts. Dealers short wings via [[Butterfly]] structures suffer accelerating losses.

For a typical commodities or FX trader, ultima awareness means recognizing that "deep OTM options reprice more aggressively in vol explosions than linear estimates suggest." Explicit ultima hedging is rare outside dealer exotic option desks.

## Concrete example

**Concrete:** Vol fund long 200 contracts of [[VIX]] 80 strike calls, 90 days to expiry. Spot VIX 14, VVIX 100. Deeply OTM. Premium $0.30 per contract. Greeks per contract: vega 0.008, volga 0.004, ultima 0.003. Black swan: VVIX jumps 100 to 180 in a week on growing vol explosion fears. Spot VIX still at 18. First order P&L: vega × ΔVol = 0.008 × 80 = $0.64 per contract = $12,800 estimated. Volga add: 0.5 × 0.004 × 6400 = $12.80 per contract = $2,560. Ultima add: 0.166 × 0.003 × 512,000 = $255 per contract = $51,000. The ultima term, normally negligible, dominates because (ΔVol)³ is enormous (80³ = 512,000). A $15,000 trade became $66,000 because ultima matters when vol moves are huge. If VVIX had moved 100 to 105, ultima contribution would be $12 total. Ultima is invisible at small moves, dominant at large ones, by construction of the cube term.

**Simplified:** Volga is the second derivative of price with respect to vol. Ultima is the third. The cube of a small number is tiny; the cube of a big number is enormous. So ultima sits silent through normal markets and explodes during vol regime changes. If you own deep OTM options expecting a crash, ultima is what makes them pay off more than linear math predicts when vol actually explodes. If you sold those wings, ultima is what makes the losses worse than your hedge model assumed.

## Key mechanics and formulas

**Ultima for a vanilla option (Black Scholes):**

`Ultima = -Vega × (d1 × d2 × (1 - d1 × d2) + d1² + d2²) / σ²`

Computed by differentiating volga with respect to vol. Most pricing systems compute numerically.

**Useful intuition:**
- Ultima is small for ATM options
- Ultima is largest in magnitude for moderately OTM options (similar to volga peak region)
- Ultima scales with 1/σ², appearing more pronounced in low vol regimes
- Ultima can be positive or negative depending on moneyness

**Practical role in Taylor expansion:**

`ΔPrice ≈ Vega × Δσ + 0.5 × Volga × (Δσ)² + (1/6) × Ultima × (Δσ)³`

Small Δσ: linear (vega) dominates. Moderate Δσ: quadratic (volga) matters. Large Δσ (vol regime change): cubic (ultima) participates.

**When ultima matters quantitatively:**

Ultima becomes material relative to volga when:
`|Ultima × Δσ / (3 × Volga)| > 0.10`

For a typical OTM option with volga/ultima ratio around 1.5, ultima becomes >10% of volga P&L when Δσ exceeds ~5 vol points.

**Distinction from related greeks:**

Ultima is dVolga/dVol. No separate name for d⁴Price/dσ⁴ in common usage. Higher derivatives are rarely tracked.

## Prerequisites
- [[Volga]]
- [[Vega]]
- [[Vol of Vol]]
- [[Greeks]]
- [[Option]]
- [[Vol Surface]]

## Related concepts (learn next)
- [[Volga]] - ultima is the vol derivative of volga.
- [[Vega]] - ultima sits at the top of the vol greek hierarchy: vega → volga → ultima.
- [[Vol of Vol]] - ultima becomes important when vol of vol is realized as large jumps.
- [[VVIX]] - large VVIX moves activate ultima for any book with significant wing exposure.
- [[Butterfly]] - butterfly positions concentrate volga and therefore have ultima exposure in vol regime changes.
- [[Zomma]] - dGamma/dVol, another third order vol greek. Together they describe surface deformation in vol shifts.
- [[Heston Model]] - stochastic vol models capture ultima effects through vol of vol parameter (xi).

## Common misconceptions

**"Ultima is never relevant in practice."** True for typical positions and small vol moves. False during vol regime changes (Volmageddon 2018, March 2020, August 2024). Tail hedge portfolios and exotic books see ultima participate in crisis P&L.

**"Higher order greeks are academic curiosities."** Vanilla traders can mostly ignore them. Exotic dealers cannot. Autocallable structures have ultima exposure that becomes material during dislocations and is a source of structured product hedging losses in stress.

**"Ultima can be hedged with vol products."** In principle yes, through butterfly combinations at different strikes. Hedging cost usually exceeds residual risk; most desks accept ultima as residual.

**"Ultima cubic scaling means it explodes for any vol move."** No, it explodes for LARGE vol moves. Negligible at small moves, dominant at large ones. Transition point depends on volga/ultima ratio of the specific position.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form ultima and other third order vol greeks.
- Taleb, Nassim Nicholas. *Dynamic Hedging*. Discussion of high order vol greeks and tail risk pricing.
- Bergomi, Lorenzo. *Stochastic Volatility Modeling*. The reference for higher order vol greeks in stochastic vol frameworks.
- Wystup, Uwe. *FX Options and Structured Products*. Discussion of exotic option pricing including ultima.
- Carr, Wu. "Variance Risk Premiums." Background on vol regime dynamics that drive ultima P&L.
