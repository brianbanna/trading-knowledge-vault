---
aliases: [front month, prompt month, nearby, nearby contract, M1, deferred contracts, back months]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-03-20"
---

# Front Month

## Definition

The front month (also called prompt month, nearby, or M1) is the futures contract with the nearest expiration date that is still actively trading. Deferred contracts (M2, M3, etc., also called "back months") are those expiring further in the future. The distinction matters because front month contracts have the highest [[Liquidity]], the tightest [[Bid-Ask Spread]], and the strongest connection to physical market conditions. They are where supply/demand tightness shows up first and most aggressively. The relationship between front month and deferred prices defines the [[Forward Curve]] shape.

## Why it matters (commodities and FX)

When traders say "crude oil is at $75," they almost always mean the front month contract. It is the reference price for physical transactions, margin calculations, and most news headlines. But the front month is also where expiry risk lives: as the contract approaches last trading day, holders must either take/make physical delivery (for physically settled contracts) or close/roll the position. This creates predictable patterns in volume, open interest, and price behavior around expiry.

The spread between M1 and M2 (the "prompt spread") is the most liquid [[Calendar Spread]] in most commodity markets and the most direct expression of near term supply/demand tightness. A wide M1 premium (steep [[Backwardation]]) signals acute prompt demand. A wide M1 discount (steep [[Contango]]) signals near term oversupply.

## Concrete example

[[WTI Crude Oil]] CL: In a typical month, the front month (e.g., CLM6, June 2026) has open interest of 300,000+ contracts and daily volume of 500,000+. The second month (CLN6, July 2026) has ~200,000 open interest. The 12th month (CLM7, June 2027) might have only 30,000 open interest and much wider bid-ask spreads.

During the April 2020 WTI event, the front month (May 2020) went to negative $37.63 while the second month (June) was still at +$20. The spread between M1 and M2 reached negative $58, an extreme that only makes sense through the lens of front month delivery mechanics: holders of the expiring contract faced physical delivery at Cushing with no storage available.

## Key mechanics and formulas

**Standard month notation:**
- M1 = front month (nearest active contract)
- M2 = second month
- M6 = 6th month (common benchmark for "deferred")
- Red months = 12+ months out (named for the color coding on some trading screens)

**Prompt spread:** `Prompt Spread = M1 - M2`
Positive = backwardation. Negative = contango.

**Roll schedule:** Most institutional traders roll 5 to 10 business days before expiry to avoid thin liquidity and delivery mechanics. The Goldman Roll (GSCI rebalancing) occurs on the 5th to 9th business day of the month, creating predictable flow.

**Volume/open interest migration:** As expiry approaches, volume migrates from M1 to M2. When M2 volume exceeds M1 volume, the "active month" has effectively shifted. Some quote vendors switch their continuous contract to M2 at this point.

## Prerequisites
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)
- [[Roll Yield]] - the P&L of moving from the front month to the next contract. Front month behavior directly determines roll yield.
- [[Calendar Spread]] - the M1/M2 spread is the most basic calendar spread and the most liquid.
- [[Convenience Yield]] - front month premiums in backwardated markets reflect convenience yield.
- [[Liquidity]] - front months are the most liquid. Deferred months can have meaningful [[Slippage]] and wider [[Bid-Ask Spread|bid-ask spreads]].
- [[Storage Economics]] - front month behavior is driven by near term storage dynamics. Full storage crushes the front month. Tight storage lifts it.
- [[Cost of Carry]] - the theoretical relationship between M1 and deferred months.

## Common misconceptions

**"The front month is always the best contract to trade."** For directional views with multi week horizons, the second or third month often offers better risk/reward: similar directional exposure with less expiry risk and more time for the thesis to play out.

**"Front month price = spot price."** Close but not identical. The front month converges to spot as expiry approaches, but until then, it incorporates a small carry component. True spot prices are quoted in the physical OTC market, not on the exchange.

**"Deferred contracts are illiquid."** For major benchmarks (WTI, Brent, gold), contracts out to 12 months are highly liquid. Beyond 24 months, liquidity thins meaningfully. For smaller markets (platinum, coffee), even M3 can be thin.

## Sources

- CME Group: Understanding Futures Contract Expiry
- ICE Futures: Contract Specifications and Expiry Calendar
- Hull, Options, Futures, and Other Derivatives, Chapter 2
