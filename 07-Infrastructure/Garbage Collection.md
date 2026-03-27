---
aliases: [garbage collection, GC, GC pause, stop-the-world, memory management]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Garbage Collection

## Definition
Garbage collection is the automatic process by which programming languages like Python, Java, and C# reclaim memory that is no longer in use. Instead of the programmer explicitly freeing memory, the runtime periodically scans for objects that have no references and deallocates them. The problem for trading systems is that this scan can trigger a "stop the world" pause where all program threads freeze for milliseconds or even tens of milliseconds. This unpredictable latency spike is why the [[Hot Path]] of trading systems is written in C++ or Rust, languages where the programmer controls [[Memory Allocation]] and deallocation directly. Garbage collection is acceptable on the [[Cold Path]] where occasional pauses do not affect tick level execution.

## Why it matters (commodities and FX)
A GC pause of 10 milliseconds on a EUR/USD market making system means 10,000,000 nanoseconds of blindness. During that time, the system cannot update quotes, cancel stale orders, or react to price moves. If the ECB announces a surprise rate decision and the market moves 50 pips in those 10 milliseconds, every resting order gets adversely selected. For commodity futures on CME or ICE, a GC pause during a volatile USDA crop report or OPEC announcement can result in fills at the worst possible prices. This is why every serious low latency trading firm either avoids GC languages on the [[Hot Path]] or uses extreme tuning (e.g., Java's Zing JVM with pauseless GC).

## Concrete example
A copper market maker on LME uses a Java based trading system. The system quotes bid/offer on LME copper futures with a 2 tick spread ($50 per lot).

**Normal operation:** The system processes ticks in 800 nanoseconds, updates quotes, and captures spread. Java's G1 garbage collector runs minor collections every few seconds with sub millisecond pauses.

**GC disaster scenario:** After 2 hours of trading, enough garbage has accumulated to trigger a full GC collection. The JVM pauses all threads for 15 milliseconds. During this pause:
1. Copper drops $20 per tonne on a surprise China PMI print
2. The system's resting buy orders at the old, higher price get filled: 50 lots at prices $20 above fair value
3. Loss: 50 lots x $20 x 25 tonnes = $25,000 in 15 milliseconds

**Mitigation scenario:** The firm switches the hot path to C++ and keeps Java only for the [[Cold Path]] (risk, reporting). GC pauses now only affect the risk dashboard, not order execution. The same China PMI event occurs, but the C++ hot path cancels stale quotes in 300 nanoseconds. Loss avoided.

## Key mechanics and formulas
**GC pause impact on P&L:**
$$\text{GC cost per pause} = P(\text{adverse move during pause}) \times E[\text{adverse fill size}] \times E[\text{price move}]$$

For a market maker quoting 100 lots on each side with an average GC pause of 10 ms:
$$\text{Expected adverse move in 10 ms} \approx \sigma_{tick} \times \sqrt{\frac{10\text{ ms}}{T_{tick}}}$$

Where $\sigma_{tick}$ is per tick volatility and $T_{tick}$ is the average time between ticks.

**Memory pressure approximation:**
$$\text{GC frequency} \propto \frac{\text{allocation rate}}{\text{heap size}}$$

Higher allocation rates or smaller heaps trigger GC more often.

**Tail latency contribution:**
$$P_{99.9} \text{ latency} = \max(T_{hot}, T_{GC\_pause})$$

Even if median latency is 500 nanoseconds, a single GC pause dominates the 99.9th percentile.

## Prerequisites
- [[Hot Path]]
- [[Cold Path]]
- [[Memory Allocation]]
- [[Latency]]

## Related concepts (learn next)
- [[Hot Path]] must be free of garbage collection to guarantee deterministic latency.
- [[Cold Path]] tolerates GC pauses because it operates on longer timescales.
- [[Memory Allocation]] is the root cause of garbage: every allocation eventually becomes garbage.
- [[Cache Locality]] is disrupted by GC because the collector moves objects in memory during compaction.
- [[Tick to Trade]] latency spikes during GC pauses, destroying execution quality.
- [[Tail Latency]] is dominated by GC pauses in managed language systems.
- [[LMAX Disruptor]] is a Java framework designed to minimize GC by using pre allocated ring buffers.

## Common misconceptions
1. **"Modern GC is fast enough for trading."** For the [[Cold Path]], yes. For the [[Hot Path]], even Java's best garbage collectors (Shenandoah, ZGC) have occasional pauses of hundreds of microseconds. In nanosecond competitive markets, this is disqualifying.
2. **"C++ has no memory management problems."** C++ avoids GC pauses but introduces the risk of memory leaks, use after free bugs, and buffer overflows. The programmer trades automatic safety for deterministic performance.
3. **"Just increase the heap size to avoid GC."** Larger heaps delay GC but make each collection longer when it finally occurs. The tail latency spikes become less frequent but more severe, which is arguably worse for a trading system.
4. **"GC only matters for HFT."** Even a medium frequency commodity spread trader with 100 ms target latency can be hurt by a 50 ms GC pause that arrives at the worst moment, like during a USDA report release.

## Sources
- "Java Performance" by Scott Oaks, O'Reilly
- "Systems Performance" by Brendan Gregg, Pearson
- LMAX Exchange, "LMAX Disruptor" technical paper
- Azul Systems, "Understanding Java Garbage Collection" white paper
