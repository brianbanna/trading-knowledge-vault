---
aliases: [short, short position, going short, sold short]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Short

## Definition
Being short means you owe the asset and profit if its price falls. You sell something you do not currently own (or from inventory you intend to replace), then buy it back cheaper. "Short EUR/USD" means you sold euros and bought dollars, profiting if EUR weakens. A producer selling [[Futures Contract]]s to lock in a price is going short. [[PnL]] is positive when the market drops and negative when it rises.

## Why it matters (commodities and FX)
Short selling is how hedgers protect themselves and how speculators bet on declines. A copper miner sells (shorts) LME futures to lock revenue, hedging a drop before delivery. In FX, shorting a [[Currency Pair]] is as natural as going [[Long]]: no asymmetry or borrow cost because you simply sell one currency and buy another. The short side matters because markets fall faster than they rise, and crowded shorts can trigger violent [[Short Squeeze]]s when shorts are forced to cover.

## Concrete example

**Concrete:** You believe the AUD weakens on falling iron ore. Short 5M AUD/USD at 0.6700. Iron ore drops 8% over 2 weeks, AUD/USD falls to 0.6550. [[PnL]] = 5,000,000 × 0.0150 = 75,000 USD. You cover and book [[Realized PnL]] of 75,000 USD. Adverse case: short 200 lots of nat gas (10,000 MMBtu each) at 2.80 USD/MMBtu into winter. Polar vortex hits, gas spikes to 3.60. [[Unrealized PnL]] = 200 × 10,000 × (2.80 minus 3.60) = -1,600,000 USD. [[Margin]] calls force cover at 3.50 for [[Realized PnL]] of -1,400,000 USD. Commodity shorts into supply shocks are among the most dangerous trades.

**Simplified:** Short = you bet against it. Sell first, buy back cheaper later. If the price drops, you make money. If it rises, you lose. Upside is capped (price cannot go below zero), downside is theoretically unlimited because price can rally forever. That asymmetry is why shorts blow up more often than longs.

## Key mechanics and formulas
- Short PnL = Quantity × (Entry Price minus Exit Price)
  - Quantity: number of units or [[Notional]]
  - Entry Price: price at which you sold short
  - Exit Price: price at which you cover
- Short breakeven = Entry Price minus Transaction costs
- Maximum gain on a short = Entry Price × Quantity (if asset goes to zero)
- Maximum loss on a short = theoretically unlimited

## Prerequisites
- [[Position]]
- [[Long]]
- [[Notional]]
- [[Futures Contract]]

## Related concepts (learn next)
- [[Long]], the opposite direction, profits from rises
- [[Flat]], no directional exposure
- [[Short Squeeze]], forced buying by shorts drives price higher
- [[Stop Loss]], placed above entry to limit losses on a short
- [[Margin]], critical because losses are theoretically unlimited
- [[Carry Trade]], shorting low yielders funds the long
- [[Delivery]], the risk of physical delivery assignment on a short futures position

## Common misconceptions
- **Shorting FX has no borrow cost.** Unlike equities (borrow fee on shares), FX shorts just sell one currency and buy another. Cost or benefit comes from [[Interest Rate Differential]], not borrow.
- **Short does not mean bearish on the whole market.** Short EUR/USD is bearish EUR vs USD. If USD weakens against everything else, your short can still lose.
- **Maximum loss is not capped at margin.** Weekend gaps and news events can push losses past the margin. Risk managers track gross short exposure for exactly this reason.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 1
- CME Group, "Understanding Short Selling in Futures"
- Einhorn, D. *Fooling Some of the People All of the Time* (short selling case study)
