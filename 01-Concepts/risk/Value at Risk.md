---
aliases: [VaR, value at risk, portfolio VaR, 1-day VaR, 99% VaR]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-03-24"
---

# Value at Risk

## Definition

Value at Risk (VaR) is a single number that answers: "What is the most I expect to lose over a given horizon, at a given confidence, under normal conditions?" A 1 day 99% VaR of $500,000 means on 99 out of 100 trading days, expected loss does not exceed $500,000. On the remaining day, the loss can be much larger. VaR is a fence around normal losses. It tells you the boundary but not how far you fall beyond it. That limitation is why [[Expected Shortfall]] was developed as a complement.

## Why it matters (commodities and FX)

VaR is the universal language of risk management. Banks, hedge funds, prop desks, and clearing houses use it to set position limits, calculate margin, and allocate capital. Any institutional commodity or FX role will have risk limits expressed as VaR.

In commodities, VaR is tricky because return distributions are far from normal. Crude, natural gas, and softs have fat tails and skewed distributions that parametric VaR systematically underestimates. Parametric VaR on a TTF natural gas position in 2021 would have understated risk dramatically — a move from EUR 20 to EUR 340/MWh is not in any normal distribution's vocabulary. Sophisticated commodity desks supplement parametric VaR with historical, Monte Carlo, and [[Expected Shortfall]].

In FX, VaR works better for G10 pairs (closer to normal) but breaks down for EM where gap risk (devaluations, capital controls) creates discontinuous losses.

## Concrete example

**Concrete:** A trader holds 200 lots long [[Brent Crude]] and 50 lots short [[WTI Crude Oil]]. Daily vol Brent 2.0%, WTI 2.2%, correlation 0.92. Brent notional $16.4M, WTI $3.9M short. Portfolio variance = (16.4M × 0.02)² + (3.9M × 0.022)² − 2 × 0.92 × (16.4M × 0.02) × (3.9M × 0.022). Daily vol ≈ $278,000. 1 day 99% VaR = 2.33 × $278,000 = $648,000. In March 2020, Brent fell 25% in a day; the actual portfolio loss would have been ~$3.5M, roughly 5.4x the VaR estimate. VaR set the fence at $648,000; reality cleared it by a factor of 5.

**Simplified:** VaR estimates a loss threshold you should not breach more than X% of the time. It depends on your assumed distribution, lookback window, and correlations. The number is useful for comparing risk across positions and meeting regulatory requirements. It is dangerous when treated as a worst case. The worst case is unbounded; VaR only describes the boundary of "normal."

### Freight book VaR

A freight book carries different risk factors from a flat price book: route rates ([[Baltic Route Codes]] such as C5 and P2A), vessel classes ([[Vessel Classes and Deadweight Tonnage]]), and the [[Forward Freight Agreement]] forward curve by maturity (front month, quarters, calendar years), plus a [[Bunkers, IFO versus MGO, and the Bunker Hedge|bunker]] leg and an FX leg when hire is earned in one currency while costs fall in another.

**Concrete:** An operator is long 10 Capesize C5 FFA lots for the coming quarter at 18,000 USD per day and short 6 Panamax P2A lots. Daily vol of the C5 rate is 4.5 percent, P2A 3.8 percent, correlation 0.7. Aggregating the two route legs gives a 1 day 95 percent VaR near 95,000 USD. Adding the bunker leg (hedged with gasoil futures) and a small EUR/USD leg lifts the diversified VaR to roughly 110,000 USD, less than the sum of the legs because freight, fuel, and FX are imperfectly correlated. The trap is the same as flat price VaR: if one load region such as Brazilian iron ore drives C5 and P2A together, realised correlation jumps toward 1 and the loss runs well past the estimate. Freight VaR must be run on the [[Forward Freight Agreement|FFA]] curve by maturity, not the front month alone, because a long front and short deferred book can show low flat VaR while carrying large curve risk.

## Key mechanics and formulas

### 3 Methods of Calculating VaR

**1. Parametric (Variance-Covariance) VaR**

Assumes normal returns.

`VaR = Position Value × z_alpha × sigma × sqrt(time)`

- z_alpha = z score for confidence (1.65 for 95%, 2.33 for 99%)
- sigma = daily vol (annual / sqrt(252))
- time = holding period in days

For a portfolio: `VaR = z_alpha × sqrt(w' × Sigma × w)` where w is position vector, Sigma covariance matrix.

**Pros:** Fast, easy to decompose into risk contributions.
**Cons:** Assumes normality. Underestimates tail risk in commodities.

**2. Historical VaR**

Uses actual historical returns. Sort past daily P&L worst to best. The 1st percentile is the 99% VaR. 1,000 days of history → 10th worst day = 99% VaR.

**Pros:** No distributional assumptions. Captures fat tails if they occurred in the window.
**Cons:** Assumes the future looks like the past. Sensitive to lookback length.

**3. Monte Carlo VaR**

Simulates thousands of scenarios using a chosen distribution (fat tailed, skewed, correlated). Compute P&L per scenario. 1st percentile = 99% VaR.

**Pros:** Flexible. Models non-normal, path dependent, option payoffs.
**Cons:** Computationally intensive. Only as good as the model.

### VaR Parameters

| Parameter | Common choices |
|-----------|---------------|
| Confidence level | 95% (trading desks), 99% (regulatory) |
| Time horizon | 1 day (trading), 10 days (Basel), 1 month (portfolio) |
| Lookback window | 250 days (1Y), 500 days (2Y), or full history |

### Scaling VaR

`VaR_T = VaR_1day × sqrt(T)`

Square root of time assumes iid returns. Serial correlation and vol clustering (common in commodities) make this unreliable beyond a few days.

### VaR Decomposition

**Marginal VaR:** change in VaR from adding $1 to a position. Used for optimization.
**Component VaR:** each position's contribution to total VaR. Sum = total VaR.
**Incremental VaR:** change in portfolio VaR from adding or removing a specific position entirely.

## Prerequisites

- [[Volatility]]
- [[Correlation]]
- [[Tail Risk]]

## Related concepts (learn next)

- [[Expected Shortfall]] answers what VaR ignores: "How bad is it when VaR breaches?" Natural complement.
- [[Maximum Drawdown]] captures peak to trough loss that VaR's single day framing misses.
- [[Tail Risk]] because VaR's biggest weakness is blindness to tail severity.
- [[Correlation]] because portfolio VaR depends critically on correlation assumptions, and correlations spike during crises.
- [[Margin]] because exchange margin (SPAN, CME) uses VaR logic.
- [[Hedging]] because VaR decomposition shows which positions contribute most to risk.

## Common misconceptions

**"VaR is the worst case."** VaR is not the worst case. It is the best case of the worst scenarios. A 99% VaR is the 99th percentile boundary. The 1% beyond has no ceiling. VaR says "you lose at most X 99% of the time." It says nothing about the other 1%.

**"Lower VaR means a safer portfolio."** A portfolio of short OTM options can have very low VaR (small frequent gains, rare huge losses) while being catastrophically exposed to tails. VaR rewards strategies that collect pennies in front of steamrollers.

**"Parametric VaR works for commodities."** Commodity returns are fat tailed and often positively skewed. Parametric VaR understates risk. Use historical or Monte Carlo, or adjust the parametric estimate with a fat tail multiplier.

**"VaR is additive across desks."** Diversification (imperfect correlations) makes combined VaR less than the sum of individual VaRs. Each desk within limits can hide aggregate tail risk concentrated in a single macro scenario hitting all desks at once.

## Sources

- Jorion, Philippe. *Value at Risk: The New Benchmark for Managing Financial Risk*, 3rd ed. (2006).
- Hull, John. *Risk Management and Financial Institutions*, 5th ed. (2018).
- JP Morgan. *RiskMetrics Technical Document*, 4th ed.
- Danielsson, Jon. *Financial Risk Forecasting* (2011).
- Basel Committee on Banking Supervision. *Minimum capital requirements for market risk* (FRTB framework).
