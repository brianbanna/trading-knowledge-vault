---
aliases: [correlation, cross-asset correlation, rolling correlation, conditional correlation]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-20"
---

# Correlation

## Definition

Correlation is the strength and direction of the linear relationship between 2 variables, ranging from -1 (perfect inverse) to +1 (perfect co-movement), with 0 meaning no linear relationship. In trading, correlation quantifies how assets move together and is the foundation of portfolio risk management, [[Hedging]], and [[Relative Value Trade|spread trading]]. Correlation is NOT constant. It varies over time, across market regimes, and conditional on the direction and magnitude of moves. Calm market correlation differs sharply from crisis correlation ([[Risk-On Risk-Off]]).

## Why it matters (commodities and FX)

Correlation determines whether adding a position increases or reduces portfolio risk. Long [[Brent Crude]] plus long [[WTI Crude Oil]] at 0.95+ correlation is almost double the exposure, not diversification. Long Brent plus long [[Gold Futures]] at near zero unconditional correlation provides genuine diversification. In a crisis the structure changes: Brent and gold both fall (liquidation) or gold rallies while Brent falls ([[Safe Haven Assets]]). Conditional correlation under stress matters for risk management, not the average.

For spread traders, correlation between the 2 legs determines hedged directional risk. A [[Brent-WTI Spread]] at 0.95 correlation hedges ~95% of directional risk. A gold/oil spread at 0.20 correlation hedges little and is closer to 2 separate directional bets.

## Concrete example

**Concrete:** Long $1M [[Brent Crude]] at 30% vol and long $1M [[Copper Futures]] at 25% vol. Correlation 0.50. Portfolio vol = sqrt(0.30² + 0.25² + 2 × 0.50 × 0.30 × 0.25) = sqrt(0.2275) = 47.7%. At ρ = 1.0: vol = 55%. At ρ = 0: vol = 39.1%. At ρ = -0.50: vol = 27.8%. The correlation swing from 0.5 to -0.5 changes portfolio risk by ~20 percentage points. In Q1 2020 the rolling 60 day correlation between crude oil and AUDUSD was 0.55 (normal); during the COVID crash, the 20 day correlation spiked to 0.85. A trader sized to the 0.55 long term correlation was undercapitalized for the stress period.

**Simplified:** Two assets that move together give you no diversification, even if you own them in different names. Two assets that move opposite hedge each other. Two assets uncorrelated cut your risk via the square root of sum of squares math. The size of that risk reduction depends entirely on the correlation number. Correlation also flips in a crisis: things that normally do their own thing all crash together when everyone needs cash. Plan for the crisis correlation, not the calm one.

## Key mechanics and formulas

**Pearson correlation:**
`ρ = Cov(X,Y) / (σ_X × σ_Y) = Σ((X_i - X̄)(Y_i - Ȳ)) / (n × σ_X × σ_Y)`

**Portfolio variance (2 assets):**
`σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂`

**Correlation vs causation:** Correlation measures co-movement, not causation. Gold and silver are correlated through shared demand drivers (safe haven, monetary metal), not because one causes the other.

**Correlation vs cointegration:** Two assets can be highly correlated but NOT cointegrated (they move together but diverge permanently). Cointegration implies a stable long run equilibrium between levels, a stronger condition required for [[Mean Reversion]] strategies. Test for cointegration (Engle-Granger, Johansen) before assuming a spread will revert.

**Correlation instability:**
Rolling 60 day correlations for major commodity pairs:
- Brent/WTI: 0.90 to 0.99 (very stable)
- Oil/Gold: -0.20 to +0.40 (unstable, regime dependent)
- Copper/AUD: 0.40 to 0.80 (moderately stable)
- Oil/CAD: 0.30 to 0.70 (moderately stable)

## Prerequisites
- [[Volatility]]
- [[Forward Curve]]

## Related concepts (learn next)
- [[Relative Value Trade]] - spread trading requires correlation between legs to size hedged directional risk.
- [[Risk-On Risk-Off]] - RORO regimes change correlation structure. Risky assets become highly correlated in stress.
- [[Hedging]] - optimal hedge ratio depends on correlation. Hedge effectiveness = ρ².
- [[Commodity Currencies]] - specific commodity/currency correlations underpin cross asset trading.
- [[Structural Break]] - correlation regime changes are structural breaks affecting risk and spread strategies.
- [[Mean Reversion]] - correlation is necessary but not sufficient. Cointegration is the stronger requirement.
- [[Z-Score]] - Z-score signals on correlated spreads are not independent. Portfolio Z-score analysis requires correlation adjustment.

## Common misconceptions

**"Correlation = diversification."** Low correlation provides diversification in normal times. In crises correlations spike toward 1.0, and diversification evaporates when you need it most. Stress test under crisis correlations.

**"Correlation is stable."** It is not. Use rolling windows and regime conditioned estimates.

**"Two highly correlated assets make a good spread trade."** Correlation alone does not ensure reversion. You need cointegration and a fundamental reason for the relationship.

## Sources

- Engle, Robert, "Dynamic Conditional Correlation" (2002, Journal of Business and Economic Statistics)
- Longin and Solnik, "Extreme Correlation of International Equity Markets" (2001, Journal of Finance)
- Erb and Harvey, "The Tactical and Strategic Value of Commodity Futures" (2006)
