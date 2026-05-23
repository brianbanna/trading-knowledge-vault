---
aliases: [nanosecond, microsecond, millisecond, time units, latency units, ns, us, ms]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Latency Units

## Definition

Latency units are the time measurements used to describe trading system speed. The 3 key units are millisecond (ms, 10^-3 sec), microsecond (us, 10^-6 sec), and nanosecond (ns, 10^-9 sec). Modern electronic trading operates across all 3 scales. Knowing which unit applies to which part of the system is essential for identifying bottlenecks and setting realistic performance targets.

## Why it matters (commodities and FX)

An FX market maker's [[Tick to Trade]] latency decides whether quotes are fresh or [[Stale Quote|stale]]. Knowing "50 microseconds" is fast for a quoting engine but "50 milliseconds" is dangerous prevents miscommunication and bad architecture. When evaluating [[Co-location]] providers, API vendors, or execution platforms, units tell you whether you are comparing apples to apples.

## Concrete example

**Concrete:** Desk builds an [[EUR USD]] quoting system and measures latency at each stage:

| Stage | Latency | Unit |
|-------|---------|------|
| Network hop (co located) | 500 | nanoseconds |
| Market data parsing | 2 | microseconds |
| Pricing engine | 8 | microseconds |
| Risk check | 3 | microseconds |
| Order encoding + send | 1.5 | microseconds |
| **Total [[Tick to Trade]]** | **~15** | **microseconds** |

At 15 microseconds, the desk updates quotes before competitors can [[Sniping|snipe]] stale prices. [[Stale Quote]] events approach zero. A logging library adding a 2 ms (2,000 us) GC pause on the [[Hot Path]] is 130x the entire T2T budget. During the pause, 3 stale quotes get sniped for $28,000.

**Simplified:** A millisecond is 1,000 microseconds. A microsecond is 1,000 nanoseconds. CPU cache and memory operate in nanoseconds. Network hops within a data center operate in microseconds. Internet round trips operate in milliseconds. Adding a few "milliseconds" to a system measured in microseconds is adding hundreds of times the existing budget.

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

- [[Tick to Trade]] for the end to end latency metric these units measure
- [[Hot Path]] for identifying which code paths operate at microsecond or nanosecond scale
- [[Cache Miss]] for why nanosecond memory access patterns matter
- [[Cache Locality]] for how data layout affects access times at nanosecond scale
- [[Garbage Collection]] for a common source of millisecond scale spikes
- [[Jitter]] for why variance in these units matters as much as the average

## Common misconceptions

1. **"Milliseconds and microseconds are basically the same."** A millisecond is 1,000 microseconds. In trading, that is the difference between a competitive engine and one constantly sniped. Never conflate the two.

2. **"Only HFT cares about microseconds."** Any electronic market maker on a competitive venue cares. Even a desk at 100 microsecond target must think in microseconds to stay within budget.

3. **"Nanoseconds only matter for hardware."** Software choices (data structures, memory layout, branch patterns) create nanosecond differences that compound across millions of operations per second.

## Sources

- Rajiv Ranjan, "Low Latency Trading Infrastructure," Springer
- CME Group, "Co Location Services Technical Guide"
- Intel, "Optimization Reference Manual"
