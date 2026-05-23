---
aliases: [REER, real effective exchange rate, real exchange rate]
tags:
  - "#fx"
  - "#macro"
date-added: "2026-03-20"
---

# Real Effective Exchange Rate

## Definition
REER is a trade weighted average of a currency against its trading partners, adjusted for relative inflation. Unlike the nominal rate, which compares 2 currencies, REER captures purchasing power in the context of international trade. Higher domestic inflation than trading partners causes REER to appreciate even with the nominal rate flat, because goods become more expensive versus competitors. REER mean reverts over 5 to 15 years, giving it real long term predictive power. IMF, BIS, and central banks publish REER indices.

## Why it matters (commodities and FX)
REER is a fundamental valuation anchor. A REER far above its historical average implies overvaluation in purchasing power terms and long run depreciation pressure. For commodity exporters, sustained booms cause real appreciation (Dutch disease), eroding non commodity competitiveness. AUD REER hit multi decade highs during the 2010 to 2014 mining boom, then reverted sharply as iron ore fell. Systematic macro uses REER z scores as value signals alongside [[Carry Trade|carry]] and momentum.

## Concrete example

**Concrete:** 2022. Turkish lira REER index falls to 50 (base 100) after years of high inflation and nominal depreciation. Contrarian value trader buys TRY against an EM basket expecting reversion. Over 18 months, TRY stabilizes nominally, Turkish inflation eases, REER recovers to 60. Position gains 15% in real terms. Contrast: in 2011, AUD REER hit 130 versus a long term mean of 100. Trader short AUD on overvaluation was right (AUD fell 30% over 4 years) but absorbed 12 months of further appreciation before the turn.

**Simplified:** REER asks: adjusted for inflation and weighted by who you trade with, is your currency cheap or expensive? Currencies that get far above their long run average usually drift back down, eventually. Currencies that get far below usually drift back up. The catch is "eventually" can mean years, and you can be early and lose a lot before being right.

## Key mechanics and formulas
- **REER**: ∏(e_i × P_domestic / P_i)^(w_i), where e_i is the bilateral nominal rate against partner i, P is the price level, w_i is the trade weight.
- **Simplified**: REER ≈ Nominal effective rate × (Domestic CPI / Foreign CPI basket).
- **Z score**: (Current REER − Mean REER) / Std dev. Above +2 = overvalued, below −2 = undervalued.
- **Mean reversion half life**: 3 to 7 years for G10.
- **Balassa Samuelson**: faster productivity growth in tradeables causes real appreciation without losing competitiveness, complicating interpretation for developing economies.

## Prerequisites
- [[Spot Rate]]
- [[Currency Pair]]
- [[Purchasing Power Parity]]
- [[Terms of Trade]]

## Related concepts (learn next)
- [[Purchasing Power Parity]]: theoretical foundation. PPP says rates should equalize price levels; REER measures the deviation.
- [[Terms of Trade]]: commodity shocks shift REER by changing relative export/import prices.
- [[Dollar Index]]: DXY is nominal. The Fed's real trade weighted dollar index is the USD REER equivalent.
- [[Monetary Policy Divergence]]: sustained gaps push REER far from equilibrium.
- [[Petrocurrency]]: petrocurrency REERs are cyclical with oil.
- [[Central Bank Intervention]]: CBs intervene when REER is "misaligned" relative to fundamentals.
- [[Uncovered Interest Parity]]: REER mean reversion may explain why UIP holds better at long horizons.

## Common misconceptions
1. **REER is a timing tool**: reversion runs in years, not weeks. Short term signal quality is poor.
2. **High REER means crash**: real appreciation can be justified by productivity, terms of trade, or capital inflows. Not all high REERs are bubbles.
3. **REER data is precise**: CPI is lagged, trade weights are updated infrequently, IMF/BIS/JPMorgan use different methodologies. Indices can disagree by 5 to 10%.
4. **REER replaces nominal rates**: REER is the valuation anchor; nominal rates drive transactional P&L. Both matter.

## Sources
- Rogoff, Kenneth, "The Purchasing Power Parity Puzzle," Journal of Economic Literature, 1996.
- IMF, "External Balance Assessment (EBA) Methodology."
- Bank for International Settlements, "Real Effective Exchange Rate Indices," BIS Statistics.
