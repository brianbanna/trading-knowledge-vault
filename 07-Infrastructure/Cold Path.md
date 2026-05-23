---
aliases: [cold path, slow path, non-critical path, batch path]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Cold Path

## Definition
The cold path is the portion of a trading system where correctness, maintainability, and flexibility matter more than raw speed. It runs periodically rather than per tick: [[Risk Management]], position reconciliation, P&L, regulatory reporting, strategy parameter updates. Cold path code is written in Python or Java because developer productivity and library ecosystems outweigh the performance cost. It communicates with the [[Hot Path]] through shared memory or message queues, pushing updated parameters without interrupting it. A clean, explicit hot/cold boundary defines a well designed system.

## Why it matters (commodities and FX)
Commodity and FX desks generate massive data that must be processed for risk, compliance, and strategy calibration. A copper trader on LME needs end of day P&L attribution, [[VaR]], and position limit checks. An FX desk on EUR/USD needs real time (not nanosecond critical) exposure aggregation across venues. The cold path handles all of this. A broken cold path will not lose you the race to the [[Matching Engine]], but it can blow risk limits, trigger fines, or drift strategy parameters and bleed money over weeks.

## Concrete example
**Concrete:** Natural gas mean reversion desk on CME. Hot path in C++: receives ticks, updates the book, prices quotes, sends orders, 500 ns [[Tick to Trade]]. Cold path in Python: every 30 seconds, recalculates fair value model parameters (mean, stdev, half life) over the last 5,000 ticks and pushes them through shared memory; every 5 minutes runs [[VaR]]; every hour reconciles fills against the exchange drop copy. The cold path detects realized vol spiking from 35% to 55%, widens the model spread from 0.003 to 0.005, and pushes it to the hot path. The wider spread protects the desk during the volatile period and saves an estimated $12,000 over 2 hours.

**Simplified:** Two parts of the system. The fast part trades on every tick. The slow part runs every few seconds or minutes to recalibrate, check risk, and report. The slow part feeds parameters to the fast part. The slow part is written in Python because development speed beats microseconds. Done right, you get fast trading without sacrificing flexibility for risk and analytics.

## Key mechanics and formulas
**Cold path cycle time:**
$$T_{cold} = T_{data\_fetch} + T_{compute} + T_{publish}$$

Unlike [[Hot Path]], $T_{cold}$ runs in milliseconds or seconds.

**Risk update frequency tradeoff:**
$$\text{Staleness cost} \propto \frac{\sigma_{market}}{f_{update}}$$

Where $\sigma_{market}$ is market volatility and $f_{update}$ is cold path update frequency. Higher vol demands more frequent cycles.

**Position reconciliation check:**
$$\Delta_{recon} = \sum \text{internal fills} - \sum \text{exchange reported fills}$$

$\Delta_{recon}$ must be 0 at all times. Any nonzero value triggers an alert.

## Prerequisites
- [[Hot Path]]
- [[Risk Management]]
- [[Latency]]

## Related concepts (learn next)
- [[Hot Path]] is the counterpart handling tick level, latency critical operations.
- [[VaR]] is a standard risk metric calculated on the cold path.
- [[Garbage Collection]] is acceptable on the cold path because pauses do not affect tick latency.
- [[Memory Allocation]] constraints are relaxed, allowing dynamic data structures.
- [[Position Reconciliation]] is a core cold path responsibility.
- [[P&L Attribution]] breaks down daily profits into spread capture, directional, and carry.
- [[Regulatory Reporting]] (EMIR, Dodd Frank) lives entirely on the cold path.

## Common misconceptions
1. **"The cold path does not matter for performance."** A slow cold path starves the [[Hot Path]] of updated parameters, forcing trading on stale signals. Cold path latency matters, on a different timescale.
2. **"Everything not on the hot path is cold path."** Often a warm path handles real time risk needing sub second updates without nanosecond precision. The architecture is a spectrum.
3. **"Python is always fine for the cold path."** For large portfolios with complex [[Greeks]] across thousands of strikes, even the cold path may need C++ or GPU to finish within cycle time.

## Sources
- "Trading and Exchanges" by Larry Harris, Oxford University Press
- "Algorithmic Trading and DMA" by Barry Johnson
- CME Group, "Risk Management for Clearing Members" documentation
- "Python for Finance" by Yves Hilpisch, O'Reilly
