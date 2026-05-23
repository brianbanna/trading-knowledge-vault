---
aliases: [refinery runs, refinery throughput, utilization rate]
tags:
  - "#energy/crude"
  - "#energy/refined"
date-added: "2026-03-20"
---

# Refinery Utilization

## Definition

Refinery utilization is the percentage of a refinery's or country's crude processing capacity actually being used, calculated as throughput / operable capacity. US operable capacity is ~18M barrels/day. Utilization runs between 85% and 95%, with seasonal peaks in summer (gasoline) and winter (heating oil), and troughs during [[Turnaround Season]] (spring and fall maintenance). The [[EIA Report]] publishes weekly US utilization, one of the most watched operational metrics in energy.

## Why it matters (commodities and FX)

Utilization is the link between crude demand and refined product supply. High utilization (above 92%) means refiners run hard, pulling crude from storage: bullish crude, often bearish product inventories. Low utilization (below 87%) means weaker crude demand and crude builds. [[Crack Spread]] levels drive utilization decisions: wide cracks, max throughput; narrow cracks, reduced runs. The seasonal cycle helps anticipate [[Calendar Spread]] moves, inventory trends, and product dynamics.

## Concrete example

**Concrete:** June 2025: US utilization hits 95.2%, near max, on peak summer driving. Crude draws run 3M barrels/week, supporting backwardated WTI. A trader goes long the [[Gasoline Crack]] expecting strong refinery demand for crude. If utilization holds above 94% through August, gasoline cracks widen to $35/bbl and the position profits. If a hurricane forces Gulf Coast offline, utilization drops to 88%, gasoline cracks initially spike (less product output) then collapse as demand fears set in. Complex dynamics, but utilization is the leading indicator.

**Simplified:** How hard refineries are running. High = lots of crude burned, lots of gasoline and diesel made. Low = maintenance season or weak demand. Track it weekly via EIA to anticipate crude inventory swings and product price moves.

## Key mechanics and formulas

**Utilization rate:** `Utilization = Crude Throughput / Operable Capacity × 100%`

**Seasonal pattern (US):**
- Q1 (Jan to Mar): 85 to 90% (winter / early turnaround)
- Q2 (Apr to Jun): 88 to 93% (ramp to summer)
- Q3 (Jul to Sep): 92 to 96% (peak summer driving)
- Q4 (Oct to Dec): 87 to 92% (fall turnaround, then winter ramp)

**Crude demand impact:** each 1% change in US utilization ≈ 180,000 barrels/day of crude demand change.

## Prerequisites

- [[Brent Crude]]
- [[WTI Crude Oil]]
- [[Crack Spread]]
- [[EIA Report]]

## Related concepts (learn next)

- [[Turnaround Season]]: scheduled maintenance drives the seasonal lows
- [[Crack Spread]]: refining margins determine whether refiners run hard or cut
- [[EIA Report]]: utilization reported weekly in the petroleum status report
- [[Gasoline Crack]]: summer driving season drives the primary utilization peak
- [[Heating Crack]]: winter heating drives the secondary peak
- [[Contango]]: low utilization periods coincide with crude builds and contango

## Common misconceptions

**"100% utilization is possible."** Max sustained utilization is ~96 to 97% due to unplanned maintenance, blending constraints, and quality issues. Nameplate capacity includes units that may be offline.

**"Low utilization is always bearish for crude."** During turnaround season, low utilization is expected and priced in. Only bearish when it drops unexpectedly outside maintenance windows.

**"Utilization is the same everywhere."** Regional differences matter. Gulf Coast at 95% while Midwest at 88% due to different crude supply dynamics and seasonal patterns.

## Sources

- EIA: Weekly Petroleum Status Report (refinery utilization section)
- EIA: Refinery Capacity Report (annual)
- Baker & O'Brien: US Refinery Capacity and Utilization Data
