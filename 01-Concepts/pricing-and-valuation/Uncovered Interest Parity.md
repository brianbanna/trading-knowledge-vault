---
aliases: [uncovered interest parity, UIP]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Uncovered Interest Parity

## Definition
UIP says the expected change in the [[Spot Rate|spot exchange rate]] between 2 currencies should equal the [[Interest Rate Differential|interest rate differential]]. In plain English: high rate currencies should depreciate against low rate currencies by exactly enough to offset the yield advantage, leaving expected returns equal across currencies. Unlike [[Covered Interest Parity|CIP]], UIP involves no forward hedge. UIP is 1 of the most tested and most rejected hypotheses in international finance: empirically, high rate currencies appreciate rather than depreciate over short to medium horizons (the "forward premium puzzle"). This persistent failure is the theoretical foundation for why [[Carry Trade|carry trades]] are profitable.

## Why it matters (commodities and FX)
The failure of UIP is the single most important empirical fact in FX for active traders. If UIP held, carry strategies would earn no risk adjusted return; high yielding AUD or BRL would depreciate by the rate gap. Since UIP fails, carry has delivered 4 to 6% annual returns in G10 and higher in EM. For commodity traders, UIP failure means [[Petrocurrency|petrocurrencies]] with high rates (BRL, NOK) do not fully depreciate against USD, letting exporters benefit from both oil prices and carry.

## Concrete example

**Concrete:** 2023. USD rates 5.25%, JPY rates −0.10%, IRD 5.35%. UIP predicts USD/JPY should depreciate (JPY strengthen) by ~5.35% over 1 year, from 145 to ~137. Instead, USD/JPY rises to 151 by October 2023, a 4% USD appreciation. The carry trader long USD/JPY earned the 5.35% carry plus a 4% spot gain, total ~9.35%. UIP was not just wrong, spot moved the opposite direction. Then in August 2024, USD/JPY crashed from 162 to 142, a 12% move in weeks. Long run, JPY depreciation may partially reverse; timing is unpredictable.

**Simplified:** Textbook says: if you can earn 5% on dollars and 0% on yen, the yen must appreciate 5% to make both equally attractive. Real world says: the yen does not appreciate. It often weakens further. So a trader who borrows yen and buys dollars earns the rate gap and the spot move on top. That works for years, then snaps back hard in a few weeks of pure carnage. The pattern is consistent enough to be a strategy and dangerous enough to blow accounts.

## Key mechanics and formulas
- **UIP condition**: E[S(t+1)] / S(t) = (1 + r_domestic) / (1 + r_foreign)
- **Approximate form**: E[Δs] ≈ r_domestic − r_foreign
- **Fama regression**: Δs(t+1) = α + β × (f(t) − s(t)) + ε. Under UIP, β = 1. Empirically, β is consistently negative (around −1 to −2), meaning high forward premium currencies appreciate rather than depreciate.
- **Forward premium puzzle**: systematic finding that β < 1 (often β < 0).
- **Carry trade return**: r_carry ≈ IRD − Δs_actual. Since Δs_actual is often wrong sign, r_carry > IRD on average.
- **Sharpe ratio of UIP violation**: G10 carry delivers 0.3 to 0.6 before transaction costs.

## Prerequisites
- [[Interest Rate Differential]]
- [[Covered Interest Parity]]
- [[Forward Points]]
- [[Spot Rate]]

## Related concepts (learn next)
- [[Carry Trade]]: practical strategy that profits from UIP failure.
- [[Covered Interest Parity]]: hedged version, holds much more closely (with a [[Cross Currency Basis|basis]]).
- [[Carry Unwind]]: episodes when UIP temporarily works as high yielders crash.
- [[Forward Points]]: under UIP, forward points should be an unbiased predictor of future spot. They are not.
- [[Monetary Policy Divergence]]: source of large IRDs UIP says should be neutralized.
- [[Real Effective Exchange Rate]]: over 5 to 10+ years, UIP holds somewhat better, especially for overvalued currencies.
- [[Purchasing Power Parity]]: another long run parity that fails short term, may hold over decades.

## Common misconceptions
1. **UIP is wrong, ignore it**: UIP captures a long run force. Over 10+ year horizons, high rate currencies do tend to depreciate, partially vindicating it. Failure is most pronounced 1 month to 2 years, where carry operates.
2. **UIP failure is riskless profit**: carry returns are compensation for crash risk. Average positive, distribution negatively skewed. Risk premium, not anomaly.
3. **UIP and CIP are the same**: CIP uses a forward to eliminate FX risk and holds approximately. UIP is an expectations condition with no hedge and fails dramatically. Same rate inputs, different propositions.
4. **Carry always works**: Aug 2024 yen unwind moved 12% in weeks. Strategies sized as if UIP failure is permanent blow up in the tail.

## Sources
- Fama, Eugene, "Forward and Spot Exchange Rates," Journal of Monetary Economics, 1984.
- Engel, Charles, "The Forward Discount Anomaly and the Risk Premium," Handbook of International Economics, 2014.
- Burnside, Craig et al., "Do Peso Problems Explain the Returns to the Carry Trade?" Review of Financial Studies, 2011.
