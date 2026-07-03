---
aliases: [ULSD, heating oil, HO, gasoil, ultra low sulfur diesel, diesel futures]
tags:
  - "#energy/refined/diesel"
date-added: "2026-07-03"
---

# ULSD Heating Oil Futures

## Definition

The NYMEX heating oil contract, ticker HO, is the US benchmark for the middle of the barrel: diesel, heating oil, and a close proxy for jet fuel and gasoil. Priced in USD per gallon, it now specifies ultra low sulfur diesel (ULSD, maximum 15 ppm sulfur), reflecting that highway diesel and heating oil converged on the same low sulfur spec. It is the deliverable diesel proxy in the US, settling by physical delivery in New York Harbor. It is distinct from ICE Gasoil (ICE Europe, priced in USD per tonne), the European and Asian distillate benchmark that the two markets arb against. Last close was 3.1923 USD/gal on 2026-07-03, up 34.71% over 1 year, with the distillate crack near 65 USD/bbl. A supportive catalyst in the current tape is Russian refinery drone damage and the risk of a Russian diesel export ban.

## Why it matters (commodities and FX)

Distillate is the fuel of the industrial economy: trucking, rail, marine shipping, agriculture, construction, plus winter heating in the US Northeast. Because diesel demand tracks freight and industrial output rather than consumer travel, the distillate crack is a real time read on economic momentum in a way the [[Gasoline Crack]] is not. FX angle: diesel is a globally traded barrel, so Russian and Middle Eastern export bans and refinery outages reroute flows, feed into European inflation, and move the EUR. ULSD is also a jet fuel proxy relevant to airline hedging, since jet fuel competes for the same distillate pool. The industrial read plus the winter heating overlay make it a natural pairing against the more consumer driven gasoline in the refined complex.

## Concrete example

**Concrete:** Late September. Ukrainian drone strikes hit 2 large Russian refineries and knock out roughly 300,000 bbl/d of distillate capacity, and Moscow signals an extension of its diesel export ban. HO front month (HOX6) was 3.0600. Trader buys 4 HO at 3.0600. European gasoil rips, the transatlantic arb pulls US cargoes toward Europe, and NY Harbor distillate stocks draw hard, taking HO to the 3.1923 print. Win case P&L: (3.1923 minus 3.0600) USD/gal × 42,000 gal × 4 = 0.1323 × 42,000 × 4 = 22,226.40 USD (each cent per gallon is 420 USD per contract). Fail case: instead a ceasefire headline lands, Russian exports resume, a mild winter forecast trims heating demand, and EIA reports a distillate build of 5 million barrels. HO falls from 3.0600 to 2.9400. Loss: (2.9400 minus 3.0600) × 42,000 × 4 = minus 0.1200 × 42,000 × 4 = minus 20,160 USD.

**Simplified:** ULSD heating oil futures is the price of 1 gallon of diesel grade fuel delivered by pipeline and barge in New York Harbor. The same fuel runs trucks, trains, ships, and tractors, and heats homes in the US Northeast in winter. So it moves on freight and industrial demand plus winter cold, and on supply shocks like Russian refinery outages or export bans. Traders watch the Wednesday EIA distillate inventory number, Heating Degree Day forecasts, and European gasoil. Each contract is 42,000 gallons, so 1 cent per gallon equals 420 USD per contract.

## Contract specifications

| Field | Value |
|-------|-------|
| Exchange | NYMEX (CME Group) |
| Ticker | HO |
| Contract size | 42,000 gallons |
| Tick size | $0.0001/gallon |
| Tick value | $4.20 |
| Trading hours | Sun to Fri, 18:00 to 17:00 ET |
| Settlement | Physical delivery, New York Harbor (ULSD, 15 ppm sulfur) |
| Expiry months | Monthly, consecutive |
| Last trading day | Last business day of month prior to delivery |
| Currency | USD |

ICE Gasoil (ICE Europe, ticker G): 100 tonne contract, priced in USD/tonne, the European and Asian distillate benchmark. Convert using roughly 7.45 barrels per tonne of gasoil when comparing to HO.

## Fundamentals

### Supply drivers
- US refinery distillate yield and [[Refinery Utilization]]: the middle distillate slate competes with gasoline for barrels
- [[Turnaround Season]] and unplanned refinery outages
- Russian and Middle Eastern diesel exports and export bans: swing factors for the global balance
- Crude feedstock cost ([[WTI Crude Oil]])
- ICE Gasoil and European diesel balance, which clears against HO through the transatlantic arb
- IMO low sulfur marine fuel rules, which structurally pull distillate into the bunker pool

### Demand drivers
- Freight and trucking activity: diesel is the freight fuel
- Winter heating demand (US Northeast heating oil, roughly October to March)
- Agricultural cycles (planting and harvest diesel use)
- Jet fuel demand, a close substitute drawing on the same distillate pool
- Industrial production and GDP momentum

### Seasonality
Distillate carries 2 demand peaks: winter heating (November to February) and a lesser agricultural pull around planting and harvest. Heating demand is weather driven, so a cold snap in the US Northeast or Europe spikes the crack. The heating crack builds into winter and fades in spring. The current snapshot is July, so the roughly 65 USD/bbl crack is driven less by heating and more by the supply catalyst (Russian outages and export ban risk) and firm freight and industrial demand. See [[Seasonality]].

## Key data and reports
- EIA Weekly Petroleum Status Report: distillate inventories, production, and product supplied (implied demand)
- EIA distillate stocks by PADD (PADD 1 Northeast is the heating region)
- Refinery utilization rate (EIA weekly)
- Heating Degree Day (HDD) forecasts
- ICE Gasoil settlements, the European distillate benchmark
- COT report: NYMEX HO managed money positioning
- Freight indices (trucking, rail) as industrial demand proxies

## Curve structure
The distillate curve reflects winter heating demand, so winter contracts (December to February) usually trade at a premium in normal years. During supply shocks or cold snaps the front spikes into [[Backwardation]] as physical buyers scramble. In shoulder and summer months with ample stocks the curve softens toward [[Contango]]. The current tape shows front end strength driven by the Russian supply catalyst rather than by heating demand.

## Key spreads and relative value
- **[[Heating Crack]] (HO crack):** HO price in USD/bbl minus crude. The distillate refining margin. Snapshot near 65 USD/bbl.
- **[[Crack Spread]] 3:2:1:** 3 crude : 2 RBOB : 1 ULSD, the standard US refinery margin proxy.
- **HO vs [[RBOB Gasoline Futures|RBOB]] spread:** gasoline leads in summer, distillate leads in winter. A seasonal relative value pair.
- **HO vs ICE Gasoil (transatlantic distillate arb):** New York Harbor vs European gasoil, the flow that clears imbalances across the Atlantic.
- **HO calendar spreads:** winter vs summer, centered on the heating season roll.
- **Jet fuel vs HO differential:** jet fuel prices off HO as a distillate proxy.
- **[[Process Margin]]:** distillate is the middle of the barrel in the full refining economics.

## Important relationships
- The distillate crack is a business cycle indicator: strong freight and industrial demand widen it, unlike the gasoline crack, which is tied to consumer travel.
- Crude feedstock ([[WTI Crude Oil]]) is the dominant cost input.
- Russian and Middle Eastern export flows swing the global distillate balance, and export bans widen cracks.
- Winter Heating Degree Days drive the seasonal heating component.
- ICE Gasoil is tightly linked, with the transatlantic arb clearing imbalances.
- Jet fuel demand competes for the same distillate pool.
- IMO low sulfur marine fuel rules structurally raised distillate demand.

## Trading notes

*Add personal observations here.*

## Related instruments
- [[WTI Crude Oil]]
- [[Brent Crude]]
- [[RBOB Gasoline Futures]]
- [[Henry Hub Natural Gas]]

## Related concepts
- [[Crack Spread]]
- [[Heating Crack]]
- [[Process Margin]]
- [[Refinery Utilization]]
- [[Turnaround Season]]
- [[Seasonality]]
- [[Backwardation]]
- [[Contango]]
- [[Forward Curve]]
