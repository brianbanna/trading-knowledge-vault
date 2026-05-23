---
aliases: [ultima, DvolgaDvol, dVolga/dVol, third order vega, vol convexity of convexity]
tags:
  - "#quant"
date-added: "2026-05-23"
---

# Ultima

## Definition

Ultima is the third order greek that measures the rate at which [[Volga]] changes as implied volatility changes. Plain English: volga is the convexity of the option price in vol space (how the price curves with respect to vol). Ultima tells you how that convexity itself curves. Mathematically, ultima = d(Volga) / d(σ) = d³(Option price) / d(σ)³.

Ultima is the deepest vol greek a practitioner is likely to encounter without writing custom code. It captures the asymmetry of volga across vol levels: at low vol, volga can be growing rapidly with vol; at high vol, volga can be decreasing. Ultima describes that transition.

Practically, ultima matters in three domains: deeply OTM option pricing during severe vol regime changes, exotic option pricing in stochastic vol models, and tail risk hedging strategies that depend on the vol convexity convexity (how aggressively wings reprice in vol explosions).

For nearly all retail and most institutional traders, ultima is below the threshold of conscious management. It is included here for completeness and because it occasionally explains anomalous behavior of deep OTM option books in crisis periods.

## Why it matters (commodities and FX)

Ultima rarely matters in normal markets. It matters in three specific situations:

- **Crisis tail hedging.** Funds holding deep OTM options as crash protection ([[VIX]] calls struck at 50+, deep OTM SPX puts, deep OTM commodity wings) see their volga exposure itself change with vol. When VVIX rises sharply, volga on these wings grows nonlinearly via ultima, making the position more reactive to subsequent vol moves. Hedge funds that priced these positions assuming constant volga underestimate the gain in crisis.
- **Exotic option books in stochastic vol regimes.** Barrier options, autocallables, and lookback options have ultima exposure baked into their stochastic vol pricing. When the underlying [[Vol of Vol]] regime shifts (e.g. 2008, March 2020, August 2024), ultima drives part of the systematic repricing of these structures across the dealer ecosystem.
- **Commodity wing repricing.** Deep OTM [[Henry Hub Natural Gas]] options struck at $10+ during normal regimes have negligible volga and trivial ultima. During a polar vortex spike where vol explodes, volga on these wings grows via ultima faster than first order analysis predicts. Dealers short these wings via [[Butterfly]] structures suffer accelerating losses.

For a typical commodities or FX trader, ultima awareness consists of recognizing that "deep OTM options reprice more aggressively in vol explosions than my linear estimates suggest." That recognition is enough; explicit ultima hedging is rare outside dealer exotic option desks.

## Concrete example

A volatility fund is long 200 contracts of [[VIX]] 80 strike calls expiring in 90 days. Spot VIX: 14. Implied vol on VIX options (VVIX): 100. The option is deeply OTM. Premium paid: $0.30 per contract.

Initial greeks per contract:
- Vega: 0.008
- Volga: 0.004
- Ultima: 0.003

The position has tiny vega, small volga, and small ultima. Looks like dead premium burning theta.

Black swan event: VVIX jumps from 100 to 180 in a week, on growing fear of a vol explosion. Spot VIX still at 18 (only moderate move).

First order P&L estimate: vega × ΔVol = 0.008 × 80 = $0.64 per contract gain. Multiply by 200 contracts: $12,800 estimated gain.

Add second order (volga): 0.5 × volga × (ΔVol)² = 0.5 × 0.004 × 6400 = $12.80 per contract additional. Multiply by 200: $2,560 additional.

Add third order (ultima): 0.166 × ultima × (ΔVol)³ = 0.166 × 0.003 × 512,000 = $255 per contract additional. Multiply by 200: $51,000 additional.

The ultima term, normally negligible, dominates the P&L because (ΔVol)³ is enormous (80³ = 512,000). What looked like a $15,000 trade turned into a $66,000 trade because ultima matters when vol moves are huge.

Of course, in reality the model would break down well before this regime (Black Scholes assumes constant vol, and stochastic vol models price these wings differently). But the qualitative point holds: wing options in vol explosions reprice with ultima participating, not just vega and volga.

What if VVIX moved only from 100 to 105? (ΔVol)³ is 125, ultima contribution is 0.166 × 0.003 × 125 × 200 = $12.45. Negligible. Ultima is invisible at small moves and dominant at large ones, by construction of the cube term.

## Key mechanics and formulas

**Ultima for a vanilla option (Black Scholes):**

`Ultima = -Vega × (d1 × d2 × (1 - d1 × d2) + d1² + d2²) / σ²`

This is computed by differentiating volga with respect to vol. Most pricing systems compute it numerically rather than analytically.

**Useful intuition:**
- Ultima is small for ATM options
- Ultima is largest in magnitude for moderately OTM options (similar region to volga peak)
- Ultima scales with 1/σ², so it appears more pronounced in low vol regimes (where small absolute vol changes are large relative)
- Ultima can be positive or negative depending on moneyness

**Practical role in Taylor expansion:**

`ΔPrice ≈ Vega × Δσ + 0.5 × Volga × (Δσ)² + (1/6) × Ultima × (Δσ)³`

For small Δσ, the linear term (vega) dominates. For moderate Δσ, the quadratic term (volga) matters. For large Δσ (vol regime change), the cubic term (ultima) participates.

**When ultima matters quantitatively:**

Ultima becomes material relative to volga when:
`|Ultima × Δσ / (3 × Volga)| > 0.10`

For a typical OTM option with volga/ultima ratio around 1.5, this means ultima becomes >10% of volga P&L when Δσ exceeds roughly 5 vol points.

**Distinction from related greeks:**

Ultima is dVolga/dVol. There is no separate name for d⁴Price/dσ⁴ in common usage. Higher derivatives are rarely tracked even by sophisticated desks.

## Prerequisites
- [[Volga]]
- [[Vega]]
- [[Vol of Vol]]
- [[Greeks]]
- [[Option]]
- [[Vol Surface]]

## Related concepts (learn next)
- [[Volga]] - ultima is the vol derivative of volga. Understanding volga is the prerequisite.
- [[Vega]] - ultima sits at the top of the vol greek hierarchy: vega → volga → ultima.
- [[Vol of Vol]] - ultima is the price sensitivity that becomes important when vol of vol is realized, i.e., when vol moves in large jumps.
- [[VVIX]] - large VVIX moves activate ultima for any book with significant wing exposure.
- [[Butterfly]] - butterfly positions concentrate volga and therefore have ultima exposure during vol regime changes.
- [[Zomma]] - zomma is dGamma/dVol, another third order vol greek. Together with ultima they describe how the option surface deforms in vol regime shifts.
- [[Heston Model]] - stochastic vol models implicitly capture ultima effects through their vol of vol parameter (xi).

## Common misconceptions

**"Ultima is never relevant in practice."** True for typical positions and typical vol moves. False during vol regime changes (Volmageddon 2018, March 2020, August 2024). For tail hedge portfolios and exotic option books, ultima participates in P&L during crisis weeks.

**"Higher order greeks are just academic curiosities."** Vanilla traders can mostly ignore them. Exotic option dealers cannot. Autocallable structures, in particular, have ultima exposure that becomes material during market dislocations and is one source of structured product hedging losses in stressed markets.

**"Ultima can be hedged with vol products."** In principle yes, through specific combinations of butterflies at different strikes. In practice, the hedging cost usually exceeds the residual risk, so most desks accept ultima as residual.

**"Ultima cubic scaling means it explodes for any vol move."** No, it explodes for LARGE vol moves. The cube term means it is negligible at small vol moves and dominant at large ones. The transition point depends on the volga/ultima ratio of the specific position.

**"Ultima is just a renamed volga."** Distinct greeks. Volga measures how vega changes with vol (d²Price/dσ²). Ultima measures how volga changes with vol (d³Price/dσ³). Each captures one more order of vol convexity.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form ultima and other third order vol greeks.
- Taleb, Nassim Nicholas. *Dynamic Hedging*. Discussion of high order vol greeks and tail risk pricing.
- Bergomi, Lorenzo. *Stochastic Volatility Modeling*. The reference for higher order vol greeks in stochastic vol frameworks.
- Wystup, Uwe. *FX Options and Structured Products*. Discussion of exotic option pricing including ultima.
- Carr, Wu. "Variance Risk Premiums." Background on vol regime dynamics that drive ultima P&L.
