---
aliases: [floating storage, oil on water, tanker storage]
tags:
  - "#energy/crude"
date-added: "2026-03-20"
---

# Floating Storage

## Definition

Floating storage is storing crude or refined products on tankers at sea instead of in onshore tank farms. It happens when [[Contango]] in the curve is wide enough to cover chartering a tanker, insurance, and financing the oil for the storage duration. Traders buy oil at spot, store it on a ship, and simultaneously sell futures at the higher deferred price, locking in a profit. Floating storage builds during oversupply (2015 to 2016 glut, COVID 2020) and draws as markets tighten. AIS (Automatic Identification System) satellite data allows real time tanker tracking, making floating storage a high frequency supply indicator.

## Why it matters (commodities and FX)

Floating storage is both a symptom and an active strategy. A buildup signals that onshore tanks are filling and the market is in significant oversupply. When floating storage draws, it signals tightening. For physical houses, floating storage is a core profit center in contango: Vitol and Trafigura stored hundreds of millions of barrels during the 2020 crash. For financial traders, AIS tracking via Kpler and Vortexa provides a leading indicator of supply/demand changes before they appear in [[EIA Report]] or [[IEA]] statistics.

## Concrete example

**Concrete:** April 2020. WTI front month collapses to −$37/bbl while 6 month forward trades at $35/bbl, contango of over $70. A trading house charters a VLCC for 6 months at $50,000/day (~$0.15/bbl/day for 2M barrels). Total 6 month storage cost: ~$5.50/bbl (charter + insurance + financing at near zero rates). Trader buys physical at $10/bbl, sells the 6 month forward at $35, locking in $19.50/bbl profit after storage. If the contango had narrowed before execution, or counterparty risk materialized, profit shrinks or evaporates.

**Simplified:** When future oil prices are much higher than today's, you can make money by buying oil now, holding it, and delivering against the higher forward price. If onshore tanks are full, you put the oil on a ship at sea. As long as the price gap covers the cost of the ship plus insurance and financing, the trade prints. When the market tightens, that gap closes, the trade dies, and the ships come back to normal duty.

## Key mechanics and formulas

**Floating storage profit:** `Profit = Deferred Futures − Spot Price − (Charter Cost + Insurance + Financing)`

**Breakeven contango:** `Min Contango = Charter Rate ($/bbl/month) × Months + Insurance + Financing Rate × Oil Value × Time`

**Typical VLCC charter for storage:** $30,000 to $80,000/day depending on market conditions.

**Tracking data sources:**
- Kpler: real time floating storage estimates
- Vortexa: tanker tracking and storage analytics
- AIS data: vessel position monitoring

## Prerequisites

- [[Contango]]
- [[Cost of Carry]]
- [[Freight]]
- [[Forward Curve]]

## Related concepts (learn next)

- [[Contango]]: floating storage is only profitable in contango.
- [[Cost of Carry]]: the trade is bounded by the cost of carry relationship.
- [[Tank Tops]]: onshore storage filling forces oil onto tankers.
- [[Freight]]: tanker charter rates are the primary cost.
- [[Storage Economics]]: floating storage is one form of the broader storage trade.
- [[Backwardation]]: floating storage draws down as the curve flips to backwardation.

## Common misconceptions

**"Floating storage is wasteful."** It is a rational response to contango that performs the market function of balancing supply across time.

**"Floating storage is only relevant during crises."** Some always exists (oil in transit, slow steaming for logistics). Dedicated contango storage is the crisis signal.

**"AIS data gives exact floating storage numbers."** AIS requires interpretation: distinguishing storage from slow transit, ship to ship transfers, and port congestion is not trivial. Providers give different estimates.

## Sources

- Kpler: Floating Storage Methodology
- Vortexa: Tanker Analytics Platform
- IEA: Oil Market Report (floating storage estimates)
