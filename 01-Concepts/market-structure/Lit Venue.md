---
aliases: [lit market, lit pool, transparent venue, lit exchange]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Lit Venue

## Definition

A lit venue is a trading venue where all resting orders are visible in a public [[Central Limit Order Book|order book]]. Anyone connected sees [[Bid]], [[Ask]], and [[Depth of Book|depth]] at every price level. CME, ICE, and LME are lit. In FX, ECNs like EBS and Refinitiv operate as lit venues. The opposite is a [[Dark Pool]], where orders are hidden until execution.

## Why it matters (commodities and FX)

Lit venues provide price transparency. A trader sees exactly how much [[Brent Crude]] is bid and offered at each level, informing execution. Transparency cuts both ways: showing a large order signals intent, and others may trade ahead ([[Market Impact]]). The lit vs dark execution choice is core for any desk managing significant flow.

## Concrete example

**Concrete:** A trader needs to sell 500 lots of [[WTI]] on CME Globex. The book shows 120 lots at $82.50, 200 at $82.49, 180 at $82.48. Route A: use a [[TWAP]] algo to drip 500 lots over 30 minutes, never showing more than 10 at once. Others do not detect the large sell. Average fill $82.49. Minimal [[Market Impact]]. Route B: post all 500 lots as one sell at $82.48. Others see the visible offer, front run by selling ahead, market drops to $82.40 before the order clears. Average fill $82.42: 8 ticks of slippage from posting a visible block.

**Simplified:** On a lit venue, everyone sees your order. Useful when you want fast price discovery. Bad when you have size, because other traders will trade ahead of you. Small orders: post and forget. Large orders: split into pieces or route to a [[Dark Pool]].

## Key mechanics and formulas

**Lit venue characteristics:**
- Full order book visibility (price and size at each level)
- Price/time priority matching
- Pre trade transparency (orders visible before trading)
- Post trade transparency (all trades reported)

**Information leakage cost of lit execution:**

Leakage cost = market_impact_from_visibility * order_size

This is why large orders split between lit and [[Dark Pool|dark]] via [[Smart Order Routing]].

**Lit vs dark trade off:**

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

- [[Dark Pool]] for the hidden alternative
- [[Central Limit Order Book]] for the order book structure
- [[Market Impact]] for why lit visibility creates execution cost
- [[Top of Book]] for the best prices on the lit venue
- [[Smart Order Routing]] for splitting between lit and dark
- [[ECN]] for electronic lit venues in FX

## Common misconceptions

1. **"Lit venues always give better prices."** Transparency costs information. For large orders, a [[Dark Pool]] fill at [[Mid Price]] beats sweeping visible lit depth.

2. **"All FX trading happens on lit venues."** Most FX volume trades bilaterally on [[Single Dealer Platform|SDPs]] or voice with no public book. Lit FX venues (EBS, Refinitiv) capture only a fraction.

3. **"Lit books show the true market."** Real liquidity sits in dark pools, internal crossing ([[Internalization]]), and iceberg orders that show only a fraction of their size.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- SEC, "Regulation NMS" (equity market structure context)
- BIS, "Triennial Central Bank Survey" (FX market structure)
