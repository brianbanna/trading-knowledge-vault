---
aliases: [stocks to use, stocks-to-use ratio, S/U ratio, ending stocks ratio]
tags:
  - "#agri/grains"
  - "#quant"
date-added: "2026-03-20"
---

# Stocks to Use Ratio

## Definition
The stocks to use ratio (S/U ratio) is ending inventory divided by total annual consumption, calculated as ending stocks divided by total use. It is the single most important metric for assessing whether an agricultural commodity is tight, balanced, or in surplus. Lower ratio = scarcity, supports higher prices; higher = surplus, pressures prices lower. For US [[Corn]], S/U below 10% is extremely tight, 10 to 15% is tight, above 15% is comfortable. Calculated on a [[Crop Year]] basis from [[WASDE]] data published monthly by USDA. The concept applies across all agricultural commodities and has direct analogues in energy (days of supply) and metals (weeks of supply).

## Why it matters (commodities and FX)
The S/U ratio is the primary quantitative link between fundamental balance sheets and price levels in [[Grains]], oilseeds, and [[Sugar Futures|soft commodities]]. Historically, corn prices show a non linear convex relationship with S/U: prices decline slowly as S/U rises from 12% to 20%, but spike sharply below 10%. This non linearity creates outsized returns for traders who identify tightening balances before the market fully prices them in. The ratio also drives forward curve shape: low S/U favors [[Backwardation Roll Gain|backwardation]], high S/U favors [[Contango Roll Cost|contango]].

## Concrete example

**Concrete:** August 2020 US corn S/U projected at 17.6% (comfortable). By January 2021, surging Chinese imports and strong ethanol demand led USDA to cut ending stocks, dropping S/U to 10.3%. A trader long December 2021 corn at $4.00/bu from September 2020 saw prices reach $5.80/bu by March 2021, a $9,000 per contract gain. The S/U decline from 17.6% to 10.3% correctly signaled a regime shift from surplus to scarcity. Contrast: 2015, a trader shorted corn at $4.00 expecting the 19% S/U to rise further on record yields. Instead USDA revised demand higher and S/U stabilized near 18%. Corn traded sideways $3.50 to $4.20 for 4 months. The short earned $0.15/bu after carry, near breakeven. High but stable S/U does not guarantee further price declines when demand absorbs supply growth.

**Simplified:** S/U is how many months of consumption sit in storage. Low number means you cannot afford a bad harvest or a demand spike, and prices rise to ration usage. High number means you can absorb shocks and prices stay calm. The relationship is not linear: prices barely move as S/U drops from 20% to 12%, then explode as it drops from 10% to 6%. The asymmetry is where the money is for fundamental traders.

## Key mechanics and formulas
- **Stocks to Use Ratio = Ending stocks / Total use × 100**
- **Total use = Domestic consumption + Exports**
- **Ending stocks = Beginning stocks + Production + Imports - Total use**
- **Price sensitivity (US corn):** Each 1 pp decline in S/U below 12% corresponds to ~$0.30 to $0.50/bu price increase
- **Threshold levels (US corn):** below 8% = rationing/crisis; 8 to 12% = tight; 12 to 16% = balanced; above 16% = surplus
- **Threshold levels (global wheat):** below 25% = tight; 25 to 30% = balanced; above 30% = comfortable
- **Non linearity:** Convex price vs S/U relationship; plotting historical prices against S/U reveals the steep curve below critical thresholds

## Prerequisites
- [[Grains]]
- [[WASDE]]
- [[Crop Year]]
- [[Futures Contract]]

## Related concepts (learn next)
- [[WASDE]] is the primary data source for S/U ratios globally.
- [[Old Crop New Crop]] spreads widen when old crop S/U is much lower than projected new crop S/U.
- [[Weather Premium]] is justified when adverse conditions threaten S/U below critical thresholds.
- [[Backwardation Roll Gain]] persists when S/U is low and nearby contracts price current scarcity.
- [[Contango Roll Cost]] dominates when S/U is high and storage economics drive the forward curve.
- [[COT Positioning]] reaches extreme long levels when S/U is low and extreme short when S/U is high.
- [[Crush Spread]] reacts to soybean S/U changes affecting processing margins.
- [[Basis Risk]] increases in tight S/U environments as regional supply imbalances widen.

## Common misconceptions
- **"A universal S/U threshold applies to all commodities."** Corn below 10% is crisis; global wheat below 25% is already tight. Each commodity has its own thresholds based on demand elasticity, storability, and substitutes.
- **"S/U is static between WASDE reports."** Weekly export sales, ethanol production reports, and private crop estimates make the market re estimate S/U continuously between monthly USDA updates.
- **"Low S/U guarantees higher prices."** If the market has priced tight stocks already, further upside requires S/U to tighten beyond current expectations. A low but stable S/U can lead to consolidation or decline if demand destruction occurs at elevated prices.

## Sources
- USDA Economic Research Service, Feed Grains Database
- Westcott, P. and Hoffman, L., "Price Determination for Corn and Wheat," USDA Technical Bulletin
- "Commodity Price Dynamics: A Structural Approach" by Craig Pirrong
- CME Group, "Understanding Grain Stocks and Usage"
