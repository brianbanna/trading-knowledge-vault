---
aliases: [mean reversion, reversion to the mean, mean reverting]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Mean Reversion

## Definition

Mean reversion is the tendency of a price, spread, or statistical metric to move back toward its long run average after deviating from it. The core assumption: extreme values are temporary and will normalize. In commodity markets, mean reversion is strongest in SPREADS (calendar spreads, inter-commodity spreads, location spreads) because physical arbitrage constrains how far a spread can deviate. It is weaker in outright prices because commodities can trend for extended periods driven by fundamental supply/demand shifts. Mean reversion is not guaranteed: it requires a STABLE [[Equilibrium Price|equilibrium]]. When a [[Structural Break]] occurs, the old mean is no longer the reversion target.

## Why it matters (commodities and FX)

Mean reversion is the theoretical foundation of most [[Relative Value Trade|relative value]] and [[Calendar Spread|spread trading]] strategies. When a trader says the [[Brent-WTI Spread]] is "wide" or a crack spread is "rich," they are implicitly claiming that the spread will revert to a mean. The mean reversion framework provides: (1) a signal (deviation from mean, measured by [[Z-Score]]), (2) an entry level (sufficiently large deviation), (3) an exit level (back to or through the mean), and (4) a risk framework (what if it does not revert?).

In FX, purchasing power parity (PPP) is a long run mean reversion anchor: currencies that are "cheap" on PPP metrics tend to appreciate over multi year horizons. But the reversion is extremely slow, making it a positioning guide rather than a tactical signal.

## Concrete example

**Calendar spread mean reversion:** The [[Henry Hub Natural Gas]] Mar/Apr spread (crossing winter to shoulder season) has a 10 year average of +$0.35 (March premium) with a standard deviation of $0.20. Currently, the spread is at +$0.80 (2.25 sigma above mean). A mean reversion trader shorts the spread (sell Mar, buy Apr), targeting reversion to +$0.35. If the spread reverts: profit = ($0.80 - $0.35) x 10,000 MMBtu = $4,500 per spread. If instead a polar vortex hits and the spread widens to +$1.50 (5.75 sigma): loss = ($1.50 - $0.80) x 10,000 = $7,000 per spread. The asymmetry is unfavorable: limited upside (spread compresses by $0.45), potentially unlimited downside (spread can widen further). This concavity is the core risk of mean reversion strategies ([[Convexity]]).

**When mean reversion fails:** A trader shorts the gold/silver ratio at 85 (historically "wide," mean of 65). The ratio moves to 90, then 100 (COVID crisis). The trader adds to the position at each level, expecting reversion. But the structural driver (silver's industrial demand collapsed while gold's safe haven demand surged) is a [[Regime Shift]], not a temporary dislocation. The ratio peaks at 125. Mean reversion worked eventually (ratio returned to 70 by 2021), but the drawdown would have blown up most positions.

## Key mechanics and formulas

**Half life of mean reversion (Ornstein-Uhlenbeck):**
`dX = θ(μ - X)dt + σdW`

Where θ = speed of reversion (higher = faster), μ = long run mean, σ = volatility, W = Brownian motion.

`Half-life = ln(2) / θ`

A half life of 20 days means the spread reverts halfway to the mean in 20 trading days. Estimate θ from: `ΔX_t = a + b x X_{t-1} + ε`, then `θ = -b`, half-life = -ln(2)/ln(1+b).

**[[Z-Score]] entry/exit:**
- Entry: Z > 2.0 or Z < -2.0 (spread is 2 standard deviations from mean)
- Exit: Z crosses 0 (spread has returned to mean)
- Stop loss: Z > 3.5 or Z < -3.5 (spread moving further away, possible [[Structural Break]])

**Augmented Dickey-Fuller (ADF) test:**
Tests whether a time series is stationary (mean reverting) vs non-stationary (trending). The test statistic must be below the critical value to confirm mean reversion. Run this on the SPREAD, not on individual prices. Individual commodity prices are almost always non-stationary. Spreads may be stationary.

**Hurst exponent:**
H < 0.5: mean reverting. H = 0.5: random walk. H > 0.5: trending.
Estimate using rescaled range analysis or DFA (detrended fluctuation analysis).

## Prerequisites
- [[Z-Score]]
- [[Correlation]]
- [[Equilibrium Price]]
- [[Forward Curve]]

## Related concepts (learn next)
- [[Z-Score]] - the standard metric for measuring deviation from the mean. Essential for calibrating entry and exit levels.
- [[Structural Break]] - the primary risk to mean reversion. If the mean has shifted, the strategy loses money indefinitely.
- [[Regime Shift]] - a broader concept encompassing structural breaks. Regime shifts change the mean reversion dynamics.
- [[Convexity]] - mean reversion strategies are naturally concave (limited upside, unlimited downside). Understanding this risk profile is essential.
- [[Calendar Spread]] - the most common mean reversion instrument in commodity markets.
- [[Relative Value Trade]] - the broader category that includes mean reversion as one approach.
- [[Equilibrium Price]] - the "mean" in mean reversion. Must be correctly identified and updated.

## Common misconceptions

**"If it went up, it must come down."** Mean reversion applies to stationary series only. Commodity outright prices are generally NOT stationary (they can trend for years). Spreads are more likely to be stationary, but even this must be tested, not assumed.

**"A bigger deviation means a better trade."** Bigger deviations can also indicate a [[Structural Break]]. The signal/noise ratio does not improve linearly with deviation size. A 5 sigma deviation is more likely to be a structural break than a 2 sigma deviation.

**"Mean reversion strategies have high Sharpe ratios."** They can, during stable regimes. But the Sharpe ratio is misleading because it does not capture the tail risk (concavity). A strategy with Sharpe 2.0 that blows up once every 5 years is not actually safe. Evaluate risk adjusted returns including max drawdown and kurtosis, not just Sharpe.

## Sources

- Pairs Trading: Quantitative Methods and Analysis (Vidyamurthy, 2004)
- Earnest Chan, "Algorithmic Trading" (2013), mean reversion chapters
- Avellaneda and Lee, "Statistical Arbitrage in the US Equities Market" (2010)
