---
aliases: [TWAP, time weighted average price]
tags:
  - "#execution"
date-added: "2026-03-20"
---

# TWAP

## Definition

TWAP (Time Weighted Average Price) is an execution strategy that splits a large order into equal sized child orders executed at regular time intervals over a specified period, regardless of market volume. Unlike [[VWAP]] (which weights execution by volume), TWAP distributes orders uniformly across time. The resulting benchmark price is simply the arithmetic average of prices over the execution window. TWAP is simpler, more predictable, and harder to game than VWAP.

## Why it matters (commodities and FX)

TWAP is preferred in commodity markets when: (1) the volume profile is unpredictable or lumpy (many commodity contracts have less regular volume patterns than equities), (2) you want to avoid being clustered around the same execution times as other participants using VWAP, (3) you want to minimize information leakage (TWAP behavior is less predictable to observers). For FX execution, TWAP is extremely common because FX is a 24 hour market with no single "volume profile" and no centralized volume data.

## Concrete example

You need to buy 200 [[Brent Crude]] contracts over a 2 hour window (10:00 to 12:00). TWAP with 5 minute intervals = 24 slices = ~8.3 contracts per slice (round to 8 or 9, alternating).

Every 5 minutes, the algo places a limit order for 8 to 9 contracts slightly inside the [[Bid-Ask Spread]] or at the midpoint. If the order does not fill within the interval, it can be made more aggressive or carried to the next interval. The execution price will approximate the arithmetic average of the mid price sampled every 5 minutes.

If the average mid price over the 2 hours was $78.50 and you achieved $78.53, the TWAP shortfall is $0.03/bbl ($30/contract, $6,000 on 200 contracts).

## Key mechanics and formulas

**TWAP benchmark:**
`TWAP = (1/N) x Σ P_i`

Simple arithmetic average of N price observations over the execution window.

**Child order size:**
`Child Size = Total Order / Number of Intervals`

**Interval selection:**
Shorter intervals (1 minute) = smoother execution but more individual orders, higher commission cost.
Longer intervals (15 minutes) = fewer orders but more timing risk per slice.
Typical: 1 to 5 minute intervals for liquid commodity futures.

**TWAP vs VWAP trade-off:**

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
- [[VWAP]] - the volume weighted alternative. Understanding when to choose TWAP vs VWAP.
- [[Execution Algorithms]] - TWAP and VWAP are passive algos. More aggressive algos (IS, POV) exist for time sensitive orders.
- [[Market Impact]] - TWAP spreads impact over time but does not adapt to market conditions.
- [[Slippage]] - TWAP minimizes average slippage but can underperform if the market trends during execution (buying evenly as price rises steadily).

## Common misconceptions

**"TWAP is always worse than VWAP."** In markets with unreliable volume forecasts or when execution predictability is a concern, TWAP outperforms VWAP. Simplicity has value.

**"TWAP eliminates market impact."** It spreads impact over time but does not eliminate it. If your total order is large relative to average volume, even evenly distributed flow will push the price.

**"TWAP is only for unsophisticated traders."** Many sophisticated desks use TWAP specifically because it is harder to reverse engineer and game. Unpredictability is an edge in execution.

## Sources

- Kissell, "The Science of Algorithmic Trading and Portfolio Management" (2013)
- Almgren, "Optimal Trading in a Dynamic Market" (2012)
