---
aliases: [Being Assigned, Option Assignment]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-06-18"
---

# Assignment

## Definition
Assignment is the obligation side of [[Exercise]]. When an option buyer exercises, a [[Short]] option holder is assigned and must fulfill the contract. An assigned short [[Call Option]] must sell (deliver) at the [[Strike Price]], and an assigned short [[Put Option]] must buy at the [[Strike Price]]. The short does not choose to be assigned. The clearinghouse allocates assignments, typically at random or pro rata, among all accounts holding short positions in that series. In plain terms, if you sold an option and someone on the other side exercises, you can be picked to take the losing side of the trade whether you like it or not.

## Why it matters (commodities and FX)
Selling options collects [[Premium]] up front, but it sells away control. Assignment is the moment that obligation becomes a real position with real [[Margin]] calls. In commodities, being assigned on a futures option lands you in a live [[Futures Contract]] that can lead to physical [[Delivery]], so an oil short who ignores expiry can wake up obligated to deliver barrels. Two specific risks dominate near [[Expiration]]. Assignment risk is the chance you get assigned at all. Pin risk is the nastier one: when the underlying settles right at the strike, you cannot tell whether you will be assigned, so you do not know if you are flat or holding a position when the market reopens.

## Concrete example
**Concrete:** You are [[Short]] 1 [[WTI Crude Oil]] 80 call (you sold it), collecting a [[Premium]] of 1.50 per barrel (1,500 on a 1,000 barrel contract).

Fail case (surprise overnight assignment): Crude settles at 85 on expiry. The long exercises. You are assigned a [[Short]] futures position at 80 while the market is 85, an immediate mark of minus 5 per barrel (minus 5,000). Net of the 1.50 premium you kept, you are down 3.50 per barrel (minus 3,500). You discover the short futures the next morning, now exposed to overnight moves and a [[Margin]] call you did not plan for. If crude gapped higher overnight, the loss grows before you can react.

Win case (clean OTM expiry): Same short 80 call, but crude settles at 78. The call is [[OTM]], so no rational long exercises. The option expires worthless, you are not assigned, you keep the full 1.50 per barrel (1,500) premium, and you hold no position.

Pin risk variant: Crude settles at exactly 80.00. The call is right at the money. Some longs exercise, some do not, and the clearinghouse assigns pro rata. You might be assigned a short futures, or you might be flat, and you only find out after the close. You may hedge defensively into the close to manage the uncertainty.

**Simplified:** When you sell an option, you can be forced to honor it if the buyer exercises. If the buyer wins, you take the matching loss, often discovered the next morning as a new futures position. If the option expires worthless, you keep the premium and walk away clean.

## Key mechanics and formulas
- Assigned short call result = you are short the underlying (or futures) at the [[Strike Price]]; mark to market = Strike minus Underlying per unit.
- Assigned short put result = you are long the underlying at the [[Strike Price]]; mark to market = Underlying minus Strike per unit.
- Allocation: the clearinghouse assigns to shorts at random or pro rata; you cannot opt out.
- Assignment risk rises as the option moves [[ITM]] approaching [[Expiration]].
- Pin risk: underlying settles at or near the strike, so assignment is uncertain and you do not know your post expiry position.
- Assigned commodity futures options create a live [[Futures Contract]] with [[Margin]] obligations and potential physical [[Delivery]].

## Prerequisites
- [[Exercise]]: assignment exists only because someone on the long side exercises.
- [[Short]]: only short option positions get assigned.
- [[Call Option]] and [[Put Option]]: define what the assigned obligation is.
- [[Strike Price]]: the price at which the assigned position is created.
- [[Premium]]: what the short collected and the cushion against assignment loss.

## Related concepts (learn next)
- [[Exercise]]: the action that triggers assignment, so master the buyer's side too.
- [[Margin]]: an assigned futures position immediately consumes margin, so understand the funding hit.
- [[Delivery]]: assignment on physically settled commodity options can end in delivery obligations.
- [[Expiration]]: assignment and pin risk concentrate at expiry, so study expiry mechanics closely.
- [[Open Interest]]: high open interest near a strike signals where pin risk and assignment cluster.
- [[ITM]]: in the money shorts are the ones most likely to be assigned, so this gauges your exposure.
- [[Short]]: deepen your understanding of selling options as a strategy and its full risk profile.
- [[Cash Settlement]]: shows how assignment resolves without delivery for cash settled contracts.

## Common misconceptions
- "I can decide whether to accept assignment." Wrong. The short has no choice. Once a long exercises and the clearinghouse allocates to your account, you are obligated.
- "Only deep [[ITM]] options get assigned." Wrong. Any option that finishes in the money can be assigned, and pin risk means even an at the money option at [[Expiration]] may or may not be assigned unpredictably.
- "If I am assigned, I have lost the premium too." Wrong. You keep the [[Premium]] you collected. It offsets the assigned position's loss, so your breakeven sits at strike plus premium (for a short call), not at the strike itself.
- "An expired worthless option still risks assignment." Wrong. An [[OTM]] option that expires has no value to exercise, so no rational long exercises it and no assignment occurs. You simply keep the premium.

## Sources
- OCC, assignment allocation methodology (random and pro rata).
- CME Group, Options on Futures exercise and assignment procedures.
- Natenberg, Option Volatility and Pricing, pin risk and expiration risk.
