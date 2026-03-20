---
aliases: [real rates, real interest rates, real yields, TIPS yield]
tags:
  - "#macro"
  - "#rates/govies/ust"
  - "#metals/precious/gold"
date-added: "2026-03-20"
---

# Real Interest Rates

## Definition

Real interest rates are nominal interest rates adjusted for inflation. They represent the true cost of borrowing or the true return on saving after accounting for the erosion of purchasing power. The most commonly traded expression is the US 10 year TIPS (Treasury Inflation Protected Securities) yield, which directly quotes the real yield on US government debt. Real rates are the single most important macro variable for cross asset allocation because they determine the opportunity cost of holding non yielding assets like [[Gold Futures|gold]] and affect the discount rate applied to all future cash flows.

## Why it matters (commodities and FX)

Real rates are the dominant driver of [[Gold Futures|gold]] prices. Gold produces no income, so its opportunity cost is the real return available on safe assets (TIPS). When real rates are negative (inflation exceeds nominal yields), holding gold has zero or positive relative carry compared to bonds. When real rates are positive and rising, gold faces a headwind because bonds offer a real return that gold cannot.

For FX, real rate differentials between countries drive capital flows and exchange rates. A country with higher real rates attracts capital, strengthening its currency. This is the real rate version of the [[Carry Trade]]: what matters is not nominal rate differentials but real rate differentials after adjusting for inflation expectations.

For commodities broadly, real rates affect the [[Cost of Carry]] (the "r" in the carry formula) and the discount rate applied to future production investment, influencing supply decisions.

## Concrete example

US 10 year nominal yield: 4.5%. US 10 year breakeven inflation: 2.3%. US 10 year real yield (TIPS): 2.2%.

From 2020 to 2021, the 10 year TIPS yield fell to negative 1.0%. Gold rallied from $1,500 to $2,070. From 2022 to 2023, the Fed hiked aggressively, pushing real yields to +2.5%. Gold initially fell to $1,620 (Oct 2022). However, gold subsequently rallied despite high real rates due to massive [[Central Bank Policy|central bank buying]] (China, India, Turkey), breaking the historical real rate/gold correlation. This is a [[Structural Break]] in the relationship that traders must recognize.

In FX: US real rates rose above European real rates by ~200bp in 2022, driving EUR/USD from 1.15 to 0.96. The real rate differential explained the bulk of the move.

## Key mechanics and formulas

**Fisher equation (approximate):**
`Real Rate ≈ Nominal Rate - Expected Inflation`

**Fisher equation (exact):**
`(1 + Real Rate) = (1 + Nominal Rate) / (1 + Expected Inflation)`

**Breakeven inflation:**
`Breakeven = Nominal Treasury Yield - TIPS Yield`

The market's implied inflation expectation. If the 10Y UST yields 4.5% and the 10Y TIPS yields 2.2%, breakeven inflation is 2.3%.

**Gold/real rate relationship (approximate):**
Historically, a 100bp increase in 10 year real yields has been associated with a ~$100 to $150/oz decline in gold. This sensitivity (the "beta") has weakened since 2022 due to central bank demand.

**Real rate differential (FX):**
`Real Rate Differential = (Nominal_A - Inflation_A) - (Nominal_B - Inflation_B)`

Positive differential favors currency A appreciation.

## Prerequisites
- [[Forward Curve]]
- [[Central Bank Policy]]
- [[Carry Trade]]

## Related concepts (learn next)
- [[Gold Futures]] - the asset most directly and inversely correlated with real rates. Understanding this relationship is the foundation of gold trading.
- [[Safe Haven Assets]] - gold and US Treasuries are both safe havens, but they respond differently to real rate changes.
- [[Carry Trade]] - real rate differentials are a better predictor of FX carry returns than nominal rate differentials.
- [[Central Bank Policy]] - central banks set the nominal rate. Inflation expectations set the real rate. Both matter.
- [[Risk-On Risk-Off]] - real rates influence risk appetite. Very negative real rates = financial repression = pushes capital into risk assets.
- [[Commodity Currencies]] - EM commodity currencies are sensitive to US real rates through capital flow effects (higher US real rates attract capital away from EM).

## Common misconceptions

**"Nominal rates are what matter for gold."** No. Gold rallied from 2019 to 2020 even as nominal rates fell, because inflation expectations rose faster, pushing real rates deeply negative. It is real rates, not nominal, that drive gold.

**"Higher real rates are always bearish for commodities."** Higher real rates increase the cost of carry and discount rate, which is bearish at the margin. But real rates often rise because the economy is strong, which is bullish for industrial commodity demand. The net effect depends on which force dominates.

**"The TIPS yield is a clean measure of real rates."** TIPS have their own supply/demand dynamics (Fed QE buying, pension fund demand, TIPS breakeven trading). The TIPS yield can diverge from "true" real rates, especially during periods of QE or QT.

## Sources

- Federal Reserve FRED database: 10 year TIPS yield (series DGS10, DFII10)
- Piazzesi and Schneider, "Equilibrium Yield Curves" (2006)
- World Gold Council: "Gold and US Real Rates" research notes
- Ilmanen, Antti, "Expected Returns" (2011), Chapter on real returns
