---
aliases: [bunker risk, fuel risk, bunker price risk, fuel cost risk, marine fuel risk]
tags:
  - "#risk"
  - "#freight/wet"
date-added: "2026-06-17"
---

# Bunker Risk

## Definition
Bunker risk is the chance that the price of the marine fuel a ship burns moves against you between the moment a deal is struck and the moment the ship finishes steaming. Fuel is bought along the way, often weeks after the rate is agreed, so the price you pay is not the price you assumed when you fixed. Technically it is the sensitivity of voyage or charter profit and loss to the spot price of the bunker grade actually consumed (VLSFO, HSFO, or MGO), driven by the time lag between fixing and burning and by who in the [[Charter Party]] is contractually obliged to buy the fuel. It is a price risk on a physical input, distinct from the freight rate risk on revenue. For the grades, regulation, and the instruments that hedge it, see [[Bunkers, IFO versus MGO, and the Bunker Hedge]].

## Why it matters (commodities and FX)
Bunkers are typically 40 to 60 percent of the cash cost of a spot voyage, so they dominate the voyage budget. An owner who fixes a [[Voyage Charter]] at a fixed USD per tonne freight and then buys fuel later is implicitly short fuel, equivalently long a chunk of oil exposure, whether or not anyone wrote it down. A bunker spike eats the freight margin directly and can flip a profitable fixture into a loss. Who carries the exposure is set by the charter form: under a [[Voyage Charter]] the owner buys bunkers against a fixed per tonne freight and bears the risk, while under a [[Time Charter]] the charterer pays for fuel across the whole term and carries it instead. The risk shows up the moment you quote a fixture, size a fleet position, or decide steaming speed, and it interacts with slow steaming, the [[Scrubber Spread]], and emissions rules under [[EEXI and CII Regulations]].

## Concrete example
**Concrete:** A VLCC is fixed for a single laden voyage, roughly a 22-day laden leg, burning about 55 t/day of VLSFO, so consumption is about 55 * 22 = 1,210 t, call it 1,200 t. At fixing the owner budgets fuel at VLSFO 550 USD/t, a fuel bill of 1,200 * 550 = 660,000 USD, and on that basis the fixture pencils out at a [[Time Charter Equivalent|TCE]] of about 35,000 USD/day. By the time the ship bunkers, VLSFO has jumped to 700 USD/t. The actual bill is 1,200 * 700 = 840,000 USD, an extra 1,200 * 150 = 180,000 USD the fixed freight never priced in. Spread across the round trip days that drop is roughly 8,000 USD/day, cutting TCE from about 35,000 to about 27,000 USD/day. Now suppose the owner had hedged: 12 gasoil futures lots at 100 t/lot equals 1,200 t of cover. If gasoil rallies about 150 USD/t alongside the VLSFO move, the hedge returns about 1,200 * 150 = 180,000 USD, offsetting the physical overspend and restoring TCE close to the original 35,000 USD/day, minus the gasoil versus VLSFO basis. If instead bunkers had fallen from 550 to 400 USD/t, the unhedged owner pockets a 180,000 USD windfall, but the hedged owner gives that windfall back on the short futures position. Hedging cuts both tails: it removes the loss and the lucky upside alike.

**Simplified:** You agree a flat price to ship oil before you know what fuel will cost. Fuel is more than half the bill. If fuel gets more expensive after you agree the price, the extra cost comes straight out of your profit. You can place a bet that pays you when fuel rises to cancel that out, but the same bet loses if fuel falls and hands back the savings. Either way the surprise is removed.

## Key mechanics and formulas
- `exposure_tonnes = consumption_per_day * voyage_days` where consumption_per_day is the burn rate of the grade in tonnes and voyage_days counts every day the ship is steaming on that fuel.
- `dollar_exposure = exposure_tonnes * price_move` where price_move is the change in USD/t of the burned grade between fixing and bunkering; this is the raw, unhedged P&L swing.
- `fuel_share_of_voyage_cost = bunker_cost / total_voyage_cost`, normally 0.4 to 0.6 on a spot voyage, which tells you how much of the freight margin is at the mercy of fuel.
- Fuel consumption scales roughly with the cube of speed, `fuel_per_day ~ speed^3`, so slow steaming cuts both burn and exposure_tonnes sharply, at the cost of more days.
- `residual_risk = physical_grade_move - hedge_instrument_move`, the basis left after hedging because the proxy (gasoil or fuel oil futures, or a port bunker swap) is not the exact grade or location burned. See [[Basis Risk]] and [[Freight Basis Risk]].

## Prerequisites
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]]
- [[Voyage Charter]]
- [[Time Charter]]
- [[Hedging]]

## Related concepts (learn next)
- [[Scrubber Spread]] — a scrubber lets a ship burn cheaper HSFO instead of VLSFO, changing which grade you are exposed to and the size of that exposure.
- [[Freight Rate Risk]] — the revenue side twin of bunker risk; together they define the full P&L spread of a fixture.
- [[Basis Risk]] — explains why a gasoil or fuel oil hedge never fully closes the exposure to the physical grade burned.
- [[Value at Risk]] — frames bunker exposure as a quantified loss distribution so it can be sized and limited across a book.
- [[Ballast Leg Economics]] — the empty repositioning leg still burns fuel, so bunker risk spans the full round trip, not just the laden leg.
- [[EEXI and CII Regulations]] — emissions limits push speed and fuel choice, reshaping both consumption and which grades carry the risk.
- [[Time Charter Equivalent]] — the metric where a bunker move actually lands, since fuel is a voyage cost subtracted before TCE.
- [[Strait of Hormuz]] — a chokepoint whose disruption spikes both freight and bunker prices, compounding the exposure on tanker routes through it.

## Common misconceptions
- "The charterer always pays for fuel, so the owner never has bunker risk." Wrong. Who buys bunkers is set by the charter form. Under a [[Voyage Charter]] the owner buys the fuel against a fixed per tonne freight and carries the full exposure; only under a [[Time Charter]] does the charterer pay across the term. Assuming the charterer always pays mislabels the party that actually holds the risk.
- "A gasoil futures hedge removes all bunker risk." Wrong. The futures track a related but different product at a different location, so a residual basis between the proxy and the exact grade burned remains. The hedge converts a large outright price risk into a smaller basis risk; it does not erase exposure.
- "Bunker risk is a minor line item." Wrong. Fuel is usually the single largest cash cost of a spot voyage at 40 to 60 percent of the total, so a moderate price move dominates the freight margin. Treating it as small understates the biggest swing factor in voyage P&L.
- "If I fixed a profitable freight rate, the voyage is locked in." Wrong. The freight is fixed but the fuel cost is not bought until later. A fixed freight with floating fuel is an open oil position, and a spike between fixing and bunkering can turn the locked in profit into a loss.

## Sources
- Alizadeh and Nomikos, Shipping Derivatives and Risk Management, chapters on bunker price risk and fuel hedging.
- Kavussanos and Visvikis, The International Handbook of Shipping Finance, sections on bunker exposure and freight cost structure.
- Stopford, Maritime Economics, 3rd edition, on voyage cost composition and speed fuel relationships.
- Baltic Exchange route and methodology guides for VLSFO bunker price assessments.
- Ship and Bunker, daily VLSFO, HSFO, and MGO price indications by port.
- Platts and Argus marine fuel methodology documents for grade and port assessments.
- ICE Gasoil and Fuel Oil contract specifications for the hedge instruments referenced.
