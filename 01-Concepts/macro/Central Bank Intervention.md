---
aliases: [central bank intervention, FX intervention, currency intervention]
tags:
  - "#fx"
  - "#macro"
date-added: "2026-03-20"
---

# Central Bank Intervention

## Definition
Central bank intervention is the act of a central bank buying or selling its own currency in the FX market to influence the exchange rate. It can be direct (actual market transactions) or verbal (statements meant to shift expectations without trading). Targets: a specific level (peg or floor), smoothing volatility, or signaling displeasure with direction. Intervention is funded from FX reserves: to strengthen the domestic currency, the CB sells reserves (usually USD) and buys local currency; to weaken it, the CB buys foreign currency and sells local, expanding reserves. Intervention produces discontinuous, gap like price action that standard risk models and stop losses cannot handle, making it one of the most dangerous events for FX traders.

## Why it matters (commodities and FX)
Interventions have produced some of the largest single day FX moves in history: the SNB removing its EUR/CHF 1.20 floor in January 2015 caused 30% CHF appreciation in minutes, bankrupting brokers and hedge funds. For commodity traders, intervention risk is embedded in [[Petrocurrency|petrocurrency]] and [[EM Currencies|EM currency]] exposure. The Bank of Japan intervened in 2022 when USD/JPY hit 152, creating 500+ pip reversals in a single day. Understanding intervention risk is critical for position sizing, stop placement, and the decision to hold through known intervention zones.

## Concrete example

**Concrete:** September 2022, BOJ intervenes for the first time since 1998, selling ~$20bn from reserves to buy JPY after USD/JPY breaches 145. Pair drops from 145.90 to 140.35 in hours, a 555 pip move. Traders long USD/JPY with stops at 144 fill at 142 or worse due to slippage. A second intervention in October at 151.95 pushes USD/JPY to 146 intraday. Interventions ultimately failed to reverse trend: USD/JPY returned to 151 within weeks because the 5%+ [[Interest Rate Differential|rate differential]] held. Contrast SNB January 2015 (removing 1.20 floor on EUR/CHF): EUR/CHF crashed from 1.2010 to 0.8500 in minutes before stabilizing near 1.0000, never returning to 1.20.

**Simplified:** A central bank does not like where its currency sits. So it walks into the FX market with billions and trades against the prevailing flow. If the trend is fundamental (rate gap, structural flow), the intervention slows it but does not reverse it. If the intervention removes a structural commitment like a peg, the gap is permanent and instantaneous. Stops do not save you because there is no liquidity between the old price and the new one.

## Key mechanics and formulas
- **Direct intervention**: CB enters FX market as counterparty, buying or selling through banks. Visible in reserves data with a lag.
- **Sterilized vs unsterilized**: Sterilized intervention offsets the monetary base impact (sells bonds to absorb local currency injected). Unsterilized intervention changes money supply and is more effective.
- **Reserve adequacy**: A CB can always weaken its own currency (by printing) but can only strengthen it as long as reserves last. Reserve coverage ratio = Reserves / (Months of imports).
- **Verbal intervention**: Official statements or "jawboning." Free to execute, loses credibility if not backed by action.
- **Intervention signals**: Unusual volume at key levels, sudden liquidity gaps, coordinated official commentary, finance ministry/CB joint statements.
- **SNB floor (2011 to 2015)**: SNB held EUR/CHF at 1.20 by buying unlimited EUR. Worked until the cost (balance sheet expansion) became politically untenable.

## Prerequisites
- [[Spot Rate]]
- [[Currency Pair]]
- [[G10 Currencies]]
- [[EM Currencies]]

## Related concepts (learn next)
- [[Carry Unwind]]: CB actions are among the most common triggers, creating sudden moves against carry positions.
- [[Monetary Policy Divergence]]: intervention often occurs when policy divergence creates exchange rate moves CBs deem excessive.
- [[Cross Currency Basis]]: central bank swap lines (a form of intervention) compress the basis by providing USD liquidity.
- [[NDF]]: EM central banks influence NDF pricing by managing onshore fixing rates, a form of indirect intervention.
- [[Petrocurrency]]: EM petrocurrency CBs (Russia, Brazil, Nigeria) frequently intervene to smooth oil driven FX volatility.
- [[Real Effective Exchange Rate]]: CBs justify intervention by arguing [[Real Effective Exchange Rate|REER]] is misaligned.
- [[Dollar Index]]: coordinated G7 intervention (Plaza Accord 1985) moved DXY 30%+ over multi year periods.

## Common misconceptions
1. **Interventions always work**: Most unilateral interventions in liquid G10 pairs fail unless aligned with fundamentals or coordinated. The BOJ's 2022 interventions slowed USD/JPY but did not reverse it.
2. **Intervention is announced**: Some are surprise (SNB 2015), others telegraphed (BOJ jawboning at 150). The most dangerous are surprise interventions on Friday afternoons or in Asian hours when liquidity is thin.
3. **Only EM central banks intervene**: G10 CBs intervene too. Switzerland, Japan, Israel, and the ECB (indirectly) have all intervened in FX markets within the last decade.
4. **You can use a stop loss**: In SNB 2015, EUR/CHF gapped from 1.2010 to below 1.0000 with no liquidity. Stops at 1.1950 filled at 1.0200 or worse. Intervention risk cannot be fully managed with stops.

## Sources
- Dominguez, Kathryn and Frankel, Jeffrey, "Does Foreign Exchange Intervention Work?" Institute for International Economics, 1993.
- Ito, Takatoshi, "Is Foreign Exchange Intervention Effective?" NBER Working Paper, 2003.
- Swiss National Bank, "Discontinuation of the Minimum Exchange Rate," Press Release, January 15, 2015.
