---
aliases: [flat, flat position, square, no position]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Flat

## Definition
Flat means you have no [[Position]]. You are neither [[Long]] nor [[Short]] in a given instrument. "I'm flat EUR/USD" means you have zero exposure to that [[Currency Pair]]. Going flat is the act of closing out an existing position entirely. On a trading desk, "squaring up" or "getting flat" before the weekend or a major event is common practice. Being flat is itself a decision, choosing not to have risk on.

## Why it matters (commodities and FX)
In FX and commodities, the decision to be flat is as important as the decision to be [[Long]] or [[Short]]. Before major data releases (NFP, CPI, OPEC meetings), many traders go flat to avoid the binary risk of a surprise outcome. FX desks that run 24 hour books must decide at handover whether to carry positions or go flat. Commodities traders with physical exposure are almost never truly flat because they hold inventory, but they can be flat on a delta adjusted, hedged basis. Knowing when to be flat, rather than always having a position, separates disciplined traders from gamblers.

## Concrete example
**Win scenario (flat saves you):** You were [[Long]] 3 million USD/JPY at 149.50, up 30 [[Pip]]s. The Bank of Japan meeting is tomorrow and you suspect intervention risk. You close the position at 149.80 and go flat, locking in [[Realized PnL]] of 3,000,000 x 0.0030 / 149.80 = approximately 60,000 USD. Overnight, the BOJ intervenes and USD/JPY drops 300 pips to 146.80. Being flat saved you from a 600,000 USD loss.

**Fail scenario (flat costs you):** You go flat on crude oil before an OPEC meeting, closing your [[Long]] 50 lots at 80.00. OPEC announces a surprise 2 million barrel per day cut and oil gaps to 85.00 at the open. You missed 50 x 1,000 x 5.00 = 250,000 USD of profit. Being flat protected your downside but also eliminated your upside.

## Key mechanics and formulas
- Flat position value = 0
- Flat PnL exposure = 0 (no gain or loss from market moves)
- To go flat from [[Long]]: sell the entire position (quantity sold = quantity held)
- To go flat from [[Short]]: buy back the entire position (quantity bought = quantity owed)
- Transaction cost of going flat = [[Bid-Ask Spread]] x [[Notional]] + commissions

## Prerequisites
- [[Position]]
- [[Long]]
- [[Short]]

## Related concepts (learn next)
- [[Position]] , the holding that you eliminate when going flat
- [[Realized PnL]] , which is booked when you close a position to go flat
- [[Risk Management]] , where going flat is a key tool for reducing exposure
- [[Margin]] , which is freed up when you go flat
- [[Bid-Ask Spread]] , the cost you pay to close a position and go flat
- [[Hedging]] , an alternative to going flat, where you offset risk without closing

## Common misconceptions
- **Flat does not mean safe.** If you should be [[Long]] because your mandate requires a hedge, being flat means you are actually exposed. A commodity producer with no futures hedge is not "safe," they are exposed to falling prices.
- **Flat book does not mean flat risk.** A trader can have offsetting [[Long]] and [[Short]] positions in correlated instruments (long Brent, short WTI) that net to flat notional but still carry significant [[Basis Risk]].
- **Going flat always costs money.** Crossing the [[Bid-Ask Spread]] to close a position is a real cost. Repeatedly going flat and re entering positions erodes [[PnL]] through transaction costs.

## Sources
- Taleb, N.N. *Dynamic Hedging*, Chapter 1
- CME Group, "Position Management Best Practices"
- Schwager, J. *Market Wizards* (multiple interviews on the discipline of being flat)
