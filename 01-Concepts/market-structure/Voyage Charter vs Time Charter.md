---
aliases: [voyage vs time charter, vc vs tc, charter type comparison, voyage charter versus time charter]
tags:
  - "#freight/contracts"
date-added: "2026-06-17"
---

# Voyage Charter vs Time Charter

## Definition
There are 2 fundamental ways to hire a ship, and they differ in who pays for fuel and who carries which risk. In a [[Voyage Charter]] you pay an owner a price per tonne of cargo to move it from A to B, and the owner does everything: provides the ship, burns and pays for the bunkers, and absorbs any delay at sea. In a [[Time Charter]] you rent the ship by the day, you direct where it goes and what it carries, and you pay for the fuel and the voyage costs yourself. Technically, a voyage charter prices in USD per tonne (or as a lump sum) and the owner retains commercial and operational control of the laden voyage, while a time charter prices in USD per day of hire and transfers commercial control to the charterer with the owner retaining technical and crew responsibility. The choice of structure is a choice of risk allocation, and it determines whether you, or the counterparty, are long or short freight and bunkers.

## Why it matters (commodities and FX)
Picking the contract type is the first risk decision a freight trader makes, before any price is agreed. Under a voyage charter the owner is short bunkers and short freight market for the duration of the trip, because a higher fuel price or a slower passage eats a fixed per tonne revenue. Under a time charter the charterer takes on both [[Bunker Risk]] and [[Freight Rate Risk]]: they pay whatever fuel costs, they earn whatever the spot voyage market gives them when they employ the ship, and they only know their daily vessel cost is fixed. This is exactly the position an operator runs when they [[TC In and TC Out]] or [[Relet]] a vessel, taking a ship on period hire and trying to cover the daily cost with voyage employment. Knowing which side of each risk you sit on tells you what to hedge: a voyage owner hedges bunkers and may sell [[Forward Freight Agreement]] cover, while a time charterer hedges the spot freight they need to earn and the fuel they will burn.

## Concrete example
**Concrete:** Take one Panamax (about 75,000 dwt) to carry coal on a route benchmarked near a [[Baltic Route Codes]] assessment. Price it both ways. As a voyage charter the owner quotes USD 18.00 per tonne on a 70,000 tonne cargo, so gross freight is 70,000 * 18.00 = USD 1,260,000. The round trip is 35 days, the ship burns 35 tonnes per day of VLSFO over say 24 steaming days plus auxiliary load, call it 900 tonnes of fuel, and bunkers are priced at USD 600 per tonne, so fuel cost is 900 * 600 = USD 540,000. Add port, canal, and commissions of USD 120,000. Voyage costs total 660,000. The [[Time Charter Equivalent|TCE]] is (1,260,000 - 660,000) / 35 = USD 17,143 per day. Now suppose bunkers spike to USD 800 per tonne after fixing. Fuel cost rises to 900 * 800 = USD 720,000, voyage costs become 840,000, and TCE drops to (1,260,000 - 840,000) / 35 = USD 12,000 per day. The owner absorbed the entire USD 180,000 fuel hit because the freight rate was locked at 18.00 per tonne. Price the same ship as a time charter instead: the charterer pays USD 15,500 per day of hire and pays the bunkers themselves. If bunkers spike to 800, the charterer pays the extra 180,000, and the owner is untouched because hire is fixed at 15,500 regardless of fuel. Converting to compare directly: against a period [[Market Hire]] of 15,500 per day, the voyage at unchanged bunkers earns a TCE of 17,143 per day, so the spot voyage beats taking the ship out on period by about 1,643 per day. After the bunker spike the voyage TCE of 12,000 falls 3,500 below the 15,500 period hire, so the same fixture is now a loss relative to the period alternative.

**Simplified:** Same ship, 2 ways to hire it. Voyage charter: the owner gets a fixed price per tonne and pays for fuel, so when fuel jumps the owner eats it. Time charter: you rent by the day and buy your own fuel, so when fuel jumps you eat it. To compare a voyage price to a daily rent you turn the voyage into a per day number called TCE. Here the voyage looked better than renting by the day until fuel spiked, and then renting by the day would have been the safer choice.

## Key mechanics and formulas
- `voyage gross freight = rate per tonne * cargo tonnes` or a flat lump sum. The owner keeps this and pays voyage costs out of it.
- `voyage costs = bunkers + port + canal + commissions`. These are subtracted to get the owner net.
- `TCE = (gross freight revenue - voyage costs) / round trip days`. TCE is gross of OPEX and crew, so do not subtract running cost. This is the bridge that lets you compare a USD per tonne voyage to a USD per day hire.
- `time charter cost to charterer = hire per day * on-hire days + bunkers + port + canal`. The charterer, not the owner, pays the fuel and voyage costs here.
- Off hire: under a time charter, if the ship breaks down or fails performance, hire stops accruing for the off hire period, so the owner carries breakdown risk while on hire is the charterer's risk.

## Prerequisites
[[Freight]]
[[Charter Party]]
[[Voyage Charter]]
[[Time Charter]]

## Related concepts (learn next)
- [[Time Charter Equivalent]] is the single number that makes a voyage rate and a daily hire comparable, so learn it next to price both structures on one scale.
- [[TC In and TC Out]] shows the operator trade of renting a ship on period and re employing it, which is the live application of this comparison.
- [[Relet]] is sub letting a chartered ship, the other way an operator monetises the gap between hire paid and voyage earned.
- [[Bunker Risk]] is the fuel exposure that sits with the owner under VC and the charterer under TC, the cleanest illustration of the risk split.
- [[Freight Rate Risk]] is the spot market exposure that the charterer absorbs under a time charter and the owner locks away under a fixed voyage.
- [[Laytime, Demurrage and Despatch]] only bites under a voyage charter and explains why slow port operations cost the charterer, not the owner.
- [[Forward Freight Agreement]] is the paper tool a voyage owner or time charterer uses to hedge the freight side of these exposures.
- [[Physical vs Paper Freight]] frames how the physical fixture choices here connect to the cleared derivatives market.

## Common misconceptions
- "The charterer pays the fuel on a voyage charter." Wrong. Under a voyage charter the owner buys and burns the bunkers and bears the price, because the owner is paid a fixed rate per tonne that already has to cover fuel. The charterer only pays fuel under a time charter.
- "Hire and the freight rate are the same number." Wrong. Hire is USD per day and the voyage rate is USD per tonne or a lump sum. They are different units measuring different things, and you must convert the voyage to a [[Time Charter Equivalent|TCE]] before any comparison means anything.
- "A time charter locks in your profit." Wrong. A time charter only fixes your vessel cost per day. Your profit still depends on the spot voyage market when you employ the ship and on the bunkers you pay, both of which you now own as risks. Fixed cost is not fixed margin.
- "Demurrage punishes the owner for being slow." Wrong. Demurrage is paid by the charterer to the owner when the charterer's cargo operations exceed the agreed laytime. It compensates the owner for a detained ship, so slow load or discharge costs the charterer, not the owner.

## Sources
- Baltic Exchange, route definitions and assessment guides for voyage and period assessments.
- Stopford, Maritime Economics, 3rd edition, chapters on chartering markets and the four shipping markets.
- Alizadeh and Nomikos, Shipping Derivatives and Risk Management, on TCE, freight risk, and contract structures.
- Kavussanos and Visvikis, The International Handbook of Shipping Finance, chartering and risk allocation chapters.
- Clarksons Shipping Intelligence Network, vessel and route fixture data.
- Ship and Bunker, VLSFO and MGO price references for bunker cost inputs.
