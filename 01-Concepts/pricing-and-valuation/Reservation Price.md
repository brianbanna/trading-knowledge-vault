---
aliases: [reservation price, indifference price, adjusted fair value, Avellaneda-Stoikov]
tags:
  - "#microstructure"
  - "#quant"
date-added: "2026-03-27"
---

# Reservation Price

## Definition
The reservation price is a market maker's internal adjusted fair value that accounts for current [[inventory risk]]. From the Avellaneda Stoikov (2008) model of optimal market making. Core insight: if a market maker is long, they should lower fair value below the [[mid price]] to attract sell flow and reduce inventory. If short, raise it above mid to attract buy flow. Formula: `r = s - q × γ × σ² × T`, where q is current inventory, γ is risk aversion, σ is asset [[volatility]], T is time remaining. The reservation price replaces the naive mid as the center for setting bid and offer.

## Why it matters (commodities and FX)
Commodity and FX market makers constantly accumulate inventory from client flow. A copper market maker who bought 500 lots is long and exposed to a decline. The reservation price says exactly how much to skew quotes to incentivize offsetting flow. Banks running EUR/USD books use reservation price logic (often more sophisticated variants) for intraday inventory management. Critical for anyone building a quant market making strategy, or for reading why dealer prices on [[Multi Dealer Platform]]s are skewed versus mid. Also explains why a bank shows a tight bid (wants more) or wide bid (already long).

## Concrete example

**Concrete:** Brent crude quote. Mid $83.00, 4 hours left (T = 0.5 of session), annualized vol 30% (σ ≈ $1.11 for remaining session), γ = 1, inventory q = 0.02 (fraction of max). Reservation price = $83.00 − 0.02 × 1 × 1.23 × 0.5 = $82.99. Market maker centers quotes 1 cent below mid, bidding $82.97 and offering $83.01 instead of $82.98 and $83.02. Subtle skew attracts sellers, sheds the long. Without the skew, client flow keeps adding to the long; if the market drops $2, loss is $2 × accumulated inventory.

**Simplified:** A market maker who is already long does not want more inventory, so they shade their fair value down. Quotes drop too, making the bid less attractive and the offer more attractive. Sellers hit them less, buyers lift them more. Position drifts back toward flat. If they ignore inventory, they keep getting longer until a price move wipes them out. The reservation price is just "fair value, adjusted for the position I already have."

## Key mechanics and formulas
- **Reservation price**: r = s − q × γ × σ² × T. s = mid, q = inventory (+ long, − short), γ = risk aversion, σ = vol, T = time remaining.
- **Optimal spread**: δ = γ × σ² × T + (2/γ) × ln(1 + γ/k), k = order arrival intensity.
- **Optimal bid and ask**: bid = r − δ/2, ask = r + δ/2. Centered on r, not s.
- **Inventory skew**: q × γ × σ² × T. Larger position, higher γ, higher vol, longer horizon all increase skew.
- **Risk aversion (γ)**: higher γ = more aggressive inventory management. γ = 0 ignores inventory entirely.

## Prerequisites
- [[Mid Price]]
- [[Bid-Ask Spread]]
- [[Realized Volatility]]
- [[Market Making]]

## Related concepts (learn next)
- [[Market Making]]: the broader strategy where reservation price is the central pricing mechanism.
- [[Inventory Risk]]: the risk reservation price is designed to manage.
- [[Adverse Selection]]: informed flow can accumulate losing inventory despite reservation price adjustments.
- [[Skew]]: reservation price creates a quote skew versus mid. In options, "skew" means vol differences across strikes, unrelated.
- [[Arrival Price]]: mid at order submission, differs from reservation price because it ignores inventory.
- [[Mean Reversion]]: reservation price implicitly assumes some reversion. Trending markets break it.
- [[Optimal Execution]]: same stochastic control math.

## Common misconceptions
1. **"The reservation price is the fair value of the asset"**: it is the market maker's personal price given their inventory. 2 market makers with different inventories have different reservation prices for the same asset.
2. **"Avellaneda Stoikov works out of the box"**: original assumes continuous trading, no costs, normal returns, known vol. Every parameter must be calibrated in real time. Framework, not algorithm.
3. **"Only market makers use it"**: any trader managing continuous flow benefits. Corporate FX desks, commodity desks managing client orders, prop traders all apply reservation price logic.
4. **"The skew is small so it does not matter"**: small per quote, large in aggregate. Over thousands of trades the inventory drift dominates daily P&L for a market maker.

## Sources
- Avellaneda, Marco and Stoikov, Sasha, "High-Frequency Trading in a Limit Order Book," Quantitative Finance (2008)
- Gueant, Olivier, Lehalle, Charles-Albert, and Fernandez-Tapia, Joaquin, "Dealing with the Inventory Risk," Mathematics and Financial Economics (2013)
- Cartea, Alvaro, Jaimungal, Sebastian, and Penalva, Jose, "Algorithmic and High-Frequency Trading" (2015)
