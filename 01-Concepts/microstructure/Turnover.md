---
aliases: [turnover, position turnover, inventory turnover, trading frequency]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Turnover

## Definition
Turnover measures how frequently positions are flattened and re established. A high turnover market maker holds inventory briefly, buying and selling quickly to capture the [[Bid-Ask Spread]] without taking directional risk. Turnover can be expressed as total traded volume / average position size, or as the number of [[Round Trip|round trips]] per unit time. High turnover means cycling through positions rapidly, earning many small spread captures while paying many [[Round Trip]] costs. Low turnover means holding longer, relying on directional moves rather than spread capture. Optimal turnover depends on strategy, instrument [[Liquidity]], and transaction costs.

## Why it matters (commodities and FX)
In FX market making, turnover is extremely high. A EUR/USD dealer might turn over $5B notional per day against a max inventory of $50M, implying 100x daily turnover ratio. Each position held seconds to minutes. In commodity futures, a Brent scalper might turn over 500 lots per day against a max position of 20 lots (25x). Turnover directly determines how much spread cost a strategy incurs. A strategy turning over 50x/day in a 1 pip spread instrument pays 50 pips/day in friction, ~12,600 pips/year. Alpha must exceed this hurdle.

## Concrete example

**Concrete:** 2 strategies on Brent crude (1000 bbl/contract). Strategy A (high turnover scalper): 200 round trips/day, 5 lots average. Spread $0.04/bbl. Daily spread cost: 200 x 5 x 1000 x $0.04 = $40,000. Profit per RT $0.07/bbl. Daily gross: 200 x 5 x 1000 x $0.07 = $70,000. Net $30,000/day. Turnover (200 x 5) / 10 avg position = 100x/day. Strategy B (low turnover swing): 2 RT/day, 50 lots avg. Daily spread cost: 2 x 50 x 1000 x $0.04 = $4,000. Profit per RT $0.80/bbl. Daily gross $80,000. Net $76,000/day. Turnover (2 x 50) / 50 = 2x/day. Strategy A failure: spread widens to $0.08 in a volatile period. Daily spread cost doubles to $80,000. Alpha per trade stays $0.07 (signal does not improve with vol). Now losing $10,000/day. High turnover amplifies any cost increase. Strategy B barely notices: $4,000 to $8,000, rounding error vs $80,000 gross.

**Simplified:** Turnover is how fast positions cycle through the book. High turnover earns the spread many times but pays the spread many times too. Low turnover holds longer, depends on bigger price moves. The right level depends on how quickly your edge decays and how expensive the round trip is.

## Key mechanics and formulas
- **Turnover ratio** = total volume traded / average position size (over a period)
- **Turnover in round trips** = number of complete buy and sell cycles per day
- **Total spread cost** = Turnover x [[Round Trip]] cost = Turnover x [[Bid-Ask Spread]] x Size
- **Holding period** = 1 / Turnover (approximate). 100x/day ≈ 5 minute average hold
- **Break even alpha per trade** = [[Round Trip]] cost / 2. Each trade must generate at least [[Half Spread]] in alpha
- **Sharpe impact:** for given alpha and vol, higher turnover raises Sharpe (more independent bets), but only if alpha per trade exceeds transaction costs

## Prerequisites
- [[Round Trip]]
- [[Bid-Ask Spread]]
- [[Half Spread]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Round Trip]] , the cost per turnover cycle
- [[Half Spread]] , the single side cost making turnover expensive
- [[Slippage]] , additional cost scaling with turnover, especially for large orders
- [[Market Impact]] , high turnover at large size compounds impact
- [[Inventory Risk]] , high turnover cuts inventory risk by holding briefly
- [[Capacity]] , maximum capital deployable before turnover costs exceed alpha
- [[Bid-Ask Spread]] , the primary friction determining if high turnover is viable

## Common misconceptions
1. **"High turnover means high risk."** Often the opposite. A high turnover maker holds positions seconds, risk per position is small. A low turnover swing trader holds days with larger drawdown potential. Turnover and risk are not synonyms.
2. **"Turnover does not matter if I use limit orders."** Limit orders avoid crossing the spread on entry but introduce adverse selection and non fill risk. Effective cost is not zero: opportunity cost of missed fills and AS on fills that execute. [[Markout]] on limit fills is often negative.
3. **"I should minimize turnover to minimize costs."** Cutting turnover cuts spread cost but also alpha capture. If signal decays in 5 minutes, turn over within 5 minutes or lose the edge. Optimal turnover maximizes net alpha, not gross or cost alone.
4. **"Turnover is constant."** Turnover varies with conditions. In high vol (oil crashes, FX interventions), a maker's turnover can double because more counterparties trade. Raises both revenue and risk. Models should account for regime dependence.

## Sources
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- CME Group, "Market Making and Liquidity Provision"
- Kissell, R. *The Science of Algorithmic Trading and Portfolio Management*, Academic Press
