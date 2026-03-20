---
aliases: [WASDE, World Agricultural Supply and Demand Estimates, USDA WASDE, USDA report]
tags:
  - "#agri/grains"
  - "#agri/oilseeds"
date-added: "2026-03-20"
---

# WASDE

## Definition
The World Agricultural Supply and Demand Estimates (WASDE) is a comprehensive monthly report published by the United States Department of Agriculture (USDA) that provides global supply and demand forecasts for major crops including [[Corn]], [[Wheat]], [[Soybeans]], [[Rice]], [[Cotton Futures|cotton]], and [[Sugar Futures|sugar]]. The report is released around the 10th of each month at 12:00 PM Eastern Time, with agricultural futures markets often experiencing extreme volatility in the minutes surrounding publication. WASDE covers beginning stocks, production, imports, domestic consumption, exports, and ending stocks for each commodity across all major producing and consuming countries. It is the agricultural commodity market's equivalent of the EIA Weekly Petroleum Status Report for crude oil, serving as the benchmark reference for global crop pricing. The report is compiled by an interagency committee that enters a "lockup" procedure to prevent information leaks before release. WASDE numbers set the consensus baseline for global [[Grains]] and oilseed pricing until the next monthly update arrives.

## Why it matters (commodities and FX)
WASDE is the single most market moving scheduled event for agricultural futures, routinely causing 3 to 5% price swings in [[Corn]], [[Wheat]], and [[Soybeans]] within minutes of release. The ending stocks figure and its implied [[Stocks to Use Ratio]] directly determine whether a market is in surplus or deficit, shaping the entire forward curve structure from [[Contango Roll Cost|contango]] to [[Backwardation Roll Gain|backwardation]]. For FX traders, WASDE outcomes affect currencies of major exporters: a bullish corn report strengthens [[BRL/USD]] sentiment via Brazil's export revenue expectations. Commodity trading firms build entire research teams around anticipating WASDE revisions and trading the post report price adjustment.

## Concrete example
**Success case:** In January 2023, WASDE cut Argentina's soybean production estimate by 8 million metric tons due to La Nina drought, dropping the global [[Stocks to Use Ratio]] to 23%. A trader long March soybean futures at $14.80/bu before the report saw soybeans gap to $15.40/bu within 10 minutes, a $3,000 per contract gain. The trader had pre positioned based on satellite imagery showing severe Argentine crop stress that USDA had not yet incorporated.

**Failure case:** In June 2019, WASDE surprised by raising US corn planted acreage estimates despite widespread flooding in the Midwest. A trader who was long December corn at $4.50/bu expecting a planted area cut saw corn drop $0.25/bu intraday, a $1,250 per contract loss. The lesson: USDA survey methodology can diverge from market consensus derived from satellite and field reports.

## Key mechanics and formulas
- **Balance sheet identity:** Ending stocks = Beginning stocks + Production + Imports - Domestic use - Exports
- **[[Stocks to Use Ratio]] = Ending stocks / (Domestic use + Exports) x 100**
- **Production = Harvested area x Yield**
- **Surprise = WASDE estimate - Trade consensus estimate** (consensus measured via pre report surveys from Reuters, Bloomberg)
- **Price sensitivity (corn):** A 100 million bushel surprise in US corn ending stocks historically moves corn futures approximately $0.10 to $0.15/bu
- **Release schedule:** Monthly, typically the 2nd Thursday or Friday of each month at 12:00 PM ET

## Prerequisites
- [[Grains]]
- [[Stocks to Use Ratio]]
- [[Crop Year]]
- [[Old Crop New Crop]]
- [[Futures Contract]]

## Related concepts (learn next)
- [[Stocks to Use Ratio]] is the key derived metric from WASDE that summarizes whether a crop is in surplus or deficit.
- [[Old Crop New Crop]] spread reacts sharply to WASDE changes in current year versus next year balance sheets.
- [[Weather Premium]] builds into prices when WASDE yield assumptions are at risk from adverse growing conditions.
- [[COT Positioning]] shows whether speculators have already priced in expected WASDE outcomes before release.
- [[Grains]] are the primary asset class affected by WASDE data each month.
- [[Crush Spread]] reacts when WASDE revises soybean meal or soybean oil supply and demand estimates.
- [[Implied Volatility]] in grain options typically spikes heading into WASDE and collapses after the release.
- [[Basis Risk]] can increase when WASDE shifts national level estimates that diverge from local supply conditions.

## Common misconceptions
- **"WASDE is the final word on supply and demand."** WASDE is revised every month, and intra month developments (weather, export sales, policy changes) can make the latest report stale within days. Private analysts at firms like StoneX, AgResource, and Informa frequently disagree with USDA estimates.
- **"You can trade WASDE by reacting to the headline number."** The market reacts to the full balance sheet: a bearish production number can be offset by a simultaneous demand cut. Traders must parse beginning stocks, production, each demand category, and exports simultaneously.
- **"WASDE only matters for US markets."** WASDE includes global estimates for Brazil, Argentina, China, India, EU, and dozens of other countries. A revision to Brazilian soybean output can move US soybean futures as much as a domestic revision.

## Sources
- USDA Office of the Chief Economist, WASDE Archives (usda.gov/oce/commodity/wasde)
- "Commodity Price Dynamics: A Structural Approach" by Craig Pirrong
- CME Group, "Understanding USDA Reports" educational series
- Irwin, S. and Good, D., "The Accuracy of USDA Crop Production Forecasts," farmdoc daily, University of Illinois
