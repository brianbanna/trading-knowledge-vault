---
aliases: [realized volatility, realized vol, historical volatility]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Realized Volatility

## Definition
Realized volatility (RV) is the actual annualized standard deviation of returns observed in the [[underlying]] asset over a specific historical period. Unlike [[implied volatility]], which is forward looking and derived from option prices, realized vol is backward looking and computed directly from price data. The standard calculation uses close to close log returns, though variants exist (open to close, high low, Parkinson, Garman-Klass) that capture intraday information. Realized vol is the benchmark against which option traders measure whether they overpaid or underpaid for [[Volatility]]. When realized vol comes in below implied vol, option sellers profit; when it exceeds implied, buyers profit.

## Why it matters (commodities and FX)
The spread between [[implied volatility]] and realized volatility (the "vol risk premium") is one of the most important quantities in options trading. In FX, implied vol on major pairs like EUR/USD typically trades 1 to 2 vol points above realized, creating a structural opportunity for systematic vol sellers. In commodities, [[Brent Crude]] and [[Henry Hub Natural Gas]] show volatile RV regimes: quiet periods with 15% annualized RV punctuated by spikes above 50%. Monitoring RV relative to implied helps traders decide whether to be long or short [[Vega]]. A trader who buys a [[Straddle]] at 8% implied vol and delta hedges is effectively betting that realized vol will exceed 8% over the option's life.

## Concrete example
**Success:** EUR/USD 1 month implied vol is 8.5%. A systematic fund computes trailing 1 month realized vol at 6.2% and sells the 1 month ATM [[Straddle]], collecting 120 pips. Over the next month, realized vol stays at 6.0%. The straddle expires with only 30 pips of intrinsic value. Net profit is 90 pips. The vol risk premium of 2.5 points (8.5 minus 6.0) was captured.

**Failure:** A vol selling fund shorts USD/MXN 1 month straddles at 12% implied vol, noting trailing RV is only 9%. A week later, Mexico's president announces a surprise nationalization policy, and USD/MXN gaps 8% in 2 days. Realized vol spikes to 35% annualized. The short straddle loses 800 pips, far exceeding the 150 pip premium collected. Backward looking RV gave no warning of the regime change.

## Key mechanics and formulas
- **Close to close RV** = sqrt(252 / n × sum of (ln(close_i / close_{i minus 1}))² for i = 1 to n), where 252 is the annualization factor for daily data
- **Parkinson (high low) estimator** = sqrt(252 / (4 × n × ln(2)) × sum of (ln(high_i / low_i))²), more efficient because it uses intraday range
- **Garman-Klass estimator**: uses open, high, low, close for even greater efficiency
- **Yang-Zhang estimator**: combines overnight (close to open) and intraday (open to close) components, robust to drift
- **Vol risk premium** = implied vol minus subsequent realized vol; positive on average in most markets
- **RV sampling windows**: common choices are 5 day, 10 day, 21 day, 63 day, corresponding roughly to 1 week, 2 weeks, 1 month, 3 months

## Prerequisites
- [[Volatility]]
- [[Implied Volatility]]
- [[Standard Deviation]]
- [[Log Returns]]
- [[ATM]]

## Related concepts (learn next)
- [[Implied Volatility]]: the forward looking counterpart; the spread between implied and realized is the core options trading signal
- [[Vol Surface]]: implied vol surface changes are tradeable when they diverge from realized vol dynamics
- [[Straddle]]: the standard vehicle for expressing a realized vs. implied vol view
- [[Gamma]]: delta hedged P&L is proportional to (realized vol² minus implied vol²) × gamma × spot²
- [[Theta]]: the daily cost of carrying long gamma, offset only if realized vol exceeds implied
- [[Vega]]: sensitivity to implied vol changes, distinct from realized vol exposure
- [[Regime Shift]]: RV can jump discontinuously between regimes, breaking backward looking models
- [[Structural Break]]: events that permanently change the RV regime

## Common misconceptions
1. **"Realized vol predicts future vol."** RV is backward looking and can change regime instantaneously. A market with 6% trailing RV can realize 25% next week if a shock occurs.
2. **"Selling vol is always profitable because implied exceeds realized on average."** The vol risk premium exists on average, but the distribution of outcomes is heavily skewed. Occasional large losses from vol spikes can exceed cumulative premium collected.
3. **"Close to close RV captures all volatility."** Close to close estimators miss intraday moves entirely. A market that gaps up 2% and closes unchanged shows zero daily return but significant intraday vol. Use high low or tick based estimators for a fuller picture.
4. **"Higher realized vol means higher future implied vol."** While correlated, the relationship is not mechanical. Markets can have high RV with falling implied vol if the market believes the volatility episode is temporary.

## Sources
- Gatheral, Jim. *The Volatility Surface: A Practitioner's Guide*.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Parkinson, Michael. "The Extreme Value Method for Estimating the Variance of the Rate of Return," *Journal of Business*, 1980.
- Yang, Dennis and Zhang, Qiang. "Drift Independent Volatility Estimation Based on High, Low, Open, and Close Prices," *Journal of Business*, 2000.
