---
aliases: [cash settlement, financial settlement, cash settled]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Cash Settlement

## Definition
Cash settlement settles a [[Futures Contract]] or derivatives position without physical [[Delivery]] of the underlying. Parties exchange the cash difference between the contract price and a reference price (typically a published index or assessment) at expiry. Cash settlement applies when physical delivery is impractical (equity index futures, weather derivatives), when the underlying is intangible, or to simplify participation for financial traders who cannot handle physical commodities. ICE Brent (financial version), CME E mini S&P 500, and most FX non deliverable forwards ([[NDF]]s) are cash settled. The reference price must be liquid, transparent, and resistant to manipulation for the contract to function as a reliable benchmark.

## Why it matters (commodities and FX)
Cash settlement removes logistics and storage risk, opening commodity markets to financial traders, hedge funds, and systematic strategies that cannot handle barrels or bushels. It also removes the physical arbitrage that forces futures to converge perfectly with spot, creating [[Basis Risk]] between the contract's reference price and the hedger's actual physical price. The choice between physical (NYMEX WTI) and cash settled (ICE Brent) affects liquidity patterns and price behavior near expiry. Financial participants prefer cash settled; physical traders prefer deliverable for stronger convergence.

## Concrete example

**Concrete:** A trader is long 10 ICE Brent futures (cash settled) at $80.00/bbl. At expiry, the ICE Brent Index settles at $82.50/bbl. Settlement: ($82.50 − $80.00) × 1,000 × 10 = $25,000 credit. No oil changes hands. No pipeline nominations, no tank inspections. Failure mirror: a Singapore jet fuel buyer hedges with cash settled Brent. At settlement Brent is $80.00/bbl but Singapore jet is $92.00/bbl as crack spreads widened. Hedge underperforms by $12.00/bbl, $12,000 per contract of realized [[Basis Risk]]. Cash settlement simplifies logistics, does not eliminate the mismatch between the settlement index and the actual exposure.

**Simplified:** Instead of trucking real barrels of oil or bushels of corn to a warehouse on expiry, the parties just exchange the cash difference between what they agreed and what the published index says on the settlement day. Easier and cheaper to participate, but you are betting on the index, not the actual price you face in your real business. If the index drifts away from your real cost, your hedge does not work as well as you expected.

## Key mechanics and formulas
- **Cash settlement payoff (long):** PnL = (Reference price − Entry price) × Contract size
- **Cash settlement payoff (short):** PnL = (Entry price − Reference price) × Contract size
- **Reference price sources:**
  - ICE Brent: ICE Brent Index (derived from Dated Brent physical market)
  - CME feeder cattle: CME Feeder Cattle Index (cash market survey)
  - Equity index futures: official closing index
  - FX NDFs: official central bank fixing rate
- **Basis risk from cash settlement:** Basis = Physical exposure price − Cash settlement reference price. Managed separately.
- **No convergence guarantee:** Unlike physical delivery, cash settlement does not force futures = spot. Convergence depends on the reference index accuracy.

## Prerequisites
- [[Futures Contract]]
- [[Delivery]]
- [[Basis Risk]]

## Related concepts (learn next)
- [[Delivery]] is the physical alternative, with stronger price anchoring through arbitrage.
- [[Basis Risk]] is the primary cash settlement risk: reference may not match actual exposure.
- [[Forward Contract]] can be physical or cash settled depending on the counterparties.
- [[Swap]] is inherently cash settled, with periodic fixed vs floating payments.
- [[Futures Contract]] specs define cash or physical settlement.
- [[Contango Roll Cost]] applies to both as traders roll between expiries.
- [[Implied Volatility]] in options on cash settled futures reflects uncertainty about the settlement index at expiry.

## Common misconceptions

**"Cash settled contracts track the physical market."** They track a reference index, which may diverge from the actual cost at a specific location, grade, or timing. That divergence is [[Basis Risk]].

**"Cash settlement eliminates delivery risk."** Eliminates physical logistics but introduces settlement risk if the reference is volatile, illiquid, or subject to manipulation on the fixing date.

**"Financial traders should always use cash settled."** Some physically settled contracts (NYMEX WTI) are more liquid with tighter spreads. Liquidity, not settlement method, drives contract choice.

## Sources
- CME Group, "Cash Settled vs. Physically Settled Futures"
- ICE, "Brent Crude Oil Index Methodology"
- John Hull, "Options, Futures, and Other Derivatives"
- Platts, "Methodology and Specifications Guide: Crude Oil"
