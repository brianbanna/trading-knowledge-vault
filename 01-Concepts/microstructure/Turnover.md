---
aliases: [turnover, position turnover, inventory turnover, trading frequency]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Turnover

## Definition
Turnover measures how frequently I flatten and re establish positions. A market maker with high turnover holds inventory briefly, buying and selling quickly to capture the [[Bid-Ask Spread]] without taking directional risk. Turnover can be expressed as the ratio of total traded volume to average position size, or simply as the number of [[Round Trip|round trips]] per unit time. High turnover means I am cycling through positions rapidly, earning many small spread captures but paying many [[Round Trip]] costs. Low turnover means I hold positions longer, relying on directional moves rather than spread capture. The optimal turnover depends on the strategy, the instrument's [[Liquidity]], and transaction costs.

## Why it matters (commodities and FX)
In FX market making, turnover is extremely high. A EUR/USD dealer might turn over $5 billion in notional per day against a maximum inventory of $50 million, implying a turnover ratio of 100x per day. The dealer holds each position for seconds to minutes. In commodity futures, a scalper on Brent crude might turn over 500 lots per day against a maximum position of 20 lots (25x turnover). Understanding turnover is critical because it directly determines how much spread cost a strategy incurs. A quantitative strategy that turns over 50x per day in a 1 pip spread instrument pays 50 pips per day in friction, approximately 12,600 pips per year. The alpha must exceed this hurdle.

## Concrete example
I run 2 strategies on Brent crude futures (contract = 1000 barrels).

**Strategy A (high turnover scalper):** I trade 200 round trips per day, average 5 lots per trade. The spread is $0.04 per barrel. Daily spread cost: 200 x 5 x 1000 x $0.04 = $40,000. My average profit per round trip is $0.07 per barrel. Daily gross profit: 200 x 5 x 1000 x $0.07 = $70,000. Net after spread cost: $30,000/day. Turnover ratio: (200 x 5) / 10 average position = 100x/day.

**Strategy B (low turnover swing trader):** I trade 2 round trips per day, average 50 lots per trade. Daily spread cost: 2 x 50 x 1000 x $0.04 = $4,000. My average profit per round trip is $0.80 per barrel (larger moves). Daily gross profit: 2 x 50 x 1000 x $0.80 = $80,000. Net after spread cost: $76,000/day. Turnover ratio: (2 x 50) / 50 average position = 2x/day.

**Fail scenario for Strategy A:** The spread widens to $0.08 during a volatile period. Daily spread cost doubles to $80,000. But my alpha per trade stays at $0.07 (the signal does not improve with volatility). I am now losing $10,000/day. High turnover amplifies any increase in transaction costs. Strategy B barely notices: its spread cost goes from $4,000 to $8,000, a rounding error against $80,000 gross.

## Key mechanics and formulas
- **Turnover ratio** = Total volume traded / Average position size (over a given period)
- **Turnover in round trips** = Number of complete buy and sell cycles per day
- **Total spread cost** = Turnover x [[Round Trip]] cost per trade = Turnover x [[Bid-Ask Spread]] x Size
- **Holding period** = 1 / Turnover (approximate). If turnover is 100x/day, average holding period is approximately 1/100 of a trading day, or about 5 minutes
- **Break even alpha per trade** = [[Round Trip]] cost / 2. Each trade must generate at least the [[Half Spread]] in alpha
- **Sharpe ratio impact:** For a given alpha and volatility, higher turnover increases the Sharpe ratio (more independent bets), but only if the alpha per trade exceeds transaction costs

## Prerequisites
- [[Round Trip]]
- [[Bid-Ask Spread]]
- [[Half Spread]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Round Trip]] , the cost incurred per turnover cycle
- [[Half Spread]] , the single side cost that makes turnover expensive
- [[Slippage]] , an additional cost that scales with turnover, especially for large orders
- [[Market Impact]] , high turnover strategies that trade large size face compounding impact costs
- [[Inventory Risk]] , high turnover reduces inventory risk by holding positions briefly
- [[Capacity]] , the maximum capital a strategy can deploy before turnover costs exceed alpha
- [[Bid-Ask Spread]] , the primary friction that determines whether high turnover is viable

## Common misconceptions
1. **"High turnover means high risk."** The opposite is often true. A high turnover market maker holds positions for seconds, so the risk per position is small. A low turnover swing trader holds positions for days, with much larger drawdown potential. Turnover and risk are not synonymous.
2. **"Turnover does not matter if I use limit orders."** Limit orders avoid crossing the spread on entry, but they introduce adverse selection risk and non fill risk. The effective cost of a limit order strategy is not zero; it includes the opportunity cost of missed fills and the adverse selection on fills that do execute. The [[Markout]] on limit fills is often negative.
3. **"I should minimize turnover to minimize costs."** Minimizing turnover reduces spread costs but may also reduce alpha capture. If my signal decays in 5 minutes, I need to turn over within 5 minutes or lose the edge. The optimal turnover maximizes net alpha (gross alpha minus transaction costs), not gross or cost alone.
4. **"Turnover is constant."** In practice, turnover varies with market conditions. During high volatility (oil price crashes, FX interventions), a market maker's turnover may double because more counterparties are trading. This increases both revenue (more spread capture) and risk (more adverse selection). Models should account for regime dependent turnover.

## Sources
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- CME Group, "Market Making and Liquidity Provision"
- Kissell, R. *The Science of Algorithmic Trading and Portfolio Management*, Academic Press
