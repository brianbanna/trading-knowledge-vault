---
aliases: [cross asset value, value factor, mean reversion factor]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Value Cross Asset

## Definition
Cross asset value is a systematic factor that buys assets trading below estimated fair value and sells those trading above, applied across FX, commodities, bonds, and equities. Unlike [[Momentum Cross Asset]], which follows trends, value is contrarian: it bets on reversion to a fundamental anchor. In FX, the primary value measure is [[purchasing power parity]] (PPP), comparing current exchange rate to PPP fair value. In commodities, value is proxied by current price vs 5 year average or marginal production cost. In bonds, value compares current real yields to historical norms. Value is the slowest moving systematic factor, with holding periods of months to years. It has positive expected returns over long horizons but can underperform for extended periods (5+ years), making it psychologically difficult.

## Why it matters (commodities and FX)
Value is the contrarian anchor that prevents systematic portfolios from becoming pure trend chasers. In FX, PPP value signals have predicted multi year moves: EUR was 30% undervalued vs PPP in 2000 and appreciated 80% over 8 years; CHF was 40% overvalued in 2015 and partially mean reverted. In commodities, buying metals or energy below marginal production cost has generated strong multi year returns because sub cost prices eventually trigger supply cuts. For portfolio construction, value is most powerful combined with [[Carry Cross Asset]] and [[Momentum Cross Asset]]: 3 factors with low correlation, and value naturally hedges momentum's crash risk (value buys what momentum sells after a reversal). [[Risk Parity]] frameworks with value tilts have historically improved risk adjusted returns.

## Concrete example

**Concrete:** A systematic macro fund computes PPP value scores for all G10 pairs. In 2022 the model flags JPY as 35% undervalued (USDJPY 150 vs PPP fair ~98), NOK as 20% undervalued, CHF as 15% overvalued. Long JPY and NOK, short CHF, sized to 5% annualized vol. Over 3 years JPY appreciates 150 to 128 (capturing 14% of the 35% misalignment), NOK appreciates 8%, CHF weakens 5%. Portfolio earns ~12% cumulative. But the timing was painful: in the first 12 months USDJPY rallied to 162 before reversing, causing a 10% drawdown. A value trader without sufficient risk tolerance would have stopped out at the worst point. In commodities the fund identified natgas at $1.80/MMBtu (below $2.50 production cost) and went long. Natgas spiked to $3.50 within 18 months as producers shut in wells, but the position endured 6 months of decline to $1.50 first.

**Simplified:** Buy cheap, sell expensive, where "cheap" means below some fundamental anchor and "expensive" means above it. The anchor differs by asset: PPP for currencies, production cost for commodities, historical yields for bonds. Value works on long horizons because mispricings take years to resolve. The challenge is sitting through the years before reversion happens, when the trade keeps losing. Value combined with momentum and carry is the standard recipe because each factor's bad periods are different.

## Key mechanics and formulas
- **FX value (PPP based)**: Value score = (PPP fair value - current spot) / current spot; positive = undervalued, negative = overvalued
- **PPP fair value estimate**: from OECD or World Bank PPP data, updated annually
- **Commodity value (mean reversion)**: Value score = (5 year average price - current price) / 5 year average price
- **Commodity value (cost based)**: Value score = (marginal production cost - current price) / marginal production cost; positive = below cost = cheap
- **Bond value**: Value score = current real yield - 10 year average real yield; positive = cheap
- **Portfolio construction**: rank by value score; long most undervalued quintile, short most overvalued; equal risk weight
- **Historical Sharpe**: cross asset value Sharpe ~0.3 to 0.5 standalone; 0.6 to 0.8 combined with momentum and carry
- **Mean reversion half life**: time for half the mispricing to correct. FX PPP half life ~3 to 5 years; commodity ~2 to 4 years

## Prerequisites
- [[Purchasing Power Parity]]
- [[Fair Value]]
- [[Mean Reversion]]
- [[Real Yield]]

## Related concepts (learn next)
- [[Momentum Cross Asset]]: natural complement. Momentum captures trends, value captures reversals; combined Sharpe exceeds either alone.
- [[Carry Cross Asset]]: carry and value can conflict (cheap currency may have low carry) or align (cheap commodity exporter currency may have high carry from resource revenues).
- [[Risk Parity]]: value tilts within risk parity improve long term returns by overweighting cheap assets.
- [[Macro Regime]]: value works best during regime transitions from overvaluation to fair value, worst during persistent bubbles.
- [[CTA]]: CTAs rarely trade value because holding periods are too long and drawdowns too deep for trend mandates.
- [[Real Rates Regime]]: real rate levels are both a value signal for bonds and a driver of FX fair value.
- [[DXY Correlation]]: USD overvaluation vs PPP creates opportunities in commodity currencies inversely correlated with the dollar.

## Common misconceptions
1. **"Cheap assets always recover quickly."** Value is the slowest factor. PPP mispricings persist for 5 to 10 years. A currency 30% undervalued can become 40% undervalued before reverting. Position sizing must account for this.
2. **"PPP is a precise fair value."** PPP is a rough model dependent estimate with wide bands. Different data sources produce estimates differing by 10 to 20%. Directional guide, not precision tool.
3. **"Value and momentum are always negatively correlated."** Weakly negatively correlated on average; in some environments (sharp reversal in an overvalued asset) they both lose simultaneously. Diversification benefit is real but not guaranteed.

## Sources
- Asness, Clifford, Moskowitz, Tobias, Pedersen, Lasse, "Value and Momentum Everywhere," Journal of Finance (2013)
- Rogoff, Kenneth, "The Purchasing Power Parity Puzzle," Journal of Economic Literature (1996)
- Erb, Claude, Harvey, Campbell, "The Strategic and Tactical Value of Commodity Futures," Financial Analysts Journal (2006)
- Koijen, Ralph, Moskowitz, Tobias, Pedersen, Lasse, Vrugt, Evert, "Carry," Journal of Financial Economics (2018)
