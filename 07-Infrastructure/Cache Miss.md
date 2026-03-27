---
aliases: [cache miss, L1 miss, L2 miss, L3 miss, cache fault]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Cache Miss

## Definition
A cache miss occurs when the CPU requests data that is not present in its fast cache and must fetch it from a slower level of the memory hierarchy. An L1 cache miss forces a lookup in L2 (roughly 5 nanoseconds), an L2 miss goes to L3 (roughly 10 nanoseconds), and an L3 miss goes all the way to main RAM (roughly 100 nanoseconds). Each miss stalls the CPU pipeline, meaning no useful work is done during the fetch. In high frequency and low latency trading, a single cache miss on the [[Hot Path]] can double the [[Tick to Trade]] time. Minimizing cache misses through [[Cache Locality]], data structure design, and prefetching is one of the most impactful optimizations in trading system engineering.

## Why it matters (commodities and FX)
Every tick of Brent crude on ICE or EUR/USD on EBS triggers a cascade of lookups: order book state, position, model parameters, risk limits. If any of these data structures cause a cache miss, the system stalls. A market maker that suffers 5 L3 misses per tick adds 500 nanoseconds to its response time. In a competitive environment where the top 3 firms are separated by 100 nanoseconds, those 5 cache misses move you from first in queue to last. For commodity spread traders working calendar spreads on CME natural gas, cache misses in the spread calculator can cause the system to miss the fleeting moment when the spread is mispriced.

## Concrete example
A WTI crude oil market maker on CME processes 50,000 ticks per second during active US hours. The pricing function reads 3 data structures on every tick:

1. **Order book** (contiguous array, 256 bytes): Always in L1 cache. 0 misses.
2. **Position tracker** (contiguous struct, 64 bytes): Usually in L1. Occasional L1 miss, hit in L2. Cost: 5 nanoseconds when missed.
3. **Risk limits** (hash map with heap allocated nodes): Pointer chasing causes 2 L3 misses per tick on average. Cost: 200 nanoseconds per tick.

**Total cache miss penalty per tick:** roughly 200 nanoseconds, which is 60% of the system's 330 nanosecond [[Tick to Trade]] time.

**Win scenario (after optimization):** The developer replaces the risk limits hash map with a flat array indexed by instrument ID. Cache misses drop to 0. Tick to trade falls from 330 to 140 nanoseconds. The system now consistently wins the queue for CME WTI, adding $18,000 per day in spread capture.

**Fail scenario:** The developer adds a per tick lookup into a large std::unordered_map containing 10,000 instrument parameters. The hash table is 2 MB (too large for L1/L2). Every tick triggers 3 to 5 L3 misses. Tick to trade jumps from 140 to 700 nanoseconds. The system loses queue priority on every fill.

## Key mechanics and formulas
**Memory hierarchy latencies (approximate, modern Intel Xeon):**

| Level | Size | Latency |
|-------|------|---------|
| L1 | 32 KB | 1 ns |
| L2 | 256 KB | 5 ns |
| L3 | 30 MB | 10 ns |
| RAM | 64+ GB | 100 ns |

**Cache miss cost on hot path:**
$$T_{miss\_penalty} = N_{misses} \times T_{level}$$

Where $N_{misses}$ is the number of misses per tick and $T_{level}$ is the latency of the level that eventually satisfies the request.

**Cache miss rate:**
$$\text{Miss rate} = \frac{\text{cache misses}}{\text{total memory accesses}}$$

Target for [[Hot Path]]: miss rate below 0.1% (fewer than 1 miss per 1,000 accesses).

**Daily cost of cache misses:**
$$\text{Cost} = N_{ticks/day} \times T_{miss\_penalty} \times \text{opportunity cost per nanosecond}$$

For a CME market maker processing 500,000 ticks per day with 200 ns penalty and $0.0001 per nanosecond opportunity cost:
$$\text{Cost} = 500{,}000 \times 200 \times 0.0001 = \$10{,}000 \text{ per day}$$

## Prerequisites
- [[Cache Locality]]
- [[Hot Path]]
- [[Latency]]

## Related concepts (learn next)
- [[Cache Locality]] is the design principle that prevents cache misses by keeping data contiguous.
- [[Hot Path]] performance is dominated by cache miss frequency on the critical execution path.
- [[Memory Allocation]] using pre allocated flat buffers eliminates pointer chasing that causes misses.
- [[Branch Prediction]] interacts with cache misses because speculative execution can prefetch data, hiding miss latency.
- [[Garbage Collection]] compacts memory, which paradoxically can improve or destroy cache locality depending on the collector.
- [[Co-location]] reduces network latency but cannot fix cache miss latency, which is internal to the server.
- [[Tick to Trade]] is the end to end metric that cache miss optimization directly improves.

## Common misconceptions
1. **"L1 misses are the most important to fix."** L1 misses that hit in L2 only cost 5 nanoseconds. L3 misses that go to RAM cost 100 nanoseconds, 20x more. Focus optimization effort on eliminating RAM accesses first.
2. **"Prefetching solves all cache miss problems."** Software prefetching can hide latency for predictable access patterns (sequential array scans) but cannot help with random access patterns like pointer chasing through linked data structures.
3. **"Cache misses only matter for HFT firms."** Any systematic trader running a backtest over millions of ticks will see 10x to 50x speedup from cache friendly data layouts. A backtest that takes 8 hours with poor cache behavior might take 30 minutes with proper layout.

## Sources
- "What Every Programmer Should Know About Memory" by Ulrich Drepper
- "Computer Architecture: A Quantitative Approach" by Hennessy and Patterson
- Intel, "VTune Profiler" documentation on cache analysis
- "Performance Analysis and Tuning on Modern CPUs" by Denis Bakhvalov
