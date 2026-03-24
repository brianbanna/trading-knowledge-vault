---
aliases: [skewness, skew, distributional skew, return asymmetry, statistical skew]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-24"
---

# Skewness

## Definition

Skewness measures how asymmetric a distribution of returns is around its mean. A symmetric distribution (like the normal/bell curve) has zero skew: up moves and down moves are mirror images. Positive skew means the right tail is longer or fatter, so extreme gains are more likely and more severe than extreme losses. Negative skew means the left tail is longer or fatter, so extreme losses dominate. Think of it this way: if you flip a distribution and it looks different, it is skewed. Skewness tells you WHICH direction the surprises will come from. A commodity with positive skew is more likely to spike up violently than to crash down. A carry trade with negative skew collects steady returns but faces sudden, sharp losses.

## Why it matters (commodities and FX)

Commodities and FX have distinctly different skew profiles, and understanding them is fundamental to position sizing, strategy selection, and hedging.

**Commodities tend toward positive skew.** Supply disruptions (weather, geopolitics, infrastructure failures) cause violent upward spikes, while demand weakness produces gradual declines. Cocoa doubling in 6 months is a supply shock. Cocoa falling 50% takes years. This positive skew means that being long commodities exposes you to occasional windfall gains but routine small losses, while being short exposes you to steady small gains but catastrophic tail losses.

**FX carry trades have negative skew.** You collect the interest rate differential daily (small, predictable gain), but when the trade unwinds, it does so violently. The AUD/JPY carry trade earned steady pips for years before losing 6 months of gains in 2 weeks during the 2008 [[Carry Unwind]]. This negative skew is the hidden cost of carry: the average return looks good, but the distribution is asymmetric against you.

**Options skew** (the [[Volatility Smile]] / [[Skew Microstructure]]) is a separate but related concept: it reflects the market's pricing of distributional skew into option premiums.

## Concrete example

**Positive skew (natural gas):** Over the past 5 years, [[Henry Hub Natural Gas]] daily returns show skewness of +1.2. The distribution of daily returns:
- Mean: +0.01%
- Median: -0.05% (slightly negative, typical of positively skewed assets)
- Largest daily gain: +18% (cold snap, Feb 2021)
- Largest daily loss: -9%

The right tail (gains) extends much further than the left tail (losses). A trader buying natural gas options benefits from this positive skew: OTM calls are worth more than a normal distribution would suggest because extreme upside moves are more frequent.

**Negative skew (FX carry):** A portfolio long AUD/USD and NZD/USD (high yielders) vs short JPY and CHF (low yielders) over 10 years:
- Monthly return distribution: mean +0.3%, median +0.5%
- Skewness: -1.8
- Best month: +4%
- Worst month: -12%

The steady median return of +0.5% masks the -1.8 skew. Most months are mildly positive, but the worst months are 3x as extreme as the best months. Sizing this strategy to its average return ignores the asymmetric tail risk.

## Key mechanics and formulas

### Skewness Formula

**Sample skewness:**
`Skew = [n / ((n-1)(n-2))] x sum[(x_i - mean)^3] / sigma^3`

Where n = number of observations, sigma = standard deviation.

The cubing of deviations means that large negative returns contribute strongly to negative skew, and large positive returns contribute strongly to positive skew.

### Interpreting Skewness Values

| Skewness | Interpretation | Example |
|----------|---------------|---------|
| Below -1.0 | Strong negative skew | FX carry trades, short vol strategies |
| -1.0 to -0.5 | Moderate negative skew | Equity indices, credit strategies |
| -0.5 to +0.5 | Approximately symmetric | G10 FX majors, diversified portfolios |
| +0.5 to +1.0 | Moderate positive skew | Base metals, some agricultural commodities |
| Above +1.0 | Strong positive skew | Natural gas, soft commodities, trend following |

### Typical Skewness by Asset Class (daily returns)

| Asset | Typical Skewness | Why |
|-------|------------------|-----|
| Crude oil | +0.3 to +0.8 | Supply disruptions dominate |
| Natural gas | +0.8 to +2.0 | Weather driven spikes, storage constraints |
| Cocoa, coffee | +0.5 to +1.5 | Crop failures, inelastic supply |
| Grains | +0.3 to +0.8 | Weather/drought upside, gradual demand |
| Gold | -0.2 to +0.3 | Roughly symmetric, slight positive in crises |
| S&P 500 | -0.5 to -1.0 | Crashes sharper than rallies |
| FX carry basket | -1.0 to -2.5 | Steady gains, violent unwinds |
| EM FX (single pair) | -0.5 to -3.0 | Devaluation risk creates extreme left tail |

### Skew and Strategy Selection

- **Positive skew strategies:** Trend following, long OTM options, buying commodities with supply constraints. These "bleed slowly, win big."
- **Negative skew strategies:** Carry trades, short vol, mean reversion. These "win slowly, bleed big."
- **Portfolio construction:** Combining positive and negative skew strategies can reduce aggregate portfolio skew toward zero, creating a more symmetric return profile.

### Skew and Option Pricing

The market's expectation of skewness is embedded in the [[Volatility Smile]]. For a positively skewed asset (commodities), OTM calls have higher implied vol than OTM puts (call skew). For a negatively skewed asset (equities), OTM puts have higher implied vol than OTM calls (put skew). The [[Risk Reversal]] directly measures this implied skew.

## Prerequisites

- [[Volatility]]
- [[Tail Risk]]
- [[Mean Reversion]]

## Related concepts (learn next)

- [[Kurtosis]] because kurtosis measures tail fatness while skewness measures tail asymmetry. Together they fully characterize how a distribution deviates from normality.
- [[Volatility Smile]] because the option market's implied skew is the tradeable expression of distributional skewness.
- [[Carry Trade]] because understanding negative skew is essential to sizing carry positions and knowing when the strategy is most vulnerable.
- [[Risk Reversal]] because the 25 delta risk reversal quote directly prices the market's skew expectation.
- [[Expected Shortfall]] because negative skew inflates Expected Shortfall relative to [[Value at Risk]], making ES the better risk measure for skewed portfolios.
- [[Supply Shock]] because supply disruptions are the primary source of positive skew in commodity returns.

## Common misconceptions

**"Skewness is stable over time."** Skewness varies dramatically with market regime. Crude oil had positive skew during tight supply regimes but near zero or negative skew during the 2014 to 2016 glut. Using a single historical skewness estimate for forward risk management is unreliable.

**"Positive skew means you will make money."** Positive skew means your big wins are bigger than your big losses, but it says nothing about average returns. A positively skewed strategy can have negative expected returns if it loses frequently. Buying OTM options is positively skewed but often has negative expected returns due to the vol risk premium.

**"The Sharpe ratio captures skew."** The Sharpe ratio uses only mean and standard deviation. Two strategies with identical Sharpe ratios can have completely different skew profiles. One could bleed 0.5% per month with occasional 10% gains (positive skew), the other could earn 0.5% per month with occasional 10% losses (negative skew). The Sharpe ratio treats them identically. Use the Sortino ratio or Omega ratio to capture skew in performance evaluation.

## Sources

- Ilmanen, Antti. *Expected Returns* (2011), chapters on return distributions and alternative risk premia.
- Harvey, Campbell and Siddique, Akhtar. "Conditional Skewness in Asset Pricing Tests," *Journal of Finance* (2000).
- Brunnermeier, Markus, Nagel, Stefan, and Pedersen, Lasse. "Carry Trades and Currency Crashes," *NBER Macroeconomics Annual* (2008).
- Cont, Rama. "Empirical properties of asset returns: stylized facts and statistical issues," *Quantitative Finance* (2001).
