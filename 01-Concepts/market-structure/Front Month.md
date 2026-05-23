---
aliases: [front month, prompt month, nearby, nearby contract, M1, deferred contracts, back months]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-03-20"
---

# Front Month

## Definition

The front month (or prompt month, nearby, M1) is the futures contract with the nearest expiration date still actively trading. Deferred contracts (M2, M3, "back months") expire further out. Front month contracts have the highest [[Liquidity]], the tightest [[Bid-Ask Spread]], and the strongest connection to physical conditions. They are where supply/demand tightness shows up first and hardest. The relationship between front month and deferred prices defines the [[Forward Curve]] shape.

## Why it matters (commodities and FX)

"Crude oil is at $75" almost always means the front month contract. It is the reference for physical transactions, margin calculations, and most news. The front month also carries expiry risk: as it approaches last trading day, holders must take/make physical delivery (physical contracts) or close/roll. This creates predictable volume, open interest, and price patterns around expiry.

The M1/M2 spread (prompt spread) is the most liquid [[Calendar Spread]] in most commodities and the most direct expression of near term tightness. A wide M1 premium (steep [[Backwardation]]) signals acute prompt demand. A wide M1 discount (steep [[Contango]]) signals near term oversupply.

## Concrete example

**Concrete:** [[WTI Crude Oil]] CL: in a typical month, the front month (CLM6, June 2026) has open interest 300,000+ and daily volume 500,000+. The second month (CLN6, July 2026) has ~200,000 OI. The 12th month (CLM7, June 2027) might have only 30,000 OI and much wider spreads. During the April 2020 WTI event, the front month (May 2020) went to $−37.63 while the second month (June) was at $+20. M1/M2 spread reached $−58, an extreme only explainable through front month delivery mechanics: holders faced physical delivery at Cushing with no storage available.

**Simplified:** The front month is the next futures contract to expire and the most actively traded. When the press quotes "the oil price," they mean the front month. It is the reference for physical trades and the most direct read on near term supply and demand. As expiry approaches, traders close or roll positions to the next month to avoid delivery; this rolling creates patterns that are themselves tradeable.

## Key mechanics and formulas

**Standard month notation:**
- M1 = front month (nearest active)
- M2 = second month
- M6 = 6th month (common "deferred" benchmark)
- Red months = 12+ months out (color coded on some trading screens)

**Prompt spread:** `Prompt Spread = M1 − M2`
Positive = backwardation. Negative = contango.

**Roll schedule:** Most institutional traders roll 5 to 10 business days before expiry to avoid thin liquidity and delivery mechanics. The Goldman Roll (GSCI rebalancing) occurs on the 5th to 9th business day, creating predictable flow.

**Volume/OI migration:** As expiry approaches, volume migrates from M1 to M2. When M2 volume exceeds M1, the "active month" effectively shifts. Some quote vendors switch their continuous contract to M2 at this point.

## Prerequisites
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)
- [[Roll Yield]] - PnL of moving from front month to next contract.
- [[Calendar Spread]] - M1/M2 spread is the most basic and most liquid.
- [[Convenience Yield]] - front month premiums in backwardated markets reflect convenience yield.
- [[Liquidity]] - front months are most liquid; deferred can have meaningful slippage.
- [[Storage Economics]] - front month behavior is driven by near term storage. Full storage crushes the front; tight storage lifts it.
- [[Cost of Carry]] - theoretical relationship between M1 and deferred.

## Common misconceptions

**"The front month is always the best contract to trade."** For directional views with multi week horizons, the second or third month often offers better risk/reward: similar exposure with less expiry risk.

**"Front month price = spot price."** Close, not identical. Front month converges to spot as expiry nears, but until then incorporates a small carry component. True spot is quoted in physical OTC, not the exchange.

**"Deferred contracts are illiquid."** For major benchmarks (WTI, Brent, gold), contracts out to 12 months are highly liquid. Beyond 24 months, liquidity thins. For smaller markets (platinum, coffee), even M3 can be thin.

## Sources

- CME Group: Understanding Futures Contract Expiry
- ICE Futures: Contract Specifications and Expiry Calendar
- Hull, Options, Futures, and Other Derivatives, Chapter 2
