---
aliases: [DXY correlation, dollar correlation, USD commodity correlation]
tags:
  - "#fx/g10"
  - "#macro"
date-added: "2026-03-20"
---

# DXY Correlation

## Definition
The DXY correlation is the persistent inverse relationship between the trade weighted US dollar and the price of commodities, especially those priced and settled in USD. The DXY is a basket of 6 major currencies (EUR 57.6%, JPY 13.6%, GBP 11.9%, CAD 9.1%, SEK 4.2%, CHF 3.6%) and serves as the benchmark for dollar strength. When DXY rises, commodities fall, and vice versa. Three drivers: (1) commodities are priced in USD, so a stronger dollar makes them more expensive for non US buyers, cutting demand; (2) a strong USD reflects tighter US monetary policy, which slows global growth and commodity demand; (3) the same risk on/off dynamics that weaken the dollar push money into commodities and EM. The correlation varies by commodity, period, and [[Macro Regime]], but it is one of the most important structural relationships in cross asset trading.

## Why it matters (commodities and FX)
The USD commodity inverse relationship is the most important cross asset correlation for trading both markets. A crude trader who ignores dollar dynamics is missing a variable that explains 15 to 30% of oil's variance at monthly frequency. An FX trader who ignores commodity prices misses the fundamental driver of commodity exporter currencies (AUD, CAD, NOK, BRL, CLP). The relationship creates a cross hedging framework: an Australian gold miner benefits when gold rises (revenue up) and AUD weakens (costs down), and these tend to happen together because both are driven by a weakening USD. For systematic strategies, the DXY commodity correlation can be exploited directly (short DXY as commodity trend proxy) or used as a regime filter (avoid long commodities when DXY is in a strong uptrend). [[Risk Parity]] portfolios benefit from this correlation as a diversification source.

## Concrete example

**Concrete:** From June 2021 to September 2022, DXY rallied from 90 to 114 (27%), driven by Fed hikes. Gold fell from $1,900 to $1,620 (15%), copper fell from $4.60 to $3.30 (28%), and EURUSD fell from 1.22 to 0.96 (21%). Commodity exporters were crushed: AUDUSD from 0.77 to 0.64, USDCAD from 1.23 to 1.38. A systematic trader who shorted copper and gold when DXY broke above its 200 day moving average captured the bulk of the decline. Crude defied the correlation for much of the period, rallying from $70 to $120 on the Russia Ukraine supply shock. Key caveat: DXY correlation holds on average but can be overwhelmed by asset specific supply shocks. Mechanical shorting of crude on USD strength would have lost heavily in H1 2022 before being proven right in H2 when oil corrected to $75.

**Simplified:** Most commodities are quoted in dollars. When the dollar gets more expensive in other currencies, foreign buyers can afford less commodity, so demand drops and prices fall. The Fed sets the dollar's price, so the Fed indirectly sets commodity prices. The relationship is statistical, not a law: a real supply disruption can override the dollar effect for months at a time. Use it as one input among several, not as the only signal.

## Key mechanics and formulas
- **DXY commodity correlation**: historically ~-0.3 to -0.6 for gold, -0.2 to -0.5 for crude, -0.2 to -0.4 for copper, at monthly frequency
- **Dollar beta of a commodity**: Beta = Cov(commodity return, DXY return) / Var(DXY return); gold's beta to DXY ≈ -0.8, meaning a 1% DXY move = 0.8% gold move opposite
- **FX commodity pass through**: for commodity currencies, Currency change = alpha + beta1 x commodity price change + beta2 x DXY change + error; for AUDUSD, beta1 (copper) ≈ 0.15, beta2 (DXY) ≈ -0.85
- **Real effective exchange rate (REER)**: broader dollar measure adjusting for inflation differentials; more fundamentally meaningful than nominal DXY
- **Regime conditioning**: DXY commodity correlation is strongest in "dollar driven" regimes (Fed tightening/easing cycles), weakest in "supply driven" commodity regimes (OPEC cuts, mine disruptions)

## Prerequisites
- [[US Dollar]]
- [[Commodity Pricing]]
- [[Correlation]]
- [[Macro Regime]]

## Related concepts (learn next)
- [[Terms of Trade Shock]]: a sudden commodity price shift affecting USD through terms of trade for exporters/importers.
- [[Carry Cross Asset]]: USD strength often coincides with carry unwinds in EM, amplifying commodity currency weakness.
- [[Real Rates Regime]]: rising real rates strengthen USD and weaken commodities (especially gold) through the opportunity cost channel.
- [[Macro Regime]]: DXY commodity correlation varies by regime; strongest in Deflation/Recession, weakest in supply driven Reflation.
- [[Momentum Cross Asset]]: trending DXY provides a useful filter for commodity trend signals.
- [[Risk Parity]]: the negative USD commodity correlation is a diversification source.
- [[Correlation Breakdown]]: in extreme risk off, the inverse can invert (both fall) as EM central banks sell USD reserves.

## Common misconceptions
1. **"DXY strength always means commodity weakness"**: Supply driven rallies (OPEC cuts, mine strikes) can overpower the dollar effect. In 2005 and 2022, oil rallied despite a strong dollar.
2. **"DXY is a complete measure of dollar strength"**: DXY is 57.6% EUR and ignores CNY, the world's 2nd largest economy. For commodity analysis, the Fed's real broad dollar index is more appropriate.
3. **"The correlation is stable enough for hedging"**: Correlation ranges from -0.7 to near 0 depending on regime. Static correlation assumptions lead to over or under hedging.

## Sources
- Akram, Q. Farooq, "Commodity Prices, Interest Rates, and the Dollar," Energy Economics (2009)
- Zhang, Yue-Jun et al., "The Crude Oil Market and the Gold Market: Evidence for Cointegration, Causality, and Price Discovery," Resources Policy (2010)
- Federal Reserve Bank, "Trade-Weighted Dollar Indices" (methodology papers)
- Frankel, Jeffrey, "The Effect of Monetary Policy on Real Commodity Prices," NBER Working Paper (2006)
