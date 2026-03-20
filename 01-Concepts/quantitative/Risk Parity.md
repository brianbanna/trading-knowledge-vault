---
aliases: [risk parity, equal risk contribution]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-20"
---

# Risk Parity

## Definition
Risk parity is a portfolio construction method that allocates capital so that each asset or asset class contributes equally to the total portfolio risk, rather than allocating equal dollar amounts. In a traditional 60/40 stock/bond portfolio, equities contribute roughly 90% of total portfolio risk because they are far more volatile than bonds. Risk parity corrects this imbalance by leveraging low-volatility assets (bonds, short-term rates) and reducing allocation to high-volatility assets (equities, commodities) so that each component's risk contribution is equal. The approach was popularized by Bridgewater Associates' All Weather fund and has become a multi-hundred-billion-dollar strategy category. Risk parity requires leverage (since low-risk assets must be scaled up to match higher-risk assets' contribution) and is inherently a [[volatility]] targeting framework. It bridges all major asset classes: equities, bonds, commodities, and often FX or inflation-linked instruments.

## Why it matters (commodities and FX)
Risk parity is one of the primary reasons institutional capital flows into commodities and commodity-linked FX. A risk parity fund allocating to 4 asset classes (equities, bonds, commodities, inflation-linked bonds) might put 25% of its risk budget into commodities, which translates to significant notional exposure given commodities' higher volatility. This creates structural demand for commodity futures (typically via [[roll yield]] generating positions in energy, metals, and agriculture). In FX, risk parity funds create flows when they hedge or do not hedge their international bond and commodity positions. Risk parity rebalancing (which is typically monthly and volatility-triggered) generates predictable FX flows analogous to [[FX Fix]] rebalancing flows. When volatility spikes, risk parity funds deleverage across all assets simultaneously, contributing to [[correlation breakdown]] and cross-asset selling pressure.

## Concrete example
A risk parity fund with 10 billion in capital targets 10% annualized portfolio volatility. Current annualized volatilities: equities 15%, bonds 5%, commodities 20%, gold 18%. To equalize risk contribution, the fund allocates: equities 1.67 billion (10% / 15% x scaling), bonds 5 billion (10% / 5% x scaling), commodities 1.25 billion (10% / 20% x scaling), gold 1.39 billion (10% / 18% x scaling). Total notional: 9.31 billion, close to 1x leverage. But if bond vol drops to 3%, the bond allocation scales to 8.33 billion, pushing total notional to 12.64 billion (1.26x leverage). Now suppose equity volatility spikes from 15% to 30% (a stress event). The fund must cut equity exposure by 50% and simultaneously reduce leverage. This forced selling amplifies the equity decline and spills into other assets via [[correlation breakdown]]. In 2020 (March), risk parity funds' simultaneous deleveraging across stocks, bonds, and commodities contributed to the "sell everything" dynamic.

## Key mechanics and formulas
- **Risk contribution of asset i**: RC(i) = w(i) x (covariance matrix x weight vector)(i) / portfolio volatility
- **Equal risk contribution condition**: RC(i) = RC(j) for all assets i, j
- **Inverse volatility weighting (simplified)**: w(i) = (1 / vol(i)) / sum(1 / vol(j) for all j); ignores correlations but is a common approximation
- **Portfolio volatility**: sigma(p) = sqrt(w' x Sigma x w), where Sigma is the covariance matrix and w is the weight vector
- **Leverage ratio**: L = total notional exposure / capital; risk parity typically runs 1.5x to 3x leverage
- **Volatility targeting**: scale all weights by target vol / realized vol to maintain constant portfolio risk
- **Rebalancing trigger**: rebalance when any asset's risk contribution deviates from target by more than a threshold (e.g., 20% relative)

## Prerequisites
- [[Volatility]]
- [[Correlation]]
- [[Portfolio Construction]]
- [[Leverage]]

## Related concepts (learn next)
- [[Carry Cross Asset]]: risk parity portfolios earn carry from bond coupons, commodity roll yield, and FX rate differentials.
- [[Momentum Cross Asset]]: risk parity is a static allocation framework; adding momentum as a timing overlay can improve risk-adjusted returns.
- [[Correlation Breakdown]]: risk parity's biggest vulnerability; when correlations between assets spike to 1, diversification vanishes.
- [[Macro Regime]]: risk parity performs differently across macro regimes; stagflation (rising inflation, falling growth) is the worst environment.
- [[CTA]]: CTAs and risk parity funds overlap in commodity futures positioning and can amplify each other's flows.
- [[Value Cross Asset]]: value signals can inform tactical tilts within a risk parity framework.
- [[Real Rates Regime]]: the real rate environment determines bond returns, the largest nominal allocation in risk parity.

## Common misconceptions
1. **"Risk parity is just equal weighting"**: Equal dollar weighting ignores the vast differences in asset volatilities. Risk parity weights inversely by risk, which often means bonds receive 3 to 5x the dollar allocation of equities.
2. **"Risk parity eliminates drawdowns"**: Risk parity reduces concentration risk but does not eliminate drawdowns. In periods when all assets decline simultaneously (e.g., March 2020, 2022 rate hiking cycle), risk parity suffers because its diversification assumption fails.
3. **"Leverage makes risk parity dangerous"**: The leverage in risk parity is applied to low-volatility assets (primarily bonds), so the leveraged portfolio's total risk is comparable to an unleveraged equity portfolio. The danger is not the leverage per se but the assumption that bond volatility stays low.

## Sources
- Qian, Edward, "Risk Parity Portfolios: Efficient Portfolios Through True Diversification," Panagora Asset Management (2005)
- Asness, Clifford, Frazzini, Andrea, Pedersen, Lasse, "Leverage Aversion and Risk Parity," Financial Analysts Journal (2012)
- Bridgewater Associates, "The All Weather Story" (2012)
- Roncalli, Thierry, "Introduction to Risk Parity and Budgeting," Chapman & Hall (2013)
