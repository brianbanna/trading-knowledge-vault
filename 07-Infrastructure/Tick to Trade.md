---
aliases: [tick to trade, tick-to-trade, T2T, end-to-end latency, wire-to-wire]
tags:
  - "#infrastructure"
  - "#execution"
date-added: "2026-03-27"
---

# Tick to Trade

## Definition
Tick to trade (T2T) is the total elapsed time from a market data update arriving at the trading system's network interface to the resulting order leaving that same interface for the exchange. It is the single most important latency metric for a latency sensitive system. T2T spans network receive, market data decoding, order book update, signal/pricing, order construction, risk checks, and network transmit. For HFT market makers, T2T is in nanoseconds (100 to 500 ns). For medium frequency systematic traders, microseconds to milliseconds. Reducing T2T requires optimizing every component on the [[Hot Path]]: [[Cache Locality]], no [[Memory Allocation]], minimal [[Branch Prediction]] misses, and no [[Garbage Collection]].

## Why it matters (commodities and FX)
In commodity futures on CME and ICE, queue position decides profitability for market makers. First quote at a price level fills first. A Brent market maker at 200 ns T2T consistently beats a competitor at 500 ns. Over a trading day this is thousands of extra fills and hundreds of thousands in spread capture. In FX, where EUR/USD trades on multiple [[ECN]]s simultaneously, T2T decides whether a cross venue arbitrage gets captured. An opportunity might exist for 5 microseconds. A 10 microsecond T2T system cannot exploit it; a 1 microsecond system can.

## Concrete example
**Concrete:** WTI market maker on CME Globex receives a trade message at $72.45 and must update its quote. T2T breakdown (optimized C++, co located):

| Stage | Time |
|-------|------|
| NIC to userspace (kernel bypass) | 50 ns |
| Decode CME MDP 3.0 binary | 40 ns |
| Update internal book | 30 ns |
| Evaluate pricing model | 60 ns |
| Construct FIX/iLink order | 30 ns |
| Pre trade risk check | 20 ns |
| Serialize and write to NIC | 40 ns |
| **Total T2T** | **270 ns** |

270 ns puts the system 2nd out of 12 competing market makers. Top 3 firms share roughly 60% of passive fills on WTI. The system captures 4,000 fills per day at $12.50 average, $50,000 daily gross. A new regulatory compliance check adds 2 [[Cache Miss]]es (200 ns). T2T jumps to 470 ns. The system drops from rank 2 to rank 7. Daily fills fall to 1,200. Gross drops to $15,000. Measurement: use hardware NIC timestamps. Software timestamps are unreliable because kernel scheduling adds noise.

**Simplified:** T2T is the full round trip clock inside your machine: data comes in the network card, your code reacts, an order goes back out the same card. Everything in between is your T2T budget. Hot path code, network stack, risk checks, all of it. The best firms measure this in nanoseconds and obsess about every step.

## Key mechanics and formulas
**T2T decomposition:**
$$T_{T2T} = T_{network\_in} + T_{decode} + T_{book\_update} + T_{signal} + T_{order\_build} + T_{risk} + T_{network\_out}$$

**Amdahl's Law for T2T:**
$$S = \frac{T_{T2T,old}}{T_{T2T,new}} = \frac{T_{T2T,old}}{(T_{T2T,old} - T_{optimized} + \frac{T_{optimized}}{s})}$$

Where $T_{optimized}$ is the portion being improved and $s$ is its speedup factor.

**Percentile analysis:**
Median T2T matters less than the tail:
- P50: typical performance
- P99: 1 in 100 ticks this slow or worse
- P99.9: worst case under normal conditions

A system with P50 = 200 ns but P99 = 5,000 ns (from [[Garbage Collection]] or [[Memory Allocation]]) is worse than one at P50 = 300 ns and P99 = 350 ns.

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
- [[Hot Path]] is the code path that determines T2T. Every nanosecond on it is T2T.
- [[Co-location]] reduces network T2T by placing the server near the [[Matching Engine]].
- [[Cache Miss]] is the largest single contributor to T2T variability.
- [[Memory Allocation]] on the hot path causes T2T spikes at the 99th percentile.
- [[Kernel Bypass]] (DPDK, Solarflare OpenOnload) removes OS overhead from network stages.
- [[FPGA]] can reduce T2T below 100 ns by implementing the entire pipeline in hardware.
- [[Branch Prediction]] mispredictions add 5 to 7 ns each to signal evaluation.
- [[Market Impact]] is what T2T optimization ultimately controls. Faster execution means less information leakage.

## Common misconceptions
1. **"T2T is just software speed."** T2T includes network hardware (NIC, switches, cables). A system with 100 ns processing but a 2 microsecond network stack has 2.1 microsecond T2T.
2. **"Median T2T is the right benchmark."** Tail latency (P99, P99.9) matters more because adverse selection peaks during volatile moments, which are exactly when tail spikes occur.
3. **"Sub microsecond T2T requires an FPGA."** Many competitive market makers hit 200 to 500 ns T2T with optimized C++ on commodity hardware using [[Kernel Bypass]] networking. FPGAs push below 100 ns at much higher development cost.

## Sources
- CME Group, "iLink 3 Binary Order Entry" specification
- "Trading and Exchanges" by Larry Harris, Oxford University Press
- Cisco, "Low Latency Networking" white paper
- Solarflare (now Xilinx), "OpenOnload" kernel bypass documentation
