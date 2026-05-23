---
aliases: [maximum drawdown, max drawdown, MDD, drawdown, peak to trough loss]
tags:
  - "#risk"
  - "#quant"
date-added: "2026-03-24"
---

# Maximum Drawdown

## Definition

Maximum drawdown (MDD) is the largest peak to trough decline in portfolio value before a new peak is reached. It answers the simplest, most visceral risk question: "What was the worst losing streak?" A portfolio that went from $10M to $6M before recovering had a 40% MDD. Unlike [[Value at Risk]] (single period) or [[Expected Shortfall]] (averaged tail losses), drawdown captures cumulative, multi day pain over a sustained losing period. It maps closest to how traders experience losses psychologically — drawdowns happen over time, eroding confidence and capital simultaneously.

## Why it matters (commodities and FX)

Drawdown determines survival. A 50% drawdown requires a 100% gain to recover. A 75% drawdown requires a 300% gain. The math is asymmetric, and professional traders and allocators focus on drawdown control as much as return generation.

In commodities, drawdowns are deeper and faster than equities because of leverage. A 5 lot [[Brent Crude]] position at 10:1 effective leverage turns a 10% adverse move into a 100% margin loss. Commodity [[Carry Trade]] strategies (harvesting backwardation, selling contango) show attractive Sharpe but devastating drawdowns when regimes shift (a supply glut flipping backwardation to contango). The 2014 to 2016 oil crash produced 70%+ drawdowns in energy commodity funds.

In FX, carry trades (long high yielding EM, short low yielding G10) are notorious for drawdowns during [[Carry Unwind]] events. The October 1998 JPY unwind, the 2008 global carry crash, and the 2020 COVID EM sell off all produced 20 to 40% drawdowns within weeks.

## Concrete example

**Concrete:** A commodity systematic fund starts the year at $50M NAV.

| Month | P&L | NAV | Drawdown from Peak |
|-------|-----|-----|--------------------|
| Jan | +$2M | $52M | 0% |
| Feb | +$1M | $53M (peak) | 0% |
| Mar | −$4M | $49M | −7.5% |
| Apr | −$3M | $46M | −13.2% |
| May | −$5M | $41M | −22.6% |
| Jun | +$2M | $43M | −18.9% |
| Jul | +$4M | $47M | −11.3% |
| Aug | +$3M | $50M | −5.7% |
| Sep | +$4M | $54M (new peak) | 0% |

**MDD:** 22.6% ($53M Feb peak to $41M May trough). **Duration:** 7 months. **Recovery:** 4 months. If the fund had a 20% drawdown limit, the risk manager would have forced position cuts in May, locking in losses and preventing the recovery. The drawdown control dilemma: cutting risk during a drawdown protects capital but reduces recovery potential.

**Simplified:** Drawdown is the gap between your last high water mark and your current value. Maximum drawdown is the worst such gap in the entire history. It matters because losses compound asymmetrically: the deeper the hole, the harder it is to climb out. A 50% loss needs a 100% gain just to break even. Allocators and risk managers cap drawdown because past a threshold, redemptions and forced de-risking ensure you cannot recover even if your strategy still works.

## Key mechanics and formulas

### Drawdown Calculation

**Drawdown at time t:**
`DD(t) = (Peak(t) − Value(t)) / Peak(t)`

Peak(t) = max portfolio value from inception to t.

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

The asymmetry is why drawdown control matters more than return maximization for long term compounding.

### Drawdown Based Metrics

**Calmar Ratio = Annualized Return / Maximum Drawdown**
Above 1.0 is good. Above 2.0 is excellent. Below 0.5 means drawdowns are too deep relative to returns.

**Sterling Ratio = Annualized Return / (Average of N worst drawdowns + 10%)**
More stable than Calmar.

**Ulcer Index = sqrt(mean of squared drawdowns)**
Penalizes both depth and duration.

### Drawdown Duration

**Time to recovery:** periods from drawdown start to a new peak. Average duration is often more informative than max depth. A 15% drawdown lasting 18 months is psychologically harder (and more capital destructive via redemptions) than a 25% drawdown lasting 3 months.

### Expected Maximum Drawdown

For a strategy with Sharpe S and N periods:
`E[MDD] ≈ sigma × sqrt(N) × f(S)`

Higher Sharpe gives shallower expected drawdowns. Longer horizons give deeper expected drawdowns. Even good strategies eventually show catastrophic looking drawdowns.

## Prerequisites

- [[Volatility]]
- [[Value at Risk]]
- [[Tail Risk]]

## Related concepts (learn next)

- [[Value at Risk]] because VaR measures single period risk while drawdown measures cumulative risk. A strategy can have low VaR but deep drawdowns if losses are serially correlated.
- [[Expected Shortfall]] because ES captures tail severity within a period while drawdown captures it across periods.
- [[Carry Unwind]] because carry drawdowns are the classic "picking up pennies in front of a steamroller" — small steady gains punctuated by devastating losses.
- [[Structural Break]] because the deepest drawdowns occur during regime changes that invalidate historical models.
- [[Convexity]] because convex strategies (trend, long options) have shallower drawdowns than concave strategies (carry, mean reversion).
- [[Correlation]] because drawdowns deepen when position correlations spike toward 1, as they do in crises.

## Common misconceptions

**"Maximum drawdown is predictive."** Past MDD is not a ceiling on future drawdowns. It is a single observation from one historical path. A strategy that never drew down more than 15% is not safe; it may simply not have hit its worst case yet.

**"Drawdown limits protect you."** Fixed limits (e.g., cut all positions at 20%) protect capital but guarantee selling at the worst point. They lock in losses and miss recoveries. Better: gradual risk reduction proportional to drawdown depth, or vol targeting (cut when vol spikes regardless of drawdown).

**"Sharpe is more important than drawdown."** A 2.0 Sharpe with 60% MDD is not investable for most allocators because the drawdown triggers redemptions and forced deleveraging long before the Sharpe manifests. Drawdown is the binding survival constraint.

**"Drawdown is just about money."** Drawdowns destroy decision making. Traders in drawdown take more risk (trying to recover), cut winners early (fear of giving back), and deviate from process. The psychological damage often exceeds the financial.

## Sources

- Magdon-Ismail, Malik and Atiya, Amir. "Maximum Drawdown," *Risk Magazine* (2004).
- Ilmanen, Antti. *Expected Returns* (2011), chapters on risk metrics and portfolio construction.
- Lo, Andrew. "The Statistics of Sharpe Ratios," *Financial Analysts Journal* (2002).
- Chekhlov, Uryasev, and Zabarankin. "Drawdown Measure in Portfolio Optimization," *International Journal of Theoretical and Applied Finance* (2005).
