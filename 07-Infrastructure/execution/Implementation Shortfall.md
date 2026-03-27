---
aliases: [implementation shortfall, IS, execution cost, slippage cost, Perold shortfall]
tags:
  - "#execution"
  - "#quant"
date-added: "2026-03-27"
---

# Implementation Shortfall

## Definition
Implementation shortfall (IS) is the difference between the theoretical return of a portfolio decision and the actual return after execution. It was introduced by Andre Perold in 1988 as a comprehensive measure of execution cost. IS captures everything that erodes trading profits: [[Market Impact]] from your own orders moving the price, timing cost from the market drifting while you execute, [[Bid-Ask Spread]] crossing cost, commission and fees, and opportunity cost from shares you never managed to execute. The decision price (also called arrival price) is the market price at the moment the trading decision was made, and IS is measured as the gap between this price and the average execution price. IS is expressed in basis points or as a dollar cost.

## Why it matters (commodities and FX)
For a commodity fund executing a 10,000 lot Brent crude position, IS is the ultimate measure of whether the execution desk did its job. A strategy might generate 50 basis points of alpha per trade, but if IS consumes 30 basis points, only 20 basis points reach the P&L. For systematic FX strategies trading EUR/USD, IS determines the minimum signal strength required for a trade to be profitable after costs. A strategy with 5 basis point expected return and 6 basis points of IS is net negative. Understanding and minimizing IS is the bridge between a theoretically profitable strategy and an actually profitable one.

## Concrete example
A macro fund decides at 09:00 London to buy 3,000 lots of LME copper futures (25 tonnes per lot). The decision price (mid) at 09:00 is $9,200 per tonne.

The execution desk uses a [[POV]] algorithm at 8% participation to buy over 4 hours.

**Execution log:**

| Time | Lots filled | Avg fill price |
|------|------------|---------------|
| 09:00 to 10:00 | 600 | $9,205 |
| 10:00 to 11:00 | 900 | $9,218 |
| 11:00 to 12:00 | 800 | $9,230 |
| 12:00 to 13:00 | 500 | $9,240 |
| **Total** | **2,800** | **$9,222.50** |

200 lots were not filled (opportunity cost). The close price is $9,250.

**IS decomposition:**

1. **Execution cost (filled portion):**
$$\text{Avg fill} - \text{Decision price} = 9{,}222.50 - 9{,}200 = \$22.50 \text{ per tonne}$$
$$\text{Dollar cost} = 22.50 \times 2{,}800 \times 25 = \$1{,}575{,}000$$

2. **Opportunity cost (unfilled portion):**
$$\text{Close} - \text{Decision price} = 9{,}250 - 9{,}200 = \$50 \text{ per tonne}$$
$$\text{Dollar cost} = 50 \times 200 \times 25 = \$250{,}000$$

3. **Total IS:** $1,575,000 + $250,000 = $1,825,000

4. **IS in basis points:**
$$\text{IS (bps)} = \frac{9{,}222.50 - 9{,}200}{9{,}200} \times 10{,}000 = 24.5 \text{ bps (execution only)}$$

**Win scenario:** The desk compares this against a [[TWAP]] backtest which would have cost 35 basis points. The [[POV]] algorithm saved 10.5 basis points ($700,000) by concentrating fills during the liquid morning session.

**Fail scenario:** The desk delayed execution by 30 minutes due to a system issue. Copper rallied $15 in that window. The timing cost alone was $15 x 3,000 x 25 = $1,125,000. IS jumped from 24.5 bps to 40+ bps.

## Key mechanics and formulas
**Total implementation shortfall (Perold decomposition):**
$$IS = \underbrace{(\bar{P}_{exec} - P_{decision}) \times Q_{filled}}_{\text{execution cost}} + \underbrace{(P_{close} - P_{decision}) \times Q_{unfilled}}_{\text{opportunity cost}}$$

**IS in basis points:**
$$IS_{bps} = \frac{\bar{P}_{exec} - P_{decision}}{P_{decision}} \times 10{,}000$$

**Decomposition into components:**
$$IS = \underbrace{\frac{s}{2}}_{\text{spread cost}} + \underbrace{\text{impact}(\sigma, Q, V)}_{\text{market impact}} + \underbrace{\alpha \times T_{exec}}_{\text{timing/drift cost}} + \underbrace{\text{fees}}_{\text{commission}}$$

Where $s$ is the [[Bid-Ask Spread]], $\sigma$ is volatility, $Q$ is order size, $V$ is volume, $\alpha$ is the drift rate, and $T_{exec}$ is execution duration.

**Almgren Chriss optimal execution (IS minimization):**
$$\min_{x(t)} E[\text{IS}] + \lambda \times \text{Var}[\text{IS}]$$

Where $x(t)$ is the trading trajectory, $\lambda$ is the risk aversion parameter. Higher $\lambda$ trades faster (reducing timing risk) at the cost of higher [[Market Impact]].

## Prerequisites
- [[Market Impact]]
- [[Slippage]]
- [[Bid-Ask Spread]]
- [[VWAP]]
- [[Arrival Price]]

## Related concepts (learn next)
- [[TCA]] uses IS as a primary metric for evaluating execution quality across trades and brokers.
- [[Market Impact]] is the largest component of IS for large orders in less liquid commodity markets.
- [[POV]] and [[VWAP]] are algorithms designed to minimize IS by spreading execution over time.
- [[Smart Order Routing]] reduces IS by finding the best prices across fragmented venues.
- [[Almgren Chriss Model]] provides the theoretical framework for IS minimizing execution trajectories.
- [[Slippage]] is the informal term for the execution cost component of IS.
- [[Arrival Price]] is the decision price benchmark most commonly used to compute IS.
- [[Opportunity Cost]] captures the cost of unexecuted shares, often overlooked but critical for large orders.

## Common misconceptions
1. **"IS is just slippage."** [[Slippage]] is only the execution cost component. IS also includes opportunity cost (unfilled quantity), timing cost, and commissions. A trade that executes at a great price but leaves 20% unfilled may have higher IS than one that fills completely at a slightly worse price.
2. **"Lower IS always means better execution."** IS depends on market conditions. Executing during a trending market will always have higher IS than executing during a mean reverting market. [[TCA]] must adjust for market conditions to be meaningful.
3. **"IS is only relevant for large orders."** Even a 1 lot retail trade has IS: the half spread cost plus commission. The difference is that market impact is negligible for small orders, so IS is dominated by fixed costs.
4. **"Minimizing IS means trading as slowly as possible."** Trading slowly reduces [[Market Impact]] but increases timing risk (the market may drift away). The optimal speed balances impact cost against timing cost, as captured by the [[Almgren Chriss Model]].

## Sources
- Perold, Andre, "The Implementation Shortfall: Paper vs. Reality," Journal of Portfolio Management, 1988
- Almgren, Robert and Chriss, Neil, "Optimal Execution of Portfolio Transactions," 2000
- "Algorithmic Trading and DMA" by Barry Johnson
- "Optimal Trading Strategies" by Robert Kissell
