---
aliases: [equilibrium price, fair value, fundamental value, clearing price]
tags:
  - "#macro"
date-added: "2026-03-20"
---

# Equilibrium Price

## Definition

The equilibrium price is the level at which supply and demand balance for a given commodity or asset, producing no excess inventory build or draw. It is not a fixed number but a moving target that shifts with changes in production costs, demand growth, inventory levels, and market structure. After a [[Supply Shock]] or demand disruption, markets reprice toward a new equilibrium that may be permanently higher or lower than the prior one. The concept is essential for distinguishing temporary dislocations (tradeable via [[Mean Reversion]]) from permanent [[Structural Break|structural shifts]] (which require adapting to a new level).

## Why it matters (commodities and FX)

Every mean reversion trade assumes the existence of an equilibrium to revert to. If you trade [[Calendar Spread|calendar spreads]], [[Brent-WTI Spread]], or any [[Relative Value Trade]], you are implicitly betting on a specific equilibrium. Getting the equilibrium wrong is the primary risk in spread trading: if you assume the Brent-WTI spread will revert to $4 but the true new equilibrium is $8 due to infrastructure changes, you will bleed money waiting for a reversion that never comes. Identifying whether a price move is a deviation from equilibrium or a shift to a new equilibrium is the core analytical challenge in commodity trading.

## Concrete example

Pre 2014, [[Brent Crude]] equilibrium was roughly $100 to $110/bbl, supported by rising EM demand and constrained non OPEC supply. US shale production growth from 5 million to 9+ million bbl/d permanently lowered the marginal cost of the next barrel. The equilibrium shifted to $50 to $70/bbl. Traders who kept $100 as their mental anchor lost money for years. The correct response was recognizing the [[Structural Break]] and recalibrating.

In FX, EUR/USD equilibrium shifted from 1.30 to 1.40 (2010 to 2014) to 1.05 to 1.15 (2015+) as ECB monetary policy diverged from the Fed. Carry traders and relative value traders needed to adjust their mean reversion targets.

## Key mechanics and formulas

**Static equilibrium (commodity):**
At equilibrium: Production + Imports + Inventory Draws = Consumption + Exports + Inventory Builds

When production + imports > consumption + exports, inventories build and prices fall toward equilibrium. The reverse for draws.

**Marginal cost as equilibrium anchor:**
For commodities, the long run equilibrium price tends to track the marginal cost of production of the highest cost producer needed to meet demand. For crude oil, this is roughly the breakeven cost of US shale ($40 to $60/bbl depending on the basin). Below this level, production declines. Above it, production grows.

**Speed of adjustment:**
Markets do not jump to equilibrium instantly. Adjustment speed depends on supply elasticity (how fast production responds), demand elasticity (how fast consumption adjusts), and inventory buffers ([[Storage Economics]]). Oil markets adjust over months. Natural gas (seasonal storage) adjusts over quarters. Metals with large above ground stocks adjust slowly.

## Prerequisites
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Cost of Carry]]

## Related concepts (learn next)
- [[Mean Reversion]] - the statistical expression of equilibrium. Mean reversion strategies assume a stable equilibrium exists and prices oscillate around it.
- [[Structural Break]] - when the equilibrium itself shifts permanently. The single biggest risk to any mean reversion trade.
- [[Supply Shock]] - events that temporarily or permanently displace the market from equilibrium. Distinguishing "temporary shock, will revert" from "new equilibrium" is the key skill.
- [[Regime Shift]] - broader market environment changes that alter the equilibrium for multiple assets simultaneously.
- [[Storage Economics]] - inventories act as a buffer between supply and demand, slowing the adjustment to equilibrium.
- [[Seasonality]] - seasonal equilibria: the market's equilibrium price is different in winter vs summer for energy commodities.

## Common misconceptions

**"Equilibrium is a number you can calculate precisely."** It is a range, not a point. It depends on assumptions about supply elasticity, demand growth, and time horizon. Different market participants have different estimates.

**"Prices always revert to equilibrium."** They revert to the CURRENT equilibrium, which may have shifted. The equilibrium of 2 years ago may be irrelevant today. Always test whether the fundamentals supporting your equilibrium estimate are still intact.

**"Long run equilibrium matters for short term trading."** Short term prices are driven by positioning, sentiment, and flows, not fundamentals. Equilibrium analysis is most useful for trades with horizons of weeks to months, not hours.

## Sources

- Fattouh, Bassam, "The Dynamics of Crude Oil Price Differentials" (2010)
- Hamilton, James D., "Understanding Crude Oil Prices" (2009)
- CME Group: Economics of Commodity Pricing
