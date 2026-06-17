---
aliases: [ITM, in the money, in-the-money, deep ITM, deep in the money]
tags:
  - "#quant"
  - "#fx"
date-added: "2026-06-18"
---

# ITM

## Definition

An option is in the money (ITM) when exercising it right now would put cash in your pocket, ignoring the premium you paid. A call is ITM when the [[underlying]] trades above the [[Strike Price]]: you hold the right to buy cheap and sell at the higher market. A put is ITM when the underlying trades below the strike: you hold the right to sell high into a lower market. The amount you would collect on immediate exercise is the [[intrinsic value]]. The further ITM, the more the option behaves like the underlying itself and the less its price depends on [[Implied Volatility]]. The benchmark for "above" or "below" is conventionally the [[forward rate]], the same reference [[ATM]] uses, not spot.

## Why it matters (commodities and FX)

Moneyness decides what an option actually is. A deep ITM option has [[Delta]] near 100 (or −100 for a put), so it tracks the underlying almost one for one. Traders use deep ITM calls as a financed, lower capital substitute for owning [[Brent Crude]] or [[Gold Futures]] outright, with a built in stop at the strike. ITM options carry intrinsic value, so they cost more premium than [[OTM]] strikes, but they decay less per day ([[Theta]] is small relative to premium) because most of their value is intrinsic, not [[time value]]. On American style commodity options, deep ITM also raises early exercise and assignment risk, which matters for anyone short the strike. In FX, the ITM/OTM split relative to the forward is exactly what the [[Risk Reversal]] prices: which side of the [[Vol Surface]] the market pays up for.

## Concrete example

**Concrete:** WTI front month at $78. Trader buys 1 December $70 call (ITM by $8) for a premium of $9.50/bbl. Intrinsic value = $78 − $70 = $8. Time value = $9.50 − $8 = $1.50. Delta ≈ 85. WTI rallies to $86 by expiry: the call is worth $16 intrinsic. P&L = $16 − $9.50 = +$6.50/bbl, +650% of the $1.50 time value at risk relative to an ATM bet, because 85% of every dollar of crude moved into the option. Fail case: WTI drifts to $72. Call worth $2 intrinsic, time value gone. P&L = $2 − $9.50 = −$7.50/bbl. The $8 of intrinsic you paid for is exactly the capital most exposed if crude falls back toward the strike. Below $70 the call expires worthless and you lose the full $9.50.

**Simplified:** ITM means the option already has real exercise value baked in. A call is ITM when price is above the strike; a put when price is below. Deep ITM options move almost like the underlying and decay slowly, but you pay for that with a fat premium, most of which is intrinsic value you can lose if the market reverses toward the strike.

## Key mechanics and formulas

- **Call intrinsic value** = max(forward − strike, 0). ITM when forward > strike.
- **Put intrinsic value** = max(strike − forward, 0). ITM when forward < strike.
- **Option premium** = intrinsic value + [[time value]]. For ITM options, intrinsic is the larger component; for deep ITM it is nearly all of it.
- **Delta**: ITM call delta runs 50 to 100; deep ITM approaches 100. ITM put delta runs −50 to −100. Delta is the rough probability the option finishes ITM, plus the underlying exposure per unit.
- **Moneyness ratio** = forward / strike (calls) or strike / forward (puts). Above 1 means ITM.
- **Gamma and Theta are low** for deep ITM relative to [[ATM]]: little convexity left to gain, little time value left to lose.

## Prerequisites
- [[Strike Price]]
- [[intrinsic value]]
- [[Vanilla Option]]
- [[Delta]]
- [[forward rate]]

## Related concepts (learn next)
- [[ATM]]: the balance point between ITM and OTM, zero intrinsic value, maximum time value.
- [[OTM]]: the mirror case, all time value and no intrinsic value, the cheap lottery side.
- [[Moneyness]]: the umbrella concept spanning ITM, ATM, and OTM.
- [[intrinsic value]]: the exercise value that defines being ITM.
- [[time value]]: the rest of the premium, smallest for deep ITM.
- [[Delta]]: rises toward 100 the deeper ITM you go.
- [[Risk Reversal]]: prices the relative cost of ITM vs OTM strikes across the skew.

## Common misconceptions

**"ITM options are safer than OTM."** Higher win probability, but you risk far more capital per contract. The intrinsic value you pay is fully at risk if the underlying reverses through the strike. Lower probability of total loss, larger loss when it happens.

**"Deep ITM options have no time value, so they cannot lose money on time."** They have little time value, but it is not zero until expiry, and the intrinsic component still moves dollar for dollar against you if the underlying falls toward the strike.

**"An ITM option will always be exercised."** On European options you cannot exercise early; value is realized at expiry or by selling. Even at expiry, brokers may not auto exercise marginally ITM positions, and pin risk near the strike can leave assignment uncertain.

## Sources
- Hull, John. *Options, Futures, and Other Derivatives*, 10th ed., chapter on properties of options.
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- CME Group. "Options on Futures: Moneyness and Exercise."
