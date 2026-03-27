---
aliases: [TCA, transaction cost analysis, execution analysis, post-trade analysis]
tags:
  - "#execution"
date-added: "2026-03-27"
---

# TCA

## Definition
Transaction Cost Analysis (TCA) is the process of measuring and evaluating execution quality after a trade is completed. It compares actual fill prices against benchmarks such as [[VWAP]], [[TWAP]], arrival price, or close price to determine how much the execution cost. TCA answers the question: "did we execute well, and how could we do better?" It decomposes total cost into components: [[Bid-Ask Spread]] crossing, [[Market Impact]], timing cost, and opportunity cost. TCA is used by buy side firms to evaluate brokers and algorithms, by sell side firms to demonstrate execution quality, and by regulators to enforce [[Best Execution]] obligations. Modern TCA goes beyond simple benchmark comparison to include peer analysis, venue analysis, and predictive models.

## Why it matters (commodities and FX)
Commodity and FX markets have unique TCA challenges. Brent crude trades on ICE, CME (via WTI), and OTC swap markets simultaneously, making venue comparison critical. FX has no central exchange, so [[Best Execution]] requires comparing fills across 15+ ECN venues and bank liquidity pools. A copper trader on LME who consistently pays 3 ticks more than [[VWAP]] is leaking $75 per lot, which across 500 lots per day is $37,500 daily. Without TCA, this bleed is invisible. TCA also reveals whether the [[POV]] algorithm outperforms [[TWAP]] for this particular instrument and order size, directly informing future execution decisions.

## Concrete example
An energy trading desk executes 200 trades per month in Brent crude, WTI, and natural gas futures. The head of execution runs monthly TCA.

**Sample TCA report for March:**

| Metric | Brent (ICE) | WTI (CME) | Nat Gas (CME) |
|--------|------------|-----------|---------------|
| Trades | 80 | 70 | 50 |
| Avg order size | 500 lots | 300 lots | 200 lots |
| Avg IS vs arrival (bps) | 3.2 | 2.8 | 5.1 |
| Avg IS vs VWAP (bps) | 1.1 | 0.9 | 2.3 |
| % filled | 97% | 99% | 94% |
| Best algo | POV 8% | VWAP | POV 5% |

**Win scenario:** TCA reveals that natural gas has significantly higher IS (5.1 bps vs arrival) than the other products. Investigation shows the desk was using 15% [[POV]], which is too aggressive for natural gas's thinner liquidity. Reducing to 5% POV drops IS to 2.8 bps. Monthly savings: 2.3 bps x 200 lots x 50 trades x $10,000 per lot = $23,000.

**Fail scenario:** The desk ignores TCA for 6 months. During this period, Broker A's algorithm degrades due to a software update, adding 2 basis points of [[Slippage]] per trade. Undetected, this costs the desk: 2 bps x average notional x 1,200 trades = $480,000 over 6 months. Quarterly TCA would have caught this within 3 months.

## Key mechanics and formulas
**Benchmark comparisons:**

1. **VS VWAP:**
$$\text{Cost}_{VWAP} = \frac{\bar{P}_{exec} - P_{VWAP}}{P_{VWAP}} \times 10{,}000 \text{ (bps)}$$

2. **VS Arrival price:**
$$\text{Cost}_{arrival} = \frac{\bar{P}_{exec} - P_{arrival}}{P_{arrival}} \times 10{,}000 \text{ (bps)}$$

3. **VS Close:**
$$\text{Cost}_{close} = \frac{\bar{P}_{exec} - P_{close}}{P_{close}} \times 10{,}000 \text{ (bps)}$$

For buy orders, positive values mean the execution cost more than the benchmark (bad). For sell orders, negative values mean worse execution.

**Implementation shortfall decomposition (used in TCA):**
$$IS = \text{spread cost} + \text{impact cost} + \text{timing cost} + \text{opportunity cost}$$

See [[Implementation Shortfall]] for the full formula.

**Reversion analysis (detecting market impact):**
$$\text{Reversion} = P_{exec,last} - P_{30min\_post}$$

If the price reverts significantly after the last fill, the algorithm likely caused temporary [[Market Impact]].

**Participation rate analysis:**
$$\rho_{actual} = \frac{Q_{filled}}{V_{market,during\_exec}}$$

Compare against the target rate to check algo compliance.

## Prerequisites
- [[Implementation Shortfall]]
- [[VWAP]]
- [[Slippage]]
- [[Market Impact]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Implementation Shortfall]] is the primary cost metric used in TCA reports.
- [[VWAP]] is the most common benchmark for intraday execution comparison.
- [[POV]] and [[TWAP]] are algorithms whose performance TCA evaluates head to head.
- [[Smart Order Routing]] quality is assessed through venue level TCA, showing fill rates and price improvement per venue.
- [[Market Impact]] measurement in TCA separates temporary impact (which reverts) from permanent impact (information).
- [[Best Execution]] is the regulatory obligation that TCA helps firms demonstrate compliance with.
- [[Arrival Price]] is the benchmark that aligns most closely with the portfolio manager's decision, making it the gold standard for IS based TCA.

## Common misconceptions
1. **"Beating VWAP means good execution."** [[VWAP]] is easy to beat if you trade against the trend (buy on dips, sell on rallies), but this is just luck, not skill. TCA must adjust for trade difficulty: buying into a rising market should be evaluated differently than buying into a falling one.
2. **"TCA is only post trade."** Modern TCA includes pre trade cost estimation (predicting IS before executing) and real time monitoring (tracking IS during execution). Post trade analysis alone cannot prevent bad execution, only detect it.
3. **"One benchmark fits all."** Different order types need different benchmarks. Market orders should be measured vs arrival price. Passive algorithms vs VWAP. Portfolio rebalances vs close. Using the wrong benchmark produces misleading TCA results.
4. **"TCA is just a compliance exercise."** The best desks use TCA as a continuous improvement tool: testing new algorithms, optimizing participation rates, selecting brokers, and calibrating [[Market Impact]] models.

## Sources
- "Algorithmic Trading and DMA" by Barry Johnson
- "Optimal Trading Strategies" by Robert Kissell
- CFA Institute, "Trade Management Guidelines"
- MiFID II, "Best Execution" regulatory framework
- "The Market Microstructure Approach to FX" by Carol Osler
