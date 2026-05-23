---
aliases: [vol of vol, volatility of volatility, vovol, second moment of vol, vol surface curvature]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-05-23"
---

# Vol of Vol

## Definition

Vol of vol is the volatility of an asset's volatility itself. Plain English: [[Volatility]] measures how much a price moves. Vol of vol measures how much that volatility moves. If [[Brent Crude]] runs 25% realized vol on average but oscillates between 15% and 60% over different periods, that variability of vol is what vol of vol captures.

Two distinct uses of the term:
1. **Statistical (realized) vol of vol:** the standard deviation of a rolling realized vol series. Computed historically from price data.
2. **Implied vol of vol:** the market's risk neutral expectation of future variability in implied vol, extracted from option prices. [[VVIX]] is the canonical example.

Vol of vol is what makes [[Vega]] hedges imperfect, what gives [[Butterfly|butterflies]] and [[Strangle|strangles]] value beyond first order [[Vega]], and what justifies the existence of vol smiles and surface curvature. It is priced in markets through [[Volga]] and traded explicitly through vol indices (VVIX, OVXX where it exists) and through butterfly structures.

## Why it matters (commodities and FX)

Vol of vol is the dimension that separates a competent vol trader from a beginner. A trader who only thinks in [[Vega]] terms assumes vol changes are linear and small. In reality, vol moves in clusters and spikes, and that nonlinear vol behavior is the dominant P&L driver in tails.

For commodities and FX specifically:

- **Commodity vol regimes shift sharply.** [[Henry Hub Natural Gas]] vol can sit at 30% for months then jump to 100%+ during a polar vortex week. The vol of vol of natgas is extreme. A short vol position sized to 30% vol is vega bombed when vol triples.
- **FX vol of vol is mean reverting but spike prone.** [[USDJPY]] vol can sit at 6% for years then explode to 18% in a single day (BOJ intervention, SNB unpeg style events). Vol of vol pricing in long dated FX [[Butterfly|butterflies]] is the institutional way to express this.
- **OVX (oil VIX) often moves more than VIX in percentage terms.** Commodity vol of vol is structurally higher than equity vol of vol because commodity supply shocks (war, hurricane, OPEC) are more discrete than equity earnings cycles.
- **Cross asset vol of vol correlation rises in crisis.** When VVIX rises, oil OVX and gold GVZ implied vols typically follow, and FX [[Risk Reversal|risk reversals]] widen. A trader long volga across multiple commodities is implicitly long the vol of vol of the global risk regime.

Pricing vol of vol correctly is the difference between selling a [[Strangle]] at "fair" vol and bleeding for months versus catching one tail event that wipes a year of premium.

## Concrete example

A trader is short a 1 month [[Strangle]] on [[Henry Hub Natural Gas]] in October. Strikes at $2.50 put and $4.00 call. Underlying at $3.20. Sold for $0.45 in premium per contract. Implied vol at sale: 55% (typical for natgas).

Naive vega view: vol does not move, time decays, collect premium. The trader is short [[Vega]] of about -0.012 per contract.

Reality: cold snap in early November. NOAA flips its 8 to 14 day forecast to "much below normal" for the eastern US. Natgas spot jumps from $3.20 to $3.95 in 4 sessions. Implied vol explodes from 55% to 95%.

P&L decomposition:
- Spot move from $3.20 to $3.95: short call now ITM, losing about $0.30 in intrinsic.
- Vega P&L: vol up 40 points × vega of -0.012 = -$0.48 per contract.
- Total mark to market loss: about $0.78 per contract on $0.45 premium received. Loss is ~170% of premium collected.

Where did vol of vol show up? The vol move was not a smooth 5 point creep. It was a 40 point jump in a week. A trader pricing in vol of vol would have either:
1. Sold the strangle at higher vol (65% instead of 55%) to compensate for vol of vol risk, or
2. Bought a far OTM "vega convexity" hedge (long $5.50 call, long volga position), making the trade vega plus volga neutral instead of just delta hedged.

If the trader had no vol of vol awareness, position is a slow grinder with one tail year that wipes out three good years. If vol of vol was priced in, the same trade collects less premium but survives the November spike near flat.

## Key mechanics and formulas

**Realized vol of vol (simple):**

`σ_σ = stdev(σ_t)` over a rolling window, where σ_t is the rolling realized vol series.

Equivalent to applying the vol formula twice: first to returns to get vol series, then to changes in that vol series.

**Heston model parameterization:**

In the Heston stochastic vol model:
`d(v_t) = κ(θ - v_t)dt + ξ × sqrt(v_t) × dW_t`

Where v_t = instantaneous variance, κ = mean reversion speed, θ = long run variance, ξ = vol of vol parameter (sometimes called σ_v or "xi"). ξ is THE vol of vol parameter in the model. Higher ξ produces a steeper smile and more pronounced [[Volga]].

**Implied vol of vol from market:**

[[VVIX]] is the model free implied vol of vol for VIX (and indirectly for SPX). Equivalent indices exist:
- OVXX (rarely quoted): implied vol of OVX
- For FX: extracted from butterfly prices in long dated options

**Vol of vol drives smile curvature:**

In a Black Scholes world (zero vol of vol), the implied vol surface would be flat. Real world surfaces have curvature precisely because vol moves stochastically. The convexity of the smile (the [[Butterfly]] spread) is proportional to expected vol of vol over the option's life.

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
- [[VVIX]] - the direct market implementation of implied vol of vol for SPX/VIX. The canonical observable vol of vol metric.
- [[Volga]] - the option greek that measures sensitivity to vol changes. Vol of vol determines the value of volga.
- [[Butterfly]] - the cleanest vanilla way to express a long or short vol of vol view. Long butterfly = long vol of vol.
- [[Vanna]] - the cross greek between spot and vol. Vanna and volga together form the second order vol risk space.
- [[Vol Surface]] - the geometric object whose curvature is driven by vol of vol.
- [[Heston Model]] - the workhorse stochastic vol model where vol of vol enters explicitly as a parameter.
- [[Jump Diffusion]] - alternative way to model fat tails. Often combined with stochastic vol for "stochastic vol with jumps" models that capture both vol of vol and discrete event risk.

## Common misconceptions

**"Vol of vol is the same as vega."** [[Vega]] is sensitivity of option price to a 1 vol point change. Vol of vol is the actual or expected variability of vol itself. A vega hedged portfolio is still exposed to vol of vol via [[Volga]].

**"Vol of vol only matters in equities."** Commodity vol of vol is typically higher than equity vol of vol. [[Henry Hub Natural Gas]] and power markets have extreme vol of vol due to physical supply shocks. FX vol of vol shows up in central bank intervention regimes.

**"Vol of vol is captured by implied vol."** A given implied vol is a single number that does not tell you about the distribution of future vols. Two assets can have identical implied vol but very different vol of vol. The skew and smile of the [[Vol Surface]] is where vol of vol information lives, not in ATM vol alone.

**"Selling vol harvests the variance risk premium with bounded risk."** Without explicit vol of vol hedging (long volga or long deep OTM wings), short vol carries unbounded risk via vol of vol. [[Volmageddon]] February 2018 and August 2024 yen carry unwinds are both vol of vol events that destroyed short vol books.

## Sources

- Heston, Steven L. "A Closed-Form Solution for Options with Stochastic Volatility." Review of Financial Studies, 1993.
- Gatheral, Jim. "The Volatility Surface: A Practitioner's Guide." Wiley, 2006. Chapters on stochastic vol and smile dynamics.
- Carr and Wu. "Variance Risk Premiums." Review of Financial Studies, 2009.
- Park, Yang Ho. "Volatility of Volatility and Tail Risk Premiums." Journal of Financial Econometrics, 2015.
- Sinclair, Euan. "Volatility Trading," 2nd ed. Wiley.
- Bergomi, Lorenzo. "Stochastic Volatility Modeling." CRC Press, 2016. Definitive reference on practitioner stoch vol.
