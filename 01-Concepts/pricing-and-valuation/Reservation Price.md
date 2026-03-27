---
aliases: [reservation price, indifference price, adjusted fair value, Avellaneda-Stoikov]
tags:
  - "#microstructure"
  - "#quant"
date-added: "2026-03-27"
---

# Reservation Price

## Definition
The reservation price is a market maker's internal adjusted fair value that accounts for current [[inventory risk]]. It comes from the Avellaneda and Stoikov (2008) model of optimal market making. The core insight: if a market maker is long, they should lower their fair value estimate below the [[mid price]] to attract more sell flow and reduce inventory. If short, they should raise it above the mid to attract buy flow. The formula is: reservation price = mid price - q x gamma x sigma^2 x T, where q is the current inventory position, gamma is the risk aversion parameter, sigma is the asset's [[volatility]], and T is the time remaining until the end of the trading horizon. The reservation price replaces the naive mid price as the center point around which the market maker sets their bid and offer.

## Why it matters (commodities and FX)
Market makers in commodities and FX constantly accumulate inventory from client flow. A copper market maker who has bought 500 lots from clients is now long and exposed to a price decline. The reservation price framework tells this market maker exactly how much to skew their quotes to incentivize offsetting flow. In FX, banks running EUR/USD market-making books use reservation price logic (often more sophisticated variants) to manage intraday inventory. Understanding the reservation price is critical for anyone building a quantitative market-making strategy, or for understanding why the prices offered by dealers on [[Multi Dealer Platform]]s are skewed relative to the mid. It also explains why a bank might show a client an unusually tight bid (they want to buy more) or a wide bid (they are already long and do not want more).

## Concrete example
A market maker is quoting Brent crude futures. The mid price is $83.00, the remaining trading time is 4 hours (T = 4/8 = 0.5 of the trading day), annualized volatility is 30% (daily vol ~1.9%, so sigma for the remaining session ~ $83 x 0.019 x sqrt(0.5) ~ $1.11), gamma (risk aversion) = 0.1, and the market maker is long 200 lots (q = +200). The reservation price = $83.00 - 200 x 0.1 x 1.11^2 x 0.5 = $83.00 - 200 x 0.1 x 1.23 x 0.5 = $83.00 - $12.33... This example shows that parameters must be carefully scaled. With properly normalized units: if q = 0.02 (as a fraction of max inventory), gamma = 1, sigma = $1.11, T = 0.5, then reservation price = $83.00 - 0.02 x 1 x 1.23 x 0.5 = $82.99. The market maker centers quotes 1 cent below mid, bidding $82.97 and offering $83.01 instead of $82.98 and $83.02. This subtle skew attracts more sellers, helping reduce the long position.

The fail scenario: the market maker ignores inventory and keeps quoting symmetrically around the mid. Client flow keeps adding to the long position. The market drops $2, and the market maker loses $2 x total accumulated inventory. Reservation price discipline would have skewed quotes to shed inventory earlier, limiting the loss.

## Key mechanics and formulas
- **Reservation price**: r = s - q x gamma x sigma^2 x T. Where s = mid price, q = inventory (positive for long, negative for short), gamma = risk aversion coefficient, sigma = price volatility, T = time remaining.
- **Optimal spread**: The Avellaneda-Stoikov model also gives the optimal spread: delta = gamma x sigma^2 x T + (2/gamma) x ln(1 + gamma/k), where k is a parameter governing order arrival intensity.
- **Optimal bid and ask**: bid = r - delta/2, ask = r + delta/2. The quotes are centered on the reservation price, not the mid price.
- **Inventory skew**: The term q x gamma x sigma^2 x T is the skew. Larger inventory, higher risk aversion, higher volatility, or longer time horizon all increase the skew.
- **Risk aversion (gamma)**: Higher gamma means more aggressive inventory management (wider skew). A gamma of 0 means the market maker ignores inventory risk and quotes symmetrically.

## Prerequisites
- [[Mid Price]]
- [[Bid-Ask Spread]]
- [[Realized Volatility]]
- [[Market Making]]

## Related concepts (learn next)
- [[Market Making]]: the broader strategy of continuously quoting bids and offers, within which the reservation price is the central pricing mechanism.
- [[Inventory Risk]]: the risk that accumulated position loses value, which the reservation price is designed to manage.
- [[Adverse Selection]]: informed flow can cause the market maker to accumulate losing inventory despite reservation price adjustments.
- [[Skew]]: the reservation price creates a skew in quotes relative to the mid. In options, "skew" refers to volatility differences across strikes, a different concept.
- [[Arrival Price]]: the mid price at order submission, which differs from the reservation price because it does not account for inventory.
- [[Mean Reversion]]: the reservation price implicitly assumes some degree of mean reversion. If prices trend indefinitely, the inventory penalty may be insufficient.
- [[Optimal Execution]]: closely related mathematics. Both optimal market making and optimal execution use stochastic control to minimize risk-adjusted cost.

## Common misconceptions
1. **"The reservation price is the fair value of the asset"**: The reservation price is not about fundamental valuation. It is the market maker's personal adjusted price given their current inventory. Two market makers looking at the same asset will have different reservation prices if they have different inventories.
2. **"The Avellaneda-Stoikov model works out of the box"**: The original model assumes continuous trading, no transaction costs, normally distributed returns, and a known volatility. In practice, every parameter (gamma, sigma, k) must be calibrated and adapted to real-time conditions. The model is a framework, not a plug-and-play algorithm.
3. **"Reservation price only applies to market makers"**: Any trader managing a book with continuous flow can use reservation price logic. A corporate FX desk managing hedging flow, a commodity desk managing client orders, or a prop trader managing a portfolio all benefit from thinking about how inventory should adjust their pricing.

## Sources
- Avellaneda, Marco and Stoikov, Sasha, "High-Frequency Trading in a Limit Order Book," Quantitative Finance (2008)
- Gueant, Olivier, Lehalle, Charles-Albert, and Fernandez-Tapia, Joaquin, "Dealing with the Inventory Risk," Mathematics and Financial Economics (2013)
- Cartea, Alvaro, Jaimungal, Sebastian, and Penalva, Jose, "Algorithmic and High-Frequency Trading" (2015)
