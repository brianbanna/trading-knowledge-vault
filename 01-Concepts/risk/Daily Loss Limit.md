---
aliases: [daily loss limit, daily stop loss, daily PnL limit, daily drawdown limit]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Daily Loss Limit

## Definition
A daily loss limit is the maximum amount a trader or strategy is allowed to lose in a single trading day. When realized plus unrealized [[PnL]] hits the threshold, trading stops and automated systems shut down. It is the most fundamental risk control in professional trading. One bad day can undo months of profits, and human judgment deteriorates as losses mount. The limit forces a mandatory cooling off.

## Why it matters (commodities and FX)
Commodity and FX markets produce single day moves that destroy accounts. On April 20, 2020, WTI went from $17.73 to −$37.63 in one session. A trader without a daily limit could have ridden it to the bottom. In FX, the January 2015 EURCHF de-peg moved 30% in minutes and blew up multiple brokerages. Daily limits cap exposure regardless of how bad the environment gets. For market makers, the limit is set relative to expected daily revenue. A strategy making $10,000/day might have a $50,000 limit (5x daily revenue).

## Concrete example
**Concrete:** A market making desk quotes [[Natural Gas]] futures on NYMEX. Daily loss limit $75,000, [[Soft Limit]] at $50,000, [[Hard Limit]] at $75,000. On Thursday, the EIA storage report surprises bearish. The desk is long 150 lots when the number drops. P&L falls from +$8,000 to −$52,000 in 90 seconds. The soft limit triggers; the senior trader cuts exposure to 50 lots. The market stabilizes. End of day P&L: −$61,000. Desk stays under the hard limit and trades tomorrow.

**Simplified:** Set a number that represents the worst single day you can afford. When the day's losses hit that number, stop trading. No exceptions. The number should be wide enough that normal volatility does not trigger it, narrow enough that one bad day cannot kill the firm. Mark to market unrealized P&L counts the same as realized. Once stopped, you stay stopped until tomorrow. The point is to remove the trader from a decision they would make poorly under stress.

## Key mechanics and formulas
**Daily P&L:**
PnL_daily = PnL_realized + PnL_unrealized
PnL_realized = Σ (P_exit − P_entry) × Q for closed trades
PnL_unrealized = (P_current − P_entry) × Q for open positions

**Limit sizing:**
Daily loss limit = k × σ_daily_PnL
k is typically 3 to 5; σ is the standard deviation of daily P&L over 60 to 120 trading days. k = 3 implies a breach roughly once every 6 months under normal conditions.

**Alternative sizing:** Daily loss limit = n × average daily revenue, where n is 3 to 10 depending on risk appetite and strategy Sharpe.

## Prerequisites
- [[PnL]]
- [[Volatility]]
- [[Maximum Drawdown]]

## Related concepts (learn next)
- [[Soft Limit]] — warning level (60 to 75% of the daily limit) signaling the trader to reduce risk.
- [[Hard Limit]] — absolute level triggering automatic shutdown via the [[Kill Switch]].
- [[Position Limit]] — caps position size; daily loss limit caps P&L impact.
- [[Maximum Drawdown]] — cumulative peak to trough across multiple days.
- [[Kill Switch]] — enforces the hard daily limit by cancelling orders.
- [[Value at Risk]] — probabilistic measure of potential daily loss that informs the limit.
- [[Inventory Risk]] — unmanaged inventory is the main path to breaching the daily limit for market makers.

## Common misconceptions
1. **"The limit should be tight to minimize losses."** A tight limit triggers on normal volatility and stops the desk on profitable days that happen to have a midday drawdown. Calibrate to allow normal variance, prevent catastrophes.
2. **"Unrealized losses do not count."** Professional risk systems include mark to market unrealized P&L. A trader $70,000 down on paper is just as exposed as one who realized it.
3. **"I can resume if P&L improves."** Most firms lock out the rest of the day. Allowing resumption after a brief touch defeats the purpose since the market can reverse again.

## Sources
- CME Group. "Pre-Trade Risk Controls." cmegroup.com.
- Aldridge, I. (2013). *High-Frequency Trading: A Practical Guide to Algorithmic Strategies*. Wiley.
- FIA. "Risk Management Best Practices for Electronic Trading." fia.org.
