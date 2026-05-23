---
aliases: [VWAP, volume weighted average price]
tags:
  - "#execution"
date-added: "2026-03-20"
---

# VWAP

## Definition

VWAP (Volume Weighted Average Price) is the average price of an instrument over a period, weighted by volume traded at each price level. It is the "fair" average a passive participant would achieve by trading proportionally with all volume in the window. VWAP is both an execution benchmark (did you buy above or below VWAP?) and an algorithm (execute at or near VWAP by spreading orders across time proportional to expected volume).

## Why it matters (commodities and FX)

VWAP is the standard execution benchmark for institutional commodity traders. When a PM decides to buy 500 WTI contracts, the desk is judged on whether they achieved a price at or below VWAP for the window. Beating VWAP adds value. Missing it costs alpha. For a trader building a [[Calendar Spread]] or [[Relative Value Trade]], executing both legs near VWAP cuts [[Slippage]] and ensures entry reflects fair market levels rather than timing noise.

## Concrete example

**Concrete:** [[WTI Crude Oil]] from 09:00 to 10:00 CT:

| Time | Price | Volume |
|------|-------|--------|
| 09:00 to 09:15 | $74.20 | 8,000 |
| 09:15 to 09:30 | $74.35 | 12,000 |
| 09:30 to 09:45 | $74.50 | 15,000 |
| 09:45 to 10:00 | $74.30 | 10,000 |

VWAP = (74.20 x 8,000 + 74.35 x 12,000 + 74.50 x 15,000 + 74.30 x 10,000) / 45,000 = 3,346,300 / 45,000 = $74.36. Buying the full order at $74.42 misses VWAP by $0.06/bbl ($60/contract). On 500 contracts, that is $30,000 of shortfall.

**Simplified:** Take the average price over a window, but weight each price by how much actually traded there. If most of the volume happened at $74.50, VWAP is close to $74.50 even if prices ranged from $74.20 to $74.50. Then compare your fills to that number. Beat it, you did better than the average market participant.

## Key mechanics and formulas

**VWAP calculation:**
`VWAP = Σ(P_i x V_i) / Σ(V_i)`

Where P_i = price at time i, V_i = volume at time i.

**VWAP execution algorithm logic:**
1. Estimate the volume profile for the window (typically U shaped, higher at open and close)
2. Slice the parent order proportional to expected volume per bucket
3. Execute children passively (limits) or with minimal aggression to limit [[Market Impact]]
4. Track actual vs expected volume and adjust pace if needed

**Execution shortfall vs VWAP:**
`Shortfall = Execution Price - VWAP` (for buys; reverse for sells)
Negative = beat VWAP (good). Positive = missed (bad).

**Participation rate:**
`Participation = Your Volume / Total Market Volume`

VWAP algos target 5 to 20% participation. Higher = more [[Market Impact]]. Lower = slower, more timing risk.

## Prerequisites
- [[Liquidity]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[TWAP]] - time weighted alternative when volume profile dictation is unwanted.
- [[Execution Algorithms]] - VWAP is one of many. Understand when to choose VWAP vs TWAP vs IS vs iceberg.
- [[Market Impact]] - VWAP algos minimize impact by spreading orders over time.
- [[Slippage]] - VWAP benchmarking is a way to measure it.
- [[Liquidity]] - VWAP works best in liquid markets with predictable volume. In thin markets it can be gamed.

## Common misconceptions

**"Achieving VWAP means good execution."** VWAP is a passive benchmark. With information (expecting price to rise), execute FASTER than VWAP to capture alpha. Matching VWAP is fine for uninformed flow, suboptimal for informed.

**"VWAP is always a better benchmark than TWAP."** In unpredictable volume markets (some commodity futures), VWAP forecasts go wrong, causing over or under execution. TWAP ignores volume and avoids the problem.

**"VWAP algos cannot be gamed."** Sophisticated participants predict VWAP behavior (volume profiles are somewhat predictable) and front run the expected flow. Large orders sometimes use IS algos or randomized execution instead.

## Sources

- Kissell, Robert, "The Science of Algorithmic Trading and Portfolio Management" (2013)
- CME Group: execution benchmarking documentation
- Almgren and Chriss, "Optimal Execution of Portfolio Transactions" (2000)
