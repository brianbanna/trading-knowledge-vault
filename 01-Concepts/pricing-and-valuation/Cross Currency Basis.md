---
aliases: [cross currency basis, xccy basis, FX basis, dollar basis]
tags:
  - "#fx"
  - "#rates"
date-added: "2026-03-20"
---

# Cross Currency Basis

## Definition
The cross currency basis is the premium or discount in FX swap and cross currency swap markets relative to [[Covered Interest Parity|covered interest parity]] (CIP). Zero basis = CIP holds. Negative basis vs USD = borrowing USD synthetically via FX swaps costs more than borrowing USD in cash markets, signaling excess dollar demand. Since 2008, the basis has been persistently negative for most currencies vs USD, reflecting structural dollar funding demand exceeding the balance sheet supply available for arbitrage. Quoted in basis points per annum, varying by tenor (3 month, 1 year, 5 year).

## Why it matters (commodities and FX)
The basis sets the true cost of FX hedging. A Japanese oil importer buying crude in USD acquires dollars synthetically. If USD/JPY basis is −50 bps, hedging costs 50 bps annually above the raw [[Interest Rate Differential|interest rate differential]]. For European corporates issuing USD debt, a negative EUR/USD basis makes swapping USD proceeds to EUR cheaper than issuing in EUR directly, creating synthetic funding advantage. In stress (March 2020, September 2022), the basis blows out to −100 bps, signaling global dollar funding stress.

## Concrete example
**Concrete:** March 2020. EUR/USD 3 month basis collapses from −20 bps to −150 bps in a week during the global dash for dollars. A European bank rolling 1 billion USD via FX swaps faces an extra cost of 1,000,000,000 × 130/10,000 × 0.25 = $3.25M annualized beyond the rate differential. The Fed opens swap lines with foreign central banks, flooding dollars in. Basis recovers to −30 bps in 2 weeks. A trader who shorted the basis at −150 bps (receiving the distressed premium) and held through recovery earned roughly 120 bps annualized on notional.

**Simplified:** The basis is the gap between what FX swap pricing implies for the dollar rate and the actual dollar rate. If demand for dollars is high and balance sheet to arbitrage is scarce, FX swaps charge an extra fee above the pure rate differential. That fee is the basis. Negative basis means the synthetic dollar borrow is more expensive than the cash dollar borrow. The crisis version is when banks need dollars and cannot find them, so the basis goes deeply negative until central banks add supply.

## Key mechanics and formulas
- **CIP with basis:** Forward = Spot × (1 + r_quote + basis) × t / (1 + r_base × t). Basis adds to the foreign rate side.
- **Basis calc:** Basis = FX implied USD rate − Actual USD rate. Negative = USD funding premium.
- **3 month EUR/USD basis:** −10 to −40 bps calm; −50 to −150 bps stress.
- **JPY/USD basis:** Historically more negative (−30 to −80 bps) because Japanese institutional investors structurally demand USD assets and hedge via FX swaps.
- **Widening catalysts:** Quarter/year end balance sheet constraints, dollar liquidity squeezes, geopolitical stress, MMF outflows.
- **Narrowing catalysts:** Fed swap lines, USD liquidity injections, reduced hedging demand, risk on sentiment.

## Prerequisites
- [[Covered Interest Parity]]
- [[Interest Rate Differential]]
- [[FX Swap]]
- [[Forward Points]]
- [[Spot Rate]]

## Related concepts (learn next)
- [[Covered Interest Parity]]: the theoretical framework from which the basis deviates.
- [[FX Swap]]: the instrument through which the basis is traded and observed.
- [[Central Bank Intervention]]: Fed USD swap lines are the primary tool for compressing the basis during crises.
- [[Carry Trade]]: the basis adds to or subtracts from carry returns depending on funding leg.
- [[NDF]]: EM basis often embedded in NDF pricing, wider deviations reflect capital controls.
- [[Monetary Policy Divergence]]: extreme divergence (Fed tightening, BOJ holding) widens structural USD demand and the basis.
- [[Forward Points]]: forward points embed the basis; stripping out CIP reveals it.

## Common misconceptions

**"The basis should be zero."** Pre 2008, it roughly was. Post 2008, bank balance sheet constraints, leverage ratios, and regulatory costs create a structural floor. Zero basis is now the exception.

**"Negative basis means the dollar is overvalued."** The basis reflects funding supply and demand, not currency valuation. It can stay negative for years without spot USD movement.

**"Only banks care about the basis."** Any entity hedging FX (corporates, pensions, SWFs) pays or receives the basis through forward and swap pricing, even if they never hear the term.

**"The basis is constant across tenors."** Short term (1 week, 1 month) basis is far more volatile than longer tenors, especially at quarter and year ends when banks shrink balance sheet.

## Sources
- Du, Wenxin et al., "Deviations from Covered Interest Rate Parity," Journal of Finance, 2018.
- Borio, Claudio et al., "Covered Interest Parity Lost: Understanding the Cross Currency Basis," BIS Quarterly Review, 2016.
- Avdjiev, Stefan et al., "The Dollar, Bank Leverage, and Real Economic Activity," BIS Working Papers, 2019.
