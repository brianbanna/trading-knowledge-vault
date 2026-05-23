---
aliases: [LME warrant, warehouse warrant, warrant system]
tags:
  - "#metals/base"
date-added: "2026-03-20"
---

# Warrant

## Definition

An LME warrant is a document of title representing a specific lot of metal stored in an [[LME]] approved warehouse. Each warrant corresponds to a standard lot (25 tonnes for copper, aluminum, zinc, lead; 6 tonnes for nickel; 5 tonnes for tin) of approved brand metal meeting LME quality specs. Metal "on warrant" is available for delivery against LME futures. A holder wanting to withdraw metal (use it, sell physically, move it) cancels the warrant, signaling intent to take delivery. The warrant system is the mechanism anchoring LME futures prices to the physical market.

## Why it matters (commodities and FX)

The warrant system is how the LME connects financial contracts to physical reality. Rising cancelled warrants ([[Cancelled Warrants]]) signal physical buyers actively pulling metal, indicating real demand. Total stock on warrant determines how much metal is immediately deliverable, affecting delivery risk for shorts. When on warrant stocks fall to low levels, shorts face [[Backwardation Squeeze]] risk because they cannot source metal for delivery. Understanding warrants is essential for anyone trading LME or assessing physical conditions.

## Concrete example

**Concrete:** A producer delivers 1,000 tonnes of copper cathode (40 warrants × 25 tonnes) into an LME warehouse in Rotterdam, receiving warrants that trade on the exchange. A Chinese trader buys these warrants through the LME and cancels them, intending to ship the metal to Shanghai. The cancellations show up in the daily [[LME Warehouse Stocks]] report, signaling physical demand. If many traders cancel simultaneously, on warrant stocks drop rapidly and the [[Cash to 3 Month Spread]] moves into backwardation as remaining deliverable supply tightens. Watching cancellations weekly is a leading indicator of squeeze conditions.

**Simplified:** A piece of paper that says "you own 25 tonnes of copper sitting in this specific warehouse." You can trade the paper on the LME like any other asset. When you want the actual metal out, you "cancel" the paper, queue for withdrawal, and eventually take physical delivery. The whole LME pricing system rests on this paper to metal bridge.

## Key mechanics and formulas

**Warrant lifecycle:**
1. Metal delivered to LME approved warehouse
2. Warehouse issues warrant (document of title)
3. Warrant is live (on warrant), available for LME delivery
4. Holder cancels warrant (intent to withdraw)
5. Metal queued for withdrawal
6. Metal physically removed

**Cancellation to withdrawal lag:** depending on warehouse queue, 1 day to several months (historically, queues at some warehouses exceeded 2 years).

## Prerequisites

- [[LME]]
- [[LME Warehouse Stocks]]
- [[Delivery]]

## Related concepts (learn next)

- [[Cancelled Warrants]]: cancellation is the key signal within the system
- [[LME Warehouse Stocks]]: stocks measured in warrants
- [[Backwardation Squeeze]]: depleted on warrant stocks create squeeze conditions
- [[Cash to 3 Month Spread]]: warrant dynamics drive the cash/forward spread
- [[Physical Premium]]: premium above LME reflects cost of actually getting physical metal vs a warrant
- [[Cathode]]: LME copper warrants represent Grade A cathode of approved brands

## Common misconceptions

**"A warrant is like a futures contract."** A warrant is a document of title to physical metal, not a derivative. Holding a warrant means owning metal in a specific warehouse.

**"Cancelled warrants leave the LME system quickly."** Warehouse queues delay withdrawal for weeks or months. Cancellation signals intent, not immediate removal.

**"All metal in LME warehouses is deliverable."** Only metal on live (uncancelled) warrants is deliverable. Cancelled warrant metal is spoken for, reducing effective deliverable supply.

## Sources

- LME: Warrant and Metal Storage Rules
- LME: Physical Delivery Guide
- Neil Buxton, The London Metal Exchange
