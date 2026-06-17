---
aliases: [Extrinsic Value, Time Premium]
tags:
  - "#quant"
date-added: "2026-06-18"
---

# Time Value

## Definition
Time value is the slice of an option [[Premium]] that sits above its [[Intrinsic Value]]. In plain terms, it is what the market charges you for the chance that the option gains more intrinsic value before it dies. It exists because while time remains, the underlying can still move in your favor, and that possibility has a price. Time value decays to exactly zero at [[Expiration]], and the rate of that decay is [[Theta]], which is largest for [[ATM]] options and accelerates as expiry approaches. The two main drivers are [[Implied Volatility]] (more expected movement means more time value) and time remaining (more time means more chances).

## Why it matters (commodities and FX)
Time value is the cost of being an option buyer and the income of being an option seller. A trader buying a [[Gold Futures]] call is paying for time value every day they hold it, and that bleed is relentless if the market sits still. Commodity and FX markets often have sharp event risk, central bank meetings, OPEC decisions, inventory reports, which spikes [[Implied Volatility]] and inflates time value. Knowing how fast time value decays tells you whether you are paying a fair price for the chance of a move, or financing someone else's [[Theta]] income.

## Concrete example
**Concrete:** You buy an [[ATM]] [[Gold Futures]] call. Spot gold is $2,000 per ounce, [[Strike Price]] is $2,000, expiry is 30 days out, and you pay a [[Premium]] of $35 per ounce. Because the option is exactly at the money, [[Intrinsic Value]] = max(2,000 - 2,000, 0) = $0. The entire $35 premium is time value.

Win case. Over the next 20 days gold rallies to $2,050 on a surge in [[Implied Volatility]]. Intrinsic value becomes max(2,050 - 2,000, 0) = $50. Even though 20 days of time decay have eaten part of the original $35, the option now trades around $60: $50 intrinsic plus roughly $10 residual time value. The move materialized faster than [[Theta]] could erode the premium, so you profit.

Fail case. Gold instead sits flat near $2,000 for 30 days and volatility drifts lower. Intrinsic value stays at $0. As [[Expiration]] approaches the $35 of time value bleeds away, decay accelerating in the final days, until at expiry the option is worth max(2,000 - 2,000, 0) = $0. You lose the full $35 per ounce. Nothing was ever wrong with the strike; time simply ran out.

**Simplified:** Time value is the price of hope. An at the money option is all hope and no hard cash, so its whole premium is time value. If the market moves your way in time you win. If it sits still, time value melts to zero and you lose what you paid.

## Key mechanics and formulas
- Time Value = [[Premium]] - [[Intrinsic Value]].
- At [[Expiration]] time value = 0, so Premium = Intrinsic Value.
- Decay rate per unit time is [[Theta]] (typically negative for a long option holder).
- Time value is largest for [[ATM]] options and decays fastest into expiry (decay is roughly proportional to the square root of time remaining for ATM options, so it steepens near the end).
- Rises with [[Implied Volatility]] and with time to expiry, falls as either shrinks.
- Deep [[ITM]] and deep [[OTM]] options carry little time value; ATM carries the most.

## Prerequisites
- [[Intrinsic Value]] and the max(., 0) payoff floor.
- [[Premium]] as total option price.
- [[Expiration]] and the option lifecycle.
- Basic feel for [[Implied Volatility]].

## Related concepts (learn next)
- [[Intrinsic Value]]: the other half of the premium, the part that is already real.
- [[Premium]]: the total price that decomposes into intrinsic and time value.
- [[Theta]]: the Greek that measures how fast time value decays per day.
- [[Implied Volatility]]: the main lever that inflates or deflates time value.
- [[ATM]]: the moneyness state that carries the most time value.
- [[OTM]]: a state where the premium is entirely time value with zero intrinsic value.
- [[Expiration]]: the moment time value reaches zero.

## Common misconceptions
- "Time value decays in a straight line." Wrong. Decay accelerates as expiry nears, especially for [[ATM]] options, because there is progressively less time for a saving move to occur. The bleed in the final week dwarfs the bleed months out.
- "A flat market is harmless if I am right about direction long term." Wrong. If the market does not move before [[Expiration]], time value erodes to zero and a held option can expire worthless even if your thesis later proves correct.
- "Higher implied volatility always means a better trade." Wrong. High [[Implied Volatility]] inflates the time value you pay up front. If the realized move is smaller than the implied move priced in, you overpaid and lose even when the market drifts your way.
- "Deep in the money options have lots of time value." Wrong. They are dominated by [[Intrinsic Value]] and carry little time value, because there is little uncertainty left about whether they finish in the money.

## Sources
- Hull, Options, Futures, and Other Derivatives.
- Natenberg, Option Volatility and Pricing.
