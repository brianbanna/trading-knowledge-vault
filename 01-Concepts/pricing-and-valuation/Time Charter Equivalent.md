---
aliases: [tce, time charter equivalent, tce rate, daily equivalent earnings]
tags:
  - "#freight/contracts"
date-added: "2026-06-17"
---

# Time Charter Equivalent

## Definition
Time Charter Equivalent (TCE) is the daily dollar figure a voyage earns after you strip out the costs of running that specific voyage, expressed as USD per day so it can be compared directly against a daily time charter hire rate. A voyage charter is quoted in USD per tonne of cargo, a time charter in USD per day, and those two prices cannot be compared as quoted. TCE is the conversion that puts the voyage onto the same per day basis as the period market. Formally, `TCE = (gross freight revenue - voyage costs) / round trip days`, where voyage costs are bunkers, port charges, canal tolls and brokerage commissions. The critical point: TCE is gross of vessel running cost. OPEX (crew, stores, lubricants, maintenance, insurance) is NOT subtracted, so TCE is the daily earnings the voyage throws off before you pay to keep the ship operating.

## Why it matters (commodities and FX)
TCE is the single yardstick a freight desk uses to make the core employment decision: take this spot voyage, or fix the ship out on a period [[Time Charter]] instead. Because spot voyages are priced per tonne and period deals are priced per day, you cannot rank them without converting, and TCE is that converter. An owner compares the TCE a route currently yields against the period hire on offer and takes whichever is higher for the chartering horizon. A charterer running tonnage does the mirror exercise. TCE is also how positions get marked: a desk holding voyage exposure or a [[Forward Freight Agreement]] translates index levels into TCE to see what the book is actually earning. Route by route, the [[Baltic Exchange and the Dry Indices]] publishes TCE assessments per [[Baltic Route Codes]] precisely so the market has a common daily number to trade and compare against [[Market Hire]].

## Concrete example
**Concrete:** A Capesize is offered a coal voyage. Gross freight revenue on the fixture is about USD 2,040,000 (cargo intake times the per tonne rate, before any deductions). Voyage costs for the round trip add up to roughly USD 1,200,000: bunkers for the laden and ballast legs, disbursements and port charges load and discharge, any canal tolls, plus address and brokerage commission. The full round trip, including the [[Ballast Leg Economics|ballast leg]] back to the next load area, runs 35 days. So `TCE = (2,040,000 - 1,200,000) / 35 = 840,000 / 35 = USD 24,000 per day`. Now compare to the period market. If a 12-month [[Time Charter]] is fixing at USD 20,000 per day, the spot voyage earns 4,000 per day more and the owner runs spot. If period hire is 28,000 per day, the voyage is the worse employment by 4,000 per day and the owner fixes the period instead and locks in the higher daily. Note that the 24,000 TCE is before OPEX, say 7,000 per day, so the voyage nets about 17,000 per day after running cost, but you still compare it to period hire on the gross TCE basis because hire is also quoted before the owner's OPEX.

Failure case: bunkers spike from 550 to 750 USD per tonne mid voyage planning and the discharge port hits congestion, adding 6 days of waiting. Voyage costs climb to about USD 1,450,000 and round trip days rise to 41. Now `TCE = (2,040,000 - 1,450,000) / 41 = 590,000 / 41 = about USD 14,400 per day`. The same freight rate now yields a TCE well below the 20,000 period alternative. The voyage that looked profitable collapses because fuel cost and time on the water both moved against it, which is exactly the [[Bunker Risk]] and [[Port Congestion and Waiting Time]] exposure embedded in any voyage TCE.

**Simplified:** A voyage is quoted per tonne of cargo and a period charter per day, so you cannot tell which pays better just by looking. TCE rewrites the voyage as a per day number: take the freight you collect, subtract the cost of doing that trip (fuel, ports, canals, commissions), divide by how many days the trip takes. If that daily number beats the period rate on offer, run spot. If fuel jumps or the ship sits stuck at port, costs and days both grow and the per day number can fall below the alternative, turning a good looking voyage into a poor one.

## Key mechanics and formulas
- `TCE = (gross freight revenue - voyage costs) / round trip days` — the core definition, USD per day.
- `gross freight revenue` = cargo quantity (tonnes) times the freight rate (USD per tonne), for a voyage; or the agreed lump sum for a lump sum fixture. This is gross, before any deductions.
- `voyage costs` = bunkers + port and terminal charges + canal tolls + brokerage and address commissions. These are trip specific cash outflows the owner pays under a [[Voyage Charter]].
- `round trip days` = laden steaming days + ballast steaming days + port days at load and discharge + any waiting or weather days. Include the [[Ballast Leg Economics|ballast leg]] back to repositioning.
- OPEX is excluded by construction: `OPEX` (crew, stores, lubes, maintenance, insurance, registry) is the daily cost of owning and manning the ship and is NOT in the TCE formula. Net daily margin to the owner is `TCE - daily OPEX`, but you compare employment options on TCE, not on net, because period hire is also quoted gross of OPEX.
- Sensitivity: TCE falls when bunkers rise (voyage costs up), when the voyage lengthens (days up, and bunkers up), and when port disbursements or commissions rise. It rises with a higher freight rate or a shorter, faster trip.

## Prerequisites
- [[Freight]]
- [[Voyage Charter]]
- [[Time Charter]]
- [[Ballast Leg Economics]]

## Related concepts (learn next)
- [[Market Hire]] — the period daily rate you compare a voyage TCE against to make the spot versus period decision.
- [[Baltic Route Codes]] — the standardized routes the Baltic assesses, each carrying its own published TCE.
- [[Baltic Exchange and the Dry Indices]] — the source of daily TCE assessments per route that the whole market references.
- [[TC In and TC Out]] — chartering a ship in on a daily rate and out on another; TCE is how you value the voyage leg of such a book.
- [[Relet]] — re fixing chartered in tonnage out to a third party, where comparing the in hire to the implied TCE out is the whole trade.
- [[Forward Freight Agreement]] — paper freight settled against index levels that are quoted in TCE terms for the dry routes.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] — bunkers are the largest swing in voyage costs and the main driver of TCE volatility.
- [[Voyage Charter vs Time Charter]] — the contract comparison TCE exists to resolve in dollar terms.

## Common misconceptions
- "TCE includes OPEX." No. TCE is gross of vessel running cost by definition. It subtracts only voyage specific costs (bunkers, port, canal, commission). Crew, maintenance and insurance are excluded so that TCE matches the basis on which time charter hire is quoted, which is also before the owner's OPEX. Subtract OPEX and you are computing net margin, a different number, not TCE.
- "TCE equals the freight rate." No. The per tonne freight rate is gross revenue input, before any voyage costs and before annualizing to a per day figure. TCE deducts voyage costs and divides by days. A high per tonne rate on a long, fuel heavy trip can produce a low TCE.
- "A higher TCE is always the better choice." Not necessarily. TCE ignores where the ship ends up. A slightly higher TCE voyage that discharges in a weak repositioning area may be worse than a lower TCE voyage that leaves the ship near strong forward cargo, because the next [[Ballast Leg Economics|ballast leg]] and forward earnings matter. TCE is one input, not the full positioning decision.
- "TCE and time charter hire are the same thing." No. Hire is a contracted price agreed between owner and charterer in a [[Charter Party]]. TCE is a derived analytical figure computed from a voyage to allow comparison against that hire. One is a price you transact at; the other is a yardstick you calculate.

## Sources
- Baltic Exchange, Guide to Market Benchmarks and TCE assessment methodology for the Capesize, Panamax and Supramax routes.
- Stopford, Maritime Economics, 3rd ed., chapters on the freight market and voyage cost analysis.
- Alizadeh and Nomikos, Shipping Derivatives and Risk Management, on converting voyage economics to TCE and marking freight positions.
- Kavussanos and Visvikis, The International Handbook of Shipping Finance, on chartering decisions and the spot versus period choice.
- Clarksons Shipping Intelligence Network (SIN), route level TCE earnings series.
- Ship and Bunker, daily bunker price assessments used in voyage cost build up.
