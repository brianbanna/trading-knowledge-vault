---
aliases: [tick data, tick-by-tick data, raw market data]
tags:
  - "#microstructure"
  - "#quant"
date-added: "2026-03-20"
---

# Tick Data

## Definition
Tick data is the most granular form of market data, recording every individual trade execution and quote update with precise timestamps (typically to the microsecond or nanosecond). Each "tick" represents a discrete market event: a trade at a specific price and size, a new bid or offer posted, or a cancellation of an existing order. In FX, tick data from [[ECN]]s like [[EBS]] captures every quote change and trade on the platform, generating millions of data points per day for a single currency pair. Unlike [[Aggregated Data]] (OHLC bars), tick data preserves the full sequence and timing of market events, making it the essential raw material for [[microstructure]] research, high-frequency strategy development, and precise [[transaction cost analysis]]. Working with tick data requires significant computational infrastructure because file sizes for a single pair can reach several gigabytes per day.

## Why it matters (commodities and FX)
Tick data is the foundation of quantitative microstructure research in both FX and commodities. Phenomena like [[sweep]] detection, [[Skew Microstructure|book skew]] computation, [[spread]] dynamics, and [[market impact]] estimation are impossible to study without tick-level resolution. For FX, tick data reveals patterns invisible in aggregated bars: the precise sequence of quote changes before and after the [[FX Fix]], the speed of [[depth of book]] replenishment after a large trade, and the microsecond-level latency advantages of co-located traders on [[ECN]]s. In commodity futures, tick data from CME Globex allows researchers to measure the exact speed at which crude oil prices respond to inventory announcements or OPEC headlines. Systematic trading firms that operate at medium frequency (1 minute to 1 hour holding periods) use tick data for strategy research and calibration even if their live execution does not require tick-by-tick processing.

## Concrete example
A quant researcher at a systematic fund downloads 1 month of EBS tick data for EURUSD: approximately 45 million quote updates and 3 million trade records. She filters for the [[FX Fix]] window (15:57:30 to 16:02:30 London time) on each of the 22 trading days. At tick resolution, she observes that on month-end dates, the spread widens from 0.1 pips to 0.8 pips starting 30 seconds before the fix window opens, and [[depth of book]] drops 70%. Trade-by-trade analysis shows that 60% of fix-window volume consists of [[sweep]]s consuming 3 or more price levels. She builds a signal: when the pre-fix spread widening exceeds 0.5 pips, the post-fix reversal averages 8 pips (profitable for a mean-reversion strategy). The same analysis on 5 minute OHLC data would only show a single bar with a wide range; the sequencing and spread dynamics would be invisible. In a failure case, a different researcher used tick data without proper timestamp alignment and found a spurious "predictive" signal that disappeared after accounting for a 50 millisecond clock offset between trade and quote feeds.

## Key mechanics and formulas
- **Tick types**: Trade ticks (price, size, timestamp, aggressor side) and quote ticks (bid price, bid size, ask price, ask size, timestamp)
- **Tick frequency**: EURUSD on EBS averages 1,000 to 3,000 quote updates per second during London/NY overlap
- **Data volume**: approximately 2 to 5 GB per pair per day for full depth-of-book tick data
- **Realized volatility from ticks**: RV = sqrt(sum of (log(P(i+1) / P(i)))^2) for all consecutive trade prices P(i)
- **Microstructure noise correction**: raw tick-based RV overestimates true volatility due to bid-ask bounce; corrected RV uses methods like the realized kernel estimator
- **Tick-to-bar aggregation**: OHLC bars are constructed from tick data by selecting open (first tick), high (max), low (min), close (last tick), and volume (sum) within each time interval
- **Event time vs. clock time**: ticks can be aggregated by number of trades (trade bars), volume (volume bars), or dollar amount (dollar bars) rather than fixed time intervals

## Prerequisites
- [[Bid-Ask Spread]]
- [[Top of Book]]
- [[Order Book]]
- [[Time Series]]

## Related concepts (learn next)
- [[Aggregated Data]]: tick data compressed into OHLC bars for easier analysis at the cost of information loss.
- [[Top of Book]]: the most frequently updating component of tick data.
- [[Depth of Book]]: full depth tick data (Level 3) captures changes at every price level.
- [[Sweep]]: detected by analyzing consecutive trade ticks at increasing price levels within a short window.
- [[Skew Microstructure]]: computed from quote-tick snapshots of bid and ask sizes.
- [[Flow Signals]]: derived from signed trade ticks (classifying each trade as buyer or seller initiated).
- [[ECN]]: the primary source of FX tick data.

## Common misconceptions
1. **"More granular data always produces better strategies"**: Tick data contains significant [[microstructure noise]] (bid-ask bounce, phantom quotes, timestamp misalignment) that can corrupt statistical analysis. Strategies designed at tick frequency require careful noise handling that is unnecessary at lower frequencies.
2. **"Tick data from one venue represents the whole market"**: EBS tick data captures only the portion of FX volume that trades on EBS. Since [[internalization]] on [[Single Dealer Platform]]s handles 60 to 70% of spot volume, EBS ticks are a partial and potentially biased sample of total market activity.
3. **"Tick data is easy to store and process"**: A single year of full depth tick data for 10 FX pairs requires multiple terabytes of storage and specialized database infrastructure (e.g., kdb+, Arctic, InfluxDB). Many researchers underestimate the engineering investment required.

## Sources
- Dacorogna, Michel et al., "An Introduction to High-Frequency Finance," Academic Press (2001)
- Ait-Sahalia, Yacine, Jacod, Jean, "High-Frequency Financial Econometrics," Princeton University Press (2014)
- de Prado, Marcos Lopez, "Advances in Financial Machine Learning," Wiley (2018)
