---
aliases: [stop loss, stop order, stop-loss order, protective stop]
tags:
  - "#microstructure"
  - "#risk"
date-added: "2026-03-27"
---

# Stop Loss

## Definition
A stop loss is an order that triggers when price hits a specified level, designed to limit losses on an existing [[Position]]. For a [[Long]], the stop sits below entry. For a [[Short]], above. When the stop price triggers, the order converts to a [[Market Order]] and executes at the best available price. It is the primary tool for trade level risk management, enforcing discipline when the market moves against you.

## Why it matters (commodities and FX)
Without stops, a single bad trade destroys months of [[PnL]]. In commodities where prices gap violently (crude on OPEC news, agriculture on USDA reports), the stop is the last line of defense. In FX with 50:1 leverage, a 2% adverse move on a fully leveraged [[Position]] wipes 100% of equity. Professional desks set stops on every position. Risk managers enforce maximum loss limits that auto flatten when breached. Honoring stops separates surviving traders from blown up ones.

## Concrete example

**Concrete:** You go [[Long]] 10M USD/JPY at 150.00 with stop at 149.50 (50 [[Pip]] risk). PnL per pip = 10,000,000 / 150.00 × 0.01 ≈ 667 USD. Max risk = 50 × 667 = 33,350 USD. USD/JPY drops to 149.50, stop triggers, fill at 149.48 (2 pip slippage). [[Realized PnL]] = -34,700 USD. The rate then runs to 147.00, which would have been -200,000 USD. The stop saved 165,000 USD. Gap case: long 100 lots WTI at 80.00 with stop at 79.00. Sunday night Saudi announces a production increase, WTI opens Monday at 76.00, gapping through the stop. Fill at 75.80. Loss: 4.20/bbl × 100,000 = 420,000 USD instead of the intended 100,000. Stops do not guarantee the loss limit on a gap.

**Simplified:** A pre placed instruction: "if price hits X, get me out." Below entry for longs, above for shorts. Triggered stops become market orders and fill at whatever is available. Without one, a normal losing trade can become a career ending one. With one, you cap the downside (unless the market gaps).

## Key mechanics and formulas
- Stop loss placement (long): Stop = Entry minus Maximum acceptable loss per unit
- Stop loss placement (short): Stop = Entry + Maximum acceptable loss per unit
- Dollar risk = Position size × |Entry minus Stop|
- Position sizing from stop: Position size = Risk budget / |Entry minus Stop|
  - Risk budget: max dollar amount willing to lose on this trade
- Risk/reward ratio = |Entry minus Target| / |Entry minus Stop|
  - At least 2:1 means potential reward is 2x the risk

## Prerequisites
- [[Position]]
- [[Long]]
- [[Short]]
- [[Market Order]]
- [[PnL]]

## Related concepts (learn next)
- [[Market Order]], which a triggered stop becomes
- [[Limit Order]], alternative for stop limit (price guaranteed, fill not)
- [[Slippage]], the gap between stop price and actual fill
- [[Risk Management]], the broader framework stops fit into
- [[Drawdown]], cumulative loss stops are designed to limit
- [[Volatility]], which determines how far away to set the stop
- [[Gap Risk]], the scenario where price jumps past the stop

## Common misconceptions
- **A stop does not guarantee max loss.** On gaps (weekends, news), the market opens past the stop. The stop becomes a [[Market Order]] at the new price, not at your stop.
- **Obvious levels get stopped out more.** Round numbers (80.00 on crude, 1.0800 on EUR/USD) cluster stops. Large players "run the stops" by pushing through to trigger selling, then reverse. Place stops at less obvious levels or use wider stops with smaller [[Position]] sizes.
- **A tighter stop is not always safer.** Too tight and normal noise stops you out. If EUR/USD daily vol is 60 pips and your stop is 15 pips, you will be stopped out frequently even if directionally correct.

## Sources
- Schwager, J. *Market Wizards* (multiple interviews on stop discipline)
- CME Group, "Order Types: Stop Orders"
- Elder, A. *Trading for a Living*, Chapter on Risk Management
