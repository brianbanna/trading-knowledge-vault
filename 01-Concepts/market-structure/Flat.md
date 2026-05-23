---
aliases: [flat, flat position, square, no position]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Flat

## Definition
Flat means you have no [[Position]]. Neither [[Long]] nor [[Short]]. "I'm flat EUR/USD" means zero exposure to that [[Currency Pair]]. Going flat is closing out an existing position entirely. On a desk, "squaring up" or "getting flat" before the weekend or a major event is standard practice. Being flat is a decision: choosing not to have risk on.

## Why it matters (commodities and FX)
In FX and commodities, the choice to be flat is as important as choosing to go [[Long]] or [[Short]]. Before major releases (NFP, CPI, OPEC meetings), many traders go flat to avoid binary risk. 24 hour FX desks must decide at handover whether to carry or go flat. Commodity traders with physical exposure are rarely truly flat because they hold inventory, but can be flat on a delta adjusted basis. Knowing when to be flat separates disciplined traders from gamblers.

## Concrete example

**Concrete:** [[Long]] USD 3 million USD/JPY at 149.50, up 30 pips. BOJ meeting tomorrow with intervention risk. Close at 149.80 and go flat, locking in 3,000,000 × 0.0030 / 149.80 = ~$60,000. Overnight, BOJ intervenes; USD/JPY drops 300 pips to 146.80. Being flat saved a $600,000 loss. Failure mirror: go flat on crude before an OPEC meeting, closing [[Long]] 50 lots at $80.00. OPEC announces a surprise 2 mbpd cut, oil gaps to $85.00 at the open. Missed $250,000 of profit. Flat protected downside but eliminated upside.

**Simplified:** Flat means no position. Going flat closes whatever you held and removes you from the market. Traders go flat before major news to avoid binary outcomes, or at end of day to sleep without overnight risk. It is not a passive state, it is an active decision to not have a view at the moment.

## Key mechanics and formulas
- Flat position value = 0
- Flat PnL exposure = 0 (no gain or loss from market moves)
- To go flat from [[Long]]: sell the entire position
- To go flat from [[Short]]: buy back the entire position
- Transaction cost of going flat = [[Bid-Ask Spread]] × [[Notional]] + commissions

## Prerequisites
- [[Position]]
- [[Long]]
- [[Short]]

## Related concepts (learn next)
- [[Position]] , the holding you eliminate when going flat
- [[Realized PnL]] , booked when you close to go flat
- [[Risk Management]] , where going flat is a key tool
- [[Margin]] , freed up when you go flat
- [[Bid-Ask Spread]] , the cost you pay to close
- [[Hedging]] , an alternative that offsets risk without closing

## Common misconceptions

**Flat does not mean safe.** If your mandate requires a hedge, flat means actually exposed. A commodity producer with no futures hedge is not safe; they are exposed to falling prices.

**Flat book does not mean flat risk.** Offsetting [[Long]] and [[Short]] positions in correlated instruments (long Brent, short WTI) net to flat notional but carry significant [[Basis Risk]].

**Going flat always costs money.** Crossing the [[Bid-Ask Spread]] to close is a real cost. Repeatedly going flat and re entering erodes PnL through transaction costs.

## Sources
- Taleb, N.N. *Dynamic Hedging*, Chapter 1
- CME Group, "Position Management Best Practices"
- Schwager, J. *Market Wizards* (multiple interviews on the discipline of being flat)
