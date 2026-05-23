---
aliases: [message rate, messages per second, MPS, bandwidth capacity]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Throughput

## Definition

Throughput is the number of messages a trading system processes per unit of time, measured in messages per second (MPS). [[Latency]] measures speed per message; throughput measures simultaneous capacity. A system might process each message in 10 microseconds (low latency) but only handle 50,000 MPS (limited throughput). Both dimensions matter: latency for speed, throughput for capacity.

## Why it matters (commodities and FX)

During high activity periods (data releases, central bank announcements, market opens), message rates spike. An FX market data feed produces over 1 million updates per second across all pairs. A quoting engine needs enough throughput to process all incoming data, recalculate prices, and publish quotes without falling behind. Insufficient throughput queues messages, raising effective [[Latency]] and producing [[Stale Quote|stale quotes]].

## Concrete example

**Concrete:** A commodity desk processes market data for 200 instruments across CME, ICE, and LME. Normal throughput: 50,000 MPS. Designed capacity: 200,000 MPS. OPEC announces an emergency meeting. Rates spike to 180,000 MPS across all energy contracts. The system handles the spike with headroom. Quotes stay fresh, no [[Stale Quote]] losses. A second desk with the same instruments but only 80,000 MPS capacity hits the OPEC spike. Messages queue. A [[Brent Crude]] update arrives at the algo 500 ms old. Competitors [[Sniping|snipe]] 8 stale quotes. The [[Kill Switch]] triggers. The desk misses 20 minutes of trading during the most profitable period of the year.

**Simplified:** Throughput is how many messages your system can chew through per second. Capacity must exceed peak rate, with headroom. When the market gets volatile, message rates explode and any system at the limit queues messages behind older ones. Old messages are useless. The system effectively goes blind.

## Key mechanics and formulas

**Throughput capacity:**
Max throughput = 1 / processing_time_per_message

If each message takes 10 microseconds: max throughput = 100,000 MPS

**Queue buildup (Little's Law):**
Queue length = arrival_rate * processing_time

Arrival 150,000 MPS, capacity 100,000 MPS:
Excess 50,000 MPS. After 1 second, 50,000 messages waiting, each delayed up to 500 ms.

**Throughput vs latency tradeoff:**
At low utilization (arrival << capacity): latency stable and low.
At high utilization (arrival approaching capacity): latency spikes from queuing.

**Rule of thumb:** Design for 3x to 5x normal peak to handle spikes without queuing.

## Prerequisites

- [[Latency]]
- [[Data Feed]]
- [[Hot Path]]

## Related concepts (learn next)

- [[Latency]] for the per message speed dimension
- [[Jitter]] for how throughput bottlenecks cause latency variance
- [[Data Feed]] for the primary source of high throughput message flow
- [[Hot Path]] for the code that must sustain high throughput under load
- [[Garbage Collection]] for a common cause of throughput collapse
- [[Kill Switch]] for what happens when throughput failure makes quoting unsafe

## Common misconceptions

1. **"High throughput means low latency."** A system can process 1 million MPS at 10 ms per message (parallel processing). Throughput and latency are independent dimensions.

2. **"My system handles peak volume, so throughput is fine."** Peak today is not peak during the next crisis. Design for 3x to 5x the highest observed rate. The 2020 oil crash saw CME energy rates 8x normal.

3. **"Throughput problems are always hardware problems."** Often the bottleneck is software: lock contention, allocation on the [[Hot Path]], or [[Garbage Collection]]. Profile first, buy hardware second.

## Sources

- Rajiv Ranjan, "Low Latency Trading Infrastructure," Springer
- CME Group, "Market Data Feed Specifications" (message rate statistics)
- Hennessy, J. and Patterson, D., "Computer Architecture: A Quantitative Approach"
