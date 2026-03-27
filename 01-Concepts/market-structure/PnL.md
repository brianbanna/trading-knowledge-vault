---
aliases: [PnL, P&L, profit and loss, P/L]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# PnL

## Definition
PnL stands for Profit and Loss. It is the measure of how much money a trader, desk, or firm has made or lost. PnL has 2 components: [[Realized PnL]] (from closed trades) and [[Unrealized PnL]] (from open positions marked at current prices). Total PnL = [[Realized PnL]] + [[Unrealized PnL]]. It is the single most important number in trading, reported daily, and the basis for performance evaluation, risk limits, and compensation.

## Why it matters (commodities and FX)
PnL is how the business keeps score. A commodities desk's daily PnL drives risk allocation: desks making money get more capital, desks losing money get cut. In FX, PnL attribution is complex because you trade multiple [[Currency Pair]]s and the PnL itself is in different currencies that must be converted. Traders typically see a PnL blotter updated in real time that shows contribution by [[Position]], and they use it to decide whether to add to winners, cut losers, or go [[Flat]]. Monthly and yearly PnL determines bonuses and career trajectory.

## Concrete example
**Win scenario:** You start the day [[Flat]]. You go [[Long]] 20 million EUR/USD at 1.0800. By noon, the rate is 1.0835. Your [[Unrealized PnL]] = 20,000,000 x 0.0035 = 70,000 USD. You close half (10 million) at 1.0835, booking [[Realized PnL]] of 35,000 USD. The rate continues to 1.0860. Your remaining 10 million has [[Unrealized PnL]] of 10,000,000 x 0.0060 = 60,000 USD. Total day PnL = 35,000 realized + 60,000 unrealized = 95,000 USD.

**Fail scenario:** You go [[Long]] 50 lots of gold at 2,050 USD/oz. Gold drops to 2,020. Your [[Unrealized PnL]] = 50 x 100 x (2,020 minus 2,050) = negative 150,000 USD. You hold, hoping for a bounce. Gold drops further to 2,000. [[Unrealized PnL]] is now negative 250,000 USD. Your risk manager forces you to close at 2,005. [[Realized PnL]] = 50 x 100 x (2,005 minus 2,050) = negative 225,000 USD. The difference between unrealized and realized came from the [[Bid-Ask Spread]] and [[Slippage]] on exit.

## Key mechanics and formulas
- Total PnL = [[Realized PnL]] + [[Unrealized PnL]]
- Daily PnL = Today's [[Mark to Market]] value minus Yesterday's [[Mark to Market]] value + any cash flows
- FX PnL for a single position: PnL = [[Notional]] x (Current Rate minus Entry Rate)
  - Must convert to reporting currency if PnL is in a foreign currency
- Futures PnL: PnL = Number of contracts x Multiplier x (Current Price minus Entry Price)
  - Multiplier: contract size (e.g., 100 oz for gold, 1,000 barrels for WTI)
- PnL per [[Pip]] in FX = [[Notional]] x Pip value (0.0001 for most pairs, 0.01 for JPY pairs)

## Prerequisites
- [[Position]]
- [[Long]]
- [[Short]]
- [[Notional]]
- [[Mark to Market]]

## Related concepts (learn next)
- [[Realized PnL]] , the locked in profit from closed trades
- [[Unrealized PnL]] , the paper profit or loss on open positions
- [[Mark to Market]] , the process that generates daily PnL
- [[Sharpe Ratio]] , risk adjusted PnL used to evaluate performance
- [[Drawdown]] , the peak to trough decline in cumulative PnL
- [[Transaction Costs]] , the drag on PnL from spreads and commissions
- [[PnL Attribution]] , decomposing PnL into factors like delta, gamma, carry

## Common misconceptions
- **PnL is not just about winning trades.** A trader can have 60% losing trades and still be profitable if winning trades are larger than losers. PnL depends on hit rate times average win versus average loss.
- **Unrealized PnL is real.** Some traders dismiss [[Unrealized PnL]] as "just paper." But it is [[Mark to Market]] value that affects margin, risk limits, and the ability to take new positions. Ignoring it leads to ruin.
- **PnL in different currencies must be converted consistently.** If you make 100,000 EUR on a EUR/CHF trade, you need to convert to your reporting currency (say USD) at the current rate to aggregate with your other PnL.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- Taleb, N.N. *Dynamic Hedging*, Chapter 1
- CME Group, "Understanding Daily Settlement and PnL"
