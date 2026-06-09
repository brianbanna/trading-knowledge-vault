---
aliases: [charter party, charterparty, c/p, cp, charter contract]
tags:
  - "#freight/contracts"
date-added: "2026-06-09"
---

# Charter Party

## Definition
A charter party is the written contract that hires a ship. Think of it like a rental agreement, except instead of a car or an apartment you are renting a 180,000 deadweight tonne bulk carrier or a crude tanker, and the rules of who pays for what, who waits for whom, and who is to blame when something goes wrong run to dozens of pages. The two parties are the shipowner (or disponent owner) and the charterer (the party hiring the ship to move cargo). Because negotiating every clause from scratch on every fixture would be impossibly slow, the market uses standard printed forms published by bodies like [[Baltic Exchange and the Dry Indices|BIMCO]], the Baltic and International Maritime Council, which the parties then amend with typed riders and additional clauses. The form chosen and the precise wording of its clauses decide how risk, cost, and time are split between owner and charterer, which is why charter party wording is litigated constantly. In law the charter party is a contract of carriage or hire, distinct from the bill of lading, which is the receipt and document of title for the cargo itself.

## Why it matters (commodities and FX)
A freight trader does not just trade a freight rate, they trade a contract, and the contract is the charter party. The headline number on a fixture, say $18,000 per day or Worldscale 120, is only meaningful once you know which form governs it and how the clauses allocate waiting time, bunkers, off hire, and deviation. Two fixtures at the same rate can have wildly different economics if one puts demurrage risk on the charterer and the other shifts it back to the owner. When you take a vessel on [[TC In and TC Out|TC in]] to cover a [[Forward Freight Agreement]] short or to lift a physical commodity cargo, the off hire clause, the speed and consumption warranty, and the redelivery range you accept determine whether your hedge actually performs. A single ambiguous laytime clause can turn a profitable [[Voyage Charter]] into a six figure [[Laytime, Demurrage and Despatch|demurrage]] dispute, so the contract is where freight profit and loss is really won or lost.

## Concrete example

**Concrete:** A trading house fixes a Panamax, 76,000 deadweight tonnes, to carry coal from Newcastle, Australia, to Qingdao, China, on an amended [[Voyage Charter|GENCON 1994]] voyage form at a freight of $14.50 per tonne, with 72 hours total laytime allowed for loading and discharging combined, and a demurrage rate of $22,000 per day. The laytime clause says laytime counts from when the vessel tenders Notice of Readiness, "Weather Working Days, Sundays and Holidays Excepted," and the printed form ties NOR validity to the vessel being "in all respects ready to load." At Qingdao the vessel arrives but waits 6 days at anchor in heavy [[Port Congestion and Waiting Time|congestion]] before a berth opens. The dispute: was the vessel an "arrived ship" able to tender a valid NOR from the anchorage, or only once alongside? If the charter party is a port charter and the wording lets NOR be tendered at the customary anchorage, laytime runs during the wait, the allowed 72 hours is consumed, and the charterer owes roughly 5 days of demurrage, about $110,000, to the owner. That is the success case for the owner. If the charter is a berth charter or the rider clause requires the vessel to be "in berth and in free pratique" before NOR is valid, laytime does not start during the anchorage wait, the owner eats the 6 day delay as unpaid waiting time, and the $110,000 swings the other way as an opportunity loss against the owner's next fixture. Same rate, same route, same congestion: the entire outcome turns on one clause and one word, "berth" versus "port."

**Simplified:** Renting the ship comes with a rulebook. One sentence in that rulebook decides whether the clock starts ticking while the ship sits at anchor waiting for a spot to unload. If the clock runs during the wait, the cargo party pays the ship owner for the delay. If it does not, the owner absorbs the cost. The freight rate looks the same either way, but the contract wording moves a hundred thousand dollars from one side to the other.

## Key mechanics and formulas
- **Standard forms by trade and by charter type:**
  - `GENCON` (BIMCO general purpose [[Voyage Charter]] form, current 1994 and 2022 editions): the default dry bulk voyage form.
  - `NYPE` (New York Produce Exchange, current 2015 edition): the dominant dry bulk [[Time Charter]] form.
  - `BALTIME` (BIMCO Baltic time charter): an older time charter form, more owner friendly than NYPE on some clauses.
  - `ASBATANKVOY` (Association of Ship Brokers and Agents tanker voyage charter): a widely used tanker [[Voyage Charter]] form.
  - `SHELLVOY` (Shell tanker voyage form, current SHELLVOY 6): an oil major's tanker voyage form, often used with the [[Freight|Worldscale]] rate schedule.
  - Other notable forms include `BPVOY`, `GASVOY` for LPG, and `SUPPLYTIME` for offshore support vessels.
- **Core clauses and which party they favor:**
  - `Vessel description`: deadweight, draft, cubic capacity, speed and consumption warranty. A wrong description exposes the owner to a misrepresentation or performance claim. See [[Vessel Classes and Deadweight Tonnage]].
  - `Laytime`: the time allowed to load and discharge before [[Laytime, Demurrage and Despatch|demurrage]] accrues. Phrased in `running hours`, `WWDSHEX` (Weather Working Days Sundays Holidays Excepted), or `SHINC` (Sundays and Holidays Included).
  - `Demurrage and despatch`: demurrage is liquidated damages the charterer pays the owner for exceeding laytime, `demurrage = excess time × daily demurrage rate`; despatch is a reward to the charterer for finishing early, usually at half the demurrage rate.
  - `Off hire` (time charter): suspends hire payment when the vessel cannot perform due to owner side causes such as breakdown or drydocking. `Net hire owed = gross hire − off hire periods × daily rate`.
  - `Safe port / safe berth`: the charterer warrants it will only order the vessel to ports the vessel can reach and leave safely. Breach shifts grounding or damage liability to the charterer.
  - `War risk` (CONWARTIME, VOYWAR clauses): lets the owner refuse or deviate from a voyage into a war or piracy zone, relevant for the [[Strait of Hormuz]] and the Red Sea, and governs who pays additional war risk insurance premiums.
  - `Bunkers`: in a voyage charter the owner pays for fuel; in a time charter the charterer buys and pays for bunkers, so quantity and price on delivery and redelivery are agreed. See [[Bunkers, IFO versus MGO, and the Bunker Hedge]].
  - `Arbitration and law`: specifies the seat and governing law, most commonly London arbitration under English law (LMAA terms) or New York under the Society of Maritime Arbitrators.
- **Risk allocation principle:** in a voyage charter the owner bears the time and cost of the voyage and is compensated by a per tonne or [[Freight|Worldscale]] freight, with demurrage protecting the owner against charterer caused delay. In a time charter the charterer bears voyage time and cost (bunkers, port charges) and the owner is paid a daily hire, with off hire protecting the charterer against owner caused unavailability.
- **Hierarchy of terms:** typed rider clauses override the printed form; in conflict, specific overrides general, and a manuscript or typed amendment beats the standard printed wording.

## Prerequisites
- [[Time Charter]]
- [[Voyage Charter]]
- [[Laytime, Demurrage and Despatch]]
- [[Vessel Classes and Deadweight Tonnage]]
- [[Freight]]

## Related concepts (learn next)
- [[Laytime, Demurrage and Despatch]] is the single most disputed mechanic in any voyage charter party, so master its day counting next.
- [[Voyage Charter]] is the contract type the GENCON, ASBATANKVOY, and SHELLVOY forms govern, and where freight is paid per tonne.
- [[Time Charter]] is the contract type the NYPE and BALTIME forms govern, and where hire is paid per day.
- [[TC In and TC Out]] shows how a trader uses two charter parties back to back to capture a spread, with the clauses defining the risk in between.
- [[Ballast Leg Economics]] depends on charter party redelivery and delivery ranges, which fix where the unpaid repositioning leg starts and ends.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] matters because the bunker clause decides which party carries fuel price and quality risk.
- [[Forward Freight Agreement]] is the financial hedge layered on top of physical charter party exposure, and it settles against indices, not contracts.
- [[Baltic Exchange and the Dry Indices]] publishes the route assessments and standard vessel descriptions that charter party fixtures are benchmarked against.

## Common misconceptions

**"The freight rate is the deal."** The rate is one term in a contract of many. Demurrage rate, laytime allowance, off hire, safe port, and bunker clauses can move more money than the headline rate over the life of a fixture. A higher rate with charterer friendly laytime can be worse for the owner than a lower rate with tight laytime.

**"Standard forms are standard, so the wording is settled."** The printed form is a starting point. Almost every real fixture is heavily amended with rider clauses, and those typed amendments override the printed text. Two GENCON fixtures can allocate risk in opposite directions depending on their riders, which is exactly why the [[Laytime, Demurrage and Despatch|demurrage]] example above turns on one word.

**"The charter party and the bill of lading say the same thing."** They are different documents with different functions. The charter party governs the owner and charterer relationship; the bill of lading is the cargo receipt and document of title that can end up in a third party's hands. When their terms conflict, which one controls depends on incorporation clauses and who holds the bill, a frequent source of litigation.

**"Demurrage is a penalty."** Demurrage is liquidated damages, an agreed pre estimate of the owner's loss from delay, not a punitive charge. Because it is liquidated damages, the owner generally need not prove actual loss, and a court will not reduce it merely because the owner's real loss was smaller.

## Sources
- BIMCO, standard charter party forms and explanatory notes (GENCON 1994 and 2022, NYPE 2015, BALTIME, CONWARTIME)
- ASBA, ASBATANKVOY form; Shell, SHELLVOY 6 form documentation
- John Wilson, "Carriage of Goods by Sea"
- Julian Cooke et al., "Voyage Charters"; Terence Coghlin et al., "Time Charters"
- London Maritime Arbitrators Association (LMAA), terms and reported awards
- Baltic Exchange, route definitions and standard vessel descriptions
