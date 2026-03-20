---
aliases: [time spread, front-back spread]
tags:
  - "#energy/crude"
date-added: "2026-03-20"
---

# Time Spread

## Definition

A time spread (also called a [[Calendar Spread]]) is the price difference between two futures contracts of the same commodity with different delivery months. Typically expressed as the near month minus the deferred month: a positive time spread means [[Backwardation]] (front above back), and a negative time spread means [[Contango]] (front below back). The time spread is the most liquid spread in oil markets, with tighter bid/ask spreads than outright futures, because both legs share most of the same fundamental drivers (quality, location) and differ only in timing. It is the purest expression of curve shape and the market's view on near term vs deferred supply/demand balance.

## Why it matters (commodities and FX)

Time spreads are where most professional oil trading happens. Outright futures carry directional risk to broad market moves, but time spreads isolate the term structure signal. A trader who believes near term supply is tightening but is uncertain about flat price direction can go long the time spread (buy front, sell back) to express that view with lower margin and lower volatility. Time spreads also drive [[Roll Yield]] for investors and ETFs. The Brent M1 to M6 time spread is one of the most watched indicators of market health in energy.

## Concrete example

Brent June trades at $82/bbl and Brent December trades at $78/bbl. The Jun/Dec time spread is +$4 (backwardation). A trader expects an [[OPEC+]] cut to tighten the near term market further. She goes long the Jun/Dec spread at $4. If near term tightness intensifies (Cushing stocks draw, OPEC compliance improves), the spread widens to $7, earning $3/bbl. If OPEC overproduces and the near term loosens, the spread could flip to $1 or even into contango, losing $3 or more.

## Key mechanics and formulas

**Time spread:** `Time Spread = Front Month Price - Deferred Month Price`

**Key oil time spreads:**
- Brent M1/M2 (1 month spread): most liquid, signals immediate tightness
- Brent M1/M6 (6 month spread): benchmark for curve shape
- WTI Dec/Dec: annual spread, reflects structural balance expectations

**Margin advantage:** Time spread margins are typically 20 to 40% of outright margin because the two legs partially offset.

## Prerequisites

- [[Calendar Spread]]
- [[Contango]]
- [[Backwardation]]
- [[Forward Curve]]

## Related concepts (learn next)

- [[Calendar Spread]] because time spread and calendar spread are effectively synonymous.
- [[Backwardation]] because positive time spreads define a backwardated market.
- [[Contango]] because negative time spreads define a contango market.
- [[Roll Yield]] because time spreads determine the gain or cost of rolling futures positions.
- [[Convenience Yield]] because near term supply tightness drives positive time spreads.
- [[EIA Report]] because weekly inventory data is the primary short term driver of time spreads.
- [[Cost of Carry]] because time spreads in contango are bounded by carry costs.

## Common misconceptions

**"Time spreads are low risk."** While lower risk than outright, time spreads can move sharply. The Brent M1/M6 spread has moved $10+ in a single month during supply shocks.

**"Time spreads only reflect fundamentals."** Positioning, ETF roll schedules, and options expiry hedging flows all affect time spreads independently of physical supply/demand.

**"Front month time spreads are the most important."** For longer term positioning, the 12 month or Dec/Dec spreads may be more informative about structural market balance than the volatile front month.

## Sources

- CME Group: Calendar Spread Trading in Crude Oil
- ICE: Brent Crude Oil Spread Trading Guide
- Commodity Trading Manual, Chicago Board of Trade
