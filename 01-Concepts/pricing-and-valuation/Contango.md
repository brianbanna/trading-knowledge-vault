---
aliases: [contango market]
tags:
  - "#energy/crude"
  - "#energy/natgas"
date-added: "2026-03-20"
---

# Contango

## Definition

A market condition where futures prices for later delivery dates are higher than nearer delivery dates. The forward curve slopes upward. This is the "normal" state for most commodity markets because it reflects storage costs, insurance, and financing costs (the [[Cost of Carry Model|cost of carry]]).

## Why It Matters (Commodities / FX)

Understanding contango is essential for any commodity trader because it determines whether holding a long futures position bleeds money over time (negative [[Roll Yield]]) or earns it. In contango, rolling a long position forward means selling the expiring contract at a lower price and buying the next one at a higher price, creating a drag on returns.

## Concrete Example

If WTI crude June 2026 trades at $72 and July 2026 trades at $73, the market is in contango by $1. A trader rolling a long position from June to July loses $1 per barrel (before any spot price movement).

## Prerequisites

- [[Futures Contract Mechanics]]
- [[Forward Curve]]

## Related Concepts (Learn Next)

- [[Backwardation]]
- [[Roll Yield]]
- [[Cost of Carry Model]]
- [[Convenience Yield]]
- [[Calendar Spread]]
- [[Relative Value Trade]]

## Key Mechanics / Formulas

Theoretical contango: `F(t,T) = S(t) x e^((r + c - y)(T-t))`

Where: F = futures price, S = spot price, r = risk free rate, c = storage cost rate, y = convenience yield, T-t = time to delivery.

When `r + c > y`, the market is in contango.

## Common Misconceptions

**"Contango means the market expects prices to rise."** Not necessarily. Contango primarily reflects storage and financing costs, not directional expectations. A market can be in contango while spot prices are falling.

**"Contango is always bad for longs."** Only for passive long holders who must roll. An active trader can exploit contango through [[Relative Value Trade|calendar spreads]] or by timing rolls.

## Sources

- CME Group: Understanding Contango and Backwardation

## Course Module Mapping

- Module 2.3 (Futures and Forwards)
- Module 19.1 (Commodity Market Structure)

---
*Status: #stub | Last reviewed: 2026-03-20*
