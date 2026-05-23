---
aliases: [implementation shortfall, IS, execution cost, slippage cost, Perold shortfall]
tags:
  - "#execution"
  - "#quant"
date-added: "2026-03-27"
---

# Implementation Shortfall

## Definition
Implementation shortfall (IS) is the difference between the theoretical return of a portfolio decision and the actual return after execution. Introduced by Andre Perold in 1988. IS captures everything that erodes trading profits: [[Market Impact]] from your own orders moving the price, timing cost from market drift during execution, [[Bid-Ask Spread]] crossing cost, commission and fees, and opportunity cost from shares never executed. The decision price (arrival price) is the market price at the moment the decision was made. IS is the gap between this price and the average execution price. Reported in basis points or dollars.

## Why it matters (commodities and FX)
For a commodity fund executing a 10,000 lot Brent position, IS is the final word on whether the execution desk did its job. A strategy generating 50 bps alpha per trade gives up 20 bps to P&L if IS eats 30 bps. For systematic FX on EUR/USD, IS sets the minimum signal strength for profitable trades. A strategy with 5 bps expected return and 6 bps IS is net negative. Minimizing IS is the bridge between a theoretically profitable strategy and an actually profitable one.

## Concrete example
**Concrete:** A macro fund decides at 09:00 London to buy 3,000 lots of LME copper futures (25 tonnes per lot). Decision price (mid): $9,200/tonne. The desk runs a [[POV]] algo at 8% participation over 4 hours.

| Time | Lots filled | Avg fill |
|------|------------|----------|
| 09:00 to 10:00 | 600 | $9,205 |
| 10:00 to 11:00 | 900 | $9,218 |
| 11:00 to 12:00 | 800 | $9,230 |
| 12:00 to 13:00 | 500 | $9,240 |
| **Total** | **2,800** | **$9,222.50** |

200 lots unfilled. Close: $9,250. Execution cost: $22.50 x 2,800 x 25 = $1,575,000. Opportunity cost: $50 x 200 x 25 = $250,000. Total IS: $1,825,000 (24.5 bps execution only). Versus a [[TWAP]] backtest at 35 bps, POV saved 10.5 bps ($700,000) by concentrating in the liquid morning.

**Simplified:** Decide to buy at $9,200. Average fill ends up $9,222. Lose another $50/tonne on the part you never filled. The total gap between paper and reality is implementation shortfall. Every component of cost (spread, impact, drift, fees, unfilled quantity) shows up in IS.

## Key mechanics and formulas
**Total implementation shortfall (Perold decomposition):**
$$IS = \underbrace{(\bar{P}_{exec} - P_{decision}) \times Q_{filled}}_{\text{execution cost}} + \underbrace{(P_{close} - P_{decision}) \times Q_{unfilled}}_{\text{opportunity cost}}$$

**IS in basis points:**
$$IS_{bps} = \frac{\bar{P}_{exec} - P_{decision}}{P_{decision}} \times 10{,}000$$

**Decomposition into components:**
$$IS = \underbrace{\frac{s}{2}}_{\text{spread cost}} + \underbrace{\text{impact}(\sigma, Q, V)}_{\text{market impact}} + \underbrace{\alpha \times T_{exec}}_{\text{timing/drift cost}} + \underbrace{\text{fees}}_{\text{commission}}$$

Where $s$ is the [[Bid-Ask Spread]], $\sigma$ is volatility, $Q$ is order size, $V$ is volume, $\alpha$ is drift rate, $T_{exec}$ is execution duration.

**Almgren Chriss optimal execution (IS minimization):**
$$\min_{x(t)} E[\text{IS}] + \lambda \times \text{Var}[\text{IS}]$$

Where $x(t)$ is the trading trajectory, $\lambda$ is risk aversion. Higher $\lambda$ trades faster (less timing risk) at higher [[Market Impact]].

## Prerequisites
- [[Market Impact]]
- [[Slippage]]
- [[Bid-Ask Spread]]
- [[VWAP]]
- [[Arrival Price]]

## Related concepts (learn next)
- [[TCA]] uses IS as the primary metric for evaluating execution quality.
- [[Market Impact]] is the largest IS component for large orders in less liquid commodity markets.
- [[POV]] and [[VWAP]] are algorithms designed to minimize IS by spreading execution over time.
- [[Smart Order Routing]] reduces IS by finding best prices across fragmented venues.
- [[Almgren Chriss Model]] provides the theoretical framework for IS minimizing trajectories.
- [[Slippage]] is the informal term for the execution cost component of IS.
- [[Arrival Price]] is the decision price benchmark most commonly used for IS.
- [[Opportunity Cost]] captures unexecuted shares, often overlooked but critical for large orders.

## Common misconceptions
1. **"IS is just slippage."** [[Slippage]] is only the execution cost component. IS also includes opportunity cost (unfilled quantity), timing cost, and commissions. A trade with great fill prices but 20% unfilled may have higher IS than one filling fully at slightly worse prices.
2. **"Lower IS always means better execution."** IS depends on market conditions. Executing into a trending market always shows higher IS than a mean reverting one. [[TCA]] must adjust for conditions to be meaningful.
3. **"IS only matters for large orders."** Even a 1 lot retail trade has IS: half spread plus commission. Difference is that market impact is negligible for small orders, so IS is dominated by fixed costs.
4. **"Minimizing IS means trading as slowly as possible."** Slow trading reduces [[Market Impact]] but raises timing risk. Optimum balances impact against timing, per the [[Almgren Chriss Model]].

## Sources
- Perold, Andre, "The Implementation Shortfall: Paper vs. Reality," Journal of Portfolio Management, 1988
- Almgren, Robert and Chriss, Neil, "Optimal Execution of Portfolio Transactions," 2000
- "Algorithmic Trading and DMA" by Barry Johnson
- "Optimal Trading Strategies" by Robert Kissell
