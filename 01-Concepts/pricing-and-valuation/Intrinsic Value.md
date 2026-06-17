---
aliases: [Exercise Value, in the money value]
tags:
  - "#quant"
date-added: "2026-06-18"
---

# Intrinsic Value

## Definition
Intrinsic value is the money you would pocket if you could exercise the option right now and immediately close the underlying position. In plain terms, it is the part of the option's worth that is already real, not a bet on the future. For a [[Call Option]] it equals max(S - K, 0), and for a [[Put Option]] it equals max(K - S, 0), where S is the current spot or forward price of the underlying and K is the [[Strike Price]]. The max(., 0) floor means intrinsic value can never be negative, because no rational holder exercises an option at a loss. Any option premium above intrinsic value is [[Time Value]].

## Why it matters (commodities and FX)
Intrinsic value tells you how much of an option's price is hard floor versus how much is hope. A commodity hedger buying downside protection on [[WTI Crude Oil]] wants to know how much of the [[Premium]] buys actual coverage today versus optionality on future moves. It also defines the break between [[ITM]], [[ATM]], and [[OTM]] options: an option has positive intrinsic value only when it is in the money. At [[Expiration]] the entire option price collapses to intrinsic value, so for settlement and risk it is the only number that survives.

## Concrete example
**Concrete:** Consider a [[Call Option]] on [[WTI Crude Oil]] with [[Strike Price]] K = $75 per barrel, and you paid a [[Premium]] of $4 per barrel. The contract covers 1,000 barrels, so the premium cost $4,000.

Win case. WTI rallies and spot is now S = $82. Intrinsic value = max(S - K, 0) = max(82 - 75, 0) = $7 per barrel. The option is worth at least $7,000 in intrinsic terms. After subtracting the $4 premium you paid, your net gain on intrinsic value alone is $3 per barrel, or $3,000. The option is [[ITM]].

Fail case. WTI falls and spot is now S = $70. Intrinsic value = max(70 - 75, 0) = max(-5, 0) = $0. You would never [[Exercise]] the right to buy at $75 when the market sells at $70, so the floor clamps to zero. The option is [[OTM]] and any remaining price is pure [[Time Value]] that erodes toward zero as expiry nears. If it expires here you lose the full $4,000 premium.

**Simplified:** Intrinsic value is the cash already inside the option if you cashed out today. A $75 call with oil at $82 has $7 of it. With oil at $70 it has zero, because you cannot lose money by choosing not to exercise.

## Key mechanics and formulas
- [[Call Option]] intrinsic value: max(S - K, 0).
- [[Put Option]] intrinsic value: max(K - S, 0).
- S is spot for a spot settled option, or the relevant forward price for a future settled option.
- Always non negative because of the max(., 0) floor.
- Premium = Intrinsic Value + [[Time Value]]. Rearranged: Time Value = Premium - Intrinsic Value.
- An option is [[ITM]] when intrinsic value > 0, [[ATM]] when S is approximately K, [[OTM]] when intrinsic value = 0 and the option is not at the money.

## Prerequisites
- [[Call Option]] and [[Put Option]] basics.
- [[Strike Price]] and the concept of [[Exercise]].
- [[Premium]] as the total price paid.
- Spot versus forward pricing of the underlying.

## Related concepts (learn next)
- [[Time Value]]: the rest of the premium beyond intrinsic value, which is what you learn to price next.
- [[Premium]]: the full option price that splits into intrinsic and time value.
- [[Moneyness]]: the formal way to classify how far S sits from K.
- [[ITM]]: the state where intrinsic value is positive and exercise pays.
- [[Strike Price]]: the fixed level K that anchors every intrinsic value calculation.
- [[Exercise]]: the act that converts intrinsic value into a realized position.

## Common misconceptions
- "Intrinsic value can be negative when the option is deep out of the money." Wrong. The max(., 0) floor exists precisely because you can walk away. An out of the money option has zero intrinsic value, never negative, since you are never forced to exercise at a loss.
- "Intrinsic value is the option's full worth." Wrong. Before [[Expiration]] the [[Premium]] almost always exceeds intrinsic value by the [[Time Value]] component. Only at expiry do they converge.
- "A high premium means high intrinsic value." Wrong. A long dated [[ATM]] option can carry a large premium that is entirely [[Time Value]] with zero intrinsic value.

## Sources
- Hull, Options, Futures, and Other Derivatives.
- CME Group education materials on options pricing.
