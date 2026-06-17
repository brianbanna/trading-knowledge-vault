---
aliases: [In the Money, At the Money, Out of the Money]
tags:
  - "#quant"
date-added: "2026-06-18"
---

# Moneyness

## Definition
Moneyness describes the relationship between an option's [[Strike Price]] and the current spot or forward price of the underlying. Plain English: it tells you whether exercising the option right now would make money, break even, or lose money. It is the umbrella concept that spans the three states [[ITM]] (in the money), [[ATM]] (at the money), and [[OTM]] (out of the money). Moneyness determines how an option's [[Premium]] splits between [[Intrinsic Value]] and [[Time Value]], and it roughly maps to [[Delta]], which can be read as the probability of finishing in the money. As the underlying moves, an option slides along this spectrum while its strike stays fixed.

## Why it matters (commodities and FX)
Moneyness is the lens a trader uses to judge cost, leverage, and odds in one glance. A deep ITM crude call behaves almost like a long futures position with little time value, while a far OTM call is a cheap lottery ticket with low delta. An FX hedger choosing between an ATM and an OTM EUR/USD put is trading off premium cost against the protection level. Because moneyness drives the intrinsic versus time value split, it tells you how much you are paying for optionality rather than for value already embedded, which is central to whether the structure fits the view.

## Concrete example
**Concrete:** [[WTI Crude Oil]] trades at $80.00/bbl. Consider the same $90 [[Strike Price]] on two different options.
- A $90 [[Call Option]]: the strike is above the $80 market, so it is OTM. It has zero [[Intrinsic Value]]; its entire premium is [[Time Value]]. With spot $10 below the strike, its [[Delta]] might be around 0.20, implying roughly a 20% chance of finishing ITM. If WTI rallies to $95 by expiry it becomes ITM with $5/bbl intrinsic value; if WTI stays at $80 it expires worthless and the buyer loses the full premium.
- A $90 [[Put Option]]: the same $90 strike is above the $80 market, so for a put it is ITM. It carries $10/bbl intrinsic value ($90 minus $80) plus some time value, and its delta is near -0.80. If WTI falls to $75 the put gains further to $15/bbl intrinsic; if WTI rallies to $90 it loses its intrinsic value and the buyer can still lose the time value paid.

**Simplified:** Moneyness is whether the strike is favorable versus the current price. The exact same $90 strike on $80 crude is an OTM call but an ITM put. ITM options carry intrinsic value; OTM options are pure time value.

## Key mechanics and formulas
- Call: S > K is ITM, S = K is ATM, S < K is OTM, where S is the underlying price and K is the [[Strike Price]].
- Put: S < K is ITM, S = K is ATM, S > K is OTM.
- Intrinsic value (call) = max(0, S - K); intrinsic value (put) = max(0, K - S). Only ITM options have positive intrinsic value.
- Premium = [[Intrinsic Value]] + [[Time Value]]. ATM and OTM options have zero intrinsic value, so their premium is all time value. Deep ITM options are mostly intrinsic value.
- |[[Delta]]| approximates the risk neutral probability of finishing ITM: near 0 for deep OTM, near 0.50 for ATM, near 1.0 for deep ITM.

## Prerequisites
- [[Strike Price]]
- [[Option]]
- [[Call Option]]
- [[Put Option]]

## Related concepts (learn next)
- [[ITM]] because it is the in the money end of the spectrum where options carry intrinsic value.
- [[ATM]] because it is the midpoint where time value peaks and delta sits near 0.50.
- [[OTM]] because it is the out of the money end where premium is pure time value.
- [[Intrinsic Value]] because moneyness directly determines how much intrinsic value an option holds.
- [[Time Value]] because the share of premium that is time value depends on where the option sits on the moneyness scale.
- [[Delta]] because moneyness maps to delta as a rough probability of finishing in the money.
- [[Premium]] because the moneyness state explains why two strikes on the same underlying cost very different amounts.

## Common misconceptions
- "ATM means the option is free or worthless." Wrong: an ATM option has zero intrinsic value but the most time value of any strike, so it is often the most expensive on a per unit of time value basis.
- "OTM options are cheap so they are low risk." Wrong: low premium reflects low probability of paying off. OTM buyers usually lose the entire premium because the option expires worthless most of the time.
- "Delta is the exact probability of finishing in the money." Wrong: delta is only an approximation of that probability under risk neutral assumptions, and it also reflects the option's price sensitivity, not just odds.
- "Moneyness is fixed for a given option." Wrong: moneyness changes continuously as the underlying moves, even though the [[Strike Price]] never changes.

## Sources
- CME Group, "Options on Futures" and moneyness explainer guides.
- John C. Hull, "Options, Futures, and Other Derivatives," chapters on option value and the Greeks.
- ICE, FX and energy options product specifications.
