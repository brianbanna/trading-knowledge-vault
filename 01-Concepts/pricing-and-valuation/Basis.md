---
aliases: [basis, cash basis]
tags:
  - "#energy/crude"
  - "#agri/grains"
date-added: "2026-03-20"
---

# Basis

## Definition

The difference between 2 reference prices. Most commonly spot price minus futures price (`Basis = Spot − Futures`). In commodities, basis also refers to differentials between 2 locations, 2 grades, or 2 related products.

## Why It Matters (Commodities / FX)

Basis is the raw material of every [[Relative Value Trade]]. When a physical trader says "I trade basis," they mean the differential between physical and futures, or between 2 delivery points. Basis reflects local supply/demand, transport costs, and quality.

## Prerequisites

- [[Futures Contract Mechanics]]
- [[Forward Curve]]

## Related Concepts (Learn Next)

- [[Basis Risk]]
- [[Relative Value Trade]]
- [[Cost of Carry Model]]
- [[Convergence]] (basis converges to zero at expiry)
- [[Forward Freight Agreement]] (the paper freight instrument whose gap to physical freight is the freight basis)
- [[Baltic Exchange and the Dry Indices]] (the benchmark a freight FFA hedge settles against)

## Concrete example

### Freight physical to paper basis

In freight, basis is the gap between the physical rate an operator actually pays or earns on a specific voyage or [[Time Charter]] fixture and the paper [[Forward Freight Agreement]] rate, which settles against the [[Baltic Exchange and the Dry Indices|Baltic]] route average. An FFA hedge is only as good as the correlation between the operator's real route and the Baltic benchmark route; the residual is freight [[Basis Risk]].

**Concrete:** An operator runs a Capesize on a niche route and hedges by selling 10 C5 FFA lots at 20,000 USD per day. The physical market falls: the real route earns 14,000, a 6,000 shortfall versus budget, while the C5 FFA settles at 15,000 so the short pays 5,000 of gains. The hedge recovered 5,000 of the 6,000; the remaining 1,000 is the physical to paper basis, the part the benchmark did not capture. Had the odd route instead strengthened relative to C5, the basis would have moved the other way and the hedge would have over covered. Tracking the spread between actual fixtures and the hedged Baltic route is how freight desks manage this residual.

---
*Status: #stub | Last reviewed: 2026-03-20*
