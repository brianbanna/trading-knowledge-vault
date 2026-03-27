---
aliases: [heartbeat, heartbeat message, keep-alive, connection heartbeat]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Heartbeat

## Definition
A heartbeat is a periodic message sent between a trading system and an exchange (or between any 2 connected systems) to confirm that the connection is still alive and functioning. If either side fails to receive a heartbeat within a specified interval (typically 10 to 30 seconds for [[FIX Protocol]] sessions), the connection is assumed dead and reconnection procedures begin. Heartbeats are the pulse of electronic trading connectivity. They carry no trading information, just the message "I am still here." Without heartbeats, a firm could be unknowingly disconnected from the exchange, with resting orders still live but no ability to cancel or modify them, a potentially catastrophic situation.

## Why it matters (commodities and FX)
A market maker quoting 2 sided markets on [[WTI]] crude oil futures has dozens of resting orders on CME at any time. If the network connection silently drops (no error, just no more data), the maker's quotes remain live on the exchange while the maker's system thinks everything is fine. If the price moves 50 ticks against those resting orders, they will get filled and the maker will not know until the connection is restored. Heartbeats detect this scenario within seconds rather than minutes. In FX, a bank connected to 8 [[ECN]]s simultaneously must monitor heartbeats on each connection independently. If the EBS connection drops while the Refinitiv connection stays up, the bank needs to know immediately so it can cancel EBS quotes via an alternative path or adjust aggregate risk.

## Concrete example
An algo trading firm runs a market making strategy on ICE Brent crude oil with a [[FIX Protocol]] session configured for 30 second heartbeat intervals.

**Win scenario (heartbeat saves the firm):** At 14:22 UTC, a fiber cut between the firm's [[Co-location]] rack and the ICE matching engine causes a silent disconnect. No error, no reset, just silence. The last heartbeat was received at 14:22:00. At 14:22:30, the heartbeat timer expires. The system declares the connection dead, activates the [[Kill Switch]] via an alternative network path (a secondary connection), and cancels all 24 resting orders within 200 milliseconds. Meanwhile, Brent moves $0.80 against the firm's quotes. No fills occur because the orders were cancelled in time. Total loss: $0.

**Fail scenario (no heartbeat monitoring):** Same fiber cut, but the system has no heartbeat timeout. The silent disconnect persists for 6 minutes before a human notices the data feed has stopped updating. During those 6 minutes, Brent moves $1.20 and 400 lots of stale quotes are filled. Loss: approximately $480,000.

## Key mechanics and formulas
**FIX heartbeat mechanism:**
- Both sides agree on a HeartBtInt (tag 108) during Logon (e.g., 30 seconds)
- If no messages are sent within the interval, a Heartbeat message (MsgType 0) is sent
- If no messages are received within HeartBtInt + "reasonable transmission time," a TestRequest (MsgType 1) is sent
- If the TestRequest receives no response within HeartBtInt, the connection is declared dead

**Heartbeat interval tradeoff:**
- Shorter interval (e.g., 5 seconds): faster detection of disconnects, but more overhead and higher risk of false positives from transient network delays
- Longer interval (e.g., 60 seconds): fewer false positives, but slower detection of real disconnects, leaving stale orders exposed longer

**Optimal heartbeat interval formula (heuristic):**
HB_interval = max(2 x L_99th, T_min)
Where L_99th = 99th percentile network latency, T_min = minimum acceptable detection time based on risk tolerance. For co-located systems with microsecond latency, a 10 second heartbeat is common. For cross-Atlantic connections, 30 seconds is standard.

**Dead connection exposure:**
E = Q x ΔP_expected(HB_interval)
Where E = expected loss from stale quotes during a dead connection, Q = total resting order quantity, ΔP_expected = expected price move during the heartbeat interval.

## Prerequisites
- [[FIX Protocol]]
- [[Latency]]
- [[Co-location]]

## Related concepts (learn next)
- [[FIX Protocol]] — heartbeat is a core session level message in the FIX standard (MsgType 0).
- [[Kill Switch]] — heartbeat failure is a common trigger for kill switch activation.
- [[Data Feed]] — market data feeds have their own heartbeat mechanisms independent of order session heartbeats.
- [[Latency]] — heartbeat intervals must account for network latency to avoid false positive disconnection events.
- [[Jitter]] — high jitter can cause spurious heartbeat timeouts even when the connection is fundamentally healthy.
- [[Throughput]] — during high message volume periods, heartbeats may be delayed if the network is congested, requiring careful timeout tuning.

## Common misconceptions
1. **"If I am receiving market data, the order connection is fine."** Market data and order entry typically run on separate [[FIX Protocol]] sessions or even separate network paths. The data feed can be working perfectly while the order session is dead. Each connection needs its own heartbeat monitoring.
2. **"A missed heartbeat means the connection is definitely dead."** A single missed heartbeat could be caused by a transient network hiccup. This is why the FIX standard requires sending a TestRequest before declaring the connection dead. Only if the TestRequest also goes unanswered is the session terminated.
3. **"Heartbeats add unnecessary network overhead."** A FIX heartbeat message is roughly 60 bytes. On a session that handles millions of dollars in orders, the bandwidth cost of 1 heartbeat every 30 seconds is negligible. The cost of not having heartbeats (undetected disconnects) dwarfs the overhead by orders of magnitude.

## Sources
- FIX Trading Community. "FIX Session Protocol." fixtrading.org.
- CME Group. "iLink Session Layer Specification." cmegroup.com.
- ICE. "FIX Connectivity Guide." ice.com.
