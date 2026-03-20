---
aliases: [uncovered interest parity, UIP]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Uncovered Interest Parity

## Definition
Uncovered interest parity (UIP) is the theoretical proposition that the expected change in the [[Spot Rate|spot exchange rate]] between 2 currencies should equal the [[Interest Rate Differential|interest rate differential]] between them. In plain English, UIP says that high interest rate currencies should depreciate against low rate currencies by exactly enough to offset the yield advantage, leaving expected returns equal across currencies. Unlike [[Covered Interest Parity|CIP]], UIP involves no forward hedge, leaving the investor exposed to spot risk. UIP is one of the most tested and most rejected hypotheses in international finance: empirically, high rate currencies tend to appreciate rather than depreciate over short to medium horizons, generating the "forward premium puzzle" or "forward discount bias." This persistent failure of UIP is the theoretical foundation for why [[Carry Trade|carry trades]] are profitable.

## Why it matters (commodities and FX)
The failure of UIP is the single most important empirical fact in FX markets for active traders. If UIP held, there would be no risk adjusted return to carry strategies; investing in high yielding AUD or BRL would produce no excess return over low yielding JPY or CHF because the high yielder would depreciate by the rate gap. Since UIP fails, carry trades have delivered positive average returns of 4 to 6% annually across G10 and higher in EM. For commodity traders, UIP failure means that [[Petrocurrency|petrocurrencies]] with high rates (e.g., BRL, NOK) do not fully depreciate against USD, allowing commodity exporters to benefit from both oil prices and carry.

## Concrete example
In 2023, USD interest rates are 5.25% and JPY rates are −0.10%, an IRD of 5.35%. UIP predicts USD/JPY should depreciate (JPY strengthen) by approximately 5.35% over the next year, from 145 to roughly 137. Instead, USD/JPY rises to 151 by October 2023, a 4% USD appreciation. The carry trader who was long USD/JPY earned both the 5.35% carry and a 4% spot gain, a total return of roughly 9.35%. UIP was not just wrong; the spot moved in the opposite direction. However, UIP occasionally "works" violently: in August 2024, USD/JPY crashed from 162 to 142, a 12% move in weeks. Over a multi year horizon, the JPY depreciation may partially reverse, but the timing is unpredictable.

## Key mechanics and formulas
- **UIP condition**: E[S(t+1)] / S(t) = (1 + r_domestic) / (1 + r_foreign), where E[S] is the expected future spot rate.
- **Approximate form**: E[Δs] ≈ r_domestic − r_foreign, where Δs is the percentage change in the exchange rate.
- **Fama regression**: Δs(t+1) = α + β × (f(t) − s(t)) + ε. Under UIP, β = 1. Empirically, β is consistently negative (around −1 to −2), meaning high forward premium currencies appreciate rather than depreciate.
- **Forward premium puzzle**: The systematic finding that β < 1 (and often β < 0) in the Fama regression.
- **Carry trade return**: r_carry ≈ IRD − Δs_actual. Since Δs_actual is often the wrong sign, r_carry > IRD on average.
- **Sharpe ratio of UIP violation**: G10 carry strategies exploiting UIP failure deliver Sharpe ratios of approximately 0.3 to 0.6 before transaction costs.

## Prerequisites
- [[Interest Rate Differential]]
- [[Covered Interest Parity]]
- [[Forward Points]]
- [[Spot Rate]]

## Related concepts (learn next)
- [[Carry Trade]]: the practical strategy that profits from UIP failure by going long high rate currencies and short low rate currencies.
- [[Covered Interest Parity]]: the hedged version of the parity condition, which holds much more closely (though with a [[Cross Currency Basis|basis]]).
- [[Carry Unwind]]: the episodes when UIP temporarily "works" as high yield currencies crash violently.
- [[Forward Points]]: under UIP, forward points should be an unbiased predictor of future spot changes; they are not.
- [[Monetary Policy Divergence]]: the source of large interest rate differentials that UIP predicts should be neutralized by spot moves.
- [[Real Effective Exchange Rate]]: over very long horizons (5 to 10+ years), UIP holds somewhat better, especially for overvalued currencies.
- [[Purchasing Power Parity]]: another long run parity condition that fails in the short run but may hold over decades.

## Common misconceptions
1. **UIP is wrong, so ignore it**: UIP captures a long run force. Over 10+ year horizons, high rate currencies do tend to depreciate, partially vindicating UIP. The failure is most pronounced at horizons of 1 month to 2 years, exactly where carry trades operate.
2. **UIP failure is riskless profit**: Carry returns are compensation for crash risk. The average return is positive, but the distribution is negatively skewed. Carry is a risk premium, not an anomaly.
3. **UIP and CIP are the same thing**: CIP uses a forward contract to eliminate exchange rate risk and holds approximately. UIP is an expectations based condition with no hedge and fails dramatically. They share the same interest rate inputs but are fundamentally different propositions.

## Sources
- Fama, Eugene, "Forward and Spot Exchange Rates," Journal of Monetary Economics, 1984.
- Engel, Charles, "The Forward Discount Anomaly and the Risk Premium," Handbook of International Economics, 2014.
- Burnside, Craig et al., "Do Peso Problems Explain the Returns to the Carry Trade?" Review of Financial Studies, 2011.
