---
aliases: [hot path, critical path, fast path, latency-sensitive path]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Hot Path

## Definition
The hot path is the code that executes on every single market data tick and order submission, where every nanosecond of [[Latency]] matters. It is the critical execution pipeline from receiving a price update to placing or adjusting a quote. Hot path code is almost always written in C++ or Rust because these languages give the programmer direct control over memory and avoid [[Garbage Collection]] pauses. The hot path typically includes market data parsing, signal evaluation, order construction, and network transmission. Everything on the hot path is optimized ruthlessly: no dynamic [[Memory Allocation]], no system calls, no logging, no branching where avoidable. If a function is not needed on every tick, it belongs on the [[Cold Path]] instead.

## Why it matters (commodities and FX)
In commodity futures and FX, the hot path determines whether your quote arrives at the [[Matching Engine]] before a competitor's. On CME Globex, the difference between being first and second in the queue can be 200 nanoseconds. For a copper [[Market Maker]] on LME or a EUR/USD dealer on EBS, a slow hot path means consistently getting adversely selected: you are filled only when prices move against you. The hot path is where [[Tick to Trade]] latency lives, and reducing it directly improves [[Fill]] quality, tighter [[Bid-Ask Spread]] quoting, and lower [[Slippage]].

## Concrete example
A Brent crude futures market maker on ICE receives a new best bid via the market data feed. The hot path does the following in sequence:

1. Decode the binary market data message (50 nanoseconds)
2. Update the internal order book (30 nanoseconds)
3. Evaluate the pricing model: fair value = mid + skew + inventory adjustment (40 nanoseconds)
4. Construct a new quote: bid at 74.52, offer at 74.54 (20 nanoseconds)
5. Serialize and send the order to the exchange gateway (30 nanoseconds)

Total [[Tick to Trade]]: roughly 170 nanoseconds.

**Win scenario:** The hot path completes in 170 nanoseconds. The quote lands at ICE ahead of 3 competing market makers. The market maker captures the [[Bid-Ask Spread]] on 10 lots of Brent at $10 per tick, netting $200 gross.

**Fail scenario:** A developer adds a logging call to the pricing step. The log triggers a file I/O system call that takes 5,000 nanoseconds. Total tick to trade balloons to 5,170 nanoseconds. The quote arrives last. Over 1 day, the market maker misses 2,000 fills worth $400,000 in gross spread capture.

## Key mechanics and formulas
**Tick to trade (hot path contribution):**
$$T_{hot} = T_{decode} + T_{book\_update} + T_{signal} + T_{order\_build} + T_{send}$$

Where each $T$ is measured in nanoseconds and the goal is to minimize $T_{hot}$.

**Throughput constraint:**
$$\text{Max ticks per second} = \frac{1}{T_{hot}}$$

If $T_{hot}$ = 200 ns, the system can theoretically process 5,000,000 ticks per second.

**Amdahl's Law applied to hot path optimization:**
$$S = \frac{1}{(1 - p) + \frac{p}{s}}$$

Where $S$ is the overall speedup, $p$ is the fraction of time spent in the optimized portion, and $s$ is the speedup of that portion. Optimizing the hot path yields the largest $S$ because $p$ is large.

## Prerequisites
- [[Latency]]
- [[Co-location]]
- [[Matching Engine]]
- [[Tick to Trade]]

## Related concepts (learn next)
- [[Cold Path]] separates non critical work from the hot path to keep it lean.
- [[Cache Locality]] ensures the hot path data fits in CPU cache for fast access.
- [[Branch Prediction]] failures on the hot path cause pipeline stalls that add nanoseconds.
- [[Memory Allocation]] on the hot path is forbidden because malloc is slow and unpredictable.
- [[Garbage Collection]] is why Python and Java are unsuitable for the hot path.
- [[FPGA]] can replace software hot paths entirely by implementing logic in hardware.
- [[Kernel Bypass]] removes the operating system from the network stack on the hot path.

## Common misconceptions
1. **"The hot path is just the fastest code."** Not exactly. The hot path is defined by what runs on every tick. Code can be fast but still belong on the [[Cold Path]] if it only runs periodically (e.g., risk recalculation every 5 seconds).
2. **"Optimizing the hot path means rewriting everything in assembly."** Most gains come from architectural decisions: avoiding [[Memory Allocation]], removing branches, ensuring [[Cache Locality]]. Micro optimization in assembly is the last 1%.
3. **"Adding 1 microsecond does not matter."** In competitive markets like EUR/USD on EBS or ES futures on CME, 1 microsecond is 1,000 nanoseconds. That can be the difference between queue position 1 and queue position 50.

## Sources
- "Trading and Exchanges" by Larry Harris, Oxford University Press
- CME Group, "Co-location and Market Data" technical documentation
- "Low Latency Trading Systems" by Rob Gillen
- Cisco, "Ultra Low Latency Network Design" white paper
