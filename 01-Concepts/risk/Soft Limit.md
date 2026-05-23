---
aliases: [soft limit, warning limit, advisory limit, yellow light]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Soft Limit

## Definition
A soft limit is a warning threshold set below the [[Hard Limit]] that alerts the trader to reduce exposure voluntarily. When breached, the system does not force a shutdown but notifies the trader and risk manager that position or loss is approaching dangerous territory. Soft limits are the yellow light of risk management — they buy time for an orderly de-risk rather than a fire sale at the hard limit. Typical soft limits sit at 60 to 80% of the corresponding hard limit.

## Why it matters (commodities and FX)
In commodities, liquidating a large position in an illiquid contract ([[Cocoa]] back months, [[Palladium]] futures) takes time. If the first warning is the [[Hard Limit]] triggering a [[Kill Switch]], forced liquidation hits the worst prices with maximum [[Slippage]]. The soft limit gives time to unwind in pieces, perhaps hedging in a more liquid correlated instrument first. In FX, a spot [[EURUSD]] trader hitting a soft limit on a $200M position can reduce through natural client flow rather than dumping $200M in one clip, which would move price 2 to 3 pips against them.

## Concrete example
**Concrete:** A prop firm runs a [[Gold]] futures strategy on COMEX with layered limits:

| Limit type | Position | P&L |
|---|---|---|
| [[Soft Limit]] | 400 contracts | −$80,000 |
| [[Hard Limit]] | 500 contracts | −$120,000 |

The strategy builds to 410 contracts long. Soft limit triggers. A Slack alert goes to the head trader and risk manager. The trader scales down to 350 contracts over 20 minutes using limit orders, achieving average [[Slippage]] of 0.2 ticks/contract. Total slippage cost: 60 × 0.2 × $10 = $120. Orderly de-risk vs $75,000 if the hard limit had triggered the kill switch into 500 market orders.

**Simplified:** A soft limit is the warning bell. It does not stop trading; it tells the human to start cutting. The gap between soft and hard is the buffer the trader has to fix things. Set the soft limit too close to the hard limit and there is no time to act. Set it too far and the trader stops doing anything useful. Multi-tier setups (warning at 50%, urgent at 75%, hard stop at 100%) match risk response to severity.

## Key mechanics and formulas
**Soft limit as fraction:**
L_soft = α × L_hard
α is 0.6 to 0.8. For L_hard = 500 contracts, L_soft = 0.75 × 500 = 375 contracts.

**Buffer zone:** L_hard − L_soft is the operational buffer. It must be large enough to allow orderly de-risking given [[Liquidity Risk]].

**Escalation protocol (typical):**
1. Soft limit breach → automated alert to trader and risk desk
2. Trader has T minutes (e.g., 15) to bring exposure below soft limit
3. If exposure rises further, risk desk intervenes
4. [[Hard Limit]] breach → automatic [[Kill Switch]]

## Prerequisites
- [[Hard Limit]]
- [[Position Limit]]
- [[Daily Loss Limit]]

## Related concepts (learn next)
- [[Hard Limit]] — absolute threshold where the system forces a stop.
- [[Kill Switch]] — enforcement mechanism activated when the hard limit breaches.
- [[Position Limit]] — soft limits apply to position size, P&L, and [[Value at Risk]].
- [[Liquidity Risk]] — the reason soft limits exist: illiquid markets need time to de-risk.
- [[Slippage]] — cost savings from orderly soft limit de-risking vs forced hard limit liquidation.
- [[Inventory Risk]] — for market makers, soft limits on inventory trigger quote skewing before a forced shutdown.
- [[Maximum Drawdown]] — soft limits can be set on cumulative drawdown across days.

## Common misconceptions
1. **"Soft limits are optional guidelines."** They do not auto shutdown, but ignoring them is a terminable offense at most firms. Enforced through human accountability and escalation.
2. **"One tier is enough."** Many firms use multiple: 50% warning, 75% urgent, 100% hard. Each tier has a more aggressive response protocol.
3. **"Soft should be as close to hard as possible to maximize trading room."** If too close, there is no time to de-risk before the kill switch. The whole point is providing a buffer for orderly reduction.

## Sources
- FIA. "Recommended Risk Controls for Trading Firms." fia.org.
- CME Group. "Globex Credit Controls." cmegroup.com.
- Narang, R. (2013). *Inside the Black Box*. Wiley.
