---
aliases: [Arbitrageur, Arb, Relative Value Trader]
tags:
  - "#microstructure"
date-added: "2026-06-18"
---

# Arbitrageur

## Definition
In plain English, an arbitrageur is a trader who spots two prices for the same or closely related thing that do not line up, then buys the cheap one and sells the dear one to pocket the gap. The aim is profit with little or no directional risk, since the two legs largely cancel each other out. Technically, an arbitrageur exploits price discrepancies between related instruments or trading venues, and their activity is what forces those prices back into alignment. Unlike a [[Speculator]], who bets on direction, the arbitrageur ideally does not care whether the market rises or falls. In practice pure risk free arbitrage is rare; most real trades carry residual risks such as financing, timing, and convergence.

## Why it matters (commodities and FX)
Arbitrageurs are the enforcement mechanism for the law of one price. In commodities they keep the futures price tied to spot through [[Cost of Carry]], so the curve stays internally consistent across [[Contango]] and [[Backwardation]] regimes. In FX they keep cross rates coherent (for example EUR/USD, USD/JPY, and EUR/JPY) via triangular arbitrage, and keep forward points consistent with interest rate differentials via covered interest parity. When an arb opportunity appears, the act of trading it closes the gap, which is why mispricings are usually small and short lived in liquid markets.

## Concrete example
**Concrete:** Cash and carry on gold. Spot gold is 3,380 USD/oz. Financing plus storage and insurance over the period (the [[Cost of Carry]]) is 30 USD/oz, so fair value of the future is 3,410. The [[Gold Futures]] (COMEX GC, 100 oz) trades at 3,440, which is 30 above fair value. The arbitrageur sells 1 future at 3,440 and buys 100 oz spot at 3,380, funding the purchase. At [[Delivery]] the future converges to spot and they deliver the metal, locking in 3,440 minus 3,410 = 30 USD/oz, or 3,000 USD on the contract, independent of where gold goes. Win case: prices converge as expected and the 30 spread is captured. Fail case: financing rates jump mid trade so realised carry becomes 45 instead of 30, turning the +30 edge into a 15 loss; or convergence fails near [[Expiration]] due to a delivery squeeze, leaving the legs mismatched and the locked spread eroded.

**Simplified:** The future looked 30 too expensive versus owning gold and carrying it. Sell the future, buy the metal, carry it to delivery, keep the 30. If the cost of carrying it rises or the two prices do not meet at the end, the safe profit shrinks or flips to a loss.

## Key mechanics and formulas
Fair futures price under [[Cost of Carry]]: F = S x (1 + r + s minus y), where S is spot, r is the financing rate, s is storage plus insurance, and y is any [[Convenience Yield]]. Arbitrage profit on the cash and carry: profit = market futures price minus F, captured per unit if convergence holds to [[Delivery]]. The trade is profitable only while the observed mispricing exceeds the all in carrying cost. [[Location Arbitrage]] applies the same logic across venues or delivery points: buy where cheap, sell where dear, net of transport and transfer costs. Exchange arbs (for instance the same contract listed on two venues) capture tiny, frequent spreads net of fees and latency.

## Prerequisites
- [[Cost of Carry]]
- [[Futures Contract]]
- [[Delivery]]
- [[Convenience Yield]]

## Related concepts (learn next)
- [[Speculator]]: the directional counterpart; contrast risk free intent with risk seeking intent.
- [[Hedging]]: another non directional motive, useful for seeing why all three roles coexist.
- [[Cost of Carry]]: the formula that sets futures fair value and defines the arb edge.
- [[Calendar Spread]]: an arb structure between two expiries on the same underlying.
- [[Backwardation]]: the curve state where carry arbs reverse and convenience yield dominates.
- [[Contango]]: the curve state that supports the classic cash and carry.
- [[Location Arbitrage]]: the spatial version of the same price alignment logic.
- [[Delivery]]: the settlement event that forces convergence and closes the trade.

## Common misconceptions
- "Arbitrage is risk free money." Wrong, because real trades carry financing, execution, timing, and convergence risk; only the textbook case is truly riskless.
- "If I see the gap, I can capture it." Wrong, because transaction costs, fees, and latency often exceed the spread, so the visible mispricing is not the realisable profit.
- "Arbitrageurs cause volatility." Wrong, because their trading pushes prices together, which generally stabilises relationships rather than destabilising them.
- "A bigger futures premium always means a bigger arb." Wrong, because the edge is the premium net of full [[Cost of Carry]]; a high carry environment can leave no profit even with a wide nominal gap.

## Sources
- Hull, Options, Futures, and Other Derivatives, cost of carry and arbitrage pricing
- CME Group, Gold (GC) futures contract specifications
- Covered interest parity and triangular arbitrage, standard FX market microstructure references
