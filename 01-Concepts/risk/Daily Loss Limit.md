---
aliases: [daily loss limit, daily stop loss, daily PnL limit, daily drawdown limit]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Daily Loss Limit

## Definition
A daily loss limit is the maximum amount of money a trader or strategy is allowed to lose in a single trading day. When the realized plus unrealized [[PnL]] for the day hits this threshold, the trader must stop trading and all automated systems must be shut down. Daily loss limits are the most fundamental risk control in professional trading. They exist because a single catastrophic day can undo months of profits, and because human judgment deteriorates rapidly when losses are mounting. The limit forces a mandatory cooling off period.

## Why it matters (commodities and FX)
Commodity and FX markets can produce outsized single day moves that destroy accounts. On April 20, 2020, WTI crude oil went negative for the first time, falling from $17.73 to -$37.63 in a single session. A trader without a daily loss limit could have ridden that move all the way down. In FX, the January 2015 EURCHF de-peg moved 30% in minutes, blowing up multiple brokerages. Daily loss limits ensure that no matter how bad the environment gets, the firm's total daily exposure is capped. For market makers, the limit is typically set relative to the strategy's expected daily revenue. A strategy that makes $10,000 per day on average might have a daily loss limit of $50,000 (5x daily revenue).

## Concrete example
A market making desk quotes [[Natural Gas]] futures on NYMEX. The desk's daily loss limit is $75,000. The desk has a [[Soft Limit]] at $50,000 and a [[Hard Limit]] at $75,000.

**Win scenario (limit saves the desk):** On a Thursday, the EIA natural gas storage report surprises heavily bearish. The desk is long 150 lots when the number drops. PnL goes from +$8,000 to -$52,000 in 90 seconds. The $50,000 soft limit triggers an alert. The senior trader manually reduces exposure to 50 lots. The market stabilizes. End of day PnL: -$61,000. The desk stays under the hard limit and preserves the ability to trade tomorrow.

**Fail scenario (no limit):** Same event, but the junior trader running the algo is convinced the market will bounce. No daily loss limit is enforced. The trader doubles down, going long 300 lots. Natural gas keeps falling. End of day PnL: -$340,000. This wipes out 2 months of profits for the entire desk and the trader is fired.

## Key mechanics and formulas
**Daily PnL calculation:**
PnL_daily = PnL_realized + PnL_unrealized
PnL_realized = Σ (P_exit - P_entry) x Q for each closed trade
PnL_unrealized = (P_current - P_entry) x Q for open positions

**Limit sizing heuristic:**
Daily loss limit = k x σ_daily_PnL
Where k is typically between 3 and 5, and σ_daily_PnL is the standard deviation of daily PnL over the past 60 to 120 trading days. Setting k = 3 means the limit is breached roughly once every 6 months under normal conditions.

**Alternative sizing:** Daily loss limit = n x average daily revenue, where n is typically 3 to 10 depending on the firm's risk appetite and strategy Sharpe ratio.

## Prerequisites
- [[PnL]]
- [[Volatility]]
- [[Maximum Drawdown]]

## Related concepts (learn next)
- [[Soft Limit]] — the warning level (typically 60% to 75% of the daily loss limit) that signals the trader to reduce risk.
- [[Hard Limit]] — the absolute level that triggers automatic shutdown via the [[Kill Switch]].
- [[Position Limit]] — caps the size of the position, while the daily loss limit caps the PnL impact.
- [[Maximum Drawdown]] — the cumulative peak to trough loss across multiple days, a longer horizon version of daily loss limits.
- [[Kill Switch]] — the mechanism that enforces the hard daily loss limit by cancelling all orders.
- [[Value at Risk]] — a probabilistic measure of potential daily loss that can inform the daily loss limit level.
- [[Inventory Risk]] — unmanaged inventory is the primary path to breaching a daily loss limit for market makers.

## Common misconceptions
1. **"The daily loss limit should be tight to minimize losses."** A limit that is too tight gets triggered by normal volatility, causing the desk to stop trading on profitable days that happen to have a drawdown in the middle. The limit should be calibrated to allow normal variance while preventing catastrophic outcomes.
2. **"Unrealized losses do not count."** Professional risk systems include mark to market unrealized PnL in the daily limit calculation. A trader who is down $70,000 on paper but has not closed the trades is just as much at risk as one who has realized the loss.
3. **"Once I hit the daily loss limit, I can resume if PnL improves."** Most firms enforce a strict lockout for the remainder of the day. Allowing a trader to resume after briefly touching the limit defeats the purpose, because the market can immediately reverse again.

## Sources
- CME Group. "Pre-Trade Risk Controls." cmegroup.com.
- Aldridge, I. (2013). *High-Frequency Trading: A Practical Guide to Algorithmic Strategies*. Wiley.
- FIA. "Risk Management Best Practices for Electronic Trading." fia.org.
