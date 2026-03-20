---
aliases: [cost of carry, carry model, cost of carry model, full carry]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-03-20"
---

# Cost of Carry

## Definition

The cost of carry is the total expense of holding a physical commodity or financial asset over time. It includes storage costs, insurance, financing (interest on capital tied up), and minus any income or benefit the asset generates (like [[Convenience Yield]] for commodities or dividends for equities). The cost of carry model is the theoretical framework that links spot prices to futures prices: in a "full carry" market, the futures price equals the spot price plus the net cost of carry. It is the foundation of all [[Forward Curve]] analysis.

## Why it matters (commodities and FX)

The cost of carry determines whether a commodity [[Forward Curve]] is in [[Contango]] or [[Backwardation]]. When futures trade at full carry (spot + storage + financing), there is no edge in calendar spreads because the curve shape is fully explained by carrying costs. When futures trade below full carry (backwardation), the market is signaling that [[Convenience Yield]] exceeds carrying costs, meaning physical supply is tight. When futures trade above full carry (super contango), there is a cash and carry arbitrage: buy spot, store it, sell futures, and lock in risk free profit. Understanding where the curve sits relative to full carry is the starting point for every [[Calendar Spread]] and [[Relative Value Trade]].

## Concrete example

[[Gold Futures]]: Gold spot trades at $2,000/oz. Storage and insurance cost approximately 0.3%/year. The risk free rate is 5%. Gold has essentially zero [[Convenience Yield]] (no industrial urgency). The 1 year futures should trade at approximately: $2,000 x e^(0.05 + 0.003) x 1 = $2,000 x 1.0546 = $2,109. If the actual 1 year gold futures trade at $2,109, the market is at full carry. No arbitrage. If they trade at $2,130 (above full carry), a trader could buy spot gold, store it for 1 year, and sell the futures at $2,130, locking in $21/oz profit above carry costs. This arbitrage would push the futures price down and/or the spot price up until full carry is restored.

[[WTI Crude Oil]]: Spot at $74. Storage at Cushing costs approximately $0.45/bbl/month ($5.40/year). Financing at 5% = $3.70/year. Total carry = $9.10/year. If 12 month futures trade at $76 (only $2 above spot), the market is in backwardation relative to full carry. Convenience yield is approximately $7.10/year, signaling physical tightness.

## Key mechanics and formulas

**General cost of carry formula:**

`F(t,T) = S(t) x e^((r + c - y)(T-t))`

Where:
- F(t,T) = futures price at time t for delivery at T
- S(t) = current spot price
- r = risk free interest rate (annualized, continuously compounded)
- c = storage cost rate (annualized, as % of spot)
- y = [[Convenience Yield]] (annualized, as % of spot)
- T-t = time to maturity in years

**Full carry condition:** When F = S x e^((r+c)(T-t)), the market is at full carry (y = 0). Futures reflect the full cost of storage and financing.

**Backwardation condition:** When F < S x e^((r+c)(T-t)), convenience yield exceeds carry costs. Physical supply is valued.

**Super contango / cash and carry arb:** When F > S x e^((r+c)(T-t)), arbitrageurs buy spot, store, and sell futures for risk free profit. This caps the upside of contango.

**Implied convenience yield:**
`y = r + c - ln(F/S) / (T-t)`

## Prerequisites
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Basis]]

## Related concepts (learn next)
- [[Convenience Yield]] - the "missing variable" in the carry model. Understanding when and why convenience yield spikes is the key to trading the curve.
- [[Storage Economics]] - physical storage capacity, costs, and constraints determine the "c" in the carry model and set the bounds for contango.
- [[Roll Yield]] - the P&L consequence of carry for anyone holding futures. Positive carry = positive roll yield.
- [[Calendar Spread]] - directly trades the cost of carry relationship. When spreads deviate from carry, there is a tradeable opportunity.
- [[Cash and Carry Arbitrage]] - the risk free trade that enforces the upper bound of contango. Understanding this arbitrage explains why contango cannot exceed full carry for long.
- [[Carry Trade]] - the FX analogue. Interest rate differentials in FX are the equivalent of storage and convenience yield in commodities.
- [[Equilibrium Price]] - cost of carry defines the equilibrium relationship between spot and futures.

## Common misconceptions

**"Full carry means the market is bearish."** Full carry simply means carrying costs explain the curve shape. The spot price can be at any level. A market at full carry with spot at $100 is not more bearish than one in backwardation with spot at $60.

**"Backwardation means the market expects prices to fall."** Backwardation means convenience yield exceeds carry costs. It says nothing about directional expectations. Spot can continue rising in backwardation.

**"Storage costs are constant."** Storage costs vary dramatically with utilization. When Cushing is 90% full, storage rates spike. When it is 50% full, rates are at minimums. The "c" in the carry formula is dynamic.

## Sources

- Hull, Options, Futures, and Other Derivatives, Chapter 5
- CME Group: Cost of Carry Model for Commodity Futures
- Fama and French, "Commodity Futures Prices: Some Evidence on Forecast Power, Premiums, and the Theory of Storage" (1987)
- Working, Holbrook, "The Theory of Price of Storage" (1949)
