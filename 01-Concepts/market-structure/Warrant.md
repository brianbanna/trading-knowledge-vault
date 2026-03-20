---
aliases: [LME warrant, warehouse warrant, warrant system]
tags:
  - "#metals/base"
date-added: "2026-03-20"
---

# Warrant

## Definition

An LME warrant is a document of title representing a specific lot of metal stored in an [[LME]] approved warehouse. Each warrant corresponds to a standard lot (25 tonnes for copper, aluminum, zinc, lead; 6 tonnes for nickel; 5 tonnes for tin) of approved brand metal that meets LME quality specifications. Metal "on warrant" is available for delivery against LME futures contracts. When a holder wants to withdraw metal from the warehouse (to use it, sell it physically, or move it), they "cancel" the warrant, signaling their intent to take delivery. The warrant system is the mechanism that anchors LME futures prices to the physical metal market.

## Why it matters (commodities and FX)

The warrant system is how the LME connects its financial contracts to physical reality. Rising cancelled warrants ([[Cancelled Warrants]]) signal that physical buyers are actively pulling metal from the system, indicating real demand. The total stock of metal on warrant determines how much metal is immediately deliverable, which in turn affects delivery risk for short positions. When on warrant stocks fall to very low levels, shorts face the risk of a [[Backwardation Squeeze]] as they cannot source metal for delivery. Understanding the warrant system is essential for anyone trading LME metals or assessing physical market conditions.

## Concrete example

A producer delivers 1,000 tonnes of copper cathode (40 warrants at 25 tonnes each) into an LME warehouse in Rotterdam, receiving warrants that can be sold on the exchange. A Chinese trader buys these warrants through the LME and cancels them, intending to withdraw the metal for shipment to Shanghai. The cancelled warrants show up in the daily [[LME Warehouse Stocks]] report, signaling physical demand. If many traders cancel warrants simultaneously, on warrant stocks drop rapidly, and the [[Cash to 3 Month Spread]] moves into backwardation.

## Key mechanics and formulas

**Warrant lifecycle:**
1. Metal delivered to LME approved warehouse
2. Warehouse issues warrant (document of title)
3. Warrant is "live" (on warrant), available for LME delivery
4. Holder cancels warrant (intends to withdraw)
5. Metal queued for withdrawal from warehouse
6. Metal physically removed

**Cancellation to withdrawal lag:** Depending on warehouse queue length, 1 day to several months (historically, queues at some warehouses exceeded 2 years).

## Prerequisites

- [[LME]]
- [[LME Warehouse Stocks]]
- [[Delivery]]

## Related concepts (learn next)

- [[Cancelled Warrants]] because cancellation is the key signal within the warrant system.
- [[LME Warehouse Stocks]] because stocks are measured in terms of warrants.
- [[Backwardation Squeeze]] because depleted on warrant stocks create squeeze conditions.
- [[Cash to 3 Month Spread]] because warrant dynamics drive the cash/forward spread.
- [[Physical Premium]] because the premium above LME reflects the cost of actually getting physical metal vs a warrant.
- [[Cathode]] because LME copper warrants represent Grade A cathode of approved brands.

## Common misconceptions

**"A warrant is like a futures contract."** A warrant is a document of title to physical metal, not a derivative. Holding a warrant means you own metal in a specific warehouse.

**"Cancelled warrants always leave the LME system quickly."** Warehouse queues can delay actual withdrawal for weeks or months. Cancellation signals intent, not immediate removal.

**"All metal in LME warehouses is available for delivery."** Only metal on live (uncancelled) warrants is deliverable. Cancelled warrant metal is spoken for, reducing effective deliverable supply.

## Sources

- LME: Warrant and Metal Storage Rules
- LME: Physical Delivery Guide
- Neil Buxton, The London Metal Exchange
