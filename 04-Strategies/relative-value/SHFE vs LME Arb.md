---
aliases: [SHFE-LME arbitrage, China arb, import arb, copper arb]
tags:
  - "#metals/base/copper"
  - "#metals/base"
date-added: "2026-03-20"
---

# SHFE vs LME Arb

## Definition

The SHFE vs LME arbitrage is the relative value trade between Chinese ([[SHFE]]) and international ([[LME]]) base metal prices. The trade exploits price discrepancies between the two exchanges after adjusting for VAT (13% in China), freight, insurance, import duties, and the USD/CNY exchange rate. When the SHFE price is high relative to LME on an import parity basis, the "arb window is open" and it is profitable to buy metal internationally and import it into China. When SHFE is low relative to LME, the window is closed and metal may flow out of China. This arb mechanism is the primary driver of physical metal flows between the international and Chinese markets.

## Why it matters (commodities and FX)

The SHFE/LME arb is the single most important flow signal for base metals. When the arb window opens, Chinese traders import metal aggressively, drawing down [[LME Warehouse Stocks]] and supporting LME prices. When the window closes, LME stocks rebuild. The arb ratio (SHFE price / LME price adjusted for costs) is tracked by every major metals desk. For FX traders, the arb window also affects USD/CNY demand because Chinese importers need dollars to buy LME metal. Large scale metal imports can create marginal dollar demand in the Chinese FX market.

## Concrete example

LME copper is $9,500/tonne. The import parity breakeven for SHFE is CNY 74,500 (LME × 7.15 USD/CNY × 1.13 VAT + $100 premium and freight). SHFE copper is at CNY 77,000, meaning the arb window is open with CNY 2,500/tonne profit. A trader goes long LME copper and short SHFE copper (or simply buys physical for import). As Chinese imports accelerate, LME stocks fall from 150,000 to 100,000 tonnes over 2 months, and LME copper rises to $10,000. If SHFE drops to CNY 73,000 (arb window closes), the import flow stops and LME stops benefiting from the draw.

## Key mechanics and formulas

**Import parity:** `Breakeven = LME Price × USD/CNY × 1.13 + Premium + Freight + Insurance`

**Arb indicator:** `SHFE/LME Ratio = SHFE Price / (LME Price × USD/CNY × 1.13)`

- Ratio > 1.02: arb window open (profitable to import)
- Ratio 0.98 to 1.02: arb closed (marginal)
- Ratio < 0.98: reverse arb (profitable to export from China, rare)

**Lag:** Physical arb takes 4 to 8 weeks to execute (purchasing, shipping, customs clearance). The price must remain favorable long enough to complete the trade.

## Prerequisites

- [[SHFE]]
- [[LME]]
- [[Copper Futures]]
- [[Physical Premium]]

## Related concepts (learn next)

- [[SHFE]] because it is the Chinese exchange leg of the arb.
- [[LME]] because it is the international leg.
- [[LME Warehouse Stocks]] because arb flows directly affect LME inventory levels.
- [[Physical Premium]] because Shanghai bonded premiums reflect arb economics.
- [[Cancelled Warrants]] because arb driven imports show up as LME warrant cancellations in Asia.
- [[China PMI]] because Chinese economic conditions determine whether the SHFE premium persists.
- [[Location Arbitrage]] because SHFE/LME is the largest location arb in base metals.

## Common misconceptions

**"The arb is a risk free trade."** Currency risk (USD/CNY moves), execution lag (4 to 8 weeks exposure), and counterparty risk all create real risk. The arb window can close while cargo is in transit.

**"Only Chinese traders do this arb."** International trading houses (Trafigura, Glencore, IXM) are major participants, often pre positioning metal in bonded warehouses near Chinese ports.

**"The arb only matters for copper."** Similar arb dynamics exist for aluminum, zinc, nickel, and other metals, though copper is the most actively traded.

## Sources

- CRU Group: China Metal Import Parity Analysis
- Fastmarkets: Shanghai Bonded Premium Assessments
- Bloomberg: SHFE/LME Ratio and Arb Window Monitor
