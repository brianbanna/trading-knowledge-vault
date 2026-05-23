---
aliases: [equilibrium price, fair value, fundamental value, clearing price]
tags:
  - "#macro"
date-added: "2026-03-20"
---

# Equilibrium Price

## Definition

The equilibrium price is the level at which supply and demand balance, producing no inventory build or draw. Not a fixed number but a moving target shifting with production costs, demand growth, inventory levels, and market structure. After a [[Supply Shock]] or demand disruption, markets reprice toward a new equilibrium that may be permanently higher or lower than the prior one. Distinguishing temporary dislocations (tradeable via [[Mean Reversion]]) from permanent [[Structural Break|structural shifts]] (requiring adaptation) is the core analytical task.

## Why it matters (commodities and FX)

Every mean reversion trade assumes an equilibrium to revert to. [[Calendar Spread|Calendar spreads]], [[Brent-WTI Spread]], and any [[Relative Value Trade]] are implicit bets on a specific equilibrium. Getting it wrong is the primary risk: assuming the Brent-WTI spread reverts to $4 while the true new equilibrium is $8 due to infrastructure changes bleeds money on a reversion that never comes. Identifying whether a price move is a deviation from equilibrium or a shift to a new equilibrium is the core analytical challenge in commodity trading.

## Concrete example

**Concrete:** Pre 2014, [[Brent Crude]] equilibrium ran $100 to $110/bbl, supported by rising EM demand and constrained non OPEC supply. US shale production growth from 5M to 9M+ bbl/d permanently lowered the marginal cost of the next barrel. Equilibrium shifted to $50 to $70/bbl. Traders who anchored to $100 bled for years. The correct response was recognizing the [[Structural Break]] and recalibrating. In FX, EUR/USD equilibrium shifted from 1.30 to 1.40 (2010 to 2014) to 1.05 to 1.15 (2015+) as ECB diverged from the Fed. Carry traders and relative value desks had to adjust reversion targets.

**Simplified:** Equilibrium is where supply and demand balance, with no inventory build or draw. Prices oscillate around it. If your trade idea is mean reversion, you are betting the price returns to a fair level. The trap: the fair level can move. A new technology, a new producer, a policy shift can permanently change the equilibrium. If you trade against the new equilibrium thinking it is a temporary deviation, you lose money for years. The skill is telling shock from regime change.

## Key mechanics and formulas

**Static equilibrium (commodity):**
At equilibrium: Production + Imports + Inventory Draws = Consumption + Exports + Inventory Builds

When production + imports > consumption + exports, inventories build and prices fall toward equilibrium. Reverse for draws.

**Marginal cost as anchor:**
Long run equilibrium tracks the marginal cost of the highest cost producer needed to meet demand. For crude, this is roughly US shale breakeven ($40 to $60/bbl by basin). Below: production declines. Above: production grows.

**Speed of adjustment:**
Markets do not jump to equilibrium instantly. Adjustment depends on supply elasticity, demand elasticity, and inventory buffers ([[Storage Economics]]). Oil markets adjust over months. Natural gas (seasonal storage) over quarters. Metals with large above ground stocks adjust slowly.

## Prerequisites
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Cost of Carry]]

## Related concepts (learn next)
- [[Mean Reversion]]: the statistical expression of equilibrium; reversion strategies assume a stable equilibrium exists.
- [[Structural Break]]: when the equilibrium itself shifts permanently. Biggest risk to any reversion trade.
- [[Supply Shock]]: events that temporarily or permanently displace the market from equilibrium.
- [[Regime Shift]]: broader environment changes that alter equilibrium across multiple assets.
- [[Storage Economics]]: inventories buffer between supply and demand, slowing adjustment.
- [[Seasonality]]: seasonal equilibria; the equilibrium price differs in winter vs summer for energy commodities.

## Common misconceptions

**"Equilibrium is a number you can calculate precisely."** It is a range. It depends on supply elasticity, demand growth, and time horizon assumptions. Different participants have different estimates.

**"Prices always revert to equilibrium."** They revert to the CURRENT equilibrium, which may have shifted. The equilibrium of 2 years ago may be irrelevant today. Test whether the fundamentals supporting your estimate still hold.

**"Long run equilibrium matters for short term trading."** Short term prices are driven by positioning, sentiment, and flows, not fundamentals. Equilibrium analysis is most useful at weeks to months, not hours.

## Sources

- Fattouh, Bassam, "The Dynamics of Crude Oil Price Differentials" (2010)
- Hamilton, James D., "Understanding Crude Oil Prices" (2009)
- CME Group: Economics of Commodity Pricing
