---
aliases: [risk parity, equal risk contribution]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-20"
---

# Risk Parity

## Definition
Risk parity is a portfolio construction method that allocates capital so each asset or asset class contributes equally to total portfolio risk, rather than equal dollar amounts. In a traditional 60/40 stock/bond portfolio, equities contribute ~90% of total risk because they are far more volatile. Risk parity corrects this by levering low vol assets (bonds, short term rates) and reducing allocation to high vol assets (equities, commodities) so each risk contribution is equal. Popularized by Bridgewater's All Weather, the approach is now a multi hundred billion dollar category. Risk parity requires leverage (low risk assets must be scaled up) and is inherently a [[volatility]] targeting framework. It bridges equities, bonds, commodities, and often FX or inflation linked instruments.

## Why it matters (commodities and FX)
Risk parity is a primary reason institutional capital flows into commodities and commodity linked FX. A risk parity fund allocating across 4 asset classes (equities, bonds, commodities, inflation linked) might put 25% of its risk budget into commodities, translating to significant notional given commodities' higher vol. This creates structural demand for commodity futures (typically via [[roll yield]] positions in energy, metals, and agriculture). In FX, risk parity funds generate flows when they hedge or do not hedge international bond and commodity positions. Rebalancing (monthly, vol triggered) produces predictable FX flows analogous to [[FX Fix]] rebalancing. When vol spikes, risk parity funds deleverage across all assets simultaneously, contributing to [[correlation breakdown]] and cross asset selling.

## Concrete example
**Concrete:** A risk parity fund with $10B targets 10% annualized vol. Current annualized vols: equities 15%, bonds 5%, commodities 20%, gold 18%. To equalize risk contribution: equities $1.67B, bonds $5B, commodities $1.25B, gold $1.39B. Total notional $9.31B, ~1x leverage. If bond vol drops to 3%, the bond allocation scales to $8.33B, pushing total to $12.64B (1.26x leverage). If equity vol spikes 15% to 30% (stress event), the fund cuts equity exposure 50% and reduces leverage. Forced selling amplifies the equity decline and spills into other assets via [[correlation breakdown]]. In March 2020, risk parity funds' simultaneous deleveraging across stocks, bonds, and commodities contributed to the "sell everything" dynamic.

**Simplified:** Equal dollars in stocks and bonds means almost all your portfolio risk is in the stocks because they move more. Risk parity flips this: weight by inverse vol so each asset contributes the same risk. Bonds get the biggest dollar slice (and require leverage to make them matter), stocks get a small slice. Diversification improves in normal times. The catch: when everything crashes together, the leverage cuts the wrong way and you sell everything at once.

## Key mechanics and formulas
- **Risk contribution of asset i**: RC(i) = w(i) × (covariance matrix × weight vector)(i) / portfolio volatility
- **Equal risk contribution condition**: RC(i) = RC(j) for all assets i, j
- **Inverse volatility weighting (simplified)**: w(i) = (1 / vol(i)) / sum(1 / vol(j) for all j); ignores correlations
- **Portfolio volatility**: sigma(p) = sqrt(w' × Sigma × w), Sigma = covariance matrix, w = weight vector
- **Leverage ratio**: L = total notional exposure / capital; risk parity typically runs 1.5x to 3x
- **Volatility targeting**: scale weights by target vol / realized vol to maintain constant portfolio risk
- **Rebalancing trigger**: rebalance when any asset's risk contribution deviates from target by > threshold (e.g., 20% relative)

## Prerequisites
- [[Volatility]]
- [[Correlation]]
- [[Portfolio Construction]]
- [[Leverage]]

## Related concepts (learn next)
- [[Carry Cross Asset]]: risk parity portfolios earn carry from bond coupons, commodity roll yield, and FX rate differentials.
- [[Momentum Cross Asset]]: static allocation framework; adding momentum as timing overlay improves risk adjusted returns.
- [[Correlation Breakdown]]: biggest vulnerability. When correlations spike to 1, diversification vanishes.
- [[Macro Regime]]: performs differently across regimes; stagflation (rising inflation, falling growth) is worst.
- [[CTA]]: CTAs and risk parity overlap in commodity futures and can amplify each other's flows.
- [[Value Cross Asset]]: value signals can inform tactical tilts within a risk parity framework.
- [[Real Rates Regime]]: real rate environment determines bond returns, the largest nominal allocation.

## Common misconceptions
1. **"Risk parity is just equal weighting."** Equal dollar weighting ignores asset vol differences. Risk parity weights inversely by risk: bonds typically receive 3 to 5x the dollar allocation of equities.
2. **"Risk parity eliminates drawdowns."** It reduces concentration risk but does not eliminate drawdowns. When all assets decline together (March 2020, 2022 rate hiking), risk parity suffers because diversification fails.
3. **"Leverage makes risk parity dangerous."** Leverage is applied to low vol assets (mainly bonds), so total risk is comparable to an unleveraged equity portfolio. The danger is not the leverage; it is the assumption that bond vol stays low.

## Sources
- Qian, Edward, "Risk Parity Portfolios: Efficient Portfolios Through True Diversification," Panagora Asset Management (2005)
- Asness, Clifford, Frazzini, Andrea, Pedersen, Lasse, "Leverage Aversion and Risk Parity," Financial Analysts Journal (2012)
- Bridgewater Associates, "The All Weather Story" (2012)
- Roncalli, Thierry, "Introduction to Risk Parity and Budgeting," Chapman & Hall (2013)
