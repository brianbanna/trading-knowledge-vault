---
aliases: [memory allocation, malloc, heap allocation, dynamic allocation, memory pool]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Memory Allocation

## Definition
Memory allocation is reserving space in RAM for data. Dynamic allocation, where the program requests memory at runtime via malloc (C/C++) or new (Java), is slow because the allocator must search for a free block, update bookkeeping, and potentially acquire locks in multithreaded code. A single malloc call costs 100 to 500 ns, and in worst cases (fragmentation, lock contention), several microseconds. Low latency trading systems avoid all dynamic allocation on the [[Hot Path]] by pre allocating fixed size buffers, ring buffers, and memory pools at startup. All memory needed during trading is allocated before market open and nothing is freed until close.

## Why it matters (commodities and FX)
A copper market maker on LME processing 20,000 ticks per second cannot afford 500 ns per tick for allocation. That would consume the entire [[Tick to Trade]] budget. A single unexpected allocation in the pricing loop spikes latency from 200 ns to 2 microseconds, dropping the system from first in queue to last. For FX desks aggregating liquidity across 15 ECN venues, the order management system handles rapid creation and cancellation of thousands of orders per second. Dynamically allocated and freed order objects make the allocator a bottleneck and [[Garbage Collection]] (in managed languages) creates unpredictable pause spikes.

## Concrete example
**Concrete:** Natural gas market maker on CME maintains state for up to 200 active orders. Naive approach: every new order calls `new Order()`, allocating 128 bytes on the heap. Every cancel calls `delete`. At 5,000 order updates per second, the system performs 5,000 malloc/free cycles per second. Each averages 200 ns but occasionally spikes to 5,000 ns under allocator contention. Median T2T: 400 ns, P99: 5,200 ns. Tail latency causes adverse selection during fast markets. Optimized: pool of 500 Order objects in a contiguous array allocated at startup. New order = grab next free slot (single pointer increment, 1 ns). Cancel = return slot to free list. T2T is consistently 200 ns at all percentiles. During a volatile EIA storage report, the system cancels and replaces 300 quotes in 60 microseconds. The naive system takes 1.5 ms for the same operation.

**Simplified:** Asking the operating system for memory takes hundreds of nanoseconds and the time is unpredictable. On a hot path that is unacceptable. The fix is to grab a big chunk of memory once at startup, slice it into a pool of identical objects, and reuse them. No malloc, no free, no surprises.

## Key mechanics and formulas
**Allocation cost comparison:**

| Method | Typical cost | Determinism |
|--------|-------------|-------------|
| Stack allocation | 1 ns | Fully deterministic |
| Pool allocation (pre allocated) | 1 to 5 ns | Deterministic |
| malloc/new (uncontested) | 100 to 500 ns | Variable |
| malloc/new (contested/fragmented) | 1,000 to 10,000 ns | Highly variable |
| Garbage collected (Java/Python) | 0 ns per object, but periodic GC pauses of 1 to 50 ms | Unpredictable |

**Memory pool sizing:**
$$\text{Pool size} = \text{max concurrent objects} \times \text{object size} \times \text{safety factor}$$

Safety factor 2x to 3x. For 200 max orders of 128 bytes:
$$\text{Pool size} = 200 \times 128 \times 2 = 51{,}200 \text{ bytes} = 50 \text{ KB}$$

Fits easily in L2 cache, improving [[Cache Locality]].

**Fragmentation metric:**
$$\text{Fragmentation ratio} = 1 - \frac{\text{largest free block}}{\text{total free memory}}$$

Above 0.3 indicates significant fragmentation that raises allocation latency.

## Prerequisites
- [[Hot Path]]
- [[Cold Path]]
- [[Latency]]
- [[Cache Locality]]

## Related concepts (learn next)
- [[Garbage Collection]] is automatic deallocation that introduces unpredictable pauses.
- [[Hot Path]] must be free of dynamic allocation for deterministic latency.
- [[Cache Locality]] benefits from pool allocation because objects sit contiguous in memory.
- [[Cache Miss]] frequency rises with fragmented memory from scattered allocations.
- [[Lock Free Data Structures]] avoid mutex contention in multithreaded allocators.
- [[Ring Buffer]] is a pre allocated structure for passing data between [[Hot Path]] and [[Cold Path]].
- [[Stack Allocation]] is the fastest method, used for locals with known lifetimes.

## Common misconceptions
1. **"Modern allocators like jemalloc and tcmalloc make malloc fast enough."** They cut average allocation to roughly 50 ns, but tail latency still reaches microseconds under contention. For nanosecond budgets on the [[Hot Path]], 50 ns is too much.
2. **"Pre allocating wastes memory."** A 50 KB pool for orders is trivial against gigabytes of RAM. The waste is negligible, the latency savings are enormous.
3. **"Memory allocation is the same as memory access."** Allocation (reserving space) is 100x slower than accessing existing memory. A [[Cache Miss]] on existing data costs 100 ns. An allocation costs 100 to 500 ns and can destroy cache locality.
4. **"You can just avoid allocation by using global variables."** Globals avoid allocation but destroy modularity and testability. Memory pools give the same performance benefit with better engineering.

## Sources
- "Effective Modern C++" by Scott Meyers, O'Reilly
- "Systems Performance" by Brendan Gregg, Pearson
- glibc malloc documentation
- Google, "tcmalloc: Thread Caching Malloc" design document
