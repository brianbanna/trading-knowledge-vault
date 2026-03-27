---
aliases: [order cancel, order cancellation, pull an order, cancel order]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Cancel

## Definition

A cancel is the withdrawal of an open order before it gets [[Fill|filled]]. When a trader sends a cancel request, the venue attempts to remove the order from the [[Central Limit Order Book|order book]]. Cancellation is not instantaneous. There is always [[Latency]] between sending the cancel and the venue confirming it. During that window, the order can still be filled. A successful cancel returns an acknowledgement; a failed cancel (because the order was already filled) is called a "cancel reject" or "too late to cancel."

## Why it matters (commodities and FX)

Market makers cancel and replace orders thousands of times per second to keep quotes fresh. If cancels are slow, the risk of being filled on [[Stale Quote|stale quotes]] rises dramatically. In volatile markets (e.g., around [[EIA Weekly Petroleum Status Report|EIA]] data), the ability to cancel fast is the primary defense against [[Adverse Selection]]. For execution desks, cancelling a [[Limit Order]] that is no longer at the right price and replacing it is a core operation. Cancel latency is as important as order entry latency.

## Concrete example

A market maker is quoting [[WTI]] crude at $82.50 / $82.55. Breaking news: a drone strike on a Saudi oil facility. The maker immediately sends cancels for both the bid and ask.

**Success case:** Cancel messages reach the exchange in 15 microseconds. Both orders are removed before anyone trades against them. The maker re quotes at $83.50 / $83.60 reflecting the new reality. No losses.

**Failure case:** The cancel for the ask at $82.55 takes 200 microseconds due to network [[Jitter]]. During that window, a fast algo buys 20 lots at $82.55. The market has already moved to $83.50. The maker is now [[Short]] 20 lots at $82.55 with the market at $83.50, an instant loss of $0.95 * 20 * 1,000 = $19,000.

## Key mechanics and formulas

**Cancel lifecycle:**

1. Trader sends cancel request (includes original order ID)
2. Message travels to venue ([[Latency]])
3. Venue processes cancel (checks if order still live)
4. Venue sends acknowledgement (cancel confirmed) or reject (already filled)

**Cancel rate** = cancels / (cancels + fills)

Market makers typically have cancel rates above 95%, meaning most orders are cancelled and replaced before being filled. This is normal and necessary for fresh quoting.

**Cancel vulnerability window** = round trip [[Latency]] to venue

During this window, the order is "live but unwanted," exposed to [[Adverse Selection]].

## Prerequisites

- [[Limit Order]]
- [[Fill]]
- [[Latency]]

## Related concepts (learn next)

- [[Stale Quote]] for what happens when cancels are too slow
- [[Sniping]] for adversaries exploiting slow cancels
- [[IOC]] for an order type that avoids the need to cancel (auto expires)
- [[Kill Switch]] for emergency mass cancellation of all orders
- [[Latency]] for the critical factor determining cancel speed
- [[FIX Protocol]] for the standard message format for sending cancels

## Common misconceptions

1. **"Cancel means the order is gone instantly."** There is always a round trip delay. In that window, fills can and do happen. This is a major source of risk for market makers.

2. **"High cancel rates mean market manipulation."** Market makers legitimately cancel 95%+ of their orders because they update quotes continuously. This is normal, not spoofing (which involves cancelling orders placed with no intent to trade).

3. **"A cancel request always succeeds."** If the order was already filled or partially filled during the latency window, the cancel will be rejected. Systems must handle cancel rejects gracefully.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- CME Group, "Order Management and Cancel Policies"
- FIX Trading Community, "FIX Protocol Order Cancel Request (35=F)"
