---
aliases: [inventory risk, position risk, market maker risk, warehouse risk]
tags:
  - "#risk"
  - "#microstructure"
date-added: "2026-03-27"
---

# Inventory Risk

## Definition
Inventory risk is the risk that the price moves against the positions a market maker accumulates while providing liquidity. When a market maker buys from a seller they become long; if the price falls before they sell to a buyer, they lose money. Providing liquidity requires taking the other side, which naturally builds directional exposure. In commodities and FX, inventory risk is amplified by typical institutional order size and the potential for sudden macro driven moves. Managing inventory is the single most important task for any market maker, because uncontrolled inventory is how firms blow up.

## Why it matters (commodities and FX)
A crude market maker quoting [[ICE Brent]] or [[WTI]] futures accumulates inventory every time a client hits the bid or lifts the offer. If OPEC announces a surprise cut while the maker is short 500 lots, the loss is catastrophic. In FX, a [[EURUSD]] market maker on an [[ECN]] (EBS, Refinitiv) faces the same problem: client flow builds inventory, and if the [[ECB]] surprises with a rate decision, the position gaps against them. The bid ask spread the maker earns must compensate for inventory risk over time, or the business is not viable. Wider spreads in volatile periods reflect the maker demanding more compensation for holding risky inventory.

## Concrete example
**Concrete:** A maker on CME WTI quotes 1 tick wide at 78.50/78.51. A large producer hedge sells 200 lots at 78.50. The maker is now long 200 lots, notional $15.7M. Before the maker flattens, the DOE weekly inventory report drops showing a surprise 8M barrel build. WTI falls from 78.50 to 77.80 in 3 seconds. Maker is still long 200 lots. Loss: 200 × 70 ticks × $10 = $140,000. One adverse inventory event wiped out 70 winning round trips of 1 tick each. The point is not the bad luck — it is that one event can erase weeks of edge if inventory is not skewed or flattened fast.

**Simplified:** Making markets means you stand ready to buy and sell at quoted prices. Every fill leaves you holding inventory on one side. If you can offload that inventory to the next counterparty quickly at a similar price, you earn the spread. If a news event hits while you are still holding, you take the full directional loss. The bigger your position and the slower you flatten, the worse the exposure. Risk control means skewing quotes (raising bid, lowering offer) when you want to reduce inventory, capping max size, and being ready to bail out.

## Key mechanics and formulas
**Inventory P&L** = Q × (P_exit − P_entry)
Q = quantity held (positive long, negative short), P_entry = avg fill, P_exit = flatten price.

**Avellaneda Stoikov optimal spread skew:**
δ = γ × σ² × Q × T
δ = quote skew from fair value, γ = risk aversion, σ = [[Volatility]], Q = current inventory, T = time remaining in session. A long maker lowers the offer to attract sellers and raises the bid to discourage more buying.

**Inventory half life:** time for a maker to halve inventory. Healthy systems target under 30 seconds for liquid futures.

## Prerequisites
- [[Bid Ask Spread]]
- [[Market Making]]
- [[PnL]]
- [[Volatility]]

## Related concepts (learn next)
- [[Adverse Selection]] — informed traders pick off stale quotes; the primary driver of inventory accumulation on the wrong side.
- [[Market Impact]] — large inventory liquidation moves the price, compounding the loss.
- [[Value at Risk]] — standard way to quantify dollar risk of current inventory.
- [[Hedging]] — using correlated instruments to reduce inventory risk without fully flattening.
- [[Kill Switch]] — emergency mechanism to cancel all quotes when inventory becomes unmanageable.
- [[Skew]] — adjusting quote prices based on inventory to encourage mean reversion of holdings.
- [[Latency]] — faster systems flatten inventory faster, reducing time exposure to adverse moves.

## Common misconceptions
1. **"Inventory risk only matters for HFT."** Any liquidity provider faces it, including a voice broker in physical copper or a bank FX desk. The timescale differs (seconds vs hours); the mechanics are identical.
2. **"Wider spreads eliminate inventory risk."** Wider spreads raise revenue per trade but cut fill rates. A maker quoting too wide accumulates fewer trades and gets filled mainly when informed flow is about to move the market against them ([[Adverse Selection]]).
3. **"Just use a stop loss."** In fast markets, [[Gap Risk]] means stops do not fill at the intended price. Inventory management must be proactive (quote skewing, position limits), not purely reactive.

## Sources
- Avellaneda, M. and Stoikov, S. (2008). "High Frequency Trading in a Limit Order Book." *Quantitative Finance*.
- Guéant, O. (2017). *The Financial Mathematics of Market Making*. Chapman & Hall.
- CME Group. "Market Making Programs." cmegroup.com.
