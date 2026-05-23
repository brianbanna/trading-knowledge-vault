---
aliases: [cache locality, spatial locality, temporal locality, memory locality, data locality]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Cache Locality

## Definition
Cache locality is the principle of organizing data so the CPU accesses it from fast cache (L1, L2, L3) rather than slow main memory. Two flavors: spatial locality stores related data contiguously so loading 1 piece pulls neighbors into the cache line automatically; temporal locality accesses the same data repeatedly within a short window so it stays cached. Scattered data triggers [[Cache Miss]]es that stall the CPU for roughly 100 nanoseconds each. On a trading [[Hot Path]], poor cache locality multiplies [[Tick to Trade]] by 10x. Cache friendly data structures (arrays of structs, struct of arrays, pre allocated buffers) are core to low latency system design.

## Why it matters (commodities and FX)
A commodity market maker pricing Brent crude reads the top 5 levels of the order book on every tick. Stored contiguously, those 5 price/quantity pairs fit in a single 64 byte cache line and load in 1 nanosecond from L1. Stored as linked list nodes scattered across the heap, each access triggers a [[Cache Miss]] costing 100 nanoseconds, turning a 5 ns operation into 500 ns. For an FX desk quoting EUR/USD across 10 venues, the pricing loop touches venue state, position, and parameters on every tick. Cache friendly layout decides between 200 ns and 2 microsecond quotes.

## Concrete example
**Concrete:** EUR/USD market maker on EBS, internal order book with 10 levels per side. The pricing model reads all 20 levels per tick to compute [[VWAP]] weighted fair value. Array of structs (20 x 16 bytes = 320 bytes, 5 cache lines): reads in 5 ns from L1. Pricing loop completes in 50 ns total. Quote reaches EBS ahead of 8 out of 10 competitors. Daily capture: 15,000 extra spread crosses worth $75,000. A developer then refactors the book to std::map for "cleaner code". Tree nodes are separately allocated. Cache locality dies. Tick to trade jumps from 200 ns to 1,800 ns. Queue position drops from 2 to 9. Daily P&L falls $40,000.

**Simplified:** The CPU has a tiny stash of nearby memory (cache) that it reads in 1 nanosecond. Main RAM takes 100 nanoseconds. If your data sits side by side in memory, the CPU pulls it from cache. If it is scattered, the CPU stalls 100 ns per access. The cure is arrays, not linked structures, and packing only what the hot path needs.

## Key mechanics and formulas
**Cache line utilization:**
$$\text{Utilization} = \frac{\text{useful bytes per cache line}}{64 \text{ bytes}}$$

Maximize by packing only data the [[Hot Path]] needs into each cache line.

**Effective memory access time:**
$$T_{eff} = h \times T_{cache} + (1 - h) \times T_{RAM}$$

Where $h$ is the cache hit rate, $T_{cache}$ is roughly 1 ns (L1), $T_{RAM}$ is roughly 100 ns. At $h = 0.95$, $T_{eff} = 5.95$ ns. At $h = 0.80$, $T_{eff} = 20.8$ ns, a 3.5x slowdown.

**Working set size rule:**
$$\text{If working set} \leq \text{L1 size (32 KB typical)}: \text{all accesses at L1 speed}$$
$$\text{If working set} \leq \text{L3 size (30 MB typical)}: \text{most accesses at L3 speed (10 ns)}$$
$$\text{If working set} > \text{L3 size}: \text{frequent RAM accesses (100 ns)}$$

## Prerequisites
- [[Hot Path]]
- [[Cache Miss]]
- [[Latency]]

## Related concepts (learn next)
- [[Cache Miss]] is the direct consequence of poor cache locality, adding 100 ns per miss.
- [[Hot Path]] performance depends on keeping working data cache resident.
- [[Memory Allocation]] patterns determine whether data ends up contiguous or scattered.
- [[Branch Prediction]] interacts with cache locality because mispredicted branches prefetch wrong cache lines.
- [[FPGA]] sidesteps CPU cache entirely by implementing logic in hardware.
- [[Struct of Arrays]] layout improves spatial locality for columnar data access.
- [[Lock Free Data Structures]] must be cache line aligned to avoid false sharing between cores.

## Common misconceptions
1. **"Cache locality only matters at nanosecond scale."** Even a Python backtester benefits from cache friendly layouts (NumPy arrays vs lists of objects). A 10 year tick backtest runs 50x faster with proper layout.
2. **"More RAM is the same as better cache."** RAM is roughly 100x slower than L1. Adding RAM does not help cache unfriendly access. The bottleneck is latency, not capacity.
3. **"The compiler optimizes cache locality automatically."** Compilers reorder some operations but cannot change data structure layout. The programmer must choose arrays over linked lists, pack structs, and align to cache line boundaries.

## Sources
- "Computer Architecture: A Quantitative Approach" by Hennessy and Patterson
- "What Every Programmer Should Know About Memory" by Ulrich Drepper (2007)
- Intel, "Intel 64 and IA 32 Architectures Optimization Reference Manual"
- "Trading and Exchanges" by Larry Harris (market microstructure context)
