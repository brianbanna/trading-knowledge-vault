---
aliases: [long, long position, going long, bought]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Long

## Definition
Being long means you own the asset and profit if its price rises. "Long EUR/USD" means you bought euros and sold dollars; you want EUR to strengthen. "Long 10 lots of WTI" means you bought 10 [[Futures Contract]]s and profit if crude rises. Buy low, sell high. [[PnL]] is positive on up moves, negative on down moves.

## Why it matters (commodities and FX)
Precision on "long" prevents confusion on a trading floor. In FX, a [[Currency Pair]] has 2 sides, so long EUR/USD is automatically [[Short]] USD/EUR. In commodities, physical traders are naturally long inventory (barrels, tonnes, bushels) and use [[Futures Contract]]s to hedge by going [[Short]]. Knowing who is long and who is [[Short]] shows where the pressure sits. Over crowded longs make a price drop self reinforcing as [[Stop Loss]] orders cascade.

## Concrete example

**Concrete:** You go long 2M GBP/USD at 1.2600 expecting a hawkish BoE. After the meeting, the rate rallies to 1.2680. [[PnL]] = 2,000,000 × 0.0080 = 16,000 USD. You close and book [[Realized PnL]] of 16,000 USD. Different trade: you go long 100 lots of Brent (100,000 bbl) at 82.00 USD/bbl. OPEC surprises with a production increase. Brent drops to 78.50. [[Unrealized PnL]] = 100,000 × (78.50 minus 82.00) = negative 350,000 USD. Your [[Stop Loss]] at 79.00 should trigger but [[Slippage]] fills at 78.80, locking in a 320,000 USD loss instead of the planned 300,000.

**Simplified:** Long = you own it, you want it up. The simplest direction. If price goes up, you make money equal to (size × move). If it goes down, you lose the same way. Most retail trading starts here because it matches how people think about owning stocks or houses.

## Key mechanics and formulas
- Long PnL = Quantity × (Exit Price minus Entry Price)
  - Quantity: number of units or [[Notional]]
  - Exit Price: closing price or current [[Mark to Market]]
  - Entry Price: price at which you entered
- Long breakeven = Entry Price + Transaction costs (spread + commissions)
- Maximum loss on a long = Entry Price × Quantity (if the asset goes to zero)
- Maximum gain on a long = theoretically unlimited

## Prerequisites
- [[Position]]
- [[Notional]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Short]], the opposite direction, profiting from declines
- [[Flat]], no directional exposure
- [[PnL]], the profit or loss from being long
- [[Stop Loss]], the order limiting losses on a long
- [[Margin]], collateral required to hold a long futures position
- [[Carry Trade]], a common reason to go long a high yielder
- [[Market Order]], one way to enter a long immediately

## Common misconceptions
- **Long is not bullish on everything.** Long EUR/USD is bullish EUR and bearish USD simultaneously. Always specify the leg.
- **Long futures does not mean owning the physical commodity.** You own a contract obligating you to buy at expiry. Most longs close before [[Delivery]].
- **A long can lose more than 100% in rare cases.** If you are long a [[Futures Contract]] on margin and the price gaps below zero (WTI April 2020), losses exceed initial investment.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 1
- CME Group, "Introduction to Futures"
- Schwager, J. *Market Wizards*, interviews on position management
