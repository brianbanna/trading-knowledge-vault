---
aliases: [heartbeat, heartbeat message, keep-alive, connection heartbeat]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Heartbeat

## Definition
A heartbeat is a periodic message between a trading system and an exchange (or any 2 connected systems) confirming the connection is alive. If either side fails to receive one within the agreed interval (10 to 30 seconds for [[FIX Protocol]] sessions), the connection is presumed dead and reconnection begins. Heartbeats carry no trading content, just "I am still here." Without heartbeats, a firm can be silently disconnected from the exchange with resting orders still live but no ability to cancel or modify, a potentially catastrophic state.

## Why it matters (commodities and FX)
A market maker quoting 2 sided markets on [[WTI]] futures has dozens of resting orders on CME at any moment. If the network silently drops (no error, no data), the maker's quotes stay live while the maker's system thinks all is well. If price moves 50 ticks against those resting orders, they fill and the maker only learns when the connection comes back. Heartbeats catch this in seconds, not minutes. In FX, a bank connected to 8 [[ECN]]s monitors heartbeats on each independently. If EBS drops while Refinitiv stays up, the bank needs to know now so it can cancel EBS quotes via an alternative path or adjust aggregate risk.

## Concrete example
**Concrete:** Algo firm runs Brent market making with a [[FIX Protocol]] session at 30 second heartbeat. At 14:22:00 UTC, a fiber cut between the [[Co-location]] rack and the ICE matching engine causes a silent disconnect. No error, no reset, just silence. At 14:22:30, the heartbeat timer expires. The system declares the connection dead, activates the [[Kill Switch]] via a secondary network path, and cancels all 24 resting orders within 200 ms. Brent moves $0.80 against the quotes during the gap but no fills occur. Loss: $0. Without heartbeat monitoring, the same disconnect would persist 6 minutes before a human notices the data feed stopped. During those 6 minutes, Brent moves $1.20 and 400 lots of stale quotes fill. Loss: roughly $480,000.

**Simplified:** Two systems send each other an "I am alive" ping every N seconds. Miss a ping, the connection is presumed dead. The point is not the ping itself; it is detecting silence. A silent network failure with live resting orders is the worst case in electronic trading. Heartbeats put a clock on it.

## Key mechanics and formulas
**FIX heartbeat mechanism:**
- Both sides agree on HeartBtInt (tag 108) during Logon (e.g., 30 seconds)
- If no messages are sent within the interval, a Heartbeat message (MsgType 0) is sent
- If no messages are received within HeartBtInt + "reasonable transmission time," a TestRequest (MsgType 1) is sent
- If the TestRequest receives no response within HeartBtInt, the connection is declared dead

**Heartbeat interval tradeoff:**
- Shorter interval (5 seconds): faster detection, more overhead, higher false positive risk from transient delays
- Longer interval (60 seconds): fewer false positives, slower detection, longer exposure

**Optimal interval (heuristic):**
HB_interval = max(2 x L_99th, T_min)
Where L_99th = 99th percentile network latency, T_min = minimum acceptable detection based on risk tolerance. Co located systems use 10 second heartbeats. Cross Atlantic uses 30 seconds.

**Dead connection exposure:**
E = Q x ΔP_expected(HB_interval)
Where E = expected loss from stale quotes, Q = total resting quantity, ΔP_expected = expected price move during the interval.

## Prerequisites
- [[FIX Protocol]]
- [[Latency]]
- [[Co-location]]

## Related concepts (learn next)
- [[FIX Protocol]] — heartbeat is a session level message (MsgType 0).
- [[Kill Switch]] — heartbeat failure is a standard trigger.
- [[Data Feed]] — market data feeds have their own heartbeats separate from order session.
- [[Latency]] — heartbeat intervals must account for network latency to avoid false positives.
- [[Jitter]] — high jitter causes spurious timeouts on fundamentally healthy connections.
- [[Throughput]] — during high volume, heartbeats may be delayed by network congestion.

## Common misconceptions
1. **"If I am receiving market data, the order connection is fine."** Market data and order entry run on separate [[FIX Protocol]] sessions or even separate network paths. Data can work while the order session is dead. Each connection needs its own heartbeat.
2. **"A missed heartbeat means the connection is definitely dead."** A single missed heartbeat may be a transient hiccup. FIX requires a TestRequest before declaring dead. Only if that also goes unanswered is the session terminated.
3. **"Heartbeats add unnecessary network overhead."** A FIX heartbeat is roughly 60 bytes. On a session moving millions in orders, the bandwidth cost of 1 heartbeat per 30 seconds is negligible compared to the cost of undetected disconnects.

## Sources
- FIX Trading Community. "FIX Session Protocol." fixtrading.org.
- CME Group. "iLink Session Layer Specification." cmegroup.com.
- ICE. "FIX Connectivity Guide." ice.com.
