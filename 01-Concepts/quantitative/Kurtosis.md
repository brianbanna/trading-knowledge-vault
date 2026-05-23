---
aliases: [kurtosis, excess kurtosis, fat tails, leptokurtic, heavy tails, tail fatness]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-24"
---

# Kurtosis

## Definition

Kurtosis is how fat the tails of a return distribution are compared to a normal distribution. Normal has kurtosis 3 (excess kurtosis 0). Financial returns almost always sit well above 3: extreme events happen far more often than the bell curve predicts. If [[Skewness]] tells you which direction surprises come from, kurtosis tells you how OFTEN and how EXTREME the surprises are. A leptokurtic distribution has a sharp peak around the mean (many small days) AND fat tails (occasional massive moves). The boring days breed complacency; the fat tails destroy the risk model.

## Why it matters (commodities and FX)

Kurtosis is why standard risk models fail for commodities. Every formula assuming normal returns (parametric [[Value at Risk]], portfolio optimization, [[Black-Scholes]] pricing) understates the probability of large moves.

**The numbers are stark:** A 4 sigma daily move in a normal distribution should occur once every 126 years. In crude oil, 4+ sigma daily moves have occurred roughly once every 2 years. In natural gas, roughly once a year. In cocoa during 2024, multiple 5+ sigma daily moves occurred in a single quarter. A normal distribution risk model tells you these events are "impossible" right up until they wipe out your account.

For FX, G10 pairs have moderate excess kurtosis (3 to 6), making the normal approximation less dangerous but still flawed. EM currencies have extreme kurtosis (10 to 30+) from devaluations, capital controls, and central bank interventions producing discontinuous jumps.

Practical implication: positions sized to normal distribution assumptions are too large. Margin buffers based on normal VaR are too thin. Black-Scholes prices systematically underprice OTM options, which is why the [[Volatility Smile]] exists.

## Concrete example

**Concrete:** Risk manager evaluates 2 commodity strategies, both 12% annualized return, 15% annualized vol, Sharpe 0.80. Strategy A: diversified trend following, excess kurtosis 2, worst 5 year daily loss 2.8 sigma. Strategy B: concentrated cocoa and coffee carry, excess kurtosis 12, worst 5 year daily loss 6.2 sigma. Both look identical mean/variance. Strategy A's 99% parametric VaR = $2.33M on $100M; actual worst 1% days average $2.8M. Close. Strategy B's 99% parametric VaR = $2.33M (same formula); actual worst 1% days average $5.5M. Model understates risk 2.4x. An allocator ignoring kurtosis sizes them equally. An allocator accounting for it gives Strategy B half the capital or requires 2.5x the margin buffer.

**Simplified:** Two strategies can have the same average return and the same volatility yet completely different worst case days. Kurtosis is the gap. High kurtosis means most days are normal, but the occasional day is far worse than your math predicts. Risk models built on normal distributions are blind to this. The result: position sizes look safe on paper, then one bad day takes more than the model says is possible. Always check kurtosis before sizing.

## Key mechanics and formulas

### Kurtosis Formula

**Sample kurtosis:**
`Kurt = [n(n+1) / ((n-1)(n-2)(n-3))] × sum[(x_i - mean)^4] / sigma^4`

**Excess kurtosis = kurtosis - 3**

Subtracting 3 normalizes so normal has excess kurtosis 0. Positive excess kurtosis = fatter than normal.

The 4th power means extreme observations dominate the calculation. A single 6 sigma day shifts kurtosis dramatically.

### Typical Excess Kurtosis by Asset (daily returns)

| Asset | Excess Kurtosis | Implication |
|-------|-----------------|-------------|
| S&P 500 | 5 to 10 | 4+ sigma events every few years |
| Crude oil | 8 to 15 | Extreme moves from supply disruptions |
| Natural gas | 15 to 30+ | Weather spikes, storage constraints |
| Cocoa | 10 to 25+ | Crop failures, thin liquidity |
| Coffee | 8 to 15 | Frost events, supply inelasticity |
| Gold | 5 to 10 | Safe haven spikes during crises |
| EUR/USD | 3 to 6 | Relatively well behaved for FX |
| USD/TRY | 15 to 40+ | Devaluations, policy discontinuities |
| USD/JPY | 5 to 12 | BOJ intervention creates gap risk |

### Kurtosis and Risk Model Adjustment

**Cornish-Fisher VaR adjustment:**

`z_adjusted = z + (z^2 - 1) × skew/6 + (z^3 - 3z) × kurtosis/24 - (2z^3 - 5z) × skew^2/36`

Adjusts the z score for non-normality. For 99% VaR with excess kurtosis 10 and skew 0:
- Normal z = 2.33
- Adjusted z ≈ 3.2
- Adjusted VaR is 37% higher than parametric

**Rule of thumb:** Each unit of excess kurtosis raises parametric VaR by 3 to 5%. Excess kurtosis of 10 suggests VaR should be 30 to 50% higher than the normal estimate.

### Kurtosis Clustering

Kurtosis is not constant. It clusters: low kurtosis periods (calm, normal works) alternate with high kurtosis periods (crises, regime shifts, model failure). This temporal clustering means:
- Long windows average across regimes and understate current tail risk.
- Short windows capture the current regime but miss structural tails.
- GARCH type models with time varying kurtosis outperform static estimates.

## Prerequisites

- [[Volatility]]
- [[Skewness]]
- [[Tail Risk]]

## Related concepts (learn next)

- [[Skewness]] because skewness and kurtosis together describe how a distribution deviates from normal. Skewness = direction of tails. Kurtosis = fatness.
- [[Tail Risk]] because high kurtosis IS the quantitative measure. Kurtosis 15 means 5+ sigma events are not theoretical.
- [[Value at Risk]] because parametric VaR assumes kurtosis 0 and understates risk for fat tailed assets.
- [[Expected Shortfall]] because ES captures the tail severity that kurtosis describes.
- [[Volatility Smile]] because the smile exists to price kurtosis. ATM options reflect the center, OTM options reflect tails. High kurtosis means expensive OTM options.
- [[Implied Volatility]] because the gap between ATM implied and realized vol partly reflects kurtosis risk premium.

## Common misconceptions

**"High kurtosis means high volatility."** Independent. A distribution can have low vol (small average moves) and extreme kurtosis (rare huge moves). Natural gas in a calm summer has low vol but high kurtosis because the next polar vortex could produce a 20% daily move.

**"Kurtosis is driven by a few outliers."** Removing the most extreme observations and recalculating still produces excess kurtosis well above zero. The fat tails are structural, not artifacts.

**"Student's t distribution solves the kurtosis problem."** Student's t with low df captures symmetric fat tails, better than normal. It cannot capture skewed fat tails, time varying kurtosis, or jump behavior. Improvement, not solution.

**"Monthly returns have lower kurtosis, so use monthly data."** Aggregation reduces kurtosis (central limit theorem) but does NOT reduce actual risk. Your daily margin call does not care that the monthly distribution looks better.

## Sources

- Cont, Rama. "Empirical properties of asset returns: stylized facts and statistical issues," *Quantitative Finance* (2001).
- Mandelbrot, Benoit. *The (Mis)behavior of Markets* (2004).
- Taleb, Nassim Nicholas. *Statistical Consequences of Fat Tails* (2020).
- McNeil, Frey, and Embrechts. *Quantitative Risk Management: Concepts, Techniques and Tools* (2015).
- DeCarlo, Lawrence. "On the meaning and use of kurtosis," *Psychological Methods* (1997).
