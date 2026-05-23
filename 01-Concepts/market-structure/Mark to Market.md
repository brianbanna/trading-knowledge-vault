---
aliases: [mark to market, MTM, marking to market, daily settlement]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Mark to Market

## Definition
Mark to market is the process of revaluing your [[Position]] at the current market price rather than the original trade price. Long 10 lots of crude at 80 USD with the market at 82 USD gives MTM [[PnL]] of +20,000 USD (10 × 1,000 × 2). This revaluation happens daily on futures exchanges: gains credited, losses debited from your [[Margin]] account. It forces real time [[PnL]] recognition rather than waiting until the trade closes.

## Why it matters (commodities and FX)
Daily MTM is what stops credit risk from accumulating in futures markets. Each day at settlement the exchange calculates every participant's MTM PnL. Winners receive cash, losers pay. This is why futures need [[Margin]]: if MTM loss exceeds maintenance margin, you get a margin call and must post more cash or be liquidated. In FX, banks and prime brokers handle MTM internally for bilateral trades. For physical commodity traders, marking inventory to market drives hedging decisions and reveals true business value.

## Concrete example

**Concrete:** You go [[Long]] 20 lots of LME aluminum at 2,300 USD/tonne on Monday (25 tonnes per lot). Tuesday settlement is 2,340. Daily MTM = 20 × 25 × 40 = 20,000 USD credited. Wednesday settles at 2,370: another 20 × 25 × 30 = 15,000 USD credited. You close Wednesday and the cumulative 35,000 USD matches [[Realized PnL]]. Failure case: long 100 lots of WTI at 75.00 Friday. Over the weekend tensions ease, Monday settles at 72.00. MTM loss = 100 × 1,000 × 3.00 = 300,000 USD debited. Margin falls below maintenance, broker issues a call Tuesday. Cannot post: forced liquidation at whatever the [[Market Order]] gets, often worse via [[Slippage]].

**Simplified:** Every day the exchange asks "what is your position worth right now?" If it went up, cash hits your account. If it went down, cash leaves. Settled daily, not at trade close. That is why a losing futures position bleeds you every night until you close it or top up margin.

## Key mechanics and formulas
- Daily MTM PnL = Position Size × (Today's Settlement minus Yesterday's Settlement)
  - Position Size: contracts × multiplier
  - Settlement Price: official exchange close
- Cumulative MTM PnL = Position Size × (Today's Settlement minus Original Entry)
- Margin call trigger: Account equity < Maintenance margin
  - Account equity = Initial margin + Cumulative MTM PnL
- Variation margin = cash flow from daily MTM settlement (positive or negative)

## Prerequisites
- [[Position]]
- [[PnL]]
- [[Futures Contract]]
- [[Notional]]

## Related concepts (learn next)
- [[Realized PnL]], the final MTM at position close
- [[Unrealized PnL]], equals current MTM gain or loss on open positions
- [[Margin]], the collateral account absorbing daily MTM
- [[Settlement Price]], official price used for MTM
- [[Variation Margin]], daily cash flow from marking to market
- [[Liquidity]], which affects whether settlement reflects real exit value
- [[Cash Settlement]], where final MTM at expiry replaces physical delivery

## Common misconceptions
- **MTM gains are real cash, not accounting.** On futures, daily settlement means actual money moves between accounts. Not hypothetical.
- **MTM does not mean you closed the trade.** The position stays open. MTM resets your effective entry to today's settlement; tomorrow's PnL is calculated from there.
- **Illiquid markets make MTM unreliable.** If an instrument trades rarely, the last price may not reflect real exit price. Big issue for exotic commodities and [[EM Currencies]] under stress.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- CME Group, "Daily Settlement Process"
- McDonald, R. *Derivatives Markets*, 3rd ed., Chapter 5
