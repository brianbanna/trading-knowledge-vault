---
aliases: [grains, grain markets, CBOT grains]
tags:
  - "#agri/grains"
date-added: "2026-03-20"
---

# Grains

## Definition
Grains are the foundational agricultural commodities traded primarily on the Chicago Board of Trade ([[CBOT]]), encompassing [[Corn]], [[Wheat]], [[Soybeans]], and [[Rice]]. These contracts represent standardized quantities of physical grain deliverable at approved warehouses and elevators along the Illinois River and in the greater Chicago area. Grain markets are among the oldest organized futures markets in the world, dating back to the 1840s when forward contracts on corn were first standardized. Prices are quoted in cents per bushel (except rice, quoted in cents per hundredweight), and contracts trade electronically on [[CME Globex]] nearly 24 hours per day. Trading is highly seasonal, driven by Northern Hemisphere planting (April to June), pollination (July), and harvest (September to November) windows. The [[WASDE]] report from the USDA is the single most important scheduled data release for grain pricing, establishing the official supply and demand balance each month.

## Why it matters (commodities and FX)
Grains are the backbone of global food security and animal feed chains, making them critical for inflation expectations and [[terms of trade]] for agricultural exporting nations such as the US, Brazil, Argentina, and Ukraine. Large grain price moves ripple into FX pairs like [[BRL/USD]] and [[ARS/USD]], and into freight markets via [[Panamax]] and [[Capesize]] rates. Weather shocks in major growing regions can trigger 30 to 50% price rallies in a single season, creating outsized trading opportunities and hedging urgency. Grain spreads ([[Old Crop New Crop]], [[Crush Spread]], calendar spreads) are core relative value instruments for commodity desks worldwide.

## Concrete example
**Success case:** In June 2012, a severe US drought cut corn yield forecasts from 166 to 123 bushels per acre. A trader long December 2012 corn at $5.50/bu saw the contract rally to $8.40/bu by August, a gain of $2.90/bu or $14,500 per contract (5,000 bushels). The [[Stocks to Use Ratio]] fell below 6%, signaling crisis level tightness and triggering demand rationing.

**Failure case:** In 2014, a trader bought July wheat at $7.00/bu expecting a repeat drought pattern. Instead, the US and Black Sea region produced record crops with ideal growing conditions. Wheat collapsed to $5.20/bu by harvest, a loss of $1.80/bu or $9,000 per contract. The lesson: bullish weather bets fail roughly 7 out of 10 years when conditions turn out adequate and global supply is diversified.

## Key mechanics and formulas
- **Contract size:** Corn, wheat, soybeans = 5,000 bushels per contract; Rice = 2,000 cwt per contract
- **Tick size:** Corn and wheat = 1/4 cent/bu ($12.50 per tick); Soybeans = 1/4 cent/bu ($12.50 per tick)
- **Ending stocks = Beginning stocks + Production + Imports - Domestic use - Exports**
- **[[Stocks to Use Ratio]] = Ending stocks / Total use x 100**
- **Seasonality index:** Compare current month's average return over N years to identify planting and harvest price patterns
- **Crop condition index:** USDA weekly ratings (% good/excellent) regressed against final yield to estimate production in real time

## Prerequisites
- [[Futures Contract]]
- [[Contango Roll Cost]]
- [[Backwardation Roll Gain]]
- [[Delivery]]
- [[Crop Year]]

## Related concepts (learn next)
- [[WASDE]] provides the monthly supply/demand balance that is the primary catalyst for grain price moves.
- [[Old Crop New Crop]] captures the premium between current and upcoming harvest inventories.
- [[Stocks to Use Ratio]] quantifies how tight or loose a grain balance sheet is, driving the price regime.
- [[Weather Premium]] reflects the risk premium for uncertain growing conditions during pollination.
- [[Crush Spread]] measures soybean processing margins, linking beans to meal and oil.
- [[Spread Trade]] is the dominant strategy for professional grain traders who trade calendar and inter commodity spreads.
- [[Basis Risk]] arises when hedging grain exposure at a delivery point different from the physical location.
- [[COT Positioning]] reveals whether managed money is crowded long or short in grain futures.

## Common misconceptions
- **"Grain prices are purely supply driven."** Demand shocks matter enormously. China's 2020 to 2021 corn import surge added $1.50/bu to corn prices even without a US weather problem. Ethanol mandates structurally shifted corn demand by consuming roughly 35% of the US crop.
- **"All grains move together."** Corn and soybeans compete for planted acres but have different demand drivers (feed/ethanol vs. meal/oil). Wheat has its own supply geography (Black Sea, EU, Australia). Inter grain spreads can diverge by 30% or more in a single year.
- **"USDA numbers are always accurate."** [[WASDE]] estimates are revised monthly and can contain large revisions, especially early in the [[Crop Year]] when yield is uncertain. The market frequently disagrees with USDA, creating post report volatility of 3 to 5% in minutes.

## Sources
- CBOT Rulebook and Contract Specifications, CME Group
- "Trading and Hedging with Agricultural Futures and Options" by James B. Bittman
- USDA Economic Research Service, Feed Grains Database
- "Commodity Trading Advisors" edited by Gregoriou, Karavas, L'Habitant, Rouah
