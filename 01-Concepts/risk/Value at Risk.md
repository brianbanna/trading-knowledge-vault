---
aliases: [VaR, value at risk, portfolio VaR, 1-day VaR, 99% VaR]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-03-24"
---

# Value at Risk

## Definition

Value at Risk (VaR) is a single number that answers the question: "What is the most I can expect to lose over a given time horizon, at a given confidence level, under normal market conditions?" For example, a 1 day 99% VaR of $500,000 means: on 99 out of 100 trading days, you expect to lose no more than $500,000. On that 1 remaining day, you could lose more, potentially much more. Think of VaR as a fence around "normal" losses. It tells you the boundary, but says nothing about how far you can fall if you go over the edge. That limitation is why [[Expected Shortfall]] was developed as a complement.

## Why it matters (commodities and FX)

VaR is the universal language of risk management. Banks, hedge funds, prop desks, and clearing houses all use VaR to set position limits, calculate margin requirements, and allocate capital. If you trade commodities or FX at any institutional level, your risk limits will almost certainly be expressed as a VaR number.

In commodities, VaR is tricky because return distributions are far from normal. Crude oil, natural gas, and softs have fat tails and skewed distributions that parametric VaR systematically underestimates. A parametric VaR on a TTF natural gas position in 2021 would have dramatically understated the actual risk, because a move from EUR 20 to EUR 340/MWh is not in any normal distribution's vocabulary. This is why sophisticated commodity desks supplement parametric VaR with historical VaR, Monte Carlo VaR, and [[Expected Shortfall]].

In FX, VaR works better for G10 pairs (returns are closer to normal) but breaks down for EM currencies where gap risk (devaluations, capital controls) creates discontinuous losses.

## Concrete example

A trader runs a portfolio of 200 lots long [[Brent Crude]] and 50 lots short [[WTI Crude Oil]] (a [[Brent-WTI Spread]] position with directional tilt). Daily vol for Brent is 2.0%, WTI is 2.2%, and the correlation between them is 0.92.

**Parametric VaR (1 day, 99%):**

Portfolio value: Brent = 200 x 1,000 bbl x $82 = $16.4M. WTI = 50 x 1,000 bbl x $78 = $3.9M (short).

Portfolio variance = (16.4M x 0.02)^2 + (3.9M x 0.022)^2 - 2 x 0.92 x (16.4M x 0.02) x (3.9M x 0.022)

Portfolio daily vol = $278,000

1 day 99% VaR = 2.33 x $278,000 = $648,000

**What this means:** On 99% of days, the portfolio loses less than $648,000. But on the 1% worst days (about 2.5 days per year), losses exceed this number.

**What VaR misses:** In March 2020, Brent fell 25% in a single day. That day's loss on this portfolio would have been approximately $3.5 million, roughly 5.4x the VaR estimate. VaR said the fence was at $648,000. The actual loss jumped over the fence by a factor of 5.

## Key mechanics and formulas

### 3 Methods of Calculating VaR

**1. Parametric (Variance-Covariance) VaR**

Assumes returns are normally distributed.

`VaR = Position Value x z_alpha x sigma x sqrt(time)`

Where:
- z_alpha = z score for the confidence level (1.65 for 95%, 2.33 for 99%)
- sigma = daily volatility (annualized vol / sqrt(252))
- time = holding period in days

For a portfolio: `VaR = z_alpha x sqrt(w' x Sigma x w)` where w is the position vector and Sigma is the covariance matrix.

**Pros:** Fast, easy to compute, easy to decompose into risk contributions.
**Cons:** Assumes normality. Badly underestimates tail risk in commodities.

**2. Historical VaR**

Uses actual historical returns. Sort past daily P&Ls from worst to best. The 1st percentile P&L is the 99% VaR.

Example: 1,000 days of history. Sort P&Ls. The 10th worst day is the 99% VaR.

**Pros:** No distributional assumptions. Captures fat tails if they occurred in the lookback window.
**Cons:** Assumes the future looks like the past. If your lookback window does not include a crisis, historical VaR will understate risk. Sensitive to lookback length.

**3. Monte Carlo VaR**

Simulates thousands of random future scenarios using a chosen distribution (can be fat tailed, skewed, correlated). Compute P&L for each scenario. The 1st percentile of simulated P&Ls is the 99% VaR.

**Pros:** Flexible. Can model non-normal distributions, path dependency, option payoffs.
**Cons:** Computationally intensive. Only as good as the model assumptions.

### VaR Parameters

| Parameter | Common choices |
|-----------|---------------|
| Confidence level | 95% (trading desks), 99% (regulatory, risk reports) |
| Time horizon | 1 day (trading), 10 days (Basel regulatory), 1 month (portfolio management) |
| Lookback window | 250 days (1 year), 500 days (2 years), or full history |

### Scaling VaR

`VaR_T = VaR_1day x sqrt(T)`

This "square root of time" rule assumes returns are independent and identically distributed. In practice, serial correlation and volatility clustering (common in commodities) make this approximation unreliable beyond a few days.

### VaR Decomposition

**Marginal VaR:** How much VaR changes if you add $1 to a position. Used for portfolio optimization.

**Component VaR:** Each position's contribution to total portfolio VaR. Sum of component VaRs = total VaR.

**Incremental VaR:** The change in portfolio VaR from adding or removing a specific position entirely.

## Prerequisites

- [[Volatility]]
- [[Correlation]]
- [[Tail Risk]]

## Related concepts (learn next)

- [[Expected Shortfall]] because it answers the question VaR ignores: "How bad is it when VaR is breached?" The natural complement.
- [[Maximum Drawdown]] because it captures the peak to trough loss that VaR's single day framing misses.
- [[Tail Risk]] because VaR's biggest weakness is its blindness to tail severity.
- [[Correlation]] because portfolio VaR depends critically on correlation assumptions, and correlations spike during crises.
- [[Margin]] because exchange margin requirements are essentially VaR based calculations (SPAN, CME's system, uses VaR logic).
- [[Hedging]] because VaR decomposition tells you which positions contribute most to risk, guiding hedging priorities.

## Common misconceptions

**"VaR is the worst case loss."** VaR is emphatically NOT the worst case. It is the best case of the worst scenarios. A 99% VaR tells you the loss at the 99th percentile boundary. The 1% beyond that boundary has no ceiling. VaR says "you will lose at most X 99% of the time." It says nothing about the other 1%.

**"Lower VaR means a safer portfolio."** A portfolio of short OTM options can have very low VaR (small, frequent gains, rare large losses) while being catastrophically exposed to tail events. VaR rewards strategies that collect pennies in front of steamrollers.

**"Parametric VaR works for commodities."** Commodity returns are fat tailed and often positively skewed. Parametric VaR (which assumes normality) systematically understates risk. Use historical or Monte Carlo VaR for commodity portfolios, or at minimum adjust the parametric estimate with a fat tail multiplier.

**"VaR is additive across desks."** Due to diversification effects (imperfect correlations), the VaR of a combined portfolio is less than the sum of individual VaRs. This can create a false sense of security: each desk may be within limits, but the aggregate portfolio's tail risk may be concentrated in a single macro scenario that hits all desks simultaneously.

## Sources

- Jorion, Philippe. *Value at Risk: The New Benchmark for Managing Financial Risk*, 3rd ed. (2006).
- Hull, John. *Risk Management and Financial Institutions*, 5th ed. (2018).
- JP Morgan. *RiskMetrics Technical Document*, 4th ed.
- Danielsson, Jon. *Financial Risk Forecasting* (2011).
- Basel Committee on Banking Supervision. *Minimum capital requirements for market risk* (FRTB framework).
