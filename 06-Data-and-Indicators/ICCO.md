---
aliases: [ICCO, International Cocoa Organization, ICCO grindings, ICCO production forecast, cocoa grindings data]
tags:
  - "#agri/softs/cocoa"
date-added: "2026-03-24"
---

# ICCO

## Definition

The International Cocoa Organization (ICCO) is the intergovernmental body that publishes the most authoritative global cocoa supply/demand data. Think of the ICCO as the cocoa equivalent of [[WASDE]] for grains or [[IEA]] for oil. It compiles production estimates from every producing country, tracks grindings (the primary measure of cocoa demand), and publishes stock estimates. The 2 most market moving data points are the quarterly grindings reports (released by regional associations in Europe, North America, and Asia) and the ICCO's own annual production/surplus/deficit forecasts.

## Why it matters (commodities and FX)

Grindings data is the closest thing cocoa has to a demand indicator. Unlike oil (which has weekly inventory data) or grains (which have monthly WASDE updates), cocoa demand data comes quarterly, making each release a major event. A grindings number that beats or misses expectations by more than 2 to 3% moves prices. Production forecasts matter even more: cocoa's extreme supply concentration in West Africa means the global surplus or deficit is essentially a function of Ivory Coast + Ghana output. When the ICCO revises its deficit estimate larger, it directly affects the [[Forward Curve]] shape, pushing front months into steeper [[Backwardation]]. When it revises toward surplus, the curve flattens or moves into [[Contango]].

## Concrete example

The ICCO publishes its Q3 Bulletin forecasting a 2025/26 global deficit of 150,000 tonnes, wider than the prior estimate of 100,000 tonnes. The revision is driven by lower Ivory Coast main crop output (1.4 million tonnes vs the prior estimate of 1.55 million). ICE US cocoa (CC) front month rallies $250/tonne (approximately 3%) on the day. The curve steepens into backwardation as physical buyers rush to secure near term supply.

Conversely, if the ICCO had revised the deficit to 50,000 tonnes (better than expected Ivory Coast harvest), front month cocoa would likely have dropped $200/tonne and the backwardation would have compressed.

## Key mechanics and formulas

### Publication Schedule

| Report | Frequency | Timing | What It Covers |
|--------|-----------|--------|----------------|
| ICCO Quarterly Bulletin of Cocoa Statistics | Quarterly | Feb, May, Aug, Nov | Global production, grindings, stocks, prices |
| ICCO Annual Report | Annual | Usually Q1 | Full season review, medium term outlook |
| Regional Grindings Reports | Quarterly | Published by ECA (Europe), NCA (North America), CAA (Asia) about 2 weeks before ICCO compilation | Regional demand |

### Grindings Data

Grindings measure the volume of cocoa beans processed into cocoa butter, powder, and liquor. This is the primary demand indicator.

**Global grindings breakdown (approximate):**
- Europe (ECA): approximately 35% of global grindings. Published by the European Cocoa Association.
- Asia (CAA): approximately 20%. Published by the Cocoa Association of Asia.
- North America (NCA): approximately 15%. Published by the National Confectioners Association.
- Africa (local processing): approximately 20%. Growing due to origin grinding incentives in Ivory Coast and Ghana.
- Rest of world: approximately 10%.

**Reading grindings data:** Year on year change is the key metric. Above +3% = strong demand growth. Flat to -1% = stagnation. Below -3% = demand destruction (typically only during very high prices when manufacturers reformulate).

### Production Forecasts

**Global cocoa production (approximately 5.0 to 5.5 million tonnes/year):**
- Ivory Coast: approximately 2.0 to 2.2 million tonnes (approximately 40%)
- Ghana: approximately 700,000 to 1,000,000 tonnes (approximately 15 to 18%)
- Ecuador: approximately 350,000 tonnes
- Cameroon: approximately 250,000 tonnes
- Nigeria: approximately 250,000 tonnes
- Indonesia, Brazil, others: remainder

**Surplus/Deficit = Production - Grindings (adjusted for stock changes)**

A deficit above 100,000 tonnes is considered meaningful and supports prices. A surplus above 100,000 tonnes weighs on prices. The 2023/24 and 2024/25 seasons saw deficits exceeding 300,000 tonnes, the largest in decades.

### Stocks to Grindings Ratio

**Stocks to Grindings Ratio = End of Season Stocks / Annual Grindings**

This is cocoa's equivalent of the [[Stocks to Use Ratio]] in grains. Historical range: 30 to 50%. Below 30% = critically tight, supporting extreme backwardation and high prices. Above 45% = comfortable supply.

## Prerequisites

- [[Cocoa Futures]]
- [[Forward Curve]]
- [[Backwardation]]
- [[Stocks to Use Ratio]]

## Related concepts (learn next)

- [[West African Port Arrivals]] because weekly arrivals data provides higher frequency supply updates between ICCO quarterly publications.
- [[ICE Cocoa Stocks]] because exchange warehouse inventory is the most immediately deliverable supply and complements ICCO's broader stock estimates.
- [[COT Positioning]] because speculative positioning around ICCO release dates shows how the market is leaning, creating contrarian signals when positioning is extreme into a data release.
- [[Seasonality]] because cocoa production follows a clear main crop/mid crop pattern that ICCO data captures seasonally.
- [[Convenience Yield]] because ICCO deficit revisions directly affect the convenience yield priced into the front of the curve.
- [[Weather Premium]] because ICCO production forecasts are heavily influenced by West African rainfall, and the gap between current forecasts and weather risk creates trading opportunities.

## Common misconceptions

**"Grindings equals chocolate consumption."** Grindings measure industrial processing, not end consumer demand. A chocolate company may grind more beans to build butter/powder inventory ahead of anticipated price increases, inflating grindings without any change in consumer demand. Conversely, destocking can depress grindings even as retail sales grow.

**"ICCO data is timely enough for trading."** Quarterly data means you are always trading on 3 month old demand data. The market often prices in expected grindings well before the report, using proxy indicators like origin port arrivals, chocolate company earnings, and purchasing manager surveys. ICCO data confirms or refutes the market's expectations rather than providing new information.

**"A deficit automatically means higher prices."** If the deficit is already priced in (which it usually is if the ICCO is confirming what arrivals data and crop forecasters already signaled), the release may not move the market. The surprise relative to expectations is what drives the price reaction.

## Sources

- ICCO: Quarterly Bulletin of Cocoa Statistics
- ICCO: Annual Report and Monthly Cocoa Market Review
- European Cocoa Association (ECA): Quarterly Grindings
- National Confectioners Association (NCA): North American Quarterly Grindings
- Cocoa Association of Asia (CAA): Asian Quarterly Grindings
- Rabobank: Cocoa Market Outlook (quarterly)
