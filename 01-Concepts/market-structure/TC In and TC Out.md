---
aliases: [tc in, tc out, tc in tc out, sublet spread, period position]
tags:
  - "#freight/contracts"
date-added: "2026-06-09"
---

# TC In and TC Out

## Definition
Think of an operator as a middleman who rents a ship from an owner, then re-rents that same ship or uses it to carry cargo for someone else, pocketing the difference. Taking a vessel in on a [[Time Charter]] is called TC in. Putting it back out on charter, or running it on the spot and paper market, is called TC out. The operator does not own steel. They hold a position on the price of freight by controlling the use of a ship for a fixed window. TC in fixes the cost side at a known daily rate, and TC out, spot voyages, or [[Forward Freight Agreement]] cover fix the revenue side. The gap between what they pay to take the ship in and what they earn from putting it out is their margin.

## Why it matters (commodities and FX)
This is the core mechanism by which dry bulk and tanker operators make money without capital tied up in vessels. A freight trader who believes rates will rise can lock in cheap input cost today by TC in for a period, then earn the rising spot or higher TC out rate later. The position is directional on [[Freight]] just like a futures position is directional on a commodity. It also lets a desk arbitrage the difference between the period market and the spot market, the so called sublet spread. Understanding TC in versus TC out tells you whether a counterparty is long or short freight duration, which drives how they bid for cargo, how aggressively they fix, and where their risk sits if the [[Forward Curve]] moves.

## Concrete example
**Concrete:** An operator takes a [[Vessel Classes and Deadweight Tonnage|Supramax]] (around 58,000 dwt) in on a 6 month [[Time Charter]] at 12,000 USD per day, paid to the owner. This is the TC in leg and the cost is now fixed for roughly 180 days, about 2.16 million USD total before bunkers and commissions. The operator is now long freight: they profit if the market rises.
- Case it works: 2 months in, the Supramax market firms and period rates climb to 16,000 USD per day. The operator TC outs the vessel for the remaining 4 months at 16,000 USD per day. They collect 16,000 and pay 12,000, a sublet spread of 4,000 USD per day across about 120 days, roughly 480,000 USD gross before commission. Alternatively they keep running [[Voyage Charter|voyages]] and the higher [[Baltic Exchange and the Dry Indices|index]] earnings flow straight to them.
- Case it fails: instead the market sags and the [[Baltic Route Codes|S10 backhaul]] and headhaul routes collapse. Period TC out rates fall to 9,000 USD per day. The operator still owes the owner 12,000 USD per day but can only re lease or run the ship at 9,000. They bleed 3,000 USD per day for the remaining 120 days, roughly 360,000 USD of loss, plus any [[Ballast Leg Economics|ballast]] and idle exposure if they cannot keep her employed at all.

**Simplified:** You rent a truck for 6 months at a fixed daily price hoping you can rent it back out or use it for more than you paid. If demand for trucks jumps you win the difference. If demand crashes you are stuck paying the high rent while only earning low rent back.

## Key mechanics and formulas
- Sublet or period spread per day: `spread = TC_out_rate - TC_in_rate` where `TC_in_rate` is what the operator pays the owner and `TC_out_rate` is what a sub charterer pays the operator, both in USD per day.
- Total period P&L: `pnl = (TC_out_rate - TC_in_rate) * charter_days - commissions - off_hire_cost` where `charter_days` is days the vessel is actually on hire and `off_hire_cost` covers idle or breakdown days the operator eats.
- Long period position: TC in at a fixed rate while leaving the TC out or spot side open. You profit if [[Freight]] rises above your in rate. This is the synthetic equivalent of buying a [[Forward Freight Agreement]].
- Short period position: TC out at a fixed rate while sourcing tonnage on shorter spot fixtures. You profit if the market falls below your out rate, mirroring a short FFA.
- Relet: when the TC out is on the identical vessel you took in, the operator never carries cargo themselves and is purely playing the spread.
- The physical period position carries operational risk (off hire, [[Port Congestion and Waiting Time|congestion]], bunker spikes) that the paper [[Forward Freight Agreement]] does not, but TC in gives you actual control of the asset.

## Prerequisites
- [[Time Charter]]
- [[Voyage Charter]]
- [[Freight]]
- [[Vessel Classes and Deadweight Tonnage]]
- [[Charter Party]]

## Related concepts (learn next)
- [[Forward Freight Agreement]] the cash settled paper way to take the same long or short freight view without taking a ship in.
- [[Ballast Leg Economics]] because an open TC out position forces decisions on where to reposition the vessel between fixtures.
- [[Baltic Exchange and the Dry Indices]] which sets the reference rates a TC out or relet is priced against.
- [[Baltic Route Codes]] since period rates are derived from route baskets you need to read to value a position.
- [[Freight Options]] the optional version that caps downside on a period position for a premium.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] because fuel cost sits between the TC in and the voyages you run on TC out.
- [[Laytime, Demurrage and Despatch]] which determines extra earnings or costs when you run voyages on a chartered in ship.
- [[Basis Risk]] the gap between your physical TC position and any paper hedge used against it.
- [[Relet]] the operator strategy of taking a ship in on TC and employing it out on voyages to capture the spread.
- [[Market Hire]] the prevailing daily rate you mark an open period position against.
- [[Physical vs Paper Freight]] because the TC book is the physical leg traded against paper FFA positions.

## Common misconceptions
- **"TC in means the operator owns the ship."** Wrong. TC in is renting the vessel from an owner for a period under a [[Time Charter]]. The operator controls the ship's employment but the owner keeps title, crews her, and maintains her. The operator is buying time, not steel.
- **"The sublet spread is risk free arbitrage."** Wrong. The TC in leg is a fixed cost but the TC out or spot leg is open market exposure. If rates fall the operator pays the high in rate and earns the low out rate, a real and sometimes large loss, as the 9,000 USD case shows.
- **"TC in and TC out always involve different vessels."** Wrong. In a relet the operator takes a specific ship in and immediately puts that same ship out, capturing only the rate difference and never touching cargo.
- **"A physical period position and an [[Forward Freight Agreement]] are interchangeable."** Wrong. The FFA is cash settled against an index with no operational duties. The physical TC in carries off hire, bunker, and [[Port Congestion and Waiting Time|congestion]] risk plus the obligation to keep the ship working.

## Sources
- Baltic Exchange, Guide to Market Benchmarks and the Dry and Tanker indices, https://www.balticexchange.com
- Martin Stopford, Maritime Economics, 3rd edition, Routledge, chapters on the charter market and freight market cycles
- Manolis Kavussanos and Ilias Visvikis, The International Handbook of Shipping Finance, sections on period chartering and freight derivatives
- Clarksons Shipping Intelligence Network, period and spot rate reporting, https://www.clarksons.net
- FIS and SSY broker primers on period positions, reletting, and sublet economics
