---
aliases: [RBOB, RBOB gasoline, gasoline futures, RB, reformulated blendstock]
tags:
  - "#energy/refined/gasoline"
date-added: "2026-07-03"
---

# RBOB Gasoline Futures

## Definition

RBOB gasoline futures trade on NYMEX (CME Group) under the ticker RB, priced in USD per gallon. RBOB stands for Reformulated Blendstock for Oxygenate Blending: it is unfinished gasoline designed to be blended with roughly 10% ethanol to make the finished E10 fuel sold at the pump. RBOB is the light end of the barrel, the lightest large volume product a refinery makes, so its price sits above crude and its margin over crude is the [[Gasoline Crack]]. The contract settles by physical delivery in New York Harbor, the main US East Coast pricing point. Last close was 2.9360 USD/gal on 2026-07-03, up 38.58% over 1 year, with the market inside the summer US driving season.

## Why it matters (commodities and FX)

Gasoline is the largest single product yield from a barrel of US crude, so the [[Gasoline Crack]] is a primary driver of refinery profitability and, through it, of crude demand. Pump prices are a politically sensitive consumer inflation input, which links gasoline to central bank policy and therefore to FX. The transatlantic gasoline arb (New York Harbor RBOB vs European Eurobob) moves cargoes across the Atlantic and prices partly in EUR, so the spread is an FX aware relative value trade. Gasoline is also the most seasonal energy product, a clean setting for studying [[Seasonality]] and calendar spread behavior. The current tape shows the gasoline crack near 54 USD/bbl and very wide, up about 53% month on month, a classic driving season squeeze.

## Concrete example

**Concrete:** Late June, the stretch between Memorial Day and July 4 that anchors peak US driving demand. Wednesday's EIA Weekly Petroleum Status Report prints a gasoline draw of 3.4 million barrels against consensus for a small build, and implied demand (product supplied) reads above 9.4 million bbl/d. RBOB front month (RBQ6) was 2.8850. Trader buys 5 RB at 2.8850. Refinery runs stay capped by a lingering [[Turnaround Season]] unit outage on the Gulf Coast and the crack blows out, dragging RBOB to the 2.9360 close. Win case P&L: (2.9360 minus 2.8850) USD/gal × 42,000 gal × 5 = 0.0510 × 42,000 × 5 = 10,710 USD (each cent per gallon is 420 USD per contract). Fail case: instead a tropical system dissipates offshore, Gulf Coast units return from maintenance at high [[Refinery Utilization]], and a surprise gasoline build of 4 million barrels hits. RBOB slides from 2.8850 to 2.8100. Loss: (2.8100 minus 2.8850) × 42,000 × 5 = minus 0.0750 × 42,000 × 5 = minus 15,750 USD.

**Simplified:** RBOB is the price of 1 gallon of unfinished gasoline blendstock delivered by pipeline and barge in New York Harbor. Refiners make it from crude, then blenders add about 10% ethanol to sell it at the pump. Summer driving season, roughly Memorial Day through Labor Day, is peak demand, so cracks and prices tend to build into the summer. Traders watch the Wednesday EIA gasoline inventory number, refinery run rates, and hurricane risk on the Gulf Coast. Each contract is 42,000 gallons, so 1 cent per gallon equals 420 USD per contract.

## Contract specifications

| Field | Value |
|-------|-------|
| Exchange | NYMEX (CME Group) |
| Ticker | RB |
| Contract size | 42,000 gallons |
| Tick size | $0.0001/gallon |
| Tick value | $4.20 |
| Trading hours | Sun to Fri, 18:00 to 17:00 ET |
| Settlement | Physical delivery, New York Harbor |
| Expiry months | Monthly, consecutive |
| Last trading day | Last business day of month prior to delivery |
| Currency | USD |

## Fundamentals

### Supply drivers
- US refinery gasoline production and [[Refinery Utilization]] (PADD 3 Gulf Coast is the production heartland, PADD 1 East Coast is the demand and delivery region)
- [[Turnaround Season]]: spring maintenance pulls units offline and cuts gasoline output just as demand rises
- RVP (Reid Vapor Pressure) spec switch: summer grade gasoline is more costly to produce and cannot be as volatile, which tightens supply from spring into summer
- Imports into New York Harbor, with Europe as the swing supplier via the transatlantic arb
- Gulf Coast hurricanes (Jun to Nov): refinery outages spike cracks
- Crude feedstock cost ([[WTI Crude Oil]], [[Brent Crude]])
- Ethanol blending economics and RIN (Renewable Identification Number) prices

### Demand drivers
- US vehicle miles traveled (VMT) and employment
- Summer driving season (Memorial Day to Labor Day): the dominant seasonal pull
- Moderate price elasticity: high pump prices eventually curb discretionary trips
- Consumer sentiment and broad economic activity

### Seasonality
Gasoline is the most seasonal refined product. Demand peaks in summer driving season, and the spring switch from winter grade to summer grade RVP tightens supply ahead of it. Cracks typically build from February and March into the summer, peak around May to July, then fade into autumn as demand drops and the cheaper winter grade returns. The current snapshot fits the pattern: driving season underway, the [[Gasoline Crack]] near 54 USD/bbl and up about 53% month on month.

## Key data and reports
- EIA Weekly Petroleum Status Report: gasoline inventories, production, and implied demand (product supplied)
- EIA gasoline stocks by PADD (PADD 1B, the New York Harbor region, is delivery relevant)
- Refinery utilization rate (EIA weekly)
- RVP spec transition dates (winter grade to summer grade)
- COT report: NYMEX RB managed money positioning
- Colonial Pipeline flows and allocations (Gulf Coast to East Coast)
- NOAA Atlantic hurricane season forecasts

## Curve structure
The gasoline curve is strongly seasonal. Summer contracts trade at a premium to winter contracts on both demand and the costlier summer RVP spec. The September to October roll is notorious: the last summer spec contract (September) to the first winter spec contract (October) can gap sharply as the spec and demand both step down. During peak driving season with tight stocks the front trades in [[Backwardation]]. After summer the curve tends to flip toward [[Contango]] as demand falls and stocks rebuild.

## Key spreads and relative value
- **[[Gasoline Crack]] (RBOB crack):** RB price in USD/bbl minus crude. The core refining margin for the light end of the barrel. Snapshot near 54 USD/bbl and very wide.
- **[[Crack Spread]] 3:2:1:** 3 crude : 2 RBOB : 1 ULSD, the standard US refinery margin proxy.
- **RBOB vs [[ULSD Heating Oil Futures|ULSD]] spread:** gasoline leads in summer, distillate leads in winter. A seasonal relative value pair inside the refined complex.
- **RBOB calendar spreads:** summer vs winter, especially the September to October RVP roll.
- **Transatlantic gasoline arb:** New York Harbor RBOB vs European Eurobob. The arb window governs import flows into the US East Coast.
- **[[Process Margin]]:** RBOB is one leg of the full barrel refining economics alongside distillate.

## Important relationships
- Crude feedstock ([[WTI Crude Oil]], [[Brent Crude]]) is the dominant cost input. RBOB and crude are strongly correlated, but the crack isolates the refining margin.
- Refinery utilization and cracks are usually inverse: high utilization adds gasoline supply and compresses the crack, unless demand outruns supply as in peak season.
- Hurricane season (Jun to Nov) skews risk to the upside through Gulf Coast outages.
- Ethanol (corn) is a blend component, and RIN prices shape blending economics.
- Summer driving demand and VMT are the core demand signal.
- Strong seasonality dominates the product. See [[Seasonality]].

## Trading notes

*Add personal observations here.*

## Related instruments
- [[WTI Crude Oil]]
- [[Brent Crude]]
- [[ULSD Heating Oil Futures]]
- [[Henry Hub Natural Gas]]

## Related concepts
- [[Crack Spread]]
- [[Gasoline Crack]]
- [[Process Margin]]
- [[Refinery Utilization]]
- [[Turnaround Season]]
- [[Seasonality]]
- [[Backwardation]]
- [[Contango]]
- [[Forward Curve]]
