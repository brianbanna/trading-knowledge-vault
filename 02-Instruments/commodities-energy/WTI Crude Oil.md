---
aliases: [WTI, West Texas Intermediate, CL, NYMEX crude, Cushing crude]
tags:
  - "#energy/crude/wti"
date-added: "2026-03-20"
---

# WTI Crude Oil

## Overview

West Texas Intermediate is the primary US crude benchmark, traded on NYMEX (CME Group). Light sweet: 39.6 API, 0.24% sulfur, slightly lighter and sweeter than [[Brent Crude]]. The critical distinction: WTI is a landlocked benchmark with physical delivery at Cushing, Oklahoma, a pipeline hub with ~76 million barrels of storage. The landlocked structure creates unique pricing dynamics around storage economics and pipeline logistics that distinguish WTI from seaborne benchmarks. WTI is the most liquid crude oil futures contract in the world by volume.

## Concrete example

**Concrete:** Wednesday 10:30 ET. EIA Weekly Petroleum Status Report prints a Cushing draw of 3.2 million barrels vs consensus build of 0.5 mb. WTI front month (CL M6) was $78.20 going in. Trader was already long 15 CL contracts from $77.90 anticipating a draw based on Genscape satellite data the day before. Spot rips to $80.40 in 25 minutes as managed money chases. Trader sells 10 at $80.25, holds 5 for a run to $81.10 the next session. P&L: ($80.25 minus $77.90) × 1,000 × 10 plus ($81.10 minus $77.90) × 1,000 × 5 = $23,500 plus $16,000 = $39,500. The M1/M2 spread tightened 22 cents.

**Simplified:** WTI is the price of 1 barrel of US crude oil delivered at a storage hub in Oklahoma called Cushing. When Cushing tanks fill up, the price drops because nobody wants to take physical delivery. When they empty, the price rises. Traders watch the weekly EIA inventory report Wednesday morning to bet on whether storage went up or down. Each futures contract is 1,000 barrels, so $1 equals $1,000 per contract.

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
- US shale production (Permian Basin is the marginal global barrel): ~13+ million bbl/d total US output
- Pipeline capacity from Permian to Gulf Coast (Cushing or export terminals)
- Cushing inventory: the critical WTI specific variable. Low Cushing = delivery failure risk
- SPR releases and refills
- US export capacity (Gulf Coast terminals): since the 2015 export ban lift, WTI is linked to global markets via exports

### Demand Drivers
- US refinery throughput (PADD 2 and PADD 3)
- US gasoline and diesel consumption
- Export demand from Asian and European refiners (WTI as competitive grade)
- Petrochemical demand (light sweet preferred for ethane/propane rich feeds)

### Seasonality
Similar to [[Brent Crude]] but with Cushing specific effects. Spring turnaround (Mar to May) builds Cushing inventories as Midcontinent refineries go offline. Summer driving season (May to Sep) draws down product inventories, supporting crude demand. Winter sees Cushing builds if refinery maintenance extends. The WTI/Brent spread has its own seasonal patterns driven by US refinery cycles.

## Key Data and Reports
- EIA Weekly Petroleum Status Report: Cushing inventory is THE key WTI specific data point
- API Weekly Statistical Bulletin
- Baker Hughes US oil rig count
- COT report: NYMEX WTI managed money positioning
- Genscape/Kayrros Cushing tank farm satellite monitoring (real time inventory)
- US crude oil exports (EIA weekly)
- PADD 2 and PADD 3 refinery utilization

## Curve Structure
WTI curve dynamics resemble Brent but are amplified by Cushing storage constraints. When Cushing fills (>80% capacity), the front of the WTI curve collapses into extreme [[Contango]] because physical delivery becomes impossible without storage. This drove WTI to negative $37.63 on April 20 2020: with Cushing near capacity and COVID demand destroyed, expiring futures holders had no place to deliver and paid others to take the oil. When Cushing draws below 20 million barrels, [[Backwardation]] steepens sharply as delivery fears flip to scarcity fears.

## Key Spreads and Relative Value
- [[Brent-WTI Spread]]: the benchmark inter crude spread. WTI historically discounts to Brent reflecting landlocked logistics vs seaborne flexibility.
- WTI Cushing/Midland spread: Midland (Permian wellhead) vs Cushing (pipeline delivery). Pipeline constraints.
- WTI/WCS (Western Canadian Select): heavy sour Canadian vs light sweet WTI. Widens when Alberta pipeline capacity is constrained.
- [[Crack Spread]]: WTI 3:2:1 crack (3 WTI : 2 RBOB gasoline : 1 ULSD). The standard US refining margin proxy.
- [[Calendar Spread]]: M1/M2 and M1/M6 are the most liquid. Cushing inventories drive the front spread.

## Important Relationships
- Cushing inventory is the single most important WTI specific driver
- [[Brent Crude]] spread reflects Atlantic Basin relative economics
- [[Commodity Currencies]]: USD/CAD is partly driven by WTI (Canadian oil sands)
- US shale production growth responds to WTI price with 4 to 6 month lag (drilling economics)
- OPEC+ decisions affect WTI indirectly through global supply balance

## Trading Notes

The April 2020 negative print proved WTI's physical delivery mechanism carries tail risks that cash settled benchmarks (ICE Brent) do not. Traders holding WTI through expiry must understand Cushing logistics.

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
