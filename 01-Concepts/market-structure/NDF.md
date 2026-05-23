---
aliases: [NDF, non-deliverable forward, non deliverable forward]
tags:
  - "#fx/em"
date-added: "2026-03-20"
---

# NDF

## Definition
A non deliverable forward (NDF) is an FX forward cash settled in a freely convertible currency (usually USD) rather than physically delivering the 2 currencies at maturity. NDFs exist because certain [[EM Currencies|emerging market currencies]] have capital controls or restricted convertibility that block standard deliverable forwards. At maturity the difference between the contracted NDF rate and the spot fixing is calculated, and the losing party pays in USD. The most traded NDF currencies: CNH/CNY, KRW, INR, BRL, TWD, IDR. NDF turnover reached roughly 250 billion USD daily by 2022.

## Why it matters (commodities and FX)
Many major commodity producing and consuming nations have restricted currencies. China (largest commodity importer), India, Brazil, South Korea, Indonesia all have NDF markets. A commodity firm selling iron ore to China and receiving CNY payment uses NDFs or offshore CNH to hedge. NDF pricing diverges from onshore spot, creating a premium or discount that reflects expectations of devaluation, capital control changes, or [[Central Bank Intervention|intervention]]. For systematic EM FX strategies, NDFs are the only access to many of the highest carry currencies.

## Concrete example

**Concrete:** A mining company sells copper to a Korean smelter for KRW payment in 3 months. Spot USD/KRW = 1,320, 3M NDF = 1,328 (8 won forward premium reflecting higher KRW rates). The company sells 10B KRW notional via NDF at 1,328. At maturity, the fixing prints 1,350. The company receives: 10,000,000,000 × (1/1,328 minus 1/1,350) = 122,600 USD. This compensates for the weaker KRW received on physical copper. If the fixing had printed 1,300, the company would pay 162,400 USD on the NDF, but physical KRW receipts convert to more USD at the stronger rate.

**Simplified:** A forward on a currency you cannot actually deliver. Common in EM where the central bank restricts who can buy and sell the local currency. You agree a rate today; at maturity you settle the difference in USD instead of swapping the currencies. The hedge works economically even though the restricted currency never crosses borders.

## Key mechanics and formulas
- **Settlement:** cash settled in USD (or EUR for some pairs). No physical delivery.
- **NDF PnL (USD/XXX):** PnL (USD) = Notional in foreign ccy × (1/NDF rate minus 1/Fixing rate).
- **Fixing rate:** set by an official source (PBOC midpoint for CNY, RBI reference for INR, PTAX for BRL) on the fixing date, T-2 before settlement.
- **NDF premium/discount:** the gap between NDF and onshore deliverable forward, reflecting offshore sentiment and capital flow pressure.
- **Tenor:** 1 week to 2 years; 1M, 3M, 1Y are most liquid.
- **Trading:** bilateral OTC between banks and clients; increasingly cleared via CCPs. London and Singapore are the primary centers.

## Prerequisites
- [[Spot Rate]]
- [[Forward Points]]
- [[EM Currencies]]
- [[Interest Rate Differential]]

## Related concepts (learn next)
- [[EM Currencies]]: NDFs are the primary instrument for restricted EM
- [[Forward Points]]: NDF points embed rate differential plus convertibility risk premium
- [[Covered Interest Parity]]: CIP deviations for NDFs are larger and more persistent than G10
- [[Cross Currency Basis]]: NDF basis captures dollar funding premium plus restricted ccy premium
- [[Central Bank Intervention]]: EM central banks manage fixings, creating intervention risk
- [[FX Swap]]: deliverable equivalent; for NDF currencies, onshore FX swaps exist but are inaccessible to foreign participants
- [[Carry Trade]]: NDFs give carry traders access to EM yield without onshore accounts

## Common misconceptions
1. **NDFs and deliverable forwards are interchangeable.** NDF pricing diverges from onshore due to capital controls, different participant bases, and convertibility risk. Arbitrage exists but is often unexploitable because of the controls.
2. **The fixing is a fair market price.** Fixings are set by central banks or via thin windows. They can be managed and may not reflect rates at which large transactions actually execute onshore.
3. **NDFs are only for hedgers.** Speculative volume is substantial in CNH, KRW, INR. Macro funds, prop desks, and systematic funds trade NDFs actively for directional and carry exposure.
4. **NDF markets are small.** Turnover reached 250B USD daily, comparable to many G10 pairs. CNH and KRW NDFs are among the most liquid in EM FX.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- McCauley, Robert and Shu, Chang, "Non Deliverable Forwards: 2013 and Beyond," BIS Quarterly Review, 2014.
- Emerging Markets Traders Association (EMTA), "NDF Market Conventions and Documentation."
