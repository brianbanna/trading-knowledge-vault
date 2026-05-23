---
aliases: [realized PnL, realized profit, closed PnL, booked PnL]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Realized PnL

## Definition
Realized PnL is the profit or loss from trades you have closed. Once you exit a [[Position]], the gain or loss is locked in and no longer affected by market moves. Buy EUR/USD at 1.0800 and sell at 1.0850: realized PnL = the difference × [[Notional]]. It is the definitive measure of trading performance because it cannot change. Unrealized gains evaporate; realized PnL is permanent.

## Why it matters (commodities and FX)
Realized PnL is how traders, desks, and funds are ultimately judged. Year end bonuses are based on realized (booked) PnL, not open positions. In commodities, a physical house may show huge [[Unrealized PnL]] on inventory but the business only books revenue when the cargo is sold and delivered. In FX, spot trades settle T+2 and realized PnL is final at settlement. Risk managers track realized PnL to measure hit rate (% winners) and average win vs average loss, which together define edge.

## Concrete example

**Concrete:** Over a month you execute 15 round trips in gold futures. 9 winners averaging +12,000 USD, 6 losers averaging -8,000 USD. Realized PnL = (9 × 12,000) + (6 × -8,000) = 108,000 - 48,000 = 60,000 USD. Booked, final, basis for performance review. Adverse case: you close a [[Long]] Brent [[Position]] at 79.00 after entering at 82.00, booking a realized loss of 50 × 1,000 × -3.00 = -150,000 USD. The next day Brent rallies back to 82.50. The realized loss does not change. You already closed.

**Simplified:** Money you actually made or lost after closing the trade. Cannot change after that point. Different from unrealized PnL (paper profit on open trades), which moves with every tick. Bonus, taxes, performance: all calculated on realized.

## Key mechanics and formulas
- Realized PnL = Quantity × (Exit Price minus Entry Price), for [[Long]]
- Realized PnL = Quantity × (Entry Price minus Exit Price), for [[Short]]
- Multiple entries: use average entry or FIFO
  - FIFO: match exits against oldest entry first
  - Average: Realized PnL = Quantity closed × (Exit minus Weighted Average Entry)
- Total Realized PnL = sum of all closed trade PnLs
- Hit rate = Winning trades / Total trades
- Profit factor = Gross profits / Gross losses

## Prerequisites
- [[PnL]]
- [[Position]]
- [[Long]]
- [[Short]]

## Related concepts (learn next)
- [[Unrealized PnL]], the complement on open positions
- [[Mark to Market]], tracks PnL before realization
- [[PnL]], the total
- [[Transaction Costs]], drag on realized PnL each trade
- [[Bid-Ask Spread]], a component of transaction costs
- [[Sharpe Ratio]], risk adjusted realized returns over time
- [[Drawdown]], cumulative loss from peak realized PnL

## Common misconceptions
- **Realized PnL does not mean the trade was good.** Closing a winner early for small profit when the trade runs further is realized gain but poor execution. A disciplined [[Stop Loss]] limiting damage is realized loss but good trading.
- **Tax depends on realized PnL.** In most jurisdictions, you owe tax only on realized gains, not [[Unrealized PnL]]. This creates timing incentives, especially near year end.
- **Realized PnL ignores financing and carry.** Simple exit minus entry omits interest or carry earned or paid while holding. Full PnL accounting adds these.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- CME Group, "Understanding Trading Performance Metrics"
- Taleb, N.N. *Dynamic Hedging*, Chapter 1
