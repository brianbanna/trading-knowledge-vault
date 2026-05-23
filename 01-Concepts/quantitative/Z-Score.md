---
aliases: [z-score, z score, standard score, deviation from mean, sigma]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Z-Score

## Definition

The Z-score is how many standard deviations a current value is from its mean. Z = +2 means 2 std dev above the mean. Z = -1.5 means 1.5 below. Z-scores standardize different instruments and spreads onto a common scale, letting you compare "how extreme" a reading is regardless of units (dollars, basis points, barrels). In commodity trading, Z-scores are the primary tool for identifying [[Mean Reversion]] entry points in spreads.

## Why it matters (commodities and FX)

Without Z-scores, you cannot objectively compare richness or cheapness of different spreads. A $3 [[Brent-WTI Spread]] might be normal; a $3 gold/silver ratio deviation might be extreme. Z-scores normalize everything to "how unusual is this?" They are the entry signal for most systematic spread strategies: trade when Z exceeds a threshold (typically 1.5 to 2.5), exit when it reverts to 0. Z-scores also drive position sizing: a higher Z implies more extreme deviation but also potentially a [[Structural Break]], so conviction and size must be calibrated together.

## Concrete example

**Concrete:** The [[Brent-WTI Spread]] over trailing 90 days has mean $3.80, std dev $1.10. Current spread $6.50. Z = (6.50 - 3.80) / 1.10 = 2.45. The spread is 2.45 std dev above the 90 day mean. For a mean reversion trader, this exceeds the 2.0 entry threshold. Trade: short the spread (sell Brent, buy WTI), targeting reversion to $3.80 (Z = 0). Stop at Z = 3.5 ($7.65). Critical question: temporary (trade it) or [[Structural Break]] (avoid it)? At 2.45 sigma, investigate the fundamental driver first. If Cushing just had a large inventory build, temporary. If a new pipeline changed the equilibrium, this may be a new mean.

**Simplified:** A Z-score is how unusual the current reading is, measured in standard deviations. It puts every spread and every metric on the same scale: 2 is uncommon, 3 is rare, 4 is suspicious. Use it as an entry signal for mean reversion: bigger Z means bigger deviation from average means bigger snap back when it eventually mean reverts. The catch is that "eventually" can mean tomorrow or next year, and very large Z scores are often broken series rather than great trades.

## Key mechanics and formulas

**Basic Z-score:**
`Z = (X - μ) / σ`

X = current value, μ = mean, σ = standard deviation.

**Rolling Z-score (more practical):**
`Z_t = (X_t - μ_N) / σ_N`

μ_N and σ_N = mean and std dev over trailing N periods (e.g., 60, 90, 252 days).

**Lookback window selection:**
- 20 to 30 days: captures recent regime, responsive but noisy
- 60 to 90 days: balances responsiveness and stability, most common for spread trading
- 252 days (1 year): captures seasonal effects, less responsive to regime changes
- Seasonal Z-score: compare current to the same calendar window across years

**Interpretation guide:**

| Z-Score | Interpretation | Typical Action |
|---------|---------------|----------------|
| < 1.0 | Normal range | No signal |
| 1.5 to 2.0 | Moderately extended | Watch list, prepare |
| 2.0 to 2.5 | Extended, entry zone | Enter [[Mean Reversion]] trade |
| 2.5 to 3.0 | Highly extended | Enter with conviction if fundamentally supported |
| > 3.0 | Extreme | Possible [[Structural Break]], investigate before trading |

**Pitfall with non normal distributions:**
Commodity spreads have fat tails. Z = 3 in a normal distribution = 0.13% probability. In a fat tailed distribution, Z = 3 might occur 1 to 2% of the time. Do not assume normal probabilities when interpreting Z-scores.

## Prerequisites
- [[Mean Reversion]]
- [[Volatility]]
- [[Correlation]]

## Related concepts (learn next)
- [[Mean Reversion]] - Z-score is the primary signal. Understand the relationship between Z levels and reversion probability.
- [[Structural Break]] - high Z-scores can indicate breaks rather than reversion. Distinguishing the two is the core skill.
- [[Volatility]] - the Z-score denominator is volatility. If vol is shifting (regime change), Z becomes unreliable because σ is stale.
- [[Calendar Spread]] - Z-scores on calendar spreads, often via seasonal windows rather than rolling.
- [[Seasonality]] - seasonal Z-scores compare to the same point in prior years, more appropriate for seasonal instruments.
- [[Correlation]] - portfolio Z-scores and multi spread systems require correlation between spread Z-scores.

## Common misconceptions

**"A Z-score of 3 means the trade is guaranteed to revert."** It does not. Z = 3 is unusual but not impossible, and may reflect a [[Structural Break]] rather than temporary deviation. Investigate the fundamental driver.

**"The lookback window does not matter much."** It matters enormously. A 30 day Z can read +2.5 while a 252 day Z reads +0.8 for the same spread. Window must match trade horizon and spread dynamics.

**"Z-scores are valid for any time series."** Z-scores assume stationarity (mean reverting). If the series has a trend, the Z is misleading because the "mean" is not a reversion target. Test for stationarity (ADF) before using Z-scores as signals.

## Sources

- Earnest Chan, "Algorithmic Trading" (2013), mean reversion and Z-score chapters
- Vidyamurthy, "Pairs Trading" (2004)
- CME Group: quantitative spread analysis tools
