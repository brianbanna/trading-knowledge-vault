---
aliases: [book skew, order book skew, microstructure skew, bid-ask imbalance]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Skew Microstructure

## Definition
Skew in microstructure refers to the asymmetry between the bid side and ask side of an [[order book]], measured by the relative volume (or number of orders) resting at or near the [[Top of Book]]. When there is more volume on the bid side than the ask side, the book is "bid-heavy" or positively skewed, suggesting stronger buying support. When ask-side volume dominates, the book is "ask-heavy" or negatively skewed, suggesting selling pressure. Book skew is one of the most robust short-term directional predictors in microstructure research: prices tend to move toward the thinner side of the book. This is intuitive because the thinner side offers less resistance to incoming market orders. Skew can be measured at just the top level ([[Top of Book]] imbalance) or across multiple levels of [[Depth of Book]], with deeper measures generally providing more stable signals.

## Why it matters (commodities and FX)
In FX, book skew on [[EBS]] and [[Reuters Matching]] predicts the direction of the next 1 to 10 seconds of price movement with statistically significant accuracy. While this horizon is too short for most human traders, it is the foundation of high-frequency [[market making]] and short-term alpha strategies. For medium-frequency systematic traders (holding periods of minutes to hours), aggregated skew metrics serve as execution timing signals: buy when the book is bid-heavy (indicating support) and delay buying when the book is ask-heavy (indicating near-term weakness). In commodity futures, the same skew dynamics apply to [[crude oil]], [[gold]], and [[copper]] order books on CME Globex. Cross-asset skew signals (e.g., AUDUSD book skew predicting copper price moves) are an active area of quantitative research.

## Concrete example
On EBS, the USDJPY top 3 levels show: bids of 15 million at 149.520, 20 million at 149.515, 12 million at 149.510 (total bid depth = 47 million). Asks of 5 million at 149.525, 8 million at 149.530, 7 million at 149.535 (total ask depth = 20 million). The depth imbalance is (47 - 20) / (47 + 20) = 0.40, strongly positive (bid-heavy). This predicts upward price movement. Over the next 5 seconds, a series of small market buy orders consume the thin ask side, pushing the price to 149.535. A high-frequency market maker who observed the skew shifted its quotes 0.3 pips higher in advance, capturing the move. Conversely, during the 2016 GBP flash crash, the GBPUSD bid side collapsed from 50+ million of depth to under 2 million within 1 second, creating extreme negative skew. The skew signal correctly predicted the continued downward cascade, but the speed of the collapse meant that even algorithmic traders had difficulty acting before the move was largely complete.

## Key mechanics and formulas
- **Top-of-book imbalance**: I = (bid size at best - ask size at best) / (bid size at best + ask size at best); ranges from -1 (all ask) to +1 (all bid)
- **Multi-level imbalance**: I(n) = (sum of bid sizes at levels 1 to n - sum of ask sizes at levels 1 to n) / (sum of bid sizes + sum of ask sizes)
- **Weighted mid-price (skew-adjusted)**: WMid = (best ask x bid size + best bid x ask size) / (bid size + ask size); when bid size > ask size, WMid shifts toward the ask
- **Predictive regression**: next price change = alpha + beta x imbalance + error; beta is consistently positive across FX and futures markets
- **Signal decay**: imbalance predictive power decays exponentially with horizon; half-life is typically 2 to 15 seconds in FX
- **Conditional skew**: measure imbalance conditional on recent trade direction (e.g., post-[[sweep]] skew is more informative than unconditional skew)

## Prerequisites
- [[Top of Book]]
- [[Depth of Book]]
- [[Order Book]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Top of Book]]: skew at the top level is the simplest and fastest-updating imbalance measure.
- [[Depth of Book]]: multi-level skew provides a more stable signal by incorporating deeper resting liquidity.
- [[Sweep]]: sweeps on one side of the book create sudden, extreme skew that persists until the book refills.
- [[Flow Signals]]: book skew is an observable proxy for latent order flow imbalance.
- [[Tick Data]]: computing real-time skew requires tick-level depth updates.
- [[Market Impact]]: skew conditions at the time of order submission affect expected impact.
- [[Positioning Signal]]: persistent skew over longer horizons can indicate broader positioning imbalances.

## Common misconceptions
1. **"Book skew is a reliable medium-frequency signal"**: Skew is a strong predictor at sub-second to 10-second horizons, but its predictive power degrades rapidly beyond that. Traders who use top-of-book skew for 5 minute or hourly trading decisions are likely overfitting to noise.
2. **"Symmetric books mean no directional bias"**: A perfectly balanced book can be followed by a large directional move if a hidden iceberg order or off-book flow (from a [[Single Dealer Platform]]) is about to hit. Visible skew captures only publicly displayed liquidity.
3. **"Bid-heavy always means the price goes up"**: In some cases, large visible bid-side liquidity is "spoofing" or a temporary wall that will be pulled. Sophisticated participants learn to distinguish genuine depth from transient or deceptive orders.

## Sources
- Cont, Rama, Kukanov, Arseniy, Stoikov, Sasha, "The Price Impact of Order Book Events," Journal of Financial Econometrics (2014)
- Cartea, Alvaro et al., "Algorithmic and High-Frequency Trading," Cambridge University Press (2015)
- Cao, Charles, Hansch, Oliver, Wang, Xiaoxin, "The Information Content of an Open Limit-Order Book," Journal of Futures Markets (2009)
