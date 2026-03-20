---
aliases: [z-score, z score, standard score, deviation from mean, sigma]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Z-Score

## Definition

The Z-score measures how many standard deviations a current value is from its mean. A Z-score of +2 means the value is 2 standard deviations above the mean. A Z-score of -1.5 means 1.5 standard deviations below. Z-scores standardize different instruments and spreads onto a common scale, allowing comparison of "how extreme" a reading is regardless of the units (dollars, basis points, barrels). In commodity trading, Z-scores are the primary tool for identifying [[Mean Reversion]] entry points in spreads.

## Why it matters (commodities and FX)

Without Z-scores, you cannot objectively compare the richness or cheapness of different spreads. A $3 [[Brent-WTI Spread]] might be normal, while a $3 gold/silver ratio deviation might be extreme. Z-scores normalize everything to "how unusual is this?" They are the entry signal for most systematic spread strategies: trade when the Z-score exceeds a threshold (typically 1.5 to 2.5), exit when it reverts to 0. Z-scores also help with position sizing: a higher Z-score implies a more extreme deviation, but also potentially a [[Structural Break]], so conviction and size must be calibrated together.

## Concrete example

The [[Brent-WTI Spread]] over the trailing 90 days has a mean of $3.80 and a standard deviation of $1.10. The current spread is $6.50.

`Z = (6.50 - 3.80) / 1.10 = 2.45`

The spread is 2.45 standard deviations above the 90 day mean. For a mean reversion trader, this exceeds the typical entry threshold of 2.0. Trade: short the spread (sell Brent, buy WTI), targeting reversion to $3.80 (Z = 0). Stop loss at Z = 3.5 ($7.65).

Critical question: is the deviation temporary (trade it) or a [[Structural Break]] (avoid it)? At 2.45 sigma, it is worth investigating the fundamental driver before entering. If Cushing just had a large inventory build, this is likely temporary. If a new pipeline changed the equilibrium, this may be a new mean.

## Key mechanics and formulas

**Basic Z-score:**
`Z = (X - μ) / σ`

Where X = current value, μ = mean, σ = standard deviation.

**Rolling Z-score (more practical):**
`Z_t = (X_t - μ_N) / σ_N`

Where μ_N and σ_N are the mean and standard deviation calculated over the trailing N periods (e.g., 60 days, 90 days, 252 days).

**Lookback window selection:**
- 20 to 30 days: captures recent regime, responsive but noisy
- 60 to 90 days: balances responsiveness and stability, most common for spread trading
- 252 days (1 year): captures seasonal effects, less responsive to regime changes
- Seasonal Z-score: compare current value to the same calendar window across multiple years

**Interpretation guide:**

| Z-Score | Interpretation | Typical Action |
|---------|---------------|----------------|
| < 1.0 | Normal range | No signal |
| 1.5 to 2.0 | Moderately extended | Watch list, prepare |
| 2.0 to 2.5 | Extended, entry zone | Enter [[Mean Reversion]] trade |
| 2.5 to 3.0 | Highly extended | Enter with conviction if fundamentally supported |
| > 3.0 | Extreme | Possible [[Structural Break]], investigate before trading |

**Pitfall with non-normal distributions:**
Commodity spreads often have fat tails. A Z-score of 3 in a normal distribution has a 0.13% probability. In a fat-tailed distribution, a Z-score of 3 might occur 1 to 2% of the time. Do not assume normal distribution probabilities when interpreting Z-scores.

## Prerequisites
- [[Mean Reversion]]
- [[Volatility]]
- [[Correlation]]

## Related concepts (learn next)
- [[Mean Reversion]] - the Z-score is the primary signal for mean reversion strategies. Understanding the relationship between Z-score levels and mean reversion probability.
- [[Structural Break]] - high Z-scores can indicate structural breaks rather than mean reversion opportunities. Distinguishing the two is the core skill.
- [[Volatility]] - the Z-score denominator is volatility. If vol is changing (regime shift), the Z-score becomes unreliable because σ is stale.
- [[Calendar Spread]] - Z-scores applied to calendar spreads, often using seasonal windows rather than simple rolling windows.
- [[Seasonality]] - seasonal Z-scores compare the current spread to the same point in previous years, which is more appropriate for seasonal instruments than a flat rolling window.
- [[Correlation]] - portfolio Z-scores and multi-spread systems require understanding correlation between spread Z-scores.

## Common misconceptions

**"A Z-score of 3 means the trade is guaranteed to revert."** It does not. A Z-score of 3 is unusual but not impossible, and it may reflect a [[Structural Break]] rather than a temporary deviation. Always investigate the fundamental driver.

**"The lookback window does not matter much."** It matters enormously. A 30 day Z-score can read +2.5 while a 252 day Z-score reads +0.8 for the same spread. The window must match your trade horizon and the dynamics of the spread.

**"Z-scores are valid for any time series."** Z-scores assume the underlying series is stationary (mean reverting). If the series has a trend, the Z-score is misleading because the "mean" is not a reversion target. Always test for stationarity (ADF test) before using Z-scores as trading signals.

## Sources

- Earnest Chan, "Algorithmic Trading" (2013), mean reversion and Z-score chapters
- Vidyamurthy, "Pairs Trading" (2004)
- CME Group: quantitative spread analysis tools
