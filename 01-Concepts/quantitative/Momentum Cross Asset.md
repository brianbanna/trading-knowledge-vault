---
aliases: [cross asset momentum, time series momentum, TSMOM]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Momentum Cross Asset

## Definition
Cross-asset momentum is a systematic trading factor that exploits the tendency for assets that have recently risen to continue rising, and assets that have recently fallen to continue falling, across all major asset classes: equities, bonds, commodities, and FX. The most common implementation is time-series momentum (TSMOM), where each asset's own past return determines whether to go long or short, as opposed to cross-sectional momentum, which ranks assets relative to each other. Momentum has been documented as statistically significant across more than 100 years of data and across dozens of markets. It is the most robust and well-studied systematic factor, forming the core of [[CTA]] (managed futures) strategies that collectively manage hundreds of billions of dollars. The economic explanation combines behavioral biases (under-reaction to news, herding, anchoring) with structural flows (stop-losses, margin calls, forced selling by risk-parity deleveraging).

## Why it matters (commodities and FX)
Momentum is the dominant factor in commodity futures trading. Energy, metals, and agricultural futures exhibit strong trend persistence due to slow-moving supply/demand fundamentals: an oil supply shock does not resolve in days but plays out over months as production adjusts. FX momentum (trend following on currency pairs) has been profitable since at least the 1970s, driven by central bank policy divergence, capital flow persistence, and slow-moving [[macro regime]] changes. [[CTA]]s allocate the majority of their risk budget to momentum strategies, making CTA positioning a significant source of [[flow signals]] in both commodity and FX markets. Momentum also serves as a crisis hedge: during the 2008 financial crisis, TSMOM strategies across commodities and FX were profitable because they were short equities and long bonds, having captured the trend that developed over months.

## Concrete example
A TSMOM strategy trades 40 futures markets (10 equity indices, 10 bond futures, 10 commodity futures, 10 FX pairs). For each market, it computes the 12 month excess return. If the return is positive, it goes long 1 unit of risk; if negative, short 1 unit of risk. Each position is sized to contribute equal volatility (using the trailing 60 day realized volatility as the scaling denominator). In 2022, the strategy is short bonds (12 month return deeply negative as rates rise), long crude oil and natural gas (12 month return strongly positive), short EURUSD and GBPUSD (12 month return negative as USD strengthens), and long USDJPY. The portfolio earns 28% for the year, its best since 2008. In 2023, the same strategy struggles: crude oil reverses, bonds stabilize, and FX trends fade. The strategy loses 5% as multiple positions whipsaw. The key lesson: momentum works over multi-year horizons but has painful reversal periods, particularly at [[macro regime]] inflection points.

## Key mechanics and formulas
- **TSMOM signal**: Signal(i) = sign(excess return of asset i over lookback period); +1 = long, -1 = short
- **Lookback periods**: commonly 1, 3, 6, and 12 months; blending multiple lookbacks reduces turnover and whipsaw
- **Position sizing (volatility targeting)**: Position size(i) = (target vol / realized vol(i)) x signal(i)
- **Portfolio return**: R(portfolio) = (1 / N) x sum(signal(i) x return(i) x target vol / vol(i)) for N assets
- **Historical Sharpe**: TSMOM across all asset classes has delivered a Sharpe of approximately 0.8 to 1.0 over 1985 to 2025; individual asset class Sharpe is lower (0.4 to 0.7)
- **Exponential moving average signal (alternative)**: Signal = fast EMA - slow EMA; common pair: 8/24 day for medium-term, 16/64 day for slower trend
- **Maximum drawdown (historical)**: the worst drawdown for diversified TSMOM strategies is typically 15 to 25%, occurring during sharp trend reversals

## Prerequisites
- [[Volatility]]
- [[Time Series]]
- [[Futures]]
- [[Risk Management]]

## Related concepts (learn next)
- [[Carry Cross Asset]]: carry and momentum are partially uncorrelated; combining them produces a higher Sharpe than either alone.
- [[Value Cross Asset]]: value is the natural complement to momentum; it buys what momentum has sold (cheapened assets) and vice versa.
- [[CTA]]: the primary institutional vehicle for systematic momentum strategies.
- [[Risk Parity]]: risk parity provides the position sizing framework; momentum provides the directional signal.
- [[Macro Regime]]: momentum profits are highest during persistent regimes and lowest at regime transitions.
- [[Positioning Signal]]: extreme momentum positioning (everyone is long the same trend) signals potential crowding and reversal risk.
- [[Correlation Breakdown]]: momentum strategies can contribute to correlation breakdowns when many CTAs deleverage simultaneously.

## Common misconceptions
1. **"Momentum is just chasing past returns"**: While momentum mechanically buys winners, its profitability reflects genuine economic content: assets trend because fundamentals (earnings, monetary policy, supply/demand) evolve gradually. The "past returns" are a noisy proxy for the slowly changing fundamental.
2. **"Faster signals are always better"**: Shorter lookback periods generate higher turnover and higher transaction costs. After costs, a 1 month momentum signal often underperforms a blended 3/6/12 month signal for most assets.
3. **"Momentum works all the time"**: Momentum has extended losing periods (6 to 18 months) during range-bound markets or sharp reversals. The 2009 equity rally and 2023 cross-asset chop both caused significant momentum drawdowns. Patience and diversification across assets and lookback horizons are essential.
4. **"TSMOM and cross-sectional momentum are the same"**: TSMOM takes absolute positions (long or short each asset based on its own return). Cross-sectional momentum takes relative positions (long top performers, short bottom performers). They have different risk profiles and factor exposures.

## Sources
- Moskowitz, Tobias, Ooi, Yao Hua, Pedersen, Lasse, "Time Series Momentum," Journal of Financial Economics (2012)
- Asness, Clifford, Moskowitz, Tobias, Pedersen, Lasse, "Value and Momentum Everywhere," Journal of Finance (2013)
- Hurst, Brian, Ooi, Yao Hua, Pedersen, Lasse, "A Century of Evidence on Trend-Following Investing," AQR Capital Management (2017)
- Baltas, Nick, Kosowski, Robert, "Momentum Strategies in Futures Markets and Trend-Following Funds," Working Paper (2013)
