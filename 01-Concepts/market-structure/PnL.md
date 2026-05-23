---
aliases: [PnL, P&L, profit and loss, P/L]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# PnL

## Definition
PnL is Profit and Loss, the measure of how much a trader, desk, or firm has made or lost. It has 2 components: [[Realized PnL]] (closed trades) and [[Unrealized PnL]] (open positions marked at current prices). Total PnL = [[Realized PnL]] + [[Unrealized PnL]]. It is the single most important number in trading, reported daily, and the basis for performance, risk limits, and compensation.

## Why it matters (commodities and FX)
PnL is how the business keeps score. A commodities desk's daily PnL drives capital allocation: profitable desks get more, losing desks get cut. In FX, PnL attribution is complex because you trade many [[Currency Pair]]s and PnL is in different currencies needing conversion. Traders watch a real time PnL blotter showing contribution per [[Position]] and use it to decide whether to add to winners, cut losers, or go [[Flat]]. Monthly and yearly PnL drives bonuses and careers.

## Concrete example

**Concrete:** You start the day [[Flat]]. Go [[Long]] 20M EUR/USD at 1.0800. By noon the rate is 1.0835. [[Unrealized PnL]] = 20,000,000 × 0.0035 = 70,000 USD. You close half (10M) at 1.0835, booking 35,000 USD [[Realized PnL]]. The rate continues to 1.0860. The remaining 10M shows [[Unrealized PnL]] = 60,000 USD. Day total = 35,000 realized + 60,000 unrealized = 95,000 USD. Adverse case: long 50 lots of gold at 2,050 USD/oz. Gold drops to 2,020. [[Unrealized PnL]] = 50 × 100 × (2,020 minus 2,050) = -150,000 USD. You hold hoping for a bounce. Gold drops to 2,000, unrealized -250,000. Risk forces a close at 2,005. [[Realized PnL]] = -225,000 USD. The slippage between unrealized and realized came from the [[Bid-Ask Spread]] and [[Slippage]] on exit.

**Simplified:** PnL = money made minus money lost. Two flavors: realized (locked in from closed trades) and unrealized (paper profit on open positions, changes with every tick). Add them for total. Every conversation on a trading floor eventually circles back to this number.

## Key mechanics and formulas
- Total PnL = [[Realized PnL]] + [[Unrealized PnL]]
- Daily PnL = Today's [[Mark to Market]] minus Yesterday's MTM + cash flows
- FX PnL: PnL = [[Notional]] × (Current Rate minus Entry Rate)
  - Convert to reporting currency if PnL is in a foreign currency
- Futures PnL: PnL = Contracts × Multiplier × (Current Price minus Entry Price)
  - Multiplier: 100 oz for gold, 1,000 barrels for WTI
- PnL per [[Pip]] in FX = [[Notional]] × Pip value (0.0001 most pairs, 0.01 JPY)

## Prerequisites
- [[Position]]
- [[Long]]
- [[Short]]
- [[Notional]]
- [[Mark to Market]]

## Related concepts (learn next)
- [[Realized PnL]], locked in profit from closed trades
- [[Unrealized PnL]], paper profit or loss on open positions
- [[Mark to Market]], the process generating daily PnL
- [[Sharpe Ratio]], risk adjusted PnL for performance evaluation
- [[Drawdown]], peak to trough decline in cumulative PnL
- [[Transaction Costs]], drag on PnL from spreads and commissions
- [[PnL Attribution]], decomposing into factors like delta, gamma, carry

## Common misconceptions
- **PnL is not just about winning trades.** A trader with 60% losing trades is profitable if winners are larger than losers. PnL = hit rate × average win minus loss rate × average loss.
- **Unrealized PnL is real.** Some dismiss it as "just paper" but [[Mark to Market]] affects margin, risk limits, and capacity for new positions. Ignoring it leads to ruin.
- **PnL in different currencies must be converted consistently.** 100,000 EUR profit on a EUR/CHF trade must convert to reporting currency (say USD) at the current rate before aggregation.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- Taleb, N.N. *Dynamic Hedging*, Chapter 1
- CME Group, "Understanding Daily Settlement and PnL"
