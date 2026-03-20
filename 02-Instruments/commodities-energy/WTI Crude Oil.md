---
aliases: [WTI, West Texas Intermediate, CL, NYMEX crude, Cushing crude]
tags:
  - "#energy/crude/wti"
date-added: "2026-03-20"
---

# WTI Crude Oil

## Overview

West Texas Intermediate is the primary US crude oil benchmark, traded on NYMEX (CME Group). WTI is a light, sweet crude (approximately 39.6 API gravity, ~0.24% sulfur), making it slightly lighter and sweeter than [[Brent Crude]]. The critical distinction: WTI is a landlocked benchmark with physical delivery at Cushing, Oklahoma, a pipeline hub with approximately 76 million barrels of storage capacity. This landlocked nature creates unique pricing dynamics, particularly around storage economics and pipeline logistics, that distinguish WTI from seaborne benchmarks. WTI is the most liquid crude oil futures contract in the world by volume.

## Contract Specifications

| Field | Value |
|-------|-------|
| Exchange | NYMEX (CME Group) |
| Ticker | CL |
| Contract Size | 1,000 barrels |
| Tick Size | $0.01/barrel |
| Tick Value | $10.00 |
| Trading Hours | Sun to Fri, 17:00 to 16:00 CT |
| Settlement | Physical delivery at Cushing, Oklahoma |
| Expiry Months | Monthly, consecutive months for 9 years |
| Last Trading Day | 3rd business day before 25th of month prior to delivery |
| Currency | USD |

Micro WTI (MCL): 100 barrel contract, same mechanics, 1/10 size.

## Fundamentals

### Supply Drivers
- US shale production (Permian Basin is the marginal global barrel): approximately 13+ million bbl/d total US output
- Pipeline capacity from Permian to Gulf Coast (Cushing or export terminals)
- Cushing inventory levels: the critical WTI specific variable. Low Cushing = operational risk of delivery failure
- SPR releases and refills
- US export capacity (Gulf Coast terminals): since the 2015 export ban lift, WTI pricing is linked to global markets via exports

### Demand Drivers
- US refinery throughput (PADD 2 and PADD 3 refinery demand)
- US gasoline and diesel consumption
- Export demand from Asian and European refiners (WTI as a competitive grade)
- Petrochemical demand (light sweet crude preferred for ethane/propane rich feeds)

### Seasonality
Similar to [[Brent Crude]] but with Cushing specific effects. Spring turnaround season (Mar to May) can build Cushing inventories as Midcontinent refineries go offline. Summer driving season (May to Sep) draws down product inventories, supporting crude demand. Winter can see Cushing builds if refinery maintenance extends. The WTI/Brent spread has its own seasonal patterns driven by US refinery cycles.

## Key Data and Reports
- EIA Weekly Petroleum Status Report: Cushing inventory levels are THE key WTI specific data point
- API Weekly Statistical Bulletin
- Baker Hughes US oil rig count
- COT report: NYMEX WTI managed money positioning
- Genscape/Kayrros Cushing tank farm satellite monitoring (real time inventory estimates)
- US crude oil exports (EIA weekly)
- PADD 2 and PADD 3 refinery utilization

## Curve Structure
WTI curve dynamics are similar to Brent but amplified by Cushing storage constraints. When Cushing fills up (>80% capacity), the front of the WTI curve can collapse into extreme [[Contango]] because physical delivery becomes impossible without storage. This is what drove WTI to negative $37.63 on April 20, 2020: with Cushing near capacity and demand destroyed by COVID, holders of expiring futures had no place to deliver and were forced to pay others to take the oil. Conversely, when Cushing draws below 20 million barrels, [[Backwardation]] can steepen sharply as delivery fears flip to supply scarcity fears.

## Key Spreads and Relative Value
- [[Brent-WTI Spread]]: the benchmark inter crude spread. WTI historically trades at a discount to Brent reflecting landlocked logistics vs seaborne flexibility.
- WTI Cushing/Midland spread: Midland (Permian Basin wellhead) vs Cushing (pipeline delivery). Reflects pipeline constraints.
- WTI/WCS (Western Canadian Select): heavy sour Canadian crude vs light sweet WTI. Widens when pipeline capacity from Alberta is constrained.
- [[Crack Spread]]: WTI 3:2:1 crack (3 WTI : 2 RBOB gasoline : 1 ULSD). The standard US refining margin proxy.
- [[Calendar Spread]]: M1/M2 and M1/M6 are the most liquid. Cushing inventories drive the front spread.

## Important Relationships
- Cushing inventory level is the single most important WTI specific driver
- [[Brent Crude]] spread reflects Atlantic Basin relative economics
- [[Commodity Currencies]]: USD/CAD is partly driven by WTI (Canadian oil sands production)
- US shale production growth responds to WTI price with approximately 4 to 6 month lag (drilling economics)
- OPEC+ decisions affect WTI indirectly through global supply balance

## Trading Notes

The April 2020 negative price event demonstrated that WTI's physical delivery mechanism creates tail risks that purely financial benchmarks (like ICE Brent cash settled) do not have. Traders holding WTI through expiry must understand Cushing logistics.

## Related Instruments
- [[Brent Crude]]
- [[RBOB Gasoline Futures]]
- [[ULSD Heating Oil Futures]]
- [[Henry Hub Natural Gas]]

## Related Concepts
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Storage Economics]]
- [[Location Arbitrage]]
- [[Convenience Yield]]
- [[Roll Yield]]
- [[Supply Shock]]

---
*Status: #solid | Last reviewed: 2026-03-20*
