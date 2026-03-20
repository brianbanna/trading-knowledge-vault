---
aliases: [cross asset value, value factor, mean reversion factor]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Value Cross Asset

## Definition
Cross-asset value is a systematic investment factor that buys assets trading below their estimated fair value and sells assets trading above it, applied across FX, commodities, bonds, and equities. Unlike [[Momentum Cross Asset]], which follows recent price trends, value is contrarian: it bets on mean reversion to a fundamental anchor. In FX, the primary value measure is [[purchasing power parity]] (PPP), comparing a currency's current exchange rate to its PPP-implied fair value. In commodities, value is often proxied by comparing the current price to its 5 year average or to marginal production cost. In bonds, value compares current real yields to historical norms. Value is the slowest-moving of the major systematic factors, with typical holding periods of months to years. It has positive expected returns over long horizons but can underperform for extended periods (5+ years in some cases), making it psychologically and practically difficult to implement.

## Why it matters (commodities and FX)
Value provides the contrarian anchor that prevents systematic portfolios from becoming pure trend chasers. In FX, PPP-based value signals have predicted multi-year currency moves: the EUR was 30% undervalued relative to PPP in 2000 and subsequently appreciated 80% over 8 years; the CHF was 40% overvalued in 2015 and has since partially mean-reverted. In commodities, buying metals or energy when prices are well below marginal production cost has generated strong multi-year returns because sub-cost prices eventually cause supply cuts that push prices higher. For portfolio construction, value is most powerful when combined with [[Carry Cross Asset]] and [[Momentum Cross Asset]], as the 3 factors have low correlation, and value acts as a natural hedge against momentum's crash risk (value tends to buy what momentum has sold after a reversal). [[Risk Parity]] frameworks that incorporate value tilts have historically improved risk-adjusted returns.

## Concrete example
A systematic macro fund computes PPP-based value scores for all G10 currency pairs. In 2022, the model identifies JPY as 35% undervalued (USDJPY at 150 vs. PPP fair value around 98), NOK as 20% undervalued, and CHF as 15% overvalued. The fund goes long JPY and NOK, short CHF, with position sizes proportional to the deviation from fair value, scaled to 5% annualized volatility. Over 3 years, JPY appreciates from 150 to 128 (capturing 14% of the 35% misalignment), NOK appreciates 8%, and CHF weakens 5%. The portfolio earns approximately 12% cumulative. However, the timing was painful: in the first 12 months, USDJPY rallied further to 162 before reversing, causing a 10% drawdown. A value trader without sufficient risk tolerance would have stopped out at the worst point. In commodities, the fund identified natural gas at $1.80/MMBtu as below the $2.50 average production cost and went long. Natural gas eventually spiked to $3.50 within 18 months as producers shut in wells, but the position endured 6 months of further decline to $1.50 before the reversal.

## Key mechanics and formulas
- **FX value (PPP-based)**: Value score = (PPP fair value - current spot rate) / current spot rate; positive = undervalued, negative = overvalued
- **PPP fair value estimate**: typically derived from OECD or World Bank PPP data, updated annually
- **Commodity value (mean reversion)**: Value score = (5 year average price - current price) / 5 year average price
- **Commodity value (cost-based)**: Value score = (marginal production cost - current price) / marginal production cost; positive = below cost = cheap
- **Bond value**: Value score = current real yield - 10 year average real yield; positive = cheap (yields unusually high)
- **Portfolio construction**: rank assets by value score; go long most undervalued quintile, short most overvalued quintile; equal-risk-weight
- **Historical Sharpe**: cross-asset value Sharpe approximately 0.3 to 0.5 standalone; 0.6 to 0.8 when combined with momentum and carry
- **Mean reversion half-life**: the time for half the mispricing to correct; FX PPP half-life is approximately 3 to 5 years; commodity mean reversion half-life is approximately 2 to 4 years

## Prerequisites
- [[Purchasing Power Parity]]
- [[Fair Value]]
- [[Mean Reversion]]
- [[Real Yield]]

## Related concepts (learn next)
- [[Momentum Cross Asset]]: the natural complement; momentum captures trends, value captures reversals, and the combination is more robust than either alone.
- [[Carry Cross Asset]]: carry and value can conflict (a cheap currency may have low carry) or align (a cheap commodity exporter currency may have high carry from resource revenues).
- [[Risk Parity]]: value tilts within a risk parity framework improve long-term returns by overweighting cheap assets.
- [[Macro Regime]]: value works best during regime transitions (e.g., from overvaluation to fair value) and worst during persistent bubbles.
- [[CTA]]: CTAs rarely trade value signals because the holding period is too long and drawdowns too deep for trend-following mandates.
- [[Real Rates Regime]]: real rate levels are both a value signal for bonds and a driver of FX fair value.
- [[DXY Correlation]]: USD overvaluation relative to PPP creates opportunities in commodity currencies that tend to be inversely correlated with the dollar.

## Common misconceptions
1. **"Cheap assets always recover quickly"**: Value is the slowest factor. PPP mispricings can persist for 5 to 10 years. A currency can be 30% undervalued and get 40% undervalued before it mean-reverts. Position sizing must account for this uncertainty.
2. **"PPP is a precise fair value"**: PPP is a rough, model-dependent estimate with wide confidence bands. Different data sources and calculation methods produce PPP estimates that can differ by 10 to 20%. It is a directional guide, not a precision tool.
3. **"Value and momentum are always negatively correlated"**: They are weakly negatively correlated on average, but during certain market environments (e.g., a sharp reversal in an overvalued asset), they can both lose simultaneously. The diversification benefit is real but not guaranteed.

## Sources
- Asness, Clifford, Moskowitz, Tobias, Pedersen, Lasse, "Value and Momentum Everywhere," Journal of Finance (2013)
- Rogoff, Kenneth, "The Purchasing Power Parity Puzzle," Journal of Economic Literature (1996)
- Erb, Claude, Harvey, Campbell, "The Strategic and Tactical Value of Commodity Futures," Financial Analysts Journal (2006)
- Koijen, Ralph, Moskowitz, Tobias, Pedersen, Lasse, Vrugt, Evert, "Carry," Journal of Financial Economics (2018)
