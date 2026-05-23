---
aliases: [covered interest parity, CIP]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Covered Interest Parity

## Definition
Covered interest parity (CIP) is the no arbitrage condition stating that the forward exchange rate between 2 currencies reflects the [[Interest Rate Differential|interest rate differential]] between them. An investor should earn the same return whether investing domestically or converting to foreign currency, investing abroad, and locking the return with a forward. The CIP formula links [[Spot Rate|spot]], [[Forward Points|forward]], and the 2 interest rates into a single arbitrage free relationship. CIP was considered an ironclad law until 2008, after which persistent deviations (the [[Cross Currency Basis|cross currency basis]]) challenged the assumption that arbitrage capital is unlimited and frictionless.

## Why it matters (commodities and FX)
CIP is the foundation of FX forward pricing. Every [[Forward Points|forward point]] on every [[Currency Pair|pair]] derives from this relationship. Commodity firms hedging future FX exposure via forwards implicitly trade CIP. When CIP holds, there is no free lunch in the forward market. When CIP is violated (as it has been since 2008), the cross currency basis creates real costs or benefits for hedgers. A European oil company hedging USD revenue via EURUSD forwards pays or receives an extra 20 to 50 bps annually depending on basis direction, directly affecting hedging cost.

## Concrete example
**Concrete:** Spot EURUSD 1.0800. 1Y USD rate 5.00%, 1Y EUR rate 3.00%. Under CIP, 1Y forward should = 1.0800 × 1.03 / 1.05 = 1.0594. Forward points = −206 pips. EUR at forward premium (cheaper forward) because EUR rates are lower. Trader borrows USD at 5%, converts to EUR at spot, invests at 3%, sells EUR forward at 1.0594. Total USD return = exactly 5%, same as staying in USD. If actual forward is 1.0580 (−14 pip basis), trader earns slightly more than 5%, a CIP violation worth ~13 bps.

**Simplified:** If borrowing in dollars at 5% and parking in euros at 3% were profitable after hedging the FX risk forward, traders would do it until the forward rate adjusted to wipe out the gain. That adjustment is CIP: the forward price has to match the rate gap exactly. Since 2008, balance sheet costs at banks prevent full arbitrage, so a small mispricing (the basis) persists. Hedgers pay or receive it depending on which side they sit on.

## Key mechanics and formulas
- **CIP condition**: Forward / Spot = (1 + r_quote × t) / (1 + r_base × t), where r_quote and r_base are the quote and base currency rates and t is the time fraction.
- **Equivalent form**: Forward = Spot × (1 + r_quote × t) / (1 + r_base × t).
- **Forward points**: Forward − Spot = Spot × [(r_quote − r_base) × t] / (1 + r_base × t) ≈ Spot × (r_quote − r_base) × t for small rates.
- **CIP deviation (basis)**: Basis = Implied foreign rate from FX forward − Actual foreign rate. Negative basis for EUR means FX implied USD borrowing cost exceeds the cash market USD rate.
- **Arbitrage P&L** (when CIP violated): Borrow 1 currency, convert at spot, invest in the other, hedge forward. Profit ≈ Notional × Basis × Time.

## Prerequisites
- [[Spot Rate]]
- [[Forward Points]]
- [[Interest Rate Differential]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Cross Currency Basis]]: the market observable CIP deviation, reflecting USD funding premiums and balance sheet constraints.
- [[Uncovered Interest Parity]]: the unhedged version, which fails empirically in the opposite direction.
- [[FX Swap]]: the primary instrument through which CIP is arbitraged or violated; swaps embed both legs.
- [[Forward Points]]: direct market quotation of CIP, in pips.
- [[Carry Trade]]: CIP explains why hedged carry is zero; [[Uncovered Interest Parity|UIP]] failure is why unhedged carry works.
- [[NDF]]: CIP for restricted currencies involves NDFs, where basis can widen significantly.
- [[Interest Rate Differential]]: fundamental input to CIP.

## Common misconceptions
**"CIP always holds."** Since 2008, violations of 10 to 60 bps persist across G10 pairs. Bank capital constraints, Basel III leverage ratio, and reserve manager USD demand create structural deviations.

**"CIP violations are free money."** Exploiting them requires balance sheet capacity. Banks face leverage ratio and capital costs that often exceed the basis profit. For unregulated entities, counterparty and margin requirements limit arbitrage scale.

**"CIP only matters for forwards."** Violations affect cross currency swap pricing, corporate debt issuance decisions (synthetic vs direct funding), and central bank swap line usage. The basis ripples through the entire fixed income and FX ecosystem.

## Sources
- Du, Wenxin et al., "Deviations from Covered Interest Rate Parity," Journal of Finance, 2018.
- Borio, Claudio et al., "Covered Interest Parity Lost: Understanding the Cross Currency Basis," BIS Quarterly Review, 2016.
- Hull, John C., *Options, Futures, and Other Derivatives*, 11th ed.
