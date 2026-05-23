---
aliases: [ICCO, International Cocoa Organization, ICCO grindings, ICCO production forecast, cocoa grindings data]
tags:
  - "#agri/softs/cocoa"
date-added: "2026-03-24"
---

# ICCO

## Definition

The International Cocoa Organization (ICCO) is the intergovernmental body that publishes the most authoritative global cocoa supply and demand data. ICCO is to cocoa what [[WASDE]] is to grains and [[IEA]] is to oil. It compiles production estimates by country, tracks grindings (the primary demand measure), and publishes stock estimates. The two most market moving releases are quarterly grindings reports (from regional associations in Europe, North America, and Asia) and the ICCO's own annual production and surplus/deficit forecasts.

## Why it matters (commodities and FX)

Grindings is the closest proxy for cocoa demand. Unlike oil (weekly inventories) or grains (monthly WASDE), cocoa demand data comes quarterly, making each release a major event. A grindings number that beats or misses by 2 to 3% moves prices. Production forecasts matter more: cocoa's supply concentration in West Africa means the global surplus/deficit is essentially Ivory Coast + Ghana output. When ICCO revises its deficit larger, the [[Forward Curve]] steepens into [[Backwardation]]. Toward surplus, the curve flattens or moves into [[Contango]].

## Concrete example

**Concrete:** ICCO Q3 Bulletin forecasts a 2025/26 global deficit of 150,000 tonnes, wider than the prior 100,000 estimate. The revision is driven by lower Ivory Coast main crop (1.4M tonnes vs prior 1.55M). ICE US cocoa (CC) front month rallies $250/tonne (~3%) on the day. Curve steepens into backwardation as physical buyers chase nearby supply. Trader long 5 CC contracts gains $250 × 10 tonnes × 5 = $12,500.

**Simplified:** Cocoa supply comes mostly from Ivory Coast and Ghana. The ICCO publishes a quarterly tally of how much cocoa was made vs how much was consumed. If the deficit grows, prices rise and nearby contracts trade above later ones (backwardation) because users compete for scarce beans. If the deficit shrinks or flips to surplus, the opposite. The release itself is a scheduled event; you trade the gap between the new number and what was already priced in.

## Key mechanics and formulas

### Publication Schedule

| Report | Frequency | Timing | What It Covers |
|--------|-----------|--------|----------------|
| ICCO Quarterly Bulletin | Quarterly | Feb, May, Aug, Nov | Production, grindings, stocks, prices |
| ICCO Annual Report | Annual | Usually Q1 | Full season review, medium term outlook |
| Regional Grindings | Quarterly | ECA (Europe), NCA (North America), CAA (Asia), ~2 weeks before ICCO compilation | Regional demand |

### Grindings Data

Grindings measure cocoa beans processed into butter, powder, and liquor. The primary demand indicator.

**Global grindings split (approximate):**
- Europe (ECA): ~35%, European Cocoa Association
- Asia (CAA): ~20%, Cocoa Association of Asia
- North America (NCA): ~15%, National Confectioners Association
- Africa (origin processing): ~20%, growing on Ivory Coast and Ghana origin grinding incentives
- Rest of world: ~10%

**Reading grindings:** YoY change is the key metric. Above +3% = strong demand growth. Flat to −1% = stagnation. Below −3% = demand destruction (only at very high prices when manufacturers reformulate).

### Production Forecasts

**Global production (5.0 to 5.5 million tonnes/year):**
- Ivory Coast: 2.0 to 2.2M tonnes (~40%)
- Ghana: 700k to 1.0M tonnes (~15 to 18%)
- Ecuador: ~350k tonnes
- Cameroon: ~250k tonnes
- Nigeria: ~250k tonnes
- Indonesia, Brazil, others: remainder

**Surplus/Deficit = Production − Grindings (adjusted for stock changes)**

A deficit above 100,000 tonnes is meaningful and supports prices. A surplus above 100,000 weighs on prices. 2023/24 and 2024/25 saw deficits exceeding 300,000 tonnes, the largest in decades.

### Stocks to Grindings Ratio

**Stocks to Grindings Ratio = End of Season Stocks / Annual Grindings**

Cocoa's equivalent of the [[Stocks to Use Ratio]] in grains. Historical range 30 to 50%. Below 30% = critically tight, supports extreme backwardation and high prices. Above 45% = comfortable.

## Prerequisites

- [[Cocoa Futures]]
- [[Forward Curve]]
- [[Backwardation]]
- [[Stocks to Use Ratio]]

## Related concepts (learn next)

- [[West African Port Arrivals]] provides higher frequency supply updates between ICCO quarterly publications.
- [[ICE Cocoa Stocks]] is the most immediately deliverable supply, complementing ICCO's broader stock estimates.
- [[COT Positioning]] reveals how the market is leaning into the release, creating contrarian signals at extremes.
- [[Seasonality]] because cocoa production follows a main crop / mid crop pattern that ICCO captures seasonally.
- [[Convenience Yield]] because ICCO deficit revisions directly affect the convenience yield priced into the front.
- [[Weather Premium]] because ICCO production forecasts are driven by West African rainfall.

## Common misconceptions

**"Grindings equals chocolate consumption."** Grindings measure industrial processing, not consumer demand. Manufacturers can grind to build butter/powder inventory ahead of expected price increases. Destocking can depress grindings even as retail sales grow.

**"ICCO data is timely enough for trading."** Quarterly data means trading on 3 month old demand. The market prices in expected grindings before the report using proxies (port arrivals, chocolate company earnings, PMI). ICCO confirms or refutes rather than informs.

**"A deficit automatically means higher prices."** If the deficit is already priced in (usually it is, given arrivals and crop forecasters), the release may not move the market. The surprise vs expectations drives the reaction.

## Sources

- ICCO: Quarterly Bulletin of Cocoa Statistics
- ICCO: Annual Report and Monthly Cocoa Market Review
- European Cocoa Association (ECA): Quarterly Grindings
- National Confectioners Association (NCA): North American Quarterly Grindings
- Cocoa Association of Asia (CAA): Asian Quarterly Grindings
- Rabobank: Cocoa Market Outlook (quarterly)
