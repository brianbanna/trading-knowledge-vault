---
aliases: [Sharpe ratio, Sharpe, risk-adjusted return, reward-to-risk ratio]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-27"
---

# Sharpe Ratio

## Definition
The Sharpe ratio is excess return per unit of risk, where risk is defined as the [[standard deviation]] of returns. Introduced by William Sharpe in 1966. Formula: Sharpe = (R_p - R_f) / sigma_p, R_p = portfolio return, R_f = risk free rate, sigma_p = standard deviation. Sharpe above 1.0 is good, above 2.0 excellent, above 3.0 exceptional (scrutinize for data issues or overfitting). The single most cited performance metric in quantitative finance.

## Why it matters (commodities and FX)
Commodity and FX strategies are judged primarily by Sharpe. A [[trend following]] strategy on crude returning 15% per year at 30% vol has Sharpe ~0.5 (assuming 0% risk free rate). A mean reversion strategy on [[EURUSD]] returning 8% at 4% vol has Sharpe ~2.0. Despite the lower absolute return, the FX strategy is far more attractive because it can be levered. Sharpe 2.0 levered 3x produces 24% return at 12% vol, maintaining Sharpe 2.0. The fundamental insight: Sharpe tells you the quality of the return stream, and [[leverage]] scales it. CTAs, FX overlay managers, and prop desks all use Sharpe as primary metric.

## Concrete example

**Concrete:** A copper momentum strategy produces monthly returns over 1 year: +2.1%, -0.8%, +1.5%, +3.2%, -1.1%, +0.9%, +2.4%, -0.3%, +1.8%, +0.6%, -0.5%, +1.7%. Mean monthly 0.96%, monthly std dev 1.34%. Annualized Sharpe (0% risk free) = (0.96% × 12) / (1.34% × sqrt(12)) = 11.52% / 4.64% = 2.48. Excellent. Fail scenario: the same strategy is backtested over 3 years showing Sharpe 2.5 in sample, but live trading for 1 year produces Sharpe 0.6. Classic overfitting. In sample Sharpe inflated by parameter optimization, survivorship bias, or ignoring [[transaction cost analysis]]. Realistic live Sharpe is 30 to 60% of backtested.

**Simplified:** Sharpe measures how much return you get per unit of wobble. A strategy that earns 10% with smooth returns beats one earning 10% with wild swings. Once you know Sharpe, you can scale up returns with leverage as long as the underlying quality holds. The catch is that the quality rarely survives outside the backtest. Live Sharpe is almost always lower than in sample Sharpe. Treat backtest numbers as upper bounds, not forecasts.

## Key mechanics and formulas
- **Sharpe ratio**: Sharpe = (R_p - R_f) / sigma_p. R_p = annualized return, R_f = annualized risk free rate, sigma_p = annualized std dev.
- **Annualization from daily data**: Annualized return = daily mean × 252. Annualized vol = daily std × sqrt(252). Sharpe = (daily mean × 252) / (daily std × sqrt(252)) = daily mean × sqrt(252) / daily std.
- **Annualization from monthly data**: Sharpe = monthly mean × 12 / (monthly std × sqrt(12)).
- **Standard error of Sharpe**: SE(Sharpe) = sqrt((1 + 0.5 × Sharpe^2) / N), N = number of observations. Sharpe 2.0 from 1 year of monthly data (N = 12) has SE ~0.46, true Sharpe plausibly 1.1 to 2.9.
- **Leverage scaling**: A strategy with Sharpe S levered by L: new return = L × R_p, new vol = L × sigma_p, Sharpe = S (ignoring financing).

## Prerequisites
- [[Realized Volatility]]
- [[Correlation]]
- [[Mean Reversion]]

## Related concepts (learn next)
- [[Sortino Ratio]]: penalizes only downside vol. Useful for asymmetric return distributions.
- [[Maximum Drawdown]]: Sharpe says nothing about peak to trough losses. Sharpe 2.0 can have 20%+ drawdown.
- [[Risk Parity]]: portfolio construction allocating inversely to vol, implicitly maximizing portfolio Sharpe.
- [[Calmar Ratio]]: return divided by max drawdown, complementary metric.
- [[Information Ratio]]: Sharpe relative to a benchmark rather than risk free rate.
- [[Kurtosis]]: fat tails make Sharpe misleadingly high because std dev understates true risk.
- [[Skewness]]: negative skew (rare large losses) is not captured by Sharpe, dangerous for selling options.

## Common misconceptions
1. **"A high Sharpe means the strategy cannot lose money."** Sharpe 2.0 with 10% annualized vol implies a ~2.5% probability of a 20%+ annual loss (assuming normal). Returns are not normal, so actual probability is higher.
2. **"You can compare Sharpe ratios across different time periods."** A Sharpe measured over a bull market is not comparable to one through a crisis. Compare over the same period.
3. **"Sharpe above 3 means the strategy is incredible."** Sustained live Sharpe above 3 is rare. Backtest Sharpe above 3 almost always indicates overfitting, look ahead bias, or unrealistic [[transaction cost analysis]] and [[slippage]] assumptions.
4. **"The Sharpe ratio captures all risk."** Sharpe captures vol risk only. Misses [[tail risk]], [[liquidity]] risk, and drawdown risk. A strategy with small steady gains and occasional catastrophic losses (selling deep OTM options) shows high Sharpe until the blow up.

## Sources
- Sharpe, William, "Mutual Fund Performance," Journal of Business (1966)
- Sharpe, William, "The Sharpe Ratio," Journal of Portfolio Management (1994)
- Lo, Andrew, "The Statistics of Sharpe Ratios," Financial Analysts Journal (2002)
- Bailey, David and Lopez de Prado, Marcos, "The Deflated Sharpe Ratio," Journal of Portfolio Management (2014)
