---
aliases: [skewness, skew, distributional skew, return asymmetry, statistical skew]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-24"
---

# Skewness

## Definition

Skewness is the asymmetry of a return distribution around its mean. A symmetric distribution (the bell curve) has zero skew: up and down moves mirror each other. Positive skew means the right tail is longer or fatter, so extreme gains are more likely and more severe than extreme losses. Negative skew means the left tail dominates. If you flip a distribution and it looks different, it is skewed. Skewness tells you WHICH direction surprises come from. A positively skewed commodity is more likely to spike up violently than crash down. A negatively skewed carry trade collects steady returns but faces sudden sharp losses.

## Why it matters (commodities and FX)

Commodities and FX have distinctly different skew profiles, fundamental to sizing, strategy selection, and hedging.

**Commodities tend toward positive skew.** Supply disruptions (weather, geopolitics, infrastructure) cause violent upward spikes; demand weakness produces gradual declines. Cocoa doubling in 6 months is a supply shock. Cocoa falling 50% takes years. Being long commodities exposes you to occasional windfall gains and routine small losses; being short gives you steady small gains and catastrophic tail losses.

**FX carry trades have negative skew.** You collect the rate differential daily (small, predictable), but the unwind is violent. The AUDJPY carry trade earned steady pips for years before losing 6 months of gains in 2 weeks during the 2008 [[Carry Unwind]]. The negative skew is the hidden cost of carry: the average looks good, the distribution is asymmetric against you.

**Options skew** (the [[Volatility Smile]] / [[Skew Microstructure]]) is a separate but related concept: the market's pricing of distributional skew into option premiums.

## Concrete example

**Concrete:** [[Henry Hub Natural Gas]] daily returns over 5 years show skewness +1.2. Distribution: mean +0.01%, median -0.05%, largest daily gain +18% (cold snap Feb 2021), largest daily loss -9%. Right tail extends much further than left. A trader long natgas options benefits: OTM calls are worth more than a normal distribution would imply because extreme upside is more frequent. Contrast: long AUDUSD and NZDUSD vs short JPY and CHF over 10 years. Monthly mean +0.3%, median +0.5%, skewness -1.8, best month +4%, worst month -12%. The +0.5% median masks the -1.8 skew. Most months mildly positive, worst months 3x more extreme than best. Sizing to average ignores asymmetric tail risk.

**Simplified:** Average return and volatility tell you nothing about which side the surprises come from. Positive skew means rare big gains, lots of small losses. Negative skew means lots of small gains, rare big losses. The Sharpe ratio cannot see the difference. A strategy that bleeds small amounts daily and wins big rarely (positive skew) is psychologically painful but mathematically attractive. A strategy that earns small amounts daily and blows up rarely (negative skew) feels great until it doesn't.

## Key mechanics and formulas

### Skewness Formula

**Sample skewness:**
`Skew = [n / ((n-1)(n-2))] × sum[(x_i - mean)^3] / sigma^3`

n = number of observations, sigma = standard deviation.

Cubing deviations means large negative returns drive negative skew, large positives drive positive skew.

### Interpreting Skewness Values

| Skewness | Interpretation | Example |
|----------|---------------|---------|
| Below -1.0 | Strong negative skew | FX carry, short vol |
| -1.0 to -0.5 | Moderate negative skew | Equity indices, credit |
| -0.5 to +0.5 | Approximately symmetric | G10 FX majors, diversified portfolios |
| +0.5 to +1.0 | Moderate positive skew | Base metals, some agriculturals |
| Above +1.0 | Strong positive skew | Natural gas, softs, trend following |

### Typical Skewness by Asset Class (daily returns)

| Asset | Typical Skewness | Why |
|-------|------------------|-----|
| Crude oil | +0.3 to +0.8 | Supply disruptions dominate |
| Natural gas | +0.8 to +2.0 | Weather spikes, storage constraints |
| Cocoa, coffee | +0.5 to +1.5 | Crop failures, inelastic supply |
| Grains | +0.3 to +0.8 | Weather/drought upside, gradual demand |
| Gold | -0.2 to +0.3 | Symmetric, slight positive in crises |
| S&P 500 | -0.5 to -1.0 | Crashes sharper than rallies |
| FX carry basket | -1.0 to -2.5 | Steady gains, violent unwinds |
| EM FX (single pair) | -0.5 to -3.0 | Devaluation creates extreme left tail |

### Skew and Strategy Selection

- **Positive skew strategies:** Trend following, long OTM options, long commodities with supply constraints. Bleed slowly, win big.
- **Negative skew strategies:** Carry, short vol, mean reversion. Win slowly, bleed big.
- **Portfolio construction:** Combining positive and negative skew reduces aggregate skew toward zero.

### Skew and Option Pricing

The market's expectation of skewness is embedded in the [[Volatility Smile]]. For a positively skewed asset (commodities), OTM calls have higher implied vol than OTM puts (call skew). For negatively skewed assets (equities), OTM puts have higher implied vol than OTM calls (put skew). The [[Risk Reversal]] directly measures implied skew.

## Prerequisites

- [[Volatility]]
- [[Tail Risk]]
- [[Mean Reversion]]

## Related concepts (learn next)

- [[Kurtosis]] because kurtosis measures tail fatness while skewness measures tail asymmetry. Together they characterize departure from normality.
- [[Volatility Smile]] because the option market's implied skew is the tradeable expression of distributional skewness.
- [[Carry Trade]] because understanding negative skew is essential to sizing carry positions.
- [[Risk Reversal]] because the 25 delta RR quote directly prices the market's skew expectation.
- [[Expected Shortfall]] because negative skew inflates ES relative to [[Value at Risk]], making ES the better measure for skewed portfolios.
- [[Supply Shock]] because supply disruptions are the primary source of positive skew in commodity returns.

## Common misconceptions

**"Skewness is stable over time."** Skewness varies dramatically with regime. Crude had positive skew during tight supply but near zero or negative during the 2014 to 2016 glut. A single historical estimate is unreliable for forward risk management.

**"Positive skew means you will make money."** Positive skew means big wins exceed big losses but says nothing about average returns. A positively skewed strategy can have negative expected returns if it loses frequently. Buying OTM options is positively skewed but often negative expected return due to the vol risk premium.

**"The Sharpe ratio captures skew."** Sharpe uses only mean and standard deviation. Two strategies with identical Sharpe can have completely different skews. One could bleed 0.5% monthly with occasional 10% gains, the other earn 0.5% monthly with occasional 10% losses. Sharpe treats them identically. Use Sortino or Omega to capture skew.

## Sources

- Ilmanen, Antti. *Expected Returns* (2011), chapters on return distributions and alternative risk premia.
- Harvey, Campbell and Siddique, Akhtar. "Conditional Skewness in Asset Pricing Tests," *Journal of Finance* (2000).
- Brunnermeier, Markus, Nagel, Stefan, and Pedersen, Lasse. "Carry Trades and Currency Crashes," *NBER Macroeconomics Annual* (2008).
- Cont, Rama. "Empirical properties of asset returns: stylized facts and statistical issues," *Quantitative Finance* (2001).
