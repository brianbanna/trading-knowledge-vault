---
aliases: [supply shock, supply disruption, demand shock, scarcity, prompt scarcity, prompt demand]
tags:
  - "#macro"
  - "#energy"
date-added: "2026-03-20"
---

# Supply Shock

## Definition

A supply shock is a sudden, unexpected change in the availability of a commodity that forces prices to reprice rapidly. A negative supply shock (supply loss) drives prices up. A positive supply shock (sudden oversupply) drives prices down. Demand shocks work symmetrically: unexpected demand surges (prompt scarcity) or demand destruction have equivalent pricing effects. The key variables are the magnitude of the disruption, the duration of the shock, and the ability of inventories ([[Storage Economics]]) and substitution to absorb it. Short duration shocks are candidates for [[Mean Reversion]] trades. Long duration or permanent shocks shift the [[Equilibrium Price]].

## Why it matters (commodities and FX)

Supply shocks are the primary generator of large, fast commodity price moves. They produce the steepest [[Backwardation]] (because physical supply is urgently needed NOW), the sharpest [[Convenience Yield]] spikes, and the biggest [[Calendar Spread]] moves. For a trader, the critical question when a shock hits is: "Is this temporary or permanent?" A pipeline outage that will be fixed in 2 weeks is a different trade than a war that removes 3 million bbl/d of supply for years. Temporary shocks create mean reversion opportunities (fade the spike). Permanent shocks create [[Structural Break|structural breaks]] (trade with the new trend).

Supply shocks also transmit across assets. An oil supply shock reprices energy, then [[Commodity Currencies]] (CAD, NOK, RUB), then inflation expectations, then [[Real Interest Rates]], then [[Gold Futures]], then [[Risk-On Risk-Off|risk sentiment]].

## Concrete example

**Russia/Ukraine (Feb 2022):** Russia produced ~10 million bbl/d of crude and was Europe's largest gas supplier. The invasion and subsequent sanctions created a massive negative supply shock. [[Brent Crude]] spiked from $90 to $130 in 2 weeks. [[TTF Natural Gas]] went from EUR 80/MWh to EUR 340/MWh. The [[Brent-WTI Spread]] widened as seaborne supply (Brent) was more exposed than landlocked US supply (WTI).

**Duration assessment:** The physical crude shock was partially temporary (Russian oil found buyers in China and India, rerouting rather than disappearing). The gas shock was more structural (pipelines to Europe were cut, requiring multi year LNG infrastructure buildout). Traders who correctly identified the duration traded accordingly: fading the crude spike (mean reversion) while staying long the European gas structural deficit.

**Prompt scarcity:** During the shock, front month premiums (backwardation) exploded because buyers needed physical barrels immediately. Refiners, airlines, and utilities were willing to pay large premiums for near term delivery. This "prompt demand" or "scarcity premium" is the most tradeable signal from a supply shock.

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

Commodity demand is price inelastic in the short run (elasticity ~0.05 to 0.15 for oil). A 3% supply loss with elasticity of 0.1 implies a ~30% price increase to balance the market. This is why commodity shocks produce outsized price moves.

**Backwardation response:**
`Prompt Spread ≈ f(Inventory Days of Cover, Supply Gap Duration)`

The lower the inventory buffer and the longer the expected duration, the steeper the backwardation.

## Prerequisites
- [[Forward Curve]]
- [[Backwardation]]
- [[Convenience Yield]]
- [[Storage Economics]]

## Related concepts (learn next)
- [[Mean Reversion]] - the framework for trading temporary shocks. But you must correctly identify the shock as temporary first.
- [[Equilibrium Price]] - permanent shocks shift the equilibrium. Mean reverting to the old equilibrium after a structural shift is a losing trade.
- [[Structural Break]] - the statistical/quantitative framework for identifying when a relationship has permanently changed.
- [[Regime Shift]] - supply shocks can trigger broader regime shifts across multiple asset classes.
- [[Geopolitical Risk]] - the primary source of negative supply shocks in energy markets.
- [[Calendar Spread]] - supply shocks create the largest calendar spread moves. The prompt spread is the purest expression of a supply shock.
- [[Seasonality]] - supply shocks that coincide with seasonal demand peaks (hurricane + summer driving) are amplified.

## Common misconceptions

**"All supply shocks mean prices will stay high."** Most supply shocks are partially or fully offset by demand destruction (high prices reduce consumption), inventory releases (SPR), production increases elsewhere (OPEC spare capacity, US shale ramp), and substitution. The question is always about duration and offset capacity.

**"You should buy the front month when a shock hits."** By the time you see the headline, the front month has already repriced. The more profitable approach is often to trade the calendar spread or the cross asset impact (e.g., long [[Commodity Currencies]], short oil importers' currencies).

**"Demand shocks are less important than supply shocks."** COVID (2020) was the largest demand shock in oil market history, removing ~20 million bbl/d practically overnight. It drove WTI to negative prices. Demand destruction can be equally violent.

## Sources

- Hamilton, James D., "Historical Oil Shocks" (NBER Working Paper, 2011)
- Kilian, Lutz, "The Economic Effects of Energy Price Shocks" (Journal of Economic Literature, 2008)
- IEA Oil Market Report: monthly supply/demand balances
- EIA Short Term Energy Outlook
