---
aliases: [bunkers, bunker fuel, ifo 380, hsfo, vlsfo, mgo, marine gas oil, imo 2020, bunker hedge, scrubbers]
tags:
  - "#freight/wet"
  - "#energy/refined"
date-added: "2026-06-09"
---

# Bunkers, IFO versus MGO, and the Bunker Hedge

## Definition
Bunkers are the fuel a ship burns to move and to run its generators. The word has nothing to do with golf or war, it comes from the coal bunkers of old steamships, and it stuck even though ships now burn oil. Bunkers are one of the two largest costs of running a voyage, the other being the ship itself, so the price of bunkers directly decides whether a voyage makes or loses money. There are several grades of marine fuel that differ by how much sulphur they contain and how refined they are, and rules now force ships to burn cleaner, more expensive grades than they used to. Technically, bunkers are residual fuel oils and distillates sold by mass in metric tonnes, priced per tonne, and consumed at a rate that depends on vessel size, speed and sea conditions. A trader who quotes [[Freight]] without a view on bunkers is quoting a price with a hole in the cost stack.

## Why it matters (commodities and FX)
Fuel is typically 40 to 60 percent of the cash cost of a spot voyage, so a freight or commodities trader who fixes a [[Voyage Charter]] is implicitly taking a position on the oil price between fixing and steaming. If you agree a lump sum freight today and bunkers spike before you load, the voyage that looked profitable turns into a loss, because under a [[Voyage Charter]] the shipowner pays for the fuel. This is the same fuel exposure an oil refiner or a physical gasoil trader manages, which is why the freight desk and the refined products desk overlap. Bunker exposure also feeds straight into [[Time Charter]] decisions, because a charterer on [[TC In and TC Out]] pays bunkers directly and must forecast them across the whole charter. Knowing the grades, the regulations and the hedge instruments lets you protect a voyage P&L the same way you would hedge any other input cost, using [[Hedging]] with futures or swaps.

## Concrete example
**Concrete:** A [[VLCC]] (very large crude carrier, around 300,000 dwt deadweight) is fixed for a voyage from Ras Tanura to Ningbo. The voyage is roughly 22 days laden plus port time, and at an eco speed of about 12 knots the ship burns close to 55 tonnes per day of [[VLSFO]] (very low sulphur fuel oil), so call it 1,200 tonnes of fuel for the leg. The owner fixes the freight when VLSFO at Fujairah is 550 dollars per tonne, budgeting a bunker bill of 1,200 times 550 equals 660,000 dollars, and on those numbers the voyage clears a daily [[Time Charter]] equivalent of about 35,000 dollars. Then a refinery outage and a Middle East scare push VLSFO to 700 dollars per tonne before the owner stems (buys) the fuel. The bunker bill jumps to 1,200 times 700 equals 840,000 dollars, a 180,000 dollar overrun that the fixed freight does not cover, and the TCE collapses to roughly 27,000 dollars per day. If the owner had instead bought 12 gasoil futures lots (gasoil trades in 100 tonne lots on [[ICE]], so 1,200 tonnes is 12 lots) at the fixing date, and gasoil rose by about 150 dollars per tonne alongside VLSFO, the futures gain of roughly 12 times 100 times 150 equals 180,000 dollars offsets the physical overrun, and the voyage P&L is back near the budgeted 35,000 dollar TCE. That offset is imperfect because gasoil is a distillate and VLSFO is a different product, so the hedge carries [[Basis Risk]]. If instead bunkers had fallen from 550 to 450 dollars, the unhedged owner pockets a 120,000 dollar windfall, while the hedged owner gives most of that back on the futures, having locked the cost on purpose.

**Simplified:** The ship is a truck and bunkers are diesel. If you quote a fixed delivery price today but the diesel price doubles before you fill the tank, your fixed price no longer covers the trip. Buying a fuel futures contract is like pre paying for the diesel at today's price, so a price spike costs you nothing extra. The catch is the futures track a slightly different fuel than what you actually pump, so the protection is close but not exact.

## Key mechanics and formulas
- Bunker bill for a leg: `bunker_cost = consumption_per_day * days * price_per_tonne` where consumption is tonnes per day, days is steaming plus port days, and price is dollars per tonne.
- Consumption scales steeply with speed, roughly `fuel ~ speed^3` over the relevant range, which is why slow steaming saves disproportionate fuel and underpins [[Ballast Leg Economics]].
- Grades by sulphur and refining:
  - **HSFO** (high sulphur fuel oil, also called IFO 380 for its 380 centistoke viscosity) is a cheap residual fuel at up to 3.5 percent sulphur. After the 2020 cap it is legal to burn only on ships fitted with a scrubber.
  - **VLSFO** (very low sulphur fuel oil) is a residual blend at the 0.5 percent sulphur cap, the default global bunker fuel since 2020.
  - **MGO** (marine gas oil) is a cleaner distillate, roughly 0.1 percent sulphur, burned inside Emission Control Areas, for manoeuvring in port and as a more expensive backstop. It sits closest to the gasoil futures contract.
- IMO 2020: from 1 January 2020 the International Maritime Organization capped sulphur in marine fuel at 0.5 percent outside ECAs, down from 3.5 percent, forcing the switch from HSFO to VLSFO or MGO unless a scrubber is fitted.
- Scrubbers (exhaust gas cleaning systems) wash sulphur out of the exhaust so a ship can keep burning cheap HSFO legally. The economics depend on the **HSFO to VLSFO spread**, often called the scrubber spread: `scrubber_payback = capex / (annual_consumption * hsfo_vlsfo_spread)`. A wide spread makes scrubbers pay back fast, a narrow spread makes them dead weight.
- Bunker hedge instruments:
  - **Gasoil or low sulphur gasoil futures** on [[ICE]], a liquid proxy for MGO and a correlated proxy for VLSFO, traded in 100 tonne lots.
  - **Fuel oil futures and swaps** including 0.5 percent VLSFO and 3.5 percent HSFO contracts on [[ICE]] and the CME, which track bunkers more directly but are less liquid.
  - **Bunker swaps**, an over the counter cash settled swap against a published bunker index at a named port (for example Singapore or Rotterdam), removing the [[Basis Risk]] of a futures proxy at the cost of less liquidity and a counterparty.
- Hedge ratio: `lots = tonnes_to_hedge / lot_size`, adjusted by a beta if the hedge instrument moves less than one for one with the physical bunker grade.

## Prerequisites
- [[Freight]]
- [[Voyage Charter]]
- [[Hedging]]
- [[Basis Risk]]
- [[Dry Bulk versus Wet Bulk]]

## Related concepts (learn next)
- [[Forward Freight Agreement]] because hedging the freight rate and hedging the bunker cost are the two halves of locking a voyage margin.
- [[Time Charter]] because a charterer on a time charter pays bunkers directly and must forecast and hedge them across the charter term.
- [[Ballast Leg Economics]] because fuel burn on the empty repositioning leg is pure cost and drives speed and routing choices.
- [[EEXI and CII Regulations]] because carbon rules tighten on top of the sulphur cap and push fuel choice, speed and future alternative fuels.
- [[Basis Risk]] because the gap between the hedge instrument and the actual bunker grade is the main flaw in any bunker hedge.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] feeds [[Forward Curve]] reading, since [[Contango]] or [[Backwardation]] in the gasoil curve changes the cost of carrying a hedge.
- [[Strait of Hormuz]] because a chokepoint scare is a classic trigger for the bunker spikes that the hedge is meant to absorb.
- [[Value at Risk]] because sizing unhedged bunker exposure across a fleet is a portfolio risk question.

## Common misconceptions
- **"The charterer always pays for fuel, so the owner has no bunker risk."** Wrong, it depends on the charter type. Under a [[Voyage Charter]] the owner buys and pays for bunkers and carries the full price risk, while only under a [[Time Charter]] does the charterer take over the fuel cost. The party exposed is set by the [[Charter Party]], not by habit.
- **"VLSFO and MGO are basically the same fuel now that sulphur is capped at 0.5 percent."** Wrong. VLSFO is a residual blend near the 0.5 percent cap, while MGO is a cleaner distillate near 0.1 percent that is required inside ECAs and costs meaningfully more. They have different prices, different viscosities, and they track different futures, so treating them as one product mishedges the exposure.
- **"A scrubber is always worth fitting because HSFO is cheaper."** Wrong. The scrubber only pays if the HSFO to VLSFO spread stays wide enough to recover the capital cost over the ship's remaining life. When the spread narrows the scrubber becomes a stranded cost plus extra maintenance, and tightening carbon rules under [[EEXI and CII Regulations]] can shorten the window further.
- **"A gasoil futures hedge removes all my bunker risk."** Wrong. Gasoil futures are a proxy, not the same product as the VLSFO actually burned, so the hedge leaves [[Basis Risk]] between the two. A bunker swap on a port specific index removes more of that basis but adds counterparty and liquidity cost.

## Sources
- Baltic Exchange, guides to freight derivatives and bunker adjustment conventions, balticexchange.com
- IMO, MARPOL Annex VI and the 2020 global sulphur limit, imo.org
- Ship and Bunker, daily VLSFO, HSFO and MGO price assessments by port, shipandbunker.com
- ICE and CME product specifications for gasoil, low sulphur gasoil and marine fuel oil futures and swaps
- Stopford, Martin. Maritime Economics, 3rd edition, chapters on voyage costs and bunker economics
- Platts and Argus marine fuel methodology documents for bunker index pricing
