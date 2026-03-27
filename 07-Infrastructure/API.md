---
aliases: [application programming interface, trading API, venue API]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# API

## Definition

An API (Application Programming Interface) is a standardized way for software systems to communicate with each other. In trading, APIs are how a trading system connects to exchanges, brokers, data providers, and risk systems programmatically. Instead of clicking buttons on a screen, the system sends structured messages (requests) and receives structured responses. Most modern trading APIs use either [[FIX Protocol]], REST (HTTP based), or WebSocket connections for real time streaming.

## Why it matters (commodities and FX)

Every electronic trade flows through an API. A commodities trader pulling live [[Brent Crude]] prices from ICE uses the exchange's market data API. An FX desk sending orders to an [[ECN]] like EBS uses the venue's order entry API. The quality of an API (its speed, reliability, and feature set) directly determines what a trading system can do. Poor API design creates [[Latency]], limits order types, and increases operational risk.

## Concrete example

An FX market maker builds a system to quote [[EUR USD]] on 3 venues simultaneously: EBS (via [[FIX Protocol]] API), Refinitiv (via FIX API), and a [[Single Dealer Platform]] (via REST API).

**Success case:** The FIX APIs to EBS and Refinitiv deliver sub millisecond order acknowledgements. The desk places and cancels thousands of orders per second, maintaining tight [[Two Way Price]] quotes. [[Tick to Trade]] latency stays below 200 microseconds.

**Failure case:** The REST API on the SDP has a 50 millisecond round trip for each order. During volatile moments, the desk cannot update quotes fast enough, and competitors [[Sniping|snipe]] stale prices. The desk loses $12,000 per day on that venue until it switches to the SDP's newer WebSocket API with 5 millisecond round trips.

## Key mechanics and formulas

**Common trading API types:**

| Type | Use case | Latency | Direction |
|------|----------|---------|-----------|
| [[FIX Protocol]] | Order entry, execution reports | Microseconds | Bidirectional |
| WebSocket | Streaming market data, order updates | Milliseconds | Server push |
| REST/HTTP | Reference data, position queries, slow ops | 10s of milliseconds | Request/response |

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

1. **"REST APIs are fine for trading."** REST works for slow operations (pulling position reports, reference data) but its request/response model adds too much overhead for real time quoting or execution. FIX and WebSocket are standard for anything latency sensitive.

2. **"All exchange APIs are the same."** Each venue has its own message formats, rate limits, error codes, and quirks. Connecting to CME is entirely different from connecting to LME or EBS. This integration work is a major cost.

3. **"An API connection means you are trading."** Connecting is step 1. Handling disconnects, message gaps, sequence number resets, and partial fills correctly is where the real engineering happens.

## Sources

- FIX Trading Community, "FIX Protocol Specification"
- CME Group, "CME Globex API Documentation"
- ICE, "ICE Connect API Developer Guide"
