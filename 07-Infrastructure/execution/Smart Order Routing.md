---
aliases: [SOR, smart order router, intelligent order routing, best execution routing]
tags:
  - "#execution"
  - "#infrastructure"
date-added: "2026-03-27"
---

# Smart Order Routing

## Definition

Smart Order Routing (SOR) automatically chooses the best venue for each order based on price, available [[Liquidity]], fees, [[Latency]], and fill probability. The SOR scans all connected venues in real time and splits or directs orders for best execution. SOR is essential in fragmented markets where the same instrument trades on multiple venues simultaneously.

## Why it matters (commodities and FX)

FX is one of the most fragmented markets. [[EUR USD]] liquidity sits across EBS, Refinitiv, Bloomberg, Cboe FX, dozens of [[Multi Dealer Platform|MDPs]], [[Single Dealer Platform|SDPs]], and [[Dark Pool|dark pools]]. A trader buying 50 million EUR cannot assume the best price is on a single venue. SOR ensures orders hit the deepest liquidity at the tightest price, cutting [[Slippage]] and [[Market Impact]]. In commodities, SOR matters less for exchange traded futures (single [[Central Limit Order Book|CLOB]]) but is critical for OTC and cleared swap markets with multiple venues.

## Concrete example

**Concrete:** A desk needs to buy 30 million [[EUR USD]]. The SOR surveys 5 venues:

| Venue | Best ask | Size available |
|-------|----------|----------------|
| EBS | 1.08502 | 12M |
| Refinitiv | 1.08503 | 8M |
| Bank A SDP | 1.08501 | 5M |
| Bank B SDP | 1.08504 | 15M |
| Dark pool | 1.08500 | Unknown |

The SOR sends 5M to the dark pool (best price if filled), 5M to Bank A SDP, 12M to EBS, 8M to Refinitiv. Total fill: 30M at weighted average 1.08502. Sending the full 30M to EBS instead would have swept [[Depth of Book|depth]] to weighted average 1.08508, costing an extra $1,800. If the dark pool sits idle for 200 ms and EUR/USD moves 2 pips up, the remaining 25M fills worse and slippage adds $3,500 over immediate execution. SOR dark pool timeout calibration matters.

**Simplified:** When the same thing trades in many places at slightly different prices, you do not want to send your whole order to one venue and pay the cost of clearing its book. You want software that looks at every venue, finds the cheapest combination, and ships pieces of your order accordingly. That software is the SOR.

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

Subject to:
- sum of fill_i = total order size
- fill_i <= available_size_i at each venue
- timing constraints (urgency)

**Key SOR parameters:**
- Sweep vs sequential: sweep all venues at once or route sequentially
- Dark pool timeout: how long to wait for a dark match before routing lit
- Minimum venue size: ignore venues with insufficient depth
- Anti gaming: detect and avoid venues with high [[Adverse Selection]]

## Prerequisites

- [[Liquidity]]
- [[Depth of Book]]
- [[Slippage]]
- [[Market Impact]]
- [[Dark Pool]]

## Related concepts (learn next)

- [[VWAP]] for an execution algo SOR works alongside to minimize impact
- [[TCA]] for measuring whether SOR actually achieved best execution
- [[Implementation Shortfall]] for the cost metric SOR minimizes
- [[Dark Pool]] for hidden liquidity venues SOR evaluates probabilistically
- [[Last Look]] for venue rejection risk SOR must price into routing
- [[Internalization]] for how banks route internally before external venues
- [[Latency]] for why speed to each venue affects SOR effectiveness

## Common misconceptions

1. **"SOR guarantees best execution."** SOR optimizes against observable data. Hidden information (dark pool interest, incoming flow, [[Last Look]] rejections) makes the outcome probabilistic, not guaranteed.

2. **"SOR is only for equities."** SOR originated in equity (Reg NMS) but FX is more fragmented and benefits enormously. Any multi venue market needs it.

3. **"Just route to the venue with the best price."** Best price may have insufficient size, high rejection rates, or high fees. SOR must consider price, size, fill probability, and cost together.

4. **"SOR replaces execution algos."** SOR decides where. Execution algos ([[VWAP]], [[TWAP]], [[POV]]) decide when and how much. They work together.

## Sources

- Cartea, A., Jaimungal, S., and Penalva, J., "Algorithmic and High Frequency Trading," Cambridge University Press
- Johnson, Barry, "Algorithmic Trading and DMA," 4Myeloma Press
- FCA, "Best Execution and Payment for Order Flow" discussion paper
