---
aliases: [nanosecond, microsecond, millisecond, time units, latency units, ns, us, ms]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Latency Units

## Definition

Latency units are the time measurements used to describe how fast trading systems operate. The 3 key units are: millisecond (ms, 1 thousandth of a second, 10^-3), microsecond (us, 1 millionth of a second, 10^-6), and nanosecond (ns, 1 billionth of a second, 10^-9). Modern electronic trading operates across all 3 scales. Understanding which unit applies to which part of the system is essential for identifying bottlenecks and setting realistic performance targets.

## Why it matters (commodities and FX)

An FX market maker's [[Tick to Trade]] latency determines whether quotes are fresh or [[Stale Quote|stale]]. Knowing that "50 microseconds" is fast for a quoting engine but "50 milliseconds" is dangerously slow prevents miscommunication and bad architecture decisions. When evaluating [[Co-location]] providers, API vendors, or execution platforms, the units tell you whether you are comparing apples to apples.

## Concrete example

A desk builds an [[EUR USD]] quoting system and measures latency at each stage:

| Stage | Latency | Unit |
|-------|---------|------|
| Network hop (co located) | 500 | nanoseconds |
| Market data parsing | 2 | microseconds |
| Pricing engine | 8 | microseconds |
| Risk check | 3 | microseconds |
| Order encoding + send | 1.5 | microseconds |
| **Total [[Tick to Trade]]** | **~15** | **microseconds** |

**Success case:** At 15 microseconds, the desk updates quotes before competitors can [[Sniping|snipe]] stale prices. [[Stale Quote]] events are near zero.

**Failure case:** A logging library adds a 2 millisecond (2,000 microsecond) GC pause on the [[Hot Path]]. This is 130x the entire tick to trade budget. During the pause, 3 stale quotes are sniped for a $28,000 loss.

## Key mechanics and formulas

**Unit conversion:**

| Unit | Symbol | Seconds | Relative |
|------|--------|---------|----------|
| Second | s | 1 | 1 |
| Millisecond | ms | 0.001 | 1/1,000 |
| Microsecond | us | 0.000001 | 1/1,000,000 |
| Nanosecond | ns | 0.000000001 | 1/1,000,000,000 |

**Typical latency benchmarks:**

| Operation | Typical latency |
|-----------|----------------|
| L1 cache access | 1 ns |
| L2 cache access | 4 ns |
| L3 cache access | 40 ns |
| Main memory ([[Cache Miss]]) | 100 ns |
| Network hop (same data center) | 500 ns |
| Kernel context switch | 1 to 5 us |
| [[FIX Protocol]] message parse | 2 to 10 us |
| REST API call (co located) | 1 to 10 ms |
| REST API call (cross region) | 50 to 200 ms |

## Prerequisites

- [[Latency]]
- [[Tick to Trade]]

## Related concepts (learn next)

- [[Tick to Trade]] for the end to end latency metric that these units measure
- [[Hot Path]] for identifying which code paths must operate at microsecond or nanosecond scale
- [[Cache Miss]] for understanding why nanosecond level memory access patterns matter
- [[Cache Locality]] for how data layout affects access times at the nanosecond scale
- [[Garbage Collection]] for a common source of millisecond scale latency spikes
- [[Jitter]] for why variance in these timing units matters as much as the average

## Common misconceptions

1. **"Milliseconds and microseconds are basically the same."** A millisecond is 1,000 microseconds. In trading, that is the difference between a competitive quoting engine and one that gets sniped constantly. Never conflate the two.

2. **"Only HFT cares about microseconds."** Any electronic market maker on a competitive venue cares about microseconds. Even a desk targeting 100 microsecond latency needs to think in microsecond terms to stay within budget.

3. **"Nanoseconds only matter for hardware."** Software choices (data structures, memory layout, branch patterns) create nanosecond level differences that compound across millions of operations per second.

## Sources

- Rajiv Ranjan, "Low Latency Trading Infrastructure," Springer
- CME Group, "Co Location Services Technical Guide"
- Intel, "Optimization Reference Manual"
