---
aliases: [macro regime, economic regime, growth-inflation regime]
tags:
  - "#macro"
date-added: "2026-03-20"
---

# Macro Regime

## Definition
A macro regime is a persistent economic environment defined by the combination of growth and inflation conditions. The 4 canonical regimes are: (1) Goldilocks (above-trend growth, below-trend inflation), (2) Reflation (above-trend growth, above-trend inflation), (3) Stagflation (below-trend growth, above-trend inflation), and (4) Deflation/Recession (below-trend growth, below-trend inflation). Each regime produces distinct patterns in asset class returns, correlations, and volatilities. Equities and credit thrive in Goldilocks; commodities and inflation-linked bonds outperform in Reflation; cash and trend-following strategies protect in Stagflation; and government bonds rally in Deflation. Regime identification is the highest-level strategic decision a macro trader makes because it determines which asset classes, factors, and strategies are likely to work. Regimes persist for months to years, driven by central bank policy, fiscal policy, and structural economic forces.

## Why it matters (commodities and FX)
Regime awareness is the single most important context for commodity and FX trading. Commodities are the highest-beta asset to the growth/inflation regime: they strongly outperform during Reflation (rising demand, pricing power, tight supply) and strongly underperform during Deflation (collapsing demand, excess supply). FX regimes are driven by relative growth and rate differentials: in a global Goldilocks regime, carry trades work well because risk appetite is high and volatility is low; in Stagflation, commodity-exporting currencies (AUD, CAD, NOK) diverge from commodity-importing currencies (JPY, EUR), creating powerful FX trends. [[Risk Parity]] portfolios are explicitly designed to weather all 4 regimes, but in practice, rapid regime transitions cause [[correlation breakdown]] and drawdowns. [[CTA]] strategies benefit from persistent regimes (which create trends) and struggle during regime transitions (which create whipsaws).

## Concrete example
From 2020 to 2024, the world cycled through 3 regimes. In 2020 Q1 to Q2, a Deflationary shock: COVID lockdowns crashed growth and inflation simultaneously. Oil fell to negative prices, equities dropped 35%, and bonds rallied. In 2021 to mid 2022, a Reflationary boom: massive fiscal stimulus, supply chain disruptions, and reopening demand drove GDP growth above 5% and inflation above 8%. Crude oil rallied from 40 to 120, copper hit all-time highs, and commodity currencies (AUD, CAD, BRL) surged. In 2022 H2 to 2023, a Stagflationary scare: central banks hiked aggressively, growth slowed, but inflation remained sticky. Bonds and equities fell simultaneously (a rare outcome), and [[risk parity]] funds suffered. A macro trader who correctly identified the regime transitions shifted from defensive (2020) to commodity-long (2021) to cash-heavy with short bonds (2022), capturing returns in each phase. A trader who stayed in a static 60/40 portfolio endured the worst bond-equity drawdown in 40 years during 2022.

## Key mechanics and formulas
- **Regime classification**: Regime = f(growth indicator, inflation indicator); each measured relative to trend or expectations
- **Growth indicators**: ISM/PMI manufacturing and services, real GDP growth, employment, industrial production
- **Inflation indicators**: CPI, PPI, breakeven inflation, commodity price indices
- **Regime transition probability**: estimated using Markov switching models; P(regime j at t+1 | regime i at t) = transition matrix element (i,j)
- **Asset return by regime (historical averages, annualized)**:
  - Goldilocks: equities +15%, bonds +5%, commodities +5%
  - Reflation: equities +10%, bonds -2%, commodities +20%
  - Stagflation: equities -5%, bonds -5%, commodities +10%
  - Deflation: equities -15%, bonds +10%, commodities -20%
- **Regime duration**: average regime lasts 12 to 36 months; transitions take 3 to 6 months

## Prerequisites
- [[GDP]]
- [[Inflation]]
- [[Central Bank Policy]]
- [[Business Cycle]]

## Related concepts (learn next)
- [[Risk Parity]]: designed to allocate across all regimes; performs worst during rapid regime transitions.
- [[Carry Cross Asset]]: carry trades perform best in Goldilocks (low vol, positive carry) and worst in Stagflation (forced unwinding).
- [[Momentum Cross Asset]]: momentum captures persistent regime trends; struggles at regime inflection points.
- [[Correlation Breakdown]]: regime transitions cause asset correlations to shift, breaking diversification assumptions.
- [[Real Rates Regime]]: the real rate environment is a sub-regime that specifically drives bond, gold, and currency dynamics.
- [[DXY Correlation]]: the USD tends to strengthen in Deflation (safe haven) and weaken in Reflation (risk-on).
- [[CTA]]: CTAs profit from persistent regimes that create multi-month trends.
- [[Terms of Trade Shock]]: an exogenous shock that can trigger regime transitions.

## Common misconceptions
1. **"There are only 4 regimes"**: The 2x2 growth/inflation framework is a simplification. Sub-regimes (e.g., "growth scare without inflation" vs. "outright recession") have meaningfully different asset class implications. Some practitioners use 6 to 8 regimes for finer granularity.
2. **"You can identify regimes in real time"**: Regime identification is much easier in hindsight. Real-time indicators are noisy and subject to revision (GDP is revised 3 times, PMIs can give false signals). Traders should assign probabilities to regimes rather than making binary calls.
3. **"Regime-aware strategies always outperform"**: If regime identification is wrong (e.g., positioning for Deflation when the regime is actually Stagflation), the losses can be larger than a static allocation because of the concentrated bets. Humility and hedging are essential.

## Sources
- Ilmanen, Antti, "Expected Returns," Wiley (2011)
- Bridgewater Associates, "The All Weather Story" (2012)
- Ang, Andrew, "Asset Management: A Systematic Approach to Factor Investing," Oxford University Press (2014)
- Greer, Robert, "What Is an Asset Class, Anyway?," Journal of Portfolio Management (1997)
