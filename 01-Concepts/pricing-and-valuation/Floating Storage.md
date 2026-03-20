---
aliases: [floating storage, oil on water, tanker storage]
tags:
  - "#energy/crude"
date-added: "2026-03-20"
---

# Floating Storage

## Definition

Floating storage is the practice of storing crude oil or refined products on tankers at sea instead of in onshore tank farms. It occurs when the [[Contango]] in the futures curve is wide enough to cover the cost of chartering a tanker, insuring the cargo, and financing the oil for the storage duration. Traders buy oil at the current spot price, store it on a ship, and simultaneously sell futures at the higher deferred price, locking in a profit. Floating storage builds during periods of oversupply (2015 to 2016 oil glut, COVID 2020 crash) and draws down as markets tighten. AIS (Automatic Identification System) satellite data allows real time tracking of tanker positions, making floating storage a high frequency supply indicator.

## Why it matters (commodities and FX)

Floating storage is both a symptom of market conditions and an active trading strategy. A buildup of floating storage signals that onshore tanks are filling up and the market is in significant oversupply. When floating storage starts to draw, it signals tightening. For physical trading houses, floating storage is a core profit center during contango: firms like Vitol and Trafigura stored hundreds of millions of barrels during the 2020 crash. For financial traders, tracking floating storage through AIS data (Kpler, Vortexa) provides a leading indicator of supply/demand balance changes before they appear in official [[EIA Report]] or [[IEA]] statistics.

## Concrete example

In April 2020, WTI front month collapses to negative $37/bbl while the 6 month forward trades at $35/bbl, a contango of over $70. A trading house charters a VLCC for 6 months at $50,000/day (approximately $0.15/bbl/day for 2 million barrels). Total storage cost for 6 months: approximately $5.50/bbl (charter + insurance + financing at near zero rates). The trader buys physical crude at $10/bbl and sells the 6 month forward at $35, locking in a $19.50/bbl profit after storage costs. If the contango had narrowed before the trader could execute, or if counterparty risk materialized, the profit would shrink or evaporate.

## Key mechanics and formulas

**Floating storage profit:** `Profit = Deferred Futures - Spot Price - (Charter Cost + Insurance + Financing)`

**Breakeven contango:** `Minimum Contango = Charter Rate ($/bbl/month) × Months + Insurance + Financing Rate × Oil Value × Time`

**Typical VLCC charter for storage:** $30,000 to $80,000/day depending on market conditions.

**Data sources for tracking:**
- Kpler: real time floating storage estimates
- Vortexa: tanker tracking and storage analytics
- AIS data: vessel position monitoring

## Prerequisites

- [[Contango]]
- [[Cost of Carry]]
- [[Freight]]
- [[Forward Curve]]

## Related concepts (learn next)

- [[Contango]] because floating storage is only profitable in a contango market.
- [[Cost of Carry]] because the storage trade is bounded by the cost of carry relationship.
- [[Tank Tops]] because onshore storage filling up forces oil onto tankers.
- [[Freight]] because tanker charter rates are the primary cost of floating storage.
- [[Storage Economics]] because floating storage is one form of the broader storage trade.
- [[Backwardation]] because floating storage draws down as the curve shifts to backwardation.

## Common misconceptions

**"Floating storage is wasteful."** It is an economically rational response to contango that serves the market function of balancing supply across time.

**"Floating storage is only relevant during crises."** Some level of floating storage always exists (oil in transit, slow steaming for logistics optimization). Dedicated contango storage is the crisis signal.

**"AIS data gives you exact floating storage numbers."** AIS tracking involves interpretation: distinguishing storage from slow transit, ship to ship transfers, and port congestion is not trivial. Different data providers give different estimates.

## Sources

- Kpler: Floating Storage Methodology
- Vortexa: Tanker Analytics Platform
- IEA: Oil Market Report (floating storage estimates)
