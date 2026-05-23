---
aliases: [expected shortfall, CVaR, conditional VaR, conditional value at risk, ES, tail VaR, average tail loss]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-03-24"
---

# Expected Shortfall

## Definition

Expected Shortfall (ES), also called Conditional Value at Risk (CVaR), is the average loss conditional on a loss worse than [[Value at Risk]]. If 99% VaR is $500,000, ES asks: on those 1% worst days, what is the average loss? The answer might be $1.2 million. VaR is the cliff edge; ES is the average depth of the canyon below. ES is strictly better than VaR for any trader who cares about survival because it captures tail severity, not just the threshold. The Basel Committee's Fundamental Review of the Trading Book (FRTB) replaced VaR with ES as the primary regulatory measure for this reason.

## Why it matters (commodities and FX)

In commodities, the gap between VaR and ES is large because of fat tails. A crude portfolio might have 99% 1-day VaR of $1 million but ES of $3.5 million — when VaR breaches, the average loss is 3.5x the threshold. For natural gas or soft commodities (cocoa, coffee), the ratio is higher due to extreme [[Kurtosis]].

This matters for sizing: position sized to survive VaR can still be wiped out by an actual tail event. Sizing to survive ES is more conservative but far more robust. It also matters for margin: CME and ICE models increasingly use ES type calculations, so understanding ES helps anticipate margin calls during stress.

## Concrete example

**Concrete:** A trader holds long [[Cocoa Futures]] (100 lots at $8,000/tonne) and long [[Coffee Futures]] (50 lots at $4.50/lb). Using 500 days of historical data, sort daily P&L worst to best. The 5 worst days (1% of 500):
- −$2,800,000
- −$2,200,000
- −$1,900,000
- −$1,600,000
- −$1,500,000

**99% VaR** = $1,500,000 (the 5th worst, boundary of the worst 1%).
**99% Expected Shortfall** = average of the 5 worst = **$2,000,000**.

ES is 33% larger than VaR. A trader sized to survive $1.5M but not $2.0M faces a margin call or forced liquidation on the worst days. For agricultural commodities with extreme tails, ES/VaR often exceeds 2x.

**Simplified:** VaR tells you the threshold (1 day in 100 you lose at least X). It says nothing about how bad it gets beyond X. ES averages the losses on those tail days. For normal returns, ES is only 13% larger than VaR. For fat tailed assets, ES can be 2 to 3x VaR. Sizing to survive ES means you survive an actual tail event, not just touch its edge.

## Key mechanics and formulas

### Definition

**ES_alpha = E[Loss | Loss > VaR_alpha]**

The expected loss conditional on the loss exceeding the VaR threshold at confidence alpha.

### Calculation Methods

**Historical ES:**
1. Compute daily P&L for the lookback window (e.g., 500 days)
2. Sort worst to best
3. Identify the worst (1 − alpha)% of days
4. ES = average P&L of those days

**Parametric ES (normal distribution):**

`ES = Position × sigma × phi(z_alpha) / (1 − alpha)`

- phi(z_alpha) = standard normal density at the z score
- 99%: ES = Position × sigma × phi(2.33) / 0.01 = Position × sigma × 2.64
- Compare parametric VaR = Position × sigma × 2.33

ES/VaR ratio under normality: 2.64 / 2.33 = 1.13. Under fat tails: 1.5 to 3+.

**Monte Carlo ES:**
1. Simulate thousands of scenarios
2. Compute P&L per scenario
3. Sort and average the worst (1 − alpha)% of outcomes

### ES vs VaR Comparison

| Property | VaR | Expected Shortfall |
|----------|-----|--------------------|
| Question answered | "Loss threshold at the Xth percentile?" | "Average loss beyond that threshold?" |
| Tail sensitivity | None | Full (averages the entire tail) |
| Subadditivity | Not subadditive (portfolio VaR can exceed sum of parts) | Subadditive (portfolio ES ≤ sum of parts) |
| Regulatory status | Replaced by ES under FRTB (Basel III.1) | Primary regulatory measure under FRTB |
| Computation | Simpler | Slightly more complex |
| Backtesting | Easier (binary) | Harder (needs magnitude) |

### Subadditivity

ES is **subadditive**: ES(A + B) ≤ ES(A) + ES(B). Diversification always reduces ES, which is mathematically desirable. VaR is not subadditive: combining two portfolios can raise VaR, which is logically incoherent for a risk measure.

## Prerequisites

- [[Value at Risk]]
- [[Tail Risk]]
- [[Volatility]]

## Related concepts (learn next)

- [[Value at Risk]] because ES is defined relative to VaR and the two are always used together.
- [[Tail Risk]] because ES is designed to measure tail severity that VaR ignores.
- [[Maximum Drawdown]] because drawdown captures multi day cumulative losses while ES focuses on single period tails. Together they cover tail risk across timeframes.
- [[Kurtosis]] because fat tails drive the ES/VaR ratio above 1.13.
- [[Skewness]] because negative skew makes the left tail heavier, raising ES relative to VaR.
- [[Margin]] because exchange models increasingly use ES type calculations for initial margin.

## Common misconceptions

**"ES is just a slightly bigger VaR."** Under normality, ES is 13% larger at 99%. Commodity returns are not normal. In practice ES runs 2 to 3x VaR for fat tailed assets like cocoa, natural gas, or EM currencies. The difference is material for survival.

**"ES is harder to backtest, so VaR is more practical."** ES is harder to backtest (you need magnitudes beyond VaR, not just breach counts), but that is a data problem, not a conceptual one. Difficulty does not make VaR a better risk measure.

**"ES solves fat tails."** ES better captures tail severity but still depends on data or model. Historical ES only captures tail events in the lookback. If your window omits a crisis, ES understates. Monte Carlo ES is only as good as its distribution.

## Sources

- Acerbi, Carlo and Tasche, Dirk. "On the coherence of Expected Shortfall," *Journal of Banking and Finance* (2002).
- Basel Committee on Banking Supervision. *Minimum capital requirements for market risk* (FRTB, 2019).
- McNeil, Frey, and Embrechts. *Quantitative Risk Management: Concepts, Techniques and Tools* (2015).
- Rockafellar, R.T. and Uryasev, S. "Conditional Value at Risk for General Loss Distributions," *Journal of Banking and Finance* (2002).
