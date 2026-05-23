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

The non monetary benefit of holding physical commodity rather than a futures contract on it. Represents the option value of having the physical good available for immediate use, sale, or delivery during supply disruptions or demand spikes. An implicit yield accruing to the inventory holder, not directly observable but inferred from the spot/futures relationship.

## Why it matters (commodities and FX)

Convenience yield is the missing variable that explains why commodity [[Forward Curve|forward curves]] trade in [[Backwardation]] even when storage and financing costs are positive. Without it, the [[Cost of Carry Model]] looks broken. High convenience yield signals physical holders value their inventory because supply is scarce or delivery risk is elevated. A direct indicator of market stress.

When a commodity desk says "the curve is in steep backwardation," they mean convenience yield is dominating storage and financing costs. A tradeable signal for [[Relative Value Trade|calendar spreads]].

## Concrete example

**Concrete:** [[Brent Crude]] spot $82, 6 month futures $78. Risk free rate 5%, storage ~$0.50/bbl/month ($3 over 6 months). Under cost of carry without convenience yield, 6 month futures should ≈ $82 + $3 + $2 financing = $87. Actual $78 is $9 below theoretical. Implied convenience yield ≈ $9 over 6 months, or ~22% annualized. The market places enormous value on having barrels now: inventories are low and immediate delivery demand is strong.

**Simplified:** A refiner running flat out cannot wait 6 months for crude. Holding physical barrels today has option value, the ability to use them now, sell them in a squeeze, or deliver against a contract. That value shows up as a yield, invisible on its own but visible when futures trade below spot plus storage. The bigger the gap, the more the market values having the physical right now.

## Key mechanics and formulas

Full cost of carry with convenience yield:

`F(t,T) = S(t) × e^((r + c − y)(T−t))`

Where:
- F = futures price at time t for delivery at T
- S = spot price
- r = risk free interest rate (annualized)
- c = storage cost rate (annualized, % of spot)
- y = convenience yield (annualized, % of spot)
- T−t = time to delivery in years

Implied convenience yield:

`y = r + c − (1/(T−t)) × ln(F/S)`

When y > r + c → [[Backwardation]]. When y < r + c → [[Contango]].

## Prerequisites

- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Cost of Carry Model]]
- [[Basis]]

## Related concepts (learn next)

- [[Storage Economics]] — capacity, injection/withdrawal rates, and seasonal patterns drive convenience yield levels.
- [[Inventory Cycle]] — observable inventory levels (EIA, GIE, LME warehouses) vs convenience yield. Low inventories = high convenience yield.
- [[Theory of Normal Backwardation]] — Keynes's theory that futures trade below expected spot to compensate speculators. Connects convenience yield to risk premia.
- [[Calendar Spread]] — direct expression of convenience yield in a trade. Rising convenience yield strengthens front vs deferred.
- [[Contango]] — the opposite regime.
- [[Roll Yield]] — P&L consequence of convenience yield for futures holders through rolls.
- [[Squeeze]] — convenience yield spikes when a single participant controls available supply for delivery.

## Common misconceptions

**"Convenience yield is constant."** Highly volatile and regime dependent. Spikes during supply crises, collapses when inventories are comfortable. Can move from near zero to 50%+ annualized within weeks.

**"You can directly observe convenience yield."** You cannot. Always implied from the gap between theoretical cost of carry futures and actual futures price. Different participants may have different effective convenience yields based on physical infrastructure access.

**"Convenience yield only matters for physical traders."** Financial traders need it to understand curve shape, size calendar spreads, and assess whether backwardation is structural or temporary.

## Sources

- Hull, Options, Futures, and Other Derivatives, Chapter 5 (Determination of Forward and Futures Prices)
- CME Group: Understanding the Crude Oil Futures Curve
- Fama and French, "Commodity Futures Prices: Some Evidence on Forecast Power, Premiums, and the Theory of Storage" (1987)
