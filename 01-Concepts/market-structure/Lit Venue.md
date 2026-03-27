---
aliases: [lit market, lit pool, transparent venue, lit exchange]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Lit Venue

## Definition

A lit venue is a trading venue where all resting orders are visible in a public [[Central Limit Order Book|order book]]. Anyone connected to the venue can see the [[Bid]], [[Ask]], and [[Depth of Book|depth]] at every price level. Exchanges like CME, ICE, and LME are lit venues. In FX, ECNs like EBS and Refinitiv operate as lit venues where participants can see the order book. The opposite of a lit venue is a [[Dark Pool]], where orders are hidden until execution.

## Why it matters (commodities and FX)

Lit venues provide price transparency. A commodity trader can see exactly how much [[Brent Crude]] is bid and offered at each price level, informing execution decisions. However, this transparency cuts both ways: showing a large order on a lit venue signals intent, and other participants may trade ahead ([[Market Impact]]). The choice between lit and dark execution is a core decision for any desk managing significant order flow.

## Concrete example

A trader needs to sell 500 lots of [[WTI]] crude on CME Globex (a lit venue). The order book shows:

| Level | Bid | Size |
|-------|-----|------|
| 1 | $82.50 | 120 lots |
| 2 | $82.49 | 200 lots |
| 3 | $82.48 | 180 lots |

**Success case:** The trader uses a [[TWAP]] algo to drip 500 lots over 30 minutes, never showing more than 10 lots at a time. Other participants do not detect the large sell. Average fill: $82.49. Minimal [[Market Impact]].

**Failure case:** The trader posts all 500 lots as a single sell order at $82.48. Other participants see the large offer in the lit book, front run by selling ahead of it, and the market drops to $82.40 before the order fills. Average fill: $82.42, an 8 tick slippage from posting a visible large order.

## Key mechanics and formulas

**Lit venue characteristics:**
- Full order book visibility (price and size at each level)
- Price/time priority matching (first order at a price level gets filled first)
- Pre trade transparency (you see orders before they trade)
- Post trade transparency (all trades are reported)

**Information leakage cost of lit execution:**

Leakage cost = market_impact_from_visibility * order_size

This cost is why large orders are often split between lit and [[Dark Pool|dark]] venues via [[Smart Order Routing]].

**Lit vs. dark trade off:**

| Factor | Lit venue | [[Dark Pool]] |
|--------|-----------|------------|
| Transparency | Full | None |
| Price discovery | Yes | No (relies on lit prices) |
| Information leakage | High | Low |
| Fill certainty | Higher | Lower |
| Regulatory reporting | Immediate | Delayed |

## Prerequisites

- [[Central Limit Order Book]]
- [[Bid]]
- [[Ask]]
- [[Depth of Book]]

## Related concepts (learn next)

- [[Dark Pool]] for the hidden order alternative to lit venues
- [[Central Limit Order Book]] for the order book structure at the heart of lit venues
- [[Market Impact]] for why lit visibility creates execution costs
- [[Top of Book]] for the best prices visible on the lit venue
- [[Smart Order Routing]] for splitting orders between lit and dark venues
- [[ECN]] for electronic lit venues in FX markets

## Common misconceptions

1. **"Lit venues always give better prices."** Lit venues offer transparency, but that transparency has a cost (information leakage). For large orders, a [[Dark Pool]] fill at [[Mid Price]] can be cheaper than sweeping through visible lit depth.

2. **"All FX trading happens on lit venues."** The majority of FX volume is traded bilaterally on [[Single Dealer Platform|SDPs]] or voice, with no public order book. Lit FX venues (EBS, Refinitiv) capture only a fraction of total volume.

3. **"Lit order books show the true market."** Much of the real liquidity is hidden in dark pools, internal crossing engines ([[Internalization]]), and iceberg orders that show only a fraction of their true size.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- SEC, "Regulation NMS" (equity market structure context)
- BIS, "Triennial Central Bank Survey" (FX market structure)
