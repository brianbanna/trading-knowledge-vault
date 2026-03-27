---
aliases: [Sharpe ratio, Sharpe, risk-adjusted return, reward-to-risk ratio]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-27"
---

# Sharpe Ratio

## Definition
The Sharpe ratio measures the excess return of an investment per unit of risk, where risk is defined as the [[standard deviation]] of returns. It was introduced by William Sharpe in 1966. The formula is: Sharpe = (R_p - R_f) / sigma_p, where R_p is the portfolio return, R_f is the risk-free rate, and sigma_p is the standard deviation of portfolio returns. A Sharpe ratio above 1.0 is considered good, above 2.0 is excellent, and above 3.0 is exceptional (and should be scrutinized for data issues or overfitting). The Sharpe ratio is the single most widely cited performance metric in quantitative finance, used to compare strategies, allocate capital, and evaluate fund managers.

## Why it matters (commodities and FX)
Commodity and FX trading strategies are judged primarily by their Sharpe ratio. A [[trend following]] strategy on crude oil that returns 15% per year with 30% volatility has a Sharpe of ~0.5 (assuming a 0% risk-free rate), while a mean-reversion strategy on [[EURUSD]] that returns 8% with 4% volatility has a Sharpe of ~2.0. Despite the lower absolute return, the FX strategy is far more attractive on a risk-adjusted basis because it can be levered up. A Sharpe 2.0 strategy levered 3x produces 24% return with 12% volatility, still maintaining a Sharpe of 2.0. This is the fundamental insight: the Sharpe ratio tells you the quality of the return stream, and [[leverage]] scales it. Commodity trading advisors (CTAs), FX overlay managers, and prop desks all use the Sharpe ratio as their primary performance metric.

## Concrete example
A copper momentum strategy produces the following monthly returns over 1 year: +2.1%, -0.8%, +1.5%, +3.2%, -1.1%, +0.9%, +2.4%, -0.3%, +1.8%, +0.6%, -0.5%, +1.7%. The average monthly return is 0.96%. The monthly standard deviation is 1.34%. The annualized Sharpe ratio (assuming 0% risk-free rate) = (0.96% x 12) / (1.34% x sqrt(12)) = 11.52% / 4.64% = 2.48. This is an excellent Sharpe, suggesting a robust strategy.

The fail scenario: the same strategy is backtested over 3 years and shows a Sharpe of 2.5 in sample, but when traded live for 1 year, the Sharpe drops to 0.6. This is classic overfitting. The in-sample Sharpe was inflated by parameter optimization, survivorship bias, or ignoring [[transaction cost analysis]]. A realistic live Sharpe is typically 30% to 60% of the backtested Sharpe.

## Key mechanics and formulas
- **Sharpe ratio**: Sharpe = (R_p - R_f) / sigma_p. R_p = annualized portfolio return, R_f = annualized risk-free rate, sigma_p = annualized standard deviation of returns.
- **Annualization from daily data**: Annualized return = daily mean return x 252. Annualized volatility = daily std dev x sqrt(252). Sharpe = (daily mean x 252) / (daily std x sqrt(252)) = daily mean x sqrt(252) / daily std.
- **Annualization from monthly data**: Sharpe = monthly mean x 12 / (monthly std x sqrt(12)).
- **Standard error of Sharpe**: SE(Sharpe) = sqrt((1 + 0.5 x Sharpe^2) / N), where N is the number of observations. A Sharpe of 2.0 estimated from 1 year of monthly data (N = 12) has a standard error of ~0.46, meaning the true Sharpe could plausibly range from 1.1 to 2.9.
- **Leverage scaling**: If a strategy has Sharpe S and is levered by factor L, the new return = L x R_p, new volatility = L x sigma_p, and the Sharpe remains S (ignoring financing costs).

## Prerequisites
- [[Realized Volatility]]
- [[Correlation]]
- [[Mean Reversion]]

## Related concepts (learn next)
- [[Sortino Ratio]]: a variant that only penalizes downside volatility, useful for strategies with asymmetric return distributions.
- [[Maximum Drawdown]]: the Sharpe ratio says nothing about peak-to-trough losses. A Sharpe 2.0 strategy can still have a 20%+ drawdown.
- [[Risk Parity]]: a portfolio construction approach that allocates capital inversely to volatility, implicitly maximizing portfolio Sharpe.
- [[Calmar Ratio]]: return divided by maximum drawdown, a complementary metric for evaluating strategy quality.
- [[Information Ratio]]: Sharpe ratio relative to a benchmark rather than the risk-free rate, used for benchmarked portfolios.
- [[Kurtosis]]: fat tails in return distributions can make the Sharpe ratio misleadingly high because standard deviation underestimates true risk.
- [[Skewness]]: negative skew (large rare losses) is not captured by the Sharpe ratio, making it dangerous for strategies like selling options.

## Common misconceptions
1. **"A high Sharpe means the strategy cannot lose money"**: A Sharpe of 2.0 with 10% annualized volatility still implies a ~2.5% probability of a 20%+ annual loss (assuming normal returns). And returns are not normal, so the actual probability is higher.
2. **"You can compare Sharpe ratios across different time periods"**: A strategy's Sharpe measured over a bull market is not comparable to one measured through a crisis. Always compare strategies over the same time period.
3. **"Sharpe above 3 means the strategy is incredible"**: In live trading, sustained Sharpe ratios above 3.0 are extremely rare. In backtesting, Sharpe above 3.0 almost always indicates overfitting, look-ahead bias, or unrealistic assumptions about [[transaction cost analysis]] and [[slippage]].
4. **"The Sharpe ratio captures all risk"**: Sharpe only captures volatility risk. It misses [[tail risk]], [[liquidity]] risk, and drawdown risk entirely. A strategy that earns small steady gains but occasionally suffers catastrophic losses (like selling deep out-of-the-money options) can show a high Sharpe until the blow-up.

## Sources
- Sharpe, William, "Mutual Fund Performance," Journal of Business (1966)
- Sharpe, William, "The Sharpe Ratio," Journal of Portfolio Management (1994)
- Lo, Andrew, "The Statistics of Sharpe Ratios," Financial Analysts Journal (2002)
- Bailey, David and Lopez de Prado, Marcos, "The Deflated Sharpe Ratio," Journal of Portfolio Management (2014)
