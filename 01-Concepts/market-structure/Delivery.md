---
aliases: [delivery, physical delivery, physical settlement]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Delivery

## Definition
Delivery is the physical settlement process where the holder of an expiring [[Futures Contract]] takes (if long) or makes (if short) physical delivery of the underlying commodity. The exchange specifies approved locations, quality grades, timing windows, and documentation. WTI crude delivers at Cushing, Oklahoma. CBOT [[Grains]] deliver at approved elevators along the Illinois River and in Chicago. LME metals deliver at approved warehouses globally via the warrant system. Over 95% of futures positions close before expiry, but the delivery mechanism is critically important because it anchors futures to physical reality. Without credible delivery, futures could disconnect from underlying value. Convergence of futures to spot at expiry, enforced by delivery, is what makes futures reliable benchmarks for the physical supply chain.

## Why it matters (commodities and FX)
The delivery mechanism forces futures to converge to spot via arbitrage. If futures trade above spot near expiry, arbitrageurs buy physical and deliver against the futures, driving prices together. If futures trade below spot, arbitrageurs buy futures and take delivery, again forcing convergence. This linkage makes futures prices reliable global benchmarks. Delivery risk, where a short cannot source or a long cannot accept, creates squeeze dynamics producing extreme price moves. The April 2020 WTI negative price event ($−37.63/bbl) occurred because longs could not take delivery at Cushing with storage full. Understanding delivery logistics, first notice dates, and position limits near expiry is essential for any commodity futures trader.

## Concrete example

**Concrete:** A physical oil firm sees WTI June trading at a $1.50/bbl premium to Cushing physical in the last week before expiry. They buy 50,000 barrels of physical at Cushing, sell 50 WTI June contracts, and deliver physical against the futures at expiry. The $1.50/bbl arbitrage minus $0.30/bbl storage and logistics nets $1.20/bbl × 50,000 = $60,000 risk free. Failure mirror: a retail trader using a commodity ETF holds 500 long WTI May 2020 contracts approaching expiry. Cushing storage is 95% full, no storage available. They cannot take delivery and are forced to sell into a collapsing market. WTI May settles at $−37.63/bbl. Catastrophic losses. Financial participants must respect delivery mechanics and roll well before expiry.

**Simplified:** Futures contracts ultimately settle in physical commodity unless cash settled. If you hold a contract past the deadline you must either deliver the commodity (if short) or take it (if long). Most traders close their positions before this happens because they have no use for actual barrels or tonnes. The threat of delivery is what forces the futures price to match physical reality at expiry; without it, futures could drift away from spot.

## Key mechanics and formulas
- **Delivery process (typical):**
  1. First notice day: shorts notify the exchange of intent to deliver
  2. Last trading day: final day to offset before delivery is mandatory
  3. Delivery period: physical transfer over exchange specified days
  4. Payment: long pays final settlement price × contract size to the clearinghouse
- **Convergence:** At expiry, Futures → Spot. Futures > Spot: buy spot, sell futures, deliver (drives futures down). Futures < Spot: buy futures, take delivery, sell spot (drives futures up).
- **Delivery costs:** Storage, insurance, transportation, inspection, financing.
- **Position limits:** Exchanges impose limits near expiry (last 3 to 5 trading days) to prevent squeezes.

## Prerequisites
- [[Futures Contract]]
- [[Margin]]

## Related concepts (learn next)
- [[Cash Settlement]] is the alternative; removes the physical anchoring mechanism.
- [[Contango Roll Cost]] arises partly because deferred contracts embed storage costs from holding physical through delivery.
- [[Backwardation Roll Gain]] reflects nearby delivery valued more than deferred due to scarcity.
- [[Basis Risk]] between delivery point and the trader's actual location is core for hedgers.
- [[Futures Contract]] specs define exact delivery terms.
- [[Spread Trade]] near delivery can be affected by squeeze dynamics and logistics.
- [[Margin]] often increases as delivery approaches to ensure only qualified participants remain.

## Common misconceptions

**"Nobody takes delivery."** Rare for financial participants but essential for market integrity. Physical commodity firms regularly take and make delivery. Volume rises when the basis is attractive for arbitrage.

**"Delivery is simple logistics."** Quality specs (API gravity for crude, protein for wheat), timing, insurance, and documentation create operational complexity. Failures carry severe financial and legal consequences.

**"Cash settled is always better."** [[Cash Settlement]] is operationally simpler but removes the anchoring mechanism. Cash settled can diverge from physical reality if the reference index is illiquid or manipulable.

## Sources
- CME Group, "Physical Delivery Procedures for Futures Contracts"
- LME, "Delivery and Settlement Rules"
- John Hull, "Options, Futures, and Other Derivatives"
- Commodity Trading Manual, Chicago Board of Trade
