---
aliases: [time charter, t/c, tc, period charter, daily hire]
tags:
  - "#freight/contracts"
date-added: "2026-06-09"
---

# Time Charter

## Definition

A time charter is a rental agreement where you hire a whole ship for a stretch of time, not for one specific trip. Think of it like leasing a car by the month: you pay a fixed daily rate, you decide where to drive and pay for the fuel and the tolls, but the owner still keeps it serviced and provides the driver. The charterer pays a daily hire rate and controls the commercial employment of the vessel, meaning what cargo it carries and where it sails, while paying voyage costs such as bunkers, port dues and canal fees. The owner supplies and pays the crew, maintains the ship and insures the hull, and carries the risk that the vessel stops earning if it breaks down. The hire period runs from months to several years and is governed by a [[Charter Party]]. Contrast this with a [[Voyage Charter]], where the owner is paid per cargo and absorbs the voyage costs.

## Why it matters (commodities and FX)

A time charter is the central tool for taking a directional or relative value view on freight without owning steel. A trader who is bullish on dry bulk demand can charter a [[Vessel Classes and Deadweight Tonnage|Panamax]] in for 12 months at a fixed daily rate, then relet it on shorter trips or spot voyages, capturing the spread if the market rises. The hire rate is effectively the freight forward curve priced into a single instrument, so the period rate quoted today embeds the market's expectation of where spot will sit over the charter term, which links directly to the [[Forward Curve]] logic traders already use in commodities. It also sets up clean physical versus paper trades: a charterer who is long a vessel on a fixed rate is short freight risk and can hedge that exposure with a [[Forward Freight Agreement]]. For a freight desk the distinction between [[TC In and TC Out]] is the daily profit and loss engine, and the daily hire rate is the number everything else, including [[Time Charter Equivalent|TCE]] comparison against the spot voyage market, is measured against.

## Concrete example

**Concrete:** A trader charters in a [[Vessel Classes and Deadweight Tonnage|Panamax]] (about 82,000 DWT) for 12 months at a fixed hire of 15,000 USD per day, delivered Singapore. The owner's daily operating cost (crew, stores, maintenance, insurance, plus financing) is roughly 11,000 USD per day, so the owner books a margin of about 4,000 USD per day, or roughly 1.46M USD over 365 days. Now spot moves. If the Pacific round voyage market on routes like [[Baltic Route Codes|P3A or P5]] rises so that a comparable Panamax earns a [[Time Charter Equivalent|TCE]] of 22,000 USD per day, the owner who locked 15,000 USD has given up 7,000 USD per day, about 2.55M USD over the year, since the charterer pockets the upside by reletting or trading the vessel. The deal WORKED for the charterer and FAILED for the owner in opportunity terms. If instead spot collapses and comparable vessels earn only 9,000 USD per day TCE, the owner still collects the full 15,000 USD, beating the market by 6,000 USD per day, about 2.19M USD, and the charterer is now overpaying versus spot. Two risks sit on top of this. Off hire: if the main engine fails for 10 days, hire stops under the off hire clause, costing the owner 150,000 USD of revenue plus the repair while still paying the crew. Bunker exposure: the charterer, not the owner, buys the fuel, so a spike in [[Bunkers, IFO versus MGO, and the Bunker Hedge|IFO]] raises the charterer's voyage cost and erodes the relet spread.

**Simplified:** You rent the whole ship for a year at a fixed daily price. You pay the fuel and the port bills and you decide where it goes. The owner keeps it running and crewed. If freight prices go up during the year you win because your cost is locked low. If freight prices fall the owner wins because they locked you into a high rate. If the ship breaks down, the owner stops getting paid until it works again.

## Key mechanics and formulas

- **Hire rate:** quoted in USD per day, payable in advance, usually every 15 or 30 days. `Gross hire = daily hire rate x duration in days`. A 15,000 USD per day Panamax for 12 months is `15000 x 365 = 5,475,000 USD` gross before any off hire deductions.
- **Owner net margin:** `Owner margin per day = daily hire rate - daily operating cost`, where operating cost (often called OPEX) covers crew, stores, lube oil, maintenance, repairs and insurance. Financing cost on the vessel is layered on separately.
- **Delivery and redelivery:** the charter starts when the vessel is delivered at the agreed place in the agreed condition (`on hire survey`) and ends at redelivery (`off hire survey`). The charter party defines the delivery range, the laycan window, and a redelivery range with a tolerance, for example `12 months plus or minus 30 days in charterer's option`.
- **Off hire clause:** hire is suspended for time lost to causes within the owner's sphere, such as breakdown, drydocking, crew deficiency or detention. `Off hire deduction = daily hire rate x days off hire`. The charterer still does not pay during off hire, and bunkers consumed during off hire are typically for the owner's account.
- **Bunkers on delivery and redelivery:** the charterer buys back the bunkers on board at delivery and sells them back at redelivery, each at agreed prices, so the bunker quantity and price clauses matter to the net economics. See [[Bunkers, IFO versus MGO, and the Bunker Hedge]].
- **Time charter equivalent comparison:** to judge whether a fixed hire is rich or cheap, the desk compares it to the spot voyage market expressed as a [[Time Charter Equivalent|TCE]]: `TCE = (voyage freight revenue - voyage costs) / round voyage days`. If spot TCE is above the fixed hire, the charterer is winning.
- **Speed and consumption (performance warranty):** the owner warrants a service speed at a stated daily bunker consumption, for example `14 knots on 32 tonnes IFO per day`. Underperformance gives the charterer a speed and consumption claim, since slow steaming or extra fuel burn raises the charterer's voyage cost.
- **Hire types:** a standard time charter has the owner manning and maintaining the ship. A `bareboat charter` (demise charter) hands the charterer the vessel with no crew, shifting OPEX and manning to the charterer, which is a different and more capital intensive structure.

## Prerequisites

- [[Vessel Classes and Deadweight Tonnage]]
- [[Charter Party]]
- [[Freight]]
- [[Dry Bulk versus Wet Bulk]]

## Related concepts (learn next)

- [[Voyage Charter]]: the alternative structure where the owner is paid per cargo and pays the voyage costs, the direct counterpart to the time charter.
- [[TC In and TC Out]]: the desk practice of chartering vessels in and out to trade the spread, which is built directly on time charter mechanics.
- [[Time Charter Equivalent]]: the metric that converts spot voyage returns into a daily rate so you can compare them against a fixed hire.
- [[Forward Freight Agreement]]: the paper hedge a fixed rate charterer or owner uses to offset the freight exposure created by the period deal.
- [[Laytime, Demurrage and Despatch]]: relevant once a time chartered vessel is sublet on voyage terms and starts carrying cargo.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]]: the largest voyage cost the charterer carries under a time charter and a key risk to hedge.
- [[Baltic Exchange and the Dry Indices]]: the source of the period and spot assessments used to mark a time charter to market.
- [[Ballast Leg Economics]]: matters because the charterer pays for repositioning days even when no cargo is on board.

## Common misconceptions

**"Under a time charter the owner pays for the fuel."** Wrong. The charterer pays for bunkers, port dues and canal fees under a time charter. The owner pays these only under a [[Voyage Charter]]. Mixing this up flips the entire risk allocation of the contract.

**"A time charter locks in profit for the charterer."** Wrong. It locks in the cost of the vessel, not the profit. The charterer still has to find profitable employment, pay rising bunker bills and cover ballast days. If freight falls below the fixed hire, the charterer is overpaying versus spot and can lose money on the position.

**"Once fixed, the owner is guaranteed the full hire for the whole period."** Wrong. The off hire clause suspends hire whenever the vessel cannot perform due to the owner's account causes such as breakdown or drydock, so revenue is not guaranteed and downtime risk sits with the owner.

**"Time charter hire and the spot voyage rate are the same number."** Wrong. They are different units. Hire is USD per day for the whole ship over a period. A spot voyage is priced per cargo or in [[Freight|Worldscale]] for one trip. You convert a voyage into a [[Time Charter Equivalent|TCE]] before you can compare the two.

## Sources

- Baltic Exchange: time charter route assessments and period (T/C) indices for dry bulk
- BIMCO standard forms: NYPE 2015 and BALTIME 1939 (as revised) time charter party templates
- Martin Stopford, "Maritime Economics," 3rd edition, on charter structures and vessel earnings
- Clarkson Research: Shipping Intelligence Network, period rate time series
- Manolis Kavussanos and Ilias Visvikis, "The International Handbook of Shipping Finance," on chartering and freight risk management
