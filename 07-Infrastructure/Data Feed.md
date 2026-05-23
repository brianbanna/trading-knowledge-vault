---
aliases: [data feed, market data feed, price feed, live feed, ticker feed]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Data Feed

## Definition
A data feed is a live stream of market data from an exchange or venue carrying prices, quantities, and trading activity. Feeds include bid, ask, trade price, trade volume, and [[Order Book]] depth. Two main types: Level 1 (top of book, best bid and offer only) and Level 2 (full depth, all resting orders at every level). Data feeds are the eyes of any trading system. Without accurate low latency market data, an algo is blind and will make catastrophic decisions on stale information.

## Why it matters (commodities and FX)
A market maker quoting [[WTI]] futures needs every price update in real time to adjust. A 1 millisecond delay relative to a competitor means the competitor adjusts first and the slower firm gets adversely selected on stale prices. In FX, an aggregator combining 10 [[ECN]]s and bank streams needs reliable feeds from all of them to compute the best bid and offer. One stale feed sends orders to a phantom price, producing rejections or bad fills. During volatility events (OPEC, NFP, FOMC), feed message rates spike 10 to 50x normal. Any system that cannot handle the throughput drops messages and trades on incomplete information.

## Concrete example
**Concrete:** A commodity firm subscribes to 3 sources for crude: CME Globex direct (Level 2, co located), ICE direct (Level 2, co located), Bloomberg terminal (Level 1, consolidated). At 10:30 AM the DOE petroleum status report shows a large draw. CME WTI updates 50,000 times in 10 seconds. The co located feed handler processes every message at 2 microsecond latency. The algo adjusts quotes within 5 microseconds per update. The Bloomberg feed lags 200 ms. The firm earns $12,000 in the 10 second window by seeing real time price discovery. A bug that drops messages above 8,000/sec would have made the algo trade on phantom $78.00 quotes when the market was $79.50, sending a "buy at $1 over" order that fills $0.50 below market.

**Simplified:** The exchange publishes a stream of every price change and trade. You connect to it and consume it. Slow or lossy means you see prices that no longer exist. Then you send orders into a market that has already moved. Direct binary feeds are fastest; consolidated vendor feeds are slower but simpler. Co located direct feeds are the standard for any latency sensitive desk.

## Key mechanics and formulas
**Data feed types:**
- **Direct feed:** Raw exchange data, lowest latency, requires dedicated connection and feed handler. Examples: CME MDP 3.0, ICE iMpact.
- **Consolidated feed:** Aggregated from multiple exchanges by a vendor. Higher latency, simpler to consume. Examples: Bloomberg B-PIPE, Refinitiv Elektron.
- **FIX market data:** Delivered via [[FIX Protocol]] (MarketDataSnapshotFullRefresh, MsgType W). Simpler but slower than binary.

**Message rates (peak, approximate):**
- CME WTI front month: 10,000 to 100,000 messages per second during events
- ICE Brent: 5,000 to 50,000 messages per second
- EBS [[EURUSD]]: 20,000 to 200,000 messages per second during NFP
- LME Copper: 500 to 5,000 messages per second

**Feed latency components:**
L_feed = L_matching + L_publish + L_network + L_parse
Where L_matching = matching engine processing, L_publish = time for the exchange to publish, L_network = transit (near zero with [[Co-location]]), L_parse = feed handler decode time.

**Data staleness detection:**
If T_current - T_last_update > threshold, the feed is stale and the algo should widen quotes or stop. Typical thresholds: 100 ms for liquid futures, 1 second for illiquid contracts.

## Prerequisites
- [[Order Book]]
- [[Latency]]
- [[Co-location]]

## Related concepts (learn next)
- [[Latency]] — feed latency determines how fresh the algo's view is.
- [[Throughput]] — the system must handle peak rates without dropping data.
- [[Co-location]] — minimizes network latency between exchange and feed handler.
- [[FIX Protocol]] — one method of receiving market data, slower than direct binary.
- [[Heartbeat]] — feed connections use heartbeats to detect disconnections.
- [[Jitter]] — variance in feed latency matters as much as the average.
- [[Matching Engine]] — source of every feed message, publishing after each match.

## Common misconceptions
1. **"Level 1 data is sufficient for trading."** Level 1 shows only top of book. Without Level 2 depth, you cannot see size resting behind the top, making it impossible to estimate [[Market Impact]] or detect large resting orders.
2. **"All feeds from the same exchange are identical."** Exchanges offer multiple products with different latencies, rates, and content. CME MDP 3.0 differs fundamentally from CME's FIX market data feed in speed and information content.
3. **"If the feed is working, the data is accurate."** Feeds carry erroneous prints (busted trades), duplicate messages, sequence gaps. A solid handler detects and handles these rather than blindly trusting every message.

## Sources
- CME Group. "Market Data Platform (MDP 3.0)." cmegroup.com.
- ICE. "iMpact Market Data Feed." ice.com.
- Hasbrouck, J. (2007). *Empirical Market Microstructure*. Oxford University Press.
