---
aliases: [cost of carry, carry model, cost of carry model, full carry]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-03-20"
---

# Cost of Carry

## Definition

Cost of carry is the total expense of holding a physical commodity or financial asset over time: storage, insurance, financing (interest on capital tied up), minus any income or benefit the asset generates ([[Convenience Yield]] for commodities, dividends for equities). The cost of carry model links spot to futures: at "full carry," futures price = spot + net cost of carry. The foundation of all [[Forward Curve]] analysis.

## Why it matters (commodities and FX)

Cost of carry determines whether a [[Forward Curve]] sits in [[Contango]] or [[Backwardation]]. At full carry (spot + storage + financing), the curve shape is fully explained by carrying costs and there is no calendar spread edge. Below full carry (backwardation), [[Convenience Yield]] exceeds carrying costs, signaling physical tightness. Above full carry (super contango), cash and carry arbitrage opens: buy spot, store, sell futures, lock in risk free profit. Curve position vs full carry is the starting point for every [[Calendar Spread]] and [[Relative Value Trade]].

## Concrete example

**Concrete:** [[Gold Futures]] spot $2,000/oz. Storage + insurance ~0.3%/year. Risk free rate 5%. Gold has near zero [[Convenience Yield]]. 1Y futures should ≈ $2,000 × e^(0.05 + 0.003) = $2,109. Actual at $2,109 = full carry, no arb. Actual at $2,130 (above full carry) → buy spot, store 1Y, sell future at $2,130, lock $21/oz above carry. The arb pushes futures down or spot up until full carry restores. [[WTI Crude Oil]] spot $74. Cushing storage ~$0.45/bbl/month ($5.40/year). Financing 5% = $3.70/year. Total carry $9.10/year. If 12M futures trade at $76 (only $2 above spot), backwardation vs full carry. Implied convenience yield ~$7.10/year: physical tightness.

**Simplified:** To hold a barrel of oil for a year, you pay rent on a tank, pay interest on the cash tied up, and lose nothing in dividends. Add those costs to the spot price and that is roughly what a 1 year futures contract should cost. If futures cost less, the market is telling you physical barrels are precious right now. If futures cost more, somebody can make free money buying spot and selling futures, which is why it rarely happens.

## Key mechanics and formulas

**General cost of carry formula:**

`F(t,T) = S(t) × e^((r + c − y)(T−t))`

Where:
- F(t,T) = futures price at time t for delivery at T
- S(t) = current spot price
- r = risk free interest rate (annualized, continuously compounded)
- c = storage cost rate (annualized, % of spot)
- y = [[Convenience Yield]] (annualized, % of spot)
- T−t = time to maturity in years

**Full carry condition:** When F = S × e^((r+c)(T−t)), market at full carry (y = 0). Futures reflect full storage + financing.

**Backwardation condition:** F < S × e^((r+c)(T−t)) → convenience yield exceeds carry.

**Super contango / cash and carry arb:** F > S × e^((r+c)(T−t)) → arbitrageurs buy spot, store, sell futures. Caps upside of contango.

**Implied convenience yield:**
`y = r + c − ln(F/S) / (T−t)`

## Prerequisites
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Basis]]

## Related concepts (learn next)
- [[Convenience Yield]] — the missing variable. When and why it spikes is the key to trading the curve.
- [[Storage Economics]] — capacity, costs, and constraints determine "c" and set bounds for contango.
- [[Roll Yield]] — P&L consequence of carry for futures holders.
- [[Calendar Spread]] — trades the cost of carry relationship directly.
- [[Cash and Carry Arbitrage]] — enforces the upper bound of contango.
- [[Carry Trade]] — FX analogue. Rate differentials in FX are the equivalent of storage + convenience yield in commodities.
- [[Equilibrium Price]] — cost of carry defines the equilibrium between spot and futures.

## Common misconceptions

**"Full carry means the market is bearish."** Full carry means carrying costs explain the curve shape. Spot can sit at any level. Full carry with spot $100 is not more bearish than backwardation with spot $60.

**"Backwardation means prices will fall."** Backwardation means convenience yield exceeds carry. Says nothing about direction. Spot can keep rising.

**"Storage costs are constant."** Storage costs scale with utilization. Cushing at 90% full → rates spike. At 50% → rates at minimums. "c" is dynamic.

## Sources

- Hull, Options, Futures, and Other Derivatives, Chapter 5
- CME Group: Cost of Carry Model for Commodity Futures
- Fama and French, "Commodity Futures Prices: Some Evidence on Forecast Power, Premiums, and the Theory of Storage" (1987)
- Working, Holbrook, "The Theory of Price of Storage" (1949)
