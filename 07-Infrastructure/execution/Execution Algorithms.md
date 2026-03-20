---
aliases: [execution algorithms, execution algos, algo execution, algorithmic execution, child orders]
tags:
  - "#execution"
date-added: "2026-03-20"
---

# Execution Algorithms

## Definition

Execution algorithms are automated systems that break large parent orders into smaller child orders and execute them over time according to a specified strategy, minimizing [[Market Impact]] and [[Slippage]]. They are the bridge between a trading decision ("buy 500 WTI contracts") and the market microstructure reality (you cannot buy 500 contracts at once without moving the price). The main algo families are: benchmark algos ([[VWAP]], [[TWAP]]), aggressive algos (Implementation Shortfall, which front loads execution to reduce timing risk), and passive algos (iceberg, peg, sniper, which wait for favorable prices).

## Why it matters (commodities and FX)

Execution quality is a direct P&L line item. On a $50 million commodity portfolio turning over 2x per year, 2 ticks of execution improvement per trade can be worth $500,000+ annually. For [[Relative Value Trade|spread trades]], execution is even more critical: both legs must be executed near simultaneously to lock in the intended spread level. A 1 tick miss on each leg of a [[Calendar Spread]] doubles the execution cost.

In commodity markets, execution algos must account for: concentrated liquidity windows (pit session hours for many CME contracts), roll period clustering (Goldman roll, index rebalancing), and event driven [[Volatility]] (EIA inventory report, OPEC decisions). An algo running through an EIA number will behave very differently than one running in a calm afternoon.

## Concrete example

**Spread execution:** You want to enter a [[Brent-WTI Spread]] trade: buy 100 WTI, sell 100 Brent. Approaches:

1. **Legging:** Execute one leg, then the other. Risk: the market moves between legs and the spread changes. If you buy WTI at $74.00 and Brent moves from $78.00 to $78.30 before you sell, your entry spread is $4.30 instead of $4.00.

2. **Spread algo:** Simultaneously works both legs, monitoring the spread level. Buys WTI and sells Brent only when the spread is at or near the target level ($4.00). Child orders on both sides, with logic that pauses one leg if the other falls behind. Much tighter spread execution but requires cross exchange connectivity (WTI on NYMEX, Brent on ICE).

3. **Exchange listed spread:** Some exchanges list calendar spreads as a single instrument with its own order book. You can buy/sell the spread directly at a single price. Most capital efficient but limited to intra exchange spreads.

## Key mechanics and formulas

**Algo type selection:**

| Scenario | Recommended Algo |
|----------|-----------------|
| Passive, no urgency, liquid market | [[VWAP]] |
| Passive, unpredictable volume | [[TWAP]] |
| Urgent, alpha decaying | Implementation Shortfall (IS) |
| Hidden size, illiquid market | Iceberg / dark pool sweep |
| Spread trade, 2 legs | Spread algo with leg management |
| Event sensitive (pre EIA) | Hold execution, resume after |

**Implementation Shortfall (IS):**
`IS = Decision Price - Execution Price (adjusted for direction)`

IS algos trade aggressively early (when the alpha signal is strongest and information leakage risk is lowest) and slow down later. They minimize the total cost of delay + market impact.

**Child order mechanics:**
Parent order: Buy 500 CL
- Child 1: Buy 20 CL limit at $74.02 (passive, inside the bid-ask)
- If filled in 30 seconds: next child
- If not filled: adjust price to $74.04 (more aggressive)
- Repeat with size/price adjustments across the execution window

**Participation rate:**
`Participation = Algo Volume / Market Volume`

Keep below 10 to 15% to minimize footprint. Above 20%: significant [[Market Impact]] likely.

## Prerequisites
- [[VWAP]]
- [[TWAP]]
- [[Liquidity]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Market Impact]] - the cost that algos are designed to minimize. Understanding the market impact model is essential for algo selection.
- [[Slippage]] - the realized cost of imperfect execution. Algos reduce but cannot eliminate slippage.
- [[Liquidity]] - algo behavior must adapt to available liquidity. Running a VWAP in an illiquid hour produces poor results.
- [[Volatility]] - execution cost scales with volatility. Algo parameters should adjust for vol regime.

## Common misconceptions

**"Algos always beat manual execution."** In thin markets or during events, a skilled manual trader who reads the order book can outperform a rigid algo. Algos excel in liquid, normal markets.

**"Just use VWAP for everything."** Different situations call for different algos. An urgent trade with alpha decay needs IS. A patient trade in a thin market needs an iceberg. Algo selection is a skill.

**"Lower participation rate is always better."** Lower participation reduces impact but increases execution time, exposing you to adverse price movements. The optimal participation rate balances impact cost vs timing risk.

## Sources

- Kissell, "The Science of Algorithmic Trading and Portfolio Management" (2013)
- Almgren and Chriss, "Optimal Execution of Portfolio Transactions" (2000)
- CME Group: algo execution best practices for commodity futures
