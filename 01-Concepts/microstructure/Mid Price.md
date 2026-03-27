---
aliases: [mid price, mid, midpoint, mid market price]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Mid Price

## Definition
The mid price is the arithmetic average of the best [[Bid-Ask Spread|bid]] and best [[Bid-Ask Spread|ask]] currently available in the market. The formula is simply (Bid + Ask) / 2. It serves as a convenient reference point for where the "true" price of an instrument might be, but it is not necessarily the price at which any trade will actually execute. In thin or skewed markets, the mid price can be misleading because the best bid and best ask may sit far apart or carry very different sizes. A market maker uses the mid as a starting anchor and then adjusts quotes around it based on [[Skew Microstructure|skew]], [[Market Impact|market impact]], and inventory risk.

## Why it matters (commodities and FX)
In FX, the mid price is the benchmark against which transaction cost analysis (TCA) measures execution quality. If I buy EUR/USD at 1.10015 and the mid was 1.10010, my cost was 0.5 pips from mid, which equals the [[Half Spread]]. In commodities, the mid of Brent crude futures on ICE at $82.50 / $82.54 would be $82.52. Execution desks report fills relative to mid to judge whether a broker or algorithm is adding or leaking value. Understanding the mid is the first step toward understanding [[Slippage]], [[Markout]], and the economics of [[Market Impact|market making]].

## Concrete example
Brent crude front month is quoted at $82.50 bid, $82.54 offer on ICE. The mid price is ($82.50 + $82.54) / 2 = $82.52.

**Win scenario:** I am a market maker. I buy 10 lots at $82.50 (the bid) and sell 10 lots at $82.54 (the offer). My average entry is at the bid, my average exit is at the offer, so I earned $0.04 per barrel around the mid. On 10 lots of 1000 barrels each, that is 10 x 1000 x $0.04 = $400 in spread capture.

**Fail scenario:** I use mid as my fair value in a fast moving market. The true equilibrium has already shifted to $82.60 because a large buyer swept the offer, but the stale bid at $82.50 has not been cancelled yet. The mid still reads $82.52, which underestimates the real price by $0.08. I sell at $82.54 thinking I am selling above mid, but the market prints $82.62 seconds later. My [[Markout]] is negative $0.08 per barrel. Relying on mid in a moving market exposed me to [[Adverse Selection]].

## Key mechanics and formulas
- **Mid price** = (Best Bid + Best Ask) / 2
  - Best Bid = highest price a buyer is willing to pay, from [[Top of Book]]
  - Best Ask = lowest price a seller is willing to accept, from [[Top of Book]]
- **Micro price** (size weighted mid) = (Bid x Ask Size + Ask x Bid Size) / (Bid Size + Ask Size)
  - This adjusts the mid toward the side with less resting size, giving a better short term fair value estimate
- **Spread** = Ask minus Bid
- Mid is undefined when either side of the [[Depth of Book]] is empty (no bid or no ask)

## Prerequisites
- [[Bid-Ask Spread]]
- [[Top of Book]]
- [[Depth of Book]]

## Related concepts (learn next)
- [[Half Spread]] , the distance from mid to one side of the market, representing single leg cost
- [[Markout]] , measures how far the mid moves after a trade to evaluate execution quality
- [[Micro Price]] , a size weighted alternative to mid that better predicts short term direction
- [[Slippage]] , the difference between expected execution price and actual fill, often measured from mid
- [[Two Way Price]] , the bid and ask together that define the mid
- [[Stale Quote]] , when the bid or ask has not been updated, causing the mid to be misleading
- [[VWAP]] , a volume weighted benchmark that complements mid as a reference price
- [[Adverse Selection]] , the risk that the mid is stale and the counterparty knows the true price

## Common misconceptions
1. **"Mid is fair value."** Mid is a reference point, not a guarantee of fair value. In illiquid markets (lean hogs, rhodium), the spread can be wide and the mid may sit nowhere near where the next trade will print. The micro price is often a better short term fair value estimate.
2. **"I should always benchmark to mid."** For large orders that consume multiple levels of [[Depth of Book]], the relevant benchmark might be the average price across levels, not the mid at [[Top of Book]]. Using mid as the benchmark for a 500 lot Brent order overstates [[Slippage]] because no one expected to fill everything at the mid.
3. **"A tight mid means a liquid market."** A tight spread (and therefore a stable mid) can coexist with thin depth. The top of book might show 1 lot on each side of EUR/USD during a news event, making the mid technically tight but practically meaningless for any real size.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- CME Group, "Understanding Bid Ask Spread and Market Depth"
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
