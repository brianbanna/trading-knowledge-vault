---
aliases: [crude oil quality, oil quality, crude grade]
tags:
  - "#energy/crude"
date-added: "2026-03-20"
---

# Crude Quality

## Definition

Crude oil quality is defined by density ([[API Gravity]]) and sulfur content (the [[Sweet vs Sour]] spectrum). Light sweet crude (high API, low sulfur) is cheapest to refine, yielding more gasoline and diesel. Heavy sour crude (low API, high sulfur) requires complex configurations (cokers, hydrocrackers, desulfurization) and produces more residual fuel oil. Hundreds of grades trade globally, each with a unique quality profile that determines which refineries can process it. Quality differentials between grades are actively traded and reflect refinery economics, environmental regulations, and regional balances.

## Why it matters (commodities and FX)

Quality differentials are a tradeable market. When environmental regulations tighten (IMO 2020 low sulfur fuel rules), sweet crude premiums widen because low sulfur products become more valuable. When complex refinery capacity is abundant, heavy sour discounts narrow because more refiners can process difficult crudes profitably. Quality awareness is required to evaluate refining margins ([[Crack Spread]]), assess supply disruption impact (losing a light sweet grade vs heavy sour has different implications), and identify relative value across the quality spectrum.

## Concrete example

**Concrete:** Light sweet vs heavy sour differential ([[Brent Crude]] $82/bbl minus Maya $68/bbl = $14 spread) widens from its 5 year average of $8. Signals either tight complex refinery capacity (fewer refiners competing for heavy sour) or elevated light sweet demand (gasoline season). Trader sells the spread (short Brent, long Maya exposure) expecting reversion. If complex margins improve and capacity comes online, Maya demand rises and the spread narrows to $9, earning $5/bbl. If a major coker goes down for unplanned maintenance, heavy sour demand drops and the spread widens to $18, losing $4/bbl.

**Simplified:** Not all crude is the same. Lighter and less sulfurous crude is easier to turn into gasoline. Heavier, more sulfurous crude needs expensive refineries. The price gap between the two grades moves with refinery capacity and product demand. If gasoline demand jumps, the light sweet premium widens. If a complex refinery breaks, no one wants the heavy sour and its discount blows out. Trading those gaps is a relative value market separate from outright crude direction.

## Key mechanics and formulas

**Quality parameters:**
- API Gravity: light > 31, medium 22 to 31, heavy < 22
- Sulfur: sweet < 0.5%, sour > 0.5%
- TAN (Total Acid Number): high TAN crudes corrode equipment
- Metals (vanadium, nickel): poison refinery catalysts

**Quality differential:** `Grade Price = Benchmark Price + Quality Differential`

Differential can be positive (premium) or negative (discount) vs benchmark.

**Yield value:** `Crude Value = Σ (Product Yield % × Product Price) − Processing Cost`

Refiners run crude assays to determine product yield per grade.

## Prerequisites

- [[API Gravity]]
- [[Sweet vs Sour]]
- [[Brent Crude]]
- [[Crack Spread]]

## Related concepts (learn next)

- [[API Gravity]]: the primary density measure for crude classification.
- [[Sweet vs Sour]]: sulfur content, the second defining quality characteristic.
- [[Quality Spread]]: the direct trading expression of quality differentials.
- [[Crack Spread]]: refining margin depends on what the crude yields.
- [[Refinery Utilization]]: refinery complexity determines which grades are in demand.
- [[Dubai Crude]]: medium sour benchmark for Eastern Hemisphere pricing.
- [[Urals Crude]]: example of how a specific quality profile affects pricing and trade flows.

## Common misconceptions

**"Light sweet is always better than heavy sour."** Complex refineries earn higher margins on cheap heavy sour crude. Value depends on refinery configuration and the price differential.

**"Crude quality is fixed."** Crude from the same field varies as reservoirs deplete. The Brent benchmark itself evolved from a single field to the BFOET basket as quality and production changed.

**"Only API and sulfur matter."** TAN, metals, wax content, and specific product yields all affect pricing. Two crudes with identical API and sulfur can have different values based on full assay.

## Sources

- Exxon Mobil: Crude Oil Assay Library
- CME Group: Understanding Crude Oil Quality Differentials
- Petroleum Refining: Technology and Economics, James Gary et al.
