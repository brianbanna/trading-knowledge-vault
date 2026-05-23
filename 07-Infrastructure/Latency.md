---
aliases: [network latency, round trip time, RTT, delay]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Latency

## Definition

Latency is the time delay between initiating an action and seeing the result. In trading it refers to the round trip between sending a message (order, cancel, quote update) and receiving an acknowledgement from the venue. Measured in [[Latency Units|milliseconds, microseconds, or nanoseconds]] depending on the system. Lower latency means faster reaction to market changes, fresher quotes, and better execution quality.

## Why it matters (commodities and FX)

In FX market making, latency decides whether quotes are fresh or [[Stale Quote|stale]]. A desk at 50 microsecond [[Tick to Trade]] updates quotes before a desk at 500 microseconds, and the slower desk gets [[Sniping|sniped]] on stale prices. In commodity futures, latency decides the ability to react to data releases ([[EIA Weekly Petroleum Status Report|EIA]], USDA) before competitors. Even for non HFT desks, excessive latency (100+ ms) causes [[Slippage]] and [[Partial Fill|partial fills]].

## Concrete example

**Concrete:** Two desks make markets in [[EUR USD]] on EBS. Desk A is co located in Equinix NY5 (50 microsecond round trip). Desk B is in London (80 millisecond round trip, 1,600x slower). ECB surprises with a 50bp rate cut. Desk A detects the news, recalculates fair price, and cancels stale quotes in 100 microseconds. No stale quotes hit. Desk B's cancel takes 80 ms to reach EBS. During that window, fast participants [[Sniping|snipe]] Desk B's stale ask 14 times. Each snipe costs roughly $3,000 in adverse selection. Total loss: $42,000 in under a second. Desk B needs to [[Co-location|colocate]], widen spreads to compensate, or stop quoting around event risk.

**Simplified:** Latency is the time between asking and answering. Send an order, get a confirmation back. The longer the gap, the more the market moves before you know what happened. Light through fiber goes 5 microseconds per kilometer, so distance to the exchange sets a hard floor. Software on top of that adds more. Cutting both is what low latency engineering is.

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

A physical minimum. No software optimization beats it. Only [[Co-location]] eliminates it.

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
- [[Co-location]] for eliminating wire latency through proximity
- [[Jitter]] for why variance matters as much as the average
- [[Throughput]] for the other dimension of system performance (messages per second)
- [[Stale Quote]] for the consequence of excessive latency
- [[Hot Path]] for the code path that determines latency
- [[Latency Units]] for the time scales involved

## Common misconceptions

1. **"Latency only matters for HFT."** Any electronic trader cares. A 500 ms desk consistently gets worse fills than a 50 ms desk regardless of strategy.

2. **"Faster internet fixes latency."** Bandwidth (data per second) differs from latency (how fast data arrives). A 10 Gbps line from London to New York still has 28+ ms one way latency due to physics.

3. **"Software optimization can always reduce latency."** Below a certain point latency is dominated by physics. Colocation is the only fix for wire latency; software optimization only helps processing latency.

## Sources

- Rajiv Ranjan, "Low Latency Trading Infrastructure," Springer
- CME Group, "Co Location Services and Latency Metrics"
- Hasbrouck, Joel, "Empirical Market Microstructure," Oxford University Press
