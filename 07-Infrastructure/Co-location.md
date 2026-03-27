---
aliases: [co-location, colocation, colo, proximity hosting]
tags:
  - "#infrastructure"
  - "#execution"
date-added: "2026-03-27"
---

# Co-location

## Definition
Co-location is the practice of placing a trading firm's servers in the same data center as the exchange's [[Matching Engine]], minimizing the physical distance that electronic messages must travel. The closer the server is to the exchange, the lower the [[Latency]] of order submission and market data reception. Major exchanges like CME (in Aurora, Illinois), ICE (in Basildon, UK), and the Tokyo Stock Exchange offer co-location services where firms rent rack space inside the exchange's data center. The latency advantage can be the difference between getting filled on a quote update and missing it entirely. Co-location is table stakes for any serious electronic trading operation.

## Why it matters (commodities and FX)
In commodity futures, the CME Globex matching engine in Aurora, Illinois processes millions of messages per day for [[WTI]], [[Natural Gas]], [[Gold]], [[Corn]], and hundreds of other contracts. A market maker co-located in Aurora has a round trip latency of roughly 1 to 5 microseconds to the matching engine. A trader connecting from a London office has a round trip of roughly 40 to 80 milliseconds. That 40+ millisecond difference means the London trader's quotes are always stale relative to the co-located trader. In FX, the major [[ECN]]s (EBS in Secaucus, NJ; Refinitiv in London and New York) offer co-location for the same reason. A bank's FX algo that is not co-located at EBS will consistently lose on tight spread opportunities to firms that are.

## Concrete example
Two firms are market making on ICE Brent crude oil futures, both quoting 1 tick wide.

**Firm A (co-located in Basildon):** Round trip latency to ICE matching engine: 5 microseconds. When a large order hits their resting quote, the fill confirmation arrives in 5 microseconds. They begin hedging on CME within 50 microseconds total.

**Firm B (connecting from New York):** Round trip latency: 35 milliseconds (35,000 microseconds). When the same large order hits Firm B's quote, the fill confirmation takes 35 milliseconds. By the time Firm B starts hedging on CME, the price has already moved 2 ticks because Firm A and other co-located participants have already adjusted.

**Result over 1 month:** Firm A earns an average of 0.8 ticks per round trip. Firm B earns 0.3 ticks per round trip because they consistently get picked off on stale quotes ([[Adverse Selection]]). On 10,000 round trips, Firm A profits $80,000 and Firm B profits $30,000. The co-location cost is $15,000 per month. Firm A nets $65,000. Firm B nets $15,000.

## Key mechanics and formulas
**Latency components:**
L_total = L_network + L_serialization + L_processing + L_matching
Where L_network = speed of light through fiber x distance (roughly 5 microseconds per kilometer), L_serialization = time to encode/decode the message, L_processing = time for the firm's software to react, L_matching = exchange matching engine processing time.

**Co-location latency (typical):**
- Same data center (co-located): 1 to 10 microseconds round trip
- Same city (proximity hosted): 100 to 500 microseconds
- Cross-country (NY to Chicago): 8 to 13 milliseconds one way
- Cross-Atlantic (NY to London): 30 to 40 milliseconds one way

**Cost structure (approximate):**
- CME co-location rack: $4,000 to $15,000 per month
- Cross-connect to matching engine: $1,000 to $3,000 per month
- Dedicated server hardware: $5,000 to $50,000 upfront
- Total annual cost for a basic setup: $100,000 to $300,000

**Break even calculation:**
N = C_colo / (R_colo - R_remote)
Where N = trades needed to break even, C_colo = monthly co-location cost, R_colo = average revenue per trade when co-located, R_remote = average revenue per trade when remote.

## Prerequisites
- [[Latency]]
- [[Matching Engine]]
- [[FIX Protocol]]

## Related concepts (learn next)
- [[Latency]] — co-location's primary benefit is reducing latency to the lowest physically possible level.
- [[Matching Engine]] — the exchange system that co-location puts you closest to.
- [[FIX Protocol]] — the messaging standard used to communicate with the exchange from the co-located server.
- [[Jitter]] — co-location reduces not just average latency but also latency variance, improving consistency.
- [[Throughput]] — co-located connections typically offer higher bandwidth and message rate limits.
- [[Adverse Selection]] — non-co-located market makers face higher adverse selection because their quotes are slower to update.
- [[Kill Switch]] — must also be co-located to ensure rapid cancellation when triggered.

## Common misconceptions
1. **"Co-location is only for HFT."** Any electronic market maker or systematic trader benefits from co-location. Even a strategy that trades 100 times per day benefits from fresher market data and faster fill confirmations. The question is whether the revenue improvement justifies the cost.
2. **"Closer always means faster."** Network topology matters more than physical distance inside a data center. A poorly configured network stack or an overloaded switch can add more latency than 100 meters of fiber. Software optimization often matters more than the last microsecond of physical proximity.
3. **"Co-location guarantees a level playing field."** Exchanges offer different tiers of co-location (basic rack vs. premium rack closer to the matching engine) and different network speeds (1 Gbps vs. 10 Gbps). Firms with bigger budgets still have advantages within the co-located environment.

## Sources
- CME Group. "Co-Location Services." cmegroup.com.
- ICE. "Co-Location and Connectivity." ice.com.
- Aldridge, I. (2013). *High-Frequency Trading: A Practical Guide to Algorithmic Strategies*. Wiley.
