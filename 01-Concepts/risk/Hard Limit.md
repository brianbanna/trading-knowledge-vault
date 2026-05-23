---
aliases: [hard limit, absolute limit, system limit, red line]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Hard Limit

## Definition
A hard limit is an absolute maximum threshold enforced by the trading system that, when breached, automatically stops all trading. Unlike a [[Soft Limit]], it is not a suggestion. It is a hard coded constraint in the risk engine that fires the [[Kill Switch]], cancels all outstanding orders, and may auto flatten positions. Hard limits exist because in extreme stress, panic, or system malfunction, human judgment cannot be trusted. The system must protect the firm from itself. Hard limits are the last line of defense between a bad day and a firm ending event.

## Why it matters (commodities and FX)
Commodities and FX produce tail events that exceed anything in the historical record. On January 15, 2015, the SNB removed the [[EURCHF]] floor and the pair fell from 1.2000 to 0.8500 in minutes. Firms without auto liquidating hard limits lost everything. In commodities, the nickel short squeeze of March 2022 ran LME nickel from $29,000 to over $100,000/tonne in 2 days. A hard limit on [[Nickel]] size would have capped the loss at a survivable level. Hard limits are not about optimizing P&L; they ensure the firm survives to trade tomorrow.

## Concrete example
**Concrete:** An FX prop desk trades [[USDJPY]] across multiple [[ECN]]s. Risk framework:

| Metric | [[Soft Limit]] | Hard Limit |
|---|---|---|
| Net position | $150M | $200M |
| Daily P&L loss | −$300,000 | −$500,000 |

A flash crash drops USDJPY 400 pips in 2 minutes at 3 AM Tokyo. The desk algo is long $180M notional. Daily P&L falls from −$100,000 to −$500,000 in 90 seconds. The hard limit fires. Kill switch cancels all quotes on EBS, Reuters, Hotspot. The system sends market orders to flatten $180M. Final loss: $620,000 after [[Slippage]]. Painful but survivable.

**Simplified:** Two numbers protect the desk: the soft limit (warning) and the hard limit (auto shutdown). The hard limit is enforced by software, not a human. When P&L or position size crosses it, the system cancels every quote, stops sending new orders, and may liquidate. The number must be set at the maximum loss the firm can absorb without endangering its capital base. Wider hard limits mean larger possible losses. The point is binary: trade tomorrow, or do not.

## Key mechanics and formulas
**Hard limit types:**
- Position: |Q| ≤ Q_max (max contracts or notional)
- P&L: PnL_daily ≥ L_pnl (minimum allowed daily P&L, negative)
- [[Value at Risk]]: VaR_daily ≤ V_max
- Message rate: orders_per_second ≤ R_max (catches runaway algos)

**Enforcement latency:** time from breach detection to full cancellation. Target: < 100 ms.
T_enforcement = T_detection + T_cancel + T_confirm

**Loss beyond hard limit (slippage):**
L_actual = L_hard + S
S = [[Slippage]] from liquidating after the kill switch fires; depends on size, [[Liquidity Risk]], and vol at the time.

## Prerequisites
- [[Soft Limit]]
- [[Kill Switch]]
- [[Daily Loss Limit]]
- [[Position Limit]]

## Related concepts (learn next)
- [[Soft Limit]] — warning threshold preceding the hard limit, giving time for orderly de-risking.
- [[Kill Switch]] — mechanism enforcing the hard limit by cancelling orders and halting the system.
- [[Circuit Breaker]] — exchange level equivalent, halting trading for all participants.
- [[Maximum Drawdown]] — hard limits can be set on cumulative drawdown across days.
- [[Margin]] — exchange margin acts as an external hard limit on position size.
- [[Gap Risk]] — the reason hard limits must trigger instantly: prices skip through levels.
- [[Daily Loss Limit]] — the most common type of hard limit for P&L.

## Common misconceptions
1. **"Hard limits can be overridden by senior traders."** At well run firms, no one overrides a hard limit in real time. Changes require formal risk committee approval and a system deploy, not a phone call during a crisis.
2. **"Wider hard limits give more room to recover."** Wider limits raise the maximum loss. The hard limit must be the maximum loss the firm can absorb without jeopardizing capital, not the level that maximizes expected P&L.
3. **"Hard limits only need to cover the session."** Positions held overnight (see [[Overnight Risk]]) remain subject to hard limits. Some firms enforce tighter overnight and weekend hard limits.

## Sources
- FIA. "Market Access Risk Recommendations." fia.org.
- CME Group. "Globex Credit Controls and Risk Management." cmegroup.com.
- SEC Rule 15c3-5. "Market Access Rule." sec.gov.
