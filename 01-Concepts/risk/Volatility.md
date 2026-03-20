---
aliases: [volatility, vol, realized volatility, implied volatility, historical volatility]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-03-20"
---

# Volatility

## Definition

Volatility measures the magnitude of price fluctuations over time. It is the standard deviation of returns, typically annualized. Realized (historical) volatility is calculated from past price data. Implied volatility is extracted from option prices and represents the market's expectation of future volatility. High volatility means larger and more frequent price swings. Low volatility means calmer, more range bound markets. Volatility is not directional: it measures the SIZE of moves, not the direction. Volatility itself tends to cluster (high vol begets high vol) and mean revert (extreme vol eventually normalizes).

## Why it matters (commodities and FX)

Volatility is the denominator of everything in trading. Position sizing depends on it: you size smaller in high vol and larger in low vol to maintain consistent risk. Spread valuation depends on it: a $2 Brent-WTI spread is meaningless without knowing if the standard deviation is $0.50 (4 sigma move) or $3.00 (within normal range). Option pricing depends entirely on it. Margin requirements scale with it.

Commodity markets have distinct volatility regimes. [[Henry Hub Natural Gas]] annualized vol can range from 25% (calm summer) to 150% (polar vortex winter). [[WTI Crude Oil]] typically runs 20 to 40% but spiked to 300%+ in April 2020. [[Gold Futures]] typically has 12 to 18% vol but spikes to 25%+ in crises. Recognizing when you are in a low vs high vol regime ([[Regime Shift]]) is essential for survival.

## Concrete example

[[Brent Crude]] 30 day realized vol is 25% annualized. You want to risk $10,000 per day on a position. Daily vol = 25% / sqrt(252) ≈ 1.58%. Brent at $80: daily $move = $80 x 1.58% = $1.26/bbl. To risk $10,000: position size = $10,000 / $1.26 = ~7,937 barrels ≈ 8 contracts.

If vol spikes to 50% (geopolitical event): daily $move = $80 x 3.15% = $2.52/bbl. Same $10,000 risk budget: position size = $10,000 / $2.52 = ~3,968 barrels ≈ 4 contracts. You halve your position to maintain consistent risk. Failing to adjust for vol is how traders blow up.

## Key mechanics and formulas

**Realized volatility:**
`σ = sqrt((252 / (n-1)) x Σ(r_i - r̄)²)`

Where r_i = ln(P_i / P_{i-1}) = daily log return, n = number of observations, 252 = trading days per year.

**Quick approximation:**
`Daily Vol ≈ Annual Vol / 16` (since sqrt(252) ≈ 15.87)

**Volatility cone:** Plot realized vol at different lookback windows (10 day, 30 day, 60 day, 90 day) against their historical percentile. Shows whether current vol is high or low relative to history at each horizon.

**Implied vol (from options):** Backed out from Black-Scholes or Black-76 model. Implied vol > realized vol = options are "expensive." Implied vol < realized vol = options are "cheap."

**Vol of vol:** Volatility itself is volatile. The CBOE OVX index measures the implied vol of crude oil options. High OVX = market expects large crude moves.

## Prerequisites
- [[Forward Curve]]
- [[Correlation]]

## Related concepts (learn next)
- [[Regime Shift]] - volatility regime changes are one of the clearest signals of a broader regime shift.
- [[Risk-On Risk-Off]] - VIX and implied vol indices are the primary RORO thermometers.
- [[Z-Score]] - Z-scores require volatility estimates. A stale vol estimate produces misleading Z-scores.
- [[Slippage]] - high vol environments have wider [[Bid-Ask Spread|bid-ask spreads]] and more [[Slippage]].
- [[Liquidity]] - vol and liquidity are inversely related. When vol spikes, liquidity vanishes.
- [[Hedging]] - option based hedges are priced on implied vol. Understanding vol levels is essential for cost effective hedging.
- [[Mean Reversion]] - vol mean reverts more reliably than price. Selling vol at extremes is a recognized strategy (with tail risk).

## Common misconceptions

**"High volatility means the market is going down."** Vol measures the size of moves, not direction. Vol can spike during rallies (2020 to 2021 crypto, 2022 oil). The association with falling markets comes from equity markets where panic selloffs are faster than rallies.

**"Implied vol equals expected future vol."** Implied vol includes a risk premium (the "variance risk premium"). On average, implied vol exceeds realized vol by 2 to 4 percentage points in most markets. This is why selling options is profitable on average (but has tail risk).

**"You can use a single vol number for all time horizons."** Vol scales with the square root of time only under idealized assumptions. In practice, commodity vol has term structure: short term vol can be very different from long term vol. Use the vol matching your trade horizon.

## Sources

- Taleb, Nassim Nicholas, "Dynamic Hedging" (1997)
- Hull, Options, Futures, and Other Derivatives, Vol and options chapters
- CBOE: OVX (crude oil VIX), GVZ (gold VIX) methodology
- Gatheral, Jim, "The Volatility Surface" (2006)
