---
aliases: [IOC, immediate or cancel, immediate-or-cancel]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# IOC

## Definition
Immediate or Cancel (IOC) tells the [[Matching Engine]] to fill as much of the order as possible at the current best available price(s) and immediately cancel any remainder. Unlike a standard [[limit order]] that rests on the [[Central Limit Order Book]] waiting, an IOC never enters the book. It executes instantly (in full or in part) or the unfilled portion is discarded. IOC is the default aggressor order type on many [[ECN]] platforms and exchange venues. Widely used by algorithmic traders who want to take available [[liquidity]] without revealing their total order size.

## Why it matters (commodities and FX)
In FX, IOC orders are the standard way to interact with [[ECN]] liquidity on [[EBS]] and [[Reuters Matching]]. A trader who needs to buy EUR/USD but does not want to signal demand sends a series of small IOC orders rather than posting a large [[limit order]]. In commodity futures on [[CME Globex]], IOC sweeps available depth at or better than a specified price without leaving a resting order detectable by other algos. IOC behavior matters for [[transaction cost analysis]] because IOC fills reveal instantaneous liquidity, and partial fills show how thin the book actually is behind [[Top of Book]].

## Concrete example

**Concrete:** Copper trader sells 50 lots of LME copper futures (25 tonnes each). CLOB: 20 lots bid at $8,950, 15 lots bid at $8,948. IOC sell for 50 at limit $8,948. Matching engine fills 20 at $8,950 and 15 at $8,948 (35 total). Remaining 15 cancelled immediately. Average fill: ($8,950 × 20 + $8,948 × 15) / 35 = $8,949.14, 0.86 below the [[Top of Book]] bid from sweeping levels. If the book had been deeper (30 at $8,950, 25 at $8,948), full 50 fills at average $8,949.20. Failure mirror: on a thin book only 5 lots fill, 10% fill rate forces re entry and price risk.

**Simplified:** An IOC order takes what is available right now at your price or better, and throws away whatever did not fill. It never sits in the order book. Used when you want to consume visible liquidity without leaving a resting order that other algorithms can see and react to. Partial fills are normal and tell you the book was thinner than you thought.

## Key mechanics and formulas
- **Fill rate**: filled / total ordered. Below 100% means the book was thinner than expected.
- **Effective spread**: 2 × |fill price − [[mid price]] at submission|. IOC typically shows wider effective spread than passive [[limit order]]s because it consumes liquidity.
- **Partial fill cost**: trader must decide whether to re enter, adding [[opportunity cost]] if price moves away.
- **Price protection**: most venues allow a limit price on IOC, preventing "running the book" in a flash crash.

## Prerequisites
- [[Limit Order]]
- [[Central Limit Order Book]]
- [[Matching Engine]]
- [[Liquidity]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[FOK]]: stricter cousin; entire order must fill or nothing.
- [[Sweep]]: aggressive order walking through multiple levels.
- [[Iceberg Order]]: hides total size by revealing only a small portion.
- [[Market Impact]]: IOC orders that sweep create immediate visible impact.
- [[Arrival Price]]: mid at submission, used to measure execution quality.
- [[Slippage]]: especially relevant for large IOC orders on thin books.
- [[Top of Book]]: IOC interacts first with the best available price.

## Common misconceptions

**"IOC is the same as a market order."** Market orders have no price limit and fill at any price. IOC can include a limit, protecting from catastrophic fills during volatile moments. Always use a limit on IOC.

**"Partial fills on IOC mean the market is broken."** Partials are normal and expected. Available liquidity at acceptable prices was less than order size. Useful information about [[Depth of Book]].

**"IOC orders leave no trace."** They do not rest on the book, but the resulting trades print on the tape. Sophisticated participants infer IOC activity from trades without corresponding book changes.

## Sources
- CME Group, "Order Types and Functionality" reference guide
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003), Chapter 4
- BIS, "Electronic Trading in Fixed Income Markets" (2016)
