---
aliases: [memory allocation, malloc, heap allocation, dynamic allocation, memory pool]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Memory Allocation

## Definition
Memory allocation is the process of reserving space in the computer's memory (RAM) for data. Dynamic allocation, where the program requests memory at runtime via functions like malloc (C/C++) or new (Java), is slow because it requires the operating system or memory allocator to search for a free block, update bookkeeping structures, and potentially acquire locks in a multithreaded environment. A single malloc call can take 100 to 500 nanoseconds, and in worst cases (memory fragmentation, lock contention), several microseconds. In low latency trading systems, the [[Hot Path]] avoids all dynamic allocation by pre allocating fixed size buffers, ring buffers, and memory pools at startup. All memory needed during trading is allocated before the market opens, and nothing is allocated or freed until the market closes.

## Why it matters (commodities and FX)
A copper market maker on LME processing 20,000 ticks per second cannot afford 500 nanoseconds per tick for memory allocation. That would consume the entire [[Tick to Trade]] budget. Even a single unexpected allocation in the pricing loop can spike latency from 200 nanoseconds to 2 microseconds, moving the system from first in queue to last. For FX desks aggregating liquidity across 15 ECN venues, the order management system must handle rapid creation and cancellation of thousands of orders per second. If each order object is dynamically allocated and freed, the allocator becomes a bottleneck and [[Garbage Collection]] (in managed languages) creates unpredictable pause spikes.

## Concrete example
A natural gas futures market maker on CME processes ticks and sends quote updates. The order management system must maintain state for up to 200 active orders simultaneously.

**Naive approach (dynamic allocation):**
Every new order calls `new Order()`, allocating 128 bytes on the heap. Every cancelled order calls `delete`. At 5,000 order updates per second, the system performs 5,000 malloc/free cycles per second. Each takes 200 nanoseconds on average, but occasionally 5,000 nanoseconds due to allocator lock contention.

**Result:** Median tick to trade is 400 nanoseconds, but 99th percentile is 5,200 nanoseconds. The tail latency causes the system to be adversely selected during fast markets (exactly when it matters most).

**Optimized approach (pre allocated pool):**
At startup, the system allocates a pool of 500 Order objects in a contiguous array. When a new order is needed, the system grabs the next free slot from the pool (a single pointer increment, roughly 1 nanosecond). When an order is cancelled, the slot is returned to the free list.

**Win scenario:** Tick to trade is consistently 200 nanoseconds at all percentiles. No tail spikes. During a volatile EIA storage report, the system cancels and replaces 300 quotes in 60 microseconds. The naive system would take 1.5 milliseconds for the same operation.

**Fail scenario:** A developer adds a "small" logging feature that creates a std::string per tick to format the log message. Each string construction allocates 50 to 200 bytes dynamically. The system's median latency barely changes, but the 99.99th percentile explodes to 50 microseconds. It takes 2 weeks to identify the allocation as the cause.

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

Safety factor is typically 2x to 3x. For 200 max orders of 128 bytes:
$$\text{Pool size} = 200 \times 128 \times 2 = 51{,}200 \text{ bytes} = 50 \text{ KB}$$

This easily fits in L2 cache, further improving [[Cache Locality]].

**Fragmentation metric:**
$$\text{Fragmentation ratio} = 1 - \frac{\text{largest free block}}{\text{total free memory}}$$

Values above 0.3 indicate significant fragmentation that will increase allocation latency.

## Prerequisites
- [[Hot Path]]
- [[Cold Path]]
- [[Latency]]
- [[Cache Locality]]

## Related concepts (learn next)
- [[Garbage Collection]] is automatic memory deallocation that introduces unpredictable pauses.
- [[Hot Path]] must be completely free of dynamic memory allocation for deterministic latency.
- [[Cache Locality]] benefits from pool allocation because objects are contiguous in memory.
- [[Cache Miss]] frequency increases with fragmented memory from scattered allocations.
- [[Lock Free Data Structures]] avoid mutex contention in multithreaded allocators.
- [[Ring Buffer]] is a common pre allocated structure for passing data between the [[Hot Path]] and [[Cold Path]].
- [[Stack Allocation]] is the fastest allocation method, used for local variables with known lifetimes.

## Common misconceptions
1. **"Modern allocators like jemalloc and tcmalloc make malloc fast enough."** They reduce average allocation time to roughly 50 nanoseconds, but tail latency still reaches microseconds under contention. For nanosecond budgets on the [[Hot Path]], even 50 nanoseconds is too much.
2. **"Pre allocating wastes memory."** A pool of 50 KB for order objects is trivial compared to the gigabytes of RAM available. The "waste" is negligible, and the latency savings are enormous.
3. **"Memory allocation is the same as memory access."** Allocation (reserving new space) is 100x slower than accessing already allocated memory. A [[Cache Miss]] on existing data costs 100 nanoseconds. An allocation costs 100 to 500 nanoseconds plus potentially destroys cache locality.
4. **"You can just avoid allocation by using global variables."** Global variables avoid allocation but destroy code modularity and testability. Memory pools provide the same performance benefit with better software engineering.

## Sources
- "Effective Modern C++" by Scott Meyers, O'Reilly
- "Systems Performance" by Brendan Gregg, Pearson
- glibc malloc documentation
- Google, "tcmalloc: Thread Caching Malloc" design document
