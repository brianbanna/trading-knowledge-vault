---
aliases: [dwt, deadweight tonnage, dry bulk vessel classes, handysize, supramax, ultramax, panamax, kamsarmax, capesize, newcastlemax, vloc, bulker sizes]
tags:
  - "#freight/dry"
date-added: "2026-06-09"
---

# Vessel Classes and Deadweight Tonnage

## Definition
Deadweight tonnage, written dwt, is the total weight a ship can carry when fully loaded: cargo plus fuel, fresh water, crew, stores and ballast. Think of it as the maximum payload of the truck, measured in tonnes, not the weight of the empty truck itself. Dry bulk ships, the vessels that haul loose unpackaged cargo like iron ore, coal and grain, come in standard size bands, and each band has a name. The name tells everyone in the market roughly how big the ship is and therefore which cargoes and which ports it can serve. The ladder runs from the small [[Handysize]] up through Supramax, Ultramax, Panamax, Kamsarmax, Capesize, Newcastlemax and finally the giant VLOC. A trader who hears Capesize immediately knows the ship carries roughly 180,000 tonnes, cannot fit through the Panama or Suez canals, and is built for the iron ore and coal trades.

## Why it matters (commodities and FX)
Vessel class is the first thing a freight, [[Dry Bulk versus Wet Bulk|dry bulk]] or commodity trader checks because it decides the entire economics of moving a cargo. The Baltic indices that price [[Freight]] are quoted per class, so the [[Baltic Exchange and the Dry Indices|BCI]] tracks Capesize and the [[Baltic Exchange and the Dry Indices|BPI]] tracks Panamax, and a [[Forward Freight Agreement]] settles against a specific class. If you trade iron ore Brazil to China you live and die by the Capesize market, while if you trade Black Sea grain you watch Supramax and Panamax. Choosing the wrong class for a cargo or a berth turns a profitable [[Voyage Charter]] into a loss, because a ship too large for the port cannot fully load and a ship too small wastes the per tonne efficiency of scale. The class also determines what routes are physically open, which feeds directly into [[Ballast Leg Economics]] and the geography of the [[Baltic Route Codes]].

## Concrete example
**Concrete:** A trader fixes a Capesize, say 180,000 dwt, to lift iron ore from Tubarao in Brazil to Qingdao in China, a [[Baltic Route Codes|C3]] cargo. The vessel loads roughly 180,000 tonnes of ore. At a freight rate of 22 USD per tonne the voyage grosses 180,000 times 22, about 3.96 million USD, and after bunkers, port costs and canal avoidance the owner clears a healthy daily [[Time Charter|TCE]]. Now run the failure case. The same trader instead nominates a Capesize to a grain berth at a river port with a maximum draft of 11 metres and a 65,000 dwt length limit. The Capesize cannot enter at all, or can only part load to honour the draft, so it lifts perhaps 90,000 tonnes instead of 180,000. The trader now pays for a 180,000 dwt ship to move a Panamax sized parcel, the per tonne cost roughly doubles, and the laden vessel may incur [[Laytime, Demurrage and Despatch|demurrage]] waiting for tide windows. The voyage that looked profitable on a spreadsheet loses money once the wrong hull touches the wrong port.

**Simplified:** Every ship size has cargoes and ports it fits and ones it does not. Match the hull to the job and you make money. Send a giant ship to a small dock and it cannot load full, so you pay big ship costs to move small ship volume and the trade goes underwater.

## Key mechanics and formulas
- `dwt = lightship displacement subtracted from loaded displacement` where lightship is the empty steel weight and loaded displacement is the weight of water the fully loaded hull pushes aside. dwt is the carrying capacity, not the cargo weight alone.
- `cargo capacity = dwt minus bunkers minus fresh water minus stores minus constant`. On a long voyage with full fuel tanks, usable cargo can sit several thousand tonnes below the headline dwt.
- Draft is how deep the hull sits in the water when loaded. A port with a 12 metre draft limit caps how much a ship can load regardless of its dwt. `permissible cargo at port = function of available draft`.
- Air draft is the height from the waterline to the highest fixed point, the mast or radar. It governs whether a ship clears bridges and loading gantries.
- Geared means the ship carries its own cranes and can self load and discharge at ports with no shore equipment. Gearless ships need port infrastructure. [[Handysize]], Supramax and Ultramax are typically geared; Panamax and above are usually gearless.
- The dry bulk ladder, approximate bands:
  - [[Handysize]]: about 10,000 to 40,000 dwt. Geared, flexible, carries minor bulks like cement, fertiliser, steel and sugar into smaller ports.
  - Supramax and Ultramax: about 40,000 to 65,000 dwt. Geared. Workhorses for grains and minor bulks. Ultramax is the modern, slightly larger and more efficient version of Supramax.
  - Panamax and Kamsarmax: about 65,000 to 85,000 dwt. Coal and grains. Panamax beam was historically capped near 32.2 metres by the old Panama Canal locks. Kamsarmax is sized to the maximum length, about 229 metres, that loads at the bauxite port of Kamsar in Guinea.
  - Capesize: about 100,000 to 200,000 dwt. Iron ore and coal. Too large for the old Panama and often for Suez at full load, so it rounds the Cape of Good Hope and Cape Horn, hence the name.
  - Newcastlemax: about 185,000 dwt, the largest beam, around 50 metres, that fits the coal port of Newcastle, Australia.
  - VLOC, Very Large Ore Carrier: about 200,000 to 400,000 dwt, dedicated mega ships for the iron ore trade, mostly Brazil and West Africa to Asia.
- Rule of scale: larger ships move cargo at lower cost per tonne but only on deep water routes and large ports. The optimisation is to pick the largest class the route and berth can fully accommodate.

## Prerequisites
- [[Dry Bulk versus Wet Bulk]]
- [[Freight]]

## Related concepts (learn next)
- [[Wet Tanker Classes]] because the tanker ladder, VLCC down to Handy, mirrors this dry bulk ladder for liquid cargoes.
- [[Baltic Exchange and the Dry Indices]] because freight is priced per vessel class, so you must map classes to the BCI, BPI, BSI and BHSI.
- [[Baltic Route Codes]] because each class trades on named routes like C3 or P2A that define where it earns.
- [[Voyage Charter]] because mis sizing a vessel to a route shows up directly in voyage profit and loss.
- [[Ballast Leg Economics]] because a class determines which return legs are loaded and which run empty.
- [[Forward Freight Agreement]] because FFAs are written on a specific class, so you hedge Capesize risk with Capesize paper.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] because fuel burn scales with hull size and eats into usable cargo capacity.
- [[Port Congestion and Waiting Time]] because draft limits and berth size by class drive where ships queue.

## Common misconceptions
- **"Deadweight tonnage is the weight of the ship."** Wrong. dwt is carrying capacity, the maximum payload, not the steel weight of the vessel. The empty weight is lightship, and the loaded weight of water displaced is displacement. dwt is the difference between loaded and empty.
- **"A 180,000 dwt Capesize always loads 180,000 tonnes of cargo."** Wrong. dwt includes bunkers, fresh water, stores and constants. On a long laden voyage the usable cargo sits below the headline number, and port draft limits can cut it further.
- **"Bigger is always cheaper, so use the largest ship available."** Wrong only in part. Larger ships cut cost per tonne but only when the route is deep enough and the berth can fully load them. A Capesize that can only part load at a draft restricted port is more expensive per tonne than a correctly sized Panamax.
- **"The class names describe the cargo."** Wrong. The names describe physical size and canal or port constraints, not cargo. Panamax is sized to the old Panama locks, Kamsarmax to the port of Kamsar, Newcastlemax to the port of Newcastle. The cargo carried follows from the size, not the other way around.

## Sources
- Baltic Exchange, Guide to Market Benchmarks and route definitions, balticexchange.com
- Martin Stopford, Maritime Economics, 3rd edition, chapters on ship types and the cost of shipping
- Clarksons Research, World Fleet Register and Shipping Intelligence Network, vessel size definitions
- Drewry and Lloyd's List, vessel classification references for dry bulk carriers
- BIMCO, ship type and tonnage explanatory notes, bimco.org
