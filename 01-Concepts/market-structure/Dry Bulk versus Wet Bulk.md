---
aliases: [dry bulk vs wet bulk, dry vs wet, bulkers vs tankers, dry cargo versus liquid cargo]
tags:
  - "#freight"
date-added: "2026-06-09"
---
# Dry Bulk versus Wet Bulk
## Definition
Ships move two broad kinds of unpackaged cargo. Dry bulk is solid stuff poured loose into a hold, like iron ore, coal, and wheat, carried on a bulk carrier whose hold is a giant open box. Wet bulk is liquid pumped through pipes into sealed tanks, like crude oil, gasoline, chemicals, and liquefied gas, carried on a tanker. The two cargoes need fundamentally different ships, different loading equipment, and different terminals, so the world splits into two separate freight markets that almost never overlap. A [[Capesize]] iron ore carrier physically cannot load crude oil, and a [[VLCC]] crude tanker cannot load grain, which is why a [[Freight]] trader treats dry and wet as distinct businesses with their own indices, demand drivers, and price cycles.

## Why it matters (commodities and FX)
A freight trader does not trade abstract shipping. They trade a specific cargo on a specific ship type, and the choice of dry versus wet decides which fundamentals matter. Dry bulk demand tracks steel production, power generation, and the grain harvest, so a dry trader watches Chinese iron ore restocking, monsoon driven Indian coal burn, and Brazilian and Black Sea grain exports. Wet bulk demand tracks oil consumption, refinery runs, and the structure of the oil [[Forward Curve]], so a wet trader watches OPEC output, refinery margins, and whether [[Contango]] is wide enough to trigger [[Floating Storage]]. Because the markets are mechanically separate, freight rates can diverge sharply: dry can be in a boom while tankers collapse, or the reverse, which means cross hedging dry exposure with a wet instrument carries large [[Basis Risk]]. Knowing which world you are in tells you which index, which [[Forward Freight Agreement]], and which seasonal pattern applies.

## Concrete example
**Concrete:** Compare two voyages running in the same week. A [[Capesize]] of 180,000 [[Vessel Classes and Deadweight Tonnage|dwt]] loads 170,000 tonnes of iron ore at Port Hedland in Western Australia bound for Qingdao in China, the [[Baltic Route Codes|C5]] route, with the rate quoted in dollars per tonne. Suppose C5 prints 9.50 dollars per tonne. Gross freight is 170,000 times 9.50, or 1,615,000 dollars for the voyage. Separately, a [[VLCC]] of 300,000 dwt loads 270,000 tonnes, roughly 2,000,000 barrels, of crude at Ras Tanura in Saudi Arabia bound for Ningbo, the TD3C route, quoted in [[Freight|Worldscale]] points that convert to a dollar per tonne rate. Suppose TD3C works out to a [[Time Charter|time charter equivalent]] of 45,000 dollars per day on a 40 day round voyage.

If the dry trade WORKS: Chinese mills restock aggressively, C5 spikes to 14.00 dollars per tonne, and an owner who fixed a string of Capesizes earlier at lower levels, or who is long the C5 [[Forward Freight Agreement]], captures the move. The same week, tankers can be flat or falling because oil demand is soft, so the dry position is the entire story and the wet market is irrelevant noise. If the dry trade FAILS: a cyclone shuts Port Hedland, Australian iron ore exports stall, C5 collapses to 6.00 dollars per tonne, and the long FFA position bleeds about 8.00 dollars per tonne, or roughly 1,360,000 dollars on a single cargo equivalent, while the VLCC owner next door is completely unaffected because crude flows out of the Arabian Gulf on its own schedule. The lesson: the two markets did not move together, so a dry loss could not be cushioned by a wet position.

**Simplified:** Iron ore on a giant box ship and crude oil on a giant tank ship are two different businesses. When steel demand jumps, the box ship business booms while the tank ship business may not move at all, and the reverse can happen too. You cannot use one to protect the other.

## Key mechanics and formulas
- Cargo handling: dry bulk loads by conveyor, grab, or chute and discharges by grab crane or self unloader. Wet bulk loads and discharges through cargo pumps and pipeline manifolds, with [[Wet Tanker Classes|crude tankers]] and product tankers kept apart by coating and cleaning needs.
- Vessel design split: bulk carriers have open box holds with hatch covers. Tankers have segregated tanks, inert gas systems, and pump rooms. Neither can carry the other cargo, which is the structural reason the markets are separate. See [[Vessel Classes and Deadweight Tonnage]] and [[Wet Tanker Classes]].
- Index worlds, all published by the [[Baltic Exchange and the Dry Indices]]:
  - Dry: the Baltic Dry Index BDI, built from the [[Capesize]], [[Panamax]], [[Supramax]], and [[Handysize]] sub indices.
  - Wet dirty: the Baltic Dirty Tanker Index BDTI, for unrefined crude carried on [[VLCC]], [[Suezmax]], and [[Aframax]] tonnage.
  - Wet clean: the Baltic Clean Tanker Index BCTI, for refined products like gasoline and diesel on smaller coated tankers.
- Rate conventions: dry bulk [[Voyage Charter]] rates quote in `USD per tonne`. Tanker voyage rates quote in [[Freight|Worldscale]] points off a flat rate, then convert to a [[Time Charter|TCE]] in `USD per day`. TCE bridges the two: `TCE = (voyage revenue - voyage costs) / voyage days`, where voyage revenue is gross freight, voyage costs are mainly bunkers and port charges, and voyage days include the laden and [[Ballast Leg Economics|ballast]] legs.
- Demand driver mapping:
  - Dry: `dry demand proxy = steel output + thermal coal burn + grain trade`, all in tonne miles.
  - Wet: `wet demand proxy = oil consumption + refinery throughput + storage arbitrage`, where the storage term grows when [[Contango]] is wide.
- Tonne mile, the core volume metric for both worlds: `tonne miles = cargo tonnes * distance sailed`. Long haul reroutes raise tonne miles and tighten the market even if cargo tonnes are flat.

## Prerequisites
- [[Freight]]
- [[Vessel Classes and Deadweight Tonnage]]
- [[Voyage Charter]]
- [[Time Charter]]

## Related concepts (learn next)
- [[Wet Tanker Classes]] because the wet world divides further into crude and clean tankers, each with its own index and cleaning rules.
- [[Baltic Exchange and the Dry Indices]] because it publishes the BDI, BDTI, and BCTI that quantify each market separately.
- [[Baltic Route Codes]] because rates are quoted route by route, like C5 for dry ore and TD3C for crude, and you must speak this code language.
- [[Forward Freight Agreement]] because hedging dry and wet exposure uses separate FFA contracts with no fungibility between them.
- [[Ballast Leg Economics]] because the empty return leg drives the real economics differently for a backhauling bulker versus a tanker.
- [[Floating Storage]] because deep [[Contango]] in oil is a uniquely wet bulk demand shock that has no clean dry equivalent.
- [[Seasonality]] because dry follows the grain harvest and winter coal burn while wet follows the oil refining and heating cycle, so the calendars differ.
- [[Basis Risk]] because trying to hedge a dry position with a wet instrument exposes you to the divergence between the two markets.

## Common misconceptions
- **"Freight is one market, so if shipping rates are strong everything is strong."** Wrong. Dry and wet are mechanically separate fleets serving different commodities. The BDI can triple while the BDTI sinks, because steel restocking and oil demand are unrelated forces. Treating freight as a single asset hides which fundamental is actually driving your position.
- **"A big bulk carrier and a big tanker are basically the same ship and could swap cargoes in a pinch."** Wrong. A bulk carrier has open dry holds and grab cranes, while a tanker has sealed tanks, cargo pumps, and inert gas systems. Conversion is a shipyard rebuild, not a switch, so capacity does not flow between the two markets to arbitrage rate gaps.
- **"Tanker rates and dry rates are quoted the same way, so I can compare them directly."** Wrong. Dry quotes in dollars per tonne while tankers quote in [[Freight|Worldscale]] points off a flat rate. You must convert both to a [[Time Charter|TCE]] in dollars per day before any comparison is meaningful.
- **"Clean and dirty tankers are just a labeling formality."** Wrong. Dirty carries crude and fuel oil, clean carries refined products that contaminate easily, so the ships are coated and cleaned differently and price off separate indices, the BDTI versus the BCTI.

## Sources
- Baltic Exchange, Guide to Market Benchmarks, descriptions of the BDI, BDTI, and BCTI route baskets. https://www.balticexchange.com
- Martin Stopford, Maritime Economics, 3rd edition, chapters on the dry bulk and tanker markets and fleet segmentation.
- Clarksons Research, Shipping Intelligence Network, dry bulk and tanker trade and tonne mile data. https://www.clarksons.net
- Manolis Kavussanos and Ilias Visvikis, The International Handbook of Shipping Finance, on freight rate formation and FFA markets.
