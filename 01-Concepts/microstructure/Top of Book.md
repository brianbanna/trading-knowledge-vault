---
aliases: [top of book, best bid offer, BBO]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Top of Book

## Definition
Top of book refers to the best (highest) bid price and the best (lowest) ask price currently available in an [[order book]] for a given instrument. Together, these form the Best Bid and Offer (BBO), which represents the tightest price at which a trade can be immediately executed. The difference between the best ask and best bid is the [[bid-ask spread]], the most basic measure of [[liquidity]] cost. Top-of-book prices are what most traders see on their screens and what most execution algorithms reference as the starting point for trading decisions. However, top-of-book only tells you the price for the first unit of liquidity; it says nothing about how much volume is available at that price or what happens when you need to execute a larger order. For that, you need [[depth of book]]. Top-of-book data updates thousands of times per second in liquid markets and is the most widely distributed form of market data.

## Why it matters (commodities and FX)
In FX, top-of-book on [[EBS]] for [[EURUSD]] might show a 0.1 pip spread, but the available size might be only 1 to 5 million. A fund needing to trade 200 million cannot rely on top-of-book prices. In commodity futures, top-of-book on [[WTI]] crude oil might show 1 tick (1 cent) spread with 50 contracts (50,000 barrels), but a physical hedger needing 500 contracts will move through multiple price levels. Top-of-book is the benchmark for [[transaction cost analysis]] because the mid-price (average of best bid and best ask) is the standard reference for measuring [[slippage]] and [[market impact]]. For systematic strategies, changes in top-of-book spread and size are real-time indicators of [[liquidity]] conditions and can be used as signals for execution timing.

## Concrete example
At 14:00 UTC, the [[EBS]] order book for USDJPY shows: best bid 149.520 (10 million), best offer 149.525 (8 million). The top-of-book spread is 0.5 pips, and the mid-price is 149.5225. A trader sends a market buy order for 5 million. The order fills entirely at 149.525 (the best offer), paying 0.275 pips of spread cost from mid. After the fill, the best offer updates to 149.525 with 3 million remaining. A second trader then sends a market buy for 20 million. The first 3 million fills at 149.525, the next 10 million at 149.530, and the last 7 million at 149.535. The volume-weighted average price is 149.5304, representing 0.79 pips of spread cost from mid. The second trader's execution was much worse than what top-of-book suggested because the order exceeded available top-of-book depth and had to [[sweep]] deeper levels.

## Key mechanics and formulas
- **Bid-ask spread**: Spread = best ask - best bid
- **Mid-price**: Mid = (best bid + best ask) / 2
- **Spread in basis points**: Spread (bps) = (spread / mid) x 10,000
- **Top-of-book depth**: the total volume available at the best bid and best ask prices
- **Execution probability at top**: for small orders (<= top-of-book size), probability of filling at BBO approaches 100%; for larger orders, it falls rapidly
- **Quote-to-trade ratio**: the number of top-of-book quote updates relative to actual trades; in FX, ratios of 10:1 to 100:1 are common, indicating that most quotes are updated before being traded against

## Prerequisites
- [[Bid-Ask Spread]]
- [[Order Book]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Depth of Book]]: the full picture of available liquidity beyond the best bid and offer.
- [[Sweep]]: what happens when an order exhausts top-of-book liquidity and trades at successively worse prices.
- [[Skew Microstructure]]: asymmetry between top-of-book bid size and ask size predicts short-term direction.
- [[Tick Data]]: every change to top-of-book is recorded in tick-level market data.
- [[ECN]]: the venue type where top-of-book is most transparent and representative.
- [[Market Impact]]: estimating impact starts with top-of-book conditions at the time of execution.
- [[VWAP]]: execution algorithms compare achieved price against mid derived from top-of-book.

## Common misconceptions
1. **"Top-of-book spread is your execution cost"**: This is only true for very small orders that fit within the available size at the BBO. For anything larger, the effective spread will be wider because the order must consume liquidity beyond top-of-book.
2. **"A tight top-of-book spread means the market is liquid"**: A 0.1 pip spread with 1 million available is less liquid (in practical terms) than a 0.5 pip spread with 100 million available. Spread alone is insufficient; size matters equally.
3. **"Top-of-book is always real, executable liquidity"**: In some markets, top-of-book quotes can be "phantom liquidity" that is pulled before it can be traded. High quote-to-trade ratios indicate this phenomenon.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners," Oxford University Press (2003)
- Cartea, Alvaro et al., "Algorithmic and High-Frequency Trading," Cambridge University Press (2015)
- O'Hara, Maureen, "Market Microstructure Theory," Blackwell Publishers (1995)
