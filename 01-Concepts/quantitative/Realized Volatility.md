---
aliases: [realized volatility, realized vol, historical volatility]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Realized Volatility

## Definition
Realized volatility (RV) is the actual annualized standard deviation of returns observed in the [[underlying]] over a historical period. Unlike [[implied volatility]], which is forward looking and derived from option prices, RV is backward looking and computed directly from price data. The standard calculation uses close to close log returns. Variants (open to close, high low, Parkinson, Garman-Klass) capture intraday information. RV is the benchmark against which option traders judge whether they overpaid or underpaid for [[Volatility]]. When realized comes in below implied, option sellers profit; above, buyers profit.

## Why it matters (commodities and FX)
The spread between [[implied volatility]] and RV (the "vol risk premium") is one of the most important quantities in options trading. In FX, implied on EURUSD trades 1 to 2 vol points above realized, a structural opportunity for systematic vol sellers. In commodities, [[Brent Crude]] and [[Henry Hub Natural Gas]] show volatile RV regimes: quiet 15% periods punctuated by spikes above 50%. Monitoring RV vs implied tells you whether to be long or short [[Vega]]. Buying a [[Straddle]] at 8% implied and delta hedging is a bet that realized exceeds 8% over the option's life.

## Concrete example

**Concrete:** EURUSD 1 month implied vol at 8.5%. Systematic fund computes trailing 1 month RV at 6.2% and sells the 1 month ATM [[Straddle]], collecting 120 pips. Over the month, RV stays at 6.0%. Straddle expires with 30 pips intrinsic. Net 90 pips. The 2.5 point vol risk premium was captured. Contrast: a vol selling fund shorts USDMXN 1 month straddles at 12% implied (trailing RV 9%). A week later Mexico's president announces a surprise nationalization. USDMXN gaps 8% in 2 days. RV spikes to 35% annualized. The short straddle loses 800 pips vs the 150 pips collected. Backward looking RV gave no warning of the regime change.

**Simplified:** Realized vol is what the market actually did. Implied vol is what the market thinks it will do. If you own an option and the market moves more than the implied predicted, you make money via delta hedging. If you sold the option and the market moves less, you keep the premium. The trade is straightforward when realized is stable. The killer is the regime shift: yesterday's quiet market is no guide when news hits.

## Key mechanics and formulas
- **Close to close RV** = sqrt(252 / n × sum of (ln(close_i / close_{i-1}))² for i = 1 to n), 252 = annualization factor for daily data
- **Parkinson (high low) estimator** = sqrt(252 / (4 × n × ln(2)) × sum of (ln(high_i / low_i))²), more efficient via intraday range
- **Garman-Klass estimator**: uses open, high, low, close for greater efficiency
- **Yang-Zhang estimator**: combines overnight (close to open) and intraday (open to close), robust to drift
- **Vol risk premium** = implied vol minus subsequent realized; positive on average in most markets
- **RV sampling windows**: 5, 10, 21, 63 day correspond to 1 week, 2 weeks, 1 month, 3 months

## Prerequisites
- [[Volatility]]
- [[Implied Volatility]]
- [[Standard Deviation]]
- [[Log Returns]]
- [[ATM]]

## Related concepts (learn next)
- [[Implied Volatility]]: forward looking counterpart. The spread between implied and realized is the core options signal.
- [[Vol Surface]]: implied surface changes are tradeable when they diverge from RV dynamics.
- [[Straddle]]: standard vehicle for expressing realized vs implied vol view.
- [[Gamma]]: delta hedged P&L is proportional to (RV² minus implied²) × gamma × spot².
- [[Theta]]: daily cost of long gamma, offset only if realized exceeds implied.
- [[Vega]]: sensitivity to implied changes, distinct from realized exposure.
- [[Regime Shift]]: RV jumps discontinuously between regimes, breaking backward looking models.
- [[Structural Break]]: events that permanently change the RV regime.

## Common misconceptions
1. **"Realized vol predicts future vol."** RV is backward looking and changes regime instantaneously. A market at 6% trailing RV realizes 25% next week on a shock.
2. **"Selling vol is always profitable because implied exceeds realized on average."** The premium exists on average; the distribution is heavily skewed. Occasional large losses from vol spikes exceed cumulative premium.
3. **"Close to close RV captures all volatility."** It misses intraday moves entirely. A market that gaps up 2% and closes unchanged shows zero daily return but significant intraday vol. Use high low or tick estimators.
4. **"Higher realized vol means higher future implied vol."** Correlated, not mechanical. Markets show high RV with falling implied if the vol episode is judged temporary.

## Sources
- Gatheral, Jim. *The Volatility Surface: A Practitioner's Guide*.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Parkinson, Michael. "The Extreme Value Method for Estimating the Variance of the Rate of Return," *Journal of Business*, 1980.
- Yang, Dennis and Zhang, Qiang. "Drift Independent Volatility Estimation Based on High, Low, Open, and Close Prices," *Journal of Business*, 2000.
