---
aliases: [network latency, round trip time, RTT, delay]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Latency

## Definition

Latency is the time delay between initiating an action and seeing the result. In trading, it typically refers to the round trip time between sending a message (an order, a cancel, a quote update) and receiving an acknowledgement from the venue. Latency is measured in [[Latency Units|milliseconds, microseconds, or nanoseconds]] depending on the system. Lower latency means faster reaction to market changes, fresher quotes, and better execution quality.

## Why it matters (commodities and FX)

In FX market making, latency determines whether quotes are fresh or [[Stale Quote|stale]]. A desk with 50 microsecond [[Tick to Trade]] latency can update quotes before a desk with 500 microsecond latency, meaning the slower desk gets [[Sniping|sniped]] on stale prices. In commodity futures, latency affects the ability to react to data releases ([[EIA Weekly Petroleum Status Report|EIA]], USDA) before competitors. Even for non HFT desks, excessive latency (e.g., 100+ milliseconds) causes [[Slippage]] and [[Partial Fill|partial fills]].

## Concrete example

Two desks make markets in [[EUR USD]] on EBS. Desk A is co located in the Equinix NY5 data center (50 microsecond round trip). Desk B is in London (80 millisecond round trip, 1,600x slower).

**Scenario: ECB surprises with a 50bp rate cut.**

Desk A's system detects the news, recalculates the fair price, and cancels stale quotes in 100 microseconds. No stale quotes are hit.

Desk B's cancel takes 80 milliseconds to reach EBS. During that 80 millisecond window, fast participants [[Sniping|snipe]] Desk B's stale ask 14 times. Each snipe costs approximately $3,000 in adverse selection. Total loss: $42,000 in under a second.

**Lesson:** Desk B either needs to [[Co-location|co locate]], widen spreads to compensate for latency disadvantage, or stop quoting around event risk.

## Key mechanics and formulas

**Types of latency:**

| Type | Definition |
|------|-----------|
| One way latency | Time from send to receive (half the round trip) |
| Round trip time (RTT) | Send plus response time |
| [[Tick to Trade]] | Market data in to order out (internal processing) |
| Wire latency | Physical signal propagation time (speed of light) |
| Processing latency | Time spent in software logic |

**Speed of light constraint:**
Wire latency (fiber) = distance / (speed of light * 0.67)

New York to London = 5,600 km / (300,000 km/s * 0.67) = ~28 milliseconds one way

This is a physical minimum. No software optimization can beat it. Only [[Co-location]] eliminates it.

**Latency budget example:**
| Component | Time |
|-----------|------|
| Wire to venue | 500 ns (co located) |
| NIC + kernel | 2 us |
| Market data parse | 3 us |
| Strategy logic | 5 us |
| Risk check | 2 us |
| Order encode + send | 1.5 us |
| Wire to venue | 500 ns |
| **Total round trip** | **~15 us** |

## Prerequisites

- [[Tick to Trade]]
- [[Co-location]]

## Related concepts (learn next)

- [[Tick to Trade]] for the end to end internal latency metric
- [[Co-location]] for eliminating wire latency by being physically close
- [[Jitter]] for why variance in latency matters as much as the average
- [[Throughput]] for the other dimension of system performance (messages per second)
- [[Stale Quote]] for the consequence of excessive latency
- [[Hot Path]] for optimizing the code path that determines latency
- [[Latency Units]] for understanding the time scales involved

## Common misconceptions

1. **"Latency only matters for HFT."** Any electronic trader cares about latency. A desk with 500 millisecond latency will consistently get worse fills than one with 50 millisecond latency, regardless of strategy.

2. **"Faster internet fixes latency."** Bandwidth (how much data per second) is different from latency (how fast data arrives). A 10 Gbps connection from London to New York still has 28+ millisecond one way latency due to physics.

3. **"Software optimization can always reduce latency."** Below a certain point, latency is dominated by physics (speed of light in fiber). Co location is the only solution for wire latency; software optimization only helps processing latency.

## Sources

- Rajiv Ranjan, "Low Latency Trading Infrastructure," Springer
- CME Group, "Co Location Services and Latency Metrics"
- Hasbrouck, Joel, "Empirical Market Microstructure," Oxford University Press
