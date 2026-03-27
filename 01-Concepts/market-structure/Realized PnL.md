---
aliases: [realized PnL, realized profit, closed PnL, booked PnL]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Realized PnL

## Definition
Realized PnL is the profit or loss from trades you have actually closed. Once you exit a [[Position]], the gain or loss becomes "realized," meaning it is locked in and no longer affected by market moves. If you bought EUR/USD at 1.0800 and sold at 1.0850, your realized PnL is the difference times the [[Notional]]. It is the definitive measure of trading performance because it cannot change. Unrealized gains can evaporate, but realized PnL is permanent.

## Why it matters (commodities and FX)
Realized PnL is how traders, desks, and funds are ultimately judged. Year end bonuses are based on realized (booked) PnL, not open positions. In commodities trading, a physical house might show huge [[Unrealized PnL]] on inventory, but the business only books revenue when the cargo is sold and delivered. In FX, spot trades settle in T+2, and the realized PnL is final at settlement. Risk managers track realized PnL to measure hit rate (percentage of winning trades) and average win versus average loss, which together determine the edge.

## Concrete example
**Win scenario:** Over a month, you execute 15 round trip trades in gold futures. 9 are winners averaging +12,000 USD each. 6 are losers averaging negative 8,000 USD each. Your realized PnL = (9 x 12,000) + (6 x negative 8,000) = 108,000 minus 48,000 = 60,000 USD. This is booked, final, and forms the basis for your performance review.

**Fail scenario:** You close a [[Long]] [[Position]] in Brent crude at 79.00 after entering at 82.00, booking a realized loss of 50 x 1,000 x (79.00 minus 82.00) = negative 150,000 USD. The next day, Brent rallies back to 82.50. The realized loss does not change, you already closed. This is the painful reality of realized PnL: it is final regardless of what happens next.

## Key mechanics and formulas
- Realized PnL = Quantity x (Exit Price minus Entry Price), for [[Long]] positions
- Realized PnL = Quantity x (Entry Price minus Exit Price), for [[Short]] positions
- For multiple entries: use average entry price or FIFO (first in, first out) method
  - FIFO: match exits against the oldest entry first
  - Average: Realized PnL = Quantity closed x (Exit Price minus Weighted Average Entry Price)
- Total Realized PnL = Sum of all closed trade PnLs
- Hit rate = Number of winning trades / Total number of trades
- Profit factor = Gross profits / Gross losses

## Prerequisites
- [[PnL]]
- [[Position]]
- [[Long]]
- [[Short]]

## Related concepts (learn next)
- [[Unrealized PnL]] , the complement, representing open position gains or losses
- [[Mark to Market]] , which tracks PnL before it becomes realized
- [[PnL]] , the total of realized and unrealized
- [[Transaction Costs]] , which reduce realized PnL on every trade
- [[Bid-Ask Spread]] , a component of transaction costs that directly reduces realized PnL
- [[Sharpe Ratio]] , a risk adjusted measure of realized returns over time
- [[Drawdown]] , the cumulative loss from peak realized PnL

## Common misconceptions
- **Realized PnL does not mean the trade was good.** Closing a winner early for small profit when the trade runs much further is a realized gain but poor execution. Conversely, taking a disciplined [[Stop Loss]] that limits damage is a realized loss but good trading.
- **Tax treatment depends on realized PnL.** In most jurisdictions, you only owe taxes on realized gains, not [[Unrealized PnL]]. This creates incentives around when to close positions, especially near year end.
- **Realized PnL ignores financing and carry.** The simple calculation (exit minus entry) does not include the interest or carry earned or paid while holding the [[Position]]. Full PnL accounting must add these components.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- CME Group, "Understanding Trading Performance Metrics"
- Taleb, N.N. *Dynamic Hedging*, Chapter 1
