---
aliases: [book skew, order book skew, microstructure skew, bid-ask imbalance]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Skew Microstructure

## Definition
Skew in microstructure is the asymmetry between the bid side and ask side of an [[order book]], measured by relative volume at or near [[Top of Book]]. More volume on the bid than ask: book is bid heavy, positively skewed, suggesting buying support. Ask side dominates: ask heavy, negatively skewed, suggesting selling pressure. Prices tend to move toward the thinner side because it offers less resistance to incoming market orders. Book skew is one of the most robust short term directional predictors in microstructure research. Measure at the top level ([[Top of Book]] imbalance) or across multiple levels of [[Depth of Book]]; deeper measures usually give more stable signals.

## Why it matters (commodities and FX)
In FX, book skew on [[EBS]] and [[Reuters Matching]] predicts direction of the next 1 to 10 seconds with statistically significant accuracy. This horizon is too short for human traders but is the foundation of high frequency [[market making]] and short term alpha. For medium frequency systematic traders (minutes to hours), aggregated skew serves as execution timing: buy when book is bid heavy (support), delay buying when ask heavy (near term weakness). In commodity futures, the same dynamics apply to [[crude oil]], [[gold]], and [[copper]] on CME Globex. Cross asset skew (AUDUSD book predicting copper) is an active area of quant research.

## Concrete example

**Concrete:** EBS USDJPY top 3 levels: bids 15M at 149.520, 20M at 149.515, 12M at 149.510 (47M total). Asks 5M at 149.525, 8M at 149.530, 7M at 149.535 (20M total). Imbalance (47 - 20) / (47 + 20) = 0.40, strongly bid heavy. Predicts upward movement. Over next 5 seconds, small market buys consume thin ask side, pushing price to 149.535. HF market maker observing the skew shifted quotes 0.3 pips higher in advance, capturing the move. During 2016 GBP flash crash, GBPUSD bid side collapsed from 50M+ depth to under 2M within 1 second, creating extreme negative skew. Signal correctly predicted continued downward cascade, but the collapse speed meant even algos struggled to act before the move was largely complete.

**Simplified:** Look at the order book. If there is much more volume buying than selling, the price probably ticks up next. Why? Because thin side offers less resistance to incoming orders. Big buyers, thin sellers, price has to move up to fill orders. The signal works at very short horizons and decays quickly.

## Key mechanics and formulas
- **Top of book imbalance**: I = (bid size - ask size) / (bid size + ask size); -1 to +1
- **Multi level imbalance**: I(n) = (sum bid sizes levels 1 to n - sum ask sizes 1 to n) / (sum bid + sum ask)
- **Weighted mid (skew adjusted)**: WMid = (ask x bid size + bid x ask size) / (bid size + ask size); when bid > ask size, WMid shifts toward ask
- **Predictive regression**: next price change = alpha + beta x imbalance + error; beta consistently positive across FX and futures
- **Signal decay**: imbalance predictive power decays exponentially with horizon; half life 2 to 15s in FX
- **Conditional skew**: imbalance conditional on recent trade direction (post [[sweep]] skew is more informative)

## Prerequisites
- [[Top of Book]]
- [[Depth of Book]]
- [[Order Book]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Top of Book]]: skew at top level is the simplest and fastest updating measure
- [[Depth of Book]]: multi level skew gives a more stable signal
- [[Sweep]]: sweeps create sudden, extreme skew that persists until book refills
- [[Flow Signals]]: book skew is an observable proxy for latent order flow imbalance
- [[Tick Data]]: real time skew needs tick level depth updates
- [[Market Impact]]: skew at submission affects expected impact
- [[Positioning Signal]]: persistent skew over longer horizons indicates broader positioning

## Common misconceptions
1. **"Book skew is a reliable medium frequency signal"**: skew predicts at sub second to 10 second horizons. Predictive power degrades fast beyond that. Using top of book skew for 5 minute or hourly decisions is overfitting noise.
2. **"Symmetric books mean no directional bias"**: a balanced book can precede a large move if a hidden iceberg or off book flow from an [[Single Dealer Platform]] is about to hit. Visible skew captures only displayed liquidity.
3. **"Bid heavy always means price goes up"**: large visible bid liquidity is sometimes spoofing or a wall that gets pulled. Sophisticated participants learn to separate genuine depth from deceptive orders.

## Sources
- Cont, Rama, Kukanov, Arseniy, Stoikov, Sasha, "The Price Impact of Order Book Events," Journal of Financial Econometrics (2014)
- Cartea, Alvaro et al., "Algorithmic and High-Frequency Trading," Cambridge University Press (2015)
- Cao, Charles, Hansch, Oliver, Wang, Xiaoxin, "The Information Content of an Open Limit-Order Book," Journal of Futures Markets (2009)
