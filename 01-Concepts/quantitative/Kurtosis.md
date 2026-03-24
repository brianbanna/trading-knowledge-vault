---
aliases: [kurtosis, excess kurtosis, fat tails, leptokurtic, heavy tails, tail fatness]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-24"
---

# Kurtosis

## Definition

Kurtosis measures how fat the tails of a return distribution are compared to a normal distribution. A normal distribution has a kurtosis of 3 (excess kurtosis of 0). Financial returns almost always have kurtosis well above 3, meaning extreme events happen far more often than the bell curve predicts. Think of it this way: if [[Skewness]] tells you which direction the surprises come from, kurtosis tells you how OFTEN and how EXTREME the surprises are, regardless of direction. A distribution with high kurtosis (leptokurtic) has a sharp peak around the mean (many small, boring days) AND fat tails (occasional massive moves). The boring days lull you into complacency; the fat tails destroy your risk model.

## Why it matters (commodities and FX)

Kurtosis is the reason that standard risk models fail for commodities. Every formula that assumes normally distributed returns, including parametric [[Value at Risk]], portfolio optimization, and option pricing via [[Black-Scholes]], systematically underestimates the probability of large moves.

**The numbers are stark:** A 4 sigma daily move in a normal distribution should occur once every 126 years. In crude oil, 4+ sigma daily moves have occurred roughly once every 2 years. In natural gas, roughly once a year. In cocoa during 2024, multiple 5+ sigma daily moves occurred in a single quarter. If your risk model uses a normal distribution, it tells you these events are "impossible" right up until they wipe out your account.

For FX, G10 pairs have moderate kurtosis (3 to 6 excess), making the normal approximation less dangerous but still flawed. EM currencies have extreme kurtosis (10 to 30+) because of devaluation events, capital controls, and central bank interventions that produce discontinuous jumps.

The practical implication: position sizes based on normal distribution assumptions are too large. Margin buffers based on normal VaR are too thin. Option prices based on Black-Scholes (which assumes normality) systematically underprice OTM options, which is why the [[Volatility Smile]] exists.

## Concrete example

A risk manager is evaluating 2 commodity strategies. Both have annualized returns of 12% and annualized volatility of 15%, giving an identical Sharpe ratio of 0.80.

**Strategy A (low kurtosis):** Diversified commodity trend following. Excess kurtosis of daily returns: 2. Return distribution is close to normal. The worst daily loss in 5 years was 2.8 sigma.

**Strategy B (high kurtosis):** Concentrated cocoa and coffee carry. Excess kurtosis of daily returns: 12. Return distribution has extreme tails. The worst daily loss in 5 years was 6.2 sigma.

Both look identical on a mean/variance basis. But:
- Strategy A's 99% parametric VaR = $2.33 million (on a $100M book). Actual worst 1% days average $2.8 million. The model is close.
- Strategy B's 99% parametric VaR = $2.33 million (same formula). Actual worst 1% days average $5.5 million. The model understates risk by 2.4x.

An allocator who ignores kurtosis would size both strategies equally. An allocator who accounts for kurtosis would give Strategy B half the capital, or require it to maintain 2.5x the margin buffer.

## Key mechanics and formulas

### Kurtosis Formula

**Sample kurtosis:**
`Kurt = [n(n+1) / ((n-1)(n-2)(n-3))] x sum[(x_i - mean)^4] / sigma^4`

**Excess kurtosis = kurtosis - 3**

The subtraction of 3 normalizes so that a normal distribution has excess kurtosis of 0. Positive excess kurtosis = fatter tails than normal.

The 4th power of deviations means extreme observations dominate the calculation. A single 6 sigma day can shift kurtosis dramatically.

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

`z_adjusted = z + (z^2 - 1) x skew/6 + (z^3 - 3z) x kurtosis/24 - (2z^3 - 5z) x skew^2/36`

This adjusts the standard z score for non-normality. For a 99% VaR with excess kurtosis of 10 and skew of 0:
- Normal z = 2.33
- Adjusted z = approximately 3.2
- The adjusted VaR is 37% higher than the parametric estimate

**Rule of thumb:** For each unit of excess kurtosis, increase your parametric VaR by approximately 3 to 5%. Excess kurtosis of 10 suggests VaR should be 30 to 50% higher than the normal estimate.

### Kurtosis Clustering

Kurtosis is not constant. It clusters: periods of low kurtosis (calm markets, normal distribution works well) alternate with periods of high kurtosis (crises, regime shifts, model failure). This temporal clustering means that:
- Measuring kurtosis over long windows averages across regimes, potentially underestimating current tail risk.
- Short lookback windows capture the current regime but may miss structural tails.
- GARCH type models that allow time varying kurtosis perform better than static estimates.

## Prerequisites

- [[Volatility]]
- [[Skewness]]
- [[Tail Risk]]

## Related concepts (learn next)

- [[Skewness]] because skewness and kurtosis together describe how a distribution differs from normal. Skewness = direction of tails. Kurtosis = fatness of tails.
- [[Tail Risk]] because high kurtosis IS the quantitative measure of tail risk. A kurtosis of 15 means you live in a world where 5+ sigma events are not theoretical.
- [[Value at Risk]] because parametric VaR assumes kurtosis of 0 (normal distribution) and therefore systematically understates risk for high kurtosis assets.
- [[Expected Shortfall]] because ES naturally captures the fat tail severity that kurtosis describes.
- [[Volatility Smile]] because the smile exists to price kurtosis. ATM options reflect the center of the distribution. OTM options reflect the tails. High kurtosis means expensive OTM options.
- [[Implied Volatility]] because the gap between ATM implied vol and realized vol partly reflects the kurtosis risk premium: sellers of OTM options demand compensation for fat tail exposure.

## Common misconceptions

**"High kurtosis means high volatility."** Kurtosis and volatility are independent. A distribution can have low volatility (small average daily moves) but extreme kurtosis (rare days with enormous moves). Natural gas in a calm summer has low vol but still extreme kurtosis because the next polar vortex could produce a 20% daily move.

**"Kurtosis is driven by a few outliers."** While individual extreme observations heavily influence the kurtosis statistic, the property of fat tails is structural in financial markets, not an artifact of outliers. Removing the most extreme observations and recalculating still produces excess kurtosis well above zero. The fat tails are real, not data artifacts.

**"Student's t distribution solves the kurtosis problem."** Student's t with low degrees of freedom captures symmetric fat tails, which is better than normal. But it cannot capture skewed fat tails, time varying kurtosis, or the jump behavior seen in commodity markets. It is an improvement, not a solution.

**"Monthly returns have lower kurtosis, so use monthly data."** Aggregating to monthly reduces kurtosis (central limit theorem), but this does NOT reduce the actual risk. It just hides it in the statistics. Your daily margin call does not care that your monthly return distribution looks better behaved.

## Sources

- Cont, Rama. "Empirical properties of asset returns: stylized facts and statistical issues," *Quantitative Finance* (2001).
- Mandelbrot, Benoit. *The (Mis)behavior of Markets* (2004).
- Taleb, Nassim Nicholas. *Statistical Consequences of Fat Tails* (2020).
- McNeil, Frey, and Embrechts. *Quantitative Risk Management: Concepts, Techniques and Tools* (2015).
- DeCarlo, Lawrence. "On the meaning and use of kurtosis," *Psychological Methods* (1997).
