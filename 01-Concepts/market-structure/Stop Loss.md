---
aliases: [stop loss, stop order, stop-loss order, protective stop]
tags:
  - "#microstructure"
  - "#risk"
date-added: "2026-03-27"
---

# Stop Loss

## Definition
A stop loss is an order that triggers when the price hits a specified level, designed to limit losses on an existing [[Position]]. For a [[Long]] position, the stop loss is placed below the entry price. For a [[Short]] position, it is placed above. When the stop price is reached, the stop loss typically converts into a [[Market Order]] and executes at the best available price. It is the primary tool for risk management at the individual trade level, enforcing discipline when the market moves against you.

## Why it matters (commodities and FX)
Without stop losses, a single bad trade can destroy months of [[PnL]]. In commodities, where prices can gap violently (crude oil on OPEC news, agricultural products on USDA crop reports), a stop loss is the last line of defense. In FX, where leverage can be 50:1 or higher, a 2% adverse move on a fully leveraged [[Position]] wipes out 100% of equity. Professional desks set stops on every position, and risk managers enforce maximum loss limits that automatically flatten positions when breached. The discipline of placing and honoring stop losses separates surviving traders from blown up ones.

## Concrete example
**Win scenario:** You go [[Long]] 10 million USD/JPY at 150.00 with a stop loss at 149.50 (50 [[Pip]]s risk). Your [[PnL]] per pip = 10,000,000 / 150.00 x 0.01 = approximately 667 USD per pip. Maximum risk = 50 x 667 = 33,350 USD. USD/JPY drops to 149.50, your stop triggers, and you get filled at 149.48 (2 pips of [[Slippage]]). Your [[Realized PnL]] is negative 34,700 USD. The rate then continues to 147.00, which would have been a negative 200,000 USD loss. The stop loss saved you 165,000 USD.

**Fail scenario:** You go [[Long]] 100 lots of WTI crude at 80.00 with a stop at 79.00. On Sunday night, Saudi Arabia announces a production increase and WTI opens Monday at 76.00, gapping through your stop. Your stop triggers at the open, but the [[Fill]] is at 75.80 due to the gap and [[Slippage]]. Instead of losing 1.00 per barrel (100,000 USD), you lose 4.20 per barrel (420,000 USD). Stop losses do not guarantee your loss limit in gap scenarios.

## Key mechanics and formulas
- Stop loss placement (long): Stop price = Entry price minus Maximum acceptable loss per unit
- Stop loss placement (short): Stop price = Entry price + Maximum acceptable loss per unit
- Dollar risk = Position size x |Entry price minus Stop price|
- Position sizing from stop: Position size = Risk budget / |Entry price minus Stop price|
  - Risk budget: maximum dollar amount willing to lose on this trade
- Risk/reward ratio = |Entry price minus Target price| / |Entry price minus Stop price|
  - A ratio of at least 2:1 means potential reward is 2x the risk

## Prerequisites
- [[Position]]
- [[Long]]
- [[Short]]
- [[Market Order]]
- [[PnL]]

## Related concepts (learn next)
- [[Market Order]] , which a triggered stop loss becomes
- [[Limit Order]] , the alternative for stop limit orders (guaranteed price, not fill)
- [[Slippage]] , the gap between stop price and actual [[Fill]] price
- [[Risk Management]] , the broader framework that stop losses fit into
- [[Drawdown]] , the cumulative loss that stop losses are designed to limit
- [[Volatility]] , which determines how far away to set the stop
- [[Gap Risk]] , the scenario where price jumps past your stop level

## Common misconceptions
- **A stop loss does not guarantee your maximum loss.** In gap scenarios (weekend gaps, news events), the market can open far beyond your stop level. The stop becomes a [[Market Order]] at the new price, not at your stop price.
- **Placing stops at obvious levels gets you stopped out more.** Round numbers (80.00 on crude, 1.0800 on EUR/USD) attract clusters of stops. Large players can "run the stops" by pushing through these levels to trigger forced selling, then reverse. Place stops at less obvious levels or use wider stops with smaller [[Position]] sizes.
- **A tighter stop is not always safer.** Too tight a stop means you get stopped out by normal market noise. If daily [[Volatility]] on EUR/USD is 60 pips and your stop is 15 pips away, you will be stopped out frequently even if your directional view is correct.

## Sources
- Schwager, J. *Market Wizards* (multiple interviews on stop discipline)
- CME Group, "Order Types: Stop Orders"
- Elder, A. *Trading for a Living*, Chapter on Risk Management
