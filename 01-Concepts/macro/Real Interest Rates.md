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

Real interest rates are nominal interest rates adjusted for inflation. They represent the true cost of borrowing or true return on saving after accounting for purchasing power erosion. The most commonly traded expression is the US 10 year TIPS (Treasury Inflation Protected Securities) yield, which directly quotes the real yield on US government debt. Real rates are the single most important macro variable for cross asset allocation because they set the opportunity cost of holding non yielding assets like [[Gold Futures|gold]] and the discount rate applied to all future cash flows.

## Why it matters (commodities and FX)

Real rates are the dominant driver of [[Gold Futures|gold]]. Gold produces no income, so its opportunity cost is the real return available on safe assets (TIPS). When real rates are negative (inflation exceeds nominal yields), gold has zero or positive relative carry compared to bonds. When real rates are positive and rising, gold faces a headwind because bonds offer a real return gold cannot.

For FX, real rate differentials drive capital flows and exchange rates. A country with higher real rates attracts capital, strengthening its currency. This is the real rate version of the [[Carry Trade]]: real rate differentials matter more than nominal, after adjusting for inflation expectations.

For commodities broadly, real rates affect [[Cost of Carry]] (the "r" in the carry formula) and the discount rate on future production investment, influencing supply decisions.

## Concrete example

**Concrete:** US 10 year nominal yield 4.5%. US 10 year breakeven inflation 2.3%. US 10 year real yield (TIPS) 2.2%. From 2020 to 2021, the 10 year TIPS yield fell to -1.0%. Gold rallied from $1,500 to $2,070. From 2022 to 2023, the Fed hiked aggressively, pushing real yields to +2.5%. Gold initially fell to $1,620 (Oct 2022). Gold then rallied despite high real rates due to massive [[Central Bank Policy|central bank buying]] (China, India, Turkey), breaking the historical real rate/gold correlation. This is a [[Structural Break]] traders must recognize. In FX: US real rates rose above European real rates by ~200bp in 2022, driving EUR/USD from 1.15 to 0.96. The real rate differential explained the bulk of the move.

**Simplified:** Subtract expected inflation from the nominal interest rate. That is what your bond actually earns in purchasing power. When that number is negative, cash and bonds lose value, and gold (which earns nothing) looks attractive by comparison. When it goes positive, bonds beat gold on yield, so gold falls. Currencies follow the same logic: capital flows to wherever real yields are highest.

## Key mechanics and formulas

**Fisher equation (approximate):**
`Real Rate ≈ Nominal Rate - Expected Inflation`

**Fisher equation (exact):**
`(1 + Real Rate) = (1 + Nominal Rate) / (1 + Expected Inflation)`

**Breakeven inflation:**
`Breakeven = Nominal Treasury Yield - TIPS Yield`

The market's implied inflation expectation. If the 10Y UST yields 4.5% and the 10Y TIPS yields 2.2%, breakeven is 2.3%.

**Gold/real rate relationship (approximate):**
Historically, a 100bp rise in 10 year real yields was associated with a ~$100 to $150/oz decline in gold. Sensitivity weakened since 2022 due to central bank demand.

**Real rate differential (FX):**
`Real Rate Differential = (Nominal_A - Inflation_A) - (Nominal_B - Inflation_B)`

Positive differential favors currency A appreciation.

## Prerequisites
- [[Forward Curve]]
- [[Central Bank Policy]]
- [[Carry Trade]]

## Related concepts (learn next)
- [[Gold Futures]] - the asset most directly and inversely correlated with real rates. The foundation of gold trading.
- [[Safe Haven Assets]] - gold and US Treasuries are both safe havens, but they respond differently to real rate changes.
- [[Carry Trade]] - real rate differentials are a better predictor of FX carry returns than nominal differentials.
- [[Central Bank Policy]] - CBs set the nominal rate. Inflation expectations set the real rate. Both matter.
- [[Risk-On Risk-Off]] - real rates influence risk appetite. Very negative real rates = financial repression = capital into risk assets.
- [[Commodity Currencies]] - EM commodity currencies are sensitive to US real rates through capital flow effects.

## Common misconceptions

**"Nominal rates are what matter for gold."** No. Gold rallied 2019 to 2020 even as nominal rates fell, because inflation expectations rose faster, pushing real rates deeply negative. Real rates drive gold, not nominal.

**"Higher real rates are always bearish for commodities."** Higher real rates raise cost of carry and discount rate, bearish at the margin. But real rates often rise because the economy is strong, bullish for industrial demand. Net effect depends on which force dominates.

**"The TIPS yield is a clean measure of real rates."** TIPS have their own supply/demand dynamics (Fed QE buying, pension demand, breakeven trading). TIPS yields can diverge from "true" real rates, especially during QE or QT.

## Sources

- Federal Reserve FRED database: 10 year TIPS yield (series DGS10, DFII10)
- Piazzesi and Schneider, "Equilibrium Yield Curves" (2006)
- World Gold Council: "Gold and US Real Rates" research notes
- Ilmanen, Antti, "Expected Returns" (2011), Chapter on real returns
