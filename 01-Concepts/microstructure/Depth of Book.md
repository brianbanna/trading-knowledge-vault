---
aliases: [depth of book, market depth, order book depth]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Depth of Book

## Definition
Depth of book refers to the total volume of resting orders at each price level in an [[order book]], extending beyond the [[Top of Book]] (best bid and offer). A "deep" book has large volumes available across many price levels, meaning a large order can be executed with minimal price impact. A "thin" or "shallow" book has small volumes, meaning even moderate orders will [[sweep]] through multiple levels and push the price significantly. Depth of book data (also called Level 2 or Level 3 data) provides a complete snapshot of pending buy and sell interest at every price increment. In FX, depth of book on [[ECN]]s like [[EBS]] typically extends 5 to 10 pips beyond the best bid and offer, though the vast majority of resting liquidity is concentrated within 2 to 3 pips. Depth is not static; it fluctuates continuously as participants add and cancel orders, especially during volatile periods when depth can evaporate in milliseconds.

## Why it matters (commodities and FX)
Depth of book is the primary input for estimating [[market impact]] of large orders. A commodity producer hedging 500 million USD of FX exposure needs to know not just the top-of-book price but how much the price will move as the order consumes liquidity at successively worse levels. In commodity futures, depth of book on the CME for [[WTI]] crude or [[gold]] futures determines whether a hedge of 1,000 contracts can be executed in a single sweep or must be broken into smaller child orders over time. Systematic traders use real-time depth data to dynamically adjust execution algorithms: when the book is deep, they trade more aggressively; when it thins, they slow down. Depth of book also serves as an early warning signal for [[volatility]] events. A sudden drop in resting depth often precedes sharp price moves, as market makers withdraw liquidity in anticipation of news or uncertainty.

## Concrete example
At 15:00 UTC on [[EBS]], the EURUSD order book shows: bid side has 10 million at 1.08520, 15 million at 1.08515, 20 million at 1.08510, and 30 million at 1.08505. The ask side has 8 million at 1.08525, 12 million at 1.08530, 18 million at 1.08535, and 25 million at 1.08540. Total visible depth within 2 pips is 45 million bid, 38 million ask. A hedge fund sends a market sell order for 60 million. It fills 10 million at 1.08520, 15 million at 1.08515, 20 million at 1.08510, and 15 million at 1.08505. The volume-weighted average execution price is 1.08512, which is 1.3 pips below the mid-price of 1.085225. If the book had been twice as deep (double the size at each level), the same order would have averaged 1.08517, only 0.55 pips from mid. Now consider the same 60 million sell at 05:00 UTC during the thin Sydney session: depth within 2 pips is only 12 million total, and the order sweeps 8 pips, averaging 1.08480 (4.25 pips of slippage).

## Key mechanics and formulas
- **Depth at level i**: D(i) = volume available at the i-th best price level
- **Cumulative depth**: CD(n) = sum of D(i) for i = 1 to n; total volume available within n price levels
- **Weighted mid-price**: WMid = (best ask x bid size + best bid x ask size) / (bid size + ask size); adjusts mid-price for depth asymmetry
- **Market impact estimate (linear)**: Impact (pips) = order size / (cumulative depth within expected sweep range)
- **Depth imbalance**: DI = (cumulative bid depth - cumulative ask depth) / (cumulative bid depth + cumulative ask depth); positive = more buying support, negative = more selling support
- **Depth half-life**: time for depleted depth to regenerate after a sweep; typically 1 to 10 seconds in liquid FX pairs

## Prerequisites
- [[Top of Book]]
- [[Order Book]]
- [[Bid-Ask Spread]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Top of Book]]: the first level of depth; necessary but insufficient for understanding execution cost.
- [[Sweep]]: the act of consuming depth across multiple price levels in a single aggressive order.
- [[Skew Microstructure]]: depth asymmetry between bid and ask sides predicts short-term price direction.
- [[Market Impact]]: depth of book is the primary determinant of how much an order moves the price.
- [[Tick Data]]: full depth-of-book updates at tick frequency provide the richest microstructure dataset.
- [[Internalization]]: high internalization by banks means visible ECN depth understates true available liquidity.
- [[FX Market Hours]]: depth varies dramatically by session, with London/NY overlap offering the deepest books.
- [[Aggregated Data]]: compressing depth snapshots into summary metrics for medium-frequency use.

## Common misconceptions
1. **"Visible depth equals actual liquidity"**: Much of the true FX liquidity sits on [[Single Dealer Platform]]s and is not visible in the public [[ECN]] order book. Visible depth on EBS might be 50 million, but actual available liquidity (including SDP internalization) could be 10x that.
2. **"Depth is stable during stress"**: Depth can vanish in seconds during volatile events (e.g., flash crashes, surprise central bank decisions). The 2015 CHF de-peg saw EBS depth in EURCHF drop from 50+ million to effectively 0 in under 1 second.
3. **"More price levels always mean more depth"**: An order book with 20 levels showing 1 million each (20 million total) is shallower than one with 5 levels showing 10 million each (50 million total). Concentration of depth near the top of book matters more than the number of levels.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners," Oxford University Press (2003)
- Gould, Martin D. et al., "Limit Order Books," Quantitative Finance (2013)
- Cont, Rama, Stoikov, Sasha, Talreja, Rishi, "A Stochastic Model for Order Book Dynamics," Operations Research (2010)
