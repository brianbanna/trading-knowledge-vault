---
aliases: [basis risk, hedge mismatch, cross hedge risk]
tags:
  - "#risk"
date-added: "2026-03-20"
---

# Basis Risk

## Definition
Basis risk is the residual risk left when a hedge instrument differs from the actual exposure. The basis is the price difference between the asset hedged and the hedge instrument. An airline hedging jet fuel with crude futures keeps the jet fuel crack spread. A European refiner hedging Brent exposure with WTI keeps the Brent WTI spread. Mismatches arise in location (Cushing vs Rotterdam), grade (sweet vs sour), timing (expiry vs exposure date), and product (crude vs refined). Basis risk is unavoidable wherever a perfect instrument does not exist, which is the case for most physical commodity hedges.

## Why it matters (commodities and FX)
Basis risk determines whether a hedge actually reduces total risk or simply converts flat price risk into spread risk. Physical commodity delivery points, timing, and quality rarely match futures specifications. A copper trader selling physical in Shanghai cannot hedge perfectly with LME contracts in London because the Shanghai London spread moves. In FX, a corporate hedging CNY with NDFs retains basis between the fixing rate and the conversion rate achieved. Cross hedge ratios, basis swaps, and [[Spread Trade|spread positions]] are core tools, and physical traders earn most of their P&L from managing this residual.

## Concrete example
**Concrete:** An airline burns 50 million gallons of jet fuel per year. It hedges 80% with NYMEX WTI at a 0.85 hedge ratio. In Q4, crude drops $5/bbl, jet fuel drops only $1/bbl because refinery outages tightened product supply. Hedge profit is $5 × 0.85 = $4.25/bbl. Physical cost reduction is $1/bbl. Net effective cost is $3.25/bbl worse than unhedged. Across 1.19 million barrels of exposure, the basis move cost $3.87 million in a single quarter. The directional WTI hedge worked; the crack spread basis did not.

**Simplified:** You hedge one thing with another similar thing. The two prices usually move together but not perfectly. When they drift apart at the wrong time, your hedge loses money in addition to your physical exposure. The leftover risk is the basis. The closer the hedge instrument is to the real exposure, the smaller the basis. There is almost never a perfect match.

## Key mechanics and formulas
- **Basis = Spot price of exposure − Price of hedging instrument**
- **Basis risk = Standard deviation of basis changes over the hedge horizon**
- **Optimal hedge ratio:** h* = rho × (sigma_exposure / sigma_hedge)
- **Hedge effectiveness = 1 − (Variance of hedged position / Variance of unhedged position).** Above 0.80 is a good hedge.
- **Types of basis risk:**
  - Location: Brent vs WTI, LME vs SHFE, HH vs TTF
  - Quality: sweet vs sour crude, wheat classes
  - Product: crude vs jet fuel, soybeans vs meal
  - Timing: hedge expiry differs from exposure date

## Prerequisites
- [[Futures Contract]]
- [[Forward Contract]]
- [[Spread Trade]]

## Related concepts (learn next)
- [[Spread Trade]] is the primary tool for managing and trading basis.
- [[Crush Spread]] is a specific basis between soybeans and processed products.
- [[Delivery]] anchors the basis between futures and physical at the delivery point; elsewhere it diverges.
- [[Cash Settlement]] introduces basis between the settlement index and the actual physical exposure.
- [[Forward Contract]] reduces basis through customization of location, grade, and timing.
- [[Old Crop New Crop]] spread is a temporal basis between crop years.
- [[Implied Volatility]] on basis spread options reflects uncertainty about the hedging relationship.
- [[Margin]] requirements do not account for basis, so true P&L of a hedged position can deviate from margin implications.
- [[Freight Basis Risk]] is the freight specific application: hedging a physical voyage with a Baltic index FFA leaves route, timing, and basket basis.

## Common misconceptions
- **"Hedging eliminates risk."** Hedging converts flat price risk into basis risk. Total risk falls but does not vanish. A poor instrument can raise total risk.
- **"Basis risk is small and stable."** Under stress, correlations break and basis can move several standard deviations. Jet fuel cracks, Brent WTI, and regional power basis have all done this.
- **"More hedging is always better."** Over hedging or hedging with a poorly correlated instrument increases total variance. Hedge ratio must be optimized to the correlation structure.
- **"Basis risk only matters for physical traders."** Financial traders using Brent to hedge Dubai exposure face basis as large as the original directional risk.

## Sources
- John Hull, "Options, Futures, and Other Derivatives" (basis risk chapters)
- CME Group, "Understanding Basis Risk in Commodity Hedging"
- Robert McDonald, "Derivatives Markets"
- Working, H., "Hedging Reconsidered," Journal of Farm Economics, 1953
