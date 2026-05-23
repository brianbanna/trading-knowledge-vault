---
aliases: [Exchange of Futures for Swaps, Brent-Dubai spread, East-West spread]
tags:
  - "#energy/crude/brent"
  - "#energy/crude/dubai"
date-added: "2026-03-20"
---

# EFS

## Definition

EFS (Exchange of Futures for Swaps) is the spread between [[Brent Crude]] futures and [[Dubai Crude]] swaps. It connects the two dominant global oil benchmarks: Brent (Atlantic Basin light sweet) and Dubai (Asian medium sour). Quoted as Brent minus Dubai in $/bbl. Wider EFS = Brent expensive vs Dubai (Atlantic tighter than Asia). Narrower EFS = Dubai catching up (Asian demand strengthening or Atlantic supply loosening). Actively traded OTC and one of the most important relative value indicators in global crude.

## Why it matters (commodities and FX)

The EFS sets the economics of East/West crude flows. Wide EFS = Atlantic crude too expensive for Asian refiners, who source Middle East and Asian grades instead. Narrow EFS = Atlantic crude becomes competitive for Asian import and arbitrage cargoes flow East. For trading houses (Vitol, Trafigura, Gunvor), the EFS is a core trade: buy in one basin, sell in another when the spread exceeds freight. Saudi Aramco's OSPs for Asian customers are set relative to Dubai/Oman, so EFS indirectly affects Aramco pricing.

## Concrete example

**Concrete:** EFS at $3.50/bbl. Trader calculates freight from North Sea to South Korea at $2.80/bbl on an Aframax. At $3.50, Brent is too expensive vs Dubai for Asian refiners to import North Sea crude economically. Trader expects Chinese refinery expansion to tighten Asian sour crude supply and narrow the EFS. She sells the EFS (short Brent, long Dubai). If the EFS narrows to $1.50, she earns $2.00/bbl. If North Sea supply disruptions tighten the Atlantic Basin instead, EFS widens to $5.00 and she loses $1.50/bbl.

**Simplified:** Brent prices Atlantic crude. Dubai prices Asian crude. The gap between them tells you whether oil should flow West to East or stay put. If the gap is bigger than freight, traders book a ship and arbitrage the difference. If the gap is smaller, no one ships. Watching the EFS tells you which basin is tight, where the arbitrage windows are, and how the global market is rebalancing.

## Key mechanics and formulas

**EFS:** `EFS = Brent Futures Price − Dubai Swap Price`

**Arbitrage condition:** Crude flows East when `EFS < Freight (Atlantic to Asia)`

**Typical range:** $1 to $6/bbl, averaging $2 to $3. Below $1 or above $6 is unusual.

**Related spread:** EFS is closely related to the Brent/Dubai [[Quality Spread]] since Brent is light sweet and Dubai is medium sour.

## Prerequisites

- [[Brent Crude]]
- [[Dubai Crude]]
- [[Quality Spread]]
- [[Freight]]

## Related concepts (learn next)

- [[Dubai Crude]]: one leg of the EFS and the Asian crude benchmark.
- [[Brent Crude]]: the other leg and the Atlantic/global benchmark.
- [[Freight]]: shipping costs determine when the East/West arb opens.
- [[Quality Spread]]: the EFS embeds both quality and location differentials.
- [[Location Arbitrage]]: the EFS is the primary cross basin arbitrage signal in crude.
- [[Dated Brent]]: physical Brent pricing feeds into the EFS through the paper/physical link.
- [[OPEC]]: Middle East production decisions affect Dubai supply and the EFS.

## Common misconceptions

**"The EFS is purely a quality spread."** It also reflects location, logistics, and regional demand. Two identical quality crudes in different basins would still have a spread driven by freight and demand.

**"A narrow EFS is always bullish for Asian crude demand."** It can also reflect weak Atlantic Basin crude markets or abundant Middle East supply.

**"The EFS is only relevant for physical traders."** Financial traders use the EFS as a macro signal for Asian vs Atlantic demand dynamics and as a component of cross basin relative value models.

## Sources

- Platts: Brent/Dubai EFS Assessment Methodology
- ICE: Brent and Dubai Swap Specifications
- Energy Intelligence: East/West Crude Oil Arbitrage Analysis
