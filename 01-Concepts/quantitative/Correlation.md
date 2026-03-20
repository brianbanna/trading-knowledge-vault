---
aliases: [correlation, cross-asset correlation, rolling correlation, conditional correlation]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-20"
---

# Correlation

## Definition

Correlation measures the strength and direction of the linear relationship between 2 variables, ranging from -1 (perfect inverse) to +1 (perfect co-movement), with 0 indicating no linear relationship. In trading, correlation quantifies how assets move together and is the foundation of portfolio risk management, [[Hedging]], and [[Relative Value Trade|spread trading]]. Crucially, correlation is NOT constant. It varies over time, across market regimes, and conditional on the direction and magnitude of moves. Correlation in calm markets is often very different from correlation in crisis ([[Risk-On Risk-Off]]).

## Why it matters (commodities and FX)

Correlation determines whether adding a position to your portfolio increases or reduces risk. If you are long [[Brent Crude]] and long [[WTI Crude Oil]], the 0.95+ correlation means you have almost double the exposure, not diversification. If you are long Brent and long [[Gold Futures]], the near zero unconditional correlation provides genuine diversification. But in a crisis, the correlation structure changes: Brent and gold might both fall (liquidation driven) or gold might rally while Brent falls ([[Safe Haven Assets]]). The conditional correlation under stress is what matters for risk management, not the average.

For spread traders, the correlation between the 2 legs determines how much directional risk is hedged. A [[Brent-WTI Spread]] with 0.95 correlation hedges ~95% of directional risk. A gold/oil spread with 0.20 correlation hedges very little directional risk and is closer to 2 separate directional bets.

## Concrete example

**Portfolio risk with correlation:**
Position 1: long $1 million in [[Brent Crude]], vol = 30%
Position 2: long $1 million in [[Copper Futures]], vol = 25%
Correlation = 0.50

Portfolio volatility = sqrt(0.30² + 0.25² + 2 x 0.50 x 0.30 x 0.25) = sqrt(0.09 + 0.0625 + 0.075) = sqrt(0.2275) = 47.7%

If they were perfectly correlated (ρ = 1.0): vol = 30% + 25% = 55%
If uncorrelated (ρ = 0): vol = sqrt(0.09 + 0.0625) = 39.1%
If negatively correlated (ρ = -0.50): vol = sqrt(0.09 + 0.0625 - 0.075) = 27.8%

The correlation difference between 0.5 and -0.5 changes portfolio risk by ~20 percentage points. This is why correlation matters as much as individual asset volatility.

**Correlation breakdown:** In Q1 2020, the rolling 60 day correlation between crude oil and AUD/USD was 0.55 (normal). During the COVID crash, the 20 day correlation spiked to 0.85 as everything sold off together ([[Risk-On Risk-Off]]). A trader who sized their portfolio based on the 0.55 long term correlation was underestimating their actual risk during the stress period.

## Key mechanics and formulas

**Pearson correlation:**
`ρ = Cov(X,Y) / (σ_X x σ_Y) = Σ((X_i - X̄)(Y_i - Ȳ)) / (n x σ_X x σ_Y)`

**Portfolio variance (2 assets):**
`σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂`

**Correlation vs causation:** Correlation measures co-movement, not causation. Gold and silver are correlated because they share common demand drivers (safe haven, monetary metal), not because one causes the other to move.

**Correlation vs cointegration:** Two assets can be highly correlated but NOT cointegrated (they move together but can diverge permanently). Cointegration implies a stable long run equilibrium between the levels, which is a stronger condition required for [[Mean Reversion]] strategies. Always test for cointegration (Engle-Granger, Johansen) before assuming a spread will revert.

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
- [[Relative Value Trade]] - spread trading requires understanding the correlation between the 2 legs to know how much directional risk is hedged.
- [[Risk-On Risk-Off]] - RORO regimes change correlation structure. All risky assets become highly correlated in stress.
- [[Hedging]] - the optimal hedge ratio depends on correlation. Hedge effectiveness = ρ².
- [[Commodity Currencies]] - specific commodity/currency correlations are the foundation of cross asset trading.
- [[Structural Break]] - correlation regime changes are structural breaks that affect portfolio risk and spread strategies.
- [[Mean Reversion]] - correlation is necessary but not sufficient for spread trading. Cointegration is the stronger requirement.
- [[Z-Score]] - Z-score signals on correlated spreads are not independent. Portfolio level Z-score analysis requires correlation adjustment.

## Common misconceptions

**"Correlation = diversification."** Low correlation provides diversification in NORMAL times. In crises, correlations spike toward 1.0, and diversification benefits evaporate precisely when you need them most. Stress test portfolios under crisis correlations, not average correlations.

**"Correlation is stable."** It is not. Use rolling windows and regime-conditioned estimates. A single long-term correlation number is misleading.

**"Two highly correlated assets make a good spread trade."** Correlation alone does not ensure the spread will mean revert. You need cointegration (a stable equilibrium relationship between levels) and a fundamental reason for the relationship. Many correlated pairs diverge permanently.

## Sources

- Engle, Robert, "Dynamic Conditional Correlation" (2002, Journal of Business and Economic Statistics)
- Longin and Solnik, "Extreme Correlation of International Equity Markets" (2001, Journal of Finance)
- Erb and Harvey, "The Tactical and Strategic Value of Commodity Futures" (2006)
