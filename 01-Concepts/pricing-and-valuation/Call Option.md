---
aliases: [Call, Calls, Long Call, Short Call]
tags:
  - "#quant"
date-added: "2026-06-18"
---

# Call Option

## Definition
A call option is the right, not the obligation, to BUY the underlying at a fixed [[Strike Price]] before or at [[Expiration]]. The buyer pays a [[Premium]] up front for that right. If the market rises above the strike, the call gains value because you can buy cheap and sell at the higher market price. If the market stays flat or falls, the buyer simply lets the option lapse and loses only the premium paid. Technically the call is a convex claim on the underlying whose value splits into [[Intrinsic Value]] (how far in the money it is) and [[Time Value]] (the chance it moves further in your favor before expiry).

## Why it matters (commodities and FX)
Calls let you express an upside view with defined risk and embedded leverage. A producer or refiner buying a crude call caps the price it will pay for future barrels while keeping the benefit if prices fall. A [[Speculator]] uses calls to bet on a rally in [[Gold Futures]] or [[Brent Crude]] for a fraction of the capital a futures position needs. Selling calls is how desks harvest premium when they think a market will not break higher, but the short side carries open ended risk if the underlying gaps up.

## Concrete example
**Concrete:** Spot gold trades at 3400 per ounce. You buy 1 gold call, [[Strike Price]] 3500, paying a [[Premium]] of 50 (per ounce). Your cost and maximum loss as the [[Long]] holder is 50.

Win case: at [[Expiration]] gold has risen to 3700. The call is in the money. [[Intrinsic Value]] is 3700 minus 3500 equals 200. Net profit is 200 minus the 50 premium equals 150 per ounce. You turned a 50 premium into 150, a 3x return on a 9 percent move in the underlying. That amplification is the leverage of the option.

Fail case: gold falls to 3300. The strike 3500 is now well above market, so the call expires worthless. You lose the entire 50 premium and nothing more. The producer who instead just held physical gold would have lost 100 of mark to market; your loss was capped at the premium.

Short call blow up: now flip sides. You SELL (write) the same 3500 call and collect the 50 premium, expecting gold to stagnate. Gold instead surges to 4200. The buyer exercises. You must deliver at 3500 something now worth 4200, a loss of 700 in [[Intrinsic Value]]. Net loss is 700 minus the 50 you collected equals 650 per ounce. Because there is no ceiling on price, your loss as a [[Short]] call writer is theoretically unlimited. See [[Assignment]] for how the obligation lands on you.

**Simplified:** Buying a call is a small, fixed bet that the price goes up; the worst case is losing the ticket price. Selling a naked call collects a small sure premium but exposes you to large, uncapped losses if the market rallies hard.

## Key mechanics and formulas
- Payoff at expiry to the [[Long]] call: max(S minus K, 0) where S is the underlying price and K is the [[Strike Price]].
- Profit to the long: max(S minus K, 0) minus [[Premium]].
- Payoff to the [[Short]] call: minus max(S minus K, 0); profit is premium minus that payoff.
- Breakeven for the long: K plus premium. In the gold example, 3500 plus 50 equals 3550.
- [[Delta]] of a call runs from 0 (deep [[OTM]]) to plus 1 (deep [[ITM]]); it measures how much the call moves per 1 unit move in the underlying.
- Maximum loss long: the premium. Maximum loss short: unbounded (price has no upper limit).
- Plot the kinked profit line on a [[Payoff Diagram]] to see the capped downside and open upside.

## Prerequisites
- [[Strike Price]]
- [[Premium]]
- [[Intrinsic Value]]
- [[Moneyness]]
- [[Long]] and [[Short]]
- [[Expiration]]

## Related concepts (learn next)
- [[Put Option]] the mirror instrument giving the right to sell, needed to build any spread or collar.
- [[Strike Price]] the level that determines whether your call ever has [[Intrinsic Value]].
- [[Premium]] the price you pay or collect, and the only thing a long call can lose.
- [[Intrinsic Value]] the part of premium backed by real in the money distance.
- [[Moneyness]] tells you at a glance whether a call is [[ITM]], [[ATM]], or [[OTM]].
- [[Delta]] quantifies your directional exposure and how it shifts as the underlying moves.
- [[Payoff Diagram]] visualizes the hockey stick shape that defines call risk and reward.
- [[Assignment]] explains what happens to a short call when the buyer exercises.

## Common misconceptions
- "A call can lose more than the premium for the buyer." Wrong. The long holder's risk is strictly the [[Premium]] paid; the worst outcome is the option expiring worthless. Unlimited loss belongs only to the [[Short]] writer.
- "If gold finishes above my strike I always make money." Wrong. You only profit above breakeven, which is strike plus premium. Finishing between 3500 and 3550 still leaves you with a net loss because the [[Intrinsic Value]] does not yet cover the [[Premium]].
- "Out of the money calls are worthless before expiry." Wrong. An [[OTM]] call still carries [[Time Value]] because there is a chance it moves into the money; that is why [[Vega]] and [[Theta]] affect its price daily.
- "Selling calls is safe income because most expire worthless." Wrong. The payoff is asymmetric: many small premiums collected can be erased by one upside gap, since the short call loss is unbounded as shown in the gold to 4200 case.

## Sources
- Hull, Options, Futures and Other Derivatives, chapters on option mechanics and payoffs.
- CME Group educational material on options on [[Gold Futures]] and energy contracts.
