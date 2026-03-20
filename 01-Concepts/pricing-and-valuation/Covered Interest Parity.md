---
aliases: [covered interest parity, CIP]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Covered Interest Parity

## Definition
Covered interest parity (CIP) is the no arbitrage condition stating that the forward exchange rate between 2 currencies must reflect the [[Interest Rate Differential|interest rate differential]] between them. In theory, an investor should earn the same return whether they invest domestically or convert to a foreign currency, invest abroad, and lock in the return with a forward contract. The CIP formula links the [[Spot Rate|spot rate]], the [[Forward Points|forward rate]], and the interest rates of both currencies into a single arbitrage free relationship. CIP was considered an ironclad law of finance until the 2008 financial crisis, after which persistent deviations (measured by the [[Cross Currency Basis|cross currency basis]]) have challenged the assumption that arbitrage capital is unlimited and frictionless.

## Why it matters (commodities and FX)
CIP is the foundation of FX forward pricing. Every [[Forward Points|forward point]] on every [[Currency Pair|currency pair]] is derived from this relationship. Commodity firms that hedge future FX exposures through forwards are implicitly trading CIP. When CIP holds perfectly, there is no free lunch in the forward market. When CIP is violated (as it has been persistently since 2008), the cross currency basis creates real costs or benefits for hedgers. A European oil company hedging USD revenues via EUR/USD forwards may pay or receive an extra 20 to 50 basis points annually depending on the direction of the CIP violation, directly affecting hedging cost calculations.

## Concrete example
Spot EUR/USD = 1.0800. The 1 year USD rate is 5.00% and the 1 year EUR rate is 3.00%. Under CIP, the 1 year forward should be: 1.0800 × (1 + 0.03) / (1 + 0.05) = 1.0800 × 1.03 / 1.05 = 1.0594. The forward points are 1.0594 − 1.0800 = −0.0206 or −206 pips. EUR trades at a forward premium (cheaper in the forward) because EUR rates are lower. A trader borrows USD at 5%, converts to EUR at spot, invests at 3%, and sells EUR forward at 1.0594. The total return in USD should be exactly 5%, the same as staying in USD. If the actual forward is 1.0580 instead of 1.0594 (a −14 pip basis), the trader earns slightly more than 5%, reflecting a CIP violation worth roughly 13 basis points.

## Key mechanics and formulas
- **CIP condition**: Forward / Spot = (1 + r_quote × t) / (1 + r_base × t), where r_quote and r_base are the interest rates for the quote and base currencies, and t is the time fraction.
- **Equivalent form**: Forward = Spot × (1 + r_quote × t) / (1 + r_base × t).
- **Forward points**: Forward − Spot = Spot × [(r_quote − r_base) × t] / (1 + r_base × t), approximately Spot × (r_quote − r_base) × t for small rates.
- **CIP deviation (basis)**: Basis = Implied foreign rate from FX forward − Actual foreign rate. A negative basis for EUR means the FX implied USD borrowing cost exceeds the cash market USD rate.
- **Arbitrage P&L** (when CIP violated): Borrow in 1 currency, convert at spot, invest in the other, hedge with forward. Profit ≈ Notional × Basis × Time.

## Prerequisites
- [[Spot Rate]]
- [[Forward Points]]
- [[Interest Rate Differential]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Cross Currency Basis]]: the market observable deviation from CIP, reflecting USD funding premiums and balance sheet constraints.
- [[Uncovered Interest Parity]]: the unhedged version of CIP, which does not use forwards and empirically fails in the opposite direction.
- [[FX Swap]]: the primary instrument through which CIP is arbitraged or violated, as swaps embed both spot and forward legs.
- [[Forward Points]]: the direct market quotation of the CIP relationship, in pips.
- [[Carry Trade]]: CIP explains why carry is zero when hedged; [[Uncovered Interest Parity|UIP]] failure is why unhedged carry works.
- [[NDF]]: CIP for restricted currencies involves NDFs, where basis can be significantly wider.
- [[Interest Rate Differential]]: the fundamental input to the CIP equation.

## Common misconceptions
1. **CIP always holds**: Since 2008, CIP violations of 10 to 60 basis points have persisted across G10 pairs. Bank capital constraints, regulations (Basel III, leverage ratio), and reserve manager demand for USD create structural deviations.
2. **CIP violations are free money**: Exploiting CIP violations requires balance sheet capacity. Banks face leverage ratio and capital costs that often exceed the basis profit. For unregulated entities, counterparty risk and margin requirements limit arbitrage scale.
3. **CIP only matters for forwards**: CIP violations affect cross currency swap pricing, corporate debt issuance decisions (synthetic vs direct funding), and central bank swap line usage. The basis ripples through the entire fixed income and FX ecosystem.

## Sources
- Du, Wenxin et al., "Deviations from Covered Interest Rate Parity," Journal of Finance, 2018.
- Borio, Claudio et al., "Covered Interest Parity Lost: Understanding the Cross Currency Basis," BIS Quarterly Review, 2016.
- Hull, John C., *Options, Futures, and Other Derivatives*, 11th ed.
