---
aliases: [2s10s, 2s10s spread, yield curve slope, curve steepness, 10Y minus 2Y]
tags:
  - "#rates"
  - "#macro"
date-added: "2026-07-03"
---

# Yield Curve Slope

## Definition

The yield curve slope measures the difference in yield between a long maturity government bond and a short maturity one. The most watched version is the 2s10s: the [[US 10Y Treasury|10Y yield]] minus the [[US 2Y Treasury|2Y yield]]. In plain terms, it tells you whether lending to the government for longer pays more or less than lending for shorter, and that gap encodes the market's read on growth, inflation, and [[Central Bank Policy]]. Precisely, a positive (upward sloping) curve means long yields exceed short yields, the normal state where investors demand term premium for duration. A negative slope, called inversion, means short yields exceed long yields, which historically leads recessions. On 2026-07-02 the 2s10s was 35 bps (10Y at 4.485% minus 2Y at 4.170% on 2026-07-01), up 12.90% on the day, the single biggest mover on the tape, a bull steepening after soft US jobs data as the front end priced [[Central Bank Policy|Fed]] cuts faster than the long end.

## Why it matters (commodities and FX)

The curve slope is the market's cleanest business cycle indicator, and it drives cross asset positioning. An inverted 2s10s (negative slope) has preceded every US recession in the modern era, typically by 12 to 18 months, so a deep inversion is a warning that tilts a macro book toward [[Safe Haven Assets|defensive]] positioning. For a commodity trader, the slope reads the growth and policy cycle that governs industrial demand: bull steepening on soft data signals a slowing economy and easing ahead, which is mixed for cyclicals but supportive for [[Gold Futures|gold]] through falling [[Real Interest Rates|real rates]]. For an FX trader, the slope reflects where in the cycle the central bank sits, and rapid front end moves that steepen or flatten the curve map directly onto [[DXY]] and [[EUR/USD]] through the [[US 2Y Treasury|2Y]] rate differential. The slope is also a [[Regime Shift|regime]] signal: the transition from inversion to re steepening (bull steepening as cuts arrive) has historically coincided with the onset of recession and [[Risk-On Risk-Off|risk off]] episodes, not the all clear many assume.

## Concrete example

**Concrete:** Non Farm Payrolls Friday. The 2s10s is at 31 bps going in, with the [[US 2Y Treasury|2Y]] at 4.31% and the [[US 10Y Treasury|10Y]] at 4.62%. Payrolls miss hard, 60k versus 180k expected. The market prices faster [[Central Bank Policy|Fed]] cuts. The front end reacts most: the 2Y yield falls 14 bps to 4.17% while the 10Y falls only 2 bps to 4.60%, because the long end holds up as cuts support future growth. The result is a bull steepening: the 2s10s widens from 31 bps to about 43 bps, and on the tape prints 35 bps intraday, up 12.90% on the session. A desk positioned for steepening (long ZT, short ZN in duration weighted size) profits because the front end rallied more than the back end. The win case: a curve steepener into a dovish labor surprise. The fail case: had payrolls printed hot at 300k, the market would have removed cuts, the 2Y would have jumped more than the 10Y, the curve would have bear flattened back toward inversion, and the same steepener would have lost money as the spread compressed.

**Simplified:** The yield curve slope is the long rate minus the short rate, usually the 10Y minus the 2Y. When it is positive, longer loans pay more, which is normal. When it goes negative (inverted), short loans pay more than long ones, which is the market saying it expects rate cuts and a slowdown; inversion has warned of recessions for decades. The slope moves in four ways depending on which end moves and which direction. Watch it because it packs the whole growth and policy story into one number.

## Key mechanics and formulas

**2s10s slope:**
`Slope = 10Y Yield - 2Y Yield`

Positive means upward sloping (normal). Negative means inverted (recession warning). Measured in basis points.

**The four regimes** (defined by which end drives the move and the direction of rates):

- **Bull steepening:** short yields fall faster than long yields (curve steepens, rates falling). Driven by the front end pricing cuts. Typical when soft data forces [[Central Bank Policy|the Fed]] dovish. This is the 2026-07-02 case.
- **Bear steepening:** long yields rise faster than short yields (curve steepens, rates rising). Driven by the back end pricing higher inflation, term premium, or heavy supply.
- **Bull flattening:** long yields fall faster than short yields (curve flattens, rates falling). Driven by the back end rallying on growth fear or a flight to duration.
- **Bull vs bear names the direction of bond prices** (bull = prices up, yields down; bear = prices down, yields up); **steepening vs flattening names the change in the spread.**
- **Bear flattening:** short yields rise faster than long yields (curve flattens, rates rising). Driven by the front end pricing hikes; this is the path that leads into inversion.

**Inversion as a lead indicator:**
An inverted 2s10s (negative slope) has preceded every US recession since the 1970s, typically by 12 to 18 months. The signal fires on inversion, but the recession often arrives as the curve re steepens (bull steepening) once cuts begin.

## Prerequisites
- [[US 2Y Treasury]]
- [[US 10Y Treasury]]
- [[Central Bank Policy]]

## Related concepts (learn next)
- [[US 2Y Treasury]] - the short leg, dominated by policy expectations.
- [[US 10Y Treasury]] - the long leg, dominated by growth, inflation, and term premium.
- [[Central Bank Policy]] - the front end moves on the policy path, so the curve is a policy read.
- [[Real Interest Rates]] - the slope and real rates jointly describe the macro backdrop for gold and risk.
- [[Macro Regime]] - the four slope regimes are a component of the broader macro regime map.
- [[Risk-On Risk-Off]] - re steepening from inversion has historically coincided with risk off.
- [[Regime Shift]] - a decisive change in the curve's direction often flags a regime shift.

## Common misconceptions

**"A steepening curve is always good news."** No. Bull steepening driven by the front end pricing cuts often signals an imminent slowdown, not recovery. The context (which end moved and why) matters more than the direction of the spread.

**"Inversion means a recession is here."** No. Inversion is a lead indicator, typically 12 to 18 months ahead. The recession often arrives after the curve re steepens, not while it is inverted.

**"The 2s10s is the only curve that matters."** The 3m10s and the near term forward spread (18m3m) are also watched and sometimes lead the 2s10s. Different curves emphasize different horizons of the policy path.

## Sources

- Federal Reserve FRED database: 2s10s series T10Y2Y, DGS10, DGS2
- Estrella and Mishkin, "The Yield Curve as a Predictor of US Recessions" (1996)
- Federal Reserve Bank of San Francisco, Bauer and Mertens on the near term forward spread (2018)
- Ilmanen, Antti, "Expected Returns" (2011), chapters on bond risk premia
