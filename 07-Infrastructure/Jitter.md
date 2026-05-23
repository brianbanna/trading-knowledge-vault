---
aliases: [latency jitter, timing jitter, latency variance]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Jitter

## Definition

Jitter is the variance in [[Latency]] over time. If a message normally takes 50 microseconds but occasionally spikes to 500 microseconds, that 10x variation is jitter. A system with high average latency but low jitter is often more manageable than one with low average but unpredictable spikes. Jitter causes missed fills, stale quotes, and unreliable execution timing.

## Why it matters (commodities and FX)

A market maker quoting [[EUR USD]] needs predictable response times to manage [[Stale Quote]] risk. With jitter, quotes linger during volatile moments and invite [[Sniping]]. For commodity traders executing around the [[EIA Weekly Petroleum Status Report]], a latency spike at the wrong millisecond is the difference between capturing and missing a move. Consistent latency allows strategy calibration. Jitter destroys it.

## Concrete example

**Concrete:** Quoting engine on [[Brent Crude]] futures with median [[Latency]] of 80 microseconds. Normal P99: 120 microseconds (40 microsecond range, low jitter). [[Stale Quote]] timeout calibrated at 200 microseconds with comfortable margin. A garbage collection pause in a downstream logging service spikes P99 to 2,000 microseconds. Quotes go stale during volatile moments. A fast algo snipes 3 stale quotes for $45,000 combined loss before the [[Kill Switch]] triggers. With jitter controlled (pre allocated memory, pinned threads, no [[Garbage Collection]]), P99 stays at 130 microseconds. No stale quotes, no snipes.

**Simplified:** Average latency is not the whole story. What matters is the worst case: how slow do messages get at the 99th percentile? If your engine is usually fast but occasionally freezes for a few milliseconds, those freezes are exactly when fast competitors take your money. Jitter is the freeze, latency is the speed.

## Key mechanics and formulas

Jitter = P99 latency minus P50 latency (common practical measure)

Standard deviation of latency samples (statistical measure):

Jitter (std dev) = sqrt((1/N) * sum((latency_i minus mean_latency)^2))

Where:
- latency_i = individual message round trip time
- mean_latency = average of all samples
- N = number of samples

**Typical targets:**
- P99/P50 ratio below 2x is good
- P99/P50 ratio above 5x indicates a problem
- Tail latency (P99.9) matters most for [[Sniping]] risk

## Prerequisites

- [[Latency]]
- [[Tick to Trade]]
- [[Stale Quote]]

## Related concepts (learn next)

- [[Garbage Collection]] for the biggest source of jitter in managed language systems
- [[Cache Miss]] for how memory access patterns create micro latency spikes
- [[Branch Prediction]] for CPU level sources of timing variance
- [[Hot Path]] for why the critical code path must be jitter free
- [[Kill Switch]] for the emergency mechanism when jitter causes dangerous stale quotes
- [[Co-location]] for how physical proximity reduces both latency and jitter

## Common misconceptions

1. **"Low average latency means low jitter."** A system averaging 20 microseconds but spiking to 5 milliseconds once per second has terrible jitter despite a great average. The tail matters more than the mean.

2. **"Jitter only matters for HFT."** Even a desk at 100 millisecond target latency cares. Unpredictable execution timing makes [[Slippage]] estimates unreliable and [[TCA]] noisy.

3. **"Adding more hardware fixes jitter."** Jitter is often software: GC pauses, lock contention, context switches. A faster CPU with the same GC pauses still jitters.

## Sources

- Rajiv Ranjan, "Low Latency Trading Infrastructure," Springer
- Linux Foundation, "Real Time Linux" documentation
- CME Group, "Co Location Services Technical Guide"
