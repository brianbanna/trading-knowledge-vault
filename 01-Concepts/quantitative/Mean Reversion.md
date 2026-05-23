---
aliases: [mean reversion, reversion to the mean, mean reverting]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Mean Reversion

## Definition

Mean reversion is the tendency of a price, spread, or statistical metric to move back toward its long run average after deviating. The core assumption: extreme values are temporary and normalize. In commodity markets, mean reversion is strongest in SPREADS (calendar, inter-commodity, location) because physical arbitrage constrains spread deviations. It is weaker in outright prices, which trend for extended periods on fundamental shifts. Mean reversion requires a STABLE [[Equilibrium Price|equilibrium]]. After a [[Structural Break]], the old mean is no longer the target.

## Why it matters (commodities and FX)

Mean reversion is the theoretical foundation of most [[Relative Value Trade|relative value]] and [[Calendar Spread|spread trading]]. When a trader calls the [[Brent-WTI Spread]] "wide" or a crack spread "rich," they claim the spread will revert. The framework provides: (1) a signal (deviation from mean via [[Z-Score]]), (2) entry (sufficient deviation), (3) exit (back through mean), (4) risk framework (what if it does not revert).

In FX, purchasing power parity (PPP) is a long run mean reversion anchor: currencies cheap on PPP appreciate over multi year horizons. Reversion is extremely slow, making it a positioning guide rather than a tactical signal.

## Concrete example

**Concrete:** [[Henry Hub Natural Gas]] Mar/Apr spread (winter to shoulder) has a 10 year mean of +$0.35 with std dev $0.20. Current spread +$0.80 (2.25 sigma). Short the spread (sell Mar, buy Apr) targeting $0.35. If it reverts: profit = ($0.80 - $0.35) × 10,000 MMBtu = $4,500 per spread. If a polar vortex widens it to +$1.50 (5.75 sigma): loss = ($1.50 - $0.80) × 10,000 = $7,000 per spread. Asymmetry is unfavorable: limited upside ($0.45 compression), unlimited downside. This concavity is the core risk of mean reversion ([[Convexity]]). Failure case: short the gold/silver ratio at 85 (mean 65). Ratio moves to 90, 100 (COVID), peaks at 125. Reversion worked eventually (back to 70 by 2021) but the drawdown blew up most positions.

**Simplified:** Some prices wander but always come back. Spreads between linked commodities are the cleanest example because physical arbitrage caps how far they can drift. You bet on the return to average when the current value is unusually far from it. The trap: sometimes the average itself shifted. Then your trade keeps losing as the new normal pulls away from the old one. The skill is distinguishing temporary noise from a permanent change.

## Key mechanics and formulas

**Half life of mean reversion (Ornstein-Uhlenbeck):**
`dX = θ(μ - X)dt + σdW`

Where θ = speed of reversion (higher = faster), μ = long run mean, σ = volatility, W = Brownian motion.

`Half-life = ln(2) / θ`

Half life of 20 days means the spread reverts halfway in 20 trading days. Estimate θ from: `ΔX_t = a + b × X_{t-1} + ε`, then `θ = -b`, half-life = -ln(2)/ln(1+b).

**[[Z-Score]] entry/exit:**
- Entry: Z > 2.0 or Z < -2.0
- Exit: Z crosses 0
- Stop loss: Z > 3.5 or Z < -3.5 (possible [[Structural Break]])

**Augmented Dickey-Fuller (ADF) test:**
Tests whether a series is stationary (mean reverting) vs non-stationary (trending). The statistic must fall below the critical value to confirm mean reversion. Run on the SPREAD, not individual prices. Individual commodity prices are almost always non-stationary. Spreads may be stationary.

**Hurst exponent:**
H < 0.5: mean reverting. H = 0.5: random walk. H > 0.5: trending.
Estimate via rescaled range analysis or DFA (detrended fluctuation analysis).

## Prerequisites
- [[Z-Score]]
- [[Correlation]]
- [[Equilibrium Price]]
- [[Forward Curve]]

## Related concepts (learn next)
- [[Z-Score]] - standard metric for measuring deviation from mean. Essential for calibrating entry/exit.
- [[Structural Break]] - primary risk to mean reversion. If the mean has shifted, the strategy loses indefinitely.
- [[Regime Shift]] - broader concept encompassing structural breaks. Changes reversion dynamics.
- [[Convexity]] - mean reversion strategies are naturally concave (limited upside, unlimited downside).
- [[Calendar Spread]] - most common mean reversion instrument in commodities.
- [[Relative Value Trade]] - broader category including mean reversion.
- [[Equilibrium Price]] - the "mean" itself. Must be correctly identified and updated.

## Common misconceptions

**"If it went up, it must come down."** Mean reversion applies to stationary series only. Commodity outright prices are generally NOT stationary. Spreads are more likely stationary; test, do not assume.

**"A bigger deviation means a better trade."** Bigger deviations can also indicate a [[Structural Break]]. Signal/noise does not improve linearly with deviation size. A 5 sigma deviation is more likely a break than a 2 sigma deviation.

**"Mean reversion strategies have high Sharpe ratios."** During stable regimes, yes. Sharpe is misleading because it does not capture tail risk (concavity). Sharpe 2.0 that blows up once every 5 years is not safe. Evaluate with drawdown and kurtosis, not Sharpe alone.

## Sources

- Pairs Trading: Quantitative Methods and Analysis (Vidyamurthy, 2004)
- Earnest Chan, "Algorithmic Trading" (2013), mean reversion chapters
- Avellaneda and Lee, "Statistical Arbitrage in the US Equities Market" (2010)
