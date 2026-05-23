---
aliases: [sweep, book sweep, depth sweep]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-20"
---

# Sweep

## Definition
A sweep is when a market order or aggressive limit order is large enough to consume all liquidity at [[Top of Book]] and continue filling at successively worse levels in [[Depth of Book|the book]]. The order sweeps through multiple price levels, producing a VWAP execution worse than the best bid or offer at submission. Sweeps are the primary mechanism through which large orders create [[market impact]]. Detecting sweeps in real time is valuable because they signal aggressive, often informed trading. A buyer sweeping 5 levels of asks expresses urgency suggesting directional information. Sweep detection is a core component of short term alpha models and [[flow signals]] strategies.

## Why it matters (commodities and FX)
In FX, sweeps on [[ECN]]s like [[EBS]] are visible to all participants and signal aggressive directional intent. When a large bank or hedge fund sweeps the USDJPY book, algo market makers immediately widen quotes and reduce depth, amplifying the move. In commodity futures, sweeps on CME Globex for [[crude oil]] or [[gold]] often precede 5 to 15 tick directional moves as participants react. For execution, avoiding unnecessary sweeps is a key objective of [[TWAP]], [[VWAP]], and slicing algos. For alpha, detecting sweeps in correlated instruments (a sweep in AUDUSD signaling copper direction) creates [[cross-asset]] opportunities.

## Concrete example

**Concrete:** 14:30 UTC, EURUSD asks on EBS: 8M at 1.08525, 12M at 1.08530, 15M at 1.08535, 10M at 1.08540. Hedge fund sends market buy 40M. Fill: 8M at 1.08525, 12M at 1.08530, 15M at 1.08535, 5M at 1.08540. VWAP 1.08532, 0.95 pips worse than pre sweep mid 1.085225. Sweep visible immediately to all EBS participants. Algo makers pull bids and reset quotes 1 to 2 pips higher. Within 500ms, EURUSD trades 1.08545/1.08550, a 2.5 pip move. Fast systematic trader who detected the sweep bought 10M at 1.08540 and sold at 1.08550, capturing 1 pip. False signal case: one time corporate hedging flow with no follow through, price reverts to 1.08525 within 30s, systematic loses 1.5 pips.

**Simplified:** A sweep is a big order that eats through several price levels at once. The first chunk fills at the best price, the rest at progressively worse prices. Everyone watching sees it happen. Other traders react by pulling their orders and pushing the market further in the same direction. Useful as a real time signal that someone aggressive and possibly informed is moving.

## Key mechanics and formulas
- **Sweep cost**: VWAP of fills - mid at submission
- **Sweep depth**: number of price levels consumed
- **Sweep volume ratio**: SVR = sweep volume / average top of book size; SVR > 3 is a meaningful sweep
- **Price impact of sweep**: last fill price - first fill price (range traversed)
- **Sweep detection rule**: flag when a single order fills at 3+ consecutive price levels within a short window (e.g., 100ms)
- **Post sweep reversion**: price 30s after - price immediately after; positive reversion means the sweep carried permanent information

## Prerequisites
- [[Top of Book]]
- [[Depth of Book]]
- [[Market Impact]]
- [[Order Book]]

## Related concepts (learn next)
- [[Top of Book]]: the first level consumed; sweep begins when top of book depth is exhausted
- [[Depth of Book]]: total depth determines how far a sweep travels and how much it costs
- [[Skew Microstructure]]: a sweep creates immediate skew as depth depletes asymmetrically
- [[Flow Signals]]: sweep detection is one of the most reliable short term flow signals
- [[Market Impact]]: sweeps are the most direct measurable form
- [[Tick Data]]: sweep detection needs tick level trade and quote data with precise timestamps
- [[Aggregated Data]]: sweeps inside a single OHLC bar are invisible at the bar level

## Common misconceptions
1. **"All sweeps signal informed trading"**: many sweeps are passive institutional flow ([[FX Fix]] rebalancing, corporate hedging) with no directional information beyond the immediate order. Separating informed from uninformed is the alpha challenge.
2. **"Avoiding sweeps is always optimal"**: sometimes urgency beats cost. Time sensitive information (reacting to a central bank announcement) makes sweeping immediately the right call. Slicing the order risks missing the move.
3. **"Sweep impact is permanent"**: research shows 40 to 70% of sweep impact reverts within 1 to 5 minutes for FX majors. Only the permanent component reflects genuine information; the temporary component is a liquidity premium that dissipates as the book refills.

## Sources
- Cont, Rama, Kukanov, Arseniy, Stoikov, Sasha, "The Price Impact of Order Book Events," Journal of Financial Econometrics (2014)
- Cartea, Alvaro et al., "Algorithmic and High-Frequency Trading," Cambridge University Press (2015)
- Bouchaud, Jean-Philippe et al., "How Markets Slowly Digest Changes in Supply and Demand," Quantitative Finance (2009)
