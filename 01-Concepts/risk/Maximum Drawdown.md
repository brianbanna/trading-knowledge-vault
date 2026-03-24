---
aliases: [maximum drawdown, max drawdown, MDD, drawdown, peak to trough loss]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-03-24"
---

# Maximum Drawdown

## Definition

Maximum drawdown (MDD) is the largest peak to trough decline in portfolio value before a new peak is reached. It answers the simplest, most visceral risk question: "What was the worst losing streak?" If your portfolio went from $10 million to $6 million before eventually recovering, your maximum drawdown was 40%. Unlike [[Value at Risk]] (which measures single period risk) or [[Expected Shortfall]] (which averages tail losses), drawdown captures the cumulative, multi day pain of a sustained losing period. It is the risk metric that most closely maps to how traders experience losses psychologically, because drawdowns happen over time, eroding confidence and capital simultaneously.

## Why it matters (commodities and FX)

Drawdown is the metric that determines survival. A 50% drawdown requires a 100% gain to recover. A 75% drawdown requires a 300% gain. The math is brutally asymmetric, and it is why professional traders and allocators focus on drawdown control as much as return generation.

In commodities, drawdowns tend to be deeper and faster than in equities because of leverage. A 5 lot [[Brent Crude]] position at 10:1 effective leverage turns a 10% adverse move into a 100% loss of margin. Commodity [[Carry Trade]] strategies (harvesting backwardation, selling contango) often show attractive Sharpe ratios but suffer devastating drawdowns when regimes shift (e.g., a supply glut flipping a market from backwardation to contango). The 2014 to 2016 oil crash produced 70%+ drawdowns in energy focused commodity funds.

In FX, carry trades (long high yielding EM, short low yielding G10) are notorious for drawdowns during [[Carry Unwind]] events. The October 1998 JPY carry unwind, the 2008 global carry crash, and the 2020 COVID EM sell off all produced 20 to 40% drawdowns in carry strategies within weeks.

## Concrete example

A commodity systematic fund starts the year at $50 million NAV. Monthly P&L:

| Month | P&L | NAV | Drawdown from Peak |
|-------|-----|-----|--------------------|
| Jan | +$2M | $52M | 0% |
| Feb | +$1M | $53M (new peak) | 0% |
| Mar | -$4M | $49M | -7.5% |
| Apr | -$3M | $46M | -13.2% |
| May | -$5M | $41M | -22.6% |
| Jun | +$2M | $43M | -18.9% |
| Jul | +$4M | $47M | -11.3% |
| Aug | +$3M | $50M | -5.7% |
| Sep | +$4M | $54M (new peak) | 0% |

**Maximum drawdown:** 22.6% (peak of $53M in Feb to trough of $41M in May).
**Drawdown duration:** 7 months (Feb to Sep, when the previous peak was exceeded).
**Recovery time:** 4 months (May trough to Sep new peak).

If the fund had a drawdown limit of 20%, the risk manager would have forced position reductions in May, potentially locking in losses and preventing the recovery. This is the drawdown control dilemma: cutting risk during a drawdown protects capital but also reduces recovery potential.

## Key mechanics and formulas

### Drawdown Calculation

**Drawdown at time t:**
`DD(t) = (Peak(t) - Value(t)) / Peak(t)`

Where Peak(t) = maximum portfolio value from inception to time t.

**Maximum Drawdown:**
`MDD = max[DD(t)] for all t`

### Drawdown Recovery Math

| Drawdown | Return Needed to Recover |
|----------|--------------------------|
| 10% | 11.1% |
| 20% | 25.0% |
| 30% | 42.9% |
| 40% | 66.7% |
| 50% | 100.0% |
| 75% | 300.0% |

This asymmetry is why drawdown control matters more than return maximization for long term compounding.

### Drawdown Based Metrics

**Calmar Ratio = Annualized Return / Maximum Drawdown**

A Calmar above 1.0 is good. Above 2.0 is excellent. Below 0.5 suggests the strategy's drawdowns are too deep relative to returns.

**Sterling Ratio = Annualized Return / (Average of N worst drawdowns + 10%)**

More stable than Calmar because it averages multiple drawdowns.

**Ulcer Index = sqrt(mean of squared drawdowns)**

Measures the "pain" of drawdowns, penalizing both depth and duration.

### Drawdown Duration

**Time to recovery** = the number of periods from the start of a drawdown until a new peak is reached.

Average drawdown duration is often more informative than maximum drawdown depth. A 15% drawdown lasting 18 months is psychologically harder (and often more capital destructive due to redemptions) than a 25% drawdown lasting 3 months.

### Expected Maximum Drawdown

For a strategy with Sharpe ratio S and N periods:
`E[MDD] ~ sigma x sqrt(N) x f(S)`

Higher Sharpe ratios produce shallower expected drawdowns. Longer time horizons produce deeper expected drawdowns. This is why even good strategies will eventually experience drawdowns that look catastrophic.

## Prerequisites

- [[Volatility]]
- [[Value at Risk]]
- [[Tail Risk]]

## Related concepts (learn next)

- [[Value at Risk]] because VaR measures single period risk while drawdown measures cumulative risk. A strategy can have low VaR but deep drawdowns if losses are serially correlated.
- [[Expected Shortfall]] because ES captures tail severity within a single period while drawdown captures tail severity across multiple periods.
- [[Carry Unwind]] because carry strategy drawdowns are the classic example of "picking up pennies in front of a steamroller," small steady gains punctuated by devastating drawdowns.
- [[Structural Break]] because the deepest drawdowns typically occur during regime changes that invalidate historical models.
- [[Convexity]] because convex strategies (trend following, long options) tend to have shallower drawdowns than concave strategies (carry, mean reversion).
- [[Correlation]] because drawdowns deepen when position correlations spike toward 1, as they do during crises.

## Common misconceptions

**"Maximum drawdown is predictive."** Past maximum drawdown is NOT a ceiling on future drawdowns. It is a single observation from one historical path. The next drawdown could easily be deeper. A strategy that has never drawn down more than 15% is not "safe," it may simply not have encountered its worst case scenario yet.

**"Drawdown limits protect you."** Fixed drawdown limits (e.g., "cut all positions at 20% drawdown") protect capital but guarantee you sell at the worst point. They lock in losses and miss recoveries. Better approaches include gradual risk reduction (reducing position sizes proportionally as drawdown deepens) and volatility targeting (reducing when vol spikes, regardless of drawdown level).

**"Sharpe ratio is more important than drawdown."** A strategy with a 2.0 Sharpe ratio and a 60% maximum drawdown is not investable for most allocators, because the drawdown would trigger redemptions and forced deleveraging long before the Sharpe manifests over the full cycle. Drawdown is the binding constraint for survival.

**"Drawdown is just about money."** Drawdowns destroy decision making. Behavioral research shows that traders in drawdown take more risk (trying to recover), cut winners early (fear of giving back gains), and deviate from their process. The psychological damage of a drawdown often exceeds the financial damage.

## Sources

- Magdon-Ismail, Malik and Atiya, Amir. "Maximum Drawdown," *Risk Magazine* (2004).
- Ilmanen, Antti. *Expected Returns* (2011), chapters on risk metrics and portfolio construction.
- Lo, Andrew. "The Statistics of Sharpe Ratios," *Financial Analysts Journal* (2002).
- Chekhlov, Uryasev, and Zabarankin. "Drawdown Measure in Portfolio Optimization," *International Journal of Theoretical and Applied Finance* (2005).
