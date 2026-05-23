---
aliases: [arrival price, decision price, benchmark price]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Arrival Price

## Definition
Arrival price is the [[mid price]] at the exact moment an order is submitted. It is the primary benchmark for [[execution]] quality in [[transaction cost analysis]] (TCA). Perold (1988) formalized the concept as "implementation shortfall," the gap between arrival price and average fill price. Decide to buy at mid 1.0850, fill at 1.0855: shortfall is 5 pips. Arrival price captures both explicit costs ([[bid-ask spread]], commissions) and implicit costs ([[market impact]], timing, [[opportunity cost]]). It is the dominant execution benchmark for institutional asset managers, hedge funds, and algo desks.

## Why it matters (commodities and FX)
Every execution algo, from TWAP to VWAP to adaptive, is judged against arrival price. For a commodity house hedging a physical cargo, arrival price is the market level when the hedge decision was made. Poor execution (high shortfall) gives up margin on the physical trade. In FX, arrival price benchmarking is standard for evaluating bank execution on [[Multi Dealer Platform]]s. FCA and SEC now require firms to demonstrate "best execution," and arrival price is the primary metric. Systematic shortfall minimization is what separates professional execution from naive market orders.

## Concrete example

**Concrete:** A fund manager decides at 09:00 to sell 500 lots of ICE Brent futures. Mid at 09:00 is $83.20. Desk uses TWAP over 2 hours. Fills: 100 at $83.18, 150 at $83.15, 100 at $83.12, 150 at $83.10. VWAP is $83.134. Implementation shortfall is $0.066 per barrel. On 500,000 barrels, total shortfall is $33,000. An aggressive [[IOC]] at 09:00 crossing the spread at $83.18 would have produced shortfall of $0.02 per barrel ($10,000). A 1 hour delay until the market falls to $83.00 adds $100,000 of delay cost before any trading cost. Timing relative to arrival dominates spread and impact costs in this scenario.

**Simplified:** You make a trading decision when the price is at one level. By the time your order finishes filling, the price has moved. The gap between where it was when you decided and where you actually got filled is the implementation shortfall. The bigger that gap, the worse your execution. Algos try to minimize it by balancing speed (cross the spread now and pay the spread cost) against patience (work the order over time and risk the price moving away).

## Key mechanics and formulas
- **Implementation shortfall**: IS = arrival price − average fill price (buys). Sells: IS = average fill price − arrival price. Positive IS = execution cost money vs the decision price.
- **Decomposition**: IS = spread cost + market impact + timing cost + opportunity cost. Spread cost = half [[bid-ask spread]]. Market impact = price move caused by the order. Timing cost = drift during execution. Opportunity cost = cost of any unfilled portion.
- **Arrival price**: (best bid + best offer) / 2 at order submission timestamp. Millisecond resolution or better.
- **Benchmark comparison**: IS_relative = IS / arrival price × 10,000 (in bps). Normalizes across instruments.
- **Alpha decay**: Information in a trading decision decays over time. The longer execution lags the arrival moment, the less the arrival benchmark applies.

## Prerequisites
- [[Mid Price]]
- [[Bid-Ask Spread]]
- [[Market Impact]]
- [[Liquidity]]

## Related concepts (learn next)
- [[TWAP]]: time weighted average price algo, benchmarked against arrival.
- [[VWAP]]: volume weighted alternative benchmark.
- [[Transaction Cost Analysis]]: the framework for measuring execution quality.
- [[Market Impact]]: the order's own contribution to shortfall.
- [[Slippage]]: informal term formalized by the arrival framework.
- [[IOC]]: minimizes timing cost, accepts spread cost.
- [[Opportunity Cost]]: cost of unfilled portion vs end of day price.
- [[Reservation Price]]: trader's internal fair value, distinct from arrival.

## Common misconceptions
**"Arrival price is the screen price."** Arrival must be the mid at the precise submission moment, not the delayed feed shown seconds earlier. Stale prices distort TCA.

**"Beating arrival means good execution."** Sometimes the market moved your way by luck. Single trades are noisy. Skill shows up over hundreds of trades, not one.

**"Arrival is the only benchmark that matters."** For multi day programs, VWAP or interval TWAP is more appropriate. Arrival penalizes slow execution even when slow was correct to minimize [[market impact]].

## Sources
- Perold, Andre, "The Implementation Shortfall: Paper Versus Reality," Journal of Portfolio Management (1988)
- Almgren, Robert and Chriss, Neil, "Optimal Execution of Portfolio Transactions," Journal of Risk (2001)
- Kissell, Robert, "The Science of Algorithmic Trading and Portfolio Management" (2013)
- CFA Institute, "Best Execution and Transaction Cost Analysis" guidance
