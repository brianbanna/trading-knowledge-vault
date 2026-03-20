---
aliases: [slippage, execution slippage, fill slippage]
tags:
  - "#execution"
  - "#microstructure"
date-added: "2026-03-20"
---

# Slippage

## Definition

Slippage is the difference between the intended execution price and the actual fill price. It is the total cost of executing a trade, encompassing [[Bid-Ask Spread]] crossing, [[Market Impact]], timing delays, and adverse price movement during execution. Slippage is always a cost to the trader (fills are worse than intended) because you cross the spread to buy (pay the ask) or sell (hit the bid), and large orders push the price against you. Slippage is the gap between a backtest (which assumes perfect fills) and reality.

## Why it matters (commodities and FX)

Slippage determines whether a strategy that works on paper actually works in practice. A mean reversion strategy on the [[Brent-WTI Spread]] might show 5 bps of alpha per trade in backtesting. If slippage is 3 bps per leg (6 bps round trip), the strategy is unprofitable after execution costs. For spread trades with 2 legs, slippage doubles: you incur slippage on both the buy and sell side.

In commodity markets, slippage varies by orders of magnitude across instruments and times. Slippage in front month WTI during pit hours: ~1 tick ($0.01/bbl). Slippage in a deferred [[Henry Hub Natural Gas]] month during overnight: potentially $0.005 to $0.02/MMBtu ($50 to $200 per contract). A strategy must be modeled with realistic slippage for the specific instruments and times it trades.

## Concrete example

You want to enter a [[Calendar Spread]]: buy Dec WTI, sell Mar WTI. Your decision prices (midpoint when you decided to trade):
- Dec mid: $75.00
- Mar mid: $73.80
- Intended spread: $1.20

Actual fills (after execution):
- Dec fill: $75.02 (paid $0.02 above mid, crossed the ask)
- Mar fill: $73.78 (received $0.02 below mid, hit the bid)
- Actual spread: $1.24

Slippage per leg: $0.02. Total spread slippage: $0.04 (the spread entry is $0.04 worse than intended). On 100 spreads x 1,000 bbl: $4,000 of slippage cost. If your expected profit on this spread is $0.15/bbl ($15,000 on 100 spreads), slippage consumed 27% of expected profits.

## Key mechanics and formulas

**Slippage decomposition:**
`Slippage = Spread Cost + Market Impact + Timing Cost`

- Spread cost: half the [[Bid-Ask Spread]] per trade (you cross from mid to bid or ask)
- Market impact: additional price movement from your order consuming [[Liquidity]]
- Timing cost: adverse price movement between decision and execution (especially for [[Execution Algorithms|algo execution]] over extended periods)

**Slippage estimation for backtesting:**
- Conservative: assume full spread crossing per trade (buy at ask, sell at bid)
- Moderate: half spread + estimated impact based on order size / ADV
- Aggressive (unrealistic): zero slippage (only for initial screening, not production)

**Slippage as % of notional:**
`Slippage % = Slippage per unit / Price x 10,000 (bps)`

WTI front month: $0.02 / $75 = 0.27 bps (negligible)
Thin commodity: $0.50 / $20 = 25 bps (significant)

## Prerequisites
- [[Bid-Ask Spread]]
- [[Liquidity]]
- [[Market Impact]]

## Related concepts (learn next)
- [[Market Impact]] - the portion of slippage caused by your own trade moving the price.
- [[Execution Algorithms]] - the primary tool for reducing slippage on large orders.
- [[VWAP]] - benchmark for measuring whether slippage was controlled.
- [[Liquidity]] - the main determinant of slippage magnitude.
- [[Liquidity Risk]] - extreme slippage during crises can turn a controlled exit into a disorderly liquidation.

## Common misconceptions

**"Slippage is small enough to ignore."** For high frequency or high turnover strategies, slippage is the dominant cost. A strategy trading 100 round trips per month with 2 bps slippage per trade incurs 400 bps monthly in execution costs.

**"Backtests with zero slippage are directionally correct."** They can be completely wrong. Many backtested strategies show positive returns that disappear entirely when realistic slippage is applied. Always backtest with conservative slippage assumptions.

**"Limit orders have zero slippage."** Limit orders that fill have zero or negative slippage (price improvement). But limit orders that do NOT fill have infinite slippage (you missed the trade entirely). The expected slippage of a limit order strategy must include the cost of missed trades.

## Sources

- Kissell, "The Science of Algorithmic Trading" (2013)
- Harris, "Trading and Exchanges" (2003), chapters on execution costs
- Almgren, "Optimal Trading in a Dynamic Market" (2012)
