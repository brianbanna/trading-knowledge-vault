---
aliases: [delivery, physical delivery, physical settlement]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Delivery

## Definition
Delivery is the physical settlement process through which the holder of an expiring [[Futures Contract]] takes (if long) or makes (if short) delivery of the actual underlying commodity. The exchange specifies approved delivery locations, acceptable quality grades, timing windows, and documentation requirements. For WTI crude oil, delivery occurs at the Cushing, Oklahoma storage hub. For CBOT [[Grains]], delivery occurs at approved elevators along the Illinois River and in Chicago. For LME metals, delivery occurs at approved warehouses globally via the warrant system. In practice, over 95% of futures contracts are closed (offset) before expiry, but the delivery mechanism is critically important because it anchors futures prices to physical market reality. Without the credible possibility of delivery, futures prices could disconnect from the underlying commodity's actual value. The convergence of futures to spot at expiry, enforced by delivery, is what makes futures reliable reference prices for the entire physical supply chain.

## Why it matters (commodities and FX)
The delivery mechanism ensures that futures prices converge to spot prices at expiry through arbitrage. If futures trade above spot near expiry, arbitrageurs buy physical commodity and deliver against the futures, driving prices together. If futures trade below spot, arbitrageurs buy futures and take delivery, again forcing convergence. This arbitrage linkage makes futures prices reliable benchmarks for physical trade globally. Delivery risk, where a short cannot source the physical commodity or a long cannot accept it, creates squeeze dynamics that can produce extreme price moves. The April 2020 WTI negative price event ($-37.63/bbl) occurred because traders holding long positions could not take delivery at Cushing due to full storage capacity. Understanding delivery logistics, first notice dates, and position limits near expiry is essential for any trader holding commodity futures.

## Concrete example
**Success case:** A physical oil trading firm notices that WTI June futures are trading at a $1.50/bbl premium to Cushing physical crude in the last week before expiry. They buy 50,000 barrels of physical crude at Cushing, simultaneously sell 50 WTI June futures, and deliver the physical against the futures at expiry. The $1.50/bbl arbitrage profit (minus storage and logistics costs of ~$0.30/bbl) nets $1.20/bbl x 50,000 = $60,000 risk free.

**Failure case:** A retail trader using a commodity ETF holds 500 long WTI May 2020 contracts approaching expiry. Cushing storage is 95% full, and no storage is available. The trader cannot take physical delivery and is forced to sell into a collapsing market. WTI May goes negative for the first time in history, settling at negative $37.63/bbl. The trader's losses are catastrophic: instead of rolling before first notice day, they were caught holding an undeliverable position. The lesson: financial participants must respect delivery mechanics and close or roll positions well before expiry.

## Key mechanics and formulas
- **Delivery process (typical):**
  1. First notice day: short position holders notify the exchange of intent to deliver
  2. Last trading day: final day to offset a position before delivery becomes mandatory
  3. Delivery period: physical transfer occurs over exchange specified days
  4. Payment: long pays the final settlement price x contract size to the clearinghouse
- **Convergence:** At expiry, Futures price approaches Spot price. If Futures > Spot: buy spot, sell futures, deliver = arbitrage profit (drives futures down). If Futures < Spot: buy futures, take delivery, sell spot = arbitrage profit (drives futures up).
- **Delivery costs:** Storage, insurance, transportation, inspection, and financing costs affect the economics of taking or making delivery
- **Position limits:** Exchanges impose position limits near expiry (typically the last 3 to 5 trading days) to prevent squeezes and ensure orderly delivery

## Prerequisites
- [[Futures Contract]]
- [[Margin]]

## Related concepts (learn next)
- [[Cash Settlement]] is the alternative to physical delivery, eliminating logistics but removing the physical anchoring mechanism.
- [[Contango Roll Cost]] arises partly because deferred contracts embed storage costs that would be incurred if holding the physical commodity through delivery.
- [[Backwardation Roll Gain]] reflects situations where nearby delivery is valued more highly than deferred delivery due to scarcity.
- [[Basis Risk]] between the delivery point price and the trader's actual physical location is a core consideration for hedgers.
- [[Futures Contract]] specifications define the exact terms under which delivery occurs.
- [[Spread Trade]] near delivery dates can be affected by squeeze dynamics and delivery logistics.
- [[Margin]] requirements often increase as contracts approach delivery, reflecting the exchange's desire to ensure only qualified participants remain.

## Common misconceptions
- **"Nobody actually takes delivery."** While rare for financial participants, delivery is essential for market integrity. Physical commodity firms regularly take and make delivery. Delivery volume often increases when the basis (futures minus spot) is attractive for arbitrage.
- **"Delivery is simple logistics."** Quality specifications (API gravity for crude, protein content for wheat), timing windows, insurance, and documentation create significant operational complexity. Delivery failures can have severe financial and legal consequences.
- **"Cash settled contracts are always preferable."** [[Cash Settlement]] is operationally simpler but removes the physical anchoring mechanism. Cash settled contracts can diverge from physical market reality if the reference index is illiquid or subject to manipulation.

## Sources
- CME Group, "Physical Delivery Procedures for Futures Contracts"
- LME, "Delivery and Settlement Rules"
- John Hull, "Options, Futures, and Other Derivatives"
- Commodity Trading Manual, Chicago Board of Trade
