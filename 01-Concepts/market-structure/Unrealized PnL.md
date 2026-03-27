---
aliases: [unrealized PnL, paper profit, paper loss, open PnL, floating PnL]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Unrealized PnL

## Definition
Unrealized PnL is the profit or loss on [[Position]]s you still hold. It is calculated by [[Mark to Market]], comparing your entry price to the current market price. If you are [[Long]] gold at 2,000 and gold is now at 2,030, your unrealized PnL is positive 30 USD per ounce. It is called "unrealized" because nothing is locked in. The number changes with every tick. It only becomes [[Realized PnL]] when you close the trade. Until then, it is profit or loss on paper.

## Why it matters (commodities and FX)
Unrealized PnL determines your current risk exposure and margin status. A large unrealized loss can trigger [[Margin]] calls, forcing you to either deposit more cash or close the [[Position]] at unfavorable prices. In FX, unrealized PnL on open positions is continuously monitored and reported. In commodities, physical traders mark their inventory to market daily, and the unrealized PnL on that inventory drives hedging decisions. Ignoring unrealized losses ("it will come back") is one of the most common and dangerous behaviors in trading.

## Concrete example
**Win scenario:** You are [[Long]] 10 million USD/CHF at 0.8750 as a swing trade. Over 5 days, the pair drifts to 0.8820. Your unrealized PnL = 10,000,000 x (0.8820 minus 0.8750) = 70,000 CHF (approximately 79,500 USD at current rates). You decide to hold because your target is 0.8900. The unrealized gain gives you a cushion, meaning you can tighten your [[Stop Loss]] to lock in some of the profit.

**Fail scenario:** You are [[Short]] 200 lots of cocoa at 8,000 USD per tonne. Cocoa rallies to 9,200 on supply fears. Your unrealized PnL = 200 x 10 x (8,000 minus 9,200) = negative 2,400,000 USD. You face a margin call of 1,200,000 USD. You cannot meet it, so the broker liquidates 100 lots at 9,250 via [[Market Order]], converting 1,250,000 USD of unrealized loss into [[Realized PnL]]. The remaining 100 lot [[Short]] continues to show negative 1,250,000 USD unrealized.

## Key mechanics and formulas
- Unrealized PnL (long) = Quantity x (Current Price minus Entry Price)
- Unrealized PnL (short) = Quantity x (Entry Price minus Current Price)
- Total portfolio unrealized PnL = Sum of unrealized PnL across all open [[Position]]s
- Equity = Cash balance + [[Realized PnL]] + Unrealized PnL
- Margin ratio = Equity / Margin requirement
  - If margin ratio falls below maintenance level, a margin call is triggered
- Unrealized PnL becomes realized at the moment of trade closure

## Prerequisites
- [[PnL]]
- [[Position]]
- [[Mark to Market]]
- [[Long]]
- [[Short]]

## Related concepts (learn next)
- [[Realized PnL]] , the locked in PnL from closed trades
- [[Mark to Market]] , the process that calculates unrealized PnL
- [[Margin]] , which is affected by unrealized PnL levels
- [[Stop Loss]] , used to convert unrealized losses into smaller realized losses
- [[Drawdown]] , which measures the decline from peak equity including unrealized
- [[Position]] , the open holding that generates unrealized PnL
- [[Liquidity]] , which determines whether unrealized PnL can actually be realized at the quoted price

## Common misconceptions
- **"It's only a loss if I sell" is dangerous.** Unrealized losses are real. They consume margin, reduce your ability to take new trades, and can force liquidation. Treating them as imaginary leads to catastrophic drawdowns.
- **Unrealized PnL can disappear instantly.** A 100,000 USD unrealized gain can become a 50,000 USD loss in minutes during a news event. It is not "money in the bank" until you close the trade and convert it to [[Realized PnL]].
- **Unrealized PnL in futures is partly realized daily.** Because of daily [[Mark to Market]] settlement on exchanges, unrealized PnL in futures is actually settled in cash each day. The distinction between realized and unrealized is cleaner in OTC products like [[FX Swap]]s.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- Taleb, N.N. *Dynamic Hedging*, Chapters 1 and 7
- CME Group, "Marking to Market and Daily Settlement"
