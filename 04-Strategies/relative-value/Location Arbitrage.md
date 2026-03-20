---
aliases: [location arb, geographic arbitrage, locational spread, basis trade]
tags:
  - "#energy/crude"
  - "#energy/natgas"
date-added: "2026-03-20"
---

# Location Arbitrage

## Core Thesis

Location arbitrage exploits price differences for the same (or equivalent) commodity at different physical locations. The spread between locations reflects transportation costs, pipeline tariffs, shipping rates, storage availability, and local supply/demand balances. When the location spread deviates from the cost of physical transportation, an arbitrage or [[Relative Value Trade]] opportunity exists. This is one of the most fundamental forms of commodity trading, directly tied to the physical movement of goods.

## Mechanics

### The Core Logic
If [[Brent Crude]] (delivered FOB North Sea) trades at $80 and [[WTI Crude Oil]] (delivered Cushing, Oklahoma) trades at $73, the $7 spread must be explained by the cost of moving barrels between the 2 locations. If the all in cost of shipping WTI from the US Gulf Coast to Europe is $4/bbl (freight, insurance, quality adjustment), the "excess" spread is $3. A physical trader could buy WTI, ship it to Europe, and sell at Brent pricing, capturing $3/bbl profit. In futures markets, traders express this same view by going long WTI / short Brent.

### Entry Criteria
- Location spread exceeds or falls below estimated transportation cost (freight + tariff + quality adjustment + insurance)
- Infrastructure constraint creating a temporary dislocation (pipeline outage, port closure, weather)
- Inventory imbalance: one location is oversupplied while the other draws

### Exit Criteria
- Spread reverts to transportation cost equilibrium
- Physical flows respond (tankers reroute, pipeline flows adjust) and close the arb
- Infrastructure constraint resolves

### Position Sizing
Match notional value and contract size between locations. For [[Brent-WTI Spread]], both are 1,000 barrels, so 1:1. For [[TTF Natural Gas]] vs [[Henry Hub Natural Gas]], contract sizes differ (TTF is per MWh, Henry Hub per MMBtu), so conversion ratios and currency adjustments are needed.

## Instruments Used
- Crude: [[WTI Crude Oil]] vs [[Brent Crude]], WTI Midland vs WTI Cushing, Brent vs Dubai
- Natural gas: [[Henry Hub Natural Gas]] vs [[TTF Natural Gas]] (the "transatlantic gas arb"), Henry Hub vs JKM (Asia LNG)
- Metals: LME copper vs COMEX copper, LME zinc vs SHFE zinc
- Agriculture: CBOT wheat vs Euronext milling wheat

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Transportation cost changes (freight rate spikes, tariff changes) |
| Max Loss Scenario | Permanent infrastructure change that alters the equilibrium spread |
| Hedged Exposure | Commodity price direction largely cancelled |
| Unhedged Exposure | Freight risk, currency risk (if locations price in different currencies), quality basis |
| Margin Requirements | Reduced for recognized inter exchange spreads; full margin required for cross exchange |

## Edge Source

Informational: real time visibility into shipping rates, pipeline flows, port congestion, and local inventory provides an edge over participants relying on delayed data. Physical traders with access to ships, storage, and pipeline capacity have a structural edge because they can actually execute the physical arbitrage, anchoring the spread.

## When It Works / When It Fails

### Works Well When
- Transportation infrastructure is stable and costs are predictable
- Local dislocations are temporary (weather, maintenance, short term demand spikes)
- Spread has clear mean reversion properties around a known cost of transport

### Fails When
- [[Structural Break]] in infrastructure: new pipeline, terminal closure, trade sanctions
- Freight rates are volatile and unpredictable (as during COVID or Suez Canal blockage)
- Sanctions or trade policy changes redirect physical flows permanently (Russia post 2022)
- Currency moves dominate the spread (cross currency location arbs)

## Historical Examples

**Cushing vs Gulf Coast (2011 to 2014):** WTI at Cushing traded at a $15 to $25 discount to Brent because insufficient pipeline capacity existed to move barrels from the oversupplied Midcontinent to Gulf Coast export terminals. Physical traders who could arrange rail transport captured the spread. The Seaway pipeline reversal and subsequent capacity additions permanently narrowed the arb.

**Transatlantic LNG Arb (2022):** Post Russia/Ukraine, European gas prices (TTF) spiked to $70+/MMBtu equivalent while Henry Hub remained at $6 to $9. The spread far exceeded LNG shipping cost (~$2 to $3/MMBtu), attracting massive US LNG exports to Europe. The arb only closed when European storage filled and Asian competition for LNG cargoes intensified.

## Concrete Example (Current or Recent)

[[Henry Hub Natural Gas]] trades at $3.00/MMBtu. [[TTF Natural Gas]] trades at EUR 35/MWh (approximately $10.50/MMBtu at current exchange rates). LNG liquefaction + shipping + regasification cost is approximately $4 to $5/MMBtu. The netback: $10.50 - $4.50 = $6.00/MMBtu, vs Henry Hub at $3.00. The arb is open at $3.00/MMBtu. A trader going long Henry Hub / short TTF captures this if the spread narrows. Risk: TTF could spike further on a cold European winter, widening the spread before it narrows.

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
