---
aliases: [cold path, slow path, non-critical path, batch path]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Cold Path

## Definition
The cold path is the portion of a trading system where speed is not the primary concern and correctness, maintainability, and flexibility matter more. It handles tasks that run periodically rather than on every tick: [[Risk Management]], position reconciliation, P&L calculation, regulatory reporting, and strategy parameter updates. Cold path code is typically written in Python or Java because developer productivity and library ecosystems outweigh the performance cost. The cold path communicates with the [[Hot Path]] through shared memory or message queues, feeding it updated parameters without interrupting its operation. A well designed system keeps the boundary between hot and cold paths clean and explicit.

## Why it matters (commodities and FX)
Commodity and FX trading desks generate enormous amounts of data that must be processed for risk, compliance, and strategy calibration. A copper trader on LME needs end of day P&L attribution, [[VaR]] calculations, and position limits checks. An FX desk trading EUR/USD needs real time (but not nanosecond critical) exposure aggregation across multiple venues. The cold path handles all of this. Getting the cold path wrong does not lose you a race to the [[Matching Engine]], but it can cause blown risk limits, regulatory fines, or strategy drift that bleeds money over weeks.

## Concrete example
A natural gas trading desk on CME runs a mean reversion strategy. The system architecture splits into hot and cold paths:

**Hot path (C++):** Receives Henry Hub natural gas ticks, updates the order book, prices quotes, sends orders. Runs every tick, roughly 500 nanosecond [[Tick to Trade]].

**Cold path (Python):** Every 30 seconds, recalculates the fair value model parameters (mean, standard deviation, half life) using the last 5,000 ticks. Pushes new parameters to the hot path via shared memory. Every 5 minutes, runs a [[VaR]] calculation on the portfolio. Every hour, reconciles fills against the exchange's drop copy.

**Win scenario:** The cold path detects that realized volatility in natural gas has spiked from 35% to 55%. It widens the model's quoting spread from 0.003 to 0.005 and pushes this to the hot path. The wider spread protects the desk from adverse selection during the volatile period, saving an estimated $12,000 over 2 hours.

**Fail scenario:** The cold path Python script has a memory leak. After 6 hours, the parameter update job takes 45 seconds instead of 2. The hot path continues quoting with stale parameters from a low volatility regime while the market is now in a high volatility regime. The desk loses $28,000 before a human notices.

## Key mechanics and formulas
**Cold path cycle time:**
$$T_{cold} = T_{data\_fetch} + T_{compute} + T_{publish}$$

Unlike the [[Hot Path]], $T_{cold}$ is measured in milliseconds or seconds, not nanoseconds.

**Risk update frequency trade off:**
$$\text{Staleness cost} \propto \frac{\sigma_{market}}{f_{update}}$$

Where $\sigma_{market}$ is market volatility and $f_{update}$ is the cold path update frequency. Higher volatility demands more frequent cold path cycles.

**Position reconciliation check:**
$$\Delta_{recon} = \sum \text{internal fills} - \sum \text{exchange reported fills}$$

$\Delta_{recon}$ should be 0 at all times. Any nonzero value triggers an alert.

## Prerequisites
- [[Hot Path]]
- [[Risk Management]]
- [[Latency]]

## Related concepts (learn next)
- [[Hot Path]] is the counterpart that handles tick level, latency critical operations.
- [[VaR]] is a standard risk metric calculated on the cold path.
- [[Garbage Collection]] is acceptable on the cold path because occasional pauses do not affect tick level latency.
- [[Memory Allocation]] constraints are relaxed on the cold path, allowing dynamic data structures.
- [[Position Reconciliation]] is a core cold path responsibility ensuring internal state matches the exchange.
- [[P&L Attribution]] breaks down daily profits into components like spread capture, directional, and carry.
- [[Regulatory Reporting]] (EMIR, Dodd Frank) is handled entirely on the cold path.

## Common misconceptions
1. **"The cold path does not matter for performance."** A slow cold path can starve the [[Hot Path]] of updated parameters, causing the system to trade on stale signals. Cold path latency matters, just on a different timescale (seconds, not nanoseconds).
2. **"Everything not on the hot path is cold path."** There is often a warm path for tasks like real time risk that need sub second updates but not nanosecond precision. The architecture is a spectrum, not a binary.
3. **"Python is always fine for the cold path."** For very large portfolios with complex [[Greeks]] calculations across thousands of strikes, even the cold path may need C++ or GPU acceleration to complete within acceptable cycle times.

## Sources
- "Trading and Exchanges" by Larry Harris, Oxford University Press
- "Algorithmic Trading and DMA" by Barry Johnson
- CME Group, "Risk Management for Clearing Members" documentation
- "Python for Finance" by Yves Hilpisch, O'Reilly
