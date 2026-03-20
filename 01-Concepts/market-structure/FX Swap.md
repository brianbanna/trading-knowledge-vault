---
aliases: [FX swap, foreign exchange swap, currency swap]
tags:
  - "#fx"
  - "#fx/structure"
date-added: "2026-03-20"
---

# FX Swap

## Definition
An FX swap is a contract in which 2 parties simultaneously agree to exchange a pair of currencies at the [[Spot Rate|spot rate]] on 1 date (the near leg) and reverse that exchange at a pre agreed [[Forward Points|forward rate]] on a future date (the far leg). It is functionally a spot trade combined with an outright forward, packaged as a single transaction. FX swaps are the most traded instrument in the global FX market, accounting for roughly 51% of all FX turnover (approximately 3.8 trillion USD per day as of the 2022 BIS survey). They are primarily used for funding, liquidity management, and rolling maturing FX positions rather than for directional speculation. The price of an FX swap is quoted as [[Forward Points|swap points]], reflecting the [[Interest Rate Differential|interest rate differential]] between the 2 currencies.

## Why it matters (commodities and FX)
Commodity trading firms use FX swaps constantly. A US based oil trader who buys North Sea crude priced in USD but pays shipping and insurance in EUR needs EUR for a specific date and USD back later. An FX swap provides this temporary currency exchange without taking directional FX risk. For banks and institutional investors, FX swaps are the primary tool for managing short term currency funding mismatches. The FX swap market's sheer size means its pricing (the swap points and embedded [[Cross Currency Basis|basis]]) affects all other FX instruments. When swap liquidity dries up (as in March 2020), the entire FX ecosystem seizes.

## Concrete example
A Japanese life insurer holds 500 million USD of US Treasuries funded in JPY. To hedge, it enters a 3 month FX swap: selling USD and buying JPY spot at 150.00, then buying USD and selling JPY forward at 149.20 (swap points of −80 pips reflecting the US/Japan rate differential). The insurer pays 80 pips or approximately 4 million USD annualized for the privilege of holding USD assets with JPY funding. Every 3 months, the swap is rolled at prevailing points. When the [[Cross Currency Basis|basis]] widens from −30 to −80 bps (as in September 2022), the roll cost jumps, squeezing the insurer's net return on Treasuries. If the cost exceeds the Treasury yield pickup, the trade becomes uneconomic and the insurer may sell Treasuries, feeding back into US rates.

## Key mechanics and formulas
- **Near leg**: Exchange at spot rate on settlement date (typically T+2).
- **Far leg**: Reverse exchange at forward rate = Spot + [[Forward Points|swap points]] on the maturity date.
- **Swap points**: Reflect (r_quote − r_base) × time × spot, adjusted by the [[Cross Currency Basis|basis]].
- **Tom/Next swap**: Near leg is tomorrow (T+1), far leg is T+2. Used to roll spot positions daily.
- **Overnight swap**: Near leg today, far leg tomorrow. Used for same day funding needs.
- **P&L on a swap**: Primarily from changes in swap points between trade date and close/roll date.
- **Notional outstanding**: BIS estimates ~100 trillion USD in FX swaps outstanding, making it one of the largest derivative markets globally.
- **No net FX risk**: Because both legs are agreed upfront, the FX swap user has no directional spot exposure (unlike an outright forward).

## Prerequisites
- [[Spot Rate]]
- [[Forward Points]]
- [[Interest Rate Differential]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Forward Points]]: the price of an FX swap, determined by the interest rate differential and the cross currency basis.
- [[Cross Currency Basis]]: the deviation from [[Covered Interest Parity|CIP]] embedded in swap pricing, especially pronounced at quarter and year ends.
- [[Covered Interest Parity]]: the theoretical foundation; FX swaps are the primary instrument through which CIP arbitrage occurs (or fails).
- [[NDF]]: the non deliverable equivalent of an FX swap for restricted currencies, cash settled rather than physically exchanged.
- [[Carry Trade]]: FX swaps are the operational mechanism for implementing and rolling carry positions.
- [[Central Bank Intervention]]: central bank swap lines (e.g., Fed USD swaps with ECB, BOJ) directly inject liquidity into the FX swap market.
- [[Carry Unwind]]: swap market illiquidity during stress episodes forces disorderly position closures.

## Common misconceptions
1. **FX swaps are the same as cross currency swaps**: FX swaps typically involve short tenors (overnight to 1 year) with no intermediate interest payments. Cross currency swaps are multi year instruments with periodic interest exchanges. The mechanics and risk profiles are quite different.
2. **FX swaps involve directional FX risk**: The 2 legs offset each other, so there is no net spot exposure. The risk is in the interest rate differential (swap points may change when rolling) and counterparty credit.
3. **FX swaps are rarely used**: They are the single largest segment of the FX market, exceeding spot, outright forwards, and options combined. Their relative obscurity to retail traders belies their dominance in institutional markets.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- Borio, Claudio et al., "FX and OTC Derivatives Markets Through the Lens of the Triennial Survey," BIS Quarterly Review, 2022.
- Rime, Dagfinn and Schrimpf, Andreas, "The Anatomy of the Global FX Market," BIS Working Paper, 2019.
