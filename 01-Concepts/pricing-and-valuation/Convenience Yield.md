---
aliases: [convenience yield, convenience premium]
tags:
  - "#energy/crude"
  - "#energy/natgas"
  - "#metals/base"
date-added: "2026-03-20"
---

# Convenience Yield

## Definition

The non monetary benefit of holding a physical commodity rather than holding a futures contract on that commodity. It represents the option value of having the physical good available for immediate use, sale, or delivery during supply disruptions or demand spikes. It is an implicit yield that accrues to the holder of inventory, not observable directly but inferred from the relationship between spot and futures prices.

## Why it matters (commodities and FX)

Convenience yield is the missing variable that explains why commodity [[Forward Curve|forward curves]] sometimes trade in [[Backwardation]] even when storage and financing costs are positive. Without understanding convenience yield, the [[Cost of Carry Model]] appears broken. For a trader, convenience yield signals how tight physical markets are: high convenience yield means physical holders value their inventory highly because supply is scarce or delivery risk is elevated. This is a direct indicator of market stress.

In practice, when a commodity desk says "the curve is in steep backwardation," they are saying convenience yield is dominating storage and financing costs. This is a tradeable signal for [[Relative Value Trade|calendar spreads]].

## Concrete example

[[Brent Crude]] spot trades at $82. The 6 month futures trade at $78. Risk free rate is 5%, storage cost is approximately $0.50/barrel/month ($3 over 6 months). Under the [[Cost of Carry Model]] without convenience yield, the 6 month futures should be approximately $82 + $3 + $2 (financing) = $87. Instead it trades at $78, which is $9 below theoretical. The implied convenience yield is roughly $9 over 6 months, or about 22% annualized. This tells you the market places enormous value on having barrels available now, typically because inventories are low and demand for immediate delivery is strong.

## Key mechanics and formulas

Full cost of carry with convenience yield:

`F(t,T) = S(t) x e^((r + c - y)(T-t))`

Where:
- F = futures price at time t for delivery at T
- S = spot price
- r = risk free interest rate (annualized)
- c = storage cost rate (annualized, as % of spot)
- y = convenience yield (annualized, as % of spot)
- T-t = time to delivery in years

Rearranging to solve for implied convenience yield:

`y = r + c - (1/(T-t)) x ln(F/S)`

When y > r + c, the market is in [[Backwardation]].
When y < r + c, the market is in [[Contango]].

## Prerequisites

- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Cost of Carry Model]]
- [[Basis]]

## Related concepts (learn next)

- [[Storage Economics]] - physical storage capacity, injection/withdrawal rates, and seasonal patterns drive convenience yield levels. Understanding storage is understanding what makes convenience yield move.
- [[Inventory Cycle]] - the relationship between observable inventory levels (EIA, GIE, LME warehouses) and convenience yield. Low inventories = high convenience yield.
- [[Theory of Normal Backwardation]] - Keynes's theory that futures should trade below expected spot to compensate speculators for bearing risk. Connects convenience yield to risk premia.
- [[Calendar Spread]] - the direct expression of convenience yield in a trade. When convenience yield rises, front month strengthens vs deferred.
- [[Contango]] - the opposite regime. Understanding both states and what triggers transitions is essential.
- [[Roll Yield]] - the P&L consequence of convenience yield for anyone holding futures positions through expiry rolls.
- [[Squeeze]] - when convenience yield spikes to extreme levels because a single participant controls available supply for delivery.

## Common misconceptions

**"Convenience yield is constant."** It is highly volatile and regime dependent. It spikes during supply crises and collapses when inventories are comfortable. It can go from near zero to 50%+ annualized within weeks.

**"You can directly observe convenience yield."** You cannot. It is always implied from the difference between the theoretical cost of carry futures price and the actual futures price. Different market participants may have different effective convenience yields depending on their access to physical infrastructure.

**"Convenience yield only matters for physical traders."** Financial traders need it to understand curve shape, size calendar spread positions, and assess whether backwardation is structural or temporary.

## Sources

- Hull, Options, Futures, and Other Derivatives, Chapter 5 (Determination of Forward and Futures Prices)
- CME Group: Understanding the Crude Oil Futures Curve
- Fama and French, "Commodity Futures Prices: Some Evidence on Forecast Power, Premiums, and the Theory of Storage" (1987)
