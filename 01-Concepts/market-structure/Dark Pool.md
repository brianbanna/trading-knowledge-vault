---
aliases: [dark pool, dark liquidity, dark venue, hidden orders]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Dark Pool

## Definition
A dark pool is a private trading venue where orders are not displayed to other participants before execution. Unlike a [[Central Limit Order Book]] where every bid and offer is visible, dark pool orders are hidden until they match. The primary advantage is elimination of [[information leakage]]: no one can see your order and trade ahead of you. The primary disadvantage is execution uncertainty because you cannot see available liquidity. Dark pools exist in equities (Crossfinder, Sigma X), FX (EBS Market, Fastmatch dark), and increasingly fixed income. In FX, dark functionality is often embedded within [[ECN]]s or [[Multi Dealer Platform]]s as an optional matching mode rather than a standalone venue.

## Why it matters (commodities and FX)
Large commodity hedging flows and institutional FX orders are vulnerable to [[front-running]] and [[market impact]]. A mining company selling AUD 500 million to repatriate export revenue cannot display that order on a lit venue without moving the market. A dark pool lets the order rest invisibly, matching incoming flow at or near the [[mid price]] without signaling intent. In energy markets, large block trades in crude or natural gas are negotiated through dark mechanisms (exchange for physical, block trade facilities) for the same reason. Understanding dark pools is critical for execution that balances lit certainty against dark impact reduction.

## Concrete example

**Concrete:** A sovereign wealth fund buys EUR 200 million EUR/USD. On a lit [[ECN]] like [[EBS]], a 200 million bid telegraphs demand and pushes the offer higher. The fund places a dark order at the mid 1.08500. Over 3 hours the dark pool matches it against incoming sell flow in clips of 5 to 20 million, filling 140 million at average 1.08502, 0.2 pips from mid. The remaining 60 million is unfilled. Failure mirror: market rallies to 1.08700 during those 3 hours. The 140 million filled near 1.08500 is good; the remaining 60 million must now fill on a lit venue at 1.08700. Blended average is worse than aggressive execution at the start. Dark pools reduce [[market impact]] but introduce [[opportunity cost]] from delayed or incomplete fills.

**Simplified:** A dark pool is a venue where your order is hidden from everyone else until it matches. You save on market impact because no one front runs you, but you also cannot see what liquidity is there. Sometimes you wait and nothing matches because there is no counterparty hiding on the other side. Big institutions use dark pools when they are too big to show on a lit venue without moving prices.

## Key mechanics and formulas
- **Midpoint matching**: Most FX dark pools match at the [[mid price]] from a reference venue ([[EBS]], [[Reuters Matching]]), so both sides save half the [[bid-ask spread]].
- **Fill rate**: filled quantity / order quantity. Dark pool FX fill rates for large orders typically range 20% to 60%, varying by pair, time, and size.
- **Information leakage savings**: lit [[market impact]] − actual dark cost. For EUR 200 million EUR/USD, 1 to 3 pips ($20,000 to $60,000).
- **Adverse selection**: dark counterparties may have information that price is about to move against you.
- **Minimum quantity**: many dark pools enforce minimums (1 million in FX) to prevent "pinging" probes for hidden liquidity.

## Prerequisites
- [[Central Limit Order Book]]
- [[Bid-Ask Spread]]
- [[Market Impact]]
- [[Liquidity]]
- [[Mid Price]]

## Related concepts (learn next)
- [[Central Limit Order Book]]: lit alternative with execution certainty but maximum leakage.
- [[Iceberg Order]]: partial compromise; visible portion hides a larger total.
- [[Information Leakage]]: core problem dark pools solve.
- [[Adverse Selection]]: key dark pool risk.
- [[Internalization]]: banks run internal dark pools matching client flow before external routing.
- [[Market Impact]]: what dark pools are designed to minimize.
- [[Block Trade]]: exchange mechanisms for large negotiated trades, similar to dark matching.
- [[ECN]]: lit model many dark pools complement.

## Common misconceptions

**"Dark pools are unregulated."** In equities, registered trading venues under SEC/FCA oversight. In FX, dark functionality lives inside regulated platforms. "Dark" refers to order visibility, not regulatory status.

**"Dark pools guarantee better prices."** They guarantee less information leakage, not better prices. [[Adverse selection]] can make dark fills systematically worse if the pool attracts informed counterparties.

**"In a dark pool, nobody knows."** Post trade reporting exists. Equities report to the consolidated tape in seconds; FX prime brokers see all fills. Anonymity is pre trade, not post trade.

**"Dark pools always have liquidity."** Fill rates are often low. Relying on dark for time sensitive hedges (cargo pricing windows) is dangerous because execution is not guaranteed.

## Sources
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003), Chapter 18
- BIS Markets Committee, "Monitoring of Fast-Paced Electronic Markets" (2018)
- Zhu, Haoxiang, "Do Dark Pools Harm Price Discovery?," Review of Financial Studies (2014)
- SEC, "Regulation ATS and Dark Pool Transparency" guidance documents
