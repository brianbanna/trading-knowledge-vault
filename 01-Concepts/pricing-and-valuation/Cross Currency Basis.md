---
aliases: [cross currency basis, xccy basis, FX basis, dollar basis]
tags:
  - "#fx"
  - "#rates"
date-added: "2026-03-20"
---

# Cross Currency Basis

## Definition
The cross currency basis is the premium or discount observed in the FX swap and cross currency swap markets relative to what [[Covered Interest Parity|covered interest parity]] (CIP) predicts. When the basis is zero, CIP holds perfectly. A negative basis for a given currency against USD means that borrowing USD synthetically via FX swaps is more expensive than borrowing USD directly in the cash market, implying excess demand for dollars. Since the 2008 financial crisis, the basis has been persistently negative for most currencies against USD, reflecting structural demand for dollar funding that exceeds the supply of balance sheet available for arbitrage. The basis is quoted in basis points per annum and varies by tenor (3 month, 1 year, 5 year, etc.).

## Why it matters (commodities and FX)
The cross currency basis directly affects the cost of hedging. A Japanese oil importer buying crude in USD must acquire dollars; if the USD/JPY basis is −50 basis points, the hedging cost includes an extra 50 bps annually beyond the raw [[Interest Rate Differential|interest rate differential]]. For European corporates issuing USD debt, a negative EUR/USD basis means that swapping the USD proceeds back to EUR is cheaper than issuing in EUR directly, creating a synthetic funding advantage. In stressed markets (March 2020, September 2022), the basis can widen to −100 bps or more, dramatically increasing FX hedging costs and signaling dollar funding stress globally.

## Concrete example
In March 2020, the EUR/USD 3 month cross currency basis collapsed from −20 bps to −150 bps in a single week as a global dash for dollars unfolded. A European bank that needed to roll 1 billion USD of funding via FX swaps suddenly faced an additional cost of approximately 1,000,000 × (130/10,000) × 0.25 = 3.25 million USD annualized beyond the normal rate differential. The Federal Reserve responded by opening swap lines with foreign central banks, flooding dollars into the system. The basis recovered to −30 bps within 2 weeks. A trader who shorted the basis at −150 bps (receiving the distressed premium) and held through the recovery earned roughly 120 bps annualized on notional, equivalent to significant absolute returns on a large position.

## Key mechanics and formulas
- **CIP with basis**: Forward = Spot × (1 + r_quote + basis) × t / (1 + r_base × t). The basis is added to the foreign rate side.
- **Basis calculation**: Basis = FX implied USD rate − Actual USD rate. Negative = USD funding premium.
- **3 month EUR/USD basis** (typical range): −10 to −40 bps in calm markets; −50 to −150 bps in stress.
- **JPY/USD basis**: Historically more negative (−30 to −80 bps) because Japanese institutional investors structurally demand USD assets and hedge via FX swaps.
- **Widening catalysts**: Quarter end / year end balance sheet constraints, dollar liquidity squeezes, geopolitical stress, money market fund outflows.
- **Narrowing catalysts**: Fed swap lines, USD liquidity injections, reduced demand for USD hedging, risk on sentiment.

## Prerequisites
- [[Covered Interest Parity]]
- [[Interest Rate Differential]]
- [[FX Swap]]
- [[Forward Points]]
- [[Spot Rate]]

## Related concepts (learn next)
- [[Covered Interest Parity]]: the theoretical framework from which the basis deviates; understanding CIP is required to understand the basis.
- [[FX Swap]]: the instrument through which the basis is traded and observed, as swap pricing embeds both the rate differential and the basis.
- [[Central Bank Intervention]]: Fed USD swap lines with foreign central banks are the primary policy tool for compressing the basis during crises.
- [[Carry Trade]]: the basis adds to or subtracts from carry returns depending on the funding leg and direction.
- [[NDF]]: EM basis is often embedded in NDF pricing, with wider deviations reflecting capital controls and convertibility risk.
- [[Monetary Policy Divergence]]: extreme policy divergence (e.g., Fed tightening while BOJ holds) widens the structural demand for USD and thus the basis.
- [[Forward Points]]: forward points embed the basis; stripping out the theoretical CIP component reveals the basis.

## Common misconceptions
1. **The basis should be zero**: Pre 2008, it roughly was. Post 2008, bank balance sheet constraints, leverage ratios, and regulatory costs create a structural floor on basis deviations. Zero basis is now the exception, not the norm.
2. **A negative basis means the dollar is "overvalued"**: The basis reflects funding supply and demand, not currency valuation. A negative basis can persist for years without any spot USD movement.
3. **Only banks care about the basis**: Any entity that hedges FX exposure (corporates, pension funds, sovereign wealth funds) pays or receives the basis through forward and swap pricing, even if they never hear the term.
4. **The basis is constant across tenors**: Short term (1 week, 1 month) basis can be far more volatile than longer tenors, especially at quarter and year ends when banks reduce balance sheet.

## Sources
- Du, Wenxin et al., "Deviations from Covered Interest Rate Parity," Journal of Finance, 2018.
- Borio, Claudio et al., "Covered Interest Parity Lost: Understanding the Cross Currency Basis," BIS Quarterly Review, 2016.
- Avdjiev, Stefan et al., "The Dollar, Bank Leverage, and Real Economic Activity," BIS Working Papers, 2019.
