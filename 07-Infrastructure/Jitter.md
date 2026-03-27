---
aliases: [latency jitter, timing jitter, latency variance]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Jitter

## Definition

Jitter is the variance or inconsistency in [[Latency]] over time. If a message normally takes 50 microseconds but occasionally spikes to 500 microseconds, that 10x variation is jitter. A system with high average latency but low jitter is often more manageable than one with low average latency but unpredictable spikes. In trading, jitter can cause missed fills, stale quotes, and unreliable execution timing.

## Why it matters (commodities and FX)

A market maker quoting [[EUR USD]] needs predictable response times to manage [[Stale Quote]] risk. If the system jitters, quotes may linger too long during volatile moments, inviting [[Sniping]]. For commodity traders executing around data releases like the [[EIA Weekly Petroleum Status Report]], a latency spike at the wrong millisecond means the difference between capturing and missing a move. Consistent latency allows strategies to be calibrated reliably; jitter makes calibration impossible.

## Concrete example

A market making desk runs a quoting engine on [[Brent Crude]] futures with median [[Latency]] of 80 microseconds. During normal conditions, the 99th percentile latency is 120 microseconds, so jitter is low (40 microsecond range). The desk calibrates its [[Stale Quote]] timeout at 200 microseconds with comfortable margin.

One day, a garbage collection pause in a downstream logging service causes the 99th percentile to spike to 2,000 microseconds. The quoting engine's prices become stale during volatile moments. A fast algo snipes 3 stale quotes for a combined loss of $45,000 before the [[Kill Switch]] triggers.

**If jitter is controlled:** The desk pre allocates memory, pins threads to cores, and avoids [[Garbage Collection]]. The 99th percentile stays at 130 microseconds. No stale quotes, no losses from sniping.

## Key mechanics and formulas

Jitter = P99 latency minus P50 latency (common practical measure)

Standard deviation of latency samples is the statistical measure:

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

- [[Garbage Collection]] for understanding one of the biggest sources of jitter in managed language systems
- [[Cache Miss]] for how memory access patterns create micro latency spikes
- [[Branch Prediction]] for CPU level sources of timing variance
- [[Hot Path]] for why the critical code path must be jitter free
- [[Kill Switch]] for the emergency mechanism when jitter causes dangerous stale quotes
- [[Co-location]] for how physical proximity reduces both latency and jitter

## Common misconceptions

1. **"Low average latency means low jitter."** A system averaging 20 microseconds but spiking to 5 milliseconds once per second has terrible jitter despite a great average. The tail matters more than the mean.

2. **"Jitter only matters for HFT."** Even a desk with 100 millisecond target latency cares about jitter. If execution timing is unpredictable, [[Slippage]] estimates become unreliable and [[TCA]] analysis is noisy.

3. **"Adding more hardware fixes jitter."** Jitter is often caused by software issues (GC pauses, lock contention, context switches), not raw compute. A faster CPU with the same GC pauses still jitters.

## Sources

- Rajiv Ranjan, "Low Latency Trading Infrastructure," Springer
- Linux Foundation, "Real Time Linux" documentation
- CME Group, "Co Location Services Technical Guide"
