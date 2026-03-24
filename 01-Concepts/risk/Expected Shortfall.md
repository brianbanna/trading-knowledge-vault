---
aliases: [expected shortfall, CVaR, conditional VaR, conditional value at risk, ES, tail VaR, average tail loss]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-03-24"
---

# Expected Shortfall

## Definition

Expected Shortfall (ES), also called Conditional Value at Risk (CVaR), is the average loss you suffer when things go worse than [[Value at Risk]]. If your 99% VaR is $500,000, Expected Shortfall asks: "On those 1% worst days, what is the average loss?" The answer might be $1.2 million. Think of VaR as the edge of a cliff. Expected Shortfall tells you the average depth of the canyon below. This makes ES a strictly better risk measure than VaR for any trader who cares about survival, because it captures the severity of tail events, not just their threshold. The Basel Committee's Fundamental Review of the Trading Book (FRTB) replaced VaR with Expected Shortfall as the primary regulatory risk measure for exactly this reason.

## Why it matters (commodities and FX)

In commodity markets, the gap between VaR and Expected Shortfall is enormous because of fat tails. A crude oil portfolio might have a 99% 1 day VaR of $1 million, but an Expected Shortfall of $3.5 million, meaning that when VaR is breached, losses average 3.5x the VaR boundary. For natural gas or soft commodities (cocoa, coffee), this ratio can be even higher due to extreme [[Kurtosis]].

This matters for position sizing: if you size positions to survive a VaR level breach, you may still be wiped out by an actual tail event. Sizing to survive your Expected Shortfall is more conservative but far more robust. It also matters for margin: CME and ICE margin models increasingly incorporate ES type calculations, so understanding ES helps you anticipate margin calls during volatile periods.

## Concrete example

A trader has a portfolio of long [[Cocoa Futures]] (100 lots at $8,000/tonne) and long [[Coffee Futures]] (50 lots at $4.50/lb). Using 500 days of historical data:

**Step 1:** Compute daily P&L for each of the 500 days using current positions.

**Step 2:** Sort from worst to best. The 5 worst days (1% of 500):
- Day 1: -$2,800,000
- Day 2: -$2,200,000
- Day 3: -$1,900,000
- Day 4: -$1,600,000
- Day 5: -$1,500,000

**99% VaR** = $1,500,000 (the 5th worst day, the boundary of the worst 1%)

**99% Expected Shortfall** = average of the 5 worst days = ($2,800,000 + $2,200,000 + $1,900,000 + $1,600,000 + $1,500,000) / 5 = **$2,000,000**

The ES is 33% larger than VaR. If the trader sized their position to survive a $1.5M loss (VaR) but not $2.0M (ES), they would face a margin call or forced liquidation on the worst days.

In reality, for agricultural commodities with extreme tails, the ES/VaR ratio often exceeds 2x, meaning tail losses are on average double the VaR threshold.

## Key mechanics and formulas

### Definition

**ES_alpha = E[Loss | Loss > VaR_alpha]**

The expected (average) loss conditional on the loss exceeding the VaR threshold at confidence level alpha.

### Calculation Methods

**Historical ES:**
1. Compute daily P&L for the lookback window (e.g., 500 days)
2. Sort from worst to best
3. Identify the worst (1 - alpha)% of days
4. ES = average P&L of those worst days

**Parametric ES (assuming normal distribution):**

`ES = Position x sigma x phi(z_alpha) / (1 - alpha)`

Where:
- phi(z_alpha) = standard normal density at the z score
- For 99% confidence: ES = Position x sigma x phi(2.33) / 0.01 = Position x sigma x 0.0264 / 0.01 = Position x sigma x 2.64
- Compare to parametric VaR = Position x sigma x 2.33

The ES/VaR ratio under normality: ES_99% / VaR_99% = 2.64 / 2.33 = 1.13. Under fat tails, this ratio is much higher (1.5 to 3+).

**Monte Carlo ES:**
1. Simulate thousands of scenarios from a chosen distribution
2. Compute P&L for each scenario
3. Sort and average the worst (1 - alpha)% of outcomes

### ES vs VaR Comparison

| Property | VaR | Expected Shortfall |
|----------|-----|--------------------|
| Question answered | "What is the loss threshold at the Xth percentile?" | "What is the average loss beyond that threshold?" |
| Tail sensitivity | None (ignores tail severity) | Full (averages over the entire tail) |
| Subadditivity | Not subadditive (portfolio VaR can exceed sum of parts) | Subadditive (portfolio ES <= sum of individual ES) |
| Regulatory status | Replaced by ES under FRTB (Basel III.1) | Primary regulatory measure under FRTB |
| Computation | Simpler | Slightly more complex |
| Backtesting | Easier (binary: breach or not) | Harder (requires magnitude of breaches) |

### Subadditivity

ES is **subadditive**: ES(A + B) <= ES(A) + ES(B). This means diversification always reduces ES, which is mathematically desirable. VaR is NOT subadditive, meaning combining two portfolios can sometimes increase VaR, which is logically incoherent for a risk measure.

## Prerequisites

- [[Value at Risk]]
- [[Tail Risk]]
- [[Volatility]]

## Related concepts (learn next)

- [[Value at Risk]] because ES is defined relative to VaR and the 2 are always used together.
- [[Tail Risk]] because ES is specifically designed to measure the severity of tail events that VaR ignores.
- [[Maximum Drawdown]] because drawdown captures multi day cumulative losses while ES focuses on single period tail losses. Together they cover tail risk across timeframes.
- [[Kurtosis]] because fat tails (high kurtosis) are what drive the ES/VaR ratio above 1.13 (the normal distribution value). The fatter the tails, the more ES exceeds VaR.
- [[Skewness]] because negative skew means the left tail is heavier, further increasing ES relative to VaR.
- [[Margin]] because exchange margin models increasingly use ES type calculations to set initial margin levels.

## Common misconceptions

**"ES is just a slightly bigger VaR."** Under normal distributions, ES is only 13% larger than VaR at 99% confidence. But commodity returns are not normal. In practice, ES can be 2 to 3x VaR for fat tailed assets like cocoa, natural gas, or EM currencies. The difference is material for survival.

**"ES is harder to backtest, so VaR is more practical."** ES is harder to backtest (you need to assess the magnitude of losses beyond VaR, not just count breaches), but this is a data problem, not a conceptual one. The difficulty of backtesting does not make VaR a better risk measure. It just makes ES less convenient.

**"ES solves the fat tail problem."** ES better captures tail severity, but it still depends on the data or model used to estimate it. Historical ES only captures tail events that occurred in your lookback window. If your window does not include a crisis, ES will still understate risk. Monte Carlo ES is only as good as its distributional assumptions.

## Sources

- Acerbi, Carlo and Tasche, Dirk. "On the coherence of Expected Shortfall," *Journal of Banking and Finance* (2002).
- Basel Committee on Banking Supervision. *Minimum capital requirements for market risk* (FRTB, 2019).
- McNeil, Frey, and Embrechts. *Quantitative Risk Management: Concepts, Techniques and Tools* (2015).
- Rockafellar, R.T. and Uryasev, S. "Conditional Value at Risk for General Loss Distributions," *Journal of Banking and Finance* (2002).
