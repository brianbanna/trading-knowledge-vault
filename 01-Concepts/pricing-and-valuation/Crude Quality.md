---
aliases: [crude oil quality, oil quality, crude grade]
tags:
  - "#energy/crude"
date-added: "2026-03-20"
---

# Crude Quality

## Definition

Crude oil quality is defined by two primary characteristics: density (measured by [[API Gravity]]) and sulfur content (the [[Sweet vs Sour]] spectrum). Light sweet crude (high API, low sulfur) is the easiest and cheapest to refine, yielding a higher proportion of valuable products like gasoline and diesel. Heavy sour crude (low API, high sulfur) requires complex refinery configurations (cokers, hydrocrackers, desulfurization units) and produces more residual fuel oil. There are hundreds of crude grades traded globally, each with a unique quality profile that determines which refineries can process it and what products it yields. The price differences between grades, known as quality differentials, are actively traded and reflect refinery economics, environmental regulations, and regional supply/demand balances.

## Why it matters (commodities and FX)

Quality differentials are a tradeable market in their own right. When environmental regulations tighten (IMO 2020 low sulfur fuel rules, for example), sweet crude premiums widen because low sulfur products become more valuable. When complex refinery capacity is abundant, heavy sour discounts narrow because more refiners can process difficult crudes profitably. A commodities trader must understand crude quality to evaluate refining margins ([[Crack Spread]]), assess the impact of supply disruptions (losing a light sweet grade vs a heavy sour grade has very different market implications), and identify relative value opportunities across the quality spectrum.

## Concrete example

A trader observes that the light sweet vs heavy sour differential (represented by [[Brent Crude]] at $82/bbl minus Mexico's Maya crude at $68/bbl = $14 spread) has widened from its 5 year average of $8. This could signal that complex refinery capacity is tight (fewer refiners competing for heavy sour crude) or that light sweet demand is elevated (gasoline season). The trader sells the spread (short Brent, long Maya equivalent exposure) expecting mean reversion. If complex refinery margins improve and more capacity comes online, Maya demand increases and the spread narrows to $9, earning $5/bbl. If instead a major coker goes down for unplanned maintenance, reducing heavy sour demand, the spread could widen to $18, losing $4/bbl.

## Key mechanics and formulas

**Key quality parameters:**
- API Gravity: density (light > 31 API, medium 22 to 31, heavy < 22)
- Sulfur content: sweet < 0.5%, sour > 0.5%
- TAN (Total Acid Number): high TAN crudes are corrosive, require special metallurgy
- Metals content (vanadium, nickel): poison refinery catalysts

**Quality differential:** `Grade Price = Benchmark Price + Quality Differential`

The differential can be positive (premium) or negative (discount) relative to the benchmark.

**Yield value:** `Crude Value = Σ (Product Yield % × Product Price) - Processing Cost`

Refiners run crude assays to determine what products each grade yields.

## Prerequisites

- [[API Gravity]]
- [[Sweet vs Sour]]
- [[Brent Crude]]
- [[Crack Spread]]

## Related concepts (learn next)

- [[API Gravity]] because it is the primary density measure determining crude classification.
- [[Sweet vs Sour]] because sulfur content is the second defining quality characteristic.
- [[Quality Spread]] because it is the direct trading expression of quality differentials.
- [[Crack Spread]] because refining margins depend on what the crude yields.
- [[Refinery Utilization]] because refinery complexity determines which grades are in demand.
- [[Dubai Crude]] because it represents the medium sour benchmark for Eastern Hemisphere pricing.
- [[Urals Crude]] because it illustrates how a specific quality profile affects pricing and trade flows.

## Common misconceptions

**"Light sweet is always better than heavy sour."** Not necessarily. Complex refineries earn higher margins processing cheap heavy sour crude. The value depends on the refinery configuration and the price differential.

**"Crude quality is fixed."** Crude from the same field can vary over time as reservoirs deplete. The Brent benchmark itself evolved from a single field to the BFOET basket as quality and production changed.

**"Only API and sulfur matter."** TAN, metals content, wax content, and specific product yields all affect pricing. Two crudes with identical API and sulfur can have very different values based on their detailed assay.

## Sources

- Exxon Mobil: Crude Oil Assay Library
- CME Group: Understanding Crude Oil Quality Differentials
- Petroleum Refining: Technology and Economics, James Gary et al.
