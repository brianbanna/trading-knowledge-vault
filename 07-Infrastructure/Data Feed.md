---
aliases: [data feed, market data feed, price feed, live feed, ticker feed]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Data Feed

## Definition
A data feed is a continuous stream of live market data from an exchange or venue, delivering real time information about prices, quantities, and trading activity. Data feeds include bid prices, ask prices, trade prices, trade volumes, and [[Order Book]] depth (the number of contracts resting at each price level). There are 2 main types: Level 1 (top of book, showing only the best bid and offer) and Level 2 (full depth of book, showing all resting orders at every price level). Data feeds are the eyes of any trading system. Without accurate, low latency market data, a trading algorithm is blind and will make catastrophic decisions based on stale information.

## Why it matters (commodities and FX)
A market maker quoting [[WTI]] crude oil futures needs to see every price update in real time to adjust their quotes. If the data feed is delayed by even 1 millisecond relative to a competitor, the competitor will adjust quotes first and the slower firm will be adversely selected on stale prices. In FX, an aggregator that combines prices from 10 [[ECN]]s and bank streams needs reliable data feeds from all of them to compute the best available bid and offer. If one feed goes stale (stops updating), the aggregator might route orders to a venue showing an old price that no longer exists, resulting in rejections or bad fills. During high volatility events like OPEC announcements, NFP releases, or FOMC decisions, data feed message rates can spike 10x to 50x above normal levels, and any system that cannot handle the throughput will drop messages and trade on incomplete information.

## Concrete example
A commodity trading firm subscribes to 3 data sources for crude oil:
1. CME Globex direct feed (Level 2, co-located)
2. ICE direct feed (Level 2, co-located)
3. Bloomberg terminal feed (Level 1, consolidated)

**Win scenario:** At 10:30 AM, the DOE weekly petroleum status report shows a large draw. CME WTI updates 50,000 times in the next 10 seconds. The firm's co-located feed handler processes every message with 2 microsecond latency. The algo adjusts quotes within 5 microseconds of each update. The Bloomberg terminal feed lags by 200 milliseconds. The firm earns $12,000 in the 10 second window because they see the price discovery in real time.

**Fail scenario:** The firm's CME feed handler has a bug that drops messages when the update rate exceeds 8,000 messages per second. During the DOE report, the rate hits 50,000 per second. The handler drops 80% of messages. The algo thinks WTI is at $78.00 when it is actually at $79.50. It sends a buy order at $79.00 (what it thinks is $1 above the market). The order fills instantly because $79.00 is $0.50 below the actual market. 200 lots bought at $79.00 when fair value is $79.50 is a $100,000 windfall, but only by luck. On another day, the dropped data could cause the algo to sell at $1.50 below market.

## Key mechanics and formulas
**Data feed types:**
- **Direct feed:** Raw data from the exchange, lowest latency, requires dedicated connection and feed handler software. Examples: CME Market Data Platform (MDP 3.0), ICE iMpact.
- **Consolidated feed:** Aggregated from multiple exchanges by a vendor. Higher latency but simpler to consume. Examples: Bloomberg B-PIPE, Refinitiv Elektron.
- **FIX market data:** Market data delivered via [[FIX Protocol]] sessions (MarketDataSnapshotFullRefresh, MsgType W). Simpler but slower than binary feeds.

**Message rates (peak, approximate):**
- CME WTI front month: 10,000 to 100,000 messages per second during events
- ICE Brent: 5,000 to 50,000 messages per second
- EBS [[EURUSD]]: 20,000 to 200,000 messages per second during NFP
- LME Copper: 500 to 5,000 messages per second

**Feed latency components:**
L_feed = L_matching + L_publish + L_network + L_parse
Where L_matching = exchange matching engine processing, L_publish = time for exchange to publish the update, L_network = transit time (near zero if [[Co-location]]), L_parse = time for the firm's feed handler to decode the message.

**Data staleness detection:**
If T_current - T_last_update > threshold, the feed is considered stale and the algo should widen quotes or stop trading. Typical thresholds: 100 milliseconds for liquid futures, 1 second for illiquid contracts.

## Prerequisites
- [[Order Book]]
- [[Latency]]
- [[Co-location]]

## Related concepts (learn next)
- [[Latency]] — data feed latency directly determines how fresh the algo's view of the market is.
- [[Throughput]] — the system must handle peak message rates without dropping data.
- [[Co-location]] — minimizes network latency between the exchange's data publication point and the firm's feed handler.
- [[FIX Protocol]] — one method of receiving market data, though slower than direct binary feeds.
- [[Heartbeat]] — data feed connections use heartbeats to detect disconnections.
- [[Jitter]] — variance in data feed latency is as important as the average latency.
- [[Matching Engine]] — the source of all data feed messages, publishing updates after each order match.

## Common misconceptions
1. **"Level 1 data is sufficient for trading."** Level 1 shows only the best bid and offer. Without Level 2 depth, the trader cannot see how much size is resting behind the top of book, making it impossible to estimate [[Market Impact]] or detect large resting orders.
2. **"All data feeds from the same exchange are identical."** Exchanges offer multiple feed products with different latencies, update rates, and content. CME's MDP 3.0 direct feed is fundamentally different from CME's FIX market data feed in both speed and information content.
3. **"If the data feed is working, the data is accurate."** Exchange data feeds can have erroneous prints (bad trades that get busted), duplicate messages, or sequence gaps. A robust feed handler must detect and handle these anomalies rather than blindly trusting every message.

## Sources
- CME Group. "Market Data Platform (MDP 3.0)." cmegroup.com.
- ICE. "iMpact Market Data Feed." ice.com.
- Hasbrouck, J. (2007). *Empirical Market Microstructure*. Oxford University Press.
