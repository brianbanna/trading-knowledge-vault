---
aliases: [hard limit, absolute limit, system limit, red line]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Hard Limit

## Definition
A hard limit is an absolute maximum threshold enforced by the trading system that, when breached, triggers an automatic stop of all trading activity. Unlike a [[Soft Limit]], a hard limit is not a suggestion. It is a hard coded constraint in the risk engine that fires the [[Kill Switch]], cancels all outstanding orders, and may automatically flatten positions. Hard limits exist because in moments of extreme stress, panic, or system malfunction, human judgment cannot be relied upon. The system must protect the firm from itself. Hard limits are the last line of defense between a bad day and a firm ending event.

## Why it matters (commodities and FX)
Commodities and FX markets produce tail events that can exceed anything in the historical record. On January 15, 2015, the SNB removed the [[EURCHF]] floor and the pair fell from 1.2000 to 0.8500 in minutes. Any firm without a hard limit that automatically liquidated EURCHF positions lost everything. In commodities, the nickel short squeeze of March 2022 saw LME nickel rise from $29,000 to over $100,000 per tonne in 2 days. A hard limit on [[Nickel]] position size would have capped the loss at a survivable level. Hard limits are not about optimizing PnL; they are about ensuring the firm survives to trade the next day.

## Concrete example
An FX prop desk trades [[USDJPY]] on multiple [[ECN]]s. The risk framework is:

| Metric | [[Soft Limit]] | Hard Limit |
|---|---|---|
| Net position | $150 million | $200 million |
| Daily PnL loss | -$300,000 | -$500,000 |

**Win scenario (hard limit saves the firm):** A flash crash in USDJPY drops the pair 400 pips in 2 minutes at 3 AM Tokyo time. The desk's algo is long $180 million notional. The daily PnL drops from -$100,000 to -$500,000 in 90 seconds. The hard limit fires. The [[Kill Switch]] cancels all quotes on EBS, Reuters, and Hotspot. The system sends market orders to flatten the $180 million position. Final loss: $620,000 after [[Slippage]]. Painful but survivable.

**Fail scenario (no hard limit):** Same flash crash, but the algo keeps running because there is no hard cutoff. The algo interprets the crash as a buying opportunity (mean reversion signal) and adds to the long. Position grows to $350 million. USDJPY drops another 200 pips before recovering. Peak unrealized loss: $2.8 million. The firm barely survives and the algo is permanently retired.

## Key mechanics and formulas
**Hard limit types:**
- Position hard limit: |Q| ≤ Q_max (max contracts or notional)
- PnL hard limit: PnL_daily ≥ L_pnl (minimum allowed daily PnL, a negative number)
- [[Value at Risk]] hard limit: VaR_daily ≤ V_max
- Message rate hard limit: orders_per_second ≤ R_max (catches runaway algos)

**Enforcement latency:** Time from breach detection to full cancellation. Target: < 100 milliseconds. Formula:
T_enforcement = T_detection + T_cancel + T_confirm
Where T_detection = time for risk engine to compute breach, T_cancel = time to send mass cancel, T_confirm = time to receive acknowledgment from exchange.

**Loss beyond hard limit (slippage allowance):**
L_actual = L_hard + S
Where S = [[Slippage]] from liquidating the position after the kill switch fires. S depends on position size, [[Liquidity Risk]], and market volatility at the time of liquidation.

## Prerequisites
- [[Soft Limit]]
- [[Kill Switch]]
- [[Daily Loss Limit]]
- [[Position Limit]]

## Related concepts (learn next)
- [[Soft Limit]] — the warning threshold that precedes the hard limit, giving time for orderly de-risking.
- [[Kill Switch]] — the mechanism that enforces the hard limit by cancelling all orders and stopping the system.
- [[Circuit Breaker]] — an exchange level equivalent of a hard limit, halting trading for all participants.
- [[Maximum Drawdown]] — hard limits can be set on cumulative drawdown across days, not just daily PnL.
- [[Margin]] — exchange margin requirements act as an external hard limit on position size.
- [[Gap Risk]] — the reason hard limits must trigger instantly: prices can skip through levels.
- [[Daily Loss Limit]] — the most common type of hard limit for PnL.

## Common misconceptions
1. **"Hard limits can be overridden by senior traders."** At well run firms, no one can override a hard limit in real time. Changes to hard limits require formal approval from the risk committee and a system deploy, not a phone call during a crisis.
2. **"Setting hard limits wider gives more room to recover."** Wider hard limits increase the maximum possible loss. The hard limit should be set at the maximum loss the firm can absorb without jeopardizing its capital base, not at the level that maximizes expected PnL.
3. **"Hard limits only need to cover the trading session."** Positions held [[Overnight Risk]] are still subject to hard limits. Some firms have separate, tighter hard limits for overnight and weekend positions.

## Sources
- FIA. "Market Access Risk Recommendations." fia.org.
- CME Group. "Globex Credit Controls and Risk Management." cmegroup.com.
- SEC Rule 15c3-5. "Market Access Rule." sec.gov.
