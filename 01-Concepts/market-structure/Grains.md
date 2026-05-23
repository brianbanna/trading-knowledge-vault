---
aliases: [grains, grain markets, CBOT grains]
tags:
  - "#agri/grains"
date-added: "2026-03-20"
---

# Grains

## Definition
Grains are the foundational agricultural commodities traded primarily on the Chicago Board of Trade ([[CBOT]]): [[Corn]], [[Wheat]], [[Soybeans]], and [[Rice]]. Contracts represent standardized quantities of physical grain deliverable at approved warehouses and elevators along the Illinois River and in greater Chicago. Grain markets are among the oldest organized futures markets, dating to the 1840s. Prices quote in cents per bushel (rice in cents per hundredweight); contracts trade electronically on [[CME Globex]] nearly 24 hours per day. Trading is seasonal, driven by Northern Hemisphere planting (April to June), pollination (July), and harvest (September to November). The [[WASDE]] report from USDA is the single most important scheduled release.

## Why it matters (commodities and FX)
Grains are the backbone of global food security and animal feed, critical for inflation expectations and [[terms of trade]] for agricultural exporters: US, Brazil, Argentina, Ukraine. Large grain moves ripple into FX pairs like [[BRL/USD]] and [[ARS/USD]], and into freight via [[Panamax]] and [[Capesize]] rates. Weather shocks in major growing regions can trigger 30 to 50% rallies in a single season. Grain spreads ([[Old Crop New Crop]], [[Crush Spread]], calendar spreads) are core RV instruments for commodity desks.

## Concrete example

**Concrete:** June 2012, US drought cuts corn yield forecasts from 166 to 123 bushels per acre. Trader long December 2012 corn at $5.50/bu sees the contract rally to $8.40/bu by August, $2.90/bu or $14,500 per contract (5,000 bushels). [[Stocks to Use Ratio]] falls below 6%, signaling crisis tightness and triggering demand rationing. Failure mirror: 2014, trader buys July wheat at $7.00/bu expecting a repeat. US and Black Sea produce record crops with ideal conditions. Wheat collapses to $5.20/bu by harvest, $1.80/bu or $9,000 per contract loss. Bullish weather bets fail roughly 7 of 10 years when conditions turn out adequate and global supply is diversified.

**Simplified:** Grain prices come from the balance of how much was planted, how the weather treats it, and how much demand exists for food, feed, and ethanol. The USDA publishes monthly supply estimates that move the market hard. Drought years can double prices; normal years are boring. Most professional grain trading is in spreads (old crop vs new crop, crush spread) rather than flat directional bets.

## Key mechanics and formulas
- **Contract size:** Corn, wheat, soybeans = 5,000 bushels; Rice = 2,000 cwt
- **Tick size:** Corn, wheat, soybeans = 1/4 cent/bu ($12.50 per tick)
- **Ending stocks = Beginning stocks + Production + Imports − Domestic use − Exports**
- **[[Stocks to Use Ratio]] = Ending stocks / Total use × 100**
- **Seasonality index:** Compare current month's average return over N years to identify planting and harvest patterns
- **Crop condition index:** USDA weekly ratings (% good/excellent) regressed against final yield to estimate production in real time

## Prerequisites
- [[Futures Contract]]
- [[Contango Roll Cost]]
- [[Backwardation Roll Gain]]
- [[Delivery]]
- [[Crop Year]]

## Related concepts (learn next)
- [[WASDE]] provides the monthly balance and is the primary catalyst.
- [[Old Crop New Crop]] captures the premium between current and upcoming harvest inventories.
- [[Stocks to Use Ratio]] quantifies how tight or loose the balance sheet is.
- [[Weather Premium]] reflects the risk premium for uncertain growing conditions.
- [[Crush Spread]] measures soybean processing margins, linking beans to meal and oil.
- [[Spread Trade]] is the dominant professional strategy.
- [[Basis Risk]] arises when hedging at a different physical location.
- [[COT Positioning]] reveals managed money crowding.

## Common misconceptions

**"Grain prices are purely supply driven."** Demand matters enormously. China's 2020 to 2021 corn import surge added $1.50/bu without a US weather problem. Ethanol mandates consume ~35% of the US corn crop.

**"All grains move together."** Corn and soybeans compete for acres but have different demand drivers (feed/ethanol vs meal/oil). Wheat has its own supply geography (Black Sea, EU, Australia). Inter grain spreads can diverge 30%+ in a single year.

**"USDA numbers are always accurate."** [[WASDE]] estimates revise monthly with large changes early in the [[Crop Year]] when yield is uncertain. The market frequently disagrees with USDA, creating 3 to 5% post report volatility in minutes.

## Sources
- CBOT Rulebook and Contract Specifications, CME Group
- "Trading and Hedging with Agricultural Futures and Options" by James B. Bittman
- USDA Economic Research Service, Feed Grains Database
- "Commodity Trading Advisors" edited by Gregoriou, Karavas, L'Habitant, Rouah
