---
aliases: [ballast leg, ballast voyage, ballast bonus, repositioning leg, empty leg]
tags:
  - "#freight/dry"
date-added: "2026-06-09"
---

# Ballast Leg Economics

## Definition
A cargo ship only earns money when it carries cargo, but it cannot teleport to where the next cargo waits. The ballast leg is the trip the ship sails empty, filled only with seawater ballast for stability, to reposition from where it discharged to where it next loads. During that empty leg the ship burns fuel and consumes calendar days while earning zero freight. Ballast leg economics is the practice of pricing that unpaid repositioning into the freight the owner quotes for the paying laden leg, because the round trip, not the laden leg alone, is what actually pays the ship. In technical terms it is the cost allocation that converts a one way [[Freight]] rate into a realistic round voyage [[Time Charter]] equivalent.

## Why it matters (commodities and FX)
A freight trader who reads only the laden leg rate will systematically overstate vessel earnings and misprice [[Voyage Charter]] fixtures. Every dry bulk and tanker fixture sits inside a round trip, and the days and bunkers spent ballasting back to the next load zone are real costs that compress realised earnings below the headline rate. The owner who quotes a voyage must recover the ballast leg or lose money; the charterer who pays it wants to verify the owner is not double counting it. Ballast positioning also drives where vessels cluster, so it feeds directly into regional rate spreads, [[Baltic Route Codes]] differentials, and the [[Forward Freight Agreement]] curve. Triangulation, the art of chaining cargoes so the ship rarely sails empty, is the single largest lever an operator has on annual return, which makes ballast economics central to fleet level profit and loss.

## Concrete example
**Concrete:** A [[Vessel Classes and Deadweight Tonnage|Capesize]] of 180,000 dwt fixes the C3 route, Tubarao Brazil to Qingdao China, at a freight rate of 22 USD per tonne on a 170,000 tonne iron ore stem, grossing 3,740,000 USD. The laden leg runs 11,000 nautical miles at 12 knots, roughly 38 days. After Qingdao discharge there is no Pacific cargo back to Brazil, so the ship ballasts empty around the Cape of Good Hope back to Tubarao, another 11,000 miles and 38 days. Laden bunker burn is about 62 tonnes per day of [[Bunkers, IFO versus MGO, and the Bunker Hedge|VLSFO]] at 600 USD per tonne, ballast burn about 50 tonnes per day. Total bunker cost is roughly 38 days times 62 times 600 plus 38 days times 50 times 600, near 2,550,000 USD. Add port costs of about 250,000 USD. Net voyage revenue is 3,740,000 minus 2,800,000, near 940,000 USD over 76 total days, so the round voyage [[Time Charter|TCE]] is about 12,400 USD per day. If you had judged the fixture on the laden leg alone, 38 days, you would have computed near 24,700 USD per day, double the truth. If the round voyage TCE of 12,400 beats the prevailing [[TC In and TC Out|TC]] rate the owner trades the voyage and wins; if Capesize TC was fixing at 18,000 per day, the owner who ignored the ballast leg fixes this voyage, loses 5,600 USD per day versus chartering out, and the fixture fails on a relative basis.
**Simplified:** The ship gets paid to sail loaded one way but must crawl back empty for free. Spread the one paying trip over both trips and the daily wage roughly halves. Judge the deal on the empty trip included, or you will think a mediocre voyage is a great one.

## Key mechanics and formulas
- Round voyage TCE: `TCE = (gross freight - voyage costs) / total round voyage days` where voyage costs include laden and ballast bunkers, port charges, and canal dues, and total days include laden plus ballast plus port days.
- Laden only rate overstates earnings because it divides revenue by laden days only, omitting the ballast days that carry cost but no revenue.
- Voyage cost split: `voyage costs = laden bunkers + ballast bunkers + port costs + canal dues`. Ballast bunkers are lower per day because the empty hull and lighter draft reduce resistance, but ballast days often equal or exceed laden days.
- Ballast bonus: a lump sum a charterer pays an owner under a [[Time Charter]] to compensate for positioning the ship to the delivery point, quoted in USD as a one off, separate from the daily hire. It exists precisely because the repositioning leg earns no hire otherwise.
- Triangulation: chaining a second cargo that loads near the first discharge port to shrink or eliminate the empty leg. A perfect triangle converts two laden legs and near zero ballast into far higher TCE. See [[Ballast Leg Economics|backhaul]] cargoes such as C16 style fronthaul and backhaul pairings on the [[Baltic Exchange and the Dry Indices]].
- Ballast leg as embedded option: the owner implicitly chooses the next load zone that maximises forward expected TCE, so positioning is a real option on the regional [[Forward Curve]] of freight.
- Rule of thumb: for a symmetric round trip the round voyage TCE is roughly the laden only daily rate times laden days divided by total days, so a 50 percent ballast share roughly halves the daily figure.

## Prerequisites
- [[Freight]]
- [[Time Charter]]
- [[Voyage Charter]]
- [[Vessel Classes and Deadweight Tonnage]]
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]]

## Related concepts (learn next)
- [[Baltic Route Codes]] because the fronthaul and backhaul codes encode exactly which legs are laden and which tend to be ballast.
- [[TC In and TC Out]] because comparing round voyage TCE against the TC rate is how an operator decides to spot trade or charter out.
- [[Forward Freight Agreement]] because ballast positioning shifts regional supply and moves the freight forward curve you hedge on.
- [[Baltic Exchange and the Dry Indices]] because the published route assessments are quoted laden and you must layer in ballast yourself.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] because ballast bunker burn is a large and hedgeable slice of voyage cost.
- [[Port Congestion and Waiting Time]] because waiting days stretch the denominator and crush the same TCE that ballast days do.
- [[Laytime, Demurrage and Despatch]] because demurrage adds revenue and despatch subtracts it on the laden leg, shifting the round voyage result.
- [[Voyage Charter]] because the owner prices the ballast leg into the per tonne rate quoted in a voyage fixture.

## Common misconceptions
- **"The freight rate on the route is what the ship earns per day."** Wrong, because the quoted route rate is a laden only figure and the ship must also fund the empty repositioning leg. Dividing revenue by total round voyage days, not laden days, gives the true daily earning, often half the naive number.
- **"Ballast legs barely matter because the ship is light and burns little fuel."** Wrong, because while ballast burn per day is lower, the ballast leg often consumes as many calendar days as the laden leg, and days are the scarce resource. The lost time, not just the fuel, is what compresses TCE.
- **"A ballast bonus is free extra money for the owner."** Wrong, because the bonus exists to offset the unpaid positioning voyage the owner must perform to reach the delivery point. It is compensation for a real cost, not profit, and a charterer prices it against the alternative of a closer ship.
- **"Good triangulation just means finding any return cargo."** Wrong, because a backhaul cargo at a loss making rate can earn less than ballasting fast to a stronger market. The decision is whichever path maximises round voyage TCE, not whichever path avoids an empty leg.

## Sources
- Baltic Exchange, Guide to Market Benchmarks and route definitions, balticexchange.com
- Martin Stopford, Maritime Economics, 3rd edition, chapters on voyage estimation and the time charter equivalent
- Manolis Kavussanos and Ilias Visvikis, The International Handbook of Shipping Finance, sections on freight rate modelling
- Clarksons Research, Shipping Intelligence Network voyage estimation notes
- Amir Alizadeh and Nikos Nomikos, Shipping Derivatives and Risk Management, on TCE and FFA pricing
