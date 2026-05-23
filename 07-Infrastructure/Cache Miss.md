---
aliases: [cache miss, L1 miss, L2 miss, L3 miss, cache fault]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Cache Miss

## Definition
A cache miss occurs when the CPU requests data not present in its fast cache and must fetch from a slower memory level. L1 miss goes to L2 (roughly 5 ns), L2 miss to L3 (roughly 10 ns), L3 miss to RAM (roughly 100 ns). Each miss stalls the pipeline, doing no useful work during the fetch. On a trading [[Hot Path]], a single miss doubles [[Tick to Trade]]. Minimizing misses through [[Cache Locality]], data structure design, and prefetching is one of the highest impact optimizations in trading system engineering.

## Why it matters (commodities and FX)
Every tick of Brent on ICE or EUR/USD on EBS triggers lookups: order book state, position, model parameters, risk limits. Any of these causing a cache miss stalls the system. A market maker hit by 5 L3 misses per tick adds 500 ns. Where the top 3 firms are separated by 100 ns, 5 cache misses move you from first in queue to last. For commodity spread traders working CME natural gas calendar spreads, misses in the spread calculator make the system miss the fleeting moment when the spread is mispriced.

## Concrete example
**Concrete:** WTI market maker on CME processing 50,000 ticks per second. Per tick, the pricing function reads 3 structures: order book (256 byte contiguous array, always L1, 0 misses), position tracker (64 byte struct, occasional L2 hit, 5 ns), risk limits (heap allocated hash map, 2 L3 misses per tick, 200 ns). Total miss penalty: 200 ns, 60% of the system's 330 ns [[Tick to Trade]]. Developer replaces the risk limits hash map with a flat array indexed by instrument ID. Misses drop to 0. T2T falls 330 to 140 ns. The system wins the CME WTI queue consistently, adding $18,000 per day in spread capture.

**Simplified:** The CPU keeps frequently used data in tiny fast memory (cache). If the data is not there, the CPU pauses up to 100 nanoseconds while fetching from RAM. Pointer chasing through linked lists and large hash tables guarantees misses. Flat arrays guarantee hits. On a hot path, this is the difference between winning and losing.

## Key mechanics and formulas
**Memory hierarchy latencies (modern Intel Xeon):**

| Level | Size | Latency |
|-------|------|---------|
| L1 | 32 KB | 1 ns |
| L2 | 256 KB | 5 ns |
| L3 | 30 MB | 10 ns |
| RAM | 64+ GB | 100 ns |

**Cache miss cost on hot path:**
$$T_{miss\_penalty} = N_{misses} \times T_{level}$$

Where $N_{misses}$ is misses per tick and $T_{level}$ is the latency of the satisfying level.

**Cache miss rate:**
$$\text{Miss rate} = \frac{\text{cache misses}}{\text{total memory accesses}}$$

Target on [[Hot Path]]: below 0.1% (fewer than 1 miss per 1,000 accesses).

**Daily cost of cache misses:**
$$\text{Cost} = N_{ticks/day} \times T_{miss\_penalty} \times \text{opportunity cost per ns}$$

For a CME market maker at 500,000 ticks per day, 200 ns penalty, $0.0001 per ns opportunity cost:
$$\text{Cost} = 500{,}000 \times 200 \times 0.0001 = \$10{,}000 \text{ per day}$$

## Prerequisites
- [[Cache Locality]]
- [[Hot Path]]
- [[Latency]]

## Related concepts (learn next)
- [[Cache Locality]] is the design principle that prevents misses.
- [[Hot Path]] performance is dominated by miss frequency on the critical path.
- [[Memory Allocation]] using pre allocated flat buffers eliminates pointer chasing.
- [[Branch Prediction]] interacts with misses because speculative execution can prefetch, hiding miss latency.
- [[Garbage Collection]] compacts memory, which improves or destroys cache locality depending on the collector.
- [[Co-location]] reduces network latency but cannot fix miss latency, which is internal to the server.
- [[Tick to Trade]] is the end to end metric that miss optimization improves.

## Common misconceptions
1. **"L1 misses are the most important to fix."** L1 misses that hit L2 cost 5 ns. L3 misses to RAM cost 100 ns, 20x more. Focus on eliminating RAM accesses first.
2. **"Prefetching solves all cache miss problems."** Software prefetching hides latency for sequential scans but cannot help with random access patterns like pointer chasing.
3. **"Cache misses only matter for HFT firms."** Any systematic trader backtesting millions of ticks sees 10 to 50x speedup from cache friendly layouts. An 8 hour backtest with poor cache behavior runs in 30 minutes with proper layout.

## Sources
- "What Every Programmer Should Know About Memory" by Ulrich Drepper
- "Computer Architecture: A Quantitative Approach" by Hennessy and Patterson
- Intel, "VTune Profiler" documentation on cache analysis
- "Performance Analysis and Tuning on Modern CPUs" by Denis Bakhvalov
