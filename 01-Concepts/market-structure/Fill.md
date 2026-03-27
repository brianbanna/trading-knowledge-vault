---
aliases: [fill, execution, filled, partial fill, fill rate]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Fill

## Definition
A fill is the execution of an order. "I got filled" means your order has traded and you now have a [[Position]]. A fill has 3 key attributes: price (what you paid or received), quantity (how much executed), and timestamp (when it happened). A partial fill means only part of your order executed, common with [[Limit Order]]s when the available [[Liquidity]] at your price is less than your order size. Fill quality, getting filled at or near your intended price, is a core measure of execution performance.

## Why it matters (commodities and FX)
In FX, where execution happens in milliseconds on electronic platforms, fill quality varies significantly across brokers and venues. A [[Single Dealer Platform]] might show tight [[Bid-Ask Spread]]s but reject or partially fill orders during volatile periods ([[Last Look]] rejection). In commodities, especially on exchange traded futures, the fill you get depends on the depth of the [[Order Book]] and the order type you use. For large orders in illiquid contracts (far dated coffee, LME tin), getting fully filled without moving the market is a significant challenge. Every pip of fill improvement on a 50 million [[Notional]] FX trade translates to 5,000 USD.

## Concrete example
**Win scenario:** You place a [[Limit Order]] to buy 10 million EUR/USD at 1.0795. During a brief dip caused by a data release, the ask drops to 1.0793. You get filled at 1.0793, 2 [[Pip]]s better than your limit. This is called price improvement. Your fill saves 10,000,000 x 0.0002 = 2,000 USD versus your limit price. EUR/USD rebounds to 1.0830 within the hour.

**Fail scenario:** You send a [[Market Order]] to sell 200 lots of copper on the LME at what you see as 8,400 USD per tonne on the screen. The market is moving fast. Your order takes 3 seconds to route and execute. By the time it fills, the average price is 8,385. The 15 USD per tonne [[Slippage]] on 200 x 25 tonnes = 75,000 USD in lost [[PnL]]. Partial fills compound the problem: the first 80 lots fill at 8,395, but the remaining 120 lots sweep deeper into the book at 8,378.

## Key mechanics and formulas
- Fill price: the actual price at which the order executes
- Fill rate = Quantity filled / Quantity ordered
  - 100% = full fill, less than 100% = partial fill
- [[Slippage]] = Expected fill price minus Actual fill price
- Volume Weighted Average Price (VWAP) for multiple fills:
  - VWAP = Sum(price_i x quantity_i) / Sum(quantity_i)
- Implementation shortfall = Theoretical PnL (at decision price) minus Actual PnL (at fill prices)
  - Captures the total cost of execution including timing, slippage, and market impact

## Prerequisites
- [[Market Order]]
- [[Limit Order]]
- [[Bid-Ask Spread]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Slippage]] , the gap between expected and actual fill price
- [[Market Impact]] , the price movement caused by your order getting filled
- [[Liquidity]] , which determines fill quality and the likelihood of full fills
- [[Order Book]] , the queue of orders that determines available fill prices
- [[Last Look]] , the FX practice where dealers can reject fills after seeing the order
- [[Bid-Ask Spread]] , the minimum cost of getting filled (buy at ask, sell at bid)
- [[ECN]] , electronic venues where fill mechanics differ from dealer platforms

## Common misconceptions
- **A fill confirmation does not mean the trade is settled.** Fill = execution, but settlement (actual exchange of cash and securities) happens later. FX spot settles T+2. Futures settle daily via [[Mark to Market]].
- **The screen price is not always the fill price.** In fast markets, the price you see is stale by the time your order reaches the exchange. This "last look" effect is built into FX platforms and is a major source of [[Slippage]].
- **Partial fills can be worse than no fill.** Getting filled on 30% of a hedging order leaves you with an unhedged residual. The partially filled portion also incurs minimum commissions. In some cases, it is better to use a [[Market Order]] to ensure full execution.

## Sources
- Harris, L. *Trading and Exchanges*, Chapters 4, 6, and 7
- CME Group, "Order Execution and Fill Reports"
- BIS, "FX Execution Algorithms and Market Functioning" (2020)
