---
aliases: [CLS, continuous linked settlement, CLS Bank, FX settlement]
tags:
  - "#fx/structure"
  - "#regulation"
date-added: "2026-03-27"
---

# CLS

## Definition
Continuous Linked Settlement (CLS) is a global FX settlement system operated by CLS Bank International. It eliminates settlement risk by settling both legs of an FX trade simultaneously through a payment versus payment (PvP) mechanism. Before CLS launched in 2002, FX trades settled bilaterally: one party could pay its currency leg and the other could fail to deliver, creating [[Herstatt risk]] (named after the 1974 collapse of Bankhaus Herstatt). CLS settles over $6 trillion in FX daily across 18 currencies. It is the single most important piece of FX market infrastructure and a critical component of global financial stability.

## Why it matters (commodities and FX)
Every large FX trade a commodity trader or hedge fund executes is settled through CLS. When a copper trader sells $100M USD/JPY to hedge yen exposure from a smelter contract, both USD and JPY legs must settle. Without CLS, the trader faces the risk that the counterparty receives USD but fails to deliver JPY. CLS holds both payments and releases them simultaneously. For commodity firms operating across multiple currencies (buying crude in USD, selling refined products in EUR, paying suppliers in BRL), CLS ensures settlement risk does not compound across dozens of daily FX trades. CLS settlement cycles also affect the timing and cost of [[FX Swap]] rolls.

## Concrete example
**Concrete:** Swiss commodity trading firm executes spot: buy 200M EUR/USD at 1.0850, T+2. On settlement day CLS requires the firm (through its settlement member bank) to pay in $217M USD by the CLS funding deadline (06:30 CET). Bank A simultaneously pays in EUR 200M. CLS holds both, confirms both have arrived, then releases EUR 200M to the firm and $217M to Bank A at the same instant. Neither party is exposed to the other's credit risk during settlement. Without CLS: firm wires $217M to Bank A at 08:00 Tokyo. Bank A suffers a credit event at 10:00 London before delivering EUR. Firm loses $217M. This is exactly what happened to Herstatt's counterparties in 1974.

**Simplified:** When you trade EUR/USD, you and the counterparty owe each other on different sides of the world at different times. Before CLS, you sent your dollars and prayed the counterparty would send the euros. If they went bust in between, you lost the dollars. CLS sits in the middle: both sides pay CLS, CLS confirms both payments are in, then CLS releases both to the recipients at the same second. No more "I sent, they failed."

## Key mechanics and formulas
- **Payment versus payment (PvP):** Both legs settle simultaneously. If either party fails to fund, neither payment is released.
- **Settlement window:** 5 hour window each business day (07:00 to 12:00 CET), funding deadlines from 06:30 CET.
- **Multilateral netting:** CLS nets each member's obligations across all trades in a given currency, reducing funding required. Netting typically cuts gross settlement obligations by over 95%.
- **Netting efficiency:** Netting ratio = 1 − (net funding required / gross settlement value). 0.96 means only 4% of gross must be funded.
- **Eligible currencies:** 18 as of 2024, including USD, EUR, GBP, JPY, CHF, AUD, CAD, MXN, ZAR, HKD, KRW.
- **Members:** ~70 direct settlement members (major global banks). Smaller banks and buy side firms access CLS through a settlement member as "third parties."

## Prerequisites
- [[Currency Pair]]
- [[FX Swap]]
- [[Counterparty Risk]]
- [[Settlement]]

## Related concepts (learn next)
- [[Herstatt Risk]]: the specific settlement risk CLS was created to eliminate.
- [[FX Swap]]: most commonly CLS settled instrument, with both legs through CLS.
- [[Counterparty Risk]]: CLS transforms bilateral counterparty risk into centralized, netted settlement.
- [[Netting]]: CLS multilateral netting dramatically reduces actual cash flows.
- [[T+2 Settlement]]: standard FX spot cycle CLS operates within.
- [[Prime Brokerage]]: non bank participants access CLS through PB settlement membership.
- [[FX Intervention]]: central bank FX interventions for CLS eligible currencies settle through CLS.

## Common misconceptions

**"CLS settles all FX trades."** CLS covers ~50 to 60% of global FX turnover. Trades in non CLS currencies, same day settlement, and trades between non members settle bilaterally and still carry settlement risk.

**"CLS is a central counterparty (CCP)."** Not a CCP. It does not guarantee trades or take counterparty risk. It ensures both legs settle simultaneously. If unfunded by the deadline, CLS fails the settlement; it does not step in as guarantor.

**"CLS eliminates all FX risk."** Only settlement risk. It does not eliminate [[market risk]], [[counterparty risk]] on unsettled trades, or operational risk. A bank can still default between trade date and settlement date.

## Sources
- CLS Group, "CLS Overview and Settlement Process" (2023)
- BIS Committee on Payments and Market Infrastructures, "FX Settlement Risk" (2019)
- Galati, Gabriele, "Settlement Risk in Foreign Exchange Markets and CLS Bank," BIS Quarterly Review (2002)
- Federal Reserve Bank of New York, "Foreign Exchange Settlement Risk" guidance
