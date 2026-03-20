---
aliases: [LME stocks, LME inventory, warehouse stocks]
tags:
  - "#metals/base"
date-added: "2026-03-20"
---

# LME Warehouse Stocks

## Definition

LME warehouse stocks are the quantities of metal stored in [[LME]] approved warehouses around the world. These warehouses (operated by companies like ISTIM, C. Steinweg, and Henry Bath) are located in key logistics hubs across Asia, Europe, and the Americas. LME stocks represent the "visible" inventory of base metals, reported daily and broken down by warehouse location and metal type. The data includes total stocks, in/out movements, and [[Cancelled Warrants]] (metal earmarked for withdrawal). While LME stocks are the most closely watched inventory data for base metals, they represent only a fraction of total global metal inventory, as significant volumes are held in non LME warehouses, bonded zones, and producer/consumer stockpiles.

## Why it matters (commodities and FX)

LME stock changes are the highest frequency fundamental signal for base metals prices. Declining stocks signal demand strength and support prices. Rising stocks signal oversupply and weigh on prices. The rate of change matters more than the absolute level: a sharp drawdown signals urgent physical demand, while a gradual build may be tolerable. Location data adds another dimension: metal flowing into Asian warehouses suggests Chinese destocking to LME, while draws from European warehouses signal regional demand. [[Cancelled Warrants]] within the data are a leading indicator because they show intentions before actual metal movement.

## Concrete example

LME copper stocks have fallen from 200,000 tonnes to 120,000 tonnes over 8 weeks. Cancelled warrants are at 45% (meaning 54,000 tonnes are requested for withdrawal). A trader interprets this as strong physical demand and goes long copper. If drawdowns continue to 80,000 tonnes, the [[Cash to 3 Month Spread]] likely moves into steep backwardation and copper prices rally $500/tonne. If the draw was a one time Chinese import event and restocking begins, stocks could rebuild to 160,000 tonnes, and the rally fades.

## Key mechanics and formulas

**Daily data reported:**
- Opening stocks (by metal, by warehouse location)
- Arrivals (metal delivered in)
- Withdrawals (metal taken out)
- Closing stocks
- Cancelled warrants (metal earmarked for withdrawal)

**Cancellation ratio:** `Cancellation Ratio = Cancelled Warrants / Total Stocks × 100%`

Above 30% = significant physical demand. Above 50% = very tight.

**Global warehouse locations:** ~500 approved warehouses across 34 locations in 13 countries.

## Prerequisites

- [[LME]]
- [[Cash to 3 Month Spread]]
- [[Warrant]]

## Related concepts (learn next)

- [[Cancelled Warrants]] because they are the leading indicator within the warehouse stocks data.
- [[Warrant]] because stock data tracks metal on warrant (deliverable) vs cancelled (being withdrawn).
- [[Cash to 3 Month Spread]] because stock levels and changes drive the spread.
- [[Physical Premium]] because low LME stocks push up regional premiums.
- [[SHFE]] because comparing LME and SHFE stocks reveals East/West inventory dynamics.
- [[Backwardation Squeeze]] because depleted stocks create squeeze conditions.

## Common misconceptions

**"LME stocks are total global inventory."** They are only the visible, deliverable portion. Off warrant stocks in non LME warehouses, bonded storage, and producer stockpiles can be multiples of LME stocks.

**"Falling stocks always mean strong demand."** Stocks can fall because of warehouse queue manipulation, metal reclassification, or arbitrage driven flows between LME and SHFE systems.

**"All LME warehouse locations are equally important."** Asian warehouses (Singapore, South Korea) often see flows driven by Chinese arb dynamics. European and US warehouse moves reflect regional demand.

## Sources

- LME: Daily Stock Report
- LME: Warehouse and Stocks Data
- CRU Group: Metals Storage and Logistics Analysis
