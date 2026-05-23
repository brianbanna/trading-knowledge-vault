---
aliases: [garbage collection, GC, GC pause, stop-the-world, memory management]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Garbage Collection

## Definition
Garbage collection is the automatic process by which Python, Java, and C# reclaim memory no longer in use. Instead of the programmer explicitly freeing memory, the runtime periodically scans for unreferenced objects and deallocates them. The problem for trading systems is that the scan triggers a "stop the world" pause freezing all threads for milliseconds or tens of milliseconds. This unpredictable spike is why the [[Hot Path]] is written in C++ or Rust, where the programmer controls [[Memory Allocation]] and deallocation directly. GC is acceptable on the [[Cold Path]] where pauses do not affect tick level execution.

## Why it matters (commodities and FX)
A 10 ms GC pause on a EUR/USD market maker means 10,000,000 nanoseconds of blindness. During that time the system cannot update quotes, cancel stale orders, or react. If the ECB announces a surprise rate decision and the market moves 50 pips, every resting order gets adversely selected. For commodity futures on CME or ICE, a GC pause during a volatile USDA crop report or OPEC announcement produces fills at worst possible prices. This is why every serious low latency firm either avoids GC languages on the hot path or uses extreme tuning (Java's Zing JVM with pauseless GC).

## Concrete example
**Concrete:** Copper market maker on LME runs a Java system quoting bid/offer with a 2 tick spread ($50/lot). Normal: 800 ns per tick processing, G1 collector runs minor collections every few seconds with sub millisecond pauses. After 2 hours, accumulated garbage triggers a full collection. JVM pauses all threads for 15 ms. Copper drops $20/tonne on a surprise China PMI print. The system's resting buys at the old, higher price fill: 50 lots at prices $20 above fair value. Loss: 50 x $20 x 25 = $25,000 in 15 ms. Mitigation: move the hot path to C++, keep Java only for cold path (risk, reporting). GC pauses now only affect the risk dashboard, not order execution. Next PMI event, C++ cancels stale quotes in 300 ns. No loss.

**Simplified:** In languages like Java and Python, you do not free memory yourself. The runtime does it periodically. When it runs, every thread freezes for milliseconds. On a hot path, those frozen milliseconds are when the market is moving and your stale orders get hit. The fix is to write the hot path in a language without GC (C++, Rust) and accept GC only where pauses do not matter.

## Key mechanics and formulas
**GC pause impact on P&L:**
$$\text{GC cost per pause} = P(\text{adverse move during pause}) \times E[\text{adverse fill size}] \times E[\text{price move}]$$

For a market maker quoting 100 lots per side with 10 ms average pause:
$$\text{Expected adverse move in 10 ms} \approx \sigma_{tick} \times \sqrt{\frac{10\text{ ms}}{T_{tick}}}$$

Where $\sigma_{tick}$ is per tick volatility and $T_{tick}$ is average time between ticks.

**Memory pressure approximation:**
$$\text{GC frequency} \propto \frac{\text{allocation rate}}{\text{heap size}}$$

Higher allocation rates or smaller heaps trigger GC more often.

**Tail latency contribution:**
$$P_{99.9} \text{ latency} = \max(T_{hot}, T_{GC\_pause})$$

Median latency may be 500 ns, but a single GC pause dominates the 99.9th percentile.

## Prerequisites
- [[Hot Path]]
- [[Cold Path]]
- [[Memory Allocation]]
- [[Latency]]

## Related concepts (learn next)
- [[Hot Path]] must be GC free for deterministic latency.
- [[Cold Path]] tolerates pauses because it operates on longer timescales.
- [[Memory Allocation]] is the root of garbage: every allocation becomes garbage.
- [[Cache Locality]] is disrupted by GC because the collector moves objects during compaction.
- [[Tick to Trade]] latency spikes during pauses, destroying execution quality.
- [[Tail Latency]] is dominated by GC pauses in managed language systems.
- [[LMAX Disruptor]] is a Java framework that minimizes GC via pre allocated ring buffers.

## Common misconceptions
1. **"Modern GC is fast enough for trading."** For the [[Cold Path]], yes. For the [[Hot Path]], even Java's best collectors (Shenandoah, ZGC) have occasional hundred microsecond pauses. In nanosecond competitive markets, that is disqualifying.
2. **"C++ has no memory management problems."** C++ avoids GC pauses but introduces leaks, use after free, and buffer overflows. The programmer trades automatic safety for deterministic performance.
3. **"Just increase the heap size to avoid GC."** Larger heaps delay GC but make each collection longer. Tail spikes become less frequent but more severe, arguably worse for a trading system.
4. **"GC only matters for HFT."** Even a medium frequency commodity spread trader at 100 ms target latency gets hurt by a 50 ms pause during a USDA release.

## Sources
- "Java Performance" by Scott Oaks, O'Reilly
- "Systems Performance" by Brendan Gregg, Pearson
- LMAX Exchange, "LMAX Disruptor" technical paper
- Azul Systems, "Understanding Java Garbage Collection" white paper
