---
aliases: [forward curve, term structure]
tags:
  - "#energy"
  - "#rates"
date-added: "2026-03-20"
---

# Forward Curve

## Definition

The set of futures prices across all available delivery dates for a single commodity or instrument, plotted with time on the x axis and price on the y axis. It shows what the market will pay for delivery at different forward dates.

## Why It Matters (Commodities / FX)

The forward curve is the market's pricing of time. Every [[Relative Value Trade|relative value trade]] in commodities bets on some aspect of the curve: level, slope, curvature, or shape. Reading the curve is the most fundamental skill in commodity trading.

## Prerequisites

- [[Futures Contract Mechanics]]

## Related Concepts (Learn Next)

- [[Contango]]
- [[Backwardation]]
- [[Cost of Carry Model]]
- [[Convenience Yield]]
- [[Calendar Spread]]
- [[Roll Yield]]
- [[Observation Date vs Forward Date]]

## Concrete example

### Freight forward curve

The freight forward curve is the strip of [[Forward Freight Agreement]] prices across delivery periods (front month, near months, quarters, and calendar years) for a route or basket such as Capesize C5 or the [[Baltic Exchange and the Dry Indices|Baltic 5TC]]. Like a commodity curve it can sit in [[Contango]] (deferred periods priced above the front, the market pricing a recovery in rates, common when spot is weak) or [[Backwardation]] (deferred below the front, spot tight and expected to ease).

**Concrete:** Capesize spot (the front month FFA) trades at 12,000 USD per day while the next calendar year averages 18,000, a contango of 6,000. An operator needing cover for next year buys the calendar FFA at 18,000 to lock cost. If spot recovers to 20,000 the lock looks cheap and the contango was justified. If spot stays at 12,000 all year the operator overpaid by 6,000 per day and the curve was too optimistic. Reading freight curve shape is the same skill as reading a commodity [[Forward Curve]], applied to a rate rather than a price, and it drives [[TC In and TC Out]] period decisions and [[Forward Freight Agreement|FFA]] hedging.

---
*Status: #stub | Last reviewed: 2026-03-20*
