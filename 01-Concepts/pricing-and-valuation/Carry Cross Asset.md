---
aliases: [cross asset carry, carry factor, systematic carry]
tags:
  - "#quant"
  - "#macro"
date-added: "2026-03-20"
---

# Carry Cross Asset

## Definition
Cross-asset carry is a systematic investment factor that captures the return earned from holding a higher-yielding asset funded by a lower-yielding one, applied consistently across FX, fixed income, commodities, and equities. In FX, carry is the interest rate differential: going long a high-rate currency (e.g., BRL, MXN) and short a low-rate currency (e.g., JPY, CHF). In commodities, carry is the [[roll yield]]: going long backwardated markets (where the futures curve slopes downward, implying positive roll) and short contangoed markets. In bonds, carry is the yield pickup: owning longer-duration bonds funded at the short rate. Carry is one of the oldest and most persistent risk premia in finance, generating positive average returns over decades but punctuated by severe drawdowns ("crash risk"). As a systematic factor, carry can be harvested mechanically without forecasting ability, making it a foundational building block for [[CTA]] and quantitative macro strategies.

## Why it matters (commodities and FX)
Carry is the single most studied and traded factor in FX, responsible for trillions of dollars in positioning. The classic "carry trade" (long AUD, NZD, BRL vs. short JPY, CHF, EUR) has generated average annual returns of 4 to 6% historically but with tail risk: the 2008 financial crisis saw carry trade portfolios lose 20 to 30% in 3 months as risk aversion triggered rapid unwinding. In commodities, carry (roll yield) is a significant component of total futures return. A commodity index investor who ignores carry may hold deeply contangoed contracts (e.g., VIX futures) that bleed value from negative roll yield. Systematic commodity funds actively sort markets by carry, overweighting backwardated contracts and underweighting or shorting contangoed ones. The interaction between FX carry and commodity carry creates powerful cross-asset signals: commodity exporters (AUD, CAD, NOK) tend to have both high rates and backwardated commodity curves, creating reinforcing carry signals.

## Concrete example
A systematic macro fund constructs a cross-asset carry portfolio. In FX, it goes long the 3 highest-yielding G10 currencies (AUD at 4.35%, NZD at 5.50%, NOK at 4.50%) and short the 3 lowest-yielding (JPY at 0.10%, CHF at 1.50%, EUR at 3.75%), equal-risk-weighted. In commodities, it goes long the 3 most backwardated markets (WTI crude: 0.8% monthly roll yield, copper: 0.3%, live cattle: 0.5%) and short the 3 most contangoed (natural gas: -1.2%, corn: -0.4%, gold: -0.2%). In the first year, the portfolio earns 7.2% (3.8% from FX carry, 3.4% from commodity carry) with 8% annualized volatility, a Sharpe ratio of 0.9. In the second year, a global risk-off event triggers simultaneous unwinding: AUD drops 12%, crude oil falls 25%, and the portfolio loses 15% in 6 weeks. The lesson: carry returns are compensation for crash risk, and carry strategies must be sized and hedged accordingly.

## Key mechanics and formulas
- **FX carry**: Carry = interest rate(long currency) - interest rate(short currency); alternatively, Carry = forward discount = (forward rate - spot rate) / spot rate
- **Commodity carry (roll yield)**: Roll yield = (near-month futures price - next-month futures price) / near-month futures price; positive = backwardation = positive carry
- **Bond carry**: Carry = bond yield - funding rate (repo or short-term rate); for a 10 year bond at 4.5% funded at 3%, carry = 1.5% annualized
- **Carry portfolio construction**: rank all assets by carry; go long top quintile, short bottom quintile; equal-risk-weight within each leg
- **Sharpe ratio of carry (historical)**: FX carry Sharpe approximately 0.5 to 0.8; commodity carry Sharpe approximately 0.3 to 0.6; combined cross-asset carry Sharpe approximately 0.7 to 1.0
- **Carry-to-risk ratio**: a measure of whether carry compensation is sufficient for the volatility borne; Carry-to-risk = annualized carry / annualized volatility

## Prerequisites
- [[Interest Rate Differential]]
- [[Roll Yield]]
- [[Forward Rate]]
- [[Backwardation]]
- [[Contango]]

## Related concepts (learn next)
- [[Momentum Cross Asset]]: momentum and carry are partially offsetting factors; combining them improves portfolio Sharpe.
- [[Value Cross Asset]]: value signals (e.g., PPP in FX) can be used to filter carry trades, avoiding pairs where carry is offset by overvaluation.
- [[Risk Parity]]: risk parity frameworks incorporate carry as the primary expected return source across asset classes.
- [[CTA]]: many CTAs blend carry with trend-following to form hybrid strategies.
- [[Macro Regime]]: carry trades perform best in "Goldilocks" regimes (moderate growth, low volatility) and worst in risk-off episodes.
- [[Correlation Breakdown]]: carry trade unwinds are a primary driver of cross-asset correlation spikes.
- [[Positioning Signal]]: extreme carry trade positioning (e.g., record JPY shorts) signals elevated crash risk.
- [[DXY Correlation]]: a strong USD environment often coincides with carry unwinds in EM currencies.

## Common misconceptions
1. **"Carry is free money"**: Carry returns compensate for crash risk. The average annual carry return is approximately 4 to 6%, but the worst drawdowns exceed 20%. Risk-adjusted, carry is a modest premium, not an arbitrage.
2. **"Covered interest parity means FX carry should not exist"**: Covered interest parity holds for hedged positions, but the FX carry trade is unhedged. The carry premium compensates for the risk of adverse exchange rate moves. The persistence of carry returns is a violation of uncovered interest parity, which is an empirical puzzle, not a theoretical guarantee.
3. **"Commodity carry and FX carry are independent"**: They are correlated because commodity-exporting countries (Australia, Canada, Norway) tend to have higher interest rates when commodity prices are high and curves are backwardated. This creates a hidden correlation that amplifies drawdowns in combined carry portfolios.

## Sources
- Koijen, Ralph, Moskowitz, Tobias, Pedersen, Lasse, Vrugt, Evert, "Carry," Journal of Financial Economics (2018)
- Brunnermeier, Markus, Nagel, Stefan, Pedersen, Lasse, "Carry Trades and Currency Crashes," NBER (2008)
- Erb, Claude, Harvey, Campbell, "The Strategic and Tactical Value of Commodity Futures," Financial Analysts Journal (2006)
- Asness, Clifford, Moskowitz, Tobias, Pedersen, Lasse, "Value and Momentum Everywhere," Journal of Finance (2013)
