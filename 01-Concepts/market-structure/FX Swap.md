---
aliases: [FX swap, foreign exchange swap, currency swap]
tags:
  - "#fx"
  - "#fx/structure"
date-added: "2026-03-20"
---

# FX Swap

## Definition
An FX swap is a contract where 2 parties simultaneously agree to exchange a pair of currencies at the [[Spot Rate|spot rate]] on 1 date (near leg) and reverse that exchange at a pre agreed [[Forward Points|forward rate]] on a future date (far leg). Functionally a spot trade combined with an outright forward, packaged as a single transaction. FX swaps are the most traded instrument in global FX, ~51% of turnover (~$3.8 trillion/day per the 2022 BIS survey). Used primarily for funding, liquidity management, and rolling maturing positions rather than directional speculation. Price is quoted as [[Forward Points|swap points]], reflecting the [[Interest Rate Differential|rate differential]] between the 2 currencies.

## Why it matters (commodities and FX)
Commodity trading firms use FX swaps constantly. A US oil trader buying USD priced North Sea crude but paying shipping and insurance in EUR needs EUR for a specific date and USD back later. An FX swap provides the temporary exchange without directional FX risk. For banks and institutional investors, FX swaps are the primary tool for managing short term funding mismatches. The market's size means its pricing (swap points and embedded [[Cross Currency Basis|basis]]) affects all other FX instruments. When swap liquidity dries up (March 2020), the entire FX ecosystem seizes.

## Concrete example

**Concrete:** A Japanese life insurer holds USD 500 million of US Treasuries funded in JPY. To hedge: 3 month FX swap selling USD and buying JPY spot at 150.00, then buying USD and selling JPY forward at 149.20 (swap points −80 pips reflecting US/Japan rate differential). Insurer pays 80 pips, ~$4 million annualized, for the privilege of holding USD assets with JPY funding. Rolled every 3 months at prevailing points. When [[Cross Currency Basis|basis]] widens from −30 to −80 bps (September 2022), roll cost jumps, squeezing the insurer's net return. If cost exceeds Treasury yield pickup, the trade becomes uneconomic and the insurer may sell Treasuries, feeding back into US rates.

**Simplified:** An FX swap is a pair of opposite trades booked together: swap currencies today, swap back at a known rate on a future date. No net directional exposure because both legs are set upfront. Used to temporarily borrow one currency against another. The cost is the difference between the spot rate and the agreed future rate, which reflects the interest rate gap between the two currencies. The biggest FX instrument by volume, mostly invisible to retail.

## Key mechanics and formulas
- **Near leg**: Exchange at spot on settlement date (T+2 typically).
- **Far leg**: Reverse exchange at forward = Spot + [[Forward Points|swap points]] on maturity.
- **Swap points**: (r_quote − r_base) × time × spot, adjusted by [[Cross Currency Basis|basis]].
- **Tom/Next swap**: Near leg tomorrow (T+1), far leg T+2. Used to roll spot positions daily.
- **Overnight swap**: Near leg today, far leg tomorrow. Same day funding needs.
- **PnL on a swap**: Primarily from changes in swap points between trade and close/roll.
- **Notional outstanding**: BIS estimates ~$100 trillion in FX swaps outstanding.
- **No net FX risk**: Both legs agreed upfront; the user has no directional spot exposure (unlike an outright forward).

## Prerequisites
- [[Spot Rate]]
- [[Forward Points]]
- [[Interest Rate Differential]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Forward Points]]: the price of an FX swap.
- [[Cross Currency Basis]]: deviation from [[Covered Interest Parity|CIP]] embedded in swap pricing, pronounced at quarter and year ends.
- [[Covered Interest Parity]]: the theoretical foundation.
- [[NDF]]: non deliverable equivalent for restricted currencies, cash settled.
- [[Carry Trade]]: FX swaps are the mechanism for implementing and rolling carry.
- [[Central Bank Intervention]]: central bank swap lines (Fed USD swaps with ECB, BOJ) inject liquidity directly into the swap market.
- [[Carry Unwind]]: swap illiquidity during stress forces disorderly closures.

## Common misconceptions

**FX swaps are the same as cross currency swaps.** FX swaps are short tenor (overnight to 1 year), no intermediate interest payments. Cross currency swaps are multi year with periodic interest exchanges. Different mechanics and risk profiles.

**FX swaps involve directional FX risk.** The 2 legs offset; no net spot exposure. Risk is in the rate differential (swap points may change on roll) and counterparty credit.

**FX swaps are rarely used.** The single largest FX segment, exceeding spot, outright forwards, and options combined. Obscure to retail, dominant in institutional markets.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- Borio, Claudio et al., "FX and OTC Derivatives Markets Through the Lens of the Triennial Survey," BIS Quarterly Review, 2022.
- Rime, Dagfinn and Schrimpf, Andreas, "The Anatomy of the Global FX Market," BIS Working Paper, 2019.
