---
aliases: [DXY correlation, dollar correlation, USD commodity correlation]
tags:
  - "#fx/g10"
  - "#macro"
date-added: "2026-03-20"
---

# DXY Correlation

## Definition
The DXY (US Dollar Index) correlation refers to the persistent inverse relationship between the trade-weighted US dollar and the price of commodities, particularly those priced and settled in USD. The DXY is a basket of 6 major currencies (EUR 57.6%, JPY 13.6%, GBP 11.9%, CAD 9.1%, SEK 4.2%, CHF 3.6%) that serves as the standard benchmark for dollar strength. When the dollar strengthens (DXY rises), commodities tend to decline, and vice versa. This relationship exists for 3 reasons: (1) commodities are globally priced in USD, so a stronger dollar makes them more expensive for non-US buyers, reducing demand; (2) a strong USD often reflects tighter US monetary policy, which slows global growth and commodity demand; and (3) the same risk-on/risk-off dynamics that weaken the dollar (capital flowing out of US safe havens) simultaneously push money into commodities and EM assets. The correlation is not constant; it varies by commodity, time period, and [[macro regime]], but it is one of the most important structural relationships in cross-asset trading.

## Why it matters (commodities and FX)
The USD-commodity inverse relationship is the single most important cross-asset correlation for anyone trading both markets. A crude oil trader who ignores dollar dynamics is missing a variable that explains 15 to 30% of oil's variance at monthly frequencies. An FX trader who ignores commodity prices is missing the fundamental driver of commodity-exporting currencies like AUD, CAD, NOK, BRL, and CLP. The relationship creates a powerful cross-hedging framework: a gold miner in Australia benefits when gold rises (revenue up) and when AUD weakens (costs down), and these 2 things tend to happen simultaneously because both are driven by a weakening USD. For systematic strategies, the DXY-commodity correlation can be exploited directly (short DXY as a commodity trend proxy) or used as a regime filter (avoid long commodity positions when DXY is in a strong uptrend). [[Risk Parity]] portfolios that hold both commodities and US assets implicitly benefit from this correlation as a diversification source.

## Concrete example
From June 2021 to September 2022, the DXY rallied from 90 to 114 (a 27% move), driven by aggressive Fed rate hikes. During this period, gold fell from $1,900 to $1,620 (a 15% decline), copper fell from $4.60 to $3.30 (a 28% decline), and EURUSD fell from 1.22 to 0.96 (a 21% decline). Commodity-exporting currencies were crushed: AUDUSD fell from 0.77 to 0.64, USDCAD rose from 1.23 to 1.38. A systematic trader who shorted copper and gold when DXY broke above its 200 day moving average captured the bulk of the commodity decline. However, crude oil defied the DXY correlation for much of this period, rallying from $70 to $120 due to the Russia-Ukraine supply shock. This illustrates the key caveat: DXY correlation holds on average but can be overwhelmed by asset-specific supply shocks. A trader who mechanically shorted crude oil based solely on USD strength would have lost heavily in H1 2022 before eventually being proven right in H2 2022 when oil corrected to $75.

## Key mechanics and formulas
- **DXY-commodity correlation**: historically approximately -0.3 to -0.6 for gold, -0.2 to -0.5 for crude oil, -0.2 to -0.4 for copper, measured at monthly frequency
- **Dollar beta of a commodity**: Beta = Cov(commodity return, DXY return) / Var(DXY return); gold's beta to DXY is approximately -0.8, meaning a 1% DXY move corresponds to a 0.8% gold move in the opposite direction
- **FX-commodity pass-through**: for commodity currencies, Currency change = alpha + beta1 x commodity price change + beta2 x DXY change + error; for AUDUSD, beta1 (copper) is approximately 0.15, beta2 (DXY) is approximately -0.85
- **Real effective exchange rate (REER)**: a broader dollar measure that adjusts for inflation differentials; more fundamentally meaningful than nominal DXY
- **Regime conditioning**: DXY-commodity correlation is strongest during "dollar-driven" regimes (Fed tightening/easing cycles) and weakest during "supply-driven" commodity regimes (OPEC cuts, mine disruptions)

## Prerequisites
- [[US Dollar]]
- [[Commodity Pricing]]
- [[Correlation]]
- [[Macro Regime]]

## Related concepts (learn next)
- [[Terms of Trade Shock]]: a sudden commodity price shift that affects USD through the terms of trade channel for commodity exporters/importers.
- [[Carry Cross Asset]]: USD strength often coincides with carry trade unwinds in EM currencies, amplifying commodity currency weakness.
- [[Real Rates Regime]]: rising real rates strengthen the USD and weaken commodities (especially gold) through the opportunity cost channel.
- [[Macro Regime]]: the DXY-commodity correlation varies by macro regime; strongest in Deflation/Recession, weakest during supply-driven Reflation.
- [[Momentum Cross Asset]]: trending DXY provides a useful filter for commodity trend signals.
- [[Risk Parity]]: the negative USD-commodity correlation is a diversification source that risk parity frameworks exploit.
- [[Correlation Breakdown]]: in extreme risk-off events, the DXY-commodity inverse relationship can invert (both fall) as EM central banks sell USD reserves.

## Common misconceptions
1. **"DXY strength always means commodity weakness"**: Supply-driven commodity rallies (e.g., OPEC cuts, mine strikes) can overpower the dollar effect. In 2005 and 2022, oil rallied sharply despite a relatively strong dollar because supply constraints dominated.
2. **"The DXY is a complete measure of dollar strength"**: The DXY is heavily weighted toward EUR (57.6%) and ignores CNY, the world's 2nd largest economy. For commodity analysis, a broader trade-weighted index or the Fed's real broad dollar index is more appropriate.
3. **"The correlation is stable enough for hedging"**: The DXY-commodity correlation varies from -0.7 to near 0 depending on the macro regime. Using a static correlation assumption for hedging can lead to either over-hedging or under-hedging, depending on the regime.

## Sources
- Akram, Q. Farooq, "Commodity Prices, Interest Rates, and the Dollar," Energy Economics (2009)
- Zhang, Yue-Jun et al., "The Crude Oil Market and the Gold Market: Evidence for Cointegration, Causality, and Price Discovery," Resources Policy (2010)
- Federal Reserve Bank, "Trade-Weighted Dollar Indices" (methodology papers)
- Frankel, Jeffrey, "The Effect of Monetary Policy on Real Commodity Prices," NBER Working Paper (2006)
