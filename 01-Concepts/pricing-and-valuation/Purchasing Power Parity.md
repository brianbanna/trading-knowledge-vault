---
aliases: [PPP, purchasing power parity, Big Mac index]
tags:
  - "#fx"
  - "#macro"
date-added: "2026-03-20"
---

# Purchasing Power Parity

## Definition
Purchasing power parity (PPP) is the theory that exchange rates should adjust so that an identical basket of goods costs the same in every country when expressed in a common currency. In its absolute form, PPP states that the exchange rate between 2 currencies equals the ratio of their price levels: if a basket costs 100 USD in the US and 90 EUR in Europe, then EUR/USD should be 1.1111 (100/90). In its relative form, PPP states that the rate of change in the exchange rate should equal the difference in inflation rates between the 2 countries. PPP is an extremely slow acting force: deviations from PPP can persist for 5 to 15 years before mean reversion occurs. The Economist's Big Mac Index is the most famous informal PPP measure, comparing the price of a McDonald's Big Mac across countries.

## Why it matters (commodities and FX)
PPP provides the ultimate long run anchor for currency valuation. For commodity firms making decade long investment decisions (mine development, refinery construction), PPP based exchange rate forecasts inform capital budgeting. If a company invests in a Brazilian mining operation when BRL is overvalued relative to PPP, the eventual BRL depreciation toward PPP will erode the dollar value of future BRL revenues. For FX portfolio managers, PPP deviations serve as value signals: currencies trading below PPP are "cheap" and expected to appreciate over time, while those above are "rich." Academic research shows that PPP based value strategies generate positive returns with Sharpe ratios of 0.2 to 0.4 when combined with carry and momentum.

## Concrete example
In January 2023, the Big Mac Index shows a Big Mac costs 5.36 USD in the US and 590 JPY in Japan. Implied PPP for USD/JPY = 590 / 5.36 = 110.07. The actual spot rate is 130. The yen is 15% "undervalued" versus PPP. A value oriented fund goes long JPY against USD based on this undervaluation signal. Over 2 years, USD/JPY falls from 130 to 145 (JPY weakens further!), and the PPP signal produced a loss. Eventually, in late 2024, JPY begins to recover as the BOJ normalizes policy, and USD/JPY returns toward 140. The PPP signal was directionally correct but took 2+ years and required enduring a 15 big figure drawdown before any payoff began. This illustrates PPP's core challenge: right in the long run, wrong in the short run.

## Key mechanics and formulas
- **Absolute PPP**: E = P_domestic / P_foreign, where E is the exchange rate and P is the price level.
- **Relative PPP**: ΔE / E ≈ π_domestic − π_foreign, where π is the inflation rate.
- **Big Mac Index implied rate**: PPP rate = Price of Big Mac in local currency / Price of Big Mac in USD.
- **PPP deviation**: % deviation = (Spot rate − PPP rate) / PPP rate × 100.
- **Half life of PPP deviations**: Academic consensus is 3 to 5 years for G10 currencies, meaning a 20% deviation takes 3 to 5 years to shrink to 10%.
- **Penn effect (Balassa Samuelson)**: Poorer countries tend to have lower price levels, so their currencies appear "undervalued" on PPP. This is expected, not a trading signal.

## Prerequisites
- [[Spot Rate]]
- [[Currency Pair]]
- [[Real Effective Exchange Rate]]

## Related concepts (learn next)
- [[Real Effective Exchange Rate]]: REER is the trade weighted, inflation adjusted measure that operationalizes PPP across a basket of trading partners.
- [[Terms of Trade]]: commodity price shocks create persistent PPP deviations for commodity exporters by shifting relative prices.
- [[Uncovered Interest Parity]]: both PPP and UIP are long run parity conditions that fail in the short run but have some power over multi year horizons.
- [[Monetary Policy Divergence]]: policy divergence can push currencies far from PPP for years, as interest rate driven capital flows overwhelm goods market arbitrage.
- [[Petrocurrency]]: petrocurrency PPP is distorted by oil revenues, which inflate the domestic price level (Dutch disease).
- [[Dollar Index]]: comparing DXY to a PPP implied dollar index reveals whether the USD is overvalued or undervalued in real terms.
- [[EM Currencies]]: EM PPP deviations tend to be larger and more persistent due to the Balassa Samuelson effect and capital controls.

## Common misconceptions
1. **PPP is a trading signal for next month**: PPP has zero predictive power at horizons under 1 year. It is a multi year valuation framework, not a timing tool.
2. **The Big Mac Index is a serious valuation model**: It is a simplified illustration of PPP, not a rigorous measure. Differences in labor costs, taxes, rent, and ingredient sourcing make Big Mac prices a noisy proxy for broader price levels.
3. **Currencies always revert to PPP**: Some currencies have been persistently "undervalued" or "overvalued" versus PPP for decades due to structural factors like productivity differentials (Balassa Samuelson), capital controls, and persistent current account imbalances.
4. **PPP and REER are the same thing**: PPP is a theoretical condition; REER is an empirical index. REER incorporates PPP logic but adds trade weights and uses actual CPI data rather than a single goods basket.

## Sources
- Rogoff, Kenneth, "The Purchasing Power Parity Puzzle," Journal of Economic Literature, 1996.
- Taylor, Alan and Taylor, Mark, "The Purchasing Power Parity Debate," Journal of Economic Perspectives, 2004.
- The Economist, "The Big Mac Index" (updated semi annually).
