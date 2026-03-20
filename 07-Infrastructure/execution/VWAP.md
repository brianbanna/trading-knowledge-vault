---
aliases: [VWAP, volume weighted average price]
tags:
  - "#execution"
date-added: "2026-03-20"
---

# VWAP

## Definition

VWAP (Volume Weighted Average Price) is the average price of an instrument over a given period, weighted by volume traded at each price level. It represents the "fair" average price that a passive market participant would have achieved by participating proportionally in all volume throughout the period. VWAP is both a benchmark for execution quality (did you buy above or below VWAP?) and an execution strategy (algorithms that aim to execute at or near VWAP by spreading orders across time proportional to expected volume).

## Why it matters (commodities and FX)

VWAP is the most common execution benchmark for institutional commodity traders. When a portfolio manager decides to buy 500 WTI contracts, the execution desk is judged on whether they achieve a price at or below the VWAP for the execution window. Beating VWAP means execution added value. Missing VWAP means execution cost alpha. For a trader building a [[Calendar Spread]] or [[Relative Value Trade]], executing both legs near VWAP reduces [[Slippage]] and ensures the spread entry price reflects fair market levels rather than timing noise.

## Concrete example

[[WTI Crude Oil]] from 09:00 to 10:00 CT:

| Time | Price | Volume (contracts) |
|------|-------|--------------------|
| 09:00 to 09:15 | $74.20 | 8,000 |
| 09:15 to 09:30 | $74.35 | 12,000 |
| 09:30 to 09:45 | $74.50 | 15,000 |
| 09:45 to 10:00 | $74.30 | 10,000 |

VWAP = (74.20 x 8,000 + 74.35 x 12,000 + 74.50 x 15,000 + 74.30 x 10,000) / (8,000 + 12,000 + 15,000 + 10,000)
= (593,600 + 892,200 + 1,117,500 + 743,000) / 45,000
= 3,346,300 / 45,000
= $74.36

If you bought your entire order at $74.42, you missed VWAP by $0.06 per barrel ($60 per contract). On 500 contracts, that is $30,000 of execution shortfall.

## Key mechanics and formulas

**VWAP calculation:**
`VWAP = Σ(P_i x V_i) / Σ(V_i)`

Where P_i = price at time i, V_i = volume at time i.

**VWAP execution algorithm logic:**
1. Estimate the volume profile for the execution window (how volume distributes over time, typically U-shaped: higher at open and close)
2. Slice the parent order into child orders proportional to expected volume in each time bucket
3. Execute child orders passively (limit orders) or with minimal aggression to avoid [[Market Impact]]
4. Track actual vs expected volume and adjust pace if actual volume deviates from forecast

**Execution shortfall vs VWAP:**
`Shortfall = Execution Price - VWAP` (for buys; reverse for sells)
Negative shortfall = you beat VWAP (good). Positive = you missed (bad).

**Participation rate:**
`Participation = Your Volume / Total Market Volume`

VWAP algos typically target 5 to 20% participation rate. Higher participation = more [[Market Impact]]. Lower = slower execution, more timing risk.

## Prerequisites
- [[Liquidity]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[TWAP]] - time weighted alternative. TWAP distributes orders evenly over time regardless of volume, useful when you do not want volume profile to dictate execution.
- [[Execution Algorithms]] - VWAP is one of many algo types. Understanding when to use VWAP vs TWAP vs IS (Implementation Shortfall) vs iceberg.
- [[Market Impact]] - VWAP algos aim to minimize market impact by spreading orders over time.
- [[Slippage]] - the cost of execution relative to the intended price. VWAP benchmarking is a way to measure slippage.
- [[Liquidity]] - VWAP works best in liquid markets with predictable volume profiles. In thin markets, VWAP can be gamed.

## Common misconceptions

**"Achieving VWAP means good execution."** VWAP is a passive benchmark. If you have information (you expect the price to rise), you should execute FASTER than VWAP to capture the alpha. Matching VWAP is good for uninformed flow but suboptimal for informed flow.

**"VWAP is always a better benchmark than TWAP."** In markets with unpredictable volume (some commodity futures), VWAP forecasts can be wrong, causing the algo to over or under execute. TWAP avoids this problem by ignoring volume entirely.

**"VWAP algos cannot be gamed."** Sophisticated participants can predict VWAP algo behavior (because volume profiles are somewhat predictable) and front run the expected flow. This is why large orders sometimes use IS algos or randomized execution instead.

## Sources

- Kissell, Robert, "The Science of Algorithmic Trading and Portfolio Management" (2013)
- CME Group: execution benchmarking documentation
- Almgren and Chriss, "Optimal Execution of Portfolio Transactions" (2000)
