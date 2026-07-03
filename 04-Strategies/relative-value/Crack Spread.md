---
aliases: [crack spread, refinery spread, refining margin, 3-2-1 crack, 3:2:1 crack]
tags:
  - "#energy/crude"
  - "#energy/refined"
date-added: "2026-03-20"
---

# Crack Spread

## Definition
The crack spread is a refiner's gross margin expressed in the paper market: the value of the refined products made minus the cost of the crude bought. Crude is useless as crude, nobody burns it in a car, so a [[Refinery Economics|refinery]] sorts and transforms it into products people actually buy, and the crack spread is the gap between what those products sell for and what the crude cost. The word "crack" comes from the cracking units that break heavy molecules into lighter ones. A refiner is structurally long this spread: it buys crude, sells products, and lives on the difference. It is not a directional bet on oil, it is a bet on the profitability of turning crude into product. It is one instance of a [[Process Margin]], the general shape of value of outputs minus cost of inputs earned by whoever does the conversion.

## Why it matters (commodities and FX)
Two distinct uses, and both pass the front office filter.

**Commercial (hedge).** The crack is the refiner's actual margin, so when it looks fat the refiner locks it in by selling the crack: sell product futures, buy crude futures. That freezes the margin regardless of where flat price goes. This is a physical operator protecting a real margin, not a structuring trade and not systematic alpha.

**Signal (demand tell).** The crack reads the health of the demand side of the crude barrel in real time. A wide crack means refiners run hard, pull more crude, product demand is strong or product supply is tight, bullish for crude demand. A narrow or negative crack means refiners cut runs, demand destruction or product oversupply, bearish, and often the early tell before crude flat price reacts. A crude trader who ignores cracks is trading blind on the demand side. Because refined product economics set the bunker bill through the [[Scrubber Spread]] (VLSFO minus HSFO), this feeds straight into freight vessel economics and TCE.

## How a refinery makes the barrel
Three stages, needed before the spread makes sense.

1. **Separation (distillation).** Heat crude in a tall column. Molecules boil at different temperatures and tap off at different heights. Top to bottom: gases and light naphtha (blends into gasoline), kerosene / jet, diesel and gasoil (the distillate cut), then heavy fuel oil and residue at the bottom. Pure sorting, no molecules changed.
2. **Conversion (cracking).** Raw crude yields too much heavy low value junk and not enough light high value product versus what the market wants. The fluid catalytic cracker (FCC), hydrocracker, and coker break heavy molecules into lighter ones. This is what lets a refiner make a barrel worth more than the sum distillation handed it, and where "crack" comes from.
3. **Treatment.** Strip sulfur to meet specs (hydrotreating). Low sulfur product sells at a premium, high sulfur is penalized or unsellable.

**Barrel yield.** 1 barrel = 42 US gallons. Rough US yield: gasoline 45 to 50%, distillate (diesel + jet + heating oil) 25 to 30%, fuel oil / residue / other the rest. The slate is flexible but constrained by refinery configuration (how much cracking kit) and crude quality. Light crude already holds more light molecules, sweet crude is low sulfur, so light sweet ([[Brent Crude|Brent]], [[WTI Crude Oil|WTI]]) commands a premium and heavy sour (Urals, Maya, Middle East grades) trades at a discount. That discount is the refiner's compensation for the extra processing, the [[Quality Spread]] you capture through [[API Gravity]] and [[Sweet vs Sour]]. A complex refinery with lots of cracking kit buys cheap heavy sour and still makes clean product, banking the quality spread as margin.

## Concrete example
**Concrete:** Illustrative flat prices. [[WTI Crude Oil|WTI]] = 80.00/bbl. [[RBOB Gasoline Futures|RBOB gasoline]] = 2.30/gal, so 2.30 × 42 = 96.60/bbl. [[ULSD Heating Oil Futures|ULSD diesel]] = 2.45/gal, so 2.45 × 42 = 102.90/bbl.

Single product cracks: gasoline crack = 96.60 − 80.00 = 16.60/bbl. Distillate crack = 102.90 − 80.00 = 22.90/bbl.

The 3:2:1 crack (3 barrels crude in, 2 gasoline out, 1 distillate out, matching a gasoline heavy US slate):
3:2:1 = (2 × 96.60 + 1 × 102.90 − 3 × 80.00) / 3 = (193.20 + 102.90 − 240.00) / 3 = 56.10 / 3 = **18.70/bbl** of crude processed.

Hedge, case it works: the refiner sees 18.70 and locks it by selling 2 RBOB and 1 ULSD, buying 3 WTI per 3 barrel unit. Crude flat price then collapses from 80 to 60. Products fall with it, but the short product legs gain as the long crude leg loses, so the margin stays frozen near 18.70. The refiner is insulated from flat price and keeps the margin it banked.

Hedge, case it fails: after locking at 18.70, cracks widen to 25 on a product supply shock. The refiner capped its own upside and left 6.30/bbl on the table (opportunity cost, not a cash loss). Worse, if it hedged same month crude against same month product while its real barrel is time lagged (crude bought and shipped weeks before product is sold), a mid period move whipsaws the hedge. And if the paper legs do not match the plant's true yield, residual [[Basis Risk]] leaks P&L.

**Simplified:** Crude costs one number, the gasoline and diesel you make from it sell for another. The crack is the gap, the refiner's profit per barrel. When that gap is wide the refiner locks it in by shorting products and buying crude, guaranteeing the margin no matter what oil does next.

## Gasoline versus distillate spread
Inside the barrel, gasoline and distillate answer to different demand, and the spread between them states which demand is dominant.

- **Gasoline (RBOB):** light vehicles, US centric, huge, seasonal. Peak demand is summer driving season, so gasoline cracks peak spring into summer.
- **Distillate (diesel / gasoil / heating oil):** the industrial economy fuel. Trucking, rail, shipping, farming, plus heating oil in winter. Diesel strength proxies goods movement and industrial activity. Heating oil peaks in Northern Hemisphere winter.

**Seasonal flip.** Summer: gasoline strong, distillate softer. Winter: gasoline weak (nobody road trips in January), distillate strong (heating plus trucking). So the [[Gasoline Crack]] versus [[Heating Crack]] spread swings seasonally, a classic seasonal spread trade. In the numbers above distillate is 6.30 over gasoline (102.90 − 96.60), a winter shaped configuration.

**Restoring force and where it dies.** Refiners tilt yield at the margin by adjusting cut points and cracker severity, so when one product's crack blows out they shift the slate toward it, pull more to market, and partially close the spread. That restoring force works only while refiners have room to switch. When configuration binds, both products tight at once and refiners already flat out, the spread cannot self correct through yield shifting and can run far past what looks reasonable. The 2022 to 2023 diesel blowout is the textbook case: goods economy roaring, refinery capacity permanently shut after COVID, Russian diesel sanctioned off the market. Distillate cracks went vertical while gasoline lagged, and yield switching could not close it because the binding constraint was total capacity, not slate mix.

**Driver dominance, not a law.** Whether gasoline sits over distillate or under it is a driver dominance statement. In a recession, industrial diesel demand craters while consumers still drive, so gasoline holds over diesel. In a goods boom or a diesel specific supply shock, distillate dominates. The sign of the spread tells you which economy, consumer or industrial, is in control.

## Key mechanics and formulas
- **Unit conversion (the trap that kills everyone).** Crude quotes in USD per barrel, US products (RBOB, ULSD) quote in USD per gallon. Convert products to per barrel by × 42 before subtracting.
- **Single product crack** = product price × 42 − crude price, in USD per barrel.
- **3:2:1 crack** = (2 × gasoline_bbl + 1 × distillate_bbl − 3 × crude) / 3, dividing by 3 to express margin per barrel of crude processed.
- **Other ratios:** 5:3:2 is closer to real US yields, 2:1:1 for a balanced slate. Europe and Asia are diesel heavy, so cracks there compute against [[Brent Crude|Brent]] with gasoil weighted more.
- **Hedge ratio:** to lock a 3:2:1 margin, per 3 crude barrels sell 2 gasoline and 1 distillate contract. Match contract sizes and calendar to the real barrel.

## Prerequisites
- [[Refinery Economics]]
- [[WTI Crude Oil]]
- [[RBOB Gasoline Futures]]
- [[ULSD Heating Oil Futures]]
- [[Relative Value Trade]]

## Related concepts (learn next)
- [[Process Margin]]: the general form (outputs minus inputs earned by the converter) that the crack spread is one instance of.
- [[Crush Spread]]: the soybean equivalent, beans to meal plus oil, the crusher's margin.
- [[Scrubber Spread]]: VLSFO minus HSFO, the bunker fuel version that ties refined product economics into the freight seat.
- [[Gasoline Crack]]: the single product gasoline margin, one leg of the gasoline versus distillate spread.
- [[Heating Crack]]: the single product distillate margin, the other leg and the winter side of the seasonal flip.
- [[Quality Spread]]: why heavy sour crude trades at a discount, the margin a complex refiner captures.
- [[Sweet vs Sour]]: the sulfur driven crude quality split that sets processing cost and yield.
- [[Calendar Spread]]: the time structure a refiner also trades, since the real barrel is a lagged, not same month, exposure.
- [[Seasonality]]: the demand calendar driving gasoline in summer and distillate in winter.

## Common misconceptions
1. **The paper crack is a specific refiner's margin.** It is a margin proxy, not any one plant's true margin. Real refiners sell product at location specific prices with a physical premium, and 3:2:1 is a fixed ratio simplification while real yields vary by crude and refinery.
2. **The timing is same month.** Crude is bought weeks before product is sold (buy, ship, process, then sell), so the refiner's real exposure is a time lagged crack, front month crude against deferred product. Hedging the same month crack is a real calendar error.
3. **3:2:1 captures the whole barrel.** It usually ignores the fuel oil and residue at the bottom, which can trade below crude and drag the true margin under the paper number. A strong 3:2:1 can sit on top of a negative all products netback.
4. **A wide crack always means run harder.** Only if the marginal barrel is profitable across the full slate. If the residue cut is deep negative or the crude slate yields too much of it, running harder makes more money losing product even with a strong gasoline crack.

## Sources
- CME Group. *Crack Spread Handbook* and refined products contract specs (RBOB, ULSD, WTI).
- EIA. *Refinery yield and utilization data*, weekly petroleum status report.
- Fattouh, Bassam. *An Anatomy of the Crude Oil Pricing System*, Oxford Institute for Energy Studies.
- Leffler, William. *Petroleum Refining in Nontechnical Language*.

---
*Status: full note | Last reviewed: 2026-07-03*
