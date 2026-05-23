---
aliases: [TCA, transaction cost analysis, execution analysis, post-trade analysis]
tags:
  - "#execution"
date-added: "2026-03-27"
---

# TCA

## Definition
Transaction Cost Analysis (TCA) measures and evaluates execution quality after the trade. It compares actual fills against benchmarks such as [[VWAP]], [[TWAP]], arrival price, or close to determine how much execution cost. TCA answers: did we execute well, and how could we do better? It decomposes total cost into [[Bid-Ask Spread]] crossing, [[Market Impact]], timing cost, and opportunity cost. Buy side firms use TCA to evaluate brokers and algos. Sell side firms use it to demonstrate quality. Regulators use it to enforce [[Best Execution]]. Modern TCA goes beyond benchmark comparison to peer analysis, venue analysis, and predictive models.

## Why it matters (commodities and FX)
Commodity and FX markets present unique TCA challenges. Brent trades on ICE, CME (via WTI), and OTC swap markets simultaneously, making venue comparison critical. FX has no central exchange, so [[Best Execution]] requires comparing fills across 15+ ECN venues and bank pools. A copper trader on LME consistently paying 3 ticks above [[VWAP]] leaks $75/lot, which on 500 lots/day is $37,500 daily. Without TCA this bleed is invisible. TCA also reveals whether [[POV]] beats [[TWAP]] for a specific instrument and order size, directly shaping future execution choices.

## Concrete example
**Concrete:** Energy desk executes 200 trades per month across Brent, WTI, and natural gas. Monthly TCA report:

| Metric | Brent (ICE) | WTI (CME) | Nat Gas (CME) |
|--------|------------|-----------|---------------|
| Trades | 80 | 70 | 50 |
| Avg order size | 500 lots | 300 lots | 200 lots |
| IS vs arrival (bps) | 3.2 | 2.8 | 5.1 |
| IS vs VWAP (bps) | 1.1 | 0.9 | 2.3 |
| % filled | 97% | 99% | 94% |
| Best algo | POV 8% | VWAP | POV 5% |

TCA flags natural gas at 5.1 bps vs arrival, well above the others. Root cause: 15% POV is too aggressive for nat gas liquidity. Dropping to 5% POV cuts IS to 2.8 bps. Monthly savings: 2.3 bps x 200 lots x 50 trades x $10,000/lot = $23,000. Without TCA, a 2 bps degradation in Broker A's algo over 6 months would silently cost $480,000 (2 bps x notional x 1,200 trades). Quarterly TCA catches this within 3 months.

**Simplified:** After every batch of trades, compare your average fill price to a benchmark (VWAP, arrival price, close). The gap is your execution cost. Track it by algo, venue, broker, and instrument. Patterns appear: this broker is degrading, this algo is wrong for this product, this venue is leaking information.

## Key mechanics and formulas
**Benchmark comparisons:**

1. **VS VWAP:**
$$\text{Cost}_{VWAP} = \frac{\bar{P}_{exec} - P_{VWAP}}{P_{VWAP}} \times 10{,}000 \text{ (bps)}$$

2. **VS Arrival price:**
$$\text{Cost}_{arrival} = \frac{\bar{P}_{exec} - P_{arrival}}{P_{arrival}} \times 10{,}000 \text{ (bps)}$$

3. **VS Close:**
$$\text{Cost}_{close} = \frac{\bar{P}_{exec} - P_{close}}{P_{close}} \times 10{,}000 \text{ (bps)}$$

For buys, positive values mean execution cost more than benchmark (bad). For sells, negative values mean worse execution.

**IS decomposition (used in TCA):**
$$IS = \text{spread cost} + \text{impact cost} + \text{timing cost} + \text{opportunity cost}$$

See [[Implementation Shortfall]] for the full formula.

**Reversion analysis (detecting market impact):**
$$\text{Reversion} = P_{exec,last} - P_{30min\_post}$$

If price reverts after the last fill, the algo caused temporary [[Market Impact]].

**Participation rate analysis:**
$$\rho_{actual} = \frac{Q_{filled}}{V_{market,during\_exec}}$$

Compare against target to check algo compliance.

## Prerequisites
- [[Implementation Shortfall]]
- [[VWAP]]
- [[Slippage]]
- [[Market Impact]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Implementation Shortfall]] is the primary cost metric used in TCA.
- [[VWAP]] is the most common intraday execution benchmark.
- [[POV]] and [[TWAP]] are algorithms TCA evaluates head to head.
- [[Smart Order Routing]] quality shows up in venue level TCA (fill rates, price improvement).
- [[Market Impact]] in TCA separates temporary impact (which reverts) from permanent (information).
- [[Best Execution]] is the regulatory obligation TCA helps firms demonstrate.
- [[Arrival Price]] aligns most closely with the PM's decision, the gold standard for IS based TCA.

## Common misconceptions
1. **"Beating VWAP means good execution."** [[VWAP]] is easy to beat trading against the trend (buy dips, sell rallies), which is luck not skill. TCA must adjust for trade difficulty.
2. **"TCA is only post trade."** Modern TCA includes pre trade cost estimation and real time monitoring. Post trade alone cannot prevent bad execution, only detect it.
3. **"One benchmark fits all."** Market orders vs arrival price. Passive algos vs VWAP. Portfolio rebalances vs close. Wrong benchmark produces misleading results.
4. **"TCA is just a compliance exercise."** The best desks use TCA as continuous improvement: testing algos, optimizing participation rates, selecting brokers, calibrating [[Market Impact]] models.

## Sources
- "Algorithmic Trading and DMA" by Barry Johnson
- "Optimal Trading Strategies" by Robert Kissell
- CFA Institute, "Trade Management Guidelines"
- MiFID II, "Best Execution" regulatory framework
- "The Market Microstructure Approach to FX" by Carol Osler
