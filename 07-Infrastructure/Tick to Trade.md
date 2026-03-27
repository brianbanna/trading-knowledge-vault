---
aliases: [tick to trade, tick-to-trade, T2T, end-to-end latency, wire-to-wire]
tags:
  - "#infrastructure"
  - "#execution"
date-added: "2026-03-27"
---

# Tick to Trade

## Definition
Tick to trade (T2T) is the total elapsed time from the moment a market data update arrives at the trading system's network interface to the moment the resulting order leaves the network interface heading to the exchange. It is the single most important latency metric for any latency sensitive trading system. T2T encompasses network receive, market data decoding, order book update, signal/pricing computation, order construction, risk checks, and network transmit. For HFT market makers, T2T is measured in nanoseconds (100 to 500 ns). For medium frequency systematic traders, it is microseconds to milliseconds. Reducing T2T requires optimizing every component on the [[Hot Path]]: [[Cache Locality]], eliminating [[Memory Allocation]], minimizing [[Branch Prediction]] mispredictions, and avoiding [[Garbage Collection]].

## Why it matters (commodities and FX)
In commodity futures on CME and ICE, queue position determines profitability for market makers. The first quote at a price level gets filled first. A Brent crude market maker with 200 nanosecond T2T consistently beats a competitor at 500 nanoseconds. Over a full trading day, this translates to thousands of additional fills and hundreds of thousands of dollars in spread capture. In FX, where EUR/USD trades on multiple [[ECN]]s simultaneously, T2T determines whether an arbitrage opportunity is captured or missed. A cross venue arbitrage signal might exist for only 5 microseconds. A system with 10 microsecond T2T cannot exploit it, while a system with 1 microsecond T2T can.

## Concrete example
A WTI crude oil market maker on CME Globex receives a trade message indicating the last trade at $72.45. The system must update its quote.

**T2T breakdown (optimized C++ system, co located):**

| Stage | Time |
|-------|------|
| NIC to userspace (kernel bypass) | 50 ns |
| Decode CME MDP 3.0 binary message | 40 ns |
| Update internal order book | 30 ns |
| Evaluate pricing model | 60 ns |
| Construct FIX/iLink order | 30 ns |
| Pre trade risk check | 20 ns |
| Serialize and write to NIC | 40 ns |
| **Total T2T** | **270 ns** |

**Win scenario:** The system's 270 ns T2T places it 2nd out of 12 competing market makers. The top 3 firms share roughly 60% of passive fills on WTI. The system captures 4,000 fills per day at an average profit of $12.50 per fill, generating $50,000 daily gross.

**Fail scenario:** A new regulatory requirement adds a compliance check to the hot path. The check involves a hash table lookup that causes 2 [[Cache Miss]]es, adding 200 nanoseconds. T2T jumps to 470 nanoseconds. The system drops from position 2 to position 7. Daily fills fall from 4,000 to 1,200. Daily gross drops from $50,000 to $15,000.

**Measurement approach:** Use hardware timestamping on the NIC (network interface card) to capture packet arrival and departure times. Software timestamps are unreliable because kernel scheduling adds noise.

## Key mechanics and formulas
**T2T decomposition:**
$$T_{T2T} = T_{network\_in} + T_{decode} + T_{book\_update} + T_{signal} + T_{order\_build} + T_{risk} + T_{network\_out}$$

**Amdahl's Law for T2T optimization:**
$$S = \frac{T_{T2T,old}}{T_{T2T,new}} = \frac{T_{T2T,old}}{(T_{T2T,old} - T_{optimized} + \frac{T_{optimized}}{s})}$$

Where $T_{optimized}$ is the portion being improved and $s$ is the speedup factor for that portion.

**Percentile analysis:**
The median T2T is less important than the tail:
- P50: typical performance
- P99: 1 in 100 ticks are this slow or worse
- P99.9: worst case under normal conditions

A system with P50 = 200 ns but P99 = 5,000 ns (due to [[Garbage Collection]] or [[Memory Allocation]]) is worse than a system with P50 = 300 ns and P99 = 350 ns.

**Queue position approximation:**
$$\text{Queue position} \approx \text{rank of } T_{T2T} \text{ among competitors}$$

Revenue is roughly proportional to $\frac{1}{\text{queue position}}$ for passive fills.

## Prerequisites
- [[Hot Path]]
- [[Cold Path]]
- [[Latency]]
- [[Co-location]]
- [[Matching Engine]]

## Related concepts (learn next)
- [[Hot Path]] is the code path that determines T2T, every nanosecond on the hot path is a nanosecond of T2T.
- [[Co-location]] reduces network T2T by placing the server physically near the [[Matching Engine]].
- [[Cache Miss]] is typically the largest single contributor to T2T variability.
- [[Memory Allocation]] on the hot path causes T2T spikes in the 99th percentile.
- [[Kernel Bypass]] (DPDK, Solarflare OpenOnload) eliminates OS overhead from the network stages of T2T.
- [[FPGA]] can reduce T2T to below 100 nanoseconds by implementing the entire pipeline in hardware.
- [[Branch Prediction]] mispredictions add 5 to 7 nanoseconds each to the signal evaluation stage of T2T.
- [[Market Impact]] is what T2T optimization ultimately controls, faster execution means less information leakage.

## Common misconceptions
1. **"T2T is just software speed."** T2T includes network hardware latency (NIC, switches, cables). A software system with 100 nanosecond processing but 2 microsecond network stack has 2.1 microsecond T2T.
2. **"Median T2T is the right benchmark."** Tail latency (P99, P99.9) matters more because adverse selection is worst during volatile moments, which are exactly when tail latency spikes occur.
3. **"Sub microsecond T2T requires an FPGA."** Many competitive market makers achieve 200 to 500 nanosecond T2T with optimized C++ on commodity hardware using [[Kernel Bypass]] networking. FPGAs push below 100 nanoseconds but at much higher development cost.

## Sources
- CME Group, "iLink 3 Binary Order Entry" specification
- "Trading and Exchanges" by Larry Harris, Oxford University Press
- Cisco, "Low Latency Networking" white paper
- Solarflare (now Xilinx), "OpenOnload" kernel bypass documentation
