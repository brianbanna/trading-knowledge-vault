---
aliases: [CLOB, central limit order book, order book, limit order book, LOB]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Central Limit Order Book

## Definition
A Central Limit Order Book (CLOB) is a transparent, centralized system where all buy and sell orders for an instrument are aggregated, displayed, and matched by price time priority. The best bid (highest buy) and best offer (lowest sell) sit at the [[Top of Book]]. Incoming orders match against resting orders from the best price down. Two orders at the same price match in submission order. Exchanges like [[CME]], [[LME]], and ICE run CLOBs for futures and options. In FX, [[EBS]] and [[Reuters Matching]] operate CLOBs for interbank spot, but the broader FX market trades bilaterally on [[Single Dealer Platform]]s and [[Multi Dealer Platform]]s rather than a single consolidated CLOB.

## Why it matters (commodities and FX)
The CLOB is the foundation of exchange [[price discovery]]. The Brent futures price quoted comes from the CLOB on ICE. A bank quoting EUR/USD to a corporate client references the [[EBS]] CLOB. CLOB mechanics are essential for reading [[Depth of Book]] data, designing execution algos, and interpreting price moves. Commodity traders use the CLOB to see exactly how much liquidity exists at each price level, enabling strategies that post passive orders inside the [[bid-ask spread]] to earn spread while managing [[inventory risk]]. The absence of a consolidated FX CLOB (liquidity fragmented across dozens of venues) creates arb opportunities and complicates [[transaction cost analysis]].

## Concrete example

**Concrete:** Trader buys 100 lots of CME WTI futures (CL). CLOB: best offer $78.50 (45 lots), $78.51 (80 lots), $78.52 (120 lots). Best bid $78.48 (60 lots). [[Mid price]] $78.49. Trader posts limit buy at $78.49, becoming new best bid. A seller arrives, hits the bid, fills 30 lots at $78.49. Trader saved $0.01 per barrel vs lifting the offer, $300 on 30,000 barrels. Failure mirror: market drops; sellers hit the bid aggressively, filling all 100 lots at $78.49 just as price falls to $78.30. Long at $78.49 in a falling market, losing $19,000. This is [[adverse selection]]: the passive order filled precisely because informed sellers saw the move coming.

**Simplified:** The order book is just a list of every buy and sell order at every price for an instrument, sorted by price. Buyers stack from the highest price down, sellers from the lowest price up. When you send a buy order at the market, it matches against the cheapest sellers first, then the next cheapest, and so on. Whoever puts their order in first at a given price gets filled first. The visible book shows you what liquidity exists, but during a fast move that liquidity vanishes in milliseconds.

## Key mechanics and formulas
- **Price time priority**: First by price (best first), then by time (earliest within same price).
- **Bid ask spread**: Spread = best offer − best bid. On liquid contracts like CL or ES, typically 1 tick.
- **Depth**: Total quantity across all levels on one side. Depth = sum of all resting orders on that side.
- **Queue position**: Resting order's position in queue determines fill probability. Queue position = lots ahead at same price.
- **Estimated fill probability**: roughly proportional to (volume traded at price) / (lots ahead + order size). Simplified but directionally correct.
- **Market vs limit**: Market orders cross the spread and take liquidity. Limit orders add liquidity.

## Prerequisites
- [[Bid-Ask Spread]]
- [[Limit Order]]
- [[Matching Engine]]
- [[Price Discovery]]

## Related concepts (learn next)
- [[Top of Book]]: best bid and offer, most competitive prices.
- [[Depth of Book]]: full CLOB beyond top level.
- [[Matching Engine]]: implements price time priority and matching.
- [[ECN]]: in FX, ECNs operate CLOBs for interbank spot.
- [[Dark Pool]]: alternative where orders are hidden.
- [[Market Impact]]: visible orders signal intent and move prices.
- [[Adverse Selection]]: passive orders risk being picked off.
- [[Iceberg Order]]: posts large orders while hiding total size.

## Common misconceptions

**"The CLOB shows all available liquidity."** Visible is a fraction. Hidden orders, [[Iceberg Order]]s, and off book negotiation (block trades, EFPs) mean real liquidity exceeds what the CLOB displays. In FX, the [[EBS]] CLOB is a small share of total EUR/USD volume.

**"A deep order book means liquid."** Resting orders cancel in milliseconds. During volatility events visible depth evaporates as makers pull quotes. Depth at 10:00 AM may not exist at 10:00:01 AM.

**"FX has a CLOB like equities."** FX has no consolidated CLOB. Liquidity fragments across [[EBS]], [[Reuters Matching]], dozens of [[ECN]]s, [[Multi Dealer Platform]]s, and [[Single Dealer Platform]]s.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003), Chapters 3 and 4
- CME Group, "Market Data and Order Book" documentation
- Gould, Porter, Williams, McDonald, Fenn, Howison, "Limit Order Books," Quantitative Finance (2013)
- Bouchaud, Farmer, Lillo, "How Markets Slowly Digest Changes in Supply and Demand" (2009)
