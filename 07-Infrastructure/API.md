---
aliases: [application programming interface, trading API, venue API]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# API

## Definition

An API is a structured way for software systems to communicate. In trading, APIs connect systems to exchanges, brokers, data providers, and risk systems. The system sends structured messages and receives structured responses. Trading APIs use [[FIX Protocol]], REST (HTTP), or WebSocket for streaming.

## Why it matters (commodities and FX)

Every electronic trade flows through an API. A commodities desk pulling live [[Brent Crude]] prices from ICE uses the exchange's market data API. An FX desk sending orders to an [[ECN]] like EBS uses the venue's order entry API. API speed, reliability, and feature set determine system capability. Poor API design creates [[Latency]], limits order types, and increases operational risk.

## Concrete example

**Concrete:** An FX market maker quotes [[EUR USD]] on 3 venues: EBS and Refinitiv via [[FIX Protocol]], plus a [[Single Dealer Platform]] via REST. The FIX APIs deliver sub millisecond acknowledgements. The desk places thousands of orders per second with [[Tick to Trade]] below 200 microseconds. The REST API on the SDP runs 50 millisecond round trips. During volatile moments, the desk cannot update quotes fast enough and competitors [[Sniping|snipe]] stale prices. The desk bleeds $12,000 per day on that venue until it migrates to the SDP's 5 millisecond WebSocket API.

**Simplified:** Software speaks to the exchange through a defined message format. Fast formats (FIX, binary) handle order flow. Slow formats (REST) handle position queries and reference data. Mixing them poorly costs money.

## Key mechanics and formulas

**Common trading API types:**

| Type | Use case | Latency | Direction |
|------|----------|---------|-----------|
| [[FIX Protocol]] | Order entry, execution reports | Microseconds | Bidirectional |
| WebSocket | Streaming market data, order updates | Milliseconds | Server push |
| REST/HTTP | Reference data, position queries | 10s of milliseconds | Request/response |

**Key metrics:**
- Messages per second ([[Throughput]])
- Round trip time ([[Latency]])
- Reconnection time after disconnect
- Rate limits (max requests per second before throttling)

## Prerequisites

- [[FIX Protocol]]
- [[Data Feed]]
- [[Latency]]

## Related concepts (learn next)

- [[FIX Protocol]] for the dominant standard in institutional order routing
- [[Data Feed]] for the market data side of API connectivity
- [[Heartbeat]] for how connections are kept alive and monitored
- [[Throughput]] for measuring how many messages per second the API handles
- [[Latency]] for the speed dimension of API performance
- [[Co-location]] for minimizing the physical distance to the API endpoint

## Common misconceptions

1. **"REST APIs are fine for trading."** REST works for slow operations (position reports, reference data) but its request/response model adds too much overhead for real time quoting. FIX and WebSocket are standard for latency sensitive paths.

2. **"All exchange APIs are the same."** Each venue has its own message formats, rate limits, error codes, and quirks. Connecting to CME is entirely different from connecting to LME or EBS. Integration is a major cost.

3. **"An API connection means you are trading."** Connecting is step 1. Handling disconnects, message gaps, sequence number resets, and partial fills correctly is where the real engineering happens.

## Sources

- FIX Trading Community, "FIX Protocol Specification"
- CME Group, "CME Globex API Documentation"
- ICE, "ICE Connect API Developer Guide"
