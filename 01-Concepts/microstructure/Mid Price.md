---
aliases: [mid price, mid, midpoint, mid market price]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Mid Price

## Definition
The mid price is the arithmetic average of the best [[Bid-Ask Spread|bid]] and best ask: (Bid + Ask) / 2. It is a convenient reference for where the true price might be, not necessarily where any trade will execute. In thin or skewed markets, the mid is misleading because best bid and ask sit far apart or carry different sizes. A market maker uses mid as a starting anchor, then adjusts quotes around it for [[Skew Microstructure|skew]], [[Market Impact|impact]], and inventory.

## Why it matters (commodities and FX)
In FX, the mid is the TCA benchmark for execution quality. Buying EUR/USD at 1.10015 with mid 1.10010: cost 0.5 pips from mid, the [[Half Spread]]. In commodities, Brent on ICE at $82.50 / $82.54 has mid $82.52. Execution desks report fills vs mid to judge whether a broker or algo is adding or leaking value. The mid is the first step toward [[Slippage]], [[Markout]], and the economics of [[Market Impact|market making]].

## Concrete example

**Concrete:** Brent front month on ICE: $82.50 bid, $82.54 ask. Mid = $82.52. Market maker buys 10 lots at $82.50 and sells 10 lots at $82.54. Average entry at bid, exit at ask: earned $0.04/bbl around mid. 10 x 1000 x $0.04 = $400 spread capture. Failure: using mid as fair value in a fast market. True equilibrium shifted to $82.60 because a large buyer swept the offer, but the stale $82.50 bid was not cancelled. Mid still reads $82.52, underestimating real price by $0.08. Selling at $82.54 thinking it is above mid, market prints $82.62 seconds later. [[Markout]] = -$0.08/bbl. Relying on mid in a moving market exposed me to [[Adverse Selection]].

**Simplified:** Mid is the average of the best buy and sell prices. It is a reference point, not a price you can actually trade at. Traders measure execution quality against it: how far from mid did I fill? When the book is balanced, mid is meaningful. When one side is stale or sizes differ, mid lies.

## Key mechanics and formulas
- **Mid price** = (Best Bid + Best Ask) / 2
- **Micro price** (size weighted) = (Bid x Ask Size + Ask x Bid Size) / (Bid Size + Ask Size). Adjusts mid toward the side with less resting size, giving a better short term fair value estimate
- **Spread** = Ask - Bid
- Mid is undefined when either side of [[Depth of Book]] is empty

## Prerequisites
- [[Bid-Ask Spread]]
- [[Top of Book]]
- [[Depth of Book]]

## Related concepts (learn next)
- [[Half Spread]] , distance from mid to one side, single leg cost
- [[Markout]] , measures how far mid moves after a trade
- [[Micro Price]] , size weighted alternative better predicting short term direction
- [[Slippage]] , difference between expected and actual fill, often measured from mid
- [[Two Way Price]] , the bid and ask defining the mid
- [[Stale Quote]] , when bid or ask has not updated, making mid misleading
- [[VWAP]] , volume weighted benchmark complementing mid
- [[Adverse Selection]] , the risk that the mid is stale and counterparty knows true price

## Common misconceptions
1. **"Mid is fair value."** Mid is a reference, not a guarantee of fair value. In illiquid markets (lean hogs, rhodium), spread is wide and mid sits nowhere near where the next print lands. Micro price is often a better short term estimate.
2. **"Always benchmark to mid."** For large orders consuming multiple levels of [[Depth of Book]], the relevant benchmark is the average across levels, not the [[Top of Book]] mid. Using mid for a 500 lot Brent order overstates [[Slippage]].
3. **"Tight mid means liquid market."** A tight spread (stable mid) can coexist with thin depth. EUR/USD might show 1 lot per side during a news event; mid is technically tight but practically meaningless for any real size.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- CME Group, "Understanding Bid Ask Spread and Market Depth"
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
