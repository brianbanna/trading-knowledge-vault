---
aliases: [port congestion, vessel queues, waiting time, ships at anchor, port queues, congestion]
tags:
  - "#freight/dry"
date-added: "2026-06-09"
---
# Port Congestion and Waiting Time

## Definition
Port congestion is what happens when more ships show up to load or discharge cargo than the port can handle at once, so vessels sit at anchor waiting for a berth. Picture a busy restaurant with a long line out the door. The kitchen capacity is fixed, so the line grows and everyone waits longer. A ship stuck in that line is doing nothing useful, yet it is still committed to that port and cannot carry cargo anywhere else. Technically, congestion is measured by the number of vessels at anchor at a given port and by waiting days, the time between a ship arriving and getting alongside the berth. Because a queuing ship is removed from the pool of ships actually available to move cargo, congestion reduces effective fleet supply even though no ship is scrapped and no new ship is built.

## Why it matters (commodities and FX)
A freight trader cares about congestion because it is one of the fastest ways the market can tighten or loosen without the physical fleet changing size. The number of vessels in existence is nearly fixed over weeks and months, since newbuildings take 2 years to deliver and scrapping is slow. Congestion is the lever that moves on a daily timescale. When 30 ships are stuck at anchor off a discharge port, those 30 ships are not competing for the next cargo, so the spot market for that vessel class tightens and rates jump. When the queue clears, that tonnage floods back into the spot pool and rates soften. A trader who tracks anchorage counts and waiting days at key load and discharge ports can anticipate moves in the [[Baltic Exchange and the Dry Indices]] before they fully show up in the published assessments. Congestion also feeds directly into [[Laytime, Demurrage and Despatch]], since time spent waiting often counts as laytime and can put a ship on demurrage, which is real cash to whoever holds the charter.

## Concrete example
**Concrete:** In late 2021 Chinese coal import ports such as Caofeidian and the Bohai Rim terminals built large anchorage queues as power demand surged and discharge slowed. Assume 30 [[Vessel Classes and Deadweight Tonnage]] Capesize vessels, each around 180,000 dwt, are sitting at anchor off North China waiting to discharge coal and iron ore, with average waiting days running near 10. Those 30 Capes represent roughly 5.4 million dwt that the market thinks exists but that cannot take a new cargo. Suppose you are long freight via a [[Forward Freight Agreement]] on the Capesize C5 west Australia to Qingdao iron ore route, or simply running [[TC In and TC Out]] with ships chartered in at 20,000 USD per day. Effective Capesize supply has dropped, the Baltic C5 assessment climbs from say 10 USD per tonne toward 14 USD per tonne, and the time charter equivalent on your relets pushes from 20,000 USD per day toward 35,000 USD per day. If congestion holds, your FFA position pays and your chartered in ships earn far above their cost: the trade WORKS. Now the FAILURE path. Beijing pushes the ports to clear the backlog, weather improves, and over 3 weeks the 30 ship queue drains to 5. Those 25 freed Capes re-enter the spot pool all at once, effective supply jumps, C5 collapses back toward 9 USD per tonne, and your long FFA bleeds while your chartered in ships now earn less than the 20,000 USD per day you committed to pay. You lose on both legs at once.

**Simplified:** Ships stuck waiting in line cannot carry cargo, so the usable fleet shrinks and prices to hire ships go up. When the line clears, all those ships come back at once, the usable fleet grows, and prices fall. Bet on rates going up while the line is long, and you make money if the line stays long and lose money if it clears.

## Key mechanics and formulas
- Effective supply intuition: `effective fleet = total fleet - tonnage tied up in congestion`. The published fleet size barely moves week to week, so congestion is the swing factor in usable supply.
- Congestion share: `congestion share = vessels at anchor / total vessels in that trade`. A jump from 5 percent to 15 percent of a vessel class sitting idle at anchor is a large tightening even with zero change in fleet count.
- Waiting days: `waiting days = berth date - arrival date`. Multiply across the queue to get tonne days removed: `tonne days lost = sum over waiting ships of (dwt * waiting days)`.
- Speed link: when rates are high, ships sail faster to grab the next fixture, which paradoxically delivers tonnage to load ports sooner and can build congestion there. When rates are low, slow steaming spreads arrivals out.
- Laytime link: waiting at anchor before a berth is free often counts against laytime depending on the [[Charter Party]] clause (for example whether the notice of readiness can be tendered at anchorage). Excess waiting puts the ship on demurrage. See [[Laytime, Demurrage and Despatch]].
- Common triggers: weather closures and storms, port labor strikes, customs or quarantine holds (COVID 2021 protocols were a major driver), record cargo volumes outrunning berth capacity, and ice in high latitude ports seasonally. See [[Seasonality]].
- Data sources: AIS based vessel tracking gives near real time anchorage counts. Traders watch these daily as a leading indicator for the [[Baltic Exchange and the Dry Indices]].

## Prerequisites
- [[Vessel Classes and Deadweight Tonnage]]
- [[Freight]]
- [[Laytime, Demurrage and Despatch]]
- [[Charter Party]]

## Related concepts (learn next)
- [[Baltic Exchange and the Dry Indices]] because anchorage data is a leading signal for the dry indices, and congestion is one of the cleanest ways to read where the indices go next.
- [[Laytime, Demurrage and Despatch]] because waiting time at congested ports converts directly into demurrage liability or despatch credit.
- [[Forward Freight Agreement]] because FFAs are the main instrument to trade a congestion driven view on spot rates without owning a ship.
- [[Ballast Leg Economics]] because deciding whether to ballast toward a congested but high paying region depends on expected waiting days.
- [[Port Congestion and Waiting Time]] feeds [[Floating Storage]] because vessels held at anchor with cargo onboard blur the line between congestion and deliberate storage.
- [[Seasonality]] because monsoon, ice, and harvest cycles produce predictable congestion windows worth front running.
- [[Voyage Charter]] because under a voyage charter the owner bears most of the congestion risk through laytime and demurrage terms.
- [[Time Charter]] because under a time charter the charterer pays for the ship every waiting day, so congestion risk sits with the charterer.

## Common misconceptions
- **"Congestion only matters at the discharge port."** Wrong. Load port queues are just as important. Ships waiting to load at Australian or Brazilian iron ore terminals, or at US Gulf and Brazilian grain berths, are removed from supply exactly the same way, and load side congestion delays the start of revenue earning voyages.
- **"If the fleet has not changed, supply has not changed."** Wrong. Effective supply is the tonnage actually free to take cargo, not the total tonnage in existence. Congestion can pull 10 percent or more of a vessel class out of the usable pool while the official fleet count is flat, which is exactly why rates can spike without any newbuilding or scrapping.
- **"Clearing congestion is bullish because trade is flowing again."** Wrong for freight rates. Clearing a queue dumps idle tonnage back into the spot market all at once, raising effective supply and pushing rates down. What looks like good news for cargo flow is bearish for the people who hire ships out.
- **"Waiting time is dead time nobody pays for."** Wrong. Under most charter structures someone pays for every waiting day, the charterer under a [[Time Charter]] and often the charterer via demurrage under a [[Voyage Charter]]. See [[Laytime, Demurrage and Despatch]].

## Sources
- Baltic Exchange, guide to the dry freight indices and route definitions, balticexchange.com
- Martin Stopford, Maritime Economics, 3rd edition, chapters on the shipping market mechanism and supply and demand
- Clarksons Research, Shipping Intelligence Network, fleet and port congestion datasets
- AIS based congestion trackers, for example Kpler and MarineTraffic anchorage and waiting time data
- Reporting on the 2021 Chinese coal and iron ore port queues and COVID era quarantine driven congestion, Lloyd's List and TradeWinds
