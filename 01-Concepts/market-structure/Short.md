---
aliases: [short, short position, going short, sold short]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Short

## Definition
Being short means you owe the asset and profit if its price goes down. You sell something you do not currently own (or sell from inventory you intend to replace), then buy it back cheaper later. In FX, "short EUR/USD" means you sold euros and bought dollars, profiting if the euro weakens. In commodities, a producer selling [[Futures Contract]]s to lock in a price is going short. Your [[PnL]] is positive when the market drops and negative when it rises.

## Why it matters (commodities and FX)
Short selling is how hedgers protect themselves and how speculators bet on declines. A copper miner sells (goes short) LME copper futures to lock in revenue, hedging against a price drop before the metal is produced and delivered. In FX, going short a [[Currency Pair]] is as natural as going [[Long]], there is no asymmetry or special borrowing cost because you are simply selling one currency and buying another. Understanding the short side is essential because markets fall faster than they rise, and crowded short positions can create violent [[Short Squeeze]]s when shorts are forced to buy back.

## Concrete example
**Win scenario:** You believe the Australian dollar will weaken on falling iron ore prices. You go short 5 million AUD/USD at 0.6700. Iron ore drops 8% over 2 weeks and AUD/USD falls to 0.6550. Your [[PnL]] = 5,000,000 x (0.6700 minus 0.6550) = 5,000,000 x 0.0150 = 75,000 USD. You buy back (cover) the short and book [[Realized PnL]] of 75,000 USD.

**Fail scenario:** You go short 200 lots of natural gas futures (contract size: 10,000 MMBtu each) at 2.80 USD/MMBtu heading into winter. A polar vortex hits and natural gas spikes to 3.60. Your [[Unrealized PnL]] = 200 x 10,000 x (2.80 minus 3.60) = negative 1,600,000 USD. [[Margin]] calls force you to cover at 3.50 for a [[Realized PnL]] of negative 1,400,000 USD. Commodity shorts during supply shocks are among the most dangerous positions in trading.

## Key mechanics and formulas
- Short PnL = Quantity x (Entry Price minus Exit Price)
  - Quantity: number of units or [[Notional]]
  - Entry Price: the price at which you sold short
  - Exit Price: the price at which you buy back (cover)
- Short breakeven = Entry Price minus Transaction costs
- Maximum gain on a short = Entry Price x Quantity (if the asset goes to 0)
- Maximum loss on a short = theoretically unlimited (price can rise indefinitely)

## Prerequisites
- [[Position]]
- [[Long]]
- [[Notional]]
- [[Futures Contract]]

## Related concepts (learn next)
- [[Long]] , the opposite direction, profiting from price increases
- [[Flat]] , having no directional exposure
- [[Short Squeeze]] , when forced buying by shorts drives the price higher
- [[Stop Loss]] , placed above your entry to limit losses on a short
- [[Margin]] , particularly important for shorts because losses are theoretically unlimited
- [[Carry Trade]] , where shorting a low yield currency funds the long
- [[Delivery]] , the risk of being assigned physical delivery on a short futures position

## Common misconceptions
- **Shorting in FX has no borrowing cost.** Unlike equities, where you must borrow shares and pay a fee, FX shorts simply involve selling one currency and buying another. The cost or benefit comes from the [[Interest Rate Differential]], not a borrow fee.
- **Short does not mean bearish on the entire market.** Being short EUR/USD means bearish on EUR relative to USD. If USD weakens against everything else, your short might still lose.
- **Maximum loss is not capped at your margin.** If the market gaps up violently (weekend gap, news event), your loss can exceed the margin deposited. This is why risk managers monitor gross short exposure carefully.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 1
- CME Group, "Understanding Short Selling in Futures"
- Einhorn, D. *Fooling Some of the People All of the Time* (short selling case study)
