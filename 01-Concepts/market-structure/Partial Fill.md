---
aliases: [partial execution, partial fill, partial order fill]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Partial Fill

## Definition

A partial fill is when only part of an order executes, leaving the remainder working. A [[Limit Order]] to buy 50 lots of [[Brent Crude]] at $82.50 with only 20 lots available at that price gives a 20 lot partial. The remaining 30 lots stay open until filled, cancelled, or expired. Partial fills are common across all markets and a fundamental reality of order management.

## Why it matters (commodities and FX)

Partial fills create operational complexity. A desk expecting full hedge after an order may be partially covered, leaving residual [[Inventory Risk]]. In FX, partials across multiple venues leave scattered small positions expensive to close. In commodity futures with limited [[Depth of Book|depth]] (far dated contracts), partial fills are the norm rather than exception, and execution strategies must account for this.

## Concrete example

**Concrete:** An FX desk needs 100M [[EUR USD]] and posts a [[Limit Order]] at 1.08500 on EBS. Liquid scenario: the order fills in 3 tranches over 4 seconds: 40M, 35M, 25M, all at 1.08500. Full fill at target. Thin scenario: only 15M fills at 1.08500. Price ticks to 1.08510, the remaining 85M sits unfilled. The desk must raise the limit (worse price), wait (more adverse risk), or cancel and use a [[Market Order]] ([[Slippage]]). While deliberating, the price moves to 1.08525, costing $21,250 on the residual. Had the desk used [[FOK]] for the full 100M, the 15M partial would have been rejected entirely. No fill, but no dangling position.

**Simplified:** You ask for 100, the market gives you 30. The other 70 sits waiting. Now you have a half hedge, the market moved, and you have to choose: chase, wait, or cancel. Each choice has a cost. Partial fills are not free; they are an unfinished trade with a decision attached.

## Key mechanics and formulas

**Fill ratio** = filled quantity / total order quantity

Example: 20 of 50 = 40% fill ratio.

**Residual risk** = (total order minus filled) × price exposure per unit

Example: 85M EUR unfilled, market moves 25 pips adverse = 85M × 0.0025 = $212,500 potential cost.

**Order types and partial fill behavior:**

| Order type | Partial fill? |
|-----------|---------------|
| [[Market Order]] | Fills everything, may sweep levels |
| [[Limit Order]] | Yes, common |
| [[IOC]] | Fills what it can, cancels rest |
| [[FOK]] | No. All or nothing. |

## Prerequisites

- [[Limit Order]]
- [[Fill]]
- [[Depth of Book]]

## Related concepts (learn next)

- [[FOK]] for the all or nothing alternative avoiding partials
- [[IOC]] for "fill what you can, cancel rest"
- [[Depth of Book]] for why partials happen (insufficient size at price level)
- [[Slippage]] for the cost of chasing a fill after a partial
- [[Smart Order Routing]] for spreading across venues to maximize fill rate
- [[VWAP]] for an algo managing partials systematically over time

## Common misconceptions

1. **"Partials only happen in illiquid markets."** Even [[EUR USD]], the most liquid instrument in the world, produces partials regularly during volatile moments or for large orders.

2. **"I should always chase the remaining fill."** Sometimes the market moved for a reason. Chasing leads to worse average prices than waiting or accepting the partial.

3. **"Partials are free."** Each partial may incur a separate commission or clearing fee. 10 partials of 5 lots each cost more in fees than 1 fill of 50 lots.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- Johnson, Barry, "Algorithmic Trading and DMA," 4Myeloma Press
