---
aliases: [terms of trade, ToT, trade terms]
tags:
  - "#fx"
  - "#macro"
date-added: "2026-03-20"
---

# Terms of Trade

## Definition
The terms of trade (ToT) is the ratio of a country's export prices to its import prices, typically expressed as an index. When a country's export prices rise relative to its import prices, its terms of trade improve, meaning it can buy more imports for each unit of exports. For commodity exporting nations, the terms of trade are heavily driven by global commodity prices: a surge in oil prices improves Norway's ToT (oil is a major export) while worsening Japan's ToT (oil is a major import). Terms of trade shocks are among the most powerful fundamental drivers of exchange rates for commodity linked economies, transmitting through the trade balance, national income, and capital flows. The relationship between ToT and currencies is both intuitive and well documented empirically.

## Why it matters (commodities and FX)
For commodity traders who also manage FX exposure, terms of trade is the critical link between commodity prices and currency values. When iron ore prices double, Australia's ToT improves, AUD strengthens, and AUD denominated costs for Australian miners rise, partially offsetting the commodity windfall. Understanding this feedback loop is essential for hedging commodity revenue streams. For systematic FX strategies, ToT changes are among the strongest predictors of currency returns for commodity linked pairs. A model that buys currencies of countries with improving ToT and sells currencies of countries with deteriorating ToT generates Sharpe ratios of 0.4 to 0.6 in backtests, comparable to carry and momentum signals.

## Concrete example
In 2022, natural gas prices in Europe surged from 30 to over 300 EUR/MWh following the Russia Ukraine conflict. Norway, a major gas exporter, saw its ToT improve dramatically. NOK/SEK (Norway vs Sweden, a gas importer) rallied from 0.96 to 1.02, a 6% move driven almost entirely by the ToT shock. A trader who bought NOK/SEK when European gas prices broke above 100 EUR/MWh captured most of this move. Conversely, Japan's ToT deteriorated sharply as energy import costs surged: the Japanese ToT index fell from 100 to 75 in 2022, contributing to JPY weakness and USD/JPY rising from 115 to 152. A trader short JPY based on ToT deterioration profited handsomely, but the trade required conviction to hold through BOJ intervention noise.

## Key mechanics and formulas
- **Terms of trade index**: ToT = (Export price index / Import price index) × 100.
- **ToT change**: ΔToT = (ToT_current − ToT_previous) / ToT_previous × 100.
- **Commodity ToT proxy**: For commodity exporters, ToT ≈ Commodity export price index / Manufactured goods import price index.
- **FX sensitivity**: A 10% improvement in ToT is associated with approximately 3 to 5% real currency appreciation for commodity exporters (varies by country and period).
- **Current account channel**: Improved ToT → higher export revenues → larger trade surplus → greater demand for domestic currency → appreciation.
- **Income channel**: Improved ToT → higher national income → higher consumption and investment → capital inflows → further appreciation.
- **Key commodity/currency links**: Iron ore → AUD; Crude oil → NOK, CAD, BRL; Dairy → NZD; Copper → CLP; Gold → ZAR.

## Prerequisites
- [[Currency Pair]]
- [[Spot Rate]]
- [[Petrocurrency]]
- [[G10 Currencies]]

## Related concepts (learn next)
- [[Petrocurrency]]: currencies where ToT is dominated by oil price movements, making the ToT/FX link most direct and tradeable.
- [[Real Effective Exchange Rate]]: sustained ToT improvement drives REER appreciation; ToT deterioration drives REER depreciation.
- [[Purchasing Power Parity]]: ToT shocks cause persistent PPP deviations because they shift relative price levels between trading partners.
- [[Cross Pairs]]: ToT analysis is most powerful for commodity relative value crosses like AUD/NZD (iron ore vs dairy) and NOK/SEK (oil vs manufacturing).
- [[EM Currencies]]: EM commodity exporters (BRL, ZAR, CLP) have the highest ToT beta and therefore the most ToT driven FX volatility.
- [[Central Bank Intervention]]: some EM CBs intervene to smooth ToT driven currency swings, particularly during commodity booms and busts.
- [[Monetary Policy Divergence]]: ToT shocks can trigger divergent monetary policy responses (e.g., Norway hiking while Sweden holds after an oil price surge).

## Common misconceptions
1. **ToT only matters for commodity currencies**: All countries have ToT, and shocks affect all currencies. Germany's ToT deteriorated in 2022 due to energy import costs, contributing to EUR weakness. The US ToT improved as it became a net energy exporter, supporting USD.
2. **Higher commodity prices always help the exporter's currency**: If the price surge is driven by supply disruption in the exporting country itself (e.g., a Brazilian drought destroying soy exports), the volume decline can offset the price gain, and the ToT improvement may not fully materialize.
3. **ToT is a static snapshot**: ToT is dynamic and forward looking. Futures curves for commodities provide a market estimate of future ToT, and the FX market often prices in expected ToT changes before they show up in official trade data.
4. **ToT and trade balance are the same**: ToT measures the price ratio; the trade balance measures the value of exports minus imports. A country can have improving ToT but a deteriorating trade balance if export volumes fall faster than prices rise.

## Sources
- Chen, Yu Chin and Rogoff, Kenneth, "Commodity Currencies," Journal of International Economics, 2003.
- Cashin, Paul et al., "Commodity Currencies and the Real Exchange Rate," Journal of Development Economics, 2004.
- Reserve Bank of Australia, "The Terms of Trade and the Australian Economy," RBA Bulletin, 2011.
