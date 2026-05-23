---
aliases: [correlation breakdown, correlation regime change, diversification failure]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-03-20"
---

# Correlation Breakdown

## Definition
Correlation breakdown is a sudden shift in cross asset correlations, usually during financial stress, that causes diversified portfolios to suffer simultaneous losses across supposedly uncorrelated positions. The textbook case is the stock bond correlation: from 2000 to 2020, stocks and bonds were negatively correlated, providing a natural hedge. In 2022, both fell together as inflation forced aggressive hikes, producing the worst combined stock bond drawdown in decades. Correlation breakdown is the fundamental risk that undermines [[Risk Parity]] and [[Modern Portfolio Theory]]. It is not random: it is systematically linked to [[macro regime]] transitions, liquidity crises, and forced deleveraging.

## Why it matters (commodities and FX)
Correlation breakdown is the primary tail risk for multi asset portfolios that hold commodities and FX. In calm regimes, commodities correlate modestly with equities (0.2 to 0.4) and negatively with USD (−0.3 to −0.5). In a liquidity crisis, every risky asset (commodities, high beta FX) sells off together as participants liquidate to raise cash, pushing correlations toward 1.0. March 2020 saw crude, equities, credit, EM FX, and even gold decline simultaneously for several days. For FX carry traders, breakdown is devastating: in 2008, AUDJPY fell 40% in 3 months as all carry pairs unwound together. Correlations are regime dependent, not constant. Sizing and hedging must reflect this.

## Concrete example
**Concrete:** A risk parity fund holds equities, bonds, commodities, and gold with equal risk contribution, assuming correlations of equity bond −0.3, equity commodity 0.3, equity gold 0.0, bond commodity −0.1. In September 2022, the Fed hikes 75 bps and signals more. Realized correlations shift to equity bond +0.7, equity commodity +0.6, equity gold +0.5, bond commodity +0.4. The portfolio now behaves like 80% in one correlated factor. It loses 12% in a month versus an expected worst case of 5%. Separately, an FX book long AUDUSD, NZDUSD, MXNUSD against short JPYUSD sees all 3 longs fall 5 to 10% as risk aversion spikes. Pairwise correlation jumps from 0.4 to 0.9 — 3 diversified bets collapse into 1 concentrated bet.

**Simplified:** Diversification depends on assets moving independently. In a crisis, they stop. Forced selling, margin calls, and de-risking push every risky asset down together. Hedges built on the prior correlation matrix fail at the exact moment they are needed. A portfolio designed for diversification suddenly behaves like one concentrated bet. The breakdown reverses once forced flows are done, but the damage during the panic phase is what matters.

## Key mechanics and formulas
- **Conditional correlation:** Corr(X, Y | stress) > Corr(X, Y | calm)
- **DCC (Dynamic Conditional Correlation):** H(t) = D(t) × R(t) × D(t), time varying correlation
- **Copula tail dependence:** probability of joint crash. Gaussian copulas understate this, producing false diversification confidence
- **Correlation surprise:** realized stressed correlation − expected correlation; large positive values flag breakdown
- **Portfolio variance under breakdown:** Var = Σ w_i² × var_i + Σ w_i × w_j × cov_stressed_ij; substituting stressed covariance doubles or triples expected variance
- **Diversification ratio:** DR = (Σ w_i × vol_i) / portfolio vol; DR > 1 indicates diversification benefit, DR → 1 indicates breakdown

## Prerequisites
- [[Correlation]]
- [[Volatility]]
- [[Portfolio Construction]]
- [[Risk Management]]

## Related concepts (learn next)
- [[Risk Parity]]: the strategy most exposed to breakdown since its premise is stable cross asset diversification.
- [[Macro Regime]]: regime transitions (especially to stagflation) drive correlation regime change.
- [[Positioning Signal]]: crowded same direction positioning amplifies breakdown as everyone exits at once.
- [[CTA]]: CTA deleveraging during trend reversals contributes to cross asset correlation spikes.
- [[Carry Cross Asset]]: carry unwinds are a classic breakdown scenario.
- [[Momentum Cross Asset]]: momentum strategies can both suffer from and adapt to breakdown.
- [[DXY Correlation]]: USD strengthens during breakdown as a safe haven, amplifying commodity and EM FX losses.

## Common misconceptions
1. **"Diversification always works."** It reduces risk in normal regimes but partially fails in the exact scenarios when risk reduction matters most. "Correlations go to 1 in a crisis" is an exaggeration but captures the real asymmetry.
2. **"A longer lookback window solves it."** A 5 year window blends calm and stressed periods, averaging out tail risk. Regime conditional models or stress testing with crisis correlations are required.
3. **"Gold is always a safe haven."** Gold helps in 2008 and post initial 2020, but in acute liquidity crises it sells off as participants raise cash. March 2020 saw gold drop 12% before recovering.
4. **"Breakdown is unpredictable."** Timing is, but the conditions are identifiable: high leverage, crowded positioning, macro regime uncertainty, policy inflection points.

## Sources
- Longin, Francois, Solnik, Bruno, "Extreme Correlation of International Equity Markets," Journal of Finance (2001)
- Engle, Robert, "Dynamic Conditional Correlation: A Simple Class of Multivariate GARCH Models," Journal of Business & Economic Statistics (2002)
- Page, Sebastien, Panariello, Robert, "When Diversification Fails," Financial Analysts Journal (2018)
- Ilmanen, Antti, "Expected Returns," Wiley (2011)
