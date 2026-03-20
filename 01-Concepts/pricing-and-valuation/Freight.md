---
aliases: [tanker freight, shipping cost, VLCC rate, worldscale]
tags:
  - "#energy/crude"
  - "#macro"
date-added: "2026-03-20"
---

# Freight

## Definition

Freight in commodity markets refers to the cost of shipping physical commodities (primarily crude oil and refined products) by sea. Tanker freight rates are determined by vessel supply (available ships), cargo demand (volume of oil being moved), route length, and port congestion. Rates are typically quoted in Worldscale (WS, a percentage of a reference flat rate for each route) or in dollars per barrel/tonne. Tanker sizes range from small Handysize vessels (~30,000 DWT) to Very Large Crude Carriers (VLCCs, ~300,000 DWT). Freight is a crucial variable in commodity arbitrage because it determines whether moving oil from one region to another is economically viable.

## Why it matters (commodities and FX)

Freight costs are the gatekeeper for trade flow arbitrages. A Brent/Dubai [[EFS]] spread of $3/bbl only creates a profitable arbitrage if the freight from the North Sea to Asia is less than $3/bbl. When freight rates spike (due to geopolitical events, fleet shortages, or seasonal demand), arbitrage windows close even if the commodity spread looks attractive. Freight spikes can themselves move commodity prices: when Houthi attacks disrupted Red Sea shipping in 2024, tanker rates doubled and oil prices rose because effective delivered costs increased. For cross asset traders, shipping stocks and freight derivatives (FFAs) provide additional trading opportunities.

## Concrete example

A trader identifies a WTI to China arbitrage. WTI at the US Gulf Coast is $78/bbl, and the equivalent price in Shandong, China is $84/bbl. The spread is $6/bbl. VLCC freight from the US Gulf to China is currently $4.50/bbl, plus insurance and port costs of $0.50, totaling $5.00/bbl in transport. The net margin is $1.00/bbl on a 2 million barrel VLCC cargo, earning $2 million. If freight spikes to $7/bbl (seasonal tanker demand or fleet disruption), the arb turns negative and the cargo is uneconomic. The trader must lock in freight before committing to the cargo.

## Key mechanics and formulas

**Freight rate quoting:**
- Worldscale (WS): percentage of a reference flat rate. WS100 = full reference rate. WS50 = half.
- Time charter equivalent (TCE): daily revenue in $/day after voyage costs.
- Dollars per barrel: most intuitive for oil traders.

**Vessel sizes:**
- VLCC: ~2 million barrels, long haul routes (Middle East to Asia, US Gulf to China)
- Suezmax: ~1 million barrels, medium routes (West Africa to Europe)
- Aframax: ~600,000 barrels, short routes (North Sea, Caribbean)

**Arbitrage condition:** `Commodity Spread > Freight + Insurance + Port Costs`

## Prerequisites

- [[Brent Crude]]
- [[EFS]]
- [[Location Arbitrage]]

## Related concepts (learn next)

- [[EFS]] because freight costs determine whether East/West crude arbs are profitable.
- [[Location Arbitrage]] because freight is the cost component that makes or breaks location arbs.
- [[Floating Storage]] because tankers are used for floating storage when contango exceeds freight plus storage costs.
- [[Chokepoint]] because chokepoint disruptions create freight spikes and rerouting costs.
- [[Contango]] because contango width relative to freight costs determines storage trade viability.
- [[Dubai Crude]] because Asian crude pricing is heavily influenced by freight dynamics.

## Common misconceptions

**"Freight is a small cost that can be ignored."** On long haul routes, freight can be $3 to $8/bbl or more, which is significant relative to typical inter basin spreads of $2 to $6.

**"Freight rates are stable."** They are among the most volatile prices in commodity markets. VLCC rates can double in a week during supply disruptions.

**"Freight only matters for physical traders."** Freight rates affect the economics that drive physical flows, which in turn affect regional supply/demand balances and thus futures prices.

## Sources

- Baltic Exchange: Tanker Route Assessments and Baltic Dirty Tanker Index
- Clarkson Research: Shipping Intelligence Network
- Platts: Clean and Dirty Tanker Rate Assessments
