---
aliases: [voyage charter, vc, spot fixture, single voyage charter]
tags:
  - "#freight/contracts"
date-added: "2026-06-09"
---

# Voyage Charter

## Definition
A voyage charter is a rental agreement where a shipowner agrees to carry a specific cargo from one port to another for an agreed price, and the owner takes care of everything needed to actually move the ship. Think of it like hiring a taxi for a single trip across town at a quoted fare: you pay for the journey, not for the driver's time, and the driver pays for the fuel and worries about traffic. The charterer (the cargo owner) pays a freight rate, usually quoted in dollars per tonne of cargo or as a single lump sum, and the owner pays for the crew, the fuel (called [[Bunkers, IFO versus MGO, and the Bunker Hedge|bunkers]]), port charges, and canal tolls. Technically, the owner sells transportation of a stated parcel from a load port to a discharge port and retains full operational and commercial control of the vessel. The contract terms are set out in a [[Charter Party]], and [[Laytime, Demurrage and Despatch|laytime and demurrage]] govern how long the charterer has to load and discharge before penalties apply.

## Why it matters (commodities and FX)
The voyage charter is the spot market of [[Freight]], and it is the contract a commodity trader uses most when shipping a single cargo. If you buy a [[Dry Bulk versus Wet Bulk|dry bulk]] cargo of iron ore or coal and need it delivered, you fix a voyage charter and lock a known transport cost per tonne, which lets you price the delivered cargo and protect your margin. The critical distinction from a [[Time Charter]] is who bears bunker price risk and speed risk: under a voyage charter the owner pays for fuel and absorbs any delay at sea or in port, whereas under a time charter the charterer pays for bunkers and pays hire for every day the ship is used. That single difference drives whether the trader or the owner is exposed to a bunker spike or a slow passage. For a freight trader, the voyage rate is the underlying that [[Baltic Route Codes|Baltic route assessments]] track and that [[Forward Freight Agreement|forward freight agreements]] settle against, so understanding voyage economics is the foundation for hedging freight exposure.

## Concrete example
**Concrete:** A trader fixes a [[Vessel Classes and Deadweight Tonnage|Capesize]] to carry 170,000 tonnes of thermal coal from Newcastle, Australia to Qingdao, China at a freight rate of USD 12.00 per tonne. Gross freight is 170,000 * 12.00 = USD 2,040,000. The voyage is roughly 4,500 nautical miles one way; at 12 knots the laden leg takes about 15.6 days, and with the [[Ballast Leg Economics|ballast]] approach to Newcastle plus port time the round trip runs about 35 days. The owner budgeted bunkers at 45 tonnes per day of VLSFO at USD 600 per tonne, so about 35 * 45 * 600 = USD 945,000 of fuel, plus roughly USD 250,000 in port and canal-free costs, leaving an expected voyage profit near USD 845,000.

Now the failure case. Suppose VLSFO spikes to USD 780 per tonne after the fixture is signed. Fuel cost jumps to about 35 * 45 * 780 = USD 1,228,500, an extra USD 283,500 the owner eats entirely because freight is fixed per tonne. Worse, Qingdao is congested and the ship waits 6 days beyond the agreed [[Laytime, Demurrage and Despatch|laytime]]. Demurrage at USD 25,000 per day pays the owner 6 * 25,000 = USD 150,000, which partly offsets the delay, but the owner still loses 6 days of earning capacity on the next fixture. Net of the bunker hit and the lost time, the expected USD 845,000 profit can collapse toward USD 400,000 or lower. The charterer, by contrast, paid exactly USD 2,040,000 and bore none of the fuel or at-sea delay risk; the charterer only pays demurrage, and only because its own discharge operation ran slow.

**Simplified:** The owner quotes one all-in price to move the coal and pockets the difference between that price and its costs. If fuel jumps or the ship sits idle at sea, the owner loses; the cargo trader's transport cost is locked. Demurrage is the only extra the charterer pays, and only if the charterer is too slow loading or discharging.

## Key mechanics and formulas
- Gross freight (rate basis): `Freight = Rate_per_tonne * Cargo_quantity` where `Rate_per_tonne` is the agreed USD per metric tonne and `Cargo_quantity` is the contracted cargo intake in tonnes.
- Lump sum basis: `Freight = Lump_sum` where the owner is paid a single fixed amount regardless of exact tonnage, common for part cargoes or awkward parcels.
- Owner voyage profit: `Voyage_profit = Gross_freight - Bunker_cost - Port_costs - Canal_costs - Commissions` where each cost item is borne by the owner under the voyage charter.
- Time charter equivalent: `TCE = (Gross_freight - Voyage_costs) / Round_trip_days` where `Voyage_costs` are bunkers plus port and canal costs and `Round_trip_days` is the full laden plus ballast plus port duration. `TCE` converts a voyage rate into a daily figure so it can be compared directly against a [[Time Charter|time charter]] hire rate.
- Demurrage and despatch: `Demurrage = Demurrage_rate * Days_over_laytime` paid by charterer to owner for delay beyond [[Laytime, Demurrage and Despatch|laytime]]; despatch is the reverse, often at half the demurrage rate, paid by owner to charterer for finishing early.
- Risk allocation conventions: the owner bears bunker price risk, speed and weather risk on passage, and off-hire risk for breakdowns; the charterer bears cargo risk and port-side time risk via laytime. This is the inverse of [[TC In and TC Out|TC]] arrangements.
- Freight payment is typically due on a stated split, for example 95 percent on signing or release of bills of lading and the 5 percent balance on completion of discharge, with terms set in the [[Charter Party]].

## Prerequisites
- [[Freight]]
- [[Charter Party]]
- [[Vessel Classes and Deadweight Tonnage]]
- [[Dry Bulk versus Wet Bulk]]
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]]

## Related concepts (learn next)
- [[Time Charter]] because it is the direct alternative contract and flips who pays bunkers and bears speed risk.
- [[Laytime, Demurrage and Despatch]] because these clauses decide how port delays turn into payments under a voyage fixture.
- [[Ballast Leg Economics]] because the unpaid repositioning leg is buried inside every voyage rate and drives the true round-trip return.
- [[Baltic Route Codes]] because the Baltic publishes voyage rate assessments per route that benchmark your fixture.
- [[Baltic Exchange and the Dry Indices]] because the indices aggregate voyage rates into the headline numbers traders quote.
- [[Forward Freight Agreement]] because FFAs let you hedge the voyage rate you will pay or receive in the future.
- [[TC In and TC Out]] because relet and operator economics depend on comparing voyage earnings against time charter hire.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] because owner profit on a voyage charter lives or dies on the fuel bill.
- [[Voyage Charter vs Time Charter]] because the side by side comparison pins down exactly which risks shift between the two structures.
- [[Time Charter Equivalent]] because converting the voyage rate to a daily figure is how you compare it against a time charter hire.

## Common misconceptions
- **"Under a voyage charter the charterer pays for fuel."** Wrong. The owner pays for bunkers on a voyage charter and absorbs any price spike, which is precisely why the time charter exists as the contract where the charterer takes on fuel and speed risk in exchange for paying daily hire.
- **"The freight rate is the owner's profit."** Wrong. The quoted USD per tonne is gross revenue; the owner must subtract bunkers, port charges, canal tolls, and broker commissions, so the real comparison metric is the time charter equivalent, not the headline rate.
- **"Demurrage is a penalty on the owner for being late."** Wrong. Demurrage is paid by the charterer to the owner when the charterer's loading or discharging exceeds the agreed [[Laytime, Demurrage and Despatch|laytime]]. It compensates the owner for the ship being detained, it does not punish the owner.
- **"A voyage charter and a contract of affreightment are the same thing."** Wrong. A voyage charter covers one stated voyage with a single cargo, while a contract of affreightment commits the owner to carry multiple cargoes over a period on agreed terms, so the COA is a series of voyage obligations rather than a single fixture.

## Sources
- Baltic Exchange, "Manual for Panellists" and route definition guides, https://www.balticexchange.com
- Martin Stopford, "Maritime Economics", 3rd edition, Routledge, chapters on freight markets and chartering
- BIMCO standard voyage charter forms (GENCON, AMWELSH for coal), https://www.bimco.org
- Manolis G. Kavussanos and Ilias D. Visvikis, "The International Handbook of Shipping Finance", chapters on freight derivatives and the spot market
- Intertanko and Intercargo chartering guidance notes on voyage cost allocation
