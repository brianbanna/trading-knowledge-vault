---
aliases: [limit order, limit buy, limit sell, resting order]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-27"
---

# Limit Order

## Definition
A limit order sets the maximum price you will pay (for a buy) or the minimum price you will accept (for a sell). It guarantees your price but not your [[Fill]]. If you place a limit buy on gold at 2,040, you will only execute at 2,040 or lower. If the market stays above 2,040, your order sits in the [[Order Book]] waiting. Limit orders provide price certainty at the cost of execution certainty, the opposite of a [[Market Order]].

## Why it matters (commodities and FX)
Limit orders are the backbone of professional execution. In FX, a trader who wants to buy EUR/USD at 1.0780 when the market is at 1.0800 leaves a limit buy resting. If the market dips, the order fills without the trader watching the screen. In commodities, where [[Bid-Ask Spread]]s can be wide (especially in less liquid contracts like LME nickel or ICE cocoa), limit orders protect against overpaying. Market makers earn the spread by posting limit orders on both sides. For a trader, the discipline of using limits rather than chasing with [[Market Order]]s can save thousands of dollars per month in [[Slippage]].

## Concrete example
**Win scenario:** You want to buy 5 million AUD/USD but the current ask is 0.6720. You believe there is support at 0.6690 and place a limit buy at 0.6695. During the Asian session, a stop run pushes AUD/USD briefly to 0.6688. Your limit order fills at 0.6695. AUD subsequently rebounds to 0.6740 by the London open. Your entry is 25 [[Pip]]s better than the market order price would have been, worth 5,000,000 x 0.0025 = 12,500 USD.

**Fail scenario:** You place a limit buy on 50 lots of WTI crude at 78.50 when the market is at 79.00. An unexpected bullish inventory report pushes WTI straight to 82.00. Your limit order never fills. You miss a 3.00 move (50 x 1,000 x 3.00 = 150,000 USD of opportunity cost). The market never comes back to 78.50. Your insistence on a limit price cost you the entire trade.

## Key mechanics and formulas
- Limit buy: Execute at limit price or lower. Placed below current ask.
- Limit sell: Execute at limit price or higher. Placed above current bid.
- Price improvement = Limit price minus Actual fill price (if filled better than the limit)
- Opportunity cost = Profit on the missed trade if the limit order is never filled
- Fill probability decreases as the limit price moves further from the current market
- Partial fill: if only some quantity is available at the limit price, only that portion executes

## Prerequisites
- [[Market Order]]
- [[Bid-Ask Spread]]
- [[Fill]]
- [[Position]]

## Related concepts (learn next)
- [[Market Order]] , the alternative that guarantees fill but not price
- [[Fill]] , the execution event, which may be partial for limit orders
- [[Stop Loss]] , which can be combined with limit orders (stop limit orders)
- [[Bid-Ask Spread]] , which limit orders help you avoid paying
- [[Slippage]] , which is eliminated by limit orders (but opportunity cost replaces it)
- [[Order Book]] , where resting limit orders queue by price and time priority
- [[Liquidity]] , which limit orders provide to the market

## Common misconceptions
- **Limit orders are not risk free.** You avoid [[Slippage]] but gain opportunity cost risk. In fast markets, the "best" execution is often a [[Market Order]] because the move you miss costs more than the spread you save.
- **Limit orders can still fill at a worse price than expected in gaps.** On futures exchanges, if the market gaps through your limit price at the open, you may be filled at your limit price, but the market may immediately be trading much lower (for a limit buy) or higher (for a limit sell).
- **"I placed a limit order so I am safe" is false.** A resting limit buy is not a position until it fills. If it fills and the market keeps dropping, you now have an immediate [[Unrealized PnL]] loss.

## Sources
- Harris, L. *Trading and Exchanges*, Chapters 4 and 6
- CME Group, "Order Types and Execution"
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
