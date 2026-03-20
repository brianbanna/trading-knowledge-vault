---
aliases: [sweep, book sweep, depth sweep]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-20"
---

# Sweep

## Definition
A sweep occurs when a market order or aggressive limit order is large enough to consume all available liquidity at the [[Top of Book]] and continue filling at successively worse price levels deeper in the [[Depth of Book|order book]]. The order "sweeps" through multiple price levels, resulting in a volume-weighted average execution price that is significantly worse than the best bid or offer at the time the order was submitted. Sweeps are the primary mechanism through which large orders create [[market impact]]. In microstructure analysis, detecting sweeps in real-time is valuable because they signal aggressive, often informed trading. A buyer who sweeps 5 levels of the ask side is expressing urgency that suggests they possess directional information. Sweep detection is a core component of many short-term alpha models and [[flow signals]] strategies.

## Why it matters (commodities and FX)
In FX, sweeps on [[ECN]]s like [[EBS]] are observable by all participants and serve as a public signal of aggressive directional intent. When a large bank or hedge fund sweeps the USDJPY order book, algorithmic market makers immediately widen their quotes and reduce depth, amplifying the initial price move. In commodity futures, sweeps on CME Globex for [[crude oil]] or [[gold]] futures often precede 5 to 15 tick directional moves as other participants react to the signal. For execution, avoiding unnecessary sweeps is a key objective of [[TWAP]], [[VWAP]], and other slicing algorithms. For alpha generation, detecting sweeps in competing instruments (e.g., a sweep in AUDUSD as a signal for copper direction) creates [[cross-asset]] trading opportunities.

## Concrete example
At 14:30 UTC, the EURUSD ask side on EBS shows: 8 million at 1.08525, 12 million at 1.08530, 15 million at 1.08535, 10 million at 1.08540. A hedge fund sends a market buy for 40 million. The fill: 8 million at 1.08525, 12 million at 1.08530, 15 million at 1.08535, and 5 million at 1.08540. VWAP = 1.08532, which is 0.95 pips worse than the pre-sweep mid-price of 1.085225. The sweep is immediately visible to all EBS participants. Algorithmic market makers pull their remaining bids and reset quotes 1 to 2 pips higher. Within 500 milliseconds, EURUSD is trading at 1.08545/1.08550, a 2.5 pip move from the pre-sweep level. A fast systematic trader who detected the sweep in real-time bought 10 million at 1.08540 and sold at 1.08550, capturing 1 pip. However, if the sweep was a false signal (e.g., a one-time corporate hedging flow with no follow-through), the price reverts to 1.08525 within 30 seconds, and the systematic trader loses 1.5 pips.

## Key mechanics and formulas
- **Sweep cost**: Sweep cost = VWAP of fills - mid-price at time of order submission
- **Sweep depth**: the number of price levels consumed; Sweep depth = number of levels where volume was filled
- **Sweep volume ratio**: SVR = sweep volume / average top-of-book size; SVR > 3 typically constitutes a meaningful sweep
- **Price impact of sweep**: Impact = last fill price - first fill price (the range of prices traversed)
- **Sweep detection rule**: Flag a sweep when a single order fills at 3 or more consecutive price levels within a short window (e.g., 100 milliseconds)
- **Post-sweep reversion**: Reversion = price 30 seconds after sweep - price immediately after sweep; positive reversion means the sweep carried permanent information

## Prerequisites
- [[Top of Book]]
- [[Depth of Book]]
- [[Market Impact]]
- [[Order Book]]

## Related concepts (learn next)
- [[Top of Book]]: the first level consumed in any sweep; sweep begins where top-of-book depth is exhausted.
- [[Depth of Book]]: total available depth determines how far a sweep travels and how much it costs.
- [[Skew Microstructure]]: a sweep on one side of the book creates immediate skew as depth is depleted asymmetrically.
- [[Flow Signals]]: sweep detection is one of the most reliable short-term flow signals.
- [[Market Impact]]: sweeps are the most direct and measurable form of market impact.
- [[Tick Data]]: sweep detection requires tick-level trade and quote data with precise timestamps.
- [[Aggregated Data]]: sweeps that occur within a single OHLC bar may be invisible in aggregated data.

## Common misconceptions
1. **"All sweeps signal informed trading"**: Many sweeps are caused by passive institutional flow (e.g., [[FX Fix]] rebalancing, corporate hedging) that has no directional information beyond the immediate order. Distinguishing informed from uninformed sweeps is the key challenge for alpha extraction.
2. **"Avoiding sweeps is always optimal"**: Sometimes urgency matters more than cost. If a trader has time-sensitive information (e.g., reacting to a central bank announcement), sweeping the book immediately captures the opportunity before the market adjusts. Slicing the order into small pieces risks missing the move entirely.
3. **"Sweep impact is permanent"**: Empirical research shows that 40 to 70% of sweep impact reverts within 1 to 5 minutes for FX majors. Only the "permanent" component reflects genuine information; the "temporary" component is a liquidity premium that dissipates as the book refills.

## Sources
- Cont, Rama, Kukanov, Arseniy, Stoikov, Sasha, "The Price Impact of Order Book Events," Journal of Financial Econometrics (2014)
- Cartea, Alvaro et al., "Algorithmic and High-Frequency Trading," Cambridge University Press (2015)
- Bouchaud, Jean-Philippe et al., "How Markets Slowly Digest Changes in Supply and Demand," Quantitative Finance (2009)
