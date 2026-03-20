---
aliases: [terms of trade shock, ToT shock, commodity FX shock]
tags:
  - "#fx"
  - "#macro"
date-added: "2026-03-20"
---

# Terms of Trade Shock

## Definition
A terms of trade (ToT) shock is a sudden, significant change in the ratio of a country's export prices to its import prices, driven by a sharp move in commodity prices, trade policy, or global supply chain disruption. For commodity-exporting countries (Australia, Canada, Norway, Brazil, Chile), a surge in their primary export commodity (iron ore, oil, copper) improves the terms of trade, boosting national income and strengthening the currency. For commodity-importing countries (Japan, India, Turkey, most of Europe), the same commodity price spike worsens the terms of trade, draining national income and weakening the currency. ToT shocks create some of the most powerful and persistent FX trends because they directly alter a country's current account balance, corporate profitability, and fiscal position. The FX market's reaction to ToT shocks is often delayed and incomplete, creating multi-month trading opportunities for systematic and macro strategies.

## Why it matters (commodities and FX)
Terms of trade shocks are the primary fundamental driver of commodity-linked FX pairs. When crude oil spikes from $70 to $120, Norway's terms of trade improve dramatically (oil is 40 to 50% of Norwegian exports), strengthening NOK. Simultaneously, Japan's terms of trade deteriorate (Japan imports virtually all its energy), weakening JPY. The cross rate NOKJPY thus has a powerful positive beta to oil prices. For systematic traders, commodity-FX relationships driven by ToT effects are among the most reliable cross-asset signals: AUDUSD tracks iron ore and copper, USDCAD inversely tracks WTI crude oil, and NZDUSD tracks dairy prices. These relationships persist because they are grounded in real economic flows (trade balances, corporate hedging, sovereign wealth fund repatriation) rather than sentiment. Understanding ToT dynamics is essential for designing cross-asset carry, momentum, and value strategies that bridge FX and commodity markets.

## Concrete example
In February 2022, Russia's invasion of Ukraine triggers a massive oil supply shock. Brent crude rallies from $90 to $130 within 2 weeks. The ToT impact across currencies is immediate and dramatic. Positive ToT shock: USDNOK falls from 9.10 to 8.60 (NOK strengthens 5.5% as oil exports surge), USDCAD falls from 1.28 to 1.24 (CAD strengthens 3% on oil), and USDBRL falls from 5.20 to 4.80 (BRL strengthens 7.7% on agricultural and energy exports). Negative ToT shock: USDJPY rises from 115 to 122 (JPY weakens 6% as Japan's energy import bill explodes), USDINR rises from 75 to 77.5 (INR weakens 3.3% as India's oil import costs surge), and EURUSD falls from 1.13 to 1.08 (EUR weakens as Europe's gas import costs skyrocket). A macro trader who immediately went long NOK, CAD, BRL and short JPY, INR, EUR upon the oil spike captured 5 to 8% returns in 3 weeks. However, by June 2022, oil began declining from $120, and traders who did not reduce their ToT-driven positions suffered reversals as CAD and NOK weakened. The lesson: ToT shocks create powerful but finite impulses; the trade must be monitored as the commodity price itself evolves.

## Key mechanics and formulas
- **Terms of trade**: ToT = export price index / import price index; an increase = improvement = positive for the currency
- **ToT change**: Delta ToT = (change in export prices x export share) - (change in import prices x import share)
- **Commodity beta of a currency**: Beta = Cov(currency return, commodity return) / Var(commodity return); AUDUSD beta to iron ore is approximately 0.15, USDCAD beta to WTI is approximately -0.25, NOKJPY beta to Brent is approximately 0.20 to 0.30
- **Current account impact**: CA change = Delta ToT x trade openness (trade as % of GDP); larger trade openness amplifies the FX effect
- **FX fair value shift**: Delta(FX fair value) = k x Delta(ToT), where k depends on the economy's trade structure and elasticities
- **Key commodity-FX pairs**:
  - AUD: iron ore, coal, copper
  - CAD: crude oil, natural gas
  - NOK: crude oil, natural gas
  - NZD: dairy, meat, forestry
  - BRL: soybeans, iron ore, crude oil
  - CLP: copper
  - ZAR: gold, platinum, coal

## Prerequisites
- [[Current Account]]
- [[Commodity Pricing]]
- [[DXY Correlation]]
- [[Macro Regime]]

## Related concepts (learn next)
- [[DXY Correlation]]: ToT shocks in USD terms are amplified or dampened by the broader dollar trend.
- [[Carry Cross Asset]]: commodity-exporting countries often have higher interest rates (carry) when commodity prices are high, creating reinforcing signals.
- [[Momentum Cross Asset]]: ToT-driven FX trends are persistent and well-captured by momentum systems.
- [[Macro Regime]]: major ToT shocks can trigger macro regime transitions (e.g., an oil shock causing Stagflation in importers).
- [[Real Rates Regime]]: central banks in commodity importers may need to hike real rates to defend their currency after a negative ToT shock.
- [[Correlation Breakdown]]: during a massive ToT shock, the usual commodity-FX correlations intensify rather than break down, creating unusually strong cross-asset signals.
- [[Value Cross Asset]]: PPP-based value for commodity currencies must account for ToT shifts; a ToT improvement can justify a permanently higher exchange rate.
- [[Positioning Signal]]: extreme speculative positioning in commodity currencies after a ToT shock signals potential mean reversion.

## Common misconceptions
1. **"Commodity currencies only move because of commodity prices"**: While ToT is the dominant driver, commodity currencies also respond to domestic factors (central bank policy, political risk, housing markets). The AUD is sensitive to Chinese growth expectations and Australian mortgage rates independently of iron ore prices.
2. **"ToT shocks are always temporary"**: Some ToT shifts are structural (e.g., the shale oil revolution permanently improved US energy terms of trade; the energy transition may permanently improve lithium and copper exporters' ToT). Assuming mean reversion in all cases is dangerous.
3. **"The FX response to a ToT shock is immediate"**: Empirical research shows that currencies take 3 to 12 months to fully adjust to a ToT shock, creating a delayed reaction that systematic strategies can capture. The initial move captures 30 to 50% of the eventual adjustment.
4. **"All commodity exporters react the same way"**: A country's specific export basket matters enormously. An oil shock helps Canada and Norway but does nothing for Chile (copper exporter). A copper shock helps Chile and Australia but not Norway.

## Sources
- Chen, Yu-Chin, Rogoff, Kenneth, "Commodity Currencies," Journal of International Economics (2003)
- Cashin, Paul, Cespedes, Luis, Sahay, Ratna, "Commodity Currencies and the Real Exchange Rate," Journal of Development Economics (2004)
- Kohlscheen, Emanuel, "Long-Run Determinants of the Brazilian Real," Working Paper, BIS (2014)
- Ferraro, Domenico, Rogoff, Kenneth, Rossi, Barbara, "Can Oil Prices Forecast Exchange Rates?," Journal of International Money and Finance (2015)
