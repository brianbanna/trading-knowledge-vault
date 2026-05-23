---
aliases: [PPP, purchasing power parity, Big Mac index]
tags:
  - "#fx"
  - "#macro"
date-added: "2026-03-20"
---

# Purchasing Power Parity

## Definition
PPP says exchange rates should adjust so an identical basket of goods costs the same in every country when expressed in a common currency. Absolute PPP: the rate between 2 currencies equals the ratio of their price levels. If a basket costs 100 USD in the US and 90 EUR in Europe, EUR/USD should be 1.1111. Relative PPP: the rate of change in the exchange rate equals the inflation differential. PPP is slow: deviations persist 5 to 15 years before reverting. The Big Mac Index is the most famous informal PPP measure.

## Why it matters (commodities and FX)
PPP is the long run anchor for currency valuation. Commodity firms making decade long investments (mines, refineries) use PPP based forecasts for capital budgeting. Investing in a Brazilian mine while BRL is overvalued versus PPP means future BRL revenues lose dollar value as the rate reverts. For FX managers, PPP deviations are value signals: cheap currencies appreciate over years. PPP based value strategies deliver Sharpe ratios of 0.2 to 0.4 when combined with carry and momentum.

## Concrete example

**Concrete:** January 2023. Big Mac costs $5.36 in the US, 590 JPY in Japan. Implied PPP for USD/JPY = 590 / 5.36 = 110.07. Spot is 130. Yen is 15% undervalued. A value fund goes long JPY versus USD. Over 2 years, USD/JPY rises to 145 (yen weaker), then recovers toward 140 in late 2024 as the BOJ normalizes. Signal was directionally right but required absorbing a 15 big figure drawdown and 2 years of pain before payoff. Classic PPP problem: right long run, wrong short run.

**Simplified:** A basket of goods should cost the same everywhere once you convert currencies. If a Big Mac is way cheaper in Japan than in the US, the yen looks cheap. Eventually the yen should strengthen back to fair value. But this can take years, and in the meantime the currency can move further away. PPP is a slow gravitational pull, not a near term forecast.

## Key mechanics and formulas
- **Absolute PPP**: E = P_domestic / P_foreign
- **Relative PPP**: ΔE / E ≈ π_domestic − π_foreign
- **Big Mac implied rate**: PPP rate = Local Big Mac price / US Big Mac price in USD
- **PPP deviation**: (Spot − PPP) / PPP × 100
- **Half life**: 3 to 5 years for G10. A 20% deviation takes 3 to 5 years to halve.
- **Penn effect (Balassa Samuelson)**: poorer countries have lower price levels, so their currencies appear undervalued on PPP. Expected, not a signal.

## Prerequisites
- [[Spot Rate]]
- [[Currency Pair]]
- [[Real Effective Exchange Rate]]

## Related concepts (learn next)
- [[Real Effective Exchange Rate]]: trade weighted, inflation adjusted operationalization of PPP across multiple partners.
- [[Terms of Trade]]: commodity shocks create persistent PPP deviations for exporters.
- [[Uncovered Interest Parity]]: both PPP and UIP are long run parities that fail short term.
- [[Monetary Policy Divergence]]: policy gaps push currencies far from PPP for years.
- [[Petrocurrency]]: oil revenue distorts PPP via Dutch disease.
- [[Dollar Index]]: comparing DXY to a PPP implied dollar index reveals real over/undervaluation.
- [[EM Currencies]]: EM deviations are larger and more persistent (Balassa Samuelson, capital controls).

## Common misconceptions
1. **PPP is a near term signal**: zero predictive power under 1 year. Multi year framework, not timing tool.
2. **Big Mac Index is rigorous**: it is illustrative. Labor, rent, taxes, sourcing make Big Mac prices a noisy proxy.
3. **Currencies always revert to PPP**: some stay misvalued for decades due to productivity differentials, capital controls, persistent current account gaps.
4. **PPP and REER are the same**: PPP is theoretical, REER is an empirical trade weighted index using CPI.

## Sources
- Rogoff, Kenneth, "The Purchasing Power Parity Puzzle," Journal of Economic Literature, 1996.
- Taylor, Alan and Taylor, Mark, "The Purchasing Power Parity Debate," Journal of Economic Perspectives, 2004.
- The Economist, "The Big Mac Index" (updated semi annually).
