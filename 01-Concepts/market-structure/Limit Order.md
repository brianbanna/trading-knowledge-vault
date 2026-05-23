---
aliases: [limit order, limit buy, limit sell, resting order]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Limit Order

## Definition
A limit order sets the maximum price you will pay (buy) or the minimum you will accept (sell). It guarantees price, not [[Fill]]. A limit buy on gold at 2,040 only executes at 2,040 or lower. If the market stays above, the order sits in the [[Order Book]] waiting. Limit orders trade execution certainty for price certainty, the opposite of a [[Market Order]].

## Why it matters (commodities and FX)
Limit orders are the backbone of professional execution. In FX, a trader wanting EUR/USD at 1.0780 with market at 1.0800 leaves a resting limit buy; if the market dips, the order fills without watching the screen. In commodities with wide [[Bid-Ask Spread]]s (LME nickel, ICE cocoa), limits protect against overpaying. Market makers earn the spread by posting limits on both sides. The discipline of using limits over chasing with [[Market Order]]s saves thousands per month in [[Slippage]].

## Concrete example

**Concrete:** You want 5M AUD/USD but the ask is 0.6720. You see support at 0.6690 and post a limit buy at 0.6695. During Asia, a stop run pushes AUD/USD briefly to 0.6688. Your limit fills at 0.6695. AUD rebounds to 0.6740 by London open. Entry is 25 [[Pip]]s better than a market order, worth 5,000,000 × 0.0025 = 12,500 USD. Same trader posts a limit buy on 50 lots of WTI at 78.50 with market at 79.00. A bullish inventory surprise drives WTI to 82.00. The limit never fills. Opportunity cost: 50 × 1,000 × 3.00 = 150,000 USD on the missed move.

**Simplified:** Tell the venue the worst price you accept. The venue executes only at that price or better. You never overpay, but if the market moves away, you sit watching the trade you wanted run without you. Price certainty in exchange for fill certainty.

## Key mechanics and formulas
- Limit buy: execute at limit or lower. Posted below current ask.
- Limit sell: execute at limit or higher. Posted above current bid.
- Price improvement = Limit price minus Actual fill price (when filled better than limit)
- Opportunity cost = profit on the missed trade if never filled
- Fill probability decreases as the limit moves further from market
- Partial fill: only available quantity at the limit price executes

## Prerequisites
- [[Market Order]]
- [[Bid-Ask Spread]]
- [[Fill]]
- [[Position]]

## Related concepts (learn next)
- [[Market Order]], the alternative guaranteeing fill but not price
- [[Fill]], the execution event, often partial for limits
- [[Stop Loss]], combinable with limits as stop limit orders
- [[Bid-Ask Spread]], which limits help you avoid paying
- [[Slippage]], eliminated by limits (opportunity cost replaces it)
- [[Order Book]], where resting limits queue by price/time priority
- [[Liquidity]], which limit orders provide to the market

## Common misconceptions
- **Limits are not risk free.** You avoid [[Slippage]] but accept opportunity cost. In fast markets the missed move costs more than the spread saved.
- **Limits can fill at a worse effective price on gaps.** On futures, if the market gaps through your limit at the open, you fill at the limit but the market may be trading much further away.
- **"I placed a limit so I am safe" is false.** A resting limit buy is not a position until it fills. Once filled into a dropping market, you carry immediate [[Unrealized PnL]] loss.

## Sources
- Harris, L. *Trading and Exchanges*, Chapters 4 and 6
- CME Group, "Order Types and Execution"
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
