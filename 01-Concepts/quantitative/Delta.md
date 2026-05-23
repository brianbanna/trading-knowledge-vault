---
aliases: [delta, option delta, hedge ratio]
tags:
  - "#quant"
  - "#fx"
date-added: "2026-03-20"
---

# Delta

## Definition

Delta is the change in option price for a $1 change in spot. A 25 delta call gains $0.25 when spot moves up $1. Delta also approximates the probability the option expires in the money: a 25 delta call has roughly a 25% chance of finishing ITM. In FX, options are quoted by delta (10D, 25D, ATM) rather than by strike, which standardizes the vol surface across pairs. To delta hedge a long option, sell `delta × notional` of the underlying.

## Why it matters (commodities and FX)

Delta is the first thing on a dealer's risk screen. FX dealers continuously delta hedge, and the aggregate hedge flow from large option positions moves spot, especially near [[Expiry Pinning]] events. The 25 delta level defines the standard [[Risk Reversal]] and [[Butterfly]] quotes that organize the [[Vol Surface]]. In commodities, producer put hedges on [[Brent Crude]] and [[WTI Crude Oil]] create predictable selling pressure when prices fall, as dealers delta hedge their long puts. Aggregate market delta also tells you whether dealers are net long or short [[Gamma]] at the current spot.

## Concrete example

**Concrete:** Trader buys a 1 month EURUSD 25D call. Strike 1.0950, spot 1.0800, premium 22 pips. Delta 0.25 on EUR 10M notional. Delta hedge: sell EUR 2.5M spot. Spot rallies to 1.0900. Option gains ~25 pips from delta plus ~3 pips from gamma. Spot hedge loses 25 pips on EUR 2.5M. Net: +8 pips per million notional.

**Simplified:** You buy a call. Spot goes up $1. The option is worth roughly delta × $1 more. If delta is 0.25, the option gains $0.25. To not care about the spot move at all, sell 0.25 units of the underlying for each option you own. Now spot can move and your P&L stays flat at the instant of the move. That is delta hedging.

## Key mechanics and formulas

- **Call delta** = e^(-qT) × N(d1), where d1 = [ln(S/K) + (r - q + σ²/2) × T] / (σ × sqrt(T))
- **Put delta** = call delta − e^(-qT), always negative
- **Hedge ratio:** sell `delta × notional` of underlying to be delta flat
- **Delta vs ITM probability:** delta uses N(d1). The true risk neutral ITM probability is N(d2). They diverge for longer dated and higher vol options.
- **Spot vs forward delta:** spot delta discounts, forward delta does not. FX convention varies by pair.
- **Premium adjusted delta:** when premium is paid in the foreign ccy (EUR for EURUSD), delta is adjusted by subtracting option value / spot.

## Prerequisites
- [[Vanilla Option]]
- [[Implied Volatility]]
- [[Forward Curve]]
- [[Hedging]]
- [[Normal Distribution]]

## Related concepts (learn next)
- [[Gamma]]: rate of change of delta. Drives rehedging cost.
- [[Risk Reversal]]: difference between 25D call vol and 25D put vol.
- [[Vol Surface]]: organized by delta on one axis, tenor on the other.
- [[Vega]]: vol sensitivity, managed alongside delta.
- [[Vanna]]: dDelta/dVol, the second order spot/vol cross.
- [[Expiry Pinning]]: aggregate delta hedging flow near expiry can pin spot to a strike.
- [[ATM]]: the delta neutral straddle strike, where call delta is around 0.5.

## Common misconceptions

**"Delta is the probability of expiring ITM."** Close, not exact. The true risk neutral probability is N(d2), not delta's N(d1). The gap widens with vol and tenor.

**"Delta hedging eliminates risk."** It removes first order directional risk only. Gamma, vega, theta, and gap risk all remain. In gapping markets, delta hedging fails completely.

**"50 delta is ATM."** In FX with premium adjusted conventions, the ATM strike (delta neutral straddle) can produce a delta that deviates from 0.50 depending on premium currency and rate differential.

**"Delta is constant."** It moves with spot (gamma), vol (vanna), and time (charm). Managing that drift is the actual job of an options market maker.

## Sources
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Bossens, Frédéric et al. "Vanna-Volga Methods Applied to FX Derivatives," *International Journal of Theoretical and Applied Finance*, 2010.
