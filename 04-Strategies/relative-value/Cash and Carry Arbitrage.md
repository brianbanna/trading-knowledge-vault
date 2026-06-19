---
aliases: [cash and carry, cash and carry trade, cash-and-carry, cash and carry arb, reverse cash and carry]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-06-19"
---

# Cash and Carry Arbitrage

## Definition

Buy the physical asset now, store it, and at the same instant sell a futures contract against it. You hold the asset until the future expires, then deliver it to close the future. Because you locked the sale price (the futures price) on day 1 and you know your carrying costs, the profit is fixed regardless of where the price goes. The trade exists to capture a future that is priced too high relative to spot plus the [[Cost of Carry]]. It is the no-arbitrage force that pins the [[Forward Curve]] to spot plus carry, and it sets the upper bound on how steep [[Contango]] can get.

The mirror trade, **reverse cash and carry** (sell the physical short, buy the future), would cap [[Backwardation]], but it rarely works in commodities because you usually cannot borrow and short a physical barrel or tonne. That asymmetry is central.

## Why it matters (commodities and FX)

Cash and carry is the mechanism, not just a trade. It is *why* the forward curve cannot drift arbitrarily far from spot:

- In commodities, whenever [[Contango]] exceeds all-in carrying cost (financing plus storage plus insurance), the arb opens, traders pile in, they buy spot and sell futures, and the buying of spot plus selling of forward flattens the curve back toward full carry. This is the textbook explanation of the [[Cost of Carry]] upper bound and the engine behind every [[Calendar Spread]] in a carry market.
- The binding constraint is almost always **storage**. In the 2020 oil collapse and the 2008 to 2009 contango, the trade printed money on paper but only desks with secured tank or VLCC storage could actually put it on. When storage fills, the arb cannot enforce the bound and you get super contango.
- In FX the identical structure is **covered interest parity**: borrow one currency, convert spot, deposit the other, and sell the forward. The forward points are pinned to the rate differential by exactly this arbitrage. A persistent deviation is the FX market's version of super contango.

## Concrete example

### Crude oil super contango

WTI spot = 60.00 USD per barrel. The 12 month future trades at 70.00. Your all-in carry for one year:

- Storage (tank lease): 0.40 per bbl per month × 12 = 4.80
- Financing on the 60.00 spot outlay at 5 percent = 3.00
- Insurance and handling ≈ 0.20
- **Total carry ≈ 8.00 per bbl**, so full-carry fair value of the future is 60.00 + 8.00 = 68.00.

The future at 70.00 sits 2.00 above full carry. The trade, per 1,000 bbl lot:

1. Buy 1,000 bbl spot at 60.00, funded.
2. Lease storage, sell 1 oil future (1,000 bbl) at 70.00.
3. Hold 12 months, then deliver the stored oil into the expiring future at 70.00.

Locked profit = 70.00 − (60.00 + 8.00) = **2.00 per bbl = 2,000 USD**, independent of where oil trades.

- **Win case:** the future converges to spot at [[Expiration]], you deliver, and the 2.00 edge is realised. If anything, a deeper contango next year lets you roll the storage play again.
- **Fail case:** storage suddenly reprices. Tank lease jumps from 0.40 to 0.70 per month, lifting carry to 60.00 financing-and-insurance plus 8.40 storage ≈ 11.60, so the locked result flips to 70.00 − 71.60 = **−1.60 per bbl**. Or financing floats higher mid-trade. Or, the 2020 problem, you simply cannot secure storage at any price and the trade is uninvestable. Or a delivery squeeze or grade and location basis mismatch breaks convergence near expiry, leaving the legs unhedged.

### Gold (the clean textbook case)

Worked in [[Arbitrageur]]: spot gold 3,380, carry 30, [[Gold Futures]] at 3,440 versus 3,410 fair value, sell the future and buy and store 100 oz to lock 30 USD per oz. Metals are the cleanest version because storage is cheap, dense, and non-perishable, so [[Convenience Yield]] is low and fair value is almost pure carry.

## Key mechanics and formulas

Let `S` = spot price, `r` = financing rate, `u` = storage plus insurance cost rate, `y` = [[Convenience Yield]], `T − t` = time to delivery.

- **Fair futures price (full carry):** continuous form `F* = S · e^{(r + u − y)(T − t)}`; additive shorthand `F* ≈ S + financing + storage − convenience yield`.
- **Cash and carry profit per unit:** `π = F_market − (S + C)`, where `C` is all-in carry. The trade is live only while `F_market > S + C`, i.e. above full carry (super contango).
- **Reverse cash and carry profit per unit:** `π = (S − C_avoided) − F_market`, live only while `F_market < S − convenience benefit`, and only executable if you can borrow and short the physical.

Plain English: you are short the basis. You win the gap between the rich future and the true cost of carrying the physical to meet it. Every input in `C` that is left floating is a risk, not a cost.

## Prerequisites

- [[Cost of Carry]]
- [[Forward Curve]]
- [[Contango]]
- [[Storage Economics]]
- [[Futures Contract Mechanics]]

## Related concepts (learn next)

- [[Convenience Yield]] — the value of holding physical; it is exactly what blocks the reverse trade and lets [[Backwardation]] persist while contango stays capped.
- [[Covered Interest Parity]] — the FX twin of cash and carry; same arbitrage, rates instead of storage.
- [[Calendar Spread]] — the tradeable expression of curve shape that the arb enforces.
- [[Storage Economics]] — storage availability and cost is the binding constraint that decides whether the arb can actually be put on.
- [[Roll Yield]] — the return a contango or backwardation curve hands a passive holder, the flip side of the carry the arb harvests.
- [[Arbitrageur]] — the actor and the gold worked example.
- [[Backwardation]] — the regime where the reverse trade would apply but usually cannot.

## Common misconceptions

1. **"Cash and carry is risk-free."** Only if storage, financing, and the delivery mechanism are all locked at inception. Floating financing, storage repricing or unavailability, quality and location basis, and delivery squeezes are real and have blown up real trades.
2. **"It works symmetrically in backwardation."** No. The reverse trade needs you to short the physical, which for commodities means borrowing inventory you typically cannot get. That is why contango is capped at full carry but backwardation is not, and why [[Convenience Yield]] is the asymmetry's name.
3. **"Any contango is free money."** No. Only super contango, where the contango exceeds all-in carry, opens an edge. Normal contango below full carry is just the market pricing storage correctly.
4. **"Storage is a footnote."** It is usually the entire trade. When tanks or warehouses fill, the arb cannot enforce the upper bound, and that is precisely when contango blows out to extremes.

## Sources

- CME Group and ICE delivery and storage rules; LME warehousing.
- Hull, Options, Futures, and Other Derivatives, on cost of carry and covered interest parity.
- Geman, Commodities and Commodity Derivatives.
- Pirrong, on the economics of commodity storage and arbitrage.

---
*Status: #stub | Last reviewed: 2026-06-19*
