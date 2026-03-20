---
aliases: [Shanghai Futures Exchange, SHFE]
tags:
  - "#metals/base"
date-added: "2026-03-20"
---

# SHFE

## Definition

The Shanghai Futures Exchange is China's primary commodity futures exchange, trading copper, aluminum, zinc, nickel, tin, lead, gold, silver, steel rebar, hot rolled coil, and other contracts. As China consumes approximately 50% of global base metals, SHFE prices are critical reference points for Asian and global metal markets. SHFE contracts are denominated in Chinese yuan (CNY), trade in Chinese trading hours, and have their own warehouse delivery system within China. SHFE is not directly accessible to most foreign traders (except through the Shanghai International Energy Exchange for certain contracts), creating a natural segmentation between LME (international) and SHFE (Chinese) pricing.

## Why it matters (commodities and FX)

China's dominant consumption of base metals means that SHFE prices often lead global moves, particularly for copper and aluminum. The price ratio between SHFE and [[LME]] (adjusted for VAT, freight, and exchange rate) determines whether it is profitable for Chinese traders to import metal, driving physical flows. When the [[SHFE vs LME Arb]] window opens (SHFE price high relative to LME), metal flows into China, drawing down LME stocks. When it closes, Chinese metal may flow out. For macro traders, SHFE price action during Chinese trading hours provides early signals for LME direction when London opens.

## Concrete example

SHFE copper is at CNY 76,000/tonne while LME copper is at $9,500/tonne. The import parity calculation (LME × exchange rate × 1.13 VAT + premium + freight) shows breakeven at CNY 74,500. The SHFE premium of CNY 1,500 above import parity means importing is profitable. Metal flows into China, drawing down LME Asian warehouse stocks. LME prices rise as available metal decreases. A trader who monitored the SHFE premium went long LME copper ahead of the flow.

## Key mechanics and formulas

**Key SHFE contracts:**
| Metal | Ticker | Contract Size | Currency |
|---|---|---|---|
| Copper | CU | 5 tonnes | CNY/tonne |
| Aluminum | AL | 5 tonnes | CNY/tonne |
| Zinc | ZN | 5 tonnes | CNY/tonne |
| Nickel | NI | 1 tonne | CNY/tonne |

**Import parity:** `SHFE Breakeven = LME × USD/CNY × 1.13 (VAT) + Premium + Freight`

**Trading hours:** 9:00 to 11:30, 13:30 to 15:00 Beijing time, plus night session 21:00 to 01:00.

## Prerequisites

- [[LME]]
- [[Copper Futures]]
- [[China PMI]]

## Related concepts (learn next)

- [[SHFE vs LME Arb]] because the inter exchange arb drives physical metal flows.
- [[LME]] because LME is the international counterpart to SHFE's Chinese pricing.
- [[China PMI]] because Chinese economic indicators drive SHFE demand.
- [[Physical Premium]] because Shanghai bonded premiums signal Chinese import demand.
- [[LME Warehouse Stocks]] because SHFE arb flows affect LME inventory levels.
- [[Green Metals]] because Chinese energy transition policy affects SHFE metal demand.

## Common misconceptions

**"SHFE and LME prices are the same after currency conversion."** VAT (13%), premiums, freight, and capital controls create persistent differences. The two prices can diverge significantly.

**"Foreign traders cannot access SHFE."** While SHFE is mostly domestic, some contracts are available to international traders through the INE (International Energy Exchange) platform.

**"SHFE follows LME."** During Chinese trading hours, SHFE often leads, and LME adjusts when London opens. The influence is bidirectional.

## Sources

- SHFE: Contract Specifications and Trading Rules
- SHFE: Approved Delivery Warehouses
- CRU Group: Chinese Metals Market Analysis
