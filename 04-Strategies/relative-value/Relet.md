---
aliases: [relet, reletting, tc in voyage out, charter in employ out]
tags:
  - "#freight/contracts"
date-added: "2026-06-17"
---

# Relet

## Definition
Relet is renting a ship from its owner at a fixed daily cost, then putting that ship to work yourself to capture the difference between what you pay and what you earn. You do not own the vessel. You control it for a period under a [[Time Charter]] (TC), paying a fixed hire per day, and you take on the job of finding it cargo. There are two ways to employ it out. Pure relet means you sublet the identical vessel to another party on a time charter and pocket the hire spread, which is the definition used in [[TC In and TC Out]]. The variant a freight desk runs most is "TC in, voyage out", where you keep operating control and fix the ship on spot [[Voyage Charter|voyages]], earning the voyage market expressed as a [[Time Charter Equivalent|TCE]]. Your margin per day is the voyage TCE minus the TC in hire, and you are structurally long freight duration for the length of the charter.

## Why it matters (commodities and FX)
Relet is the core operator position on a physical freight desk. It is how a charterer with a view that rates will firm takes that view with a real ship instead of, or alongside, paper. When you TC in a vessel and run it on voyages, you convert a fixed cost (hire) into a variable revenue stream (the spot voyage market), so the position is a directional bet on freight: you profit if the spot market firms above your locked hire and you bleed if it falls below. It shows up in real decisions constantly: whether to fix a relet vessel out fast on the next available cargo or hold for a better route, whether to ballast her to a stronger loading region, how to cover the embedded [[Bunker Risk]] since under a TC in the bunkers are your cost, and how to size the position against the [[Forward Freight Agreement|FFA]] curve. The relet is also how operators monetize information edge: knowing a cargo is coming, knowing a region is short of tonnage, knowing a [[Baltic Route Codes|route]] is mispriced. Paper cannot capture that operational alpha; a physical ship can.

## Concrete example
**Concrete:** A desk has a constructive view on Atlantic Supramax rates for the second half of the year. It TCs in a 58,000 dwt Supramax for 6 months at 12,000 USD/day, delivery Continent, redelivery worldwide. Under the TC in, the desk pays the 12,000/day hire and pays for bunkers; the owner covers OPEX and crew. The desk then employs her out on a string of [[Voyage Charter|voyage charters]] (grains, coal, fertilizers) and, after netting voyage costs (bunkers, port, canal, address commissions) against gross freight, the voyages produce an average [[Time Charter Equivalent|TCE]] of 16,000 USD/day. Margin per day = 16,000 - 12,000 = 4,000 USD/day. Across roughly 180 days of the period, gross spread is about 4,000 * 180 = 720,000 USD, before brokerage commission (often around 1.25 percent on hire and 2.5 to 3.75 percent on voyage freight) and before any idle or ballast days where the ship earns no freight but still owes hire. Net, the desk might keep 550,000 to 650,000 USD if utilization is high.

Now the failure case. The market sags instead of firming. Voyage TCE drops to 9,000 USD/day while the desk still owes 12,000/day hire. Margin per day = 9,000 - 12,000 = -3,000 USD/day. If the ship is fully employed at that level she bleeds about 3,000 * 180 = 540,000 USD over the period. It is usually worse than that: in a soft market cargoes are scarce, so the desk eats unproductive [[Ballast Leg Economics|ballast legs]] and idle waiting days where TCE is effectively zero or negative but the 12,000/day hire keeps running. A few weeks of idleness can add 200,000 to 300,000 USD of pure carry loss on top. The desk is long duration and cannot walk away: the TC in obligation runs to redelivery.

**Simplified:** You rent a ship for 6 months at 12,000 a day. You find it cargo and the trips pay you the equivalent of 16,000 a day, so you make about 4,000 a day, roughly 720,000 over the period before costs. But if freight falls and the trips only pay 9,000 a day, you lose 3,000 a day, and worse if the ship sits empty while you still pay the rent. You rented the ship, you did not buy it, and you cannot hand the rent back early.

## Key mechanics and formulas
- `margin_per_day = voyage_TCE - tc_in_hire` where `voyage_TCE` is the spot voyage employment converted to a USD/day figure and `tc_in_hire` is the fixed daily hire you pay the owner.
- `voyage_TCE = (gross_freight_revenue - voyage_costs) / round_trip_days` where `voyage_costs` are bunkers, port charges, canal dues, and commissions. Note: OPEX and crew are NOT subtracted because under a TC in the owner carries those; TCE is gross of vessel running cost. See [[Time Charter Equivalent]].
- `period_pnl = sum over employed days of (voyage_TCE - tc_in_hire) - commissions - idle_and_ballast_cost` where `idle_and_ballast_cost` captures days the ship earns no freight (or negative TCE on a ballast leg) while hire still accrues.
- Directional sign: the relet is long freight. `d(period_pnl)/d(market) > 0`. Rising spot TCE widens margin; falling spot TCE compresses or inverts it.
- Bunker exposure: under a TC in, fuel is your cost, so `voyage_TCE` already nets bunkers and the position carries [[Bunker Risk]] separate from the freight rate view.

## Prerequisites
[[Time Charter]]
[[Voyage Charter]]
[[TC In and TC Out]]
[[Time Charter Equivalent]]

## Related concepts (learn next)
- [[Forward Freight Agreement]] — the synthetic paper alternative to a relet: a long FFA expresses the same bullish freight view with no operational duties and no operational alpha.
- [[Physical vs Paper Freight]] — frames the choice between renting a real ship (relet) and taking a paper position, and which risks attach to each.
- [[Market Hire]] — the prevailing TC rate you benchmark your locked in TC in hire against to judge whether the relet entry is cheap or rich.
- [[Freight Rate Risk]] — the open market exposure on the out leg; the relet is one concrete way to express and bear it.
- [[Bunker Risk]] — under a TC in you pay fuel, so the relet bundles a fuel price exposure inside the freight bet.
- [[Ballast Leg Economics]] — quantifies the unproductive repositioning legs that erode relet margin in a soft market.
- [[Baltic Route Codes]] — the standardized routes whose published rates you watch to decide where and how to fix the relet vessel out.
- [[TC In and TC Out]] — the parent concept distinguishing pure relet (TC out the identical vessel) from the TC in/voyage out operation covered here.

## Common misconceptions
- "Relet is risk free arbitrage." Wrong. Only the in leg is fixed. The out leg is open market exposure: voyage TCE floats with the spot market, so the spread can invert and the position can lose money for the full duration you cannot exit.
- "Relet means you own the ship." Wrong. You rent it under a time charter. You hold operational control for the period but the owner holds title, carries OPEX and crew, and takes the ship back at redelivery.
- "A relet and an FFA are interchangeable." Wrong. The FFA is cash settled paper with no operational duties. The relet is a physical position that also carries off hire, port congestion, idle days, and bunker exposure, none of which exist in the paper instrument. They share a freight direction but not a risk profile.
- "Reletting requires a different vessel." Wrong. Pure relet is the same vessel subletted out on a TC. The "different employment" is the cargo or the sub charterer, not a different ship.

## Sources
- Alizadeh and Nomikos, Shipping Derivatives and Risk Management — TCE conversion, freight rate exposure, physical versus derivative freight positions.
- Stopford, Maritime Economics, 3rd ed. — charter types, the relet operator role, and freight market cycles.
- Kavussanos and Visvikis, The International Handbook of Shipping Finance — chartering structures and operator economics.
- Baltic Exchange route and index guides — route definitions and TCE assessment methodology used to mark voyage employment.
- Clarksons Shipping Intelligence Network (SIN) — period hire and spot rate references for Supramax and other dry segments.
- Ship and Bunker — bunker price references underpinning the fuel cost component of voyage TCE.
