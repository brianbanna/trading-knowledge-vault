---
aliases: [FIX protocol, FIX, Financial Information Exchange, FIX messaging]
tags:
  - "#infrastructure"
  - "#execution"
date-added: "2026-03-27"
---

# FIX Protocol

## Definition
The FIX (Financial Information eXchange) Protocol is the standardized messaging format used to send orders, receive fills, and exchange market data electronically between trading firms and exchanges or brokers. It is the lingua franca of electronic trading. FIX defines message types for every stage of the trade lifecycle: new order (MsgType D), execution report (MsgType 8), order cancel request (MsgType F), and market data (MsgType W), among dozens of others. First developed in 1992 for equity trading between Fidelity and Salomon Brothers, FIX is now used across all asset classes including futures, options, FX, and fixed income. The current widely used version is FIX 4.4, with FIX 5.0 and FIXT gaining adoption.

## Why it matters (commodities and FX)
Every electronic order sent to CME, ICE, LME, or any major commodity exchange travels as a FIX message (or a proprietary binary protocol that maps to FIX semantics). When a trader's algorithm decides to buy 50 lots of [[WTI]] crude oil at $78.50 limit, that decision is encoded as a FIX NewOrderSingle message with fields specifying the instrument, side, quantity, price, order type, and time in force. The exchange's [[Matching Engine]] processes this message and returns a FIX ExecutionReport confirming the fill or rejection. In FX, the major [[ECN]]s (EBS, Refinitiv, Hotspot, Currenex) all accept FIX messages for order routing. A bank's FX algo might connect to 5 venues simultaneously, all via FIX, aggregating liquidity across the market. Understanding FIX is not optional for any electronic trader.

## Concrete example
A market making firm sends a limit order to sell 100 lots of ICE Brent crude oil at $82.75. The outbound FIX message (simplified) looks like:

```
8=FIX.4.4 | 35=D | 49=MYTRADER | 56=ICE | 55=BRN | 54=2 | 38=100 | 44=82.75 | 40=2 | 59=0
```

Key fields: 35=D (NewOrderSingle), 54=2 (Sell), 38=100 (quantity), 44=82.75 (price), 40=2 (Limit order), 59=0 (Day order).

**Win scenario:** The exchange fills 100 lots at 82.75. The inbound ExecutionReport: 35=8 | 39=2 (Filled) | 31=82.75 | 32=100. The maker's system parses this in microseconds and immediately sends a hedge order to CME WTI.

**Fail scenario:** The firm's FIX session disconnects due to a network glitch. The 100 lot sell order is resting on the exchange but the firm cannot cancel it. Price drops to $81.50 before the connection is restored. The firm gets filled on the sell at $82.75 (good) but cannot hedge because they did not receive the fill confirmation. By the time the session reconnects 45 seconds later, the hedge cost is $81.60 instead of $82.70. [[Slippage]]: $1.10 x 100 x 1,000 = $110,000.

## Key mechanics and formulas
**FIX message structure:**
Tag=Value pairs separated by the SOH delimiter (ASCII 01). Every message starts with BeginString (8), BodyLength (9), and MsgType (35), and ends with Checksum (10).

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

**Sequence numbers:** Every FIX message has a sequence number (tag 34). Both sides track expected sequence numbers. If a message is missed, a ResendRequest (MsgType 2) asks for retransmission. This ensures no orders or fills are lost.

**Session vs application layer:** FIX separates the session layer (logon, heartbeat, sequence management) from the application layer (orders, fills, market data). A [[Heartbeat]] failure at the session layer triggers reconnection procedures.

## Prerequisites
- [[Latency]]
- [[Matching Engine]]
- [[Order Book]]

## Related concepts (learn next)
- [[Heartbeat]] — FIX heartbeat messages keep the session alive and detect disconnections.
- [[Co-location]] — FIX messages travel faster when the server is co-located with the exchange.
- [[Latency]] — FIX message serialization and parsing contribute to total round trip latency.
- [[Kill Switch]] — uses the FIX MassCancelRequest (MsgType q) to cancel all orders instantly.
- [[Data Feed]] — market data can be delivered via FIX (MarketData messages) or proprietary binary feeds.
- [[Throughput]] — FIX message rate limits are set by the exchange and affect how many orders per second a firm can send.
- [[Order Types]] — FIX encodes all order types (limit, market, stop, IOC, FOK) via tags 40 and 59.

## Common misconceptions
1. **"FIX is the fastest protocol available."** FIX is a text based protocol with significant overhead from tag=value encoding. Most exchanges offer proprietary binary protocols (e.g., CME iLink, ICE ETL) that are faster. FIX is the standard for connectivity, but latency sensitive firms often use native binary protocols.
2. **"FIX handles market data well."** FIX was designed for order routing, not high throughput market data. For instruments like [[WTI]] with thousands of price updates per second, exchanges provide dedicated market data feeds (e.g., CME Market Data Platform) that are separate from the FIX order session.
3. **"All FIX implementations are the same."** Every exchange adds custom fields and tags to the base FIX specification. CME's FIX implementation differs from ICE's, which differs from LME's. Integration with each venue requires reading their specific FIX specification document and handling custom tags.

## Sources
- FIX Trading Community. "FIX Protocol Specifications." fixtrading.org.
- CME Group. "iLink 3 and FIX Connectivity." cmegroup.com.
- ICE. "FIX Specification for ICE Futures." ice.com.
