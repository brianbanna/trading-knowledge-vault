---
aliases: [CLS, continuous linked settlement, CLS Bank, FX settlement]
tags:
  - "#fx/structure"
  - "#regulation"
date-added: "2026-03-27"
---

# CLS

## Definition
Continuous Linked Settlement (CLS) is a global settlement system operated by CLS Bank International that eliminates settlement risk in foreign exchange transactions by settling both legs of an FX trade simultaneously through a payment-versus-payment (PvP) mechanism. Before CLS launched in 2002, FX trades were settled bilaterally, meaning one party could pay out its currency leg and the other party could fail to deliver, creating [[Herstatt risk]] (named after the 1974 collapse of Bankhaus Herstatt). CLS settles over $6 trillion in FX transactions daily across 18 currencies. It is the single most important piece of FX market infrastructure and a critical component of global financial stability.

## Why it matters (commodities and FX)
Every large FX transaction that a commodity trader or hedge fund executes is likely settled through CLS. When a copper trader sells 100 million USD/JPY to hedge Japanese yen exposure from a smelter contract, both the USD and JPY legs must settle. Without CLS, the trader faces the risk that their counterparty receives the USD but fails to deliver the JPY. CLS eliminates this by holding both payments and releasing them simultaneously. For commodity firms operating across multiple currencies (buying crude in USD, selling refined products in EUR, paying suppliers in BRL), CLS ensures that FX settlement risk does not compound across the dozens of daily FX trades. Understanding CLS is also important for [[FX Swap]] pricing, because CLS settlement cycles affect the timing and cost of rolling positions.

## Concrete example
A Swiss commodity trading firm executes a spot trade: buy 200 million EUR/USD at 1.0850 with Bank A, settling T+2. On settlement day, CLS requires the firm (through its settlement member bank) to pay in $217 million USD by the CLS funding deadline (06:30 CET). Simultaneously, Bank A must pay in EUR 200 million. CLS holds both payments, confirms both have arrived, and then releases EUR 200 million to the firm and USD 217 million to Bank A at the same instant. Neither party is exposed to the other's credit risk during settlement.

The fail scenario without CLS: the firm wires $217 million to Bank A at 08:00 Tokyo time. Bank A suffers a credit event at 10:00 London time before delivering the EUR. The firm loses $217 million. This is exactly what happened to Herstatt's counterparties in 1974. CLS makes this scenario impossible for participating currencies.

## Key mechanics and formulas
- **Payment-versus-payment (PvP)**: Both legs of the trade are settled simultaneously. If either party fails to fund, neither payment is released.
- **Settlement window**: CLS settles during a 5 hour window each business day (07:00 to 12:00 CET), with funding deadlines starting at 06:30 CET.
- **Multilateral netting**: CLS nets each member's obligations across all trades in a given currency, reducing the total funding required. Netting typically reduces gross settlement obligations by over 95%.
- **Netting efficiency**: Netting ratio = 1 - (net funding required / gross settlement value). A ratio of 0.96 means only 4% of the gross value must actually be funded.
- **Eligible currencies**: 18 currencies as of 2024, including USD, EUR, GBP, JPY, CHF, AUD, CAD, and major EM currencies like MXN, ZAR, HKD, and KRW.
- **CLS settlement members**: Approximately 70 direct settlement members (major global banks). Smaller banks and buy-side firms access CLS through a settlement member as "third parties."

## Prerequisites
- [[Currency Pair]]
- [[FX Swap]]
- [[Counterparty Risk]]
- [[Settlement]]

## Related concepts (learn next)
- [[Herstatt Risk]]: the specific settlement risk that CLS was created to eliminate, named after the 1974 bank failure.
- [[FX Swap]]: the most commonly CLS-settled instrument, with both the near and far legs going through CLS.
- [[Counterparty Risk]]: CLS transforms bilateral counterparty risk into a centralized, netted settlement process.
- [[Netting]]: CLS's multilateral netting dramatically reduces the actual cash flows needed to settle FX trades.
- [[T+2 Settlement]]: the standard FX spot settlement cycle that CLS operates within.
- [[Prime Brokerage]]: non-bank participants typically access CLS through their prime broker's settlement membership.
- [[FX Intervention]]: central bank FX interventions for CLS-eligible currencies are also settled through CLS.

## Common misconceptions
1. **"CLS settles all FX trades"**: CLS covers about 50% to 60% of global FX turnover. Trades in non-CLS currencies, same-day settlement trades, and trades between non-members settle bilaterally and still carry settlement risk.
2. **"CLS is a central counterparty (CCP)"**: CLS is not a CCP. It does not guarantee trades or take on counterparty risk. It simply ensures that both legs settle simultaneously. If a trade is not funded by the deadline, CLS can fail the settlement, but it does not step in as a guarantor.
3. **"CLS eliminates all FX risk"**: CLS eliminates settlement risk only. It does not eliminate [[market risk]], [[counterparty risk]] on unsettled trades, or operational risk. A bank can still default on its obligations between trade date and settlement date.

## Sources
- CLS Group, "CLS Overview and Settlement Process" (2023)
- BIS Committee on Payments and Market Infrastructures, "FX Settlement Risk" (2019)
- Galati, Gabriele, "Settlement Risk in Foreign Exchange Markets and CLS Bank," BIS Quarterly Review (2002)
- Federal Reserve Bank of New York, "Foreign Exchange Settlement Risk" guidance
