---
aliases: [space time form, physical trading strategies, transformations in space time and quality]
tags:
  - "#physical-trading/analysis"
date-added: "2026-11-17"
---

# Three Transformations

## Definition

A physical trader changes a commodity in 1 of 3 ways and is paid by the spread between 2 prices: in space (moving it from a surplus place to a short place, paid by the location spread), in time (storing it from a surplus period to a short period, paid by the calendar spread) and in form or quality (blending it to the spec a buyer needs, paid by the quality spread). Each spread is capped by the cost of doing the transformation.

## Why it matters

A house almost never earns a flat price. It hedges the shared index and keeps the gap between 2 prices that differ in where, when or what. Knowing which transformation a trade is, and what caps its spread, tells you where the margin sits and how the trade breaks.

## Concrete example with real numbers

- Space: corn FOB US Gulf 200 $/t plus freight 35 = 235 delivered to Egypt; Brazil FOB 195 plus freight 42 = 237. Egypt pays 250 CFR, so the US wins: 250 − 235 − 5 other costs = 10 $/t, 600,000 $ on 60,000 t. Brazil takes over once its freight disadvantage falls below its 5 $/t price advantage.
- Time: spot wheat 220 $/t, 3 month forward 232, full carry 10 (storage 6, financing 3.30, insurance 0.70). Buy, store, sell forward: +2 $/t locked on day 1. With the forward at 226 the spread is 4 below full carry, so a holder sells spot and buys forward and saves 4 $/t.
- Quality: 0.5% marine fuel sells at 585 $/t. 1.0% residue blended with 0.1% cutter at 650 needs 44.4% residue (1.0x + 0.1(1 − x) = 0.5). At 540 the blend costs 601, a loss; the residue breaks even at about 504 $/t.

## Key mechanics and formulas

- Space margin = destination price − origin price − freight − other costs. Choose origin by delivered cost, not port price.
- Incoterms set the freight exposure: buy FOB and sell CFR, CIF or DAP and you are short freight until you fix the ship or buy FFAs.
- Time margin = forward − spot − full carry. Contango has a ceiling at full carry (anyone with money and a tank can store); backwardation has no floor (closing it needs the commodity today).
- Freight cannot be stored, so an FFA curve has no carry arbitrage and the front month is a pure forecast of the monthly average.
- Blend share for a target spec t from components a and b: x = (t − b) / (a − b). Blend to just under spec: overshooting is giveaway.

## Prerequisites

- [[Full Carry]]
- [[Storage Economics]]
- [[Quality Spread]]
- [[Forward Freight Agreement]]

## Related concepts

- [[Sources of Trading House Edge]]
- [[Floating Storage]]
- [[Blending]]
- [[Backwardation Squeeze]]
- [[Probo Koala 2006]]

## Common misconceptions

- "The cheapest origin wins." The cheapest delivered origin wins; freight can reverse the ranking.
- "Contango always pays storage." Only the part above full carry pays.
- "Under CFR the seller carries the voyage risk." The seller pays the freight but risk passes at loading; only delivered terms keep risk with the seller.
- "A wide quality spread is free money." It often hides a cost not in the price, such as waste disposal.

## Sources

- Trafigura, Commodities Demystified, on the 3 transformations (pages to cite at lesson 1.1).
- Worked numbers from the elective lesson of 17 November 2026; Capesize levels from the settles of 16 November 2026.
