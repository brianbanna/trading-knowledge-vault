---
aliases: [basis risk, hedge mismatch, cross hedge risk]
tags:
  - "#risk"
date-added: "2026-03-20"
---

# Basis Risk

## Definition
Basis risk is the risk that a hedge does not perfectly offset the underlying exposure because the hedging instrument and the actual exposure are not identical. The "basis" is the price difference between the asset being hedged and the hedging instrument. For example, an airline hedging jet fuel costs with crude oil futures retains the risk that the jet fuel crack spread (the price gap between jet fuel and crude) moves against them. A European refiner hedging with WTI crude futures when their actual exposure is Brent crude retains the Brent/WTI spread as basis risk. Basis risk arises from mismatches in location (Cushing vs. Rotterdam), quality/grade (sweet vs. sour crude), timing (hedge expiry vs. exposure date), and product (crude vs. refined product). Basis risk is unavoidable whenever a perfect, identical hedge instrument is not available, which is the case for the vast majority of physical commodity hedges.

## Why it matters (commodities and FX)
Basis risk is the residual risk that remains after hedging, and it determines whether a hedge actually reduces total risk or merely transforms flat price risk into spread risk. In commodity markets, perfect hedges are rare because physical delivery locations, timing, and quality specifications almost always differ from futures contract standards. A copper trader selling physical copper in Shanghai cannot perfectly hedge with LME contracts in London because the Shanghai/London spread fluctuates. In FX, a company hedging Chinese yuan exposure with NDF contracts retains basis risk between the NDF fixing rate and the actual exchange rate achieved on physical conversion. Managing basis risk through cross hedge ratios, basis swaps, and [[Spread Trade|spread positions]] is a core competency of professional commodity traders and forms the basis of many physical trading profits.

## Concrete example
**Success case:** An airline consumes 50 million gallons of jet fuel per year and hedges 80% with NYMEX WTI crude futures, using an optimal hedge ratio of 0.85 based on the historical correlation between jet fuel and crude. In Q3, crude drops $10/bbl and jet fuel drops $8/bbl (the crack spread widened by $2/bbl). The hedge profit is $10 x 0.85 = $8.50/bbl, which more than offsets the $8/bbl reduction in fuel costs, producing a net $0.50/bbl windfall. The basis risk worked in the airline's favor this quarter.

**Failure case:** In Q4, crude drops $5/bbl but jet fuel drops only $1/bbl because refinery outages tightened product supply (the crack spread widened by $4/bbl). The hedge profit is $5 x 0.85 = $4.25/bbl, but the fuel cost only decreased $1/bbl. The airline's total cost is effectively higher by $3.25/bbl than if it had not hedged, because the basis (jet fuel vs. crude) moved adversely. Over 50 million gallons (approximately 1.19 million barrels), the basis mismatch cost the airline approximately $3.87 million. The lesson: cross commodity hedges reduce but do not eliminate risk, and basis can move against you by more than the flat price hedge saves.

## Key mechanics and formulas
- **Basis = Spot price of exposure - Price of hedging instrument**
- **Basis risk = Standard deviation of basis changes over the hedge horizon**
- **Optimal hedge ratio:** h* = rho x (sigma_exposure / sigma_hedge), where rho = correlation between exposure and hedge, sigma = standard deviation of price changes
- **Hedge effectiveness = 1 - (Variance of hedged position / Variance of unhedged position).** Values above 0.80 indicate a good hedge.
- **Types of basis risk:**
  - Location: Brent vs. WTI, LME vs. SHFE, HH vs. TTF
  - Quality/grade: sweet vs. sour crude, different wheat classes
  - Product: crude vs. jet fuel, soybeans vs. soybean meal
  - Timing: hedge expiry does not match exposure date

## Prerequisites
- [[Futures Contract]]
- [[Forward Contract]]
- [[Spread Trade]]

## Related concepts (learn next)
- [[Spread Trade]] is the primary tool for managing and trading basis risk, isolating the spread between hedge and exposure.
- [[Crush Spread]] is a specific form of basis between soybeans and their processed products.
- [[Delivery]] anchors the basis between futures and physical at the delivery point, but basis elsewhere can diverge.
- [[Cash Settlement]] introduces basis risk between the settlement index and the trader's actual physical exposure.
- [[Forward Contract]] can reduce basis risk through customization of location, grade, and timing.
- [[Old Crop New Crop]] spread is a temporal basis between supply from different crop years.
- [[Implied Volatility]] on basis spread options reflects uncertainty about the stability of the hedging relationship.
- [[Margin]] requirements on the hedge do not account for basis risk, meaning the true P&L of a hedged position can differ from what the margin calculation implies.

## Common misconceptions
- **"Hedging eliminates risk."** Hedging transforms flat price risk into basis risk. Total risk is reduced (often substantially), but not eliminated. A poorly chosen hedge instrument can actually increase total portfolio risk if basis is volatile.
- **"Basis risk is small and stable."** During market stress, correlations break down and basis risk can spike dramatically. The jet fuel crack spread, Brent/WTI spread, and regional power basis have all experienced multi standard deviation moves during crises.
- **"More hedging is always better."** Over hedging (hedge ratio above 1.0) or hedging with a poorly correlated instrument can increase total risk rather than reduce it. Optimizing the hedge ratio requires understanding the correlation structure.
- **"Basis risk only matters for physical traders."** Financial traders who use one futures contract to hedge another (e.g., Brent to hedge Dubai exposure) face basis risk that can be as significant as the original directional risk they were hedging.

## Sources
- John Hull, "Options, Futures, and Other Derivatives" (basis risk chapters)
- CME Group, "Understanding Basis Risk in Commodity Hedging"
- Robert McDonald, "Derivatives Markets"
- Working, H., "Hedging Reconsidered," Journal of Farm Economics, 1953
