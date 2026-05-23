---
aliases: [crop year, marketing year, crop cycle]
tags:
  - "#agri/grains"
date-added: "2026-03-20"
---

# Crop Year

## Definition
A crop year (marketing year) is the 12 month window defining production and consumption for one commodity, starting when the new harvest enters the market. Crop years vary by commodity and hemisphere. US [[Corn]] and [[Soybeans]]: September 1 to August 31. US [[Wheat]]: June 1 to May 31. Brazilian soybeans: roughly February to January. All [[WASDE]] balance sheet data (beginning stocks, production, ending stocks) is organized on a crop year basis. The crop year a futures contract references determines whether it is [[Old Crop New Crop|old crop or new crop]].

## Why it matters (commodities and FX)
The crop year defines the time horizon for supply and demand analysis. A deficit in the 2025/26 corn crop year means tightness from September 2025 through August 2026. Mixing calendar and crop year data corrupts [[Stocks to Use Ratio]] math. [[Old Crop New Crop]] spreads straddling the boundary are among the highest conviction trades in agricultural markets. FX flows tied to ag exports (BRL strength during Brazil's March to June soybean window) follow crop year timing, not calendar year.

## Concrete example
**Concrete:** March 2021. US 2020/21 corn ending stocks projected at 1.1 billion bushels, [[Stocks to Use Ratio]] of 7.4%. Trader buys July 2021 (old crop) at $5.00/bu, sells December 2021 (new crop) at $4.60/bu. By May the July/December spread widens to $1.80, netting $0.80/bu or $4,000 per spread.

**Simplified:** The supply year for corn runs September to August, not January to December. If this year's harvest is small, prices for delivery before next harvest stay high while prices after the new harvest stay lower. Trading that gap is the old crop vs new crop spread. Using calendar year stats instead of crop year stats gives you the wrong picture of how much grain is actually available.

## Key mechanics and formulas
- **US Corn:** September 1 to August 31
- **US Soybeans:** September 1 to August 31
- **US Wheat:** June 1 to May 31
- **Brazil Soybeans:** approximately February 1 to January 31
- **Balance sheet:** Beginning stocks + Production + Imports = Supply; Supply − Domestic use − Exports = Ending stocks
- **Aggregation:** [[WASDE]] uses local marketing year per country, then reconciles to global totals
- **Futures mapping:** US corn September = last old crop month; December = first new crop month

## Prerequisites
- [[Grains]]
- [[Futures Contract]]
- [[WASDE]]
- [[Delivery]]

## Related concepts (learn next)
- [[Old Crop New Crop]] spreads are defined and priced relative to the crop year boundary.
- [[WASDE]] reports all balance sheet data organized by crop year rather than calendar year.
- [[Stocks to Use Ratio]] is calculated on a crop year basis to properly assess supply tightness.
- [[Weather Premium]] is most relevant during the growing season portion of the crop year.
- [[Contango Roll Cost]] can differ across contracts within versus straddling crop years.
- [[Backwardation Roll Gain]] is strongest in late crop year months when old crop supplies are tightest.
- [[Basis Risk]] shifts seasonally within a crop year as local supply and demand patterns evolve.

## Common misconceptions

**"Crop year and calendar year are interchangeable."** Calendar year data on a September to August commodity produces wrong supply conclusions and broken [[Stocks to Use Ratio]] math.

**"All grains share the same crop year."** Wheat, corn, and soybeans start on different dates. Southern Hemisphere crop years are offset 6 months from Northern Hemisphere equivalents.

**"The crop year is fixed globally."** US, EU, Brazil, and Australia crop years differ by months even for the same commodity. Global balance sheet aggregation requires explicit alignment.

## Sources
- USDA Economic Research Service, "Commodity Marketing Year Definitions"
- "Fundamentals of the Grain Market" by CME Group Institute
- "Commodity Trading Advisors" edited by Gregoriou, Karavas, L'Habitant, Rouah
