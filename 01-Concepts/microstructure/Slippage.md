---
aliases: [slippage, execution slippage, fill slippage]
tags:
  - "#execution"
  - "#microstructure"
date-added: "2026-03-20"
---

# Slippage

## Definition

Slippage is the difference between intended execution price and actual fill price. It is the total execution cost, including [[Bid-Ask Spread]] crossing, [[Market Impact]], timing delays, and adverse movement during execution. Slippage is always a cost (fills are worse than intended) because you cross the spread to buy (pay ask) or sell (hit bid), and large orders push price against you. Slippage is the gap between a backtest (perfect fills) and reality.

## Why it matters (commodities and FX)

Slippage decides whether a paper strategy works in practice. A mean reversion on the [[Brent-WTI Spread]] might show 5 bps alpha per trade in backtest. If slippage is 3 bps per leg (6 bps round trip), it is unprofitable. For 2 leg spread trades, slippage doubles: incurred on both buy and sell.

Commodity slippage varies by orders of magnitude across instruments and times. Front month WTI in pit hours: ~1 tick ($0.01/bbl). Deferred [[Henry Hub Natural Gas]] overnight: $0.005 to $0.02/MMBtu ($50 to $200/contract). Strategies need realistic slippage modeled for the specific instruments and times traded.

## Concrete example

**Concrete:** Enter [[Calendar Spread]]: buy Dec WTI, sell Mar WTI. Decision prices (mid at decision): Dec $75.00, Mar $73.80, intended spread $1.20. Actual fills: Dec $75.02 (paid $0.02 above mid), Mar $73.78 (received $0.02 below mid). Actual spread $1.24. Slippage per leg $0.02. Total spread slippage $0.04 (entry $0.04 worse than intended). 100 spreads x 1,000 bbl: $4,000 slippage. Expected profit $0.15/bbl ($15,000 on 100 spreads): slippage consumed 27% of expected profit.

**Simplified:** Slippage is the gap between the price you wanted and the price you got. Always works against you. Comes from crossing the spread, your own order pushing the market, and the market moving while you wait. Backtests assume zero slippage; reality has plenty. A strategy that looks great on paper can lose money once realistic execution costs are applied.

## Key mechanics and formulas

**Slippage decomposition:**
`Slippage = Spread Cost + Market Impact + Timing Cost`

- Spread cost: half the [[Bid-Ask Spread]] per trade (cross from mid to bid or ask)
- Market impact: additional movement from your order consuming [[Liquidity]]
- Timing cost: adverse movement between decision and execution (especially for [[Execution Algorithms|algo]] over extended periods)

**Slippage for backtests:**
- Conservative: assume full spread crossing per trade
- Moderate: half spread + estimated impact based on size / ADV
- Aggressive (unrealistic): zero slippage (initial screening only)

**Slippage as % of notional:**
`Slippage % = Slippage per unit / Price x 10,000 (bps)`

WTI front: $0.02 / $75 = 0.27 bps (negligible)
Thin commodity: $0.50 / $20 = 25 bps (significant)

## Prerequisites
- [[Bid-Ask Spread]]
- [[Liquidity]]
- [[Market Impact]]

## Related concepts (learn next)
- [[Market Impact]] - the portion of slippage from your own trade moving price
- [[Execution Algorithms]] - primary tool for reducing slippage on large orders
- [[VWAP]] - benchmark for measuring whether slippage was controlled
- [[Liquidity]] - the main determinant of slippage magnitude
- [[Liquidity Risk]] - extreme slippage in crises turns controlled exits into disorderly liquidations

## Common misconceptions

**"Slippage is small enough to ignore."** For high frequency or high turnover strategies, slippage is the dominant cost. 100 round trips per month at 2 bps slippage per trade = 400 bps monthly in execution costs.

**"Zero slippage backtests are directionally correct."** They can be completely wrong. Many backtested strategies show positive returns that vanish under realistic slippage. Always backtest with conservative assumptions.

**"Limit orders have zero slippage."** Limit orders that fill have zero or negative slippage (price improvement). Limit orders that do NOT fill have infinite slippage (missed trade entirely). Expected slippage on limit strategies must include cost of missed trades.

## Sources

- Kissell, "The Science of Algorithmic Trading" (2013)
- Harris, "Trading and Exchanges" (2003), chapters on execution costs
- Almgren, "Optimal Trading in a Dynamic Market" (2012)
