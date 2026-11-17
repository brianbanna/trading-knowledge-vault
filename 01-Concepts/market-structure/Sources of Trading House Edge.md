---
aliases: [trading house edge, position edge, why houses make money]
tags:
  - "#physical-trading/analysis"
date-added: "2026-11-17"
---

# Sources of Trading House Edge

## Definition

A physical trading house earns the gap between 2 prices that differ in where, when or what (the [[Three Transformations]]). Competition pushes each gap down to the cost of the marginal house still needed to do the transformation. A house keeps the difference between that marginal cost and its own, and that difference comes from position, not from a better model.

## Why it matters

Every desk sees the same screens and builds similar models. P&L differs because houses hold different assets, contracts, information, capital and risk capacity. In a dislocation the marginal player cannot enter, so the house already holding the asset or contract keeps the whole gap.

## Concrete example with real numbers

- Merit order of houses: the Med gap settles at 1.20 $/bbl. House A pays 0.90 freight and 0.30 financing, total 1.20, and earns 0. House B, on a long time charter and a cheaper balance sheet, pays 0.80 and earns 0.40, or 400,000 $ on 1m bbl.
- US LNG on the 9 November 2026 settles: Henry Hub 3.218 $/MMBtu, NWE DES 26.516. Offtake cost 1.15 × 3.218 + 3.00 fee = 6.70, plus 3.00 shipping = 9.70 delivered. Margin 16.82 $/MMBtu, about 58.9m $ on a 3.5m MMBtu cargo. The plant earns only its fee, 10.5m $.
- Hedge against naked short: a house with 5 ships on time charter at 14,000 $/day sells Q1 FFAs at 16,000. Whether rates go to 13,000 or 19,000, it locks +2,000 $/day × 450 days = +900,000 $. A fund selling the same FFAs at 16,000 loses 1.35m $ if rates reach 19,000.

## Key mechanics and formulas

- Margin of a house = gap set by the marginal house − own cost of the transformation.
- 5 edges: assets (who can act at all), options inside contracts (destination, volume ±10%, loading window, grade), information from volume, capital and relationships (prepays, credit to carry margin calls), willingness to hold risk.
- Lift or cancel an offtake cargo: the fee is sunk, so lift only if destination price > gas cost + shipping.
- A ±10% volume clause on 1m bbl when the market sits X below the contract: take 0.9m, worth 100,000 × X.

## Prerequisites

- [[Three Transformations]]
- [[Merit Order]]
- [[Full Carry]]
- [[Offtake Agreement]]

## Related concepts

- [[Floating Storage]]
- [[Henry Hub-TTF Spread]]
- [[Hedge Ratio]]
- [[Trading Taxonomy]]
- [[War Risk Premium]]
- [[2022 European Gas Crisis and US LNG]]

## Common misconceptions

- "Houses make more because they negotiate better differentials." The differential is the result; the cost advantage behind it is the cause.
- "A better model is the edge." Everyone sees the signal; only the house with the asset can act on it.
- "Assets always pay." Fees, hire and tank rent are owed in bad years too; the edge is an option with a premium.
- "The same trade carries the same risk for everyone." A sale that hedges physical length for a house is a naked short for a fund.

## Sources

- Market history: the 2020 contango and the 2022 European gas crisis.
- US LNG contract structure, 115% of Henry Hub plus a fixed fee, set by the early Gulf Coast offtake contracts.
- Market data, settles of 9 November 2026.
