---
aliases: [stocks to use, stocks-to-use ratio, S/U ratio, ending stocks ratio]
tags:
  - "#agri/grains"
  - "#quant"
date-added: "2026-03-20"
---

# Stocks to Use Ratio

## Definition
The stocks to use ratio (S/U ratio) is the percentage of a commodity's ending inventory relative to its total annual consumption, calculated as ending stocks divided by total use. It is the single most important metric for assessing whether an agricultural commodity's supply situation is tight, balanced, or in surplus. A lower ratio indicates scarcity and supports higher prices, while a higher ratio signals surplus and pressures prices lower. For US [[Corn]], an S/U ratio below 10% is considered extremely tight, 10 to 15% is tight, and above 15% is comfortable. The ratio is calculated on a [[Crop Year]] basis using data from the [[WASDE]] report published monthly by the USDA. The concept applies across all agricultural commodities and has direct analogues in energy (days of supply) and metals (weeks of supply).

## Why it matters (commodities and FX)
The S/U ratio is the primary quantitative link between fundamental balance sheets and price levels in [[Grains]], oilseeds, and [[Sugar Futures|soft commodities]]. Historically, corn prices exhibit a non linear, convex relationship with S/U: prices decline slowly as S/U rises from 12% to 20%, but spike sharply when S/U drops below 10%. This non linearity creates outsized returns for traders who identify tightening balances before the market fully prices them in. The ratio also determines the shape of the forward curve: low S/U favors [[Backwardation Roll Gain|backwardation]], while high S/U favors [[Contango Roll Cost|contango]].

## Concrete example
**Success case:** In August 2020, US corn S/U was projected at 17.6% (comfortable). By January 2021, surging Chinese corn imports and strong ethanol demand led USDA to cut ending stocks, dropping S/U to 10.3%. A trader who went long December 2021 corn at $4.00/bu in September 2020 saw prices reach $5.80/bu by March 2021, a $9,000 per contract gain. The S/U decline from 17.6% to 10.3% correctly signaled a regime shift from surplus to scarcity.

**Failure case:** In 2015, a trader shorted corn at $4.00/bu expecting the 19% S/U ratio to rise further on continued record yields. Instead, USDA revised demand higher over several months, and S/U stabilized near 18%. Corn traded sideways between $3.50 and $4.20 for 4 months. The short earned only $0.15/bu after carry costs, delivering a near breakeven result. The lesson: a high but stable S/U does not guarantee further price declines when demand is absorbing supply growth.

## Key mechanics and formulas
- **Stocks to Use Ratio = Ending stocks / Total use x 100**
- **Total use = Domestic consumption + Exports**
- **Ending stocks = Beginning stocks + Production + Imports - Total use**
- **Price sensitivity (US corn):** Each 1 percentage point decline in S/U below 12% historically corresponds to roughly $0.30 to $0.50/bu of price increase
- **Threshold levels (US corn):** below 8% = rationing/crisis; 8 to 12% = tight; 12 to 16% = balanced; above 16% = surplus
- **Threshold levels (global wheat):** below 25% = tight; 25 to 30% = balanced; above 30% = comfortable
- **Non linearity:** The price versus S/U relationship is convex; plotting historical prices against S/U reveals the steep curve below critical thresholds

## Prerequisites
- [[Grains]]
- [[WASDE]]
- [[Crop Year]]
- [[Futures Contract]]

## Related concepts (learn next)
- [[WASDE]] is the primary data source for calculating S/U ratios across all major crops globally.
- [[Old Crop New Crop]] spreads widen when old crop S/U is significantly lower than projected new crop S/U.
- [[Weather Premium]] is justified when adverse conditions threaten to push S/U below critical thresholds.
- [[Backwardation Roll Gain]] is most persistent when S/U is low and nearby contracts price in current scarcity.
- [[Contango Roll Cost]] dominates when S/U is high and storage economics drive the forward curve.
- [[COT Positioning]] tends to reach extreme long levels when S/U is low and extreme short when S/U is high.
- [[Crush Spread]] reacts to soybean S/U changes that affect processing margins and crusher throughput incentives.
- [[Basis Risk]] increases in tight S/U environments as regional supply imbalances widen relative to national averages.

## Common misconceptions
- **"A universal S/U threshold applies to all commodities."** Corn below 10% is crisis level, but global wheat below 25% is already tight. Each commodity has its own critical thresholds based on demand elasticity, storability, and the availability of substitutes.
- **"S/U is static between WASDE reports."** Weekly export sales data, ethanol production reports, and private crop estimates cause the market to continuously re estimate S/U between official USDA monthly updates.
- **"Low S/U guarantees higher prices."** If the market has already priced in tight stocks, further upside requires S/U to tighten beyond current expectations. A low S/U that stabilizes can lead to price consolidation or even a decline if demand destruction occurs at elevated price levels.

## Sources
- USDA Economic Research Service, Feed Grains Database
- Westcott, P. and Hoffman, L., "Price Determination for Corn and Wheat," USDA Technical Bulletin
- "Commodity Price Dynamics: A Structural Approach" by Craig Pirrong
- CME Group, "Understanding Grain Stocks and Usage"
