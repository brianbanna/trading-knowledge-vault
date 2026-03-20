---
aliases: [central bank intervention, FX intervention, currency intervention]
tags:
  - "#fx"
  - "#macro"
date-added: "2026-03-20"
---

# Central Bank Intervention

## Definition
Central bank intervention is the act of a central bank buying or selling its own currency in the foreign exchange market to influence the exchange rate. Intervention can be direct (actual market transactions) or verbal (statements intended to shift expectations without trading). It can target a specific level (a peg or floor), smooth excessive volatility, or signal displeasure with the rate's direction. Intervention is funded from foreign exchange reserves: to strengthen the domestic currency, the CB sells reserves (typically USD) and buys the local currency; to weaken it, the CB buys foreign currency and sells the local currency, expanding reserves. Intervention creates discontinuous, gap like price action that standard risk models and stop losses cannot handle, making it one of the most dangerous events for FX traders.

## Why it matters (commodities and FX)
Central bank interventions have historically produced some of the largest single day FX moves in history: the SNB removing its EUR/CHF 1.20 floor in January 2015 caused a 30% CHF appreciation in minutes, bankrupting multiple brokers and hedge funds. For commodity traders, intervention risk is embedded in [[Petrocurrency|petrocurrency]] and [[EM Currencies|EM currency]] exposure. The Bank of Japan intervened to weaken the yen in 2022 when USD/JPY hit 152, creating 500+ pip reversals in a single day. Understanding intervention risk is critical for position sizing, stop loss placement, and the decision of whether to hold positions through known intervention zones.

## Concrete example
In September 2022, the Bank of Japan intervened for the first time since 1998, selling approximately 20 billion USD from reserves to buy JPY after USD/JPY breached 145. The pair dropped from 145.90 to 140.35 in hours, a 555 pip move. Traders who were long USD/JPY with stops at 144 were filled at 142 or worse due to slippage in the illiquid intervention environment. A second intervention in October at 151.95 pushed USD/JPY to 146 intraday. However, the interventions ultimately failed to reverse the trend: USD/JPY returned to 151 within weeks because the underlying [[Interest Rate Differential|rate differential]] of 5%+ remained. In contrast, the SNB's January 2015 intervention (removing the 1.20 floor on EUR/CHF) was a permanent regime change. EUR/CHF crashed from 1.2010 to 0.8500 in minutes before stabilizing near 1.0000, and it never returned to 1.20.

## Key mechanics and formulas
- **Direct intervention**: CB enters the FX market as a counterparty, buying or selling through banks. Visible in reserves data with a lag.
- **Sterilized vs unsterilized**: Sterilized intervention offsets the monetary base impact (sells bonds to absorb the local currency injected). Unsterilized intervention changes the money supply and is more effective.
- **Reserve adequacy**: A CB can always weaken its own currency (by printing it) but can only strengthen it as long as reserves last. Reserve coverage ratio = Reserves / (Months of imports).
- **Verbal intervention**: Official statements or "jawboning." Free to execute but loses credibility if not backed by action.
- **Intervention signals**: Unusual volume at key levels, sudden liquidity gaps, coordinated official commentary, finance ministry/CB joint statements.
- **SNB floor (2011 to 2015)**: The SNB maintained EUR/CHF at 1.20 by buying unlimited EUR. This worked until the cost (swelling balance sheet) became politically untenable.

## Prerequisites
- [[Spot Rate]]
- [[Currency Pair]]
- [[G10 Currencies]]
- [[EM Currencies]]

## Related concepts (learn next)
- [[Carry Unwind]]: central bank actions are among the most common triggers for carry unwinds, as they create sudden, large moves against carry positions.
- [[Monetary Policy Divergence]]: intervention often occurs when policy divergence creates exchange rate moves that CBs deem excessive.
- [[Cross Currency Basis]]: central bank swap lines (a form of intervention) directly compress the basis by providing USD liquidity.
- [[NDF]]: EM central banks influence NDF pricing by managing onshore fixing rates, a form of indirect intervention.
- [[Petrocurrency]]: EM petrocurrency central banks (Russia, Brazil, Nigeria) frequently intervene to smooth oil driven FX volatility.
- [[Real Effective Exchange Rate]]: CBs sometimes justify intervention by arguing the [[Real Effective Exchange Rate|REER]] is misaligned with fundamentals.
- [[Dollar Index]]: coordinated G7 intervention (e.g., Plaza Accord 1985) can move DXY by 30%+ over multi year periods.

## Common misconceptions
1. **Interventions always work**: Most unilateral interventions in liquid G10 pairs fail unless accompanied by a shift in underlying fundamentals. The BOJ's 2022 interventions slowed USD/JPY but did not reverse the trend. Interventions work best when they align with fundamentals or are coordinated among multiple CBs.
2. **Intervention is announced in advance**: Some interventions are "surprise" (SNB 2015). Others are telegraphed (BOJ jawboning at 150). The most dangerous are surprise interventions on a Friday afternoon or in Asian hours when liquidity is thin.
3. **Only EM central banks intervene**: G10 central banks intervene too. Switzerland, Japan, Israel, and even the ECB (indirectly through policy) have all intervened in FX markets within the last decade.
4. **You can just use a stop loss**: In the SNB 2015 event, EUR/CHF gapped from 1.2010 to below 1.0000 with no liquidity in between. Stop losses at 1.1950 were filled at 1.0200 or worse. Intervention risk cannot be fully managed with stops.

## Sources
- Dominguez, Kathryn and Frankel, Jeffrey, "Does Foreign Exchange Intervention Work?" Institute for International Economics, 1993.
- Ito, Takatoshi, "Is Foreign Exchange Intervention Effective?" NBER Working Paper, 2003.
- Swiss National Bank, "Discontinuation of the Minimum Exchange Rate," Press Release, January 15, 2015.
