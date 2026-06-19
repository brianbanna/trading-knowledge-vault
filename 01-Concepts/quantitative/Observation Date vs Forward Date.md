---
aliases: [observation date, forward date, value date, as-of date, forward curve data structure, constant maturity series, fixed contract series]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-06-19"
---

# Observation Date vs Forward Date

## Definition

A table of forward or futures prices has 2 different date axes, and they answer 2 different questions. The **observation date** (also value date or as-of date) is the day the price was recorded: when you looked. The **forward date** (also delivery date, maturity, expiry, or contract month) is the delivery the price is for: what you looked at. On any single observation date you see the entire [[Forward Curve]] at once, that is many forward dates side by side. Across many observation dates you see how any one point on that curve moves through time. Mixing the 2 axes is one of the most common data handling errors in commodities, and it silently corrupts every downstream risk number.

## Why it matters (commodities and FX)

Commodity and FX forward data arrives as a 2 dimensional panel: price as a function of (observation date, forward date). To do anything quantitative you must collapse it to a 1 dimensional series, and the axis you collapse along decides what the series means.

- To measure **how a market moved**, you fix a forward point and walk the observation axis. That is a return series, the input to volatility, [[Value at Risk|VaR]], correlation, [[Beta]], and any [[Backtest|backtest]].
- To measure **what the market is pricing**, you fix one observation date and read across the forward axis. That is the curve shape: [[Contango]], [[Backwardation]], slope, curvature.

Key down the wrong axis and you compute term structure when you wanted time series, or vice versa. The numbers still look plausible, which is what makes the error dangerous. FX forwards (spot plus [[Forward Points]] per tenor) and commodity futures strips share the exact same trap.

## Concrete example

### The correct construction vs the classic error

Brent forward prices, USD per barrel, M1 is the nearest contract:

| Observation date | M1 (front) | M2 | M3 | ... | M12 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-01 | 78.00 | 77.50 | 77.10 | ... | 74.00 |
| 2026-06-02 | 78.40 | 77.85 | 77.40 | ... | 74.10 |
| 2026-06-03 | 77.90 | 77.45 | 77.05 | ... | 74.05 |

**Correct (walk the observation axis, fix the forward point).** Fix M1 and difference down the observation column:

- r(2026-06-02) = 78.40 − 78.00 = +0.40
- r(2026-06-03) = 77.90 − 78.40 = −0.50

That is the front-month return series. Feed it to a vol or VaR model and it is meaningful.

**The error (read across the forward axis, one observation date).** Take only the 2026-06-01 row and difference across delivery months:

- 77.50 − 78.00 = −0.50
- 77.10 − 77.50 = −0.40

Those −0.50 and −0.40 are not returns. They are the **slope of the curve** on a single day, the [[Contango|contango]] step between adjacent contracts. Treating them as a time series tells you the market fell every period when in fact nothing moved through time at all: you measured shape and labelled it change. Annualise that as volatility and you produce a number with no relationship to risk.

### The constant maturity vs fixed contract subtlety

"Fix one forward point" hides a choice:

- **Fixed contract.** Follow a single delivery, for example Aug-2026, across observation dates. Real and tradeable, but its time to maturity shrinks every day, so its behaviour drifts and the series ends at expiry.
- **Constant maturity.** Always take the nth nearby or a fixed tenor, for example "front month" or "3 month forward". The underlying contract changes at each [[Roll Yield|roll]], so the series is comparable through time, which is what risk and factor models want.

When you splice nearby contracts into a constant maturity series, the roll injects a price gap. If on the roll day the expiring Aug-26 sits at 78.00 and the new front Sep-26 at 77.50, a naive splice prints a spurious −0.50 "return" that is pure curve, not a market move. Back adjust by subtracting that gap, exactly as a continuous back-adjusted futures series does, or the [[Contango|contango]] leaks into your P&L series as fake drift.

## Key mechanics and formulas

Let `P(t, T)` be the price observed on observation date `t` for delivery date `T`. The panel is indexed by both.

- **Curve (cross-section), one observation date `t0`:** `{ P(t0, T) : all T }`. Read across `T`. Gives shape, not returns.
- **Fixed-contract series for delivery `T*`:** `s_t = P(t, T*)` for `t` up to the expiry of `T*`. Time to maturity `T* − t` shrinks as `t` advances.
- **Constant-maturity series at tenor τ:** `c_t = P(t, t + τ)`, where the delivery date moves with `t` to hold time to maturity τ fixed. In practice take the nth nearby or interpolate between the 2 bracketing contracts.
- **Return series (the thing you actually want for risk):** difference along the `t` axis with the forward point held fixed.
  - Absolute: `r_t = c_t − c_{t−1}`
  - Log: `r_t = ln(c_t / c_{t−1})`
- **Roll adjustment** for a continuous nth-nearby series: on each roll day subtract the gap `P(t, T_new) − P(t, T_old)` so the series reflects price change, not the contract switch.

Plain English: time series differences go **down the observation axis**; curve shape reads **across the forward axis**. Never difference across forward dates and call it a return.

## Prerequisites

- [[Forward Curve]]
- [[Futures Contract Mechanics]]
- [[Forward Points]]

## Related concepts (learn next)

- [[Continuous Contract]] — how nearby contracts are spliced and back adjusted into one constant maturity series.
- [[Roll Yield]] — the return component created at each roll, the thing the back adjustment isolates and removes.
- [[Contango]] and [[Backwardation]] — the curve shapes you misread as returns when you key the wrong axis.
- [[Calendar Spread]] — a trade that is literally the difference across the forward axis on one observation date, the cross-section made tradeable.
- [[Point-in-Time Data]] — the discipline of using only data available as of each observation date, the same axis you must respect to avoid lookahead.
- [[Lookahead Bias]] — what creeps in when observation dates are misaligned with the information available then.
- [[Realized Volatility]] — computed from the return series, so it is only correct if you collapsed the right axis.

## Common misconceptions

1. **"Reading down a single day's column gives a return series."** No. A single observation date is a snapshot. Differencing across forward dates measures the term structure ([[Contango|contango]] or [[Backwardation|backwardation]]) step, a cross-section, not change through time.
2. **"A fixed contract's price history is already a clean constant maturity series."** No. Its time to maturity shrinks daily, so its volatility, sensitivity, and roll behaviour drift, and the series dies at expiry. For stable risk you need a constant maturity (rolled) series.
3. **"Splicing nearby contracts together needs no adjustment."** No. The roll injects the spread between the old and new contract as a fake return. Back adjust it out, or [[Contango|contango]] shows up as spurious drift in your P&L.
4. **"Observation date and forward date are just two labels for the same timestamp."** No. One is when the price was quoted, the other is what delivery it is for. Confusing them is the entire error: a 5 by 12 panel has 60 prices but only 5 distinct moments in time.

## Sources

- CME Group and ICE market data guides on futures settlement and contract months.
- Bloomberg generic futures convention (for example CL1, CO1 where the numeral is the nth nearby), and the GFUT roll documentation.
- Geman, Commodities and Commodity Derivatives, on forward curve dynamics and continuous series construction.
- Standard quant practice on point-in-time panels and back-adjusted continuous contracts.

---
*Status: #stub | Last reviewed: 2026-06-19*
