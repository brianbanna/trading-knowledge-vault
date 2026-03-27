---
aliases: [market order, at market, market buy, market sell]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Market Order

## Definition
A market order tells the exchange or broker to execute immediately at the best available price. You are guaranteed a [[Fill]], but not guaranteed a price. If you submit a market buy for 10 lots of WTI crude and the order book has 5 lots at 80.00 and 5 lots at 80.05, you get filled on both levels, paying an average of 80.025. Market orders prioritize speed over price. They are the fastest way to enter or exit a [[Position]], and they are essential when you need to get out immediately.

## Concrete example
**Win scenario:** Breaking news: an OPEC emergency meeting is called. You want to go [[Long]] Brent crude immediately. You send a market buy for 20 lots. The [[Bid-Ask Spread]] is 82.48/82.50. You get filled at 82.50 (the ask). Brent rallies to 85.00 within the hour. Your speed of execution captured the move, and the 2 tick cost of the market order is trivial relative to the 250 tick gain.

**Fail scenario:** You are [[Long]] 50 lots of natural gas and want to exit during a volatile session. You send a market sell. The bid side of the order book is thin: 10 lots at 3.40, 15 lots at 3.38, 25 lots at 3.35. Your 50 lots sweep through all 3 levels, getting an average [[Fill]] of 3.37. You expected to sell around 3.40 but [[Slippage]] cost you 0.03 per unit. On 50 lots of 10,000 MMBtu each, that is 50 x 10,000 x 0.03 = 15,000 USD lost to [[Market Impact]].

## Why it matters (commodities and FX)
Market orders are the default tool for urgent execution. In FX, where [[Liquidity]] is deep for major [[Currency Pair]]s, market orders on EUR/USD or USD/JPY in 1 to 5 million clips typically execute with minimal [[Slippage]]. But in commodities, especially illiquid contracts like far dated agriculture futures or off peak power, a market order can move the price significantly. The choice between a market order and a [[Limit Order]] is one of the most frequent decisions a trader makes, and it comes down to: do I need certainty of execution or certainty of price?

## Key mechanics and formulas
- Market order execution price = best available price(s) in the order book
- [[Slippage]] = Expected price minus Actual [[Fill]] price
- [[Market Impact]] = Price change caused by your order consuming [[Liquidity]]
- Effective cost = [[Slippage]] + Commission
- For large orders: Average fill price = Sum(price_i x quantity_i) / Total quantity
  - Where price_i and quantity_i are the price and size at each level consumed
- Rule of thumb: market order cost increases with order size relative to available [[Liquidity]]

## Prerequisites
- [[Position]]
- [[Bid-Ask Spread]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Limit Order]] , the alternative that guarantees price but not execution
- [[Stop Loss]] , which often converts into a market order when triggered
- [[Fill]] , the confirmation that your market order has executed
- [[Slippage]] , the cost of market orders in fast or thin markets
- [[Market Impact]] , the broader price effect of executing large market orders
- [[Liquidity]] , which determines how much slippage a market order will experience
- [[Order Book]] , the queue of resting orders that market orders consume

## Common misconceptions
- **Market orders are not always "at the last price."** The last traded price might have been 80.00, but if the current best offer is 80.10, your market buy will fill at 80.10 or worse.
- **Market orders in illiquid markets are extremely dangerous.** In commodities like lumber, cocoa, or exotic [[EM Currencies]], the order book can be so thin that a market order moves the price by several percent.
- **Market orders at the open or close are different from intraday.** Many exchanges have opening and closing auctions with different mechanics than continuous trading. A "market on close" order participates in the closing auction, not the continuous book.

## Sources
- Harris, L. *Trading and Exchanges*, Chapters 4 and 6
- CME Group, "Order Types and Execution"
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
