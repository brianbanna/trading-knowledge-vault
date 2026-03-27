---
aliases: [FOK, fill or kill, fill-or-kill, all or nothing]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# FOK

## Definition
Fill or Kill (FOK) is an order instruction that requires the entire order quantity to be filled immediately in a single execution, or the entire order is cancelled. Unlike [[IOC]], which accepts partial fills and cancels only the remainder, FOK is all or nothing. If the [[Central Limit Order Book]] does not have enough liquidity at the specified price (or better) to fill the full size in one shot, the order is rejected entirely. FOK is used when partial execution would leave the trader in a worse position than no execution at all, for example when hedging a specific notional amount or executing one leg of a [[spread]] trade where a partial fill would create unwanted directional risk.

## Why it matters (commodities and FX)
In commodities, FOK is essential for [[spread]] trades. If a trader wants to buy 100 lots of Brent December and sell 100 lots of Brent January as a [[calendar spread]], a partial fill on one leg creates naked exposure. FOK ensures both sides are either fully executed or not at all. In FX, FOK is used on [[Multi Dealer Platform]]s where a client requests a firm price from multiple banks for a specific amount. The bank quotes a price good for the full amount, and the client either fills the whole clip or walks away. FOK is also the standard order type for [[block trade]]s on exchanges, where the minimum size threshold must be met in full.

## Concrete example
A trader needs to buy exactly 200 lots of ICE Brent crude futures at $82.50 or better to hedge a physical cargo. The [[Central Limit Order Book]] shows 150 lots offered at $82.50 and another 100 lots at $82.52. The trader sends a FOK buy order for 200 lots at $82.50. Because only 150 lots are available at $82.50, the [[Matching Engine]] cannot fill the full 200 at the limit price, so the entire order is killed. The trader gets zero fills.

If instead the book had shown 200 lots at $82.50, the FOK would fill completely at $82.50. The win: the trader gets the exact hedge size at the exact price needed. The risk: by insisting on FOK, the trader misses the 150 lots that were available and the market moves to $82.80 before enough liquidity appears. The opportunity cost is $0.30 per barrel x 200 lots x 1,000 barrels = $60,000.

## Key mechanics and formulas
- **Execution condition**: if available quantity at limit price or better >= order quantity, fill everything. Otherwise, cancel everything.
- **Opportunity cost of rejection**: Opportunity cost = (next available fill price - FOK limit price) x order size. This measures what the trader pays for insisting on FOK instead of accepting partial fills via [[IOC]].
- **Book depth requirement**: FOK orders require the full order size to be visible on one side of the book. On thin markets, FOK rejection rates can exceed 80%.
- **No resting**: like [[IOC]], FOK orders never enter the order book. They are evaluated and resolved in a single matching cycle.

## Prerequisites
- [[IOC]]
- [[Central Limit Order Book]]
- [[Matching Engine]]
- [[Limit Order]]
- [[Liquidity]]

## Related concepts (learn next)
- [[IOC]]: the more flexible alternative that accepts partial fills, cancelling only the unfilled remainder.
- [[Block Trade]]: large negotiated trades that often use FOK logic to ensure the full size is committed.
- [[Calendar Spread]]: a common strategy where FOK prevents dangerous partial fills on spread legs.
- [[Market Impact]]: FOK avoids the incremental information leakage that comes from partial fills, but also forfeits available liquidity.
- [[Request for Quote]]: on OTC and [[Multi Dealer Platform]] venues, RFQ workflows function like FOK, where the full amount must be quoted.
- [[Depth of Book]]: understanding visible depth is critical before choosing FOK, because shallow books will reject FOK orders frequently.
- [[Slippage]]: FOK eliminates slippage risk (you get your price or nothing) but introduces rejection risk.

## Common misconceptions
1. **"FOK and IOC are interchangeable"**: They are fundamentally different. IOC accepts whatever it can get and cancels the rest. FOK demands 100% fill or nothing. Choosing the wrong one can leave you with an unwanted partial position (IOC) or no position at all when liquidity was available (FOK).
2. **"FOK guarantees execution at my price"**: FOK guarantees that if you are filled, it is at your price or better. But it absolutely does not guarantee execution. On illiquid contracts, FOK orders are rejected more often than they fill.
3. **"FOK is always better for large orders"**: For truly large orders, the insistence on full fills means repeated rejections and potential information leakage from the pattern of attempts. A well-designed algorithm using [[IOC]] slices often achieves better total execution than repeated FOK attempts.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003), Chapter 4
- CME Group, "Order Types Available on CME Globex"
- ICE Futures, "Order Type Reference Guide"
