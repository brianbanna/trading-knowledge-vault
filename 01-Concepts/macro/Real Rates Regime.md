---
aliases: [real rates regime, negative real rates, real rate environment]
tags:
  - "#macro"
  - "#rates"
date-added: "2026-03-20"
---

# Real Rates Regime

## Definition
The real rates regime refers to the prevailing level and direction of real (inflation-adjusted) interest rates, which serve as a structural driver of asset allocation and cross-asset pricing. The real rate is calculated as the nominal interest rate minus expected inflation (using TIPS breakevens, inflation swaps, or survey-based measures). When real rates are deeply negative (nominal rates below inflation), the opportunity cost of holding non-yielding assets like gold and commodities is low, and financial repression incentivizes capital to seek inflation hedges. When real rates are significantly positive, cash and bonds offer attractive real returns, drawing capital away from commodities, gold, and speculative risk assets. The real rate regime is distinct from (though related to) the broader [[Macro Regime]] because it specifically captures the policy stance of central banks relative to inflation. Real rates are arguably the single most important variable connecting monetary policy, FX, and commodity markets.

## Why it matters (commodities and FX)
Real rates are the dominant driver of gold prices over medium-term horizons (6 to 24 months), with a correlation of approximately -0.7 to -0.9 between US 10 year TIPS yields and gold. The mechanism is direct: when real rates are -2%, holding gold (which has zero yield) costs nothing in real terms, while cash loses purchasing power. When real rates are +2%, gold's zero yield is a significant disadvantage. From 2020 to 2022, deeply negative US real rates (as low as -1.5% on 10 year TIPS) drove gold to all-time highs above $2,000 and fueled a broad commodity bull market. The real rate regime also drives FX: currencies of countries with higher real rates attract capital inflows (the real-rate-adjusted carry trade), and the USD strengthens when US real rates rise relative to global peers. For [[Risk Parity]] portfolios, the real rate regime determines the return on the bond allocation (the largest notional position) and thus has an outsized impact on total portfolio performance.

## Concrete example
In August 2020, the US 10 year TIPS yield falls to -1.08%, its lowest level in history. Federal funds rate is near 0%, CPI inflation is 1.3% but rising, and the Fed has signaled extended accommodation. Gold prices surge from $1,500 to $2,075 (a 38% rally in 5 months), silver doubles, and copper rallies 60%. AUDUSD rises from 0.66 to 0.78 as the weak-USD/strong-commodity-currency regime takes hold. A macro trader who monitors real rates goes long gold, long AUDUSD, and long copper, capturing the bulk of the move. By October 2022, the regime has completely reversed: the Fed has hiked rates to 4%, TIPS yields have risen to +1.7% (a 280 basis point swing in real rates), gold has fallen to $1,620, and AUDUSD has dropped to 0.63. The same trader who shifted from long commodities to short commodities when real rates crossed from negative to positive territory captured both legs. A trader who ignored real rates and stayed long gold through the 2022 hiking cycle suffered a 22% drawdown before the eventual recovery.

## Key mechanics and formulas
- **Real rate**: Real rate = nominal yield - expected inflation; for market-based measure: Real rate = TIPS yield (read directly from inflation-protected bonds)
- **Breakeven inflation**: Breakeven = nominal yield - TIPS yield; measures the market's inflation expectation
- **Gold-real rate regression**: Gold price change = alpha + beta x (change in 10yr TIPS yield) + error; beta is approximately -$150 to -$200 per 100 bps change in real rates
- **Real rate differential (FX)**: RRD = (real rate country A) - (real rate country B); positive RRD attracts capital to country A's currency
- **Commodity real rate sensitivity**: varies by commodity; gold has the highest sensitivity (beta approximately -0.8), followed by silver (-0.6), then industrial metals (-0.3)
- **Financial repression threshold**: when real rates are below -1%, the incentive to hold real assets (commodities, real estate, equities) becomes very strong; this threshold has historically coincided with commodity bull markets

## Prerequisites
- [[Interest Rates]]
- [[Inflation]]
- [[TIPS]]
- [[Breakeven Inflation]]

## Related concepts (learn next)
- [[DXY Correlation]]: rising real rates strengthen the USD, which in turn weakens commodities through the dollar channel, creating a compounding effect.
- [[Macro Regime]]: the real rate environment is a sub-component of the broader macro regime; Goldilocks features moderate positive real rates, Stagflation features negative real rates with high inflation.
- [[Carry Cross Asset]]: real-rate-adjusted carry (rather than nominal carry) is a more robust signal for FX and bond trades.
- [[Risk Parity]]: the bond allocation in risk parity is a direct bet on the real rate regime; rising real rates erode bond returns.
- [[Value Cross Asset]]: real rates inform the fair value of currencies and commodities; negative real rates justify higher commodity valuations.
- [[Momentum Cross Asset]]: real rate trends are slow-moving and produce persistent trends in gold, bonds, and FX that momentum strategies capture.
- [[Terms of Trade Shock]]: commodity price shocks driven by real rate shifts feed through to terms of trade for commodity exporters.

## Common misconceptions
1. **"Nominal rates drive gold, not real rates"**: Gold is insensitive to nominal rate moves that are accompanied by proportional inflation changes. A rate hike from 2% to 4% with inflation rising from 2% to 4% leaves real rates unchanged and has minimal impact on gold. It is the change in real rates that matters.
2. **"Negative real rates are abnormal"**: Negative real rates occurred for extended periods in the 1940s, 1970s, and 2010 to 2022. They are a policy choice (financial repression) used by central banks to erode the real value of government debt. Treating negative real rates as temporary can lead to premature positioning.
3. **"TIPS yields perfectly measure real rates"**: TIPS yields incorporate a liquidity premium (TIPS are less liquid than nominal Treasuries) and a risk premium, meaning TIPS yields can diverge from the "true" real rate. During the March 2020 liquidity crisis, TIPS yields spiked higher even as real economic rates were falling.

## Sources
- Piazzesi, Monika, Schneider, Martin, "Equilibrium Yield Curves," NBER Macroeconomics Annual (2007)
- Erb, Claude, Harvey, Campbell, "The Golden Dilemma," Financial Analysts Journal (2013)
- Ilmanen, Antti, "Expected Returns," Wiley (2011)
- Federal Reserve Bank of Cleveland, "Inflation Expectations" data series
