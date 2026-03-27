---
aliases: [arrival price, decision price, benchmark price]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Arrival Price

## Definition
Arrival price is the [[mid price]] of an instrument at the exact moment an order is submitted to the market. It serves as the primary benchmark for measuring [[execution]] quality in [[transaction cost analysis]] (TCA). The concept was formalized by Perold (1988) as "implementation shortfall," which measures the gap between the arrival price and the actual average fill price. If a trader decides to buy when the mid is 1.0850 and eventually fills at 1.0855, the implementation shortfall is 5 pips. Arrival price captures both explicit costs ([[bid-ask spread]], commissions) and implicit costs ([[market impact]], timing cost, [[opportunity cost]]). It is the most widely used execution benchmark by institutional asset managers, hedge funds, and algorithmic trading desks.

## Why it matters (commodities and FX)
Every execution algorithm, from TWAP to VWAP to adaptive strategies, is ultimately judged against the arrival price. For a commodity trading house hedging a physical cargo, the arrival price is the market level when the hedge decision was made. If the hedge is executed poorly (high implementation shortfall), the firm gives up margin on the physical trade. In FX, arrival price benchmarking is standard for evaluating bank execution quality on [[Multi Dealer Platform]]s. Regulators (FCA, SEC) increasingly require firms to demonstrate they achieved "best execution," and arrival price is the primary metric. A systematic approach to minimizing shortfall versus arrival price is what separates professional execution from naive market orders.

## Concrete example
A fund manager decides at 09:00 to sell 500 lots of ICE Brent crude futures. At 09:00, the mid price is $83.20. The desk uses a TWAP algorithm to execute over 2 hours. Fills come in at: 100 lots at $83.18, 150 lots at $83.15, 100 lots at $83.12, 150 lots at $83.10. The volume-weighted average fill price is $83.134. The implementation shortfall versus arrival price is $83.20 - $83.134 = $0.066 per barrel. On 500 lots x 1,000 barrels = 500,000 barrels, the total shortfall is $33,000.

The win scenario: if the desk had used an aggressive [[IOC]] strategy at 09:00, crossing the spread to fill at $83.18, the shortfall would be only $0.02 per barrel ($10,000 total). The fail scenario: if the desk delays and starts executing at 10:00 after the market has fallen to $83.00, the "delay cost" component is $0.20 per barrel ($100,000) even before trading costs. This shows that timing relative to the arrival price often dominates spread and impact costs.

## Key mechanics and formulas
- **Implementation shortfall**: IS = arrival price - average fill price (for buy orders). For sell orders, IS = average fill price - arrival price. Positive IS means the execution cost money versus the decision price.
- **Decomposition**: IS = spread cost + market impact cost + timing cost + opportunity cost. Spread cost = half the [[bid-ask spread]]. Market impact = price movement caused by the order. Timing cost = price drift during execution. Opportunity cost = cost of any unfilled portion.
- **Arrival price calculation**: Arrival price = (best bid + best offer) / 2 at the timestamp of order submission. The timestamp must be precise (millisecond resolution or better).
- **Benchmark comparison**: IS_relative = IS / arrival price x 10,000 (in basis points). This normalizes across instruments with different price levels.
- **Alpha decay**: The information embedded in a trading decision decays over time. The further the execution deviates in time from the arrival moment, the more the arrival price loses relevance as a benchmark.

## Prerequisites
- [[Mid Price]]
- [[Bid-Ask Spread]]
- [[Market Impact]]
- [[Liquidity]]

## Related concepts (learn next)
- [[TWAP]]: time-weighted average price algorithm, a common execution strategy benchmarked against arrival price.
- [[VWAP]]: volume-weighted average price, an alternative benchmark that weights by market volume rather than the decision moment.
- [[Transaction Cost Analysis]]: the systematic framework for measuring execution quality, with arrival price as the primary benchmark.
- [[Market Impact]]: the component of implementation shortfall caused by the order itself moving the price.
- [[Slippage]]: informal term for the gap between expected and actual fill price, formalized by the arrival price framework.
- [[IOC]]: an order type that attempts immediate execution near the arrival price, minimizing timing cost but accepting spread cost.
- [[Opportunity Cost]]: the cost of shares or lots that never get filled, measured as the difference between arrival price and the end-of-day price on the unfilled portion.
- [[Reservation Price]]: the trader's internal adjusted fair value, related to but distinct from arrival price.

## Common misconceptions
1. **"Arrival price is the same as the price I see on my screen"**: The arrival price must be the mid price at the precise moment of order submission, not the price displayed seconds before on a delayed feed. Stale prices can make execution look artificially good or bad.
2. **"Beating the arrival price means good execution"**: Sometimes beating the arrival price is lucky (the market moved in your favor after submission). Consistent measurement over many trades is needed to distinguish skill from luck. A single trade's shortfall is noisy.
3. **"Arrival price is the only benchmark that matters"**: For orders with long execution horizons (multi-day programs), VWAP or interval TWAP may be more appropriate. Arrival price penalizes slow execution even when going slowly was the right strategy to minimize [[market impact]].

## Sources
- Perold, Andre, "The Implementation Shortfall: Paper Versus Reality," Journal of Portfolio Management (1988)
- Almgren, Robert and Chriss, Neil, "Optimal Execution of Portfolio Transactions," Journal of Risk (2001)
- Kissell, Robert, "The Science of Algorithmic Trading and Portfolio Management" (2013)
- CFA Institute, "Best Execution and Transaction Cost Analysis" guidance
