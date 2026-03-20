---
aliases: [REER, real effective exchange rate, real exchange rate]
tags:
  - "#fx"
  - "#macro"
date-added: "2026-03-20"
---

# Real Effective Exchange Rate

## Definition
The real effective exchange rate (REER) is a trade weighted average of a country's currency against a basket of its trading partners' currencies, adjusted for relative inflation differences. Unlike the nominal exchange rate, which simply compares 2 currencies, the REER captures the purchasing power of the currency in the context of international trade. When a country's inflation is higher than its trading partners' inflation, its REER appreciates even if the nominal rate stays constant, because its goods become more expensive relative to competitors. REER is mean reverting over long horizons (5 to 15 years), making it one of the few FX indicators with genuine long term predictive power. Central banks, the IMF, and the BIS publish REER indices regularly.

## Why it matters (commodities and FX)
REER provides a fundamental valuation anchor for currencies. A currency with a REER far above its historical average is "overvalued" in purchasing power terms and faces long run depreciation pressure. For commodity exporters, REER matters because sustained commodity booms can cause real appreciation ("Dutch disease"), eroding the competitiveness of non commodity sectors. AUD REER rose to multi decade highs during the 2010 to 2014 mining boom, then reverted sharply as iron ore prices fell. For systematic macro strategies, REER z scores (current REER relative to its long term mean) serve as value signals in FX portfolios, typically combined with [[Carry Trade|carry]] and momentum signals.

## Concrete example
In 2022, the Turkish lira REER index fell to 50 (against a base of 100), signaling extreme real undervaluation after years of high inflation and nominal depreciation. A contrarian value trader buys TRY against a basket of EM currencies, expecting mean reversion. Over 18 months, TRY stabilizes in nominal terms while Turkish inflation gradually declines, and the REER recovers to 60. The position gains roughly 15% in real terms. Conversely, in 2011, the AUD REER reached 130, far above its long term average of 100. A trader short AUD on REER overvaluation was correct in the long run (AUD fell 30% over the next 4 years) but endured 12 months of further REER appreciation before the reversion began, requiring significant patience and risk tolerance.

## Key mechanics and formulas
- **REER formula**: REER = ∏(e_i × P_domestic / P_i)^(w_i), where e_i is the bilateral nominal rate against partner i, P is the price level, and w_i is the trade weight.
- **Simplified**: REER ≈ Nominal effective exchange rate × (Domestic CPI / Foreign CPI basket).
- **Z score**: REER z score = (Current REER − Mean REER) / Std dev of REER. Values above +2 suggest overvaluation; below −2 suggest undervaluation.
- **Mean reversion half life**: Academic estimates range from 3 to 7 years for G10 REER, meaning deviations from the mean correct slowly.
- **Balassa Samuelson effect**: Higher productivity growth in tradeable sectors causes real appreciation without loss of competitiveness, complicating REER interpretation for rapidly developing economies.

## Prerequisites
- [[Spot Rate]]
- [[Currency Pair]]
- [[Purchasing Power Parity]]
- [[Terms of Trade]]

## Related concepts (learn next)
- [[Purchasing Power Parity]]: the theoretical foundation of REER; PPP posits that exchange rates should equalize price levels, and REER measures how far reality deviates.
- [[Terms of Trade]]: commodity price shocks shift REER by changing the relative price of exports to imports.
- [[Dollar Index]]: DXY is a nominal index; the Fed's real trade weighted dollar index is the USD REER equivalent.
- [[Monetary Policy Divergence]]: sustained policy divergence can push REER far from equilibrium, creating long run reversion opportunities.
- [[Petrocurrency]]: petrocurrency REERs are especially cyclical, rising during oil booms and falling during busts.
- [[Central Bank Intervention]]: some CBs intervene specifically because REER is "misaligned" relative to fundamentals.
- [[Uncovered Interest Parity]]: REER mean reversion is a possible explanation for why UIP holds better at long horizons.

## Common misconceptions
1. **REER is a timing tool**: REER mean reversion works over years, not weeks. Using REER as a short term trading signal produces poor results because REER can stay "overvalued" for 3 to 5 years before reverting.
2. **A high REER means the currency will crash**: Real appreciation can be justified by productivity gains (Balassa Samuelson), improved terms of trade, or sustained capital inflows. Not all high REERs are bubbles.
3. **REER data is precise and timely**: CPI data is lagged, trade weights are updated infrequently, and different institutions (IMF, BIS, JPMorgan) use different methodologies, producing REER indices that can disagree by 5 to 10%.

## Sources
- Rogoff, Kenneth, "The Purchasing Power Parity Puzzle," Journal of Economic Literature, 1996.
- IMF, "External Balance Assessment (EBA) Methodology."
- Bank for International Settlements, "Real Effective Exchange Rate Indices," BIS Statistics.
