---
aliases: [IOC, immediate or cancel, immediate-or-cancel]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# IOC

## Definition
Immediate or Cancel (IOC) is an order instruction that tells the [[Matching Engine]] to fill as much of the order as possible at the current best available price(s) and immediately cancel any remaining unfilled quantity. Unlike a standard [[limit order]] that rests on the [[Central Limit Order Book]] waiting for a counterparty, an IOC order never enters the book. It either executes instantly (in full or in part) or the unfilled portion is discarded. IOC is the default aggressor order type on many [[ECN]] platforms and exchange venues. It is widely used by algorithmic traders who want to take available [[liquidity]] without revealing their total order size to the market.

## Why it matters (commodities and FX)
In FX, IOC orders are the standard way to interact with [[ECN]] liquidity on [[EBS]] and [[Reuters Matching]]. A trader who needs to buy EUR/USD but does not want to signal demand to the market will send a series of small IOC orders rather than posting a large [[limit order]]. In commodities futures on [[CME Globex]], IOC is used when a trader wants to sweep available depth at or better than a specified price without leaving a resting order that could be detected by other algorithms. Understanding IOC behavior is critical for [[transaction cost analysis]] because IOC fills reflect available instantaneous liquidity, and partial fills reveal how thin the book really is behind the [[Top of Book]].

## Concrete example
A copper trader wants to sell 50 lots of LME copper futures (each lot = 25 tonnes). The current [[Central Limit Order Book]] shows 20 lots bid at $8,950 and another 15 lots bid at $8,948. The trader sends an IOC sell order for 50 lots at a limit of $8,948. The [[Matching Engine]] fills 20 lots at $8,950, then 15 lots at $8,948, for a total fill of 35 lots. The remaining 15 lots are cancelled immediately because no more bids exist at $8,948 or above. The trader's average fill price is ($8,950 x 20 + $8,948 x 15) / 35 = $8,949.14, which is 0.86 below the [[Top of Book]] bid due to the [[slippage]] from sweeping through levels.

If the book had been deeper, say 30 lots at $8,950 and 25 lots at $8,948, the full 50 lots would have filled at an average of $8,949.20. The fail scenario: on a thin book, only 5 lots are available and the trader gets a 10% fill rate, forcing them to re-enter the market and risk prices moving against them.

## Key mechanics and formulas
- **Fill rate**: Fill rate = filled quantity / total order quantity. A fill rate below 100% on IOC tells you the book was thinner than expected.
- **Effective spread**: Effective spread = 2 x |fill price - [[mid price]] at order submission|. IOC orders typically show wider effective spreads than passive [[limit order]]s because they consume liquidity.
- **Partial fill cost**: When an IOC partially fills, the trader must decide whether to re-enter, which adds [[opportunity cost]] if the price moves away.
- **Price protection**: Most venues allow a limit price on IOC orders, meaning the order will not fill worse than the specified price. This prevents "running the book" in a flash crash scenario.

## Prerequisites
- [[Limit Order]]
- [[Central Limit Order Book]]
- [[Matching Engine]]
- [[Liquidity]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[FOK]]: the stricter cousin of IOC, where the entire order must fill or nothing does.
- [[Sweep]]: an aggressive order that walks through multiple price levels, similar to how IOC can partially fill across levels.
- [[Iceberg Order]]: a strategy to hide total size by revealing only a small portion, often paired with IOC logic on the hidden portion.
- [[Market Impact]]: IOC orders that sweep the book create immediate and visible market impact.
- [[Arrival Price]]: the mid price at the moment the IOC order is submitted, used as the benchmark to measure execution quality.
- [[Slippage]]: the difference between expected fill price and actual fill price, especially relevant for large IOC orders on thin books.
- [[Top of Book]]: IOC orders interact first with the best available price at the top of the order book.

## Common misconceptions
1. **"IOC is the same as a market order"**: A market order has no price limit and will fill at any price. An IOC order can include a limit price, protecting the trader from catastrophic fills during volatile moments. Always use a limit price on IOC orders.
2. **"Partial fills on IOC mean the market is broken"**: Partial fills are the normal and expected outcome. They simply mean available liquidity at acceptable prices was less than the order size. This is useful information about [[Depth of Book]].
3. **"IOC orders leave no trace"**: While IOC orders do not rest on the book, the resulting trades are still reported on the tape. Sophisticated participants can infer IOC activity from trade prints without corresponding book changes.

## Sources
- CME Group, "Order Types and Functionality" reference guide
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003), Chapter 4
- BIS, "Electronic Trading in Fixed Income Markets" (2016)
