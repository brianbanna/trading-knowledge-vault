---
aliases: [dark pool, dark liquidity, dark venue, hidden orders]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Dark Pool

## Definition
A dark pool is a private trading venue where orders are not displayed to other market participants before execution. Unlike a [[Central Limit Order Book]] where every bid and offer is visible, dark pool orders are hidden until they match. The primary advantage is elimination of [[information leakage]]: no one can see your order and trade ahead of you. The primary disadvantage is that execution is uncertain because you cannot see available liquidity. Dark pools exist in equities (Crossfinder, Sigma X), FX (EBS Market, Fastmatch dark), and increasingly in fixed income. In FX, dark pool functionality is often embedded within [[ECN]]s or [[Multi Dealer Platform]]s as an optional matching mode rather than a standalone venue.

## Why it matters (commodities and FX)
Large commodity hedging flows and institutional FX orders are vulnerable to [[front-running]] and [[market impact]]. A mining company that needs to sell 500 million AUD/USD to repatriate export revenue cannot display that order on a lit venue without moving the market. A dark pool allows the order to rest invisibly, matching against incoming flow at or near the [[mid price]] without signaling to the market. In energy markets, large block trades in crude or natural gas futures are sometimes negotiated through dark mechanisms (exchange-for-physical, block trade facilities) for the same reason. Understanding dark pools is critical for designing execution strategies that balance the certainty of lit venues against the reduced impact of dark venues.

## Concrete example
A sovereign wealth fund needs to buy 200 million EUR/USD. On a lit [[ECN]] like [[EBS]], placing a 200 million bid would instantly telegraph demand and push the offer price higher. Instead, the fund places a dark order on an FX dark pool at the current mid price of 1.08500. Over the next 3 hours, the dark pool matches the order against incoming sell flow in clips of 5 to 20 million, filling a total of 140 million at an average price of 1.08502, just 0.2 pips from mid. The remaining 60 million is unfilled because not enough natural sell flow arrived.

The fail scenario: the market rallies to 1.08700 during those 3 hours. The fund filled 140 million near 1.08500 (good), but the remaining 60 million must now be sourced on a lit venue at 1.08700 (bad). The blended average is worse than if the fund had executed everything aggressively at the start. This is the fundamental tradeoff: dark pools reduce [[market impact]] but introduce [[opportunity cost]] from delayed or incomplete fills.

## Key mechanics and formulas
- **Midpoint matching**: Most FX dark pools match at the prevailing [[mid price]] from a reference venue ([[EBS]], [[Reuters Matching]]), meaning both buyer and seller save half the [[bid-ask spread]].
- **Fill rate**: Fill rate = filled quantity / total order quantity. Dark pool fill rates for large FX orders typically range from 20% to 60%, depending on pair, time of day, and order size.
- **Information leakage savings**: Estimated savings = [[market impact]] of lit execution - actual cost of dark execution. For a 200 million EUR/USD order, this can be 1 to 3 pips, worth $20,000 to $60,000.
- **Adverse selection**: Dark pool participants face [[adverse selection]] risk. If the market is moving, the counterparty filling your dark order may have information that the price is about to move against you.
- **Minimum quantity**: Many dark pools enforce minimum order sizes (e.g., 1 million in FX) to prevent small "pinging" orders that probe for hidden liquidity.

## Prerequisites
- [[Central Limit Order Book]]
- [[Bid-Ask Spread]]
- [[Market Impact]]
- [[Liquidity]]
- [[Mid Price]]

## Related concepts (learn next)
- [[Central Limit Order Book]]: the lit alternative where all orders are visible, offering execution certainty but maximum information leakage.
- [[Iceberg Order]]: a partial compromise between dark and lit, where a small visible portion hides a larger total order.
- [[Information Leakage]]: the core problem dark pools solve, where visible orders reveal trading intentions to the market.
- [[Adverse Selection]]: the key risk in dark pools, where counterparties may be better informed about short term price direction.
- [[Internalization]]: banks run internal dark pools by matching client flow against each other before routing to external venues.
- [[Market Impact]]: the price movement caused by large visible orders, which dark pools are designed to minimize.
- [[Block Trade]]: exchange mechanisms for large negotiated trades that function similarly to dark pool matching.
- [[ECN]]: the lit venue model that many dark pools complement, often offered as a dual mode on the same platform.

## Common misconceptions
1. **"Dark pools are unregulated and shady"**: In equities, dark pools are registered trading venues subject to regulatory oversight (SEC in the US, FCA in the UK). In FX, dark pool functionality is embedded in regulated platforms. The "dark" refers to order visibility, not regulatory status.
2. **"Dark pools guarantee better prices"**: Dark pools guarantee less information leakage, not better prices. [[Adverse selection]] can make dark pool fills systematically worse if the pool attracts informed counterparties. Monitoring realized P&L of dark fills versus lit fills is essential.
3. **"If I trade in a dark pool, nobody knows"**: Post-trade reporting exists in most markets. In equities, dark pool trades are reported to the consolidated tape within seconds. In FX, prime brokers see all fills. The anonymity applies to pre-trade intent, not post-trade activity.
4. **"Dark pools always have enough liquidity"**: Fill rates are often low. Relying solely on dark liquidity for time-sensitive hedges (like a commodity cargo that prices at a specific window) is dangerous because execution is not guaranteed.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003), Chapter 18
- BIS Markets Committee, "Monitoring of Fast-Paced Electronic Markets" (2018)
- Zhu, Haoxiang, "Do Dark Pools Harm Price Discovery?," Review of Financial Studies (2014)
- SEC, "Regulation ATS and Dark Pool Transparency" guidance documents
