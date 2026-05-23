---
aliases: [order cancel, order cancellation, pull an order, cancel order]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Cancel

## Definition

A cancel withdraws an open order before it gets [[Fill|filled]]. The cancel request travels to the venue, which attempts to remove the order from the [[Central Limit Order Book|order book]]. Cancellation is not instantaneous: there is always [[Latency]] between sending and confirmation. During that window the order can still fill. A successful cancel returns an acknowledgement; a failed cancel (order already filled) is a "cancel reject" or "too late to cancel."

## Why it matters (commodities and FX)

Market makers cancel and replace orders thousands of times per second to keep quotes fresh. Slow cancels mean fills on [[Stale Quote|stale quotes]]. In volatile markets (around [[EIA Weekly Petroleum Status Report|EIA]] data), cancel speed is the primary defense against [[Adverse Selection]]. For execution desks, cancelling a [[Limit Order]] no longer at the right price and replacing it is a core operation. Cancel latency is as important as order entry latency.

## Concrete example

**Concrete:** Market maker quoting [[WTI]] at $82.50 / $82.55. News breaks: drone strike on a Saudi facility. Maker sends cancels for both sides. With 15 microsecond round trip, both orders are removed before anyone trades against them. Maker requotes $83.50 / $83.60. No losses. Failure path: cancel for the $82.55 ask takes 200 microseconds due to network [[Jitter]]. During that window, a fast algo lifts 20 lots at $82.55. Market has moved to $83.50. Maker is now [[Short]] 20 lots at $82.55 in a $83.50 market: instant loss of $0.95 × 20 × 1,000 = $19,000.

**Simplified:** When you cancel an order, the message has to travel to the exchange and the exchange has to act on it. In that brief window, your order is still live and someone can hit it. If news breaks and prices move, slow cancels mean you trade at the old price right when the market has shifted against you. Speed of cancel is what protects market makers from getting picked off when conditions change.

## Key mechanics and formulas

**Cancel lifecycle:**

1. Trader sends cancel request (with original order ID)
2. Message travels to venue ([[Latency]])
3. Venue processes cancel (checks if order still live)
4. Venue sends acknowledgement (confirmed) or reject (already filled)

**Cancel rate** = cancels / (cancels + fills)

Market makers run cancel rates above 95%: most orders are cancelled and replaced before filling. Normal and necessary for fresh quoting.

**Cancel vulnerability window** = round trip [[Latency]] to venue

During this window the order is "live but unwanted," exposed to [[Adverse Selection]].

## Prerequisites

- [[Limit Order]]
- [[Fill]]
- [[Latency]]

## Related concepts (learn next)

- [[Stale Quote]] for what happens when cancels are too slow
- [[Sniping]] for adversaries exploiting slow cancels
- [[IOC]] for an order type that avoids cancels (auto expires)
- [[Kill Switch]] for emergency mass cancellation
- [[Latency]] for the critical factor in cancel speed
- [[FIX Protocol]] for the standard cancel message format

## Common misconceptions

**"Cancel means the order is gone instantly."** There is always a round trip delay. Fills happen in that window. Major risk for market makers.

**"High cancel rates mean manipulation."** Market makers legitimately cancel 95%+ because they update quotes continuously. Normal, not spoofing (which involves orders placed with no intent to trade).

**"A cancel always succeeds."** If the order filled or partially filled during the latency window, the cancel is rejected. Systems must handle rejects.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- CME Group, "Order Management and Cancel Policies"
- FIX Trading Community, "FIX Protocol Order Cancel Request (35=F)"
