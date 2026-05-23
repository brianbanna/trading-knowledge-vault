---
aliases: [depth of book, market depth, order book depth]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Depth of Book

## Definition
Depth of book is the total volume of resting orders at each price level in an [[order book]], beyond the [[Top of Book]]. A deep book has large volumes across many levels, so a large order executes with minimal price impact. A thin book has small volumes, so even moderate orders [[sweep]] through multiple levels and push price hard. Depth of book data (Level 2 or Level 3) provides a full snapshot of pending interest at every price increment. In FX, depth on [[ECN]]s like [[EBS]] extends 5 to 10 pips beyond top of book, though most resting liquidity sits within 2 to 3 pips. Depth fluctuates continuously as participants add and cancel, especially during volatility when depth evaporates in milliseconds.

## Why it matters (commodities and FX)
Depth is the primary input for estimating [[market impact]] on large orders. A commodity producer hedging $500M of FX exposure needs to know not just top of book price but how price moves as the order consumes liquidity at worse levels. In commodity futures, CME depth for [[WTI]] crude or [[gold]] determines whether a 1,000 contract hedge executes in a single sweep or must be sliced. Systematic traders use real time depth to adjust algos: deep book = trade aggressively, thinning book = slow down. Depth also warns of [[volatility]] events. A sudden drop in resting depth often precedes sharp moves as makers pull liquidity ahead of news.

## Concrete example

**Concrete:** 15:00 UTC on [[EBS]], EURUSD bids: 10M at 1.08520, 15M at 1.08515, 20M at 1.08510, 30M at 1.08505. Asks: 8M at 1.08525, 12M at 1.08530, 18M at 1.08535, 25M at 1.08540. Visible depth within 2 pips: 45M bid, 38M ask. Hedge fund sends market sell 60M. Fills: 10M at 1.08520, 15M at 1.08515, 20M at 1.08510, 15M at 1.08505. VWAP = 1.08512, 1.3 pips below mid 1.085225. With double depth, same order averages 1.08517, only 0.55 pips slip. Same 60M sell at 05:00 UTC thin Sydney: depth within 2 pips only 12M, order sweeps 8 pips, averaging 1.08480 (4.25 pips slip).

**Simplified:** Top of book shows the best price. Depth shows everything sitting underneath. A deep book has lots of orders stacked at many price levels, so big trades barely move price. A thin book has few orders, so even a moderate trade walks through several prices and gets a bad average. Depth depends on time of day, news, and stress.

## Key mechanics and formulas
- **Depth at level i**: D(i) = volume at the i-th best price level
- **Cumulative depth**: CD(n) = sum of D(i) for i = 1 to n
- **Weighted mid**: WMid = (best ask x bid size + best bid x ask size) / (bid size + ask size)
- **Market impact (linear)**: Impact (pips) = order size / cumulative depth within sweep range
- **Depth imbalance**: DI = (CD bid - CD ask) / (CD bid + CD ask); positive = more buying support
- **Depth half life**: time for depleted depth to regenerate after a sweep; 1 to 10s in liquid FX

## Prerequisites
- [[Top of Book]]
- [[Order Book]]
- [[Bid-Ask Spread]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Top of Book]]: the first level; necessary but insufficient for execution cost
- [[Sweep]]: consuming depth across multiple levels in a single aggressive order
- [[Skew Microstructure]]: depth asymmetry predicts short term direction
- [[Market Impact]]: depth is the primary determinant of how much an order moves price
- [[Tick Data]]: full depth updates at tick frequency, the richest microstructure dataset
- [[Internalization]]: high internalization by banks means visible ECN depth understates true liquidity
- [[FX Market Hours]]: depth varies by session, London/NY overlap is deepest
- [[Aggregated Data]]: compressing depth snapshots into summary metrics

## Common misconceptions
1. **"Visible depth equals actual liquidity"**: most FX liquidity sits on [[Single Dealer Platform]]s, invisible on the public ECN book. Visible 50M on EBS might be 10x larger including SDP internalization.
2. **"Depth is stable in stress"**: depth vanishes in seconds during stress. The 2015 CHF de-peg saw EBS EURCHF depth drop from 50M+ to effectively zero in under 1 second.
3. **"More price levels mean more depth"**: 20 levels at 1M each (20M total) is shallower than 5 levels at 10M each (50M total). Concentration near top of book matters more than level count.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners," Oxford University Press (2003)
- Gould, Martin D. et al., "Limit Order Books," Quantitative Finance (2013)
- Cont, Rama, Stoikov, Sasha, Talreja, Rishi, "A Stochastic Model for Order Book Dynamics," Operations Research (2010)
