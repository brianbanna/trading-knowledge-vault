---
aliases: [partial execution, partial fill, partial order fill]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Partial Fill

## Definition

A partial fill occurs when only a portion of an order gets executed, leaving the remainder still working in the market. If a trader places a [[Limit Order]] to buy 50 lots of [[Brent Crude]] at $82.50, and only 20 lots are available at that price, they receive a partial fill of 20 lots. The remaining 30 lots stay as an open order until filled, cancelled, or expired. Partial fills are common in all markets and are a fundamental reality of order management.

## Why it matters (commodities and FX)

Partial fills create operational complexity. A desk expecting to be fully hedged after an order may only be partially covered, leaving residual [[Inventory Risk]]. In FX, partial fills across multiple venues can leave a trader with scattered small positions that are expensive to close. In commodity futures with limited [[Depth of Book|depth]] (e.g., far dated contracts), partial fills are the norm rather than the exception, and execution strategies must account for this.

## Concrete example

An FX desk needs to buy 100 million [[EUR USD]] and places a [[Limit Order]] at 1.08500 on EBS.

**Success case:** Liquidity is good. The order fills in 3 tranches over 4 seconds: 40M, 35M, 25M, all at 1.08500. Full fill achieved at the target price.

**Failure case:** The market is thin. Only 15M fills at 1.08500. The price moves to 1.08510 and the remaining 85M sits unfilled. The desk must decide: raise the limit (accept worse price), wait (risk further adverse movement), or cancel and use a [[Market Order]] (accept [[Slippage]]). While deliberating, the price moves to 1.08525, and the delay has cost $21,250 on the remaining 85M.

**[[FOK]] alternative:** If the desk had used a Fill or Kill order for the full 100M, the 15M partial would have been rejected entirely. No fill, but no dangling partial position either.

## Key mechanics and formulas

**Fill ratio** = filled quantity / total order quantity

Example: 20 lots filled out of 50 = 40% fill ratio

**Residual risk** = (total order minus filled quantity) * price exposure per unit

Example: If 85M EUR unfilled and market moves 25 pips adverse = 85M * 0.0025 = $212,500 potential cost

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

- [[FOK]] for the all or nothing alternative that avoids partial fills
- [[IOC]] for the "fill what you can, cancel rest" approach
- [[Depth of Book]] for understanding why partial fills happen (insufficient size at price level)
- [[Slippage]] for the cost of chasing a fill after a partial
- [[Smart Order Routing]] for spreading orders across venues to maximize fill rates
- [[VWAP]] for an algo that manages partial fills systematically over time

## Common misconceptions

1. **"Partial fills only happen in illiquid markets."** Even [[EUR USD]], the most liquid instrument in the world, produces partial fills regularly during volatile moments or for large orders.

2. **"I should always chase the remaining fill."** Sometimes the market has moved for a reason. Chasing can lead to worse average prices than waiting or accepting the partial position.

3. **"Partial fills are free."** Each partial fill may incur a separate commission or clearing fee depending on the venue. 10 partial fills of 5 lots each can cost more in fees than 1 fill of 50 lots.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- Johnson, Barry, "Algorithmic Trading and DMA," 4Myeloma Press
