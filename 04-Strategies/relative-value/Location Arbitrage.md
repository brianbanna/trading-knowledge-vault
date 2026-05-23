---
aliases: [location arb, geographic arbitrage, locational spread, basis trade]
tags:
  - "#energy/crude"
  - "#energy/natgas"
date-added: "2026-03-20"
---

# Location Arbitrage

## Core Thesis

Location arbitrage exploits price differences for the same (or equivalent) commodity at different physical locations. The spread between locations reflects transportation costs, pipeline tariffs, shipping rates, storage availability, and local supply/demand. When the location spread deviates from the cost of physical transportation, an arbitrage or [[Relative Value Trade]] opportunity exists. One of the most fundamental forms of commodity trading, tied directly to the physical movement of goods.

## Mechanics

### The Core Logic
If [[Brent Crude]] (FOB North Sea) trades at $80 and [[WTI Crude Oil]] (Cushing, Oklahoma) trades at $73, the $7 spread must be explained by the cost of moving barrels between the 2 locations. If shipping WTI from US Gulf Coast to Europe costs $4/bbl (freight, insurance, quality adjustment), the excess spread is $3. A physical trader buys WTI, ships to Europe, sells at Brent pricing, captures $3/bbl. In futures, traders express the same view: long WTI / short Brent.

### Entry Criteria
- Location spread exceeds or falls below estimated transportation cost (freight + tariff + quality adjustment + insurance)
- Infrastructure constraint creating a temporary dislocation (pipeline outage, port closure, weather)
- Inventory imbalance: one location oversupplied, the other drawing

### Exit Criteria
- Spread reverts to transportation cost equilibrium
- Physical flows respond (tankers reroute, pipeline flows adjust) and close the arb
- Infrastructure constraint resolves

### Position Sizing
Match notional and contract size between locations. [[Brent-WTI Spread]]: both 1,000 barrels, 1:1. [[TTF Natural Gas]] vs [[Henry Hub Natural Gas]]: contract sizes differ (TTF per MWh, Henry Hub per MMBtu), conversion ratios and currency adjustments needed.

## Instruments Used
- Crude: [[WTI Crude Oil]] vs [[Brent Crude]], WTI Midland vs WTI Cushing, Brent vs Dubai
- Natural gas: [[Henry Hub Natural Gas]] vs [[TTF Natural Gas]] (transatlantic gas arb), Henry Hub vs JKM (Asia LNG)
- Metals: LME copper vs COMEX copper, LME zinc vs SHFE zinc
- Agriculture: CBOT wheat vs Euronext milling wheat

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Transportation cost changes (freight rate spikes, tariff changes) |
| Max Loss Scenario | Permanent infrastructure change that alters the equilibrium spread |
| Hedged Exposure | Commodity price direction largely cancelled |
| Unhedged Exposure | Freight risk, currency risk (different currency locations), quality basis |
| Margin Requirements | Reduced for recognized inter exchange spreads; full margin for cross exchange |

## Edge Source

Informational: real time visibility into shipping rates, pipeline flows, port congestion, and local inventory provides an edge over participants on delayed data. Physical traders with access to ships, storage, and pipeline capacity have a structural edge because they execute the physical arbitrage, anchoring the spread.

## When It Works / When It Fails

### Works Well When
- Transportation infrastructure is stable and costs are predictable
- Local dislocations are temporary (weather, maintenance, short term demand spikes)
- Spread has clear mean reversion around a known cost of transport

### Fails When
- [[Structural Break]] in infrastructure: new pipeline, terminal closure, trade sanctions
- Freight rates are volatile and unpredictable (COVID, Suez Canal blockage)
- Sanctions or trade policy redirect physical flows permanently (Russia post 2022)
- Currency moves dominate the spread (cross currency location arbs)

## Historical Examples

**Cushing vs Gulf Coast (2011 to 2014):** WTI at Cushing traded at $15 to $25 discount to Brent because insufficient pipeline capacity existed to move barrels from the oversupplied Midcontinent to Gulf Coast export terminals. Physical traders who arranged rail transport captured the spread. Seaway pipeline reversal and subsequent capacity additions permanently narrowed the arb.

**Transatlantic LNG Arb (2022):** Post Russia/Ukraine, European gas (TTF) spiked to $70+/MMBtu equivalent while Henry Hub remained at $6 to $9. Spread far exceeded LNG shipping cost (~$2 to $3/MMBtu), attracting massive US LNG exports to Europe. The arb only closed when European storage filled and Asian competition for cargoes intensified.

## Concrete Example (Current or Recent)

**Concrete:** [[Henry Hub Natural Gas]] at $3.00/MMBtu. [[TTF Natural Gas]] at EUR 35/MWh (~$10.50/MMBtu at current FX). LNG liquefaction + shipping + regasification ~$4 to $5/MMBtu. Netback: $10.50 - $4.50 = $6.00/MMBtu vs Henry Hub at $3.00. Arb is open at $3.00/MMBtu. Long Henry Hub / short TTF captures this if the spread narrows. Risk: TTF spikes further on cold European winter, widening the spread before it narrows.

**Simplified:** Same commodity, different places. Prices have to differ by no more than it costs to move the commodity between them. When they differ by more, physical flows kick in and force the gap shut. Trade the deviations from transport cost.

## Related Strategies
- [[Relative Value Trade]]
- [[Brent-WTI Spread]]
- [[Inter-Commodity Spread]]
- [[Calendar Spread]]

## Related Concepts
- [[Storage Economics]]
- [[Convenience Yield]]
- [[Basis]]
- [[Contango]]
- [[Supply Shock]]
- [[Structural Break]]
- [[Commodity Currencies]]

---
*Status: #solid | Last reviewed: 2026-03-20*
