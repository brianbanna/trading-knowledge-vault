---
aliases: [supply shock, supply disruption, demand shock, scarcity, prompt scarcity, prompt demand]
tags:
  - "#macro"
  - "#energy"
date-added: "2026-03-20"
---

# Supply Shock

## Definition

A supply shock is a sudden, unexpected change in commodity availability that forces prices to reprice rapidly. A negative shock (supply loss) drives prices up. A positive shock (sudden oversupply) drives prices down. Demand shocks work symmetrically: unexpected demand surges (prompt scarcity) or destruction have equivalent pricing effects. Key variables: magnitude of disruption, duration, and the ability of inventories ([[Storage Economics]]) and substitution to absorb it. Short duration shocks are [[Mean Reversion]] candidates. Long duration or permanent shocks shift the [[Equilibrium Price]].

## Why it matters (commodities and FX)

Supply shocks are the primary generator of large, fast commodity price moves. They produce the steepest [[Backwardation]] (physical supply is urgently needed NOW), the sharpest [[Convenience Yield]] spikes, and the biggest [[Calendar Spread]] moves. The critical question when a shock hits: "Is this temporary or permanent?" A pipeline outage fixed in 2 weeks is a different trade than a war that removes 3 mb/d of supply for years. Temporary shocks create mean reversion opportunities (fade the spike). Permanent shocks create [[Structural Break|structural breaks]] (trade with the new trend).

Supply shocks transmit across assets. An oil supply shock reprices energy, then [[Commodity Currencies]] (CAD, NOK, RUB), then inflation expectations, then [[Real Interest Rates]], then [[Gold Futures]], then [[Risk-On Risk-Off|risk sentiment]].

## Concrete example

**Concrete:** Russia/Ukraine (Feb 2022). Russia produced ~10 mb/d of crude and was Europe's largest gas supplier. The invasion and sanctions created a massive negative supply shock. [[Brent Crude]] spiked $90 to $130 in 2 weeks. [[TTF Natural Gas]] went EUR 80/MWh to EUR 340/MWh. [[Brent-WTI Spread]] widened as seaborne supply (Brent) was more exposed than landlocked US supply (WTI). Duration assessment: the physical crude shock was partially temporary (Russian oil found buyers in China and India, rerouting rather than disappearing). The gas shock was structural (pipelines cut, requiring multi year LNG buildout). Traders who identified the duration traded accordingly: fading the crude spike (mean reversion) while staying long the European gas structural deficit. Prompt scarcity: front month premiums (backwardation) exploded because buyers needed physical immediately.

**Simplified:** A chunk of supply disappears overnight. Inventories cushion the gap for a while, but as they drain, prices rip higher to ration the remaining supply. The hard call is duration: is the supply coming back in weeks or never? If weeks, fade the spike. If never, ride the new trend. The same shock also reprices currencies of exporters and importers, then inflation, then rates, then gold. Pick which leg to trade based on liquidity and conviction.

## Key mechanics and formulas

**Shock classification framework:**

| Dimension | Short Term | Long Term |
|-----------|-----------|-----------|
| Magnitude | Small (1 to 2% of supply) | Large (5%+ of supply) |
| Duration | Days to weeks | Months to years |
| Inventory buffer | Sufficient to absorb | Insufficient |
| Substitution | Available | Unavailable |
| Price impact | Temporary spike | [[Equilibrium Price]] shift |
| Trade response | [[Mean Reversion]] (fade) | Trend follow or spread |

**Price impact estimation (rough):**
`Price Impact ≈ (Supply Loss / Daily Consumption) x (1 / Price Elasticity of Demand) x Spot Price`

Commodity demand is price inelastic in the short run (elasticity ~0.05 to 0.15 for oil). A 3% supply loss with elasticity 0.1 implies a ~30% price increase to balance the market. This is why commodity shocks produce outsized moves.

**Backwardation response:**
`Prompt Spread ≈ f(Inventory Days of Cover, Supply Gap Duration)`

Lower inventory buffer and longer expected duration = steeper backwardation.

## Prerequisites
- [[Forward Curve]]
- [[Backwardation]]
- [[Convenience Yield]]
- [[Storage Economics]]

## Related concepts (learn next)
- [[Mean Reversion]] - framework for trading temporary shocks. You must correctly identify the shock as temporary first.
- [[Equilibrium Price]] - permanent shocks shift the equilibrium. Mean reverting to the old one is a losing trade.
- [[Structural Break]] - statistical framework for identifying when a relationship has permanently changed.
- [[Regime Shift]] - supply shocks can trigger broader regime shifts across multiple asset classes.
- [[Geopolitical Risk]] - primary source of negative supply shocks in energy markets.
- [[Calendar Spread]] - supply shocks create the largest calendar spread moves. The prompt spread is the purest expression.
- [[Seasonality]] - supply shocks that coincide with seasonal demand peaks (hurricane + summer driving) are amplified.

## Common misconceptions

**"All supply shocks mean prices stay high."** Most are partially or fully offset by demand destruction (high prices reduce consumption), inventory releases (SPR), production increases elsewhere (OPEC spare capacity, US shale ramp), and substitution. Always about duration and offset capacity.

**"Buy the front month when a shock hits."** By the time you see the headline, the front month has repriced. More profitable is the calendar spread or cross asset impact (long [[Commodity Currencies]], short oil importers' currencies).

**"Demand shocks are less important than supply shocks."** COVID (2020) was the largest demand shock in oil history, removing ~20 mb/d overnight. It drove WTI to negative prices. Demand destruction can be equally violent.

## Sources

- Hamilton, James D., "Historical Oil Shocks" (NBER Working Paper, 2011)
- Kilian, Lutz, "The Economic Effects of Energy Price Shocks" (Journal of Economic Literature, 2008)
- IEA Oil Market Report: monthly supply/demand balances
- EIA Short Term Energy Outlook
