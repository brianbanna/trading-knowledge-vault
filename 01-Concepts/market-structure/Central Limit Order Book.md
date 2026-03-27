---
aliases: [CLOB, central limit order book, order book, limit order book, LOB]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Central Limit Order Book

## Definition
A Central Limit Order Book (CLOB) is a transparent, centralized system where all buy and sell orders for a given instrument are aggregated, displayed, and matched according to price-time priority. The best bid (highest buy price) and best offer (lowest sell price) sit at the [[Top of Book]], and incoming orders are matched against resting orders starting from the best available price. If 2 orders are at the same price, the one submitted first has priority. Exchanges like [[CME]], [[LME]], and ICE use CLOBs for futures and options. In FX, [[EBS]] and [[Reuters Matching]] operate CLOBs for interbank spot trading, but the broader FX market largely operates through bilateral relationships on [[Single Dealer Platform]]s and [[Multi Dealer Platform]]s rather than a single consolidated CLOB.

## Why it matters (commodities and FX)
The CLOB is the foundation of [[price discovery]] on exchanges. When a trader looks at the Brent crude futures price, that price comes from the CLOB on ICE. When a bank quotes EUR/USD to a corporate client, the reference price comes from the CLOB on [[EBS]]. Understanding CLOB mechanics is essential for reading [[Depth of Book]] data, designing execution algorithms, and interpreting why prices move. For commodity traders, the CLOB reveals exactly how much liquidity exists at each price level, enabling strategies like placing passive orders just inside the [[bid-ask spread]] to earn the spread while managing [[inventory risk]]. The absence of a consolidated CLOB in FX (liquidity is fragmented across dozens of venues) creates arbitrage opportunities and complicates [[transaction cost analysis]].

## Concrete example
A trader wants to buy 100 lots of CME WTI crude oil futures (CL). The CLOB shows: best offer at $78.50 with 45 lots, next level at $78.51 with 80 lots, then $78.52 with 120 lots. Best bid at $78.48 with 60 lots. The [[mid price]] is ($78.50 + $78.48) / 2 = $78.49. The trader posts a limit buy at $78.49, which enters the CLOB as a new best bid. A seller arrives and hits the trader's bid, filling 30 lots at $78.49. The trader saved 1 tick ($0.01) per barrel versus lifting the offer, which on 30 lots x 1,000 barrels = $300.

The fail scenario: the trader posts the $78.49 bid, but the market drops suddenly. Sellers hit the bid aggressively, filling all 100 lots at $78.49 just as the price falls to $78.30. The trader is now long at $78.49 in a falling market, losing $0.19 per barrel x 100,000 barrels = $19,000. This is [[adverse selection]]: the trader's passive order was filled precisely because informed sellers saw the price was about to drop.

## Key mechanics and formulas
- **Price-time priority**: Orders are ranked first by price (best price first), then by time (earliest submission first within the same price level).
- **Bid-ask spread**: Spread = best offer - best bid. On liquid contracts like CL or ES, this is typically 1 tick.
- **Depth**: Total quantity available across all price levels on one side. Depth = sum of all resting buy (or sell) orders.
- **Queue position**: A resting order's position in the queue determines its probability of fill. Queue position = number of lots ahead at the same price level.
- **Estimated fill probability**: P(fill) roughly proportional to (total lots traded at price level) / (lots ahead in queue + order size). This is simplified but directionally correct.
- **Market order vs limit order**: A market order crosses the spread and takes liquidity from the CLOB. A limit order adds liquidity to the CLOB.

## Prerequisites
- [[Bid-Ask Spread]]
- [[Limit Order]]
- [[Matching Engine]]
- [[Price Discovery]]

## Related concepts (learn next)
- [[Top of Book]]: the best bid and best offer, which represent the most competitive prices in the CLOB.
- [[Depth of Book]]: the full CLOB beyond the top level, revealing available liquidity at each price.
- [[Matching Engine]]: the system that implements price-time priority and executes order matching within the CLOB.
- [[ECN]]: in FX, ECNs operate CLOBs for interbank spot trading.
- [[Dark Pool]]: the alternative model where orders are hidden rather than displayed on a CLOB.
- [[Market Impact]]: visible orders on the CLOB signal intent and can move prices before execution.
- [[Adverse Selection]]: passive orders on the CLOB face the risk of being picked off by better-informed traders.
- [[Iceberg Order]]: a way to post large orders on the CLOB while hiding the true size.

## Common misconceptions
1. **"The CLOB shows all available liquidity"**: The visible book is only a fraction of total liquidity. Hidden orders, [[Iceberg Order]]s, and off-book negotiation (block trades, EFPs) mean the real available liquidity is larger than what the CLOB displays. In FX, the CLOB on [[EBS]] represents a small share of total EUR/USD volume.
2. **"A deep order book means the market is liquid"**: Resting orders can be cancelled in milliseconds. During a volatility event, the visible depth evaporates as market makers pull their quotes. The depth you see at 10:00 AM may not exist at 10:00:01 AM.
3. **"FX has a CLOB like equities"**: FX has no consolidated CLOB. Liquidity is fragmented across [[EBS]], [[Reuters Matching]], dozens of [[ECN]]s, [[Multi Dealer Platform]]s, and [[Single Dealer Platform]]s. This fragmentation is a defining feature of FX market structure.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003), Chapters 3 and 4
- CME Group, "Market Data and Order Book" documentation
- Gould, Porter, Williams, McDonald, Fenn, Howison, "Limit Order Books," Quantitative Finance (2013)
- Bouchaud, Farmer, Lillo, "How Markets Slowly Digest Changes in Supply and Demand" (2009)
