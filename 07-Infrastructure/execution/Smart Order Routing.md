---
aliases: [SOR, smart order router, intelligent order routing, best execution routing]
tags:
  - "#execution"
  - "#infrastructure"
date-added: "2026-03-27"
---

# Smart Order Routing

## Definition

Smart Order Routing (SOR) is a system that automatically determines the best venue to send an order based on price, available [[Liquidity]], fees, [[Latency]], and likelihood of fill. Instead of a trader manually choosing where to route, the SOR scans all connected venues in real time and splits or directs orders to achieve the best execution. SOR is essential in fragmented markets where the same instrument trades on multiple venues simultaneously.

## Why it matters (commodities and FX)

FX is one of the most fragmented markets in the world. [[EUR USD]] liquidity is spread across EBS, Refinitiv, Bloomberg, Cboe FX, dozens of [[Multi Dealer Platform|MDPs]], [[Single Dealer Platform|SDPs]], and [[Dark Pool|dark pools]]. A trader wanting to buy 50 million EUR cannot assume the best price is on any single venue. SOR ensures orders access the deepest liquidity at the tightest price, reducing [[Slippage]] and [[Market Impact]]. In commodities, SOR matters less for exchange traded futures (which have a single [[Central Limit Order Book|CLOB]]) but is critical for OTC and cleared swap markets with multiple execution venues.

## Concrete example

A desk needs to buy 30 million [[EUR USD]]. The SOR surveys 5 connected venues:

| Venue | Best ask | Size available |
|-------|----------|----------------|
| EBS | 1.08502 | 12M |
| Refinitiv | 1.08503 | 8M |
| Bank A SDP | 1.08501 | 5M |
| Bank B SDP | 1.08504 | 15M |
| Dark pool | 1.08500 | Unknown |

**Success case:** The SOR sends 5M to the dark pool (best price if filled), 5M to Bank A SDP, 12M to EBS, and 8M to Refinitiv. Total fill: 30M at a weighted average of 1.08502. Without SOR, sending the full 30M to EBS would have swept [[Depth of Book|depth]], filling at a weighted average of 1.08508, costing an extra $1,800.

**Failure case:** The SOR sends 5M to the dark pool, but the pool has no matching interest and the order rests for 200 milliseconds. During that time, the market moves up 2 [[Pip|pips]]. The remaining 25M fills at worse prices. Total slippage: $3,500 more than immediate execution would have cost. The SOR's dark pool timeout was set too long.

## Key mechanics and formulas

**SOR decision inputs:**
- [[Bid]] / [[Ask]] prices at each venue (top of book and depth)
- Historical fill rates per venue
- Venue fees and rebates
- [[Latency]] to each venue
- [[Last Look]] rejection rates per venue
- Dark pool match probability estimates

**Execution cost minimization:**

Total cost = sum over venues of (fill_i * price_i) + sum of (fee_i * fill_i) + slippage from information leakage

The SOR minimizes this function subject to:
- sum of fill_i = total order size
- fill_i <= available_size_i at each venue
- timing constraints (urgency)

**Key SOR parameters:**
- Sweep vs. sequential: sweep all venues simultaneously or route sequentially
- Dark pool timeout: how long to wait for a dark match before routing to lit venues
- Minimum venue size: ignore venues with insufficient depth
- Anti gaming: detect and avoid venues with high [[Adverse Selection]]

## Prerequisites

- [[Liquidity]]
- [[Depth of Book]]
- [[Slippage]]
- [[Market Impact]]
- [[Dark Pool]]

## Related concepts (learn next)

- [[VWAP]] for an execution algo that SOR can work alongside to minimize market impact
- [[TCA]] for measuring whether the SOR actually achieved best execution
- [[Implementation Shortfall]] for the cost metric SOR tries to minimize
- [[Dark Pool]] for hidden liquidity venues that SOR must evaluate probabilistically
- [[Last Look]] for venue rejection risk that SOR must factor into routing decisions
- [[Internalization]] for how banks route internally before sending to external venues
- [[Latency]] for why speed to each venue affects SOR effectiveness

## Common misconceptions

1. **"SOR guarantees best execution."** SOR optimizes based on observable data, but hidden information (dark pool interest, incoming orders, [[Last Look]] rejections) means the outcome is probabilistic, not guaranteed.

2. **"SOR is only for equities."** While SOR originated in equity markets (Reg NMS in the US), FX markets are even more fragmented and benefit enormously from intelligent routing. Any multi venue market needs SOR.

3. **"Just route to the venue with the best price."** The best price might have insufficient size, high rejection rates, or high fees. SOR must consider price, size, fill probability, and cost together.

4. **"SOR replaces execution algos."** SOR decides where to send. Execution algos ([[VWAP]], [[TWAP]], [[POV]]) decide when and how much to send. They work together, not as substitutes.

## Sources

- Cartea, A., Jaimungal, S., and Penalva, J., "Algorithmic and High Frequency Trading," Cambridge University Press
- Johnson, Barry, "Algorithmic Trading and DMA," 4Myeloma Press
- FCA, "Best Execution and Payment for Order Flow" discussion paper
