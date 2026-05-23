---
aliases: [volatility, vol, realized volatility, implied volatility, historical volatility]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-03-20"
---

# Volatility

## Definition

Volatility measures the magnitude of price fluctuations over time. It is the standard deviation of returns, annualized by convention. Realized (historical) vol comes from past price data. Implied vol is extracted from option prices and represents the market's expectation of future vol. High vol means larger and more frequent price swings; low vol means calmer, range bound markets. Vol is not directional: it measures the size of moves, not the direction. Vol clusters (high vol begets high vol) and mean reverts (extreme vol eventually normalizes).

## Why it matters (commodities and FX)

Vol is the denominator of everything in trading. Position sizing depends on it: size smaller in high vol, larger in low vol to keep consistent risk. Spread valuation depends on it: a $2 Brent WTI spread is meaningless without knowing if the standard deviation is $0.50 (4 sigma) or $3 (normal). Option pricing depends entirely on it. Margin scales with it.

Commodity markets have distinct vol regimes. [[Henry Hub Natural Gas]] annualized vol ranges from 25% (calm summer) to 150% (polar vortex winter). [[WTI Crude Oil]] runs 20 to 40% but spiked to 300%+ in April 2020. [[Gold Futures]] runs 12 to 18% but spikes to 25%+ in crises. Recognizing when you are in a low vs high vol regime ([[Regime Shift]]) is essential for survival.

## Concrete example

**Concrete:** [[Brent Crude]] 30 day realized vol is 25% annualized. Risk budget: $10,000/day. Daily vol = 25% / sqrt(252) ≈ 1.58%. Brent at $80: daily $ move = $80 × 1.58% = $1.26/bbl. Position to risk $10,000: $10,000 / $1.26 = ~7,937 barrels ≈ 8 contracts. If vol spikes to 50% (geopolitical event): daily move = $80 × 3.15% = $2.52/bbl. Same risk budget: position = $10,000 / $2.52 ≈ 4 contracts. You halve the position to keep consistent dollar risk. Failing to adjust for vol is how traders blow up — they trade the same size in calm and storm.

**Simplified:** Volatility is how much prices wiggle. High vol means big daily moves; low vol means small. To risk the same dollars per day across different vol regimes, you must hold a smaller position when vol is high and a larger one when vol is low. Most blowups come from holding the same size as conditions shift. Vol also drives option prices, margin, and the cost of hedging — everything compresses or expands with it.

## Key mechanics and formulas

**Realized volatility:**
`σ = sqrt((252 / (n−1)) × Σ(r_i − r̄)²)`

r_i = ln(P_i / P_{i−1}) = daily log return, n = observations, 252 = trading days per year.

**Quick approximation:**
`Daily Vol ≈ Annual Vol / 16` (since sqrt(252) ≈ 15.87)

**Volatility cone:** Plot realized vol at different lookbacks (10, 30, 60, 90 day) against historical percentile. Shows whether current vol is high or low at each horizon.

**Implied vol (from options):** Backed out of Black Scholes or Black 76. IV > realized = options expensive. IV < realized = cheap.

**Vol of vol:** Vol itself is volatile. The CBOE OVX measures implied vol of crude options. High OVX = market expects large moves.

## Prerequisites
- [[Forward Curve]]
- [[Correlation]]

## Related concepts (learn next)
- [[Regime Shift]] — vol regime changes are one of the clearest signals of a broader regime shift.
- [[Risk-On Risk-Off]] — VIX and IV indices are the primary RORO thermometers.
- [[Z-Score]] — Z scores require vol estimates. A stale vol gives misleading Z scores.
- [[Slippage]] — high vol environments have wider [[Bid-Ask Spread|bid-ask spreads]] and more [[Slippage]].
- [[Liquidity]] — vol and liquidity are inversely related. When vol spikes, liquidity vanishes.
- [[Hedging]] — option hedges are priced on IV. Knowing vol levels is essential for cost effective hedging.
- [[Mean Reversion]] — vol mean reverts more reliably than price. Selling vol at extremes is a recognized strategy (with tail risk).

## Common misconceptions

**"High volatility means the market is going down."** Vol measures size of moves, not direction. Vol can spike during rallies (2020 to 2021 crypto, 2022 oil). The association with falling markets comes from equities where panic selloffs are faster than rallies.

**"Implied vol equals expected future vol."** IV includes a risk premium (variance risk premium). On average IV exceeds realized vol by 2 to 4 points across most markets. That is why selling options is profitable on average — and has tail risk.

**"One vol number works for all horizons."** Vol scales with sqrt(time) only under idealized assumptions. Commodity vol has term structure: short term vol can differ materially from long term. Use the vol matching the trade horizon.

## Sources

- Taleb, Nassim Nicholas, "Dynamic Hedging" (1997)
- Hull, Options, Futures, and Other Derivatives, Vol and options chapters
- CBOE: OVX (crude oil VIX), GVZ (gold VIX) methodology
- Gatheral, Jim, "The Volatility Surface" (2006)
