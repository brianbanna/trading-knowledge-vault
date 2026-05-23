---
aliases: [top of book, best bid offer, BBO]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Top of Book

## Definition
Top of book is the best (highest) bid and the best (lowest) ask currently available in an [[order book]]. Together they form the Best Bid and Offer (BBO), the tightest price at which a trade can immediately execute. The gap between best ask and best bid is the [[bid-ask spread]], the most basic [[liquidity]] cost. Top of book is what most traders see on screens and what most execution algorithms reference as the starting point. But top of book only tells you the price for the first unit of liquidity; it says nothing about volume available or what happens when an order is larger. For that you need [[depth of book]]. Top of book data updates thousands of times per second in liquid markets and is the most widely distributed market data.

## Why it matters (commodities and FX)
In FX, top of book on [[EBS]] for [[EURUSD]] might show 0.1 pip spread, but available size is only 1 to 5M. A fund trading 200M cannot rely on top of book. In commodity futures, top of book on [[WTI]] crude might show 1 tick spread with 50 contracts (50,000 bbl), but a physical hedger needing 500 contracts will move through multiple levels. Top of book is the benchmark for [[transaction cost analysis]] because the mid (average of best bid and ask) is the standard reference for measuring [[slippage]] and [[market impact]]. For systematic strategies, changes in top of book spread and size are real time liquidity indicators usable as execution timing signals.

## Concrete example

**Concrete:** 14:00 UTC, EBS USDJPY: best bid 149.520 (10M), best offer 149.525 (8M). Top of book spread 0.5 pips, mid 149.5225. Trader sends market buy 5M. Fills entirely at 149.525, paying 0.275 pips from mid. After fill, best offer updates to 149.525 with 3M remaining. Second trader sends market buy 20M: first 3M fills at 149.525, next 10M at 149.530, last 7M at 149.535. VWAP 149.5304, 0.79 pips from mid. The second trader's execution was far worse than top of book suggested because the order exceeded available depth and had to [[sweep]] deeper.

**Simplified:** Top of book is the best buy and best sell prices right now. It is what the screen shows. Useful for small orders that fit within available size. Useless for size, because the moment you need more than what is sitting there, you walk through worse prices.

## Key mechanics and formulas
- **Bid ask spread**: Spread = best ask - best bid
- **Mid price**: Mid = (best bid + best ask) / 2
- **Spread in bps**: (spread / mid) x 10,000
- **Top of book depth**: total volume at best bid and best ask
- **Execution probability at top**: for orders <= top size, ~100% fill at BBO; falls fast for larger
- **Quote to trade ratio**: top of book updates relative to trades; in FX, 10:1 to 100:1 is common, meaning most quotes update before being traded against

## Prerequisites
- [[Bid-Ask Spread]]
- [[Order Book]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Depth of Book]]: the full picture beyond BBO
- [[Sweep]]: what happens when an order exhausts top liquidity and trades at worse prices
- [[Skew Microstructure]]: asymmetry between top bid size and top ask size predicts direction
- [[Tick Data]]: every change to top is recorded in tick level data
- [[ECN]]: venue where top of book is most transparent
- [[Market Impact]]: impact estimation starts with top of book conditions
- [[VWAP]]: execution algos compare achieved price vs mid from top of book

## Common misconceptions
1. **"Top of book spread is your execution cost"**: only for very small orders fitting within available BBO size. Anything larger has wider effective spread because the order consumes liquidity beyond top.
2. **"Tight top of book means liquid"**: 0.1 pip spread with 1M is less liquid in practice than 0.5 pip spread with 100M. Spread alone is insufficient; size matters equally.
3. **"Top of book is always real, executable liquidity"**: in some markets, top is phantom liquidity pulled before it can be traded. High quote to trade ratios indicate this.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners," Oxford University Press (2003)
- Cartea, Alvaro et al., "Algorithmic and High-Frequency Trading," Cambridge University Press (2015)
- O'Hara, Maureen, "Market Microstructure Theory," Blackwell Publishers (1995)
