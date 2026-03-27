---
aliases: [inventory risk, position risk, market maker risk, warehouse risk]
tags:
  - "#risk"
  - "#microstructure"
date-added: "2026-03-27"
---

# Inventory Risk

## Definition
Inventory risk is the risk that the price moves against the positions a market maker accumulates while providing liquidity. When a market maker buys from a seller, they become long, and if the price falls before they can sell to a buyer, they lose money. The core tension is that providing liquidity requires taking the other side of trades, which naturally builds up directional exposure. In commodities and FX, inventory risk is amplified by the size of typical institutional orders and the potential for sudden macro driven moves. Managing inventory risk is the single most important task for any market maker, because uncontrolled inventory is how firms blow up.

## Why it matters (commodities and FX)
A crude oil market maker quoting 2 sided markets on [[ICE Brent]] or [[WTI]] futures accumulates inventory every time a client hits their bid or lifts their offer. If OPEC announces a surprise production cut while the maker is short 500 lots, the loss can be catastrophic. In FX, a [[EURUSD]] market maker on an [[ECN]] like EBS or Refinitiv faces the same problem: inventory builds up from client flow, and if the [[ECB]] surprises with a rate decision, the position can gap against them. The spread the market maker earns (the bid ask spread) must compensate for this inventory risk over time, or the business is not viable. This is why wider spreads appear during volatile periods, the market maker is demanding more compensation for holding risky inventory.

## Concrete example
A market maker on CME WTI crude oil futures is quoting a 1 tick wide market at 78.50 bid and 78.51 offer. A large producer hedging sells 200 lots at the 78.50 bid. The maker is now long 200 lots (notional value: 200 x 1000 barrels x $78.50 = $15.7 million).

**Win scenario:** The maker immediately offers 200 lots at 78.51 and gets filled within 2 seconds. Profit: 200 x 1 tick x $10 per tick = $2,000 gross. The inventory risk was held for only 2 seconds.

**Fail scenario:** Before the maker can flatten, the US DOE weekly inventory report drops showing a surprise build of 8 million barrels. WTI drops from 78.50 to 77.80 in 3 seconds. The maker is still long 200 lots. Loss: 200 x 70 ticks x $10 = $140,000. One bad inventory event just wiped out 70 winning round trips.

## Key mechanics and formulas
**Inventory PnL** = Q x (P_exit - P_entry)
Where Q = quantity held (positive if long, negative if short), P_entry = average fill price, P_exit = price at which inventory is flattened.

**Avellaneda-Stoikov optimal spread adjustment:**
δ = γ x σ² x Q x T
Where δ = spread skew (how much to shift quotes away from fair value), γ = risk aversion parameter, σ = [[Volatility]] of the asset, Q = current inventory, T = time remaining in the trading session. A market maker who is long should lower their offer to attract sellers and raise their bid to discourage more buying.

**Inventory half life:** The time it takes for a market maker to reduce inventory by 50%. A healthy system targets a half life under 30 seconds for liquid futures.

## Prerequisites
- [[Bid Ask Spread]]
- [[Market Making]]
- [[PnL]]
- [[Volatility]]

## Related concepts (learn next)
- [[Adverse Selection]] — the risk that informed traders pick off stale quotes, which is the primary driver of inventory accumulation on the wrong side.
- [[Market Impact]] — large inventory liquidation itself moves the price, compounding the loss.
- [[Value at Risk]] — a standard way to quantify the dollar risk of current inventory exposure.
- [[Hedging]] — using correlated instruments to reduce inventory risk without fully flattening.
- [[Kill Switch]] — the emergency mechanism to cancel all quotes when inventory risk becomes unmanageable.
- [[Skew]] — adjusting quote prices based on inventory position to encourage mean reversion of holdings.
- [[Latency]] — faster systems can flatten inventory more quickly, reducing the time exposure to adverse moves.

## Common misconceptions
1. **"Inventory risk only matters for HFT firms."** Any trader who provides liquidity, including a voice broker in physical copper or a bank FX desk, faces inventory risk. The timescale differs (seconds vs hours) but the mechanics are identical.
2. **"Wider spreads eliminate inventory risk."** Wider spreads increase revenue per trade but also reduce fill rates. A market maker quoting too wide will not accumulate enough trades to generate consistent PnL, and when they do get filled, it is likely because the market is about to move against them ([[Adverse Selection]]).
3. **"Just use a stop loss."** In fast markets, [[Gap Risk]] means the stop loss may not execute at the intended price. Inventory risk management must be proactive (quote skewing, position limits) rather than purely reactive.

## Sources
- Avellaneda, M. and Stoikov, S. (2008). "High Frequency Trading in a Limit Order Book." *Quantitative Finance*.
- Guéant, O. (2017). *The Financial Mathematics of Market Making*. Chapman & Hall.
- CME Group. "Market Making Programs." cmegroup.com.
