---
aliases: [Put, Puts, Long Put, Short Put, Protective Put]
tags:
  - "#quant"
date-added: "2026-06-18"
---

# Put Option

## Definition
A put option is the right, not the obligation, to SELL the underlying at a fixed [[Strike Price]] before or at [[Expiration]]. The buyer pays a [[Premium]] up front for that right. If the market falls below the strike, the put gains value because you can sell high at the strike while the market trades low. If the market stays flat or rises, the buyer lets the put lapse and loses only the premium. Technically the put is a convex claim that rises in value as the underlying falls, splitting into [[Intrinsic Value]] and [[Time Value]], which makes it the standard tool for downside [[Hedging]].

## Why it matters (commodities and FX)
Puts are the cleanest way to insure against a price collapse with a known, capped cost. A gold miner buying puts locks in a floor selling price for future production while keeping the upside if metal rallies. An airline or a commodity producer uses puts on [[WTI Crude Oil]] to protect revenue against a crash without giving up gains. Selling puts collects [[Premium]] when you are willing to buy the underlying lower, but a market that collapses turns that small income into a large loss.

## Concrete example
**Concrete:** Crude oil trades at 70 per barrel. You buy 1 put, [[Strike Price]] 68, paying a [[Premium]] of 2 (per barrel). Your cost and maximum loss as the [[Long]] holder is 2.

Win case: at [[Expiration]] oil has crashed to 60. The put is in the money. [[Intrinsic Value]] is 68 minus 60 equals 8. Net profit is 8 minus the 2 premium equals 6 per barrel. A 14 percent fall in oil turned a 2 premium into a 6 gain, a 3x return, the leverage of the option.

Fail case: oil rises to 80. The strike 68 sits well below market, so the put expires worthless. You lose the entire 2 premium and nothing more.

Gold miner hedge: a producer expects to sell 10,000 ounces of gold next quarter with spot at 3400. It buys 3300 strike puts at a [[Premium]] of 40 per ounce. If gold collapses to 3000, each put pays [[Intrinsic Value]] 300 (3300 minus 3000); net 260 after premium offsets the lower physical sale price, putting an effective floor near 3260 on revenue. If gold instead rallies to 3700, the puts expire worthless, the miner loses only the 40 premium per ounce, and it still sells physical metal at the higher price. This is downside [[Hedging]]: a known cost buys protection while keeping upside.

Short put loss: now SELL the 68 oil put and collect 2, expecting oil to hold above 68. Oil instead crashes to 50. The buyer exercises and you must buy at 68 something worth 50, a loss of 18 in [[Intrinsic Value]]. Net loss is 18 minus the 2 collected equals 16 per barrel. The short put loss is large but bounded, because the underlying cannot fall below 0; maximum loss is strike minus premium. See [[Assignment]] for how the obligation lands on the writer.

**Simplified:** Buying a put is downside insurance; the worst case is losing the premium, like an insurance policy that expires unused. Selling a put earns a small premium but obligates you to buy at the strike, so a collapsing market hands you a large loss.

## Key mechanics and formulas
- Payoff at expiry to the [[Long]] put: max(K minus S, 0) where S is the underlying price and K is the [[Strike Price]].
- Profit to the long: max(K minus S, 0) minus [[Premium]].
- Payoff to the [[Short]] put: minus max(K minus S, 0); profit is premium minus that payoff.
- Breakeven for the long: K minus premium. In the oil example, 68 minus 2 equals 66.
- Maximum loss long: the premium. Maximum loss short: strike minus premium (capped because price floors at 0).
- A protective put combines a [[Long]] position in the underlying with a long put to set a floor, the core [[Hedging]] structure.
- Plot the kinked profit line on a [[Payoff Diagram]] to see the capped cost and the gain that grows as price falls.

## Prerequisites
- [[Strike Price]]
- [[Premium]]
- [[Intrinsic Value]]
- [[Moneyness]]
- [[Long]] and [[Short]]
- [[Expiration]]

## Related concepts (learn next)
- [[Call Option]] the mirror instrument giving the right to buy, paired with puts to build collars and spreads.
- [[Strike Price]] the level that sets where your put protection or obligation begins.
- [[Premium]] the cost of the insurance and the only thing a long put can lose.
- [[Intrinsic Value]] the part of put premium backed by real in the money distance below the strike.
- [[Moneyness]] tells you whether a put is [[ITM]], [[ATM]], or [[OTM]].
- [[Hedging]] the primary use of long puts to floor revenue for producers and portfolios.
- [[Payoff Diagram]] visualizes the put profit shape and where breakeven sits.
- [[Assignment]] explains what happens to a short put writer when the buyer exercises.

## Common misconceptions
- "A long put can lose more than the premium." Wrong. The buyer's risk is strictly the [[Premium]] paid; if the market never falls below the strike, the put simply expires and you lose the premium only.
- "If oil finishes below my strike I always profit." Wrong. You only profit below breakeven, which is strike minus premium. Oil finishing between 66 and 68 still leaves a net loss because the [[Intrinsic Value]] does not yet cover the [[Premium]].
- "Selling puts is free money since markets usually drift up." Wrong. The payoff is asymmetric: a single crash, like oil to 50, wipes out many collected premiums because the [[Short]] put loss runs to strike minus premium.
- "A hedge with puts should make money." Wrong. The miner's puts expiring worthless in the rally case is a successful hedge, not a failure; the 40 premium is the cost of insurance you were glad not to need.

## Sources
- Hull, Options, Futures and Other Derivatives, chapters on option mechanics, protective puts, and hedging.
- CME Group educational material on options on [[WTI Crude Oil]] and [[Gold Futures]].
