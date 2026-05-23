---
aliases: [tick data, tick-by-tick data, raw market data]
tags:
  - "#microstructure"
  - "#quant"
date-added: "2026-03-20"
---

# Tick Data

## Definition
Tick data is the most granular form of market data, recording every individual trade execution and quote update with precise timestamps (microsecond or nanosecond). Each tick is a discrete market event: a trade at a price and size, a new bid or offer posted, or a cancellation. In FX, tick data from [[ECN]]s like [[EBS]] captures every quote change and trade, generating millions of data points per day per pair. Unlike [[Aggregated Data]] (OHLC bars), tick data preserves full sequence and timing, making it the raw material for [[microstructure]] research, HF strategy development, and precise [[transaction cost analysis]]. Working with it needs serious infrastructure: a single pair can produce several GB per day.

## Why it matters (commodities and FX)
Tick data is the foundation of quantitative microstructure research in FX and commodities. [[sweep]] detection, [[Skew Microstructure|book skew]] computation, [[spread]] dynamics, and [[market impact]] estimation are impossible without tick resolution. For FX, ticks reveal patterns invisible in bars: precise sequence of quote changes around the [[FX Fix]], speed of [[depth of book]] replenishment after a large trade, and microsecond level latency advantages of colocated traders. In commodity futures, CME Globex ticks let researchers measure exactly how fast crude prices respond to inventory announcements or OPEC headlines. Medium frequency systematic firms (1 minute to 1 hour holding) use ticks for research and calibration even if live execution does not need tick by tick processing.

## Concrete example

**Concrete:** Quant researcher downloads 1 month of EBS EURUSD ticks: ~45M quote updates and 3M trade records. Filters for [[FX Fix]] window (15:57:30 to 16:02:30 London) on 22 trading days. At tick resolution, observes that on month end dates, spread widens 0.1 pip to 0.8 pip starting 30s before the window opens, and [[depth of book]] drops 70%. Trade by trade analysis shows 60% of fix window volume consists of [[sweep]]s consuming 3+ levels. Builds a signal: when pre fix widening exceeds 0.5 pips, post fix reversal averages 8 pips (profitable for mean reversion). Same analysis on 5 min OHLC would show only a single bar with a wide range; sequencing and spread dynamics invisible. Failure case: a researcher used ticks without proper timestamp alignment, found a spurious predictive signal that vanished after accounting for a 50ms clock offset between trade and quote feeds.

**Simplified:** Tick data is every single quote and trade with exact timestamps. Bars throw away the order events happened in; ticks keep it all. Needed for any analysis where the microstructure matters: order book dynamics, who reacted first, how the spread behaved second by second. Storage and processing are heavy.

## Key mechanics and formulas
- **Tick types**: trade ticks (price, size, timestamp, aggressor side) and quote ticks (bid price, bid size, ask price, ask size, timestamp)
- **Tick frequency**: EURUSD on EBS averages 1,000 to 3,000 quote updates/second during London/NY overlap
- **Data volume**: ~2 to 5 GB per pair per day for full depth ticks
- **Realized vol from ticks**: RV = sqrt(sum of (log(P(i+1) / P(i)))^2) for consecutive trade prices
- **Microstructure noise correction**: raw tick RV overestimates true vol due to bid ask bounce; corrected RV uses methods like the realized kernel estimator
- **Tick to bar aggregation**: OHLC built from ticks by open (first), high (max), low (min), close (last), volume (sum) within each interval
- **Event time vs clock time**: ticks aggregate by trade count (trade bars), volume (volume bars), or dollar amount (dollar bars) instead of fixed time

## Prerequisites
- [[Bid-Ask Spread]]
- [[Top of Book]]
- [[Order Book]]
- [[Time Series]]

## Related concepts (learn next)
- [[Aggregated Data]]: ticks compressed into OHLC bars, cheaper but lossy
- [[Top of Book]]: the most frequently updating component
- [[Depth of Book]]: full depth tick data (Level 3) captures every level
- [[Sweep]]: detected by analyzing consecutive trade ticks at increasing prices within a short window
- [[Skew Microstructure]]: computed from quote tick snapshots of bid and ask sizes
- [[Flow Signals]]: derived from signed trade ticks (classifying each trade as buyer or seller initiated)
- [[ECN]]: the primary FX tick source

## Common misconceptions
1. **"More granular = better strategies"**: ticks contain heavy [[microstructure noise]] (bid ask bounce, phantom quotes, timestamp misalignment) that can corrupt analysis. Tick frequency strategies need careful noise handling unnecessary at lower frequencies.
2. **"Tick data from one venue is the whole market"**: EBS ticks capture only EBS volume. Since [[internalization]] on [[Single Dealer Platform]]s handles 60 to 70% of spot, EBS is a partial and possibly biased sample.
3. **"Tick data is easy to store and process"**: a year of full depth ticks for 10 FX pairs needs multiple TB and specialized databases (kdb+, Arctic, InfluxDB). Many underestimate the engineering investment.

## Sources
- Dacorogna, Michel et al., "An Introduction to High-Frequency Finance," Academic Press (2001)
- Ait-Sahalia, Yacine, Jacod, Jean, "High-Frequency Financial Econometrics," Princeton University Press (2014)
- de Prado, Marcos Lopez, "Advances in Financial Machine Learning," Wiley (2018)
