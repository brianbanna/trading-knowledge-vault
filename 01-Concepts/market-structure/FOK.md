---
aliases: [FOK, fill or kill, fill-or-kill, all or nothing]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# FOK

## Definition
Fill or Kill (FOK) is an order instruction requiring the entire quantity to fill immediately in a single execution, or the entire order is cancelled. Unlike [[IOC]] which accepts partial fills and cancels only the remainder, FOK is all or nothing. If the [[Central Limit Order Book]] lacks enough liquidity at the limit price or better to fill the full size in one shot, the order is rejected entirely. FOK is used when partial execution would leave the trader worse off than no execution, for example when hedging a specific notional or executing one leg of a [[spread]] where a partial fill creates unwanted directional risk.

## Why it matters (commodities and FX)
In commodities, FOK is essential for [[spread]] trades. Buying 100 lots of Brent December and selling 100 lots of Brent January as a [[calendar spread]] cannot tolerate partial fills on one leg, which creates naked exposure. FOK ensures both sides execute fully or not at all. In FX, FOK is used on [[Multi Dealer Platform]]s where a client requests a firm price from multiple banks for a specific amount. The client fills the whole clip or walks away. FOK is also standard for [[block trade]]s on exchanges where minimum size thresholds must be met in full.

## Concrete example

**Concrete:** Trader needs exactly 200 lots of ICE Brent at $82.50 or better to hedge a physical cargo. CLOB shows 150 lots offered at $82.50 and 100 lots at $82.52. FOK buy for 200 lots at $82.50: matching engine cannot fill full 200 at limit, order is killed. Zero fills. If the book had 200 lots at $82.50, FOK fills completely at $82.50. Win: exact hedge size at exact price. Risk: insisting on FOK misses the 150 lots that were available; market moves to $82.80 before enough liquidity appears. Opportunity cost $0.30 × 200,000 barrels = $60,000.

**Simplified:** FOK is the strictest order type. Either you get everything you asked for at your price right now, or you get nothing. Used when half the trade is worse than none, like one leg of a spread or a hedge that must match a specific cargo. The risk is high rejection rates on illiquid contracts because the book often does not have your full size waiting at your price.

## Key mechanics and formulas
- **Execution condition**: if available at limit or better >= order size, fill all. Else cancel all.
- **Opportunity cost of rejection**: (next available fill price − FOK limit) × order size. Cost of insisting on FOK vs accepting partials via [[IOC]].
- **Book depth requirement**: FOK requires full order size visible on one side. On thin markets, rejection rates can exceed 80%.
- **No resting**: like [[IOC]], FOK never enters the book. Evaluated and resolved in a single matching cycle.

## Prerequisites
- [[IOC]]
- [[Central Limit Order Book]]
- [[Matching Engine]]
- [[Limit Order]]
- [[Liquidity]]

## Related concepts (learn next)
- [[IOC]]: more flexible alternative accepting partials.
- [[Block Trade]]: large negotiated trades using FOK logic.
- [[Calendar Spread]]: where FOK prevents dangerous partial fills on legs.
- [[Market Impact]]: FOK avoids leakage from partial fills but forfeits available liquidity.
- [[Request for Quote]]: OTC and [[Multi Dealer Platform]] RFQ workflows function like FOK.
- [[Depth of Book]]: critical before choosing FOK; shallow books reject often.
- [[Slippage]]: FOK eliminates slippage but introduces rejection risk.

## Common misconceptions

**"FOK and IOC are interchangeable."** Fundamentally different. IOC accepts what it can get; FOK demands 100% or nothing. Wrong choice leaves you with an unwanted partial (IOC) or no position when liquidity existed (FOK).

**"FOK guarantees execution at my price."** It guarantees that if you fill, it is at your price or better. It does not guarantee execution. On illiquid contracts FOK rejects more often than it fills.

**"FOK is always better for large orders."** Insisting on full fills means repeated rejections and leakage from the pattern of attempts. A well designed algo using [[IOC]] slices often achieves better total execution than repeated FOK attempts.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003), Chapter 4
- CME Group, "Order Types Available on CME Globex"
- ICE Futures, "Order Type Reference Guide"
