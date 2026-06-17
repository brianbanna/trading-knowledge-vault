---
aliases: [market hire, hire rate, period rate, market hire rate, prevailing hire]
tags:
  - "#freight/contracts"
date-added: "2026-06-17"
---

# Market Hire

## Definition
Market hire is the going rate to rent a ship by the day, right now, for a given vessel class and period length. Think of it like the current market rent for an apartment of a certain size: if you signed a 2 year lease last year, your rent is fixed, but the market rent for an identical flat moves every month, and the gap between the two tells you whether your lease is a good deal today. In freight, market hire is the prevailing market clearing daily [[Time Charter]] rate you would have to pay (or could collect) to fix an equivalent ship for the equivalent tenor at this moment. It is distinct from your contracted hire, which is locked at the rate you agreed when you fixed. The difference between contracted hire and market hire is the mark to market on a period position. It is assessed from [[Baltic Exchange and the Dry Indices|Baltic]] period (time charter) assessments and live broker fixtures, and it carries the market's expectation of where spot will sit over the term, so it is the freight [[Forward Curve]] compressed into a single daily number.

## Why it matters (commodities and FX)
A freight desk does not just track cash settled. It marks every open period position to market every day, and market hire is the reference price it marks against. If you hold a TC in position (you rented a ship for a term), you are long duration: a rise in market hire makes your fixed rate deal look cheap and prints positive unrealized P&L. If you hold a TC out position (you let a ship out for a term), you are short duration and the sign flips. See [[TC In and TC Out]] for the two sides. Without a market hire mark you cannot size risk, report daily P&L, or decide whether to [[Relet]] a chartered ship back into a stronger market. Market hire is also the cleanest read on the period segment of the [[Forward Curve]]: when the 1 year TC rate sits well above spot, the market is pricing a recovery; when it sits below, it is pricing decline. That single number feeds hedge ratios against [[Forward Freight Agreement]] positions and informs whether to fix long now or stay in spot.

## Concrete example
**Concrete:** On day 0 you TC in a Panamax (about 82,000 dwt) at 15,000 USD/day for 12 months (360 days). You are the charterer, so you pay bunkers and run the ship for trading; you are long 360 days of duration at a locked 15,000. Two months in (60 days elapsed, 300 days remaining), the Baltic Panamax period assessment for the matching residual tenor has risen to 22,000 USD/day. Your mark to market per day is `mtm_per_day = market_hire - contracted_hire = 22,000 - 15,000 = +7,000 USD/day`. Position MTM is `7,000 * 300 = +2.1m USD` unrealized. You could in principle [[Relet]] the ship out at roughly 22,000 and crystallize the spread, subject to brokerage and credit. Now the failure case: instead, market hire for the residual falls to 9,000 USD/day. Your per day mark is `9,000 - 15,000 = -6,000 USD/day`, and position MTM is `-6,000 * 300 = -1.8m USD`, a large negative mark before a single dollar of hire has actually changed hands beyond the daily payments you owe regardless. The owner who chartered the ship to you holds the symmetric +1.8m. Nothing about your cash obligation changed; the mark reflects that you are now locked into paying above market.

**Simplified:** You agreed to rent a ship for a year at 15,000 a day. Two months later the same ship rents for 22,000 a day, so your deal is 7,000 a day cheap and you are up about 2.1m on paper for the rest of the term. If instead the rate had dropped to 9,000, you would be locked into paying 6,000 a day too much and showing a 1.8m paper loss. The rent you pay never changed; the market moved around your fixed price.

## Key mechanics and formulas
- `mtm_per_day = market_hire - contracted_hire` where `market_hire` is the prevailing daily TC rate for the matching class and residual tenor, and `contracted_hire` is your locked daily rate. Sign convention: a TC in (long duration) gains when `mtm_per_day > 0`; a TC out (short duration) has the opposite sign, so for a short you negate, `short_mtm_per_day = contracted_hire - market_hire`.
- `position_mtm = mtm_per_day * remaining_days` where `remaining_days` is the number of days left on the charter from the valuation date. Use the residual tenor, not the original tenor.
- To compare the spot voyage market against market hire, first convert voyages to a daily figure: `TCE = (gross_freight_revenue - voyage_costs) / round_trip_days`, where `voyage_costs` are bunkers plus port plus canal plus commissions and OPEX/crew are NOT subtracted. See [[Time Charter Equivalent]]. Market hire is already USD per day, so the comparison is `TCE vs market_hire`, both gross of vessel running cost.
- Matching tenor matters: a 12 month period rate and a 6 month period rate are different points on the curve and will not generally be equal even on the same day.

## Prerequisites
- [[Time Charter]]
- [[Freight]]
- [[Time Charter Equivalent]]

## Related concepts (learn next)
- [[TC In and TC Out]] explains the long versus short duration sides that market hire is marked against.
- [[Relet]] is how a charterer monetizes a favorable gap between contracted hire and market hire by re letting the ship.
- [[Forward Freight Agreement]] is the paper instrument whose period curve closely tracks market hire and lets you hedge the mark.
- [[Forward Curve]] is the full term structure that market hire summarizes into one number for a given tenor.
- [[Baltic Exchange and the Dry Indices]] publishes the period TC assessments that desks use as the market hire reference.
- [[Freight Rate Risk]] is the exposure that a market hire mark quantifies for an open period book.
- [[Mark to Market]] is the general valuation discipline that produces the unrealized P&L from a market hire reference.
- [[Backwardation]] explains why a period rate can sit below spot, a structure you read directly off market hire versus current spot.

## Common misconceptions
- "Market hire is my contracted hire." Wrong. Your rate is fixed at the moment you fix; market hire moves every day with supply, demand, and sentiment. The whole point of the mark is the gap between the two, and if they were equal there would be no MTM.
- "Market hire is the spot voyage rate." Wrong, and the error is a unit mismatch. Voyage rates are USD per tonne with the owner paying bunkers; market hire is USD per day with the charterer paying bunkers. You must convert the voyage to a [[Time Charter Equivalent|TCE]] before any comparison, otherwise you are comparing incompatible numbers.
- "The period rate is just an average of recent spot." Wrong. The period rate is forward looking: it embeds the market's expectation of where spot will sit over the whole term. In [[Contango]] it can sit well above current spot, in [[Backwardation]] well below. Treating it as a trailing average ignores the expectation it actually prices.
- "If market hire moves, I owe or receive cash immediately." Wrong. The mark is unrealized. Your daily hire obligation is unchanged; the MTM only becomes cash if you close, relet, or settle the position. Confusing the mark with a cash call leads to mismanaged liquidity.

## Sources
- Baltic Exchange, period (time charter) trip and period assessment methodology and daily fixture reports.
- Stopford, Maritime Economics, 3rd ed., chapters on the time charter market and freight rate formation.
- Alizadeh and Nomikos, Shipping Derivatives and Risk Management, sections on time charter rates, the term structure of freight, and mark to market valuation.
- Kavussanos and Visvikis, The International Handbook of Shipping Finance, chapters on freight derivatives and risk management.
- Clarksons Shipping Intelligence Network (SIN), period TC rate series by vessel class.
