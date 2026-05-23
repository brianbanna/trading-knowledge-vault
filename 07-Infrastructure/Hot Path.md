---
aliases: [hot path, critical path, fast path, latency-sensitive path]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Hot Path

## Definition
The hot path is the code that executes on every market data tick and order submission, where every nanosecond of [[Latency]] matters. It is the critical pipeline from receiving a price update to placing or adjusting a quote. Hot path code is almost always C++ or Rust because these give direct memory control and avoid [[Garbage Collection]] pauses. The hot path includes market data parsing, signal evaluation, order construction, and network transmission. Everything on the hot path is ruthlessly optimized: no dynamic [[Memory Allocation]], no system calls, no logging, no avoidable branching. Anything not needed per tick belongs on the [[Cold Path]].

## Why it matters (commodities and FX)
In commodity futures and FX, the hot path decides whether your quote reaches the [[Matching Engine]] ahead of a competitor's. On CME Globex, first vs second in the queue is 200 nanoseconds. For a copper [[Market Maker]] on LME or EUR/USD dealer on EBS, a slow hot path means consistent adverse selection: you only fill when prices move against you. The hot path is where [[Tick to Trade]] latency lives. Reducing it improves [[Fill]] quality, lets you quote tighter [[Bid-Ask Spread]], and cuts [[Slippage]].

## Concrete example
**Concrete:** A Brent crude market maker on ICE receives a new best bid via market data. The hot path executes in sequence: decode the binary message (50 ns), update the internal book (30 ns), evaluate pricing (fair = mid + skew + inventory, 40 ns), construct a quote (bid 74.52, offer 74.54, 20 ns), serialize and send (30 ns). Total [[Tick to Trade]]: 170 ns. The quote lands ahead of 3 competitors. The maker captures spread on 10 lots at $10/tick: $200 gross per cycle. A developer adds a "small" logging call on the pricing step. The log triggers a file I/O system call costing 5,000 ns. Total T2T balloons to 5,170 ns. The quote arrives last every cycle. Daily miss: 2,000 fills, $400,000 in gross spread.

**Simplified:** The hot path is the code that runs on every single price update. If you want to be first in the queue, this code has to be ruthlessly fast: no memory allocation, no logging, no system calls, no slow library calls. Anything that runs occasionally (risk checks, P&L, reporting) goes somewhere else. The discipline is keeping this path lean.

## Key mechanics and formulas
**Tick to trade (hot path contribution):**
$$T_{hot} = T_{decode} + T_{book\_update} + T_{signal} + T_{order\_build} + T_{send}$$

Where each $T$ is in nanoseconds and the goal is to minimize $T_{hot}$.

**Throughput constraint:**
$$\text{Max ticks per second} = \frac{1}{T_{hot}}$$

If $T_{hot}$ = 200 ns, the system can theoretically process 5,000,000 ticks per second.

**Amdahl's Law applied to hot path:**
$$S = \frac{1}{(1 - p) + \frac{p}{s}}$$

Where $S$ is overall speedup, $p$ is the time fraction in the optimized portion, $s$ is the speedup of that portion. Hot path optimization yields the largest $S$ because $p$ is large.

## Prerequisites
- [[Latency]]
- [[Co-location]]
- [[Matching Engine]]
- [[Tick to Trade]]

## Related concepts (learn next)
- [[Cold Path]] separates non critical work from the hot path to keep it lean.
- [[Cache Locality]] keeps the hot path's working data in CPU cache.
- [[Branch Prediction]] failures on the hot path cause pipeline stalls.
- [[Memory Allocation]] on the hot path is forbidden: malloc is slow and unpredictable.
- [[Garbage Collection]] is why Python and Java are unsuitable for the hot path.
- [[FPGA]] can replace software hot paths by implementing logic in hardware.
- [[Kernel Bypass]] removes the operating system from the network stack on the hot path.

## Common misconceptions
1. **"The hot path is just the fastest code."** Not exactly. The hot path is defined by what runs on every tick. Code can be fast but belong on the [[Cold Path]] if it only runs periodically (risk recalc every 5 seconds).
2. **"Optimizing the hot path means rewriting everything in assembly."** Most gains come from architecture: avoiding [[Memory Allocation]], removing branches, ensuring [[Cache Locality]]. Assembly micro optimization is the last 1%.
3. **"Adding 1 microsecond does not matter."** In competitive markets like EUR/USD on EBS or ES futures on CME, 1 microsecond is 1,000 nanoseconds. That is the difference between queue position 1 and 50.

## Sources
- "Trading and Exchanges" by Larry Harris, Oxford University Press
- CME Group, "Co-location and Market Data" technical documentation
- "Low Latency Trading Systems" by Rob Gillen
- Cisco, "Ultra Low Latency Network Design" white paper
