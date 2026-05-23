---
aliases: [unrealized PnL, paper profit, paper loss, open PnL, floating PnL]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Unrealized PnL

## Definition
Unrealized PnL is the profit or loss on [[Position]]s you still hold. Calculated by [[Mark to Market]]: entry price vs current market. Long gold at 2,000 with gold at 2,030 gives unrealized PnL of +30 USD/oz. Called "unrealized" because nothing is locked in. The number changes with every tick. It becomes [[Realized PnL]] only when you close the trade.

## Why it matters (commodities and FX)
Unrealized PnL determines your current risk exposure and margin status. Large unrealized losses trigger [[Margin]] calls, forcing you to deposit more cash or close at unfavorable prices. In FX, unrealized PnL is continuously monitored and reported. In commodities, physical traders mark inventory daily, and unrealized PnL drives hedging decisions. Ignoring unrealized losses ("it will come back") is one of the most common and dangerous trader behaviors.

## Concrete example

**Concrete:** You are [[Long]] 10M USD/CHF at 0.8750 as a swing trade. Over 5 days the pair drifts to 0.8820. Unrealized PnL = 10,000,000 × 0.0070 = 70,000 CHF (~79,500 USD). You hold because target is 0.8900. The unrealized cushion lets you tighten your [[Stop Loss]] to lock some profit. Adverse case: [[Short]] 200 lots cocoa at 8,000 USD/tonne. Cocoa rallies to 9,200 on supply fears. Unrealized PnL = 200 × 10 × -1,200 = -2,400,000 USD. Margin call of 1,200,000 USD. Cannot meet it: broker liquidates 100 lots at 9,250 via [[Market Order]], converting 1,250,000 USD unrealized into [[Realized PnL]]. Remaining 100 lot short continues showing -1,250,000 unrealized.

**Simplified:** Paper profit or loss on positions you have not closed. Changes every tick. Eats margin if you go offside. Becomes real PnL the moment you close. Cannot ignore it: it constrains how much new risk you can take.

## Key mechanics and formulas
- Unrealized PnL (long) = Quantity × (Current Price minus Entry Price)
- Unrealized PnL (short) = Quantity × (Entry Price minus Current Price)
- Total portfolio unrealized PnL = Sum across all open [[Position]]s
- Equity = Cash + [[Realized PnL]] + Unrealized PnL
- Margin ratio = Equity / Margin requirement
  - Below maintenance triggers a margin call
- Unrealized becomes realized at trade closure

## Prerequisites
- [[PnL]]
- [[Position]]
- [[Mark to Market]]
- [[Long]]
- [[Short]]

## Related concepts (learn next)
- [[Realized PnL]], locked in PnL from closed trades
- [[Mark to Market]], the process calculating unrealized PnL
- [[Margin]], affected by unrealized PnL levels
- [[Stop Loss]], used to convert unrealized losses into smaller realized losses
- [[Drawdown]], decline from peak equity including unrealized
- [[Position]], the open holding generating unrealized PnL
- [[Liquidity]], determines whether unrealized PnL can actually be realized at the quoted price

## Common misconceptions
- **"It's only a loss if I sell" is dangerous.** Unrealized losses consume margin, reduce capacity for new trades, and can force liquidation. Treating them as imaginary leads to catastrophic drawdowns.
- **Unrealized PnL disappears instantly.** A 100,000 USD unrealized gain becomes a 50,000 USD loss in minutes during news. Not "money in the bank" until you close and convert to [[Realized PnL]].
- **Unrealized PnL in futures is partly realized daily.** Daily [[Mark to Market]] settlement on exchanges means unrealized PnL in futures is settled in cash each day. The distinction is cleaner in OTC products like [[FX Swap]]s.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- Taleb, N.N. *Dynamic Hedging*, Chapters 1 and 7
- CME Group, "Marking to Market and Daily Settlement"
