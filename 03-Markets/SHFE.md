---
aliases: [Shanghai Futures Exchange, SHFE]
tags:
  - "#metals/base"
date-added: "2026-03-20"
---

# SHFE

## Definition

The Shanghai Futures Exchange is China's primary commodity futures exchange. It trades copper, aluminum, zinc, nickel, tin, lead, gold, silver, steel rebar, hot rolled coil, and other contracts. With China consuming ~50% of global base metals, SHFE prices are critical reference points for Asian and global metal markets. SHFE contracts are denominated in Chinese yuan (CNY), trade in Chinese hours, and have a separate domestic warehouse delivery system. SHFE is not directly accessible to most foreign traders (except through the Shanghai International Energy Exchange for certain contracts), creating natural segmentation between LME (international) and SHFE (Chinese) pricing.

## Why it matters (commodities and FX)

China's dominant metal consumption means SHFE often leads global moves, especially for copper and aluminum. The SHFE to [[LME]] price ratio (adjusted for VAT, freight, FX) determines whether Chinese traders profit from importing metal, driving physical flows. When the [[SHFE vs LME Arb]] window opens (SHFE high vs LME), metal flows into China and draws down LME stocks. When it closes, Chinese metal flows out. For macro traders, SHFE action during Chinese hours provides early signals for LME direction when London opens.

## Concrete example

**Concrete:** SHFE copper at CNY 76,000/tonne, LME copper at $9,500/tonne. Import parity (LME × USD/CNY × 1.13 VAT + premium + freight) breakeven at CNY 74,500. SHFE premium of CNY 1,500 above import parity makes importing profitable. Metal flows into China, drawing down LME Asian warehouse stocks. LME prices rise as available metal shrinks. Trader monitoring the SHFE premium goes long 30 LME copper 3M at $9,500 ahead of the flow. LME copper rallies to $9,700 over 3 weeks. Gain: $200 × 25 tonnes × 30 = $150,000.

**Simplified:** China consumes half the world's industrial metal. SHFE is where Chinese traders buy and sell that metal in yuan. The gap between SHFE and LME (after VAT, freight, and FX) tells you which direction metal will flow physically. If SHFE is rich, importers ship metal into China and LME warehouses empty out, supporting LME prices. If SHFE is cheap, Chinese metal looks for export and LME stocks rebuild. Track the gap, not just the prices.

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
- [[LME Warehouse Stocks]] because SHFE arb flows affect LME inventory.
- [[Green Metals]] because Chinese energy transition policy affects SHFE metal demand.

## Common misconceptions

**"SHFE and LME prices are the same after currency conversion."** VAT (13%), premiums, freight, and capital controls create persistent differences. The 2 prices can diverge significantly.

**"Foreign traders cannot access SHFE."** SHFE is mostly domestic, but some contracts are open to international traders through the INE (International Energy Exchange) platform.

**"SHFE follows LME."** During Chinese hours, SHFE often leads, and LME adjusts at London open. Influence is bidirectional.

## Sources

- SHFE: Contract Specifications and Trading Rules
- SHFE: Approved Delivery Warehouses
- CRU Group: Chinese Metals Market Analysis
