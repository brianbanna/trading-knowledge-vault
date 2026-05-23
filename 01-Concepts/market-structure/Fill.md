---
aliases: [fill, execution, filled, partial fill, fill rate]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Fill

## Definition
A fill is the execution of an order. "I got filled" means your order traded and you now hold a [[Position]]. A fill has 3 attributes: price (what you paid or received), quantity (how much executed), timestamp (when). A partial fill executes only part of the order, common with [[Limit Order]]s when available [[Liquidity]] at your price is less than your size. Fill quality, getting filled at or near your intended price, is a core measure of execution performance.

## Why it matters (commodities and FX)
In FX, where execution happens in milliseconds on electronic platforms, fill quality varies significantly across brokers and venues. A [[Single Dealer Platform]] might show tight [[Bid-Ask Spread]]s but reject or partially fill in volatile periods ([[Last Look]] rejection). In commodities, especially exchange traded futures, the fill you get depends on [[Order Book]] depth and order type. For large orders in illiquid contracts (far dated coffee, LME tin), getting fully filled without moving the market is a challenge. Every pip of improvement on a $50 million FX trade equals $5,000.

## Concrete example

**Concrete:** Limit buy 10 million EUR/USD at 1.0795. During a brief dip on a data release, the ask drops to 1.0793. Fill at 1.0793, 2 pips better than the limit. Price improvement saves 10,000,000 × 0.0002 = $2,000. EUR/USD rebounds to 1.0830 within the hour. Failure mirror: market sell 200 lots of LME copper at a screen price of $8,400/tonne. Routing and execution take 3 seconds in a fast market. Average fill $8,385. $15/tonne [[Slippage]] on 200 × 25 tonnes = $75,000 lost. Partials compound: first 80 lots fill at $8,395, remaining 120 sweep deeper to $8,378.

**Simplified:** A fill is the moment your order actually trades. The price you get may or may not match the screen, especially in fast markets. Partial fills mean you only got some of what you wanted, which can leave you with an unwanted half hedge. Good fill management is the difference between a clean execution and bleeding money to slippage over hundreds of trades.

## Key mechanics and formulas
- Fill price: actual execution price
- Fill rate = Quantity filled / Quantity ordered
  - 100% = full, less = partial
- [[Slippage]] = Expected fill price − Actual fill price
- Volume Weighted Average Price (VWAP) for multiple fills:
  - VWAP = Sum(price_i × quantity_i) / Sum(quantity_i)
- Implementation shortfall = Theoretical PnL (at decision price) − Actual PnL (at fill prices)
  - Captures total execution cost including timing, slippage, market impact

## Prerequisites
- [[Market Order]]
- [[Limit Order]]
- [[Bid-Ask Spread]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Slippage]] , gap between expected and actual fill
- [[Market Impact]] , price move caused by your order filling
- [[Liquidity]] , determines fill quality and full fill likelihood
- [[Order Book]] , queue of orders determining available fill prices
- [[Last Look]] , FX practice where dealers can reject fills after seeing the order
- [[Bid-Ask Spread]] , minimum cost of being filled
- [[ECN]] , electronic venues with different fill mechanics from dealer platforms

## Common misconceptions

**A fill confirmation does not mean settlement.** Fill = execution; settlement is later. FX spot settles T+2. Futures settle daily via [[Mark to Market]].

**The screen price is not the fill price.** In fast markets the displayed price is stale by the time your order reaches the exchange. This "last look" effect is built into FX platforms and is a major [[Slippage]] source.

**Partial fills can be worse than no fill.** A 30% fill on a hedging order leaves an unhedged residual. Minimum commissions still apply. Sometimes a [[Market Order]] is better to ensure full execution.

## Sources
- Harris, L. *Trading and Exchanges*, Chapters 4, 6, and 7
- CME Group, "Order Execution and Fill Reports"
- BIS, "FX Execution Algorithms and Market Functioning" (2020)
