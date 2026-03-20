---
aliases: [Exchange of Futures for Swaps, Brent-Dubai spread, East-West spread]
tags:
  - "#energy/crude/brent"
  - "#energy/crude/dubai"
date-added: "2026-03-20"
---

# EFS

## Definition

EFS (Exchange of Futures for Swaps) is the spread between [[Brent Crude]] futures and [[Dubai Crude]] swaps. It is the mechanism that connects the two dominant global oil pricing benchmarks: Brent (the Atlantic Basin light sweet benchmark) and Dubai (the Asian medium sour benchmark). The EFS is quoted as Brent minus Dubai in dollars per barrel. A wider EFS means Brent is expensive relative to Dubai (Atlantic tighter than Asia), while a narrower EFS means Dubai is catching up (Asian demand strengthening or Atlantic supply loosening). The EFS is actively traded OTC and is one of the most important relative value indicators in global crude oil markets.

## Why it matters (commodities and FX)

The EFS determines the economics of East/West crude oil trade flows. When the EFS is wide, it is more expensive for Asian refiners to buy Atlantic Basin crude, incentivizing them to source Middle East and Asian grades instead. When the EFS narrows, Atlantic Basin crude becomes competitive for Asian import, and arbitrage cargoes flow East. For trading houses like Vitol, Trafigura, and Gunvor, the EFS is a core trade: they buy crude in one basin and sell in another when the spread exceeds freight costs. Saudi Aramco's Official Selling Prices (OSPs) for Asian customers are set relative to Dubai/Oman, so the EFS indirectly affects how much Aramco charges for its crude.

## Concrete example

The EFS is at $3.50/bbl. A trader calculates that freight from the North Sea to South Korea costs $2.80/bbl on an Aframax. At $3.50, Brent is too expensive relative to Dubai for Asian refiners to import North Sea crude economically. The trader expects Chinese refinery expansion to tighten Asian sour crude supply, narrowing the EFS. She sells the EFS (short Brent, long Dubai). If the EFS narrows to $1.50, she profits $2.00/bbl. If instead North Sea supply disruptions tighten the Atlantic Basin, the EFS could widen to $5.00, losing $1.50/bbl.

## Key mechanics and formulas

**EFS calculation:** `EFS = Brent Futures Price - Dubai Swap Price`

**Arbitrage economics:** Crude flows East when: `EFS < Freight Cost (Atlantic to Asia)`

**Typical EFS range:** $1 to $6/bbl, averaging around $2 to $3. Below $1 or above $6 is unusual.

**Related spread:** The EFS is closely related to the Brent/Dubai [[Quality Spread]] since Brent is light sweet and Dubai is medium sour.

## Prerequisites

- [[Brent Crude]]
- [[Dubai Crude]]
- [[Quality Spread]]
- [[Freight]]

## Related concepts (learn next)

- [[Dubai Crude]] because it is one leg of the EFS and the Asian crude benchmark.
- [[Brent Crude]] because it is the other leg and the Atlantic/global benchmark.
- [[Freight]] because shipping costs determine when the East/West arb opens.
- [[Quality Spread]] because the EFS embeds both quality and location differentials.
- [[Location Arbitrage]] because the EFS is the primary cross basin arbitrage signal in crude.
- [[Dated Brent]] because physical Brent pricing feeds into the EFS through the paper/physical link.
- [[OPEC]] because Middle East production decisions directly affect Dubai supply and thus the EFS.

## Common misconceptions

**"The EFS is purely a quality spread."** It also reflects location, logistics, and regional demand differences. Two identical quality crudes in different basins would still have a spread based on freight and demand.

**"A narrow EFS is always bullish for Asian crude demand."** It could also reflect weak Atlantic Basin crude markets or abundant Middle East supply.

**"The EFS is only relevant for physical traders."** Financial traders use the EFS as a macro signal for Asian vs Atlantic demand dynamics and as a component of cross basin relative value models.

## Sources

- Platts: Brent/Dubai EFS Assessment Methodology
- ICE: Brent and Dubai Swap Specifications
- Energy Intelligence: East/West Crude Oil Arbitrage Analysis
