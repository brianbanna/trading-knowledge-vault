---
aliases: [soft limit, warning limit, advisory limit, yellow light]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Soft Limit

## Definition
A soft limit is a warning threshold set below the [[Hard Limit]] that alerts the trader to reduce exposure voluntarily. When a soft limit is breached, the system does not force a shutdown, but it notifies the trader and risk manager that the position or loss is approaching dangerous territory. Soft limits are the yellow traffic light of risk management. They give the trader time to de-risk in an orderly way rather than being forced into a fire sale at the hard limit. Typical soft limits are set at 60% to 80% of the corresponding hard limit.

## Why it matters (commodities and FX)
In commodities, liquidating a large position in an illiquid contract (e.g., [[Cocoa]] back months or [[Palladium]] futures) takes time. If the first warning a trader gets is the [[Hard Limit]] triggering a [[Kill Switch]], the forced liquidation will happen at the worst possible prices with maximum [[Slippage]]. The soft limit gives advance warning so the trader can begin unwinding in an orderly fashion, perhaps hedging in a more liquid correlated instrument first. In FX, a spot [[EURUSD]] trader who hits a soft limit on their $200 million position can start reducing through natural client flow rather than dumping $200 million into the market in 1 clip, which would move the price 2 to 3 pips against them.

## Concrete example
A prop trading firm runs a [[Gold]] futures strategy on COMEX. The risk limits are structured in layers:

| Limit type | Position | PnL |
|---|---|---|
| [[Soft Limit]] | 400 contracts | -$80,000 |
| [[Hard Limit]] | 500 contracts | -$120,000 |

**Win scenario:** The strategy builds to 410 contracts long. The soft limit triggers. A Slack alert goes to the head trader and the risk manager. The trader reviews the position and decides to scale down to 350 contracts over the next 20 minutes using limit orders, achieving average [[Slippage]] of 0.2 ticks per contract. Total slippage cost: 60 x 0.2 x $10 = $120. Orderly de-risk.

**Fail scenario (no soft limit):** The strategy builds to 500 contracts. The hard limit triggers immediately with no warning. The [[Kill Switch]] cancels all quotes and sends 500 market orders to flatten. In the 3 seconds it takes to fill, gold drops $1.50. Slippage: 500 x 15 ticks x $10 = $75,000. The forced liquidation itself causes more damage than the original loss.

## Key mechanics and formulas
**Soft limit as fraction of hard limit:**
L_soft = α x L_hard
Where α is typically 0.6 to 0.8. For position limits, if L_hard = 500 contracts, L_soft = 0.75 x 500 = 375 contracts.

**Buffer zone:** The gap between soft and hard limits (L_hard - L_soft) represents the operational buffer. It should be large enough to allow orderly de-risking given the instrument's [[Liquidity Risk]] profile.

**Escalation protocol (typical):**
1. Soft limit breach → automated alert to trader and risk desk
2. Trader has T minutes (e.g., 15) to bring exposure below soft limit
3. If exposure increases beyond soft limit, risk desk intervenes
4. [[Hard Limit]] breach → automatic [[Kill Switch]]

## Prerequisites
- [[Hard Limit]]
- [[Position Limit]]
- [[Daily Loss Limit]]

## Related concepts (learn next)
- [[Hard Limit]] — the absolute threshold where the system forces a stop, the red light that follows the yellow.
- [[Kill Switch]] — the enforcement mechanism that activates when the hard limit is breached.
- [[Position Limit]] — soft limits are commonly applied to position size, PnL, and [[Value at Risk]].
- [[Liquidity Risk]] — the reason soft limits exist: illiquid markets need more time to de-risk.
- [[Slippage]] — the cost savings from orderly soft limit de-risking vs forced hard limit liquidation.
- [[Inventory Risk]] — for market makers, soft limits on inventory trigger quote skewing before a forced shutdown.
- [[Maximum Drawdown]] — soft limits can also be set on cumulative drawdown across multiple days.

## Common misconceptions
1. **"Soft limits are optional guidelines."** While soft limits do not trigger automatic shutdown, ignoring them is a terminable offense at most firms. They are enforced through human accountability and escalation procedures.
2. **"One soft limit level is enough."** Many firms use multiple tiers: a first warning at 50% of the hard limit, a second at 75%, and the hard limit at 100%. Each tier has a more aggressive response protocol.
3. **"Soft limits should be as close to hard limits as possible to maximize trading room."** If the soft limit is too close to the hard limit, there is no time to de-risk before the kill switch triggers. The whole point is to provide an adequate buffer for orderly risk reduction.

## Sources
- FIA. "Recommended Risk Controls for Trading Firms." fia.org.
- CME Group. "Globex Credit Controls." cmegroup.com.
- Narang, R. (2013). *Inside the Black Box*. Wiley.
