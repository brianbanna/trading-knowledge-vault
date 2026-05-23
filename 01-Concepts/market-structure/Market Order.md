---
aliases: [market order, at market, market buy, market sell]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Market Order

## Definition
A market order tells the venue to execute immediately at the best available price. You are guaranteed a [[Fill]], not a price. A market buy for 10 lots of WTI with 5 lots at 80.00 and 5 lots at 80.05 fills at an average of 80.025. Market orders prioritize speed over price. They are the fastest way in or out of a [[Position]], essential when you must exit now.

## Concrete example

**Concrete:** Breaking news: OPEC emergency meeting. You want long Brent immediately. Send a market buy for 20 lots. The spread is 82.48/82.50. You fill at 82.50 (ask). Brent rallies to 85.00 within the hour. The 2 tick cost of crossing is trivial vs the 250 tick gain. Failure case: long 50 lots of natural gas, exit via market sell during a thin session. The bid side stacks 10 at 3.40, 15 at 3.38, 25 at 3.35. Your 50 lots sweep all 3 levels, average fill 3.37. Expected 3.40, [[Slippage]] cost 0.03 per unit. On 50 lots × 10,000 MMBtu × 0.03 = 15,000 USD to [[Market Impact]].

**Simplified:** Tell the venue "get me out now, any price." Guaranteed fill. The cost is whatever the book shows: best price for the first units, worse for the rest if your order eats through depth. Use when speed matters more than price.

## Why it matters (commodities and FX)
Market orders are the default for urgent execution. In FX, where [[Liquidity]] is deep in major [[Currency Pair]]s, market orders for 1 to 5M EUR/USD or USD/JPY clip through with minimal [[Slippage]]. In commodities, especially far dated agriculture or off peak power, a market order moves price visibly. The market vs [[Limit Order]] choice is one of the most frequent decisions a trader makes: certainty of execution or certainty of price.

## Key mechanics and formulas
- Market order execution price = best available price(s) in the order book
- [[Slippage]] = Expected price minus Actual [[Fill]] price
- [[Market Impact]] = price change caused by your order consuming [[Liquidity]]
- Effective cost = [[Slippage]] + Commission
- For large orders: Average fill = Sum(price_i × quantity_i) / Total quantity
- Rule of thumb: cost rises with order size relative to available [[Liquidity]]

## Prerequisites
- [[Position]]
- [[Bid-Ask Spread]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Limit Order]], the alternative guaranteeing price not execution
- [[Stop Loss]], which often converts to a market order on trigger
- [[Fill]], the execution confirmation
- [[Slippage]], the cost in fast or thin markets
- [[Market Impact]], the broader price effect of large market orders
- [[Liquidity]], which determines slippage magnitude
- [[Order Book]], the queue your market order consumes

## Common misconceptions
- **Market orders are not "at the last price."** Last trade was 80.00 but current best offer is 80.10: your market buy fills at 80.10 or worse.
- **Market orders in illiquid markets are dangerous.** Lumber, cocoa, exotic [[EM Currencies]]: the book can be so thin a market order moves price several percent.
- **Open and close are different from intraday.** Many exchanges run opening/closing auctions with different mechanics. A market on close order participates in the auction, not continuous book.

## Sources
- Harris, L. *Trading and Exchanges*, Chapters 4 and 6
- CME Group, "Order Types and Execution"
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
