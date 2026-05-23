---
aliases: [vol of vol, volatility of volatility, vovol, second moment of vol, vol surface curvature]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-05-23"
---

# Vol of Vol

## Definition

Vol of vol is the volatility of an asset's volatility itself. [[Volatility]] measures how much a price moves; vol of vol measures how much that volatility moves. If [[Brent Crude]] runs 25% realized vol on average but oscillates between 15% and 60%, that variability is vol of vol.

Two distinct uses:
1. **Statistical (realized) vol of vol:** standard deviation of a rolling realized vol series. Computed historically from price data.
2. **Implied vol of vol:** the market's risk neutral expectation of future variability in implied vol, extracted from option prices. [[VVIX]] is the canonical example.

Vol of vol makes [[Vega]] hedges imperfect, gives [[Butterfly|butterflies]] and [[Strangle|strangles]] value beyond first order [[Vega]], and justifies the existence of vol smiles and surface curvature. Priced through [[Volga]] and traded explicitly via vol indices (VVIX, OVXX) and butterfly structures.

## Why it matters (commodities and FX)

Vol of vol separates a competent vol trader from a beginner. A trader thinking only in [[Vega]] assumes vol changes are linear and small. In reality vol moves in clusters and spikes; that nonlinear behavior is the dominant tail P&L driver.

For commodities and FX:

- **Commodity vol regimes shift sharply.** [[Henry Hub Natural Gas]] vol can sit at 30% for months then jump above 100% during a polar vortex week. Natgas vol of vol is extreme. A short vol position sized to 30% vol is vega bombed when vol triples.
- **FX vol of vol is mean reverting but spike prone.** [[USDJPY]] vol can sit at 6% for years then explode to 18% in a day (BOJ intervention, SNB unpeg). Vol of vol pricing in long dated FX [[Butterfly|butterflies]] is the institutional way to express this.
- **OVX (oil VIX) often moves more than VIX in percentage terms.** Commodity vol of vol is structurally higher than equity because commodity supply shocks (war, hurricane, OPEC) are more discrete than equity earnings cycles.
- **Cross asset vol of vol correlation rises in crisis.** When VVIX rises, oil OVX and gold GVZ implied vols follow, and FX [[Risk Reversal|risk reversals]] widen. Long volga across multiple commodities is implicitly long vol of vol of the global risk regime.

Pricing vol of vol correctly is the difference between selling a [[Strangle]] at "fair" vol and bleeding for months versus catching one tail event that wipes a year of premium.

## Concrete example

**Concrete:** Trader short a 1 month [[Strangle]] on [[Henry Hub Natural Gas]] in October. Strikes $2.50 put and $4.00 call, spot $3.20. Premium $0.45 per contract. Sold at 55% implied vol (typical for natgas). Naive vega view: vol does not move, time decays, collect premium. Short [[Vega]] -0.012 per contract. Reality: cold snap in early November. NOAA flips its 8 to 14 day forecast to "much below normal" eastern US. Natgas spot jumps $3.20 to $3.95 in 4 sessions. Implied vol explodes 55% to 95%. Spot move: short call now ITM, -$0.30 intrinsic. Vega P&L: 40 vol points × -0.012 = -$0.48 per contract. Total MTM loss: ~$0.78 per contract on $0.45 received. Loss ~170% of premium. The vol move was not a smooth 5 point creep; it was a 40 point jump in a week. Pricing vol of vol would have meant either (1) selling at 65% instead of 55% to compensate, or (2) buying a far OTM "vega convexity" hedge (long $5.50 call, long volga) making the trade vega plus volga neutral.

**Simplified:** Volatility itself has volatility. The market is calm, then suddenly it is not. If you sold options assuming the calm continues, you get crushed when the regime flips, even if you predicted the average vol correctly. Pricing vol of vol means charging extra for the chance of a regime change, or hedging it with deep OTM options that pay off in vol explosions. Without vol of vol awareness, short vol strategies look great until they don't.

## Key mechanics and formulas

**Realized vol of vol (simple):**

`σ_σ = stdev(σ_t)` over a rolling window, σ_t = rolling realized vol series.

Equivalent to applying the vol formula twice: first to returns to get a vol series, then to changes in that vol series.

**Heston model parameterization:**

In the Heston stochastic vol model:
`d(v_t) = κ(θ - v_t)dt + ξ × sqrt(v_t) × dW_t`

v_t = instantaneous variance, κ = mean reversion speed, θ = long run variance, ξ = vol of vol parameter (sometimes σ_v or "xi"). ξ is THE vol of vol parameter. Higher ξ produces a steeper smile and more pronounced [[Volga]].

**Implied vol of vol from market:**

[[VVIX]] is the model free implied vol of vol for VIX (indirectly for SPX). Analogues:
- OVXX (rarely quoted): implied vol of OVX
- For FX: extracted from butterfly prices in long dated options

**Vol of vol drives smile curvature:**

In a Black Scholes world (zero vol of vol), the implied vol surface is flat. Real surfaces have curvature precisely because vol moves stochastically. Smile convexity (the [[Butterfly]] spread) is proportional to expected vol of vol over the option's life.

**Vol of vol and tail pricing:**

A jump diffusion or stochastic vol model with high ξ produces fatter tails in the simulated return distribution. This is why pure Black Scholes systematically underprices wings.

## Prerequisites
- [[Volatility]]
- [[Realized Volatility]]
- [[Implied Volatility]]
- [[Vega]]
- [[Volga]]
- [[Vol Surface]]

## Related concepts (learn next)
- [[VVIX]] - direct market implementation of implied vol of vol for SPX/VIX. Canonical observable metric.
- [[Volga]] - greek measuring sensitivity to vol changes. Vol of vol determines the value of volga.
- [[Butterfly]] - cleanest vanilla way to express a long or short vol of vol view. Long butterfly = long vol of vol.
- [[Vanna]] - cross greek between spot and vol. Vanna and volga form the second order vol risk space.
- [[Vol Surface]] - geometric object whose curvature is driven by vol of vol.
- [[Heston Model]] - workhorse stochastic vol model where vol of vol enters explicitly as a parameter.
- [[Jump Diffusion]] - alternative way to model fat tails. Often combined with stochastic vol.

## Common misconceptions

**"Vol of vol is the same as vega."** [[Vega]] is sensitivity of option price to a 1 vol point change. Vol of vol is the actual or expected variability of vol itself. A vega hedged portfolio is still exposed to vol of vol via [[Volga]].

**"Vol of vol only matters in equities."** Commodity vol of vol is typically higher than equity. [[Henry Hub Natural Gas]] and power markets have extreme vol of vol from physical supply shocks. FX vol of vol shows up in central bank intervention regimes.

**"Vol of vol is captured by implied vol."** A given implied vol is a single number that does not tell you about the distribution of future vols. Two assets can have identical implied vol but very different vol of vol. Skew and smile of the [[Vol Surface]] hold the vol of vol information, not ATM vol alone.

**"Selling vol harvests the variance risk premium with bounded risk."** Without explicit vol of vol hedging (long volga or long deep OTM wings), short vol carries unbounded risk via vol of vol. [[Volmageddon]] February 2018 and August 2024 yen carry unwinds were vol of vol events that destroyed short vol books.

## Sources

- Heston, Steven L. "A Closed-Form Solution for Options with Stochastic Volatility." Review of Financial Studies, 1993.
- Gatheral, Jim. "The Volatility Surface: A Practitioner's Guide." Wiley, 2006. Chapters on stochastic vol and smile dynamics.
- Carr and Wu. "Variance Risk Premiums." Review of Financial Studies, 2009.
- Park, Yang Ho. "Volatility of Volatility and Tail Risk Premiums." Journal of Financial Econometrics, 2015.
- Sinclair, Euan. "Volatility Trading," 2nd ed. Wiley.
- Bergomi, Lorenzo. "Stochastic Volatility Modeling." CRC Press, 2016. Definitive reference on practitioner stoch vol.
