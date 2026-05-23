---
aliases: [contango market]
tags:
  - "#energy/crude"
  - "#energy/natgas"
date-added: "2026-03-20"
---

# Contango

## Definition

A market condition where futures for later delivery trade above nearer delivery. The forward curve slopes upward. The "normal" state for most commodities because it reflects storage, insurance, and financing costs (the [[Cost of Carry Model|cost of carry]]).

## Why It Matters (Commodities / FX)

Contango determines whether a long futures position bleeds money over time (negative [[Roll Yield]]) or earns it. In contango, rolling a long position means selling the expiring contract at a lower price and buying the next at a higher price, dragging on returns.

## Concrete Example

WTI crude June 2026 at $72, July 2026 at $73: contango of $1. Rolling long June to July costs $1/bbl before any spot move.

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

Theoretical contango: `F(t,T) = S(t) × e^((r + c − y)(T−t))`

Where: F = futures price, S = spot price, r = risk free rate, c = storage cost rate, y = convenience yield, T−t = time to delivery.

When `r + c > y`, the market is in contango.

## Common Misconceptions

**"Contango means the market expects prices to rise."** Not necessarily. Contango primarily reflects storage and financing costs, not direction. A market can be in contango while spot falls.

**"Contango is always bad for longs."** Only for passive holders who must roll. Active traders exploit contango through [[Relative Value Trade|calendar spreads]] or by timing rolls.

## Sources

- CME Group: Understanding Contango and Backwardation

## Course Module Mapping

- Module 2.3 (Futures and Forwards)
- Module 19.1 (Commodity Market Structure)

---
*Status: #stub | Last reviewed: 2026-03-20*
