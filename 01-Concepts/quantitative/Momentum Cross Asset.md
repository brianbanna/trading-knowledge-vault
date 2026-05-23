---
aliases: [cross asset momentum, time series momentum, TSMOM]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Momentum Cross Asset

## Definition
Cross asset momentum is a systematic factor that exploits the tendency of recent winners to keep winning and recent losers to keep losing, applied across equities, bonds, commodities, and FX. The standard implementation is time series momentum (TSMOM), where each asset's own past return drives long or short positioning, in contrast to cross sectional momentum which ranks assets relatively. Momentum is statistically significant across 100+ years of data and dozens of markets. It is the most robust systematic factor, the core of [[CTA]] (managed futures) strategies running hundreds of billions in AUM. The economic explanation combines behavioral biases (under reaction to news, herding, anchoring) with structural flows (stops, margin calls, risk parity deleveraging).

## Why it matters (commodities and FX)
Momentum is the dominant factor in commodity futures. Energy, metals, and agricultural futures show strong trend persistence because supply/demand fundamentals move slowly: an oil supply shock plays out over months as production adjusts. FX momentum (trend following on currency pairs) has been profitable since at least the 1970s, driven by central bank policy divergence, capital flow persistence, and slow [[macro regime]] changes. [[CTA]]s allocate most of their risk to momentum, making CTA positioning a significant [[flow signals]] source in commodity and FX markets. Momentum also serves as a crisis hedge: during 2008, TSMOM across commodities and FX was profitable because it was short equities and long bonds, having captured the trend over months.

## Concrete example
**Concrete:** A TSMOM strategy trades 40 futures markets (10 equity indices, 10 bonds, 10 commodities, 10 FX pairs). Each month, the 12 month excess return determines sign: positive = long 1 unit of risk, negative = short. Positions sized to equal volatility via trailing 60 day realized vol. In 2022 the strategy is short bonds (12M return negative as rates rise), long crude and natgas (12M positive), short EURUSD and GBPUSD (USD strength), long USDJPY. Earns 28%, best since 2008. In 2023 the same strategy struggles: crude reverses, bonds stabilize, FX trends fade. Loses 5% as multiple positions whipsaw. Momentum works over multi year horizons but has painful reversal periods at [[macro regime]] inflection points.

**Simplified:** Buy what is going up, sell what is going down, across every market you can. Size each bet by its volatility so no single market dominates. Hold until the trend dies. The strategy works because real fundamentals (earnings, policy, weather, supply chains) move slowly, and prices catch up gradually. It fails at turning points: every market reverses at once and the system is on the wrong side of all of them. Diversification across markets and lookbacks softens but does not eliminate this.

## Key mechanics and formulas
- **TSMOM signal**: Signal(i) = sign(excess return of asset i over lookback); +1 = long, -1 = short
- **Lookback periods**: 1, 3, 6, and 12 months common; blending reduces turnover and whipsaw
- **Position sizing (volatility targeting)**: Position size(i) = (target vol / realized vol(i)) × signal(i)
- **Portfolio return**: R(portfolio) = (1 / N) × sum(signal(i) × return(i) × target vol / vol(i)) for N assets
- **Historical Sharpe**: TSMOM across all asset classes delivered Sharpe ~0.8 to 1.0 over 1985 to 2025; individual asset class Sharpe 0.4 to 0.7
- **Exponential moving average signal**: Signal = fast EMA - slow EMA; common pair 8/24 day (medium term), 16/64 day (slower trend)
- **Maximum drawdown (historical)**: worst drawdown for diversified TSMOM is 15 to 25%, during sharp reversals

## Prerequisites
- [[Volatility]]
- [[Time Series]]
- [[Futures]]
- [[Risk Management]]

## Related concepts (learn next)
- [[Carry Cross Asset]]: carry and momentum are partially uncorrelated; combined Sharpe exceeds either alone.
- [[Value Cross Asset]]: natural complement; buys what momentum sold (cheapened assets) and vice versa.
- [[CTA]]: primary institutional vehicle for systematic momentum.
- [[Risk Parity]]: position sizing framework; momentum provides directional signal.
- [[Macro Regime]]: momentum profits peak during persistent regimes, fall at transitions.
- [[Positioning Signal]]: extreme momentum positioning (everyone long the same trend) signals crowding and reversal risk.
- [[Correlation Breakdown]]: momentum contributes to correlation breakdowns when many CTAs deleverage at once.

## Common misconceptions
1. **"Momentum is just chasing past returns."** Momentum mechanically buys winners, but profitability reflects economic content: assets trend because fundamentals (earnings, policy, supply/demand) evolve gradually. Past returns are a noisy proxy for the slow fundamental.
2. **"Faster signals are always better."** Shorter lookbacks raise turnover and costs. After costs, 1 month momentum often underperforms blended 3/6/12 month for most assets.
3. **"Momentum works all the time."** Extended losing periods (6 to 18 months) during range bound markets or sharp reversals. The 2009 equity rally and 2023 cross asset chop caused significant momentum drawdowns. Patience and diversification across assets and lookbacks are essential.
4. **"TSMOM and cross sectional momentum are the same."** TSMOM takes absolute positions (long or short each asset based on its own return). Cross sectional momentum takes relative positions (long top, short bottom). Different risk profiles and factor exposures.

## Sources
- Moskowitz, Tobias, Ooi, Yao Hua, Pedersen, Lasse, "Time Series Momentum," Journal of Financial Economics (2012)
- Asness, Clifford, Moskowitz, Tobias, Pedersen, Lasse, "Value and Momentum Everywhere," Journal of Finance (2013)
- Hurst, Brian, Ooi, Yao Hua, Pedersen, Lasse, "A Century of Evidence on Trend-Following Investing," AQR Capital Management (2017)
- Baltas, Nick, Kosowski, Robert, "Momentum Strategies in Futures Markets and Trend-Following Funds," Working Paper (2013)
