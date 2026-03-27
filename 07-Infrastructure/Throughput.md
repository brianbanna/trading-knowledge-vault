---
aliases: [message rate, messages per second, MPS, bandwidth capacity]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Throughput

## Definition

Throughput is the number of messages a trading system can process per unit of time, typically measured in messages per second (MPS). While [[Latency]] measures how fast a single message is processed, throughput measures how many messages can be handled simultaneously. A system might process each message in 10 microseconds (low latency) but only handle 50,000 messages per second (limited throughput). Both dimensions matter: latency for speed, throughput for capacity.

## Why it matters (commodities and FX)

During high activity periods (data releases, central bank announcements, market opens), message rates spike dramatically. An FX market data feed can produce over 1 million price updates per second across all pairs. A quoting engine needs enough throughput to process all incoming data, recalculate prices, and publish updated quotes without falling behind. If throughput is insufficient, the system queues messages, which increases effective [[Latency]] and leads to [[Stale Quote|stale quotes]].

## Concrete example

A commodity trading desk processes market data for 200 instruments across CME, ICE, and LME. Normal throughput: 50,000 messages per second. The system is designed for 200,000 MPS.

**Normal conditions:** 50,000 MPS flows through easily. Processing queue is empty. [[Latency]] stays at the designed 15 microsecond level.

**Success case (high throughput headroom):** OPEC announces an emergency meeting. Message rates spike to 180,000 MPS across all energy contracts. The system handles the spike with headroom. Quotes stay fresh. The desk avoids [[Stale Quote]] losses.

**Failure case (throughput bottleneck):** A desk with the same 200 instruments but only 80,000 MPS capacity hits the OPEC spike. Messages queue up. By the time the system processes a [[Brent Crude]] update, it is 500 milliseconds old. Competitors [[Sniping|snipe]] 8 stale quotes. The [[Kill Switch]] triggers to prevent further losses. The desk misses 20 minutes of trading during the most profitable period of the year.

## Key mechanics and formulas

**Throughput capacity:**
Max throughput = 1 / processing_time_per_message

If each message takes 10 microseconds: max throughput = 100,000 MPS

**Queue buildup (Little's Law):**
Queue length = arrival_rate * processing_time

If arrival rate = 150,000 MPS and processing capacity = 100,000 MPS:
Excess rate = 50,000 MPS. Queue grows by 50,000 messages per second. After 1 second, 50,000 messages are waiting, each delayed by up to 500 milliseconds.

**Throughput vs. latency trade off:**
At low utilization (arrival rate << capacity): latency is stable and low.
At high utilization (arrival rate approaching capacity): latency spikes due to queuing.

**Rule of thumb:** Design for 3x to 5x normal peak throughput to handle spikes without queuing.

## Prerequisites

- [[Latency]]
- [[Data Feed]]
- [[Hot Path]]

## Related concepts (learn next)

- [[Latency]] for the per message speed dimension (throughput's complement)
- [[Jitter]] for how throughput bottlenecks cause latency variance
- [[Data Feed]] for the primary source of high throughput message flow
- [[Hot Path]] for the code that must sustain high throughput under load
- [[Garbage Collection]] for a common cause of throughput collapse (GC pauses block processing)
- [[Kill Switch]] for what happens when throughput failure makes quoting unsafe

## Common misconceptions

1. **"High throughput means low latency."** A system can process 1 million MPS but take 10 milliseconds per message (parallel processing). Throughput and latency are independent dimensions.

2. **"My system handles peak volume, so throughput is fine."** Peak volume today is not peak volume during the next crisis. Design for 3x to 5x the highest observed rate. The 2020 oil crash saw CME energy message rates 8x above normal.

3. **"Throughput problems are always hardware problems."** Often the bottleneck is software: lock contention, memory allocation on the [[Hot Path]], or [[Garbage Collection]] pauses. Profiling the software is the first step, not buying faster hardware.

## Sources

- Rajiv Ranjan, "Low Latency Trading Infrastructure," Springer
- CME Group, "Market Data Feed Specifications" (message rate statistics)
- Hennessy, J. and Patterson, D., "Computer Architecture: A Quantitative Approach"
