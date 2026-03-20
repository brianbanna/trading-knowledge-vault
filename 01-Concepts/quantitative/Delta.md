---
aliases: [delta, option delta, hedge ratio]
tags:
  - "#quant"
  - "#fx"
date-added: "2026-03-20"
---

# Delta

## Definition
Delta measures the sensitivity of an option's price to a small change in the price of the [[underlying]] asset. A call with a delta of 0.25 (25D) gains approximately 0.25 units of value for each 1 unit move in spot. Delta also serves as a rough proxy for the probability that the option expires in the money, so a 25D call has roughly a 25% chance of finishing with positive intrinsic value. In FX markets, options are quoted by delta (10D, 25D, [[ATM]]) rather than by absolute strike, which standardizes the vol surface across currency pairs. Delta is the first and most important of the [[Greeks]] because it determines the [[hedge ratio]]: to delta hedge a long call position, you sell delta units of the underlying per option.

## Why it matters (commodities and FX)
Delta is the primary risk metric for any options book. FX dealers continuously delta hedge their portfolios, and the aggregate delta hedging flow from large option positions can move spot markets, especially near [[Expiry Pinning]] events. The 25 delta level defines the standard [[Risk Reversal]] and [[Butterfly]] quotes that characterize the [[Vol Surface]]. In commodities, delta hedging of producer put positions on [[Brent Crude]] or [[WTI Crude Oil]] creates predictable buying pressure when prices fall, amplifying moves. Understanding whether a market is "long gamma" or "short gamma" at various spot levels depends entirely on the distribution of delta across outstanding options.

## Concrete example
**Success:** A trader buys a 1 month EUR/USD 25D call (strike 1.0950, spot 1.0800) for 22 pips. Delta is 0.25, so the trader sells EUR 2.5 million against a EUR 10 million notional to be delta neutral. Spot rallies to 1.0900; the option gains approximately 25 pips from delta and additional gains from [[Gamma]]. The delta hedge lost 25 pips on the EUR 2.5 million short, but the gamma gain on the option exceeds the hedge loss. Net P&L is positive 8 pips per million notional.

**Failure:** A trader is short a 25D USD/JPY put (strike 148.00, spot 151.00) with delta of negative 0.25 and has bought USD to hedge. The BOJ intervenes and spot gaps from 151.00 to 145.00 in minutes. Delta jumps from 0.25 to 0.85 instantaneously, but the trader can only rehedge at 145.00. The gap created a realized loss of approximately 250 pips per million notional that delta hedging could not capture because [[Gamma]] risk materialized as a discontinuous move.

## Key mechanics and formulas
- **Call delta** = e^(negative foreign rate × time) × N(d1), where d1 = [ln(spot / strike) + (rate differential + 0.5 × vol²) × time] / (vol × sqrt(time))
- **Put delta** = call delta minus e^(negative foreign rate × time), always negative
- **Delta hedge ratio** = delta × notional; sell this amount of underlying to be delta neutral
- **Delta as probability proxy** = N(d2) is the risk neutral probability of finishing in the money, which is close to but not identical to delta
- **Spot delta vs. forward delta**: spot delta includes the discounting factor; forward delta strips it out. FX conventions vary by currency pair
- **Premium adjusted delta**: in pairs where premium is paid in foreign currency (e.g., EUR/USD premium in EUR), delta is adjusted: premium adjusted delta = delta minus (option value / spot)

## Prerequisites
- [[Vanilla Option]]
- [[Implied Volatility]]
- [[Forward Curve]]
- [[Hedging]]
- [[Normal Distribution]]

## Related concepts (learn next)
- [[Gamma]]: the rate at which delta changes, critical for understanding rehedging costs
- [[Risk Reversal]]: defined as the difference between 25D call vol and 25D put vol
- [[Vol Surface]]: organized by delta (10D, 25D, ATM) on one axis and tenor on the other
- [[Vega]]: like delta but for volatility; options desks manage both simultaneously
- [[Vanna]]: the sensitivity of delta to changes in vol, a second order cross greek
- [[Expiry Pinning]]: large delta hedging flows near expiry can pin spot to a strike
- [[ATM]]: the delta neutral straddle strike, where call delta equals approximately 50

## Common misconceptions
1. **"Delta equals the probability of expiring in the money."** Delta approximates this probability but is not identical. The actual risk neutral probability is N(d2), not N(d1). The difference grows for longer dated or higher vol options.
2. **"Delta hedging eliminates all risk."** Delta hedging removes only first order directional risk. [[Gamma]], [[Vega]], [[Theta]], and higher order risks remain. In gapping markets, delta hedging fails entirely.
3. **"A 50 delta option is ATM."** In FX, the ATM convention (delta neutral straddle) produces a delta that can deviate from exactly 50 depending on the premium currency convention and interest rate differential.
4. **"Delta is constant."** Delta changes continuously with spot ([[Gamma]]), with vol ([[Vanna]]), and with time. Managing these second order sensitivities is the core skill of options market making.

## Sources
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Bossens, Frédéric et al. "Vanna-Volga Methods Applied to FX Derivatives," *International Journal of Theoretical and Applied Finance*, 2010.
