---
aliases: [crop year, marketing year, crop cycle]
tags:
  - "#agri/grains"
date-added: "2026-03-20"
---

# Crop Year

## Definition
A crop year (also called a marketing year) is the 12 month period that defines the production and consumption cycle for a specific agricultural commodity, beginning approximately when the new harvest enters the market and ending just before the next harvest. Unlike the calendar year, crop years vary by commodity and by hemisphere, reflecting when supply physically becomes available. For US [[Corn]] and [[Soybeans]], the crop year runs from September 1 to August 31; for US [[Wheat]], it runs from June 1 to May 31. Southern Hemisphere producers like Brazil and Argentina operate on different crop years reflecting their opposite growing seasons (e.g., Brazilian soybeans roughly February to January). The crop year framework is essential because all [[WASDE]] balance sheet data, including beginning stocks, production, and ending stocks, is organized on a crop year basis. Understanding which crop year a futures contract references determines whether it is [[Old Crop New Crop|old crop or new crop]].

## Why it matters (commodities and FX)
The crop year defines the time horizon for all supply and demand analysis: a deficit in the 2025/26 crop year means tightness from September 2025 through August 2026 for corn. Traders who confuse calendar year and crop year data will miscalculate [[Stocks to Use Ratio]] and produce flawed fundamental conclusions. Spread trades between contracts straddling crop year boundaries ([[Old Crop New Crop]] spreads) are among the highest conviction and most actively traded structures in agricultural markets. FX flows tied to agricultural exports (e.g., Brazilian real strength during Brazil's soybean export season from March to June) follow crop year timing rather than calendar year timing.

## Concrete example
**Success case:** A trader in March 2021 noticed that the US 2020/21 corn crop year (Sep 2020 to Aug 2021) had ending stocks projected at only 1.1 billion bushels, a [[Stocks to Use Ratio]] of 7.4%. They bought July 2021 (old crop) corn at $5.00/bu and sold December 2021 (new crop) corn at $4.60/bu, trading the old crop premium. By May, the July/December spread widened to $1.80, netting $0.80/bu profit or $4,000 per spread.

**Failure case:** A trader in October 2018 assumed that strong US corn demand would tighten the 2018/19 crop year. They went long March 2019 corn at $3.75/bu. However, the 2018 harvest was a record 14.4 billion bushels, and ending stocks ballooned to 2.1 billion bushels. Corn fell to $3.55/bu by January, a $1,000 per contract loss. The lesson: a massive harvest at the start of a crop year can overwhelm even strong demand growth.

## Key mechanics and formulas
- **US Corn crop year:** September 1 to August 31
- **US Soybeans crop year:** September 1 to August 31
- **US Wheat crop year:** June 1 to May 31
- **Brazil Soybeans crop year:** approximately February 1 to January 31
- **Balance sheet mapping:** Beginning stocks (crop year start) + Production + Imports = Total supply; Total supply - Domestic use - Exports = Ending stocks (crop year end)
- **Crop year alignment:** To compare global supply, analysts must reconcile different national crop years into a single aggregate. [[WASDE]] uses a "local marketing year" approach for each country.
- **Futures to crop year:** US corn September futures = last month of old crop; December futures = first major contract of new crop

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
- [[Backwardation Roll Gain]] tends to be strongest in late crop year months when old crop supplies are tightest.
- [[Basis Risk]] can shift seasonally within a crop year as local supply and demand patterns evolve with harvest and logistics.

## Common misconceptions
- **"Crop year and calendar year are interchangeable."** Using calendar year data to analyze a commodity priced on a September to August crop year will produce incorrect supply/demand conclusions and flawed [[Stocks to Use Ratio]] calculations.
- **"All grains share the same crop year."** Wheat, corn, and soybeans each have different crop year start dates, and Southern Hemisphere crop years are offset by roughly 6 months from their Northern Hemisphere equivalents.
- **"The crop year is fixed globally."** Even within a single commodity, the US, EU, Brazil, and Australia crop years can differ by months, complicating global balance sheet aggregation and requiring careful alignment in models.

## Sources
- USDA Economic Research Service, "Commodity Marketing Year Definitions"
- "Fundamentals of the Grain Market" by CME Group Institute
- "Commodity Trading Advisors" edited by Gregoriou, Karavas, L'Habitant, Rouah
