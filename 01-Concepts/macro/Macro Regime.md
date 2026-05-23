---
aliases: [macro regime, economic regime, growth-inflation regime]
tags:
  - "#macro"
date-added: "2026-03-20"
---

# Macro Regime

## Definition
A macro regime is a persistent economic environment defined by the combination of growth and inflation conditions. The 4 canonical regimes: (1) Goldilocks (above trend growth, below trend inflation), (2) Reflation (above trend growth, above trend inflation), (3) Stagflation (below trend growth, above trend inflation), (4) Deflation/Recession (below trend growth, below trend inflation). Each produces distinct patterns in asset returns, correlations, and volatilities. Equities and credit thrive in Goldilocks; commodities and inflation linked bonds outperform in Reflation; cash and trend following protect in Stagflation; government bonds rally in Deflation. Regime identification is the highest level strategic decision a macro trader makes because it determines which asset classes, factors, and strategies work. Regimes persist for months to years, driven by central bank policy, fiscal policy, and structural forces.

## Why it matters (commodities and FX)
Regime awareness is the most important context for commodity and FX trading. Commodities are the highest beta asset to growth/inflation: they strongly outperform in Reflation (rising demand, pricing power, tight supply) and strongly underperform in Deflation (collapsing demand, excess supply). FX regimes are driven by relative growth and rate differentials: in global Goldilocks, carry trades work (high risk appetite, low vol); in Stagflation, commodity exporters (AUD, CAD, NOK) diverge from importers (JPY, EUR), creating powerful FX trends. [[Risk Parity]] portfolios are designed to weather all 4 regimes, but rapid transitions cause [[Correlation Breakdown]] and drawdowns. [[CTA]] strategies benefit from persistent regimes (trends) and struggle during transitions (whipsaws).

## Concrete example

**Concrete:** From 2020 to 2024, the world cycled through 3 regimes. 2020 Q1 to Q2: Deflationary shock. COVID lockdowns crashed growth and inflation. Oil went negative, equities dropped 35%, bonds rallied. 2021 to mid 2022: Reflationary boom. Fiscal stimulus, supply chains, reopening drove GDP above 5% and inflation above 8%. Crude rallied from 40 to 120, copper hit ATHs, AUD/CAD/BRL surged. 2022 H2 to 2023: Stagflationary scare. CBs hiked aggressively, growth slowed, inflation stuck. Bonds and equities fell together (rare), and [[Risk Parity]] funds suffered. A macro trader who identified regime transitions shifted from defensive (2020) to commodity long (2021) to cash heavy with short bonds (2022), capturing returns in each phase. A 60/40 trader endured the worst bond equity drawdown in 40 years during 2022.

**Simplified:** Growth and inflation are 2 dials. Each one is either above or below trend. That gives 4 combinations, and each combination favors a different mix of assets. Knowing which quadrant you are in is more valuable than picking individual securities. The hard part: dial readings come late and get revised. You are always trading the previous quadrant while standing in the next one.

## Key mechanics and formulas
- **Regime classification**: Regime = f(growth indicator, inflation indicator); each measured relative to trend or expectations
- **Growth indicators**: ISM/PMI manufacturing and services, real GDP, employment, industrial production
- **Inflation indicators**: CPI, PPI, breakeven inflation, commodity price indices
- **Regime transition probability**: estimated with Markov switching models; P(regime j at t+1 | regime i at t) = transition matrix element (i,j)
- **Asset return by regime (historical annualized averages)**:
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
- [[Risk Parity]]: designed to allocate across regimes; performs worst during rapid transitions.
- [[Carry Cross Asset]]: carry trades perform best in Goldilocks (low vol, positive carry), worst in Stagflation (forced unwinding).
- [[Momentum Cross Asset]]: momentum captures persistent regime trends; struggles at inflection points.
- [[Correlation Breakdown]]: transitions cause correlations to shift, breaking diversification assumptions.
- [[Real Rates Regime]]: a sub regime that specifically drives bond, gold, and currency dynamics.
- [[DXY Correlation]]: USD tends to strengthen in Deflation (safe haven) and weaken in Reflation (risk on).
- [[CTA]]: profits from persistent regimes that create multi month trends.
- [[Terms of Trade Shock]]: an exogenous shock that can trigger regime transitions.

## Common misconceptions
1. **"There are only 4 regimes"**: The 2x2 framework is a simplification. Sub regimes ("growth scare without inflation" vs "outright recession") have meaningfully different implications. Some practitioners use 6 to 8 regimes.
2. **"You can identify regimes in real time"**: Identification is much easier in hindsight. Real time indicators are noisy and revised (GDP is revised 3 times, PMIs give false signals). Assign probabilities rather than make binary calls.
3. **"Regime aware strategies always outperform"**: If identification is wrong (positioning for Deflation when actually Stagflation), losses are larger than a static allocation because of concentrated bets. Humility and hedging are essential.

## Sources
- Ilmanen, Antti, "Expected Returns," Wiley (2011)
- Bridgewater Associates, "The All Weather Story" (2012)
- Ang, Andrew, "Asset Management: A Systematic Approach to Factor Investing," Oxford University Press (2014)
- Greer, Robert, "What Is an Asset Class, Anyway?," Journal of Portfolio Management (1997)
