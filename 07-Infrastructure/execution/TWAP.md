---
aliases: [TWAP, time weighted average price]
tags:
  - "#execution"
date-added: "2026-03-20"
---

# TWAP

## Definition

TWAP (Time Weighted Average Price) is an execution strategy that splits a large order into equal sized child orders executed at regular intervals, regardless of market volume. Unlike [[VWAP]] (which weights by volume), TWAP distributes orders uniformly across time. The benchmark price is the arithmetic average of prices over the window. TWAP is simpler, more predictable, and harder to game than VWAP.

## Why it matters (commodities and FX)

TWAP is preferred in commodity markets when (1) volume is unpredictable or lumpy (many commodity contracts have less regular volume than equities), (2) you want to avoid clustering with VWAP users at the same execution times, (3) you want to minimize information leakage. For FX, TWAP is extremely common because FX is a 24 hour market with no single volume profile and no centralized volume data.

## Concrete example

**Concrete:** You need to buy 200 [[Brent Crude]] contracts over a 2 hour window (10:00 to 12:00). TWAP with 5 minute intervals = 24 slices, roughly 8.3 contracts per slice (round to 8 or 9 alternating). Every 5 minutes, the algo places a limit order for 8 to 9 contracts inside the [[Bid-Ask Spread]] or at mid. If not filled within the interval, the order goes more aggressive or carries to the next interval. Average mid over the 2 hours: $78.50. Achieved: $78.53. TWAP shortfall: $0.03/bbl ($30/contract, $6,000 on 200 contracts).

**Simplified:** Chop the parent order into equal slices and feed one slice per fixed time bucket. Ignore volume entirely. If you need to buy 200 lots over 2 hours, that means 100 lots/hour, regardless of how much the market trades. Simple, predictable, hard to game.

## Key mechanics and formulas

**TWAP benchmark:**
`TWAP = (1/N) x Σ P_i`

Simple arithmetic average of N price observations over the window.

**Child order size:**
`Child Size = Total Order / Number of Intervals`

**Interval selection:**
Shorter intervals (1 minute) = smoother execution, more orders, higher commission.
Longer intervals (15 minutes) = fewer orders, more timing risk per slice.
Typical: 1 to 5 minute intervals for liquid commodity futures.

**TWAP vs VWAP tradeoff:**

| Feature | TWAP | VWAP |
|---------|------|------|
| Volume awareness | None | Yes |
| Predictability to others | Lower | Higher |
| Implementation complexity | Simple | Requires volume forecast |
| Best for | Thin/unpredictable volume | Liquid/predictable volume |
| Information leakage | Lower | Higher |

## Prerequisites
- [[Liquidity]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[VWAP]] - the volume weighted alternative.
- [[Execution Algorithms]] - TWAP and VWAP are passive. Aggressive algos (IS, POV) exist for time sensitive orders.
- [[Market Impact]] - TWAP spreads impact over time but does not adapt to conditions.
- [[Slippage]] - TWAP minimizes average slippage but underperforms in trending markets (buying evenly as price rises).

## Common misconceptions

**"TWAP is always worse than VWAP."** When volume forecasts are unreliable or execution predictability matters, TWAP wins. Simplicity has value.

**"TWAP eliminates market impact."** It spreads impact over time but does not eliminate it. If your order is large relative to average volume, even flat distribution pushes price.

**"TWAP is only for unsophisticated traders."** Many sophisticated desks use TWAP because it is harder to reverse engineer. Unpredictability is an edge.

## Sources

- Kissell, "The Science of Algorithmic Trading and Portfolio Management" (2013)
- Almgren, "Optimal Trading in a Dynamic Market" (2012)
