---
aliases: [tanker freight, shipping cost, VLCC rate, worldscale]
tags:
  - "#energy/crude"
  - "#macro"
date-added: "2026-03-20"
---

# Freight

## Definition

Freight in commodity markets is the cost of shipping physical commodities (primarily crude and refined products) by sea. Tanker rates are set by vessel supply, cargo demand, route length, and port congestion. Quoted in Worldscale (WS, a percentage of a reference flat rate per route) or in $/bbl or $/tonne. Vessel sizes range from Handysize (~30,000 DWT) to VLCC (~300,000 DWT). Freight is the gating variable in commodity arbitrage: it determines whether moving oil between regions is economic.

## Why it matters (commodities and FX)

Freight is the gatekeeper for trade flow arbitrage. A Brent/Dubai [[EFS]] spread of $3/bbl is only profitable if North Sea to Asia freight is below $3/bbl. When freight spikes (geopolitical events, fleet shortages, seasonal demand), arbitrage windows close even when commodity spreads look attractive. Freight spikes move commodity prices: when Houthi attacks disrupted Red Sea shipping in 2024, tanker rates doubled and oil prices rose because effective delivered cost increased. Shipping equities and freight derivatives (FFAs) provide additional cross asset trades.

## Concrete example

**Concrete:** Trader identifies a WTI to China arb. WTI at US Gulf Coast is $78/bbl. Equivalent landed in Shandong is $84/bbl. Spread $6/bbl. VLCC freight USG to China is $4.50/bbl plus insurance and port costs of $0.50, totaling $5.00/bbl in transport. Net margin $1.00/bbl on a 2M barrel VLCC = $2M. If freight spikes to $7/bbl (seasonal tanker demand or fleet disruption), the arb flips negative and the cargo is uneconomic. The trader must lock in freight before committing to the cargo.

**Simplified:** Freight is what you pay a ship to move oil from one place to another. If oil is cheaper in one region than another by more than the cost to ship it, you can buy in the cheap region and sell in the expensive one. When ships become scarce or geopolitical risk spikes, freight rises fast and those arbs disappear. The freight market is among the most volatile inputs in commodity trading and shapes the geography of crude flows.

## Key mechanics and formulas

**Quoting conventions:**
- Worldscale (WS): percentage of a reference flat rate. WS100 = full reference. WS50 = half.
- Time charter equivalent (TCE): daily revenue in $/day after voyage costs.
- Dollars per barrel: most intuitive for oil traders.

**Vessel sizes:**
- VLCC: ~2M barrels, long haul (Middle East to Asia, US Gulf to China)
- Suezmax: ~1M barrels, medium routes (West Africa to Europe)
- Aframax: ~600,000 barrels, short routes (North Sea, Caribbean)

**Arbitrage condition:** `Commodity Spread > Freight + Insurance + Port Costs`

## Prerequisites

- [[Brent Crude]]
- [[EFS]]
- [[Location Arbitrage]]

## Related concepts (learn next)

- [[EFS]]: freight determines whether East/West crude arbs are profitable.
- [[Location Arbitrage]]: freight is the cost component that makes or breaks location arbs.
- [[Floating Storage]]: tankers are used for storage when contango exceeds freight plus storage costs.
- [[Chokepoint]]: chokepoint disruptions create freight spikes and rerouting costs.
- [[Contango]]: contango width relative to freight determines storage trade viability.
- [[Dubai Crude]]: Asian crude pricing is heavily influenced by freight dynamics.
- [[Freight Rate Risk]]: the risk view of freight exposure, who is long or short it and how to hedge.
- [[Time Charter Equivalent]]: converts a voyage rate into a daily figure comparable to a time charter hire.

## Common misconceptions

**"Freight is small and can be ignored."** On long haul routes, freight runs $3 to $8/bbl, significant vs typical inter basin spreads of $2 to $6.

**"Freight rates are stable."** Among the most volatile prices in commodities. VLCC rates can double in a week during supply disruptions.

**"Freight only matters for physical traders."** Freight affects physical flows, which set regional supply/demand and feed into futures prices.

## Sources

- Baltic Exchange: Tanker Route Assessments and Baltic Dirty Tanker Index
- Clarkson Research: Shipping Intelligence Network
- Platts: Clean and Dirty Tanker Rate Assessments
