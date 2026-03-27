---
aliases: [long, long position, going long, bought]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Long

## Definition
Being long means you own the asset and profit if its price goes up. In FX, "long EUR/USD" means you bought euros and sold dollars, so you want the euro to strengthen. In commodities, "long 10 lots of WTI" means you bought 10 [[Futures Contract]]s and profit if crude oil rises. Going long is the most intuitive direction: buy low, sell high. Your [[PnL]] is positive when the market moves in your favor (up) and negative when it moves against you (down).

## Why it matters (commodities and FX)
Understanding "long" precisely prevents confusion in every conversation on a trading floor. In FX, a [[Currency Pair]] has 2 sides, so being long EUR/USD automatically means being [[Short]] USD/EUR. In commodities, physical traders are naturally long inventory (they hold barrels, tonnes, or bushels) and use [[Futures Contract]]s to hedge by going [[Short]]. Knowing who is long and who is [[Short]] in a market tells you where the pressure sits. When too many participants are long, a price drop can trigger forced selling as [[Stop Loss]] orders cascade.

## Concrete example
**Win scenario:** You go long 2 million GBP/USD at 1.2600 because you expect the Bank of England to sound hawkish. The rate rallies to 1.2680 after the announcement. Your [[PnL]] = 2,000,000 x (1.2680 minus 1.2600) = 2,000,000 x 0.0080 = 16,000 USD. You close the [[Position]] and book [[Realized PnL]] of 16,000 USD.

**Fail scenario:** You go long 100 lots of Brent crude (100,000 barrels) at 82.00 USD per barrel. OPEC announces a surprise production increase. Brent drops to 78.50. Your [[Unrealized PnL]] = 100,000 x (78.50 minus 82.00) = negative 350,000 USD. Your [[Stop Loss]] at 79.00 should have triggered but [[Slippage]] caused your [[Fill]] at 78.80, making the [[Realized PnL]] even worse: negative 320,000 USD.

## Key mechanics and formulas
- Long PnL = Quantity x (Exit Price minus Entry Price)
  - Quantity: number of units or [[Notional]]
  - Exit Price: the price at which you close or the current [[Mark to Market]] price
  - Entry Price: the price at which you entered the long
- Long breakeven = Entry Price + Transaction costs (spread + commissions)
- Maximum loss on a long = Entry Price x Quantity (if the asset goes to 0)
- Maximum gain on a long = theoretically unlimited (price can rise indefinitely)

## Prerequisites
- [[Position]]
- [[Notional]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Short]] , the opposite direction, profiting from price declines
- [[Flat]] , having no directional exposure
- [[PnL]] , the profit or loss from being long
- [[Stop Loss]] , the order used to limit losses on a long position
- [[Margin]] , the collateral required to hold a long futures position
- [[Carry Trade]] , a common reason to go long a high yielding currency
- [[Market Order]] , one way to enter a long position immediately

## Common misconceptions
- **Long does not mean bullish on everything.** Being long EUR/USD means bullish on EUR but simultaneously bearish on USD. Always specify which leg you are long.
- **Being long futures does not mean you own the physical commodity.** You own a contract that obligates you to buy at expiry. Most futures longs are closed before [[Delivery]].
- **A long position can lose more than 100% in rare cases.** If you are long a [[Futures Contract]] on margin and the price gaps below zero (as WTI did in April 2020), losses can exceed the initial investment.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 1
- CME Group, "Introduction to Futures"
- Schwager, J. *Market Wizards*, interviews on position management
