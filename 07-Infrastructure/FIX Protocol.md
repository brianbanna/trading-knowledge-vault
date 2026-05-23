---
aliases: [FIX protocol, FIX, Financial Information Exchange, FIX messaging]
tags:
  - "#infrastructure"
  - "#execution"
date-added: "2026-03-27"
---

# FIX Protocol

## Definition
The FIX (Financial Information eXchange) Protocol is the standardized messaging format used to send orders, receive fills, and exchange market data between trading firms and exchanges or brokers. It is the lingua franca of electronic trading. FIX defines message types for every stage of the trade lifecycle: new order (MsgType D), execution report (MsgType 8), cancel request (MsgType F), market data (MsgType W), and dozens more. First developed in 1992 for equity trading between Fidelity and Salomon Brothers, FIX now covers all asset classes including futures, options, FX, and fixed income. Current widely used version is FIX 4.4, with FIX 5.0 and FIXT gaining adoption.

## Why it matters (commodities and FX)
Every electronic order to CME, ICE, LME, or any major commodity exchange travels as a FIX message (or a proprietary binary protocol mapping to FIX semantics). When an algo decides to buy 50 lots of [[WTI]] at $78.50 limit, that decision encodes as a FIX NewOrderSingle with fields for instrument, side, quantity, price, type, and time in force. The [[Matching Engine]] processes it and returns a FIX ExecutionReport confirming fill or rejection. In FX, the major [[ECN]]s (EBS, Refinitiv, Hotspot, Currenex) all accept FIX for order routing. A bank FX algo might connect to 5 venues via FIX simultaneously, aggregating liquidity. Understanding FIX is not optional for an electronic trader.

## Concrete example
**Concrete:** A market making firm sends a limit order to sell 100 lots of ICE Brent at $82.75. Outbound FIX (simplified):

```
8=FIX.4.4 | 35=D | 49=MYTRADER | 56=ICE | 55=BRN | 54=2 | 38=100 | 44=82.75 | 40=2 | 59=0
```

Key fields: 35=D (NewOrderSingle), 54=2 (Sell), 38=100 (quantity), 44=82.75 (price), 40=2 (Limit), 59=0 (Day). The exchange fills 100 lots. Inbound: 35=8 | 39=2 (Filled) | 31=82.75 | 32=100. The system parses in microseconds and fires a CME WTI hedge. A failed FIX session during a 45 second disconnect leaves the 100 lot sell resting at $82.75 unhedged. Brent drops to $81.50. The fill executes (good) but the hedge cost is $81.60 instead of $82.70. [[Slippage]]: $1.10 x 100 x 1,000 = $110,000.

**Simplified:** FIX is the text language software uses to talk to exchanges. Every order, every cancel, every fill confirmation is a FIX message: a list of numbered tags and values. The system needs to format, send, parse, and acknowledge these correctly, including session level concerns like reconnects and sequence numbers. Get any of it wrong and orders go missing or duplicate.

## Key mechanics and formulas
**FIX message structure:**
Tag=Value pairs separated by SOH delimiter (ASCII 01). Every message starts with BeginString (8), BodyLength (9), MsgType (35), and ends with Checksum (10).

**Critical message types for trading:**

| MsgType | Tag 35 | Purpose |
|---|---|---|
| Logon | A | Establish session |
| [[Heartbeat]] | 0 | Keep connection alive |
| NewOrderSingle | D | Submit new order |
| OrderCancelRequest | F | Cancel resting order |
| OrderCancelReplaceRequest | G | Modify resting order |
| ExecutionReport | 8 | Fill, partial fill, reject, cancel confirm |
| MarketDataRequest | V | Subscribe to market data |
| MarketDataSnapshotFullRefresh | W | Market data update |
| MassCancelRequest | q | Cancel all orders ([[Kill Switch]]) |

**Sequence numbers:** Every FIX message has a sequence number (tag 34). Both sides track expected sequences. If a message is missed, a ResendRequest (MsgType 2) asks for retransmission. No orders or fills are lost.

**Session vs application layer:** FIX separates session (logon, heartbeat, sequence) from application (orders, fills, market data). A [[Heartbeat]] failure at session layer triggers reconnect.

## Prerequisites
- [[Latency]]
- [[Matching Engine]]
- [[Order Book]]

## Related concepts (learn next)
- [[Heartbeat]] — FIX heartbeats keep the session alive and detect disconnections.
- [[Co-location]] — FIX messages travel faster from a co located server.
- [[Latency]] — FIX serialization and parsing contribute to round trip latency.
- [[Kill Switch]] — uses FIX MassCancelRequest (MsgType q) for instant cancellation.
- [[Data Feed]] — market data via FIX or proprietary binary feeds.
- [[Throughput]] — FIX message rate limits are set by the exchange.
- [[Order Types]] — FIX encodes all types (limit, market, stop, IOC, FOK) via tags 40 and 59.

## Common misconceptions
1. **"FIX is the fastest protocol available."** FIX is text based with significant tag=value overhead. Most exchanges offer proprietary binary protocols (CME iLink, ICE ETL) that are faster. FIX is standard for connectivity; latency sensitive firms use native binary.
2. **"FIX handles market data well."** FIX was designed for order routing, not high throughput market data. For [[WTI]] with thousands of updates per second, exchanges provide dedicated market data feeds separate from FIX order sessions.
3. **"All FIX implementations are the same."** Every exchange adds custom fields and tags to the base spec. CME's FIX differs from ICE's, which differs from LME's. Integration requires reading the venue specific spec.

## Sources
- FIX Trading Community. "FIX Protocol Specifications." fixtrading.org.
- CME Group. "iLink 3 and FIX Connectivity." cmegroup.com.
- ICE. "FIX Specification for ICE Futures." ice.com.
