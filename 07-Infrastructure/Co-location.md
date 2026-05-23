---
aliases: [co-location, colocation, colo, proximity hosting]
tags:
  - "#infrastructure"
  - "#execution"
date-added: "2026-03-27"
---

# Co-location

## Definition
Co-location is placing a trading firm's servers in the same data center as the exchange's [[Matching Engine]] to minimize the physical distance messages travel. Closer means lower [[Latency]] on order submission and market data reception. CME (Aurora, Illinois), ICE (Basildon, UK), and the Tokyo Stock Exchange all offer colocation rack space inside their exchange data centers. The latency advantage decides whether you get filled on a quote update or miss it. Colocation is table stakes for serious electronic trading.

## Why it matters (commodities and FX)
In commodity futures, CME Globex in Aurora processes millions of daily messages for [[WTI]], [[Natural Gas]], [[Gold]], [[Corn]], and hundreds of other contracts. A market maker co located in Aurora has 1 to 5 microsecond round trip latency. A trader from a London office runs 40 to 80 milliseconds. That 40+ millisecond gap means the London quotes are always stale relative to the co located trader. In FX, the major [[ECN]]s (EBS in Secaucus, Refinitiv in London and New York) offer the same. A bank FX algo not co located at EBS consistently loses tight spread opportunities to firms that are.

## Concrete example
**Concrete:** Two firms market make ICE Brent crude oil futures, both quoting 1 tick wide. Firm A is co located in Basildon: 5 microsecond round trip. Firm B connects from New York: 35 millisecond round trip. When a large order hits both firms' quotes, Firm A confirms in 5 microseconds and hedges on CME within 50 microseconds. Firm B confirms in 35 ms; by then the price has moved 2 ticks because co located participants already adjusted. Over 1 month and 10,000 round trips: Firm A averages 0.8 ticks per round trip ($80,000), Firm B averages 0.3 ticks ($30,000). Colocation costs $15,000/month. Firm A nets $65,000, Firm B nets $15,000.

**Simplified:** Light travels through fiber at roughly 5 microseconds per kilometer. Every kilometer between your server and the exchange adds latency. Renting space inside the exchange building cuts that to almost zero. The price tag is in the thousands per month. The payoff is consistently beating non co located firms to the queue.

## Key mechanics and formulas
**Latency components:**
L_total = L_network + L_serialization + L_processing + L_matching
Where L_network = speed of light through fiber x distance (roughly 5 microseconds per kilometer), L_serialization = message encoding time, L_processing = firm's software reaction time, L_matching = exchange matching time.

**Colocation latency (typical):**
- Same data center (co located): 1 to 10 microseconds round trip
- Same city (proximity hosted): 100 to 500 microseconds
- Cross country (NY to Chicago): 8 to 13 milliseconds one way
- Cross Atlantic (NY to London): 30 to 40 milliseconds one way

**Cost structure (approximate):**
- CME colocation rack: $4,000 to $15,000 per month
- Cross connect to matching engine: $1,000 to $3,000 per month
- Dedicated server hardware: $5,000 to $50,000 upfront
- Total annual cost for a basic setup: $100,000 to $300,000

**Break even calculation:**
N = C_colo / (R_colo - R_remote)
Where N = trades to break even, C_colo = monthly colocation cost, R_colo = average revenue per trade co located, R_remote = average revenue per trade remote.

## Prerequisites
- [[Latency]]
- [[Matching Engine]]
- [[FIX Protocol]]

## Related concepts (learn next)
- [[Latency]] — colocation's primary benefit is reducing latency to the physical minimum.
- [[Matching Engine]] — the exchange system that colocation puts you closest to.
- [[FIX Protocol]] — the messaging standard used from the co located server.
- [[Jitter]] — colocation reduces both average latency and variance.
- [[Throughput]] — co located connections support higher message rate limits.
- [[Adverse Selection]] — non co located market makers face higher adverse selection because their quotes update slower.
- [[Kill Switch]] — must also be co located for rapid cancellation when triggered.

## Common misconceptions
1. **"Colocation is only for HFT."** Any electronic market maker or systematic trader benefits. Even 100 trades per day gets value from fresher market data and faster fills. The question is whether revenue improvement justifies the cost.
2. **"Closer always means faster."** Network topology matters more than physical distance inside a data center. A poorly configured stack or overloaded switch adds more latency than 100 meters of fiber. Software optimization often beats the last microsecond of proximity.
3. **"Colocation guarantees a level playing field."** Exchanges sell tiered colocation (basic vs premium rack near the matching engine) and network speeds (1 Gbps vs 10 Gbps). Bigger budgets still get advantages.

## Sources
- CME Group. "Co-Location Services." cmegroup.com.
- ICE. "Co-Location and Connectivity." ice.com.
- Aldridge, I. (2013). *High-Frequency Trading: A Practical Guide to Algorithmic Strategies*. Wiley.
