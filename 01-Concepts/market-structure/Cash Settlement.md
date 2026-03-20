---
aliases: [cash settlement, financial settlement, cash settled]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Cash Settlement

## Definition
Cash settlement is a method of settling a [[Futures Contract]] or derivatives position where no physical [[Delivery]] of the underlying asset occurs. Instead, the parties exchange the cash difference between the contract price and a reference price (typically a published index or price assessment) at expiry. Cash settled contracts are used when physical delivery is impractical (equity index futures, weather derivatives), when the underlying is intangible, or to simplify participation for financial traders who have no physical commodity handling capability. ICE Brent crude futures (the financial settlement version), CME E mini S&P 500 futures, and most FX non deliverable forwards ([[NDF]]s) are cash settled. The reference price used for cash settlement is critical: it must be liquid, transparent, and resistant to manipulation for the contract to function as a reliable hedging and pricing benchmark.

## Why it matters (commodities and FX)
Cash settlement eliminates the logistical complexity and storage risk of physical delivery, making commodity markets accessible to financial traders, hedge funds, and systematic strategies that cannot handle physical barrels of oil or bushels of corn. However, cash settlement removes the physical arbitrage mechanism that forces futures to converge perfectly with spot prices. This can create [[Basis Risk]] between the cash settled contract's reference price and the actual physical price a hedger faces. In commodity markets, the choice between physically settled and cash settled contracts (e.g., NYMEX WTI physically delivered vs. ICE Brent cash settled) affects liquidity patterns and price behavior near expiry. Financial participants generally prefer cash settled contracts, while physical traders often prefer deliverable contracts for their stronger convergence properties.

## Concrete example
**Success case:** A trader is long 10 ICE Brent crude futures (cash settled) at $80.00/bbl. At expiry, the ICE Brent Index (derived from Dated Brent assessments) settles at $82.50/bbl. Settlement: ($82.50 - $80.00) x 1,000 barrels x 10 contracts = $25,000 cash credit. No oil changes hands. The trader never had to worry about pipeline nominations, tank availability, or quality inspections.

**Failure case:** A physical jet fuel buyer hedges with cash settled Brent futures. At settlement, the Brent Index settles at $80.00/bbl, but the actual jet fuel price in Singapore (the buyer's market) is $92.00/bbl because crack spreads widened and regional premiums spiked. The hedge underperforms by $12.00/bbl because the cash settlement reference (Brent) did not track the actual physical exposure (Singapore jet fuel). The $12.00 x 1,000 barrels = $12,000 per contract shortfall is the realized [[Basis Risk]]. The lesson: cash settlement simplifies logistics but does not eliminate the mismatch between the settlement index and the hedger's true exposure.

## Key mechanics and formulas
- **Cash settlement payoff (long):** Settlement P&L = (Reference price - Entry price) x Contract size
- **Cash settlement payoff (short):** Settlement P&L = (Entry price - Reference price) x Contract size
- **Reference price sources:**
  - ICE Brent: ICE Brent Index (derived from Dated Brent physical market)
  - CME feeder cattle: CME Feeder Cattle Index (cash market survey)
  - Equity index futures: official closing index value
  - FX NDFs: official central bank fixing rate
- **Basis risk from cash settlement:** Basis = Physical exposure price - Cash settlement reference price. This residual basis must be managed separately.
- **No convergence guarantee:** Unlike physical delivery, cash settlement does not force the futures price to equal the spot price. Convergence depends on the accuracy of the reference index.

## Prerequisites
- [[Futures Contract]]
- [[Delivery]]
- [[Basis Risk]]

## Related concepts (learn next)
- [[Delivery]] is the physical alternative to cash settlement, providing stronger price anchoring through arbitrage.
- [[Basis Risk]] is the primary risk of cash settlement: the reference price may not match the trader's actual exposure.
- [[Forward Contract]] can be structured as either physically settled or cash settled depending on the counterparties' needs.
- [[Swap]] is inherently cash settled, with periodic payments based on the difference between fixed and floating prices.
- [[Futures Contract]] specifications define whether a contract is cash or physically settled.
- [[Contango Roll Cost]] applies to both cash and physically settled contracts as traders roll between expiry months.
- [[Implied Volatility]] in options on cash settled futures reflects uncertainty about the settlement index value at expiry.

## Common misconceptions
- **"Cash settled contracts always track the physical market."** They track a reference index, which may diverge from the actual cost of physical commodity at a specific location, grade, or timing. The divergence is [[Basis Risk]].
- **"Cash settlement eliminates all delivery risk."** It eliminates physical delivery logistics but introduces settlement risk if the reference price is volatile, illiquid, or susceptible to manipulation on the fixing date.
- **"Financial traders should always use cash settled contracts."** Some physically settled contracts (like NYMEX WTI) are more liquid and have tighter bid/ask spreads than cash settled alternatives. Liquidity, not settlement method, should drive contract choice.

## Sources
- CME Group, "Cash Settled vs. Physically Settled Futures"
- ICE, "Brent Crude Oil Index Methodology"
- John Hull, "Options, Futures, and Other Derivatives"
- Platts, "Methodology and Specifications Guide: Crude Oil"
