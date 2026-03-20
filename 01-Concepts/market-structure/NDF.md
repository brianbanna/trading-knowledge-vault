---
aliases: [NDF, non-deliverable forward, non deliverable forward]
tags:
  - "#fx/em"
date-added: "2026-03-20"
---

# NDF

## Definition
A non deliverable forward (NDF) is an FX forward contract that is cash settled in a freely convertible currency (usually USD) rather than physically delivering the 2 currencies at maturity. NDFs exist because certain [[EM Currencies|emerging market currencies]] have capital controls or restricted convertibility that prevent standard deliverable forwards. At maturity, the difference between the contracted NDF rate and the prevailing spot fixing rate is calculated, and the losing party pays the winning party in USD. The most actively traded NDF currencies are CNH/CNY (Chinese yuan), KRW (Korean won), INR (Indian rupee), BRL (Brazilian real), TWD (Taiwan dollar), and IDR (Indonesian rupiah). The NDF market has grown rapidly, reaching approximately 250 billion USD in daily turnover by 2022.

## Why it matters (commodities and FX)
Many major commodity producing and consuming nations have restricted currencies. China (the world's largest commodity importer), India, Brazil, South Korea, and Indonesia all have NDF markets. A commodity trading firm selling iron ore to China and receiving CNY payment must use NDFs or the offshore CNH market to hedge the CNY/USD exposure. NDF pricing often differs from onshore spot rates, creating a premium or discount that reflects market expectations of devaluation, capital control changes, or [[Central Bank Intervention|central bank intervention]]. For systematic EM FX strategies, NDFs are the only way to access many of the highest carry currencies.

## Concrete example
A mining company sells copper to a Korean smelter for payment in KRW in 3 months. The current USD/KRW spot is 1,320 and the 3 month NDF rate is 1,328 (8 won forward premium reflecting higher KRW rates vs USD). The company sells 10 billion KRW notional via NDF at 1,328. At maturity, the KRW fixing is 1,350. The company receives the difference: 10,000,000,000 × (1/1,328 − 1/1,350) = 10,000,000,000 × 0.00001226 = 122,600 USD. This compensates for the weaker KRW received on the physical copper payment. If the fixing had been 1,300 instead, the company would have paid: 10,000,000,000 × (1/1,328 − 1/1,300) = −162,400 USD, but the physical KRW receipts would convert to more USD at the stronger KRW rate.

## Key mechanics and formulas
- **Settlement**: Cash settled in USD (or EUR for some pairs) at maturity. No physical delivery of the restricted currency.
- **NDF P&L**: P&L (USD) = Notional (in foreign currency) × (1/NDF rate − 1/Fixing rate). For pairs quoted as USD/XXX.
- **Fixing rate**: Determined by an official source (e.g., PBOC midpoint for CNY, RBI reference rate for INR, PTAX for BRL) on the fixing date, typically 2 business days before settlement.
- **NDF premium/discount**: The difference between the NDF rate and the onshore deliverable forward rate, reflecting offshore market sentiment and capital flow pressure.
- **Tenor**: Standard tenors range from 1 week to 2 years, with 1 month, 3 month, and 1 year being most liquid.
- **Trading**: Bilateral OTC between banks and clients. Increasingly cleared through CCPs. London and Singapore are the primary NDF trading centers.

## Prerequisites
- [[Spot Rate]]
- [[Forward Points]]
- [[EM Currencies]]
- [[Interest Rate Differential]]

## Related concepts (learn next)
- [[EM Currencies]]: NDFs are the primary hedging and speculative instrument for restricted EM currencies.
- [[Forward Points]]: NDF forward points embed the rate differential plus an additional premium for convertibility risk and capital controls.
- [[Covered Interest Parity]]: CIP deviations for NDF currencies tend to be larger and more persistent than for deliverable G10 pairs.
- [[Cross Currency Basis]]: the NDF basis captures both the standard dollar funding premium and the additional restricted currency premium.
- [[Central Bank Intervention]]: EM central banks actively manage the fixing rates that determine NDF settlement, creating intervention risk.
- [[FX Swap]]: the deliverable equivalent; for NDF currencies, FX swaps may exist onshore but are inaccessible to foreign participants.
- [[Carry Trade]]: NDF markets allow carry traders to access EM yield differentials without needing onshore bank accounts.

## Common misconceptions
1. **NDFs and deliverable forwards are interchangeable**: NDF pricing can diverge significantly from onshore forward pricing due to capital controls, different participant bases, and convertibility risk. This creates arbitrage opportunities that are often unexploitable due to the controls themselves.
2. **The fixing rate is a fair market price**: Fixing rates are often set by central banks or through thin fixing windows. They can be manipulated or managed, and the fixing rate may not reflect the rate at which large transactions can actually be executed onshore.
3. **NDFs are only for hedgers**: Speculative NDF volume is substantial, particularly in CNH, KRW, and INR. Macro hedge funds, prop desks, and systematic funds actively trade NDFs for directional and carry exposure.
4. **NDF markets are small and illiquid**: NDF turnover has grown to approximately 250 billion USD daily, comparable to many G10 pairs. CNH and KRW NDFs are among the most liquid instruments in EM FX.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- McCauley, Robert and Shu, Chang, "Non Deliverable Forwards: 2013 and Beyond," BIS Quarterly Review, 2014.
- Emerging Markets Traders Association (EMTA), "NDF Market Conventions and Documentation."
