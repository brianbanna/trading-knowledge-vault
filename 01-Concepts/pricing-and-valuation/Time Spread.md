---
aliases: [time spread, front-back spread]
tags:
  - "#energy/crude"
date-added: "2026-03-20"
---

# Time Spread

## Definition

A time spread (also [[Calendar Spread]]) is the price difference between 2 futures contracts of the same commodity in different delivery months. Expressed as near month minus deferred: positive = [[Backwardation]] (front above back), negative = [[Contango]] (front below back). The time spread is the most liquid spread in oil markets, with tighter bid/ask than outright futures, because both legs share most fundamental drivers (quality, location) and differ only in timing. Purest expression of curve shape and near term versus deferred supply/demand balance.

## Why it matters (commodities and FX)

Time spreads are where most professional oil trading happens. Outright futures carry directional risk to broad moves; time spreads isolate the term structure signal. A trader who believes near term supply is tightening but is uncertain about flat price can go long the time spread (buy front, sell back) with lower margin and lower volatility. Time spreads drive [[Roll Yield]] for investors and ETFs. The Brent M1 to M6 time spread is 1 of the most watched energy market indicators.

## Concrete example

**Concrete:** Brent June at $82/bbl, Brent December at $78/bbl. Jun/Dec time spread at +$4 (backwardation). Trader expects an [[OPEC+]] cut to tighten near term, goes long the Jun/Dec spread at $4. Cushing draws and OPEC compliance improves, spread widens to $7, earning $3/bbl on 100 lots = $300,000. If OPEC overproduces and near term loosens, spread could flip to $1 or into contango, losing $3+/bbl.

**Simplified:** Same commodity, 2 different months. The price gap moves based on whether the near term is tight or loose relative to the future. If supply is squeezed today, the front month rallies more than the back, the gap widens. If the squeeze eases, the gap shrinks. Trading the gap is cleaner than betting on whether oil itself rallies, because you do not care about the level, only the relationship.

## Key mechanics and formulas

**Time spread:** `Time Spread = Front Month Price - Deferred Month Price`

**Key oil time spreads:**
- Brent M1/M2 (1 month spread): most liquid, signals immediate tightness
- Brent M1/M6 (6 month spread): benchmark for curve shape
- WTI Dec/Dec: annual spread, reflects structural balance expectations

**Margin advantage:** Time spread margin is 20 to 40% of outright margin because the 2 legs partially offset.

## Prerequisites

- [[Calendar Spread]]
- [[Contango]]
- [[Backwardation]]
- [[Forward Curve]]

## Related concepts (learn next)

- [[Calendar Spread]] because time spread and calendar spread are synonymous.
- [[Backwardation]] because positive time spreads define a backwardated market.
- [[Contango]] because negative time spreads define a contango market.
- [[Roll Yield]] because time spreads determine the gain or cost of rolling.
- [[Convenience Yield]] because near term supply tightness drives positive time spreads.
- [[EIA Report]] because weekly inventory data is the primary short term driver.
- [[Cost of Carry]] because time spreads in contango are bounded by carry costs.

## Common misconceptions

**"Time spreads are low risk."** Lower risk than outright, but they move sharply. Brent M1/M6 has moved $10+ in a single month during supply shocks.

**"Time spreads only reflect fundamentals."** Positioning, ETF roll schedules, and options expiry hedging all affect time spreads independently of physical balance.

**"Front month time spreads are the most important."** For longer term positioning, 12 month or Dec/Dec spreads are more informative about structural balance than the volatile front.

## Sources

- CME Group: Calendar Spread Trading in Crude Oil
- ICE: Brent Crude Oil Spread Trading Guide
- Commodity Trading Manual, Chicago Board of Trade
