---
aliases: [mark to market, MTM, marking to market, daily settlement]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Mark to Market

## Definition
Mark to market is the process of revaluing your [[Position]] at the current market price, rather than the price you originally traded at. If you are [[Long]] 10 lots of crude at 80 USD and the market is now at 82 USD, your mark to market [[PnL]] is positive 20,000 USD (10 x 1,000 x 2). This revaluation happens daily on futures exchanges, where gains are credited and losses are debited from your [[Margin]] account. It ensures that [[PnL]] is recognized in real time, not just when the trade closes.

## Why it matters (commodities and FX)
Daily mark to market is the mechanism that prevents credit risk from building up in futures markets. Every day at settlement, the exchange calculates each participant's MTM PnL. Winners receive cash, losers pay cash. This is why futures require [[Margin]]: if your mark to market loss exceeds your maintenance margin, you get a margin call and must post more cash or face forced liquidation. In FX, mark to market is done internally by banks and prime brokers for bilateral trades. For commodities traders holding physical inventory, marking inventory to market determines the value of the business and drives hedging decisions.

## Concrete example
**Win scenario:** You go [[Long]] 20 lots of LME aluminum at 2,300 USD per tonne on Monday (each lot = 25 tonnes). Tuesday's settlement price is 2,340. Your daily MTM [[PnL]] = 20 x 25 x (2,340 minus 2,300) = 20,000 USD. This cash is credited to your margin account. Wednesday, aluminum settles at 2,370. Another 20 x 25 x 30 = 15,000 USD credited. You close on Wednesday, and your cumulative MTM gain of 35,000 USD matches your [[Realized PnL]].

**Fail scenario:** You go [[Long]] 100 lots of WTI crude at 75.00 on a Friday. Over the weekend, geopolitical tensions ease and Monday's settlement is 72.00. Your MTM loss = 100 x 1,000 x (72.00 minus 75.00) = negative 300,000 USD. This is debited from your margin account. If your margin falls below the maintenance level, the broker issues a margin call by Tuesday morning. If you cannot post additional funds, your [[Position]] is liquidated at whatever price is available via [[Market Order]], which could be even worse due to [[Slippage]].

## Key mechanics and formulas
- Daily MTM PnL = Position Size x (Today's Settlement Price minus Yesterday's Settlement Price)
  - Position Size: number of units (contracts x multiplier)
  - Settlement Price: the official closing price set by the exchange
- Cumulative MTM PnL = Position Size x (Today's Settlement Price minus Original Entry Price)
- Margin call trigger: Account equity < Maintenance margin requirement
  - Account equity = Initial margin + Cumulative MTM PnL
- Variation margin = Cash flow from daily MTM settlement (positive or negative)

## Prerequisites
- [[Position]]
- [[PnL]]
- [[Futures Contract]]
- [[Notional]]

## Related concepts (learn next)
- [[Realized PnL]] , which is the final MTM when the position is closed
- [[Unrealized PnL]] , which equals the current MTM gain or loss on open positions
- [[Margin]] , the collateral account that absorbs daily MTM gains and losses
- [[Settlement Price]] , the official price used for daily MTM calculations
- [[Variation Margin]] , the daily cash flow from marking to market
- [[Liquidity]] , which affects whether settlement prices reflect true market value
- [[Cash Settlement]] , where the final MTM at expiry replaces physical delivery

## Common misconceptions
- **MTM gains are real cash, not just accounting.** On futures exchanges, daily settlement means actual money moves between accounts. This is not a hypothetical revaluation.
- **MTM does not mean you closed the trade.** Your [[Position]] is still open. The MTM process resets your effective entry price to today's settlement, so tomorrow's PnL is calculated from today's close.
- **Illiquid markets make MTM unreliable.** If an instrument trades infrequently, the last traded price may not reflect where you could actually exit. This is a major issue for exotic commodities and [[EM Currencies]] during stress periods.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- CME Group, "Daily Settlement Process"
- McDonald, R. *Derivatives Markets*, 3rd ed., Chapter 5
