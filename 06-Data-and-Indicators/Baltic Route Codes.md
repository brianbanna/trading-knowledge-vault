---
aliases: [baltic routes, route codes, c3, c5, p1a, p2a, p3a, baltic dry routes]
tags:
  - "#freight/routes"
date-added: "2026-06-09"
---
# Baltic Route Codes
## Definition
A Baltic route code is a short label, like C3 or P2A, that names one specific, standardised dry bulk shipping job. Each code fixes the cargo type, the vessel size, the load port and the discharge port, so that everyone in the market is pricing the exact same voyage. Think of it like a flight number: BA117 always means the same airline flying the same airports, so two people can compare its price without confusion. The [[Baltic Exchange and the Dry Indices]] publishes a daily price for each route, gathered from a panel of shipbroker submissions and averaged. These route prices are the raw ingredients that get bundled into the sub indices such as the Capesize, Panamax and Supramax indices.
## Why it matters (commodities and FX)
Route codes are the language a freight trader speaks. When you trade a [[Forward Freight Agreement]] you are not trading some vague notion of [[Freight]], you are trading a named route like C5 or the basket that underlies an index. The settlement price of your FFA is the published assessment of that exact route or index, so knowing precisely which ports and cargo each code covers is the difference between a clean hedge and unwanted [[Basis Risk]]. A trader who is long iron ore freight out of West Australia hedges with C5, not C3, because C3 prices a Brazil to China voyage with a much longer distance and different [[Ballast Leg Economics]]. Route codes also tell you where physical pressure is building: if the Pacific Panamax round P3A spikes while the transatlantic P1A stays flat, the tightness is regional, which informs how you position across the [[Forward Curve]].
## Concrete example
**Concrete:** Suppose you trade Capesize iron ore freight. The headline Capesize route is C5, West Australia (Port Hedland) to Qingdao China, assessed in USD per tonne. On a normal day 5 broker panellists submit assessments for C5: 10.50, 10.40, 10.60, 10.50, 10.50 USD per tonne. The Baltic averages these to 10.50 USD per tonne. You hold a long FFA position on C5 at 9.80 struck last month, so at 10.50 you are 0.70 USD per tonne in profit on, say, 150,000 tonnes per lot, roughly 105,000 USD per lot. Now Port Hedland hits heavy [[Port Congestion and Waiting Time]] after a cyclone warning. Ships queue, owners demand more to commit tonnage, and the next day panellists submit 12.80, 13.10, 12.90, 13.00, 13.20. The average jumps to 13.00 USD per tonne. The single congested load port has moved the whole C5 assessment up 2.50 USD per tonne, and your long position gains another 2.50 times 150,000, about 375,000 USD per lot. If instead you had been short C5 expecting a quiet market, that same congestion driven spike works against you and you lose roughly 480,000 USD per lot versus your 9.80 entry. The lesson: a route assessment is only as stable as the load port behind it, and one bottleneck reprices the entire benchmark.
**Simplified:** C5 is just a fixed shipping job from Australia to China, priced each day by averaging what 5 brokers say it costs. If the Australian loading port jams up, every broker raises their price, the average leaps, and anyone betting on that route wins or loses big depending on which side they took.
## Key mechanics and formulas
- Code structure: a letter denotes the vessel series, a number denotes the specific route. C series is [[Vessel Classes and Deadweight Tonnage|Capesize]], P series is Panamax, S series is Supramax, with a sometimes used for Handysize.
- Capesize C series examples: `C3` Tubarao Brazil to Qingdao China (iron ore, assessed USD per tonne), `C5` West Australia to Qingdao China (iron ore, USD per tonne). Both are voyage routes, so the price is per tonne of cargo carried.
- Panamax P series examples: `P1A` transatlantic round voyage, `P2A` Skaw Gibraltar to Far East trip (fronthaul), `P3A` transpacific round voyage. These are trip charter routes, assessed in USD per day [[Time Charter|TCE]], not per tonne.
- Supramax S series examples: `S1B`, `S4A`, `S4B` and similar trip charter routes, also assessed in USD per day TCE.
- Assessment method: each business day a panel of accredited shipbrokers submits a price for every route based on actual fixtures and their market read. The Baltic removes the panel anonymity rules aside and computes a simple average.
- Route average: `route_assessment = (sum of panellist submissions) / (number of panellists)`. Where assessment is the published daily figure, submissions are each broker's price, and panellists is the count of submitting brokers.
- Sub index aggregation: `sub_index = sum over routes of (route_assessment_in_index_units times route_weight)`. Where route_weight is the fixed percentage the Baltic assigns each route inside that index, summing to 100 percent. The Capesize, Panamax and Supramax sub indices feed the [[Baltic Exchange and the Dry Indices|Baltic Dry Index]].
- Units convention: voyage routes (most C routes) are USD per tonne. Trip charter routes (most P and S routes) are USD per day TCE. The Baltic converts voyage routes into a TCE equivalent before blending them into a TCE based index.
## Prerequisites
- [[Baltic Exchange and the Dry Indices]]
- [[Vessel Classes and Deadweight Tonnage]]
- [[Voyage Charter]]
- [[Time Charter]]
- [[Freight]]
## Related concepts (learn next)
- [[Forward Freight Agreement]] because FFAs settle against these exact route and index assessments, so the codes define what you are actually trading.
- [[Freight Options]] because options on freight reference the same Baltic route benchmarks for their underlying.
- [[Ballast Leg Economics]] because the distance and positioning baked into each route, like C3 versus C5, drives why two codes price so differently.
- [[Port Congestion and Waiting Time]] because load and discharge port delays are the single biggest mover of a route assessment.
- [[Basis Risk]] because hedging with the wrong route code leaves a gap between your physical exposure and your paper position.
- [[TC In and TC Out]] because trip charter routes are quoted in TCE, the same metric you compare when chartering vessels in and out.
- [[Forward Curve]] because each route has its own forward strip, and divergence across routes signals regional supply and demand shifts.
- [[Dry Bulk versus Wet Bulk]] because Baltic dry route codes cover dry cargoes only, while wet tanker benchmarks use a separate quoting system.
## Common misconceptions
- **"C3 and C5 are basically the same Capesize iron ore route so I can hedge either with the other."** Wrong. C3 is Brazil to China, a voyage of roughly 11,000 nautical miles, while C5 is West Australia to China at roughly 3,500 nautical miles. The far longer C3 voyage carries different bunker exposure, ballast positioning and time at sea, so the two routes can move in opposite directions. Hedging Australian ore exposure with C3 creates large [[Basis Risk]].
- **"All Baltic routes are priced in dollars per tonne."** Wrong. Only voyage routes, mostly in the C series, are USD per tonne. Most Panamax and Supramax trip charter routes are quoted in USD per day TCE, a daily hire equivalent. Mixing the two units when sizing a hedge produces a position off by orders of magnitude.
- **"The route price is set by an exchange ticker like a stock."** Wrong. There is no continuous traded tape. The price is a once daily average of subjective broker submissions based on observed fixtures and judgement, which is why a thin trading day or one disruptive fixture can swing the published number sharply.
- **"More panellists always means a more accurate route average."** Wrong. The average is only as good as the quality and independence of submissions. A few panellists all reacting to the same single congested fixture can drag the average even with a large panel, because the simple mean gives every submission equal weight.
## Sources
- Baltic Exchange, "Guide to Market Benchmarks" and the manuals for the Capesize, Panamax and Supramax indices, balticexchange.com
- Baltic Exchange route definitions and vessel descriptions, the official list of route codes and their port pairs
- Alizadeh and Nomikos, "Shipping Derivatives and Risk Management", chapters on freight indices and route construction
- Stopford, "Maritime Economics", 3rd edition, sections on dry bulk markets and freight rate benchmarks
- Clarksons Shipping Intelligence Network, route level rate histories for cross checking Baltic assessments
