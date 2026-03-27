---
aliases: [cache locality, spatial locality, temporal locality, memory locality, data locality]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Cache Locality

## Definition
Cache locality is the principle of organizing data in memory so that the CPU can access it from its fast cache (L1, L2, L3) rather than slow main memory (RAM). There are 2 types: spatial locality means storing related data contiguously so that loading 1 piece pulls nearby pieces into the cache line automatically, and temporal locality means accessing the same data repeatedly within a short time window so it stays in cache. When data is scattered across memory, the CPU suffers [[Cache Miss]]es and stalls for roughly 100 nanoseconds per miss. In a trading system's [[Hot Path]], poor cache locality can multiply [[Tick to Trade]] latency by 10x or more. Designing data structures for cache friendliness (arrays of structs, struct of arrays, pre allocated buffers) is a core skill in low latency system design.

## Why it matters (commodities and FX)
A commodity market maker pricing Brent crude needs to read the top 5 levels of the order book on every tick. If those 5 price/quantity pairs are stored in a contiguous array, they fit in a single 64 byte cache line and load in roughly 1 nanosecond from L1. If they are stored as linked list nodes scattered across the heap, each access triggers a [[Cache Miss]] costing 100 nanoseconds, turning a 5 nanosecond operation into a 500 nanosecond one. For an FX desk quoting EUR/USD across 10 venues, the pricing loop touches venue state, position, and parameter data on every tick. Cache friendly layout of this data directly determines whether the system can quote in 200 nanoseconds or 2 microseconds.

## Concrete example
An EUR/USD market maker on EBS maintains an internal order book with 10 price levels on each side. The pricing model reads all 20 levels on every tick to compute [[VWAP]] weighted fair value.

**Cache friendly design (array of structs):**
All 20 levels stored as a contiguous array of {price, quantity} pairs. Total size: 20 x 16 bytes = 320 bytes. Fits in 5 cache lines. Time to read all levels: roughly 5 nanoseconds from L1 cache.

**Cache unfriendly design (linked list):**
Each level is a heap allocated node with a pointer to the next. Nodes are scattered across memory. Reading 20 levels requires 20 pointer dereferences, each potentially a [[Cache Miss]]. Time to read all levels: roughly 500 to 2,000 nanoseconds depending on cache state.

**Win scenario:** The cache friendly system completes the pricing loop in 50 nanoseconds total. The quote reaches EBS before 8 out of 10 competitors. Over 1 trading day, the system captures 15,000 additional spread crosses worth $75,000.

**Fail scenario:** A developer refactors the order book to use a std::map (red black tree) for "cleaner code." Each tree node is separately allocated. Cache locality is destroyed. Tick to trade increases from 200 nanoseconds to 1,800 nanoseconds. The system drops from position 2 to position 9 in the queue. Daily P&L falls by $40,000.

## Key mechanics and formulas
**Cache line utilization:**
$$\text{Utilization} = \frac{\text{useful bytes per cache line}}{64 \text{ bytes}}$$

Maximizing utilization means packing only the data the [[Hot Path]] needs into each cache line.

**Effective memory access time:**
$$T_{eff} = h \times T_{cache} + (1 - h) \times T_{RAM}$$

Where $h$ is the cache hit rate, $T_{cache}$ is roughly 1 nanosecond (L1), and $T_{RAM}$ is roughly 100 nanoseconds. At $h = 0.95$, $T_{eff} = 0.95 \times 1 + 0.05 \times 100 = 5.95$ ns. At $h = 0.80$, $T_{eff} = 20.8$ ns, a 3.5x slowdown.

**Working set size rule:**
$$\text{If working set} \leq \text{L1 size (32 KB typical)}: \text{all accesses at L1 speed}$$
$$\text{If working set} \leq \text{L3 size (30 MB typical)}: \text{most accesses at L3 speed (10 ns)}$$
$$\text{If working set} > \text{L3 size}: \text{frequent RAM accesses (100 ns)}$$

## Prerequisites
- [[Hot Path]]
- [[Cache Miss]]
- [[Latency]]

## Related concepts (learn next)
- [[Cache Miss]] is the direct consequence of poor cache locality, adding 100 nanoseconds per miss.
- [[Hot Path]] performance depends heavily on keeping its working data cache resident.
- [[Memory Allocation]] patterns determine whether data ends up contiguous or scattered.
- [[Branch Prediction]] interacts with cache locality because mispredicted branches can prefetch the wrong cache lines.
- [[FPGA]] sidesteps CPU cache entirely by implementing logic directly in hardware.
- [[Struct of Arrays]] layout is a common technique to improve spatial locality for columnar data access.
- [[Lock Free Data Structures]] must be designed with cache line alignment to avoid false sharing between CPU cores.

## Common misconceptions
1. **"Cache locality only matters at nanosecond scale."** Even a Python backtesting system benefits from cache friendly data layouts (NumPy arrays vs lists of objects). A backtest over 10 years of tick data can be 50x faster with proper layout.
2. **"More RAM is the same as better cache."** RAM is roughly 100x slower than L1 cache. Adding more RAM does not help if the access pattern is cache unfriendly. The bottleneck is latency, not capacity.
3. **"The compiler optimizes cache locality automatically."** Compilers can reorder some operations but cannot change data structure layout. The programmer must choose arrays over linked lists, pack structs, and align data to cache line boundaries.

## Sources
- "Computer Architecture: A Quantitative Approach" by Hennessy and Patterson
- "What Every Programmer Should Know About Memory" by Ulrich Drepper (2007)
- Intel, "Intel 64 and IA 32 Architectures Optimization Reference Manual"
- "Trading and Exchanges" by Larry Harris (market microstructure context)
