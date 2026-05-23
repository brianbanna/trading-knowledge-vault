---
aliases: [half spread, half-spread, single-side cost]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Half Spread

## Definition
The half spread is half the [[Bid-Ask Spread]], the cost of a single trade from the [[Mid Price]]. Bid 1.1000, ask 1.1002: spread is 2 pips, half spread is 1 pip. Buying at the ask pays mid plus half spread. Selling at the bid receives mid minus half spread. The half spread is the market maker's gross revenue per side before [[Adverse Selection]] costs, and the minimum price taker cost for immediacy on a single transaction.

## Why it matters (commodities and FX)
The half spread is the fundamental unit of transaction cost analysis (TCA) in FX and commodities. Evaluating an execution algo or broker comes down to: how much did I pay vs mid? That answer is the half spread or better. In EUR/USD, the half spread at [[Top of Book]] is 0.1 to 0.5 pips in normal conditions. In thin commodities like lean hogs or cocoa, it is several ticks. A market maker's profitability equals half spread earned minus [[Adverse Selection]] cost minus hedging cost. If a maker quotes 2 pips in GBP/USD (1 pip half spread) but average [[Markout]] is -1.2 pips, the maker loses 0.2 pips per trade despite earning the half spread.

## Concrete example

**Concrete:** Gold futures on COMEX quoted $2,340.00 bid / $2,340.40 ask. Spread $0.40, half spread $0.20/oz. Market maker sells 10 contracts (100 oz each) at $2,340.40, mid does not move. Edge: $0.20/oz x 10 x 100 = $200. Buying back at $2,340.00 completes a [[Round Trip]], capturing full spread $400. Price taker side: urgent buy of 50 contracts. Lifts at $2,340.40 ($0.20 above mid). Order sweeps levels: 10 at $2,340.40, 15 at $2,340.60, 15 at $2,340.80, 10 at $2,341.00. Average fill $2,340.68, $0.48 above original mid. Effective half spread $0.48, more than double displayed, because [[Market Impact]] consumed extra levels.

**Simplified:** Half spread is what you pay relative to the middle price for one trade. Buy at the ask, you paid half a spread above mid. Sell at the bid, you got half a spread below mid. Market makers earn this on each fill. Traders pay it. Round trip costs two half spreads.

## Key mechanics and formulas
- **Half spread** = (Ask - Bid) / 2 = Spread / 2
- **Half spread in bps** = Half spread / Mid x 10000
- **Execution cost from mid** = |Fill Price - Mid| (approximates half spread for small market orders)
- **Maker gross P&L per side** = Half Spread - Adverse Selection cost
- **Maker net P&L per round trip** = Spread - 2 x Adverse Selection cost
- Price taker single side cost = Half Spread + [[Slippage]] + [[Market Impact]] (latter two = 0 for small orders in liquid markets)

## Prerequisites
- [[Bid-Ask Spread]]
- [[Mid Price]]
- [[Top of Book]]

## Related concepts (learn next)
- [[Round Trip]] , two half spreads, the full cost of buying and selling
- [[Markout]] , compares post trade movement to half spread to determine net profitability
- [[Slippage]] , execution cost beyond displayed half spread from timing or size
- [[Market Impact]] , additional cost when order size exceeds [[Top of Book]]
- [[Adverse Selection]] , the risk offsetting half spread revenue for makers
- [[Bid-Ask Spread]] , the parent concept
- [[Effective Spread]] , 2 x |Fill Price - Mid|, the realized (not quoted) half spread

## Common misconceptions
1. **"Half spread is my total cost."** Only the immediate, visible cost. For larger orders, [[Market Impact]], [[Slippage]], and information leakage add up. A 0.5 pip half spread in EUR/USD becomes 2 pip total on a 200M order.
2. **"Smaller half spread is always better."** Tight half spread with high [[Last Look]] rejection rates can be worse than wider spread with guaranteed fills. Effective cost depends on fill probability.
3. **"Half spread is constant."** Spreads widen during news, illiquid hours (Asia to London gap), and stress. Copper half spreads of $0.50 in London hours can be $2.00 during Asian hours when LME is closed.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- CME Group, "Understanding Transaction Costs in Futures Markets"
