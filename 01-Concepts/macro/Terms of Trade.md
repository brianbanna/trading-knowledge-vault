---
aliases: [terms of trade, ToT, trade terms]
tags:
  - "#fx"
  - "#macro"
date-added: "2026-03-20"
---

# Terms of Trade

## Definition
Terms of trade (ToT) is the ratio of a country's export prices to its import prices, expressed as an index. When export prices rise relative to import prices, ToT improves and the country can buy more imports per unit of exports. For commodity exporters, ToT is heavily driven by global commodity prices: a surge in oil improves Norway's ToT (oil is a major export) while worsening Japan's (oil is a major import). ToT shocks are among the most powerful fundamental drivers of exchange rates for commodity linked economies, transmitting through the trade balance, national income, and capital flows. The relationship between ToT and currencies is intuitive and well documented empirically.

## Why it matters (commodities and FX)
For commodity traders managing FX exposure, ToT is the critical link between commodity prices and currency values. When iron ore doubles, Australia's ToT improves, AUD strengthens, and AUD denominated costs for Australian miners rise, partially offsetting the windfall. Understanding this feedback is essential for hedging commodity revenue. For systematic FX strategies, ToT changes are among the strongest predictors of currency returns for commodity linked pairs. A model that buys currencies of improving ToT and sells deteriorating ToT generates Sharpe ratios of 0.4 to 0.6 in backtests, comparable to carry and momentum.

## Concrete example

**Concrete:** In 2022, natural gas prices in Europe surged 30 to over 300 EUR/MWh after Russia Ukraine. Norway, a major gas exporter, saw ToT improve dramatically. NOK/SEK (Norway vs Sweden, a gas importer) rallied 0.96 to 1.02, a 6% move driven almost entirely by the ToT shock. A trader who bought NOK/SEK when European gas broke 100 EUR/MWh captured most of the move. Japan's ToT deteriorated sharply: the Japanese ToT index fell 100 to 75 in 2022, contributing to JPY weakness and USD/JPY rising 115 to 152. A trader short JPY on ToT deterioration profited, but the trade required conviction to hold through BOJ intervention noise.

**Simplified:** A country's economic health depends on what it sells vs what it buys. When the things it sells become more expensive (relative to what it buys), it gets richer in real terms, and its currency strengthens. When the things it buys get more expensive, the opposite. Commodity producers see their ToT swing wildly with commodity prices. That swing is one of the most reliable drivers of their currency. Importers see the mirror image.

## Key mechanics and formulas
- **Terms of trade index**: ToT = (Export price index / Import price index) × 100.
- **ToT change**: ΔToT = (ToT_current − ToT_previous) / ToT_previous × 100.
- **Commodity ToT proxy**: For commodity exporters, ToT ≈ Commodity export price index / Manufactured goods import price index.
- **FX sensitivity**: A 10% ToT improvement is associated with ~3 to 5% real currency appreciation for commodity exporters (varies).
- **Current account channel**: Improved ToT → higher export revenues → larger trade surplus → greater demand for domestic currency → appreciation.
- **Income channel**: Improved ToT → higher national income → higher consumption and investment → capital inflows → further appreciation.
- **Key commodity/currency links**: Iron ore → AUD; Crude oil → NOK, CAD, BRL; Dairy → NZD; Copper → CLP; Gold → ZAR.

## Prerequisites
- [[Currency Pair]]
- [[Spot Rate]]
- [[Petrocurrency]]
- [[G10 Currencies]]

## Related concepts (learn next)
- [[Petrocurrency]]: currencies where ToT is dominated by oil, making the ToT/FX link most direct and tradeable.
- [[Real Effective Exchange Rate]]: sustained ToT improvement drives REER appreciation; deterioration drives depreciation.
- [[Purchasing Power Parity]]: ToT shocks cause persistent PPP deviations because they shift relative price levels between trading partners.
- [[Cross Pairs]]: ToT analysis is most powerful for commodity relative value crosses like AUD/NZD (iron ore vs dairy) and NOK/SEK (oil vs manufacturing).
- [[EM Currencies]]: EM commodity exporters (BRL, ZAR, CLP) have the highest ToT beta and most ToT driven FX volatility.
- [[Central Bank Intervention]]: some EM CBs intervene to smooth ToT driven swings, particularly during commodity booms and busts.
- [[Monetary Policy Divergence]]: ToT shocks can trigger divergent policy responses (Norway hiking while Sweden holds after an oil price surge).

## Common misconceptions
1. **ToT only matters for commodity currencies**: All countries have ToT, and shocks affect all currencies. Germany's ToT deteriorated in 2022 due to energy import costs, contributing to EUR weakness. The US ToT improved as it became a net energy exporter, supporting USD.
2. **Higher commodity prices always help the exporter's currency**: If the price surge is driven by supply disruption in the exporting country itself (a Brazilian drought destroying soy exports), the volume decline offsets the price gain, and the ToT improvement may not fully materialize.
3. **ToT is a static snapshot**: ToT is dynamic and forward looking. Futures curves provide a market estimate of future ToT, and FX often prices in expected ToT changes before they show up in official trade data.
4. **ToT and trade balance are the same**: ToT measures the price ratio; trade balance measures value of exports minus imports. A country can have improving ToT but a deteriorating trade balance if export volumes fall faster than prices rise.

## Sources
- Chen, Yu Chin and Rogoff, Kenneth, "Commodity Currencies," Journal of International Economics, 2003.
- Cashin, Paul et al., "Commodity Currencies and the Real Exchange Rate," Journal of Development Economics, 2004.
- Reserve Bank of Australia, "The Terms of Trade and the Australian Economy," RBA Bulletin, 2011.
