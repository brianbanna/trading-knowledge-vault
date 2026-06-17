---
aliases: [physical vs paper freight, paper freight, physical freight, steel vs paper, physical versus paper freight]
tags:
  - "#freight/ffa"
  - "#freight/contracts"
date-added: "2026-06-17"
---

# Physical vs Paper Freight

## Definition
There are 2 ways to take a position on freight. The first is to charter a real ship and move real cargo, which traders call "physical" or "steel" because there is actual steel floating on the water. The second is to buy or sell a freight derivative that never touches a vessel, which traders call "paper". Physical freight means signing a [[Voyage Charter]] (priced in USD per tonne, owner pays bunkers) or a [[Time Charter]] (priced in USD per day, charterer pays bunkers) and accepting every operational duty that comes with running a vessel: fueling, port time, congestion, off hire, laytime. Paper freight means trading a [[Forward Freight Agreement]] or [[Freight Options]] that cash settles against a published [[Baltic Exchange and the Dry Indices|Baltic]] index average, with no ship, no cargo, only daily margin and the final settlement difference. The two books express the same underlying view on rates but carry very different risk, capital, and operational profiles.

## Why it matters (commodities and FX)
A freight desk almost always runs both books at once and nets them against each other. Paper is the fast, liquid, standardized, capital light way to put on or hedge a directional view: you can sell a quarter of C5TC in minutes without owning anything. Physical gives you actual control of the asset, access to operational alpha (smart routing, ballast optimization, congestion plays), and the ability to capture the physical to paper basis, but it ties up working capital and exposes you to off hire, bunker swings, and counterparty performance. The decision between steel and paper is the core capital allocation question on a freight desk. Crucially, the published index almost never equals the rate you actually fixed, so any physical position hedged with paper leaves a residual gap. That gap is the physical to paper [[Basis]], and managing it is its own discipline (see [[Freight Basis Risk]]).

## Concrete example
A trader takes a Capesize on a 1 year [[Time Charter]] at USD 22,000 per day (a TC in position, see [[TC In and TC Out]]). They are now structurally long physical freight: if Capesize rates fall, the daily hire they committed to looks expensive relative to the market. To hedge, they sell the paper, going short C5TC [[Forward Freight Agreement]] contracts at USD 23,500 per day for the matching period. The synthetic logic: TC in equals long FFA, so to flatten the directional view you short FFA.

**Concrete:** Say the trader hedges 30 days of exposure by selling 30 lots of C5TC at USD 23,500 per day (each FFA lot is 1 day of the index). The market then falls. The C5TC settlement average for the period prints USD 19,000 per day. Paper P&L on the short: `(23,500 - 19,000) * 30 = USD 135,000` gain. Now the physical. The trader re lets the vessel into the spot market (see [[Relet]]) and achieves a realized [[Time Charter Equivalent|TCE]] of USD 18,200 per day against their USD 22,000 hire cost, a loss of `(18,200 - 22,000) * 30 = USD 114,000` on the steel. Net across both books: `+135,000 - 114,000 = +USD 21,000`. The hedge offset most of the move but not all of it. The physical realized 18,200 while the index settled at 19,000, an 800 per day gap. That USD 800 per day times 30 equals USD 24,000 of unhedged slippage, the [[Freight Basis Risk]]. Add a 5 day off hire event for engine repair where hire is suspended but the paper keeps settling, and the books diverge further: the paper hedge has no concept of your ship breaking down. If instead the market had rallied to USD 26,000, the short paper would lose `(23,500 - 26,000) * 30 = -USD 75,000` while the physical relet at, say, USD 25,300 TCE would gain `(25,300 - 22,000) * 30 = +USD 99,000`, net `+USD 24,000`. Either direction, the paper caps the directional swing and the residual is basis plus operational items.

**Simplified:** You rented a ship for a fixed daily cost and you are worried rates will drop. So you also make a side bet (paper) that pays you when rates drop. Rates drop, the side bet pays USD 135,000, and the ship loses USD 114,000, so you come out USD 21,000 ahead instead of badly down. The catch: your real ship and the index used for the side bet did not move by exactly the same amount, and if your ship breaks down the side bet keeps running on its own clock. So the hedge protects most of you, not all of you.

## Key mechanics and formulas
- Paper settlement: `paper_pnl = (index_average - fixed_price) * contract_days` where `index_average` is the arithmetic mean of the relevant [[Baltic Route Codes|Baltic route]] or basket print over the settlement window, `fixed_price` is the FFA price you traded, and `contract_days` is the number of index days bought or sold. Sign flips for a short.
- Physical P&L (voyage): `voyage_pnl = gross_freight_revenue - voyage_costs` where `voyage_costs = bunkers + port + canal + commissions`. Convert to a daily figure via `TCE = (gross_freight_revenue - voyage_costs) / round_trip_days`. Note OPEX and crew are NOT in voyage costs; TCE is gross of vessel running cost (see [[Time Charter Equivalent]]).
- Physical P&L (time charter relet): `tc_pnl = (realized_relet_rate - hire_paid) * on_hire_days` measured in USD per day, with off hire days earning nothing while paper keeps settling.
- Synthetic equivalence: `TC in ≈ long FFA` and `TC out ≈ short FFA` for directional rate exposure only. Physical adds off hire and bunker exposure (see [[Bunker Risk]]) that paper does not carry.
- Physical to paper basis: `freight_basis = physical_realized_rate - index_settlement_rate`, the source of residual hedge error (see [[Freight Basis Risk]] and [[Basis]]).

## Prerequisites
- [[Freight]]
- [[Forward Freight Agreement]]
- [[Voyage Charter]]
- [[Time Charter]]

## Related concepts (learn next)
- [[Freight Basis Risk]] — the residual gap left when a physical position is hedged with a paper index, the central reason hedges are imperfect.
- [[Basis]] — the general framework for the difference between a physical price and its reference benchmark, of which freight basis is one case.
- [[TC In and TC Out]] — defines the physical positions that map to long and short FFA, the synthetic equivalence used to hedge.
- [[Relet]] — how you monetize or re deploy a physical vessel position, the mechanism that realizes the steel side P&L.
- [[Freight Options]] — the convex paper instrument that complements linear FFAs for hedging or expressing skewed views.
- [[Baltic Exchange and the Dry Indices]] — the published averages that paper settles against, the connective tissue between steel and paper.
- [[Freight Rate Risk]] — the underlying directional exposure both books are designed to express or neutralize.
- [[Forward Curve]] — the term structure of FFA prices that tells you whether hedging forward is cheap or expensive at each tenor.

## Common misconceptions
- "Paper freight delivers a ship at expiry." Wrong. An FFA is cash settled against an index average. No vessel changes hands and no cargo moves. If you actually need tonnage you must charter physically; paper only pays or collects the settlement difference.
- "Paper has no risk because it is cleared." Wrong on 2 counts. Clearing removes most counterparty default risk but introduces daily variation margin calls that can drain cash before the position is even profitable on paper. Separately, clearing does nothing about basis: the index you settle on rarely matches the physical rate you are hedging, so the hedge can still lose money against the steel.
- "Physical and paper always move together so the hedge is exact." Wrong. The index is a basket or route average computed on a fixed methodology and timing, while your physical fix has its own route, dates, vessel, and counterparty. The two diverge constantly, and that divergence is precisely the [[Freight Basis Risk]] that survives the hedge.
- "You must own ships to trade freight." Wrong. FFAs need no steel at all, and even physical exposure can be taken without ownership by chartering in and reletting (see [[Relet]]). Owners, charterers, traders, and pure financial players all trade the same paper.

## Sources
- Alizadeh and Nomikos, Shipping Derivatives and Risk Management — physical versus paper hedging, basis risk, FFA mechanics.
- Kavussanos and Visvikis, The International Handbook of Shipping Finance — freight derivatives and risk management chapters.
- Stopford, Maritime Economics, 3rd ed. — chartering markets, voyage and time charter economics.
- Baltic Exchange, FFA and index methodology guides; route definitions and settlement conventions.
- Clarksons SIN — physical fixture data and rate references for basis comparison.
- ICE and Baltic/EEX cleared FFA contract specifications — settlement, margining, and contract sizing.
- Ship and Bunker — bunker price references underlying the bunker component of physical voyage costs.
