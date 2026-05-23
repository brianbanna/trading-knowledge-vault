---
aliases: [basis point, bp, bps, basis points]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Basis Point

## Definition
A basis point is 1/100th of 1 percent, or 0.01%. It is the standard unit for quoting changes in interest rates, credit spreads, and yield differentials. A 25 basis point hike means rates moved 0.25%. The term exists because "percent of a percent" gets confusing fast. In FX, bps measure [[Swap]] rates, [[Forward Contract]] premiums, and [[Cross Pairs]] spread differentials. In commodities they appear in financing costs and storage rates.

## Why it matters (commodities and FX)
FX traders live in bps. The gap between a 3 month EUR deposit at 3.50% and 3.75% is 25 bps, and that gap drives [[FX Swap]] pricing directly. When a commodity trader finances inventory, the borrowing rate in bps determines whether a [[Contango]] carry trade is profitable. Central bank decisions are announced in bps (25, 50, 75), and every rate decision reprices the entire FX forward curve. Misreading "25 bps" as "25%" is a career ending error.

## Concrete example

**Concrete:** Trader on EUR/USD 3 month FX swaps. Swap spread at 45 bps. ECB expected to cut 25 bps next week, which would compress the spread. Trader enters a position profiting from narrowing. ECB cuts, spread compresses to 20 bps, capturing the 25 bps move on EUR 50 million notional. PnL: 50,000,000 × 0.0025 × (90/360) = 31,250 EUR. Fail symmetry: if ECB holds, spread widens to 70 bps and the position loses 31,250 EUR.

**Simplified:** A basis point is the smallest unit used to talk about interest rate changes. One hundred of them make up one percent. When a central bank says "we cut by 25 basis points," they cut the rate by a quarter of a percent. Bond and FX desks quote everything in bps because moving a 5% rate to "5.0025%" is clumsy, but "moved up 0.25 bps" is precise and obvious.

## Key mechanics and formulas
- 1 basis point = 0.01% = 0.0001 decimal
- 100 basis points = 1%
- Dollar value of 1 bp (DV01) = [[Notional]] × 0.0001 × (days / 360)
  - [[Notional]]: face value
  - days: tenor
  - 360: day count convention (actual/360 for most money markets)
- On a 100 million USD position, 1 bp = 10,000 USD per year, about 27.78 USD per day

## Prerequisites
- [[Pip]]
- [[Notional]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Pip]] , the FX equivalent, where 1 pip = 0.0001 for most pairs
- [[DV01]] , the dollar value of a 1 basis point move in rates
- [[Swap]] , where basis points price the fixed vs floating leg
- [[FX Swap]] , where forward points tie closely to rate differentials in bps
- [[Bid-Ask Spread]] , often quoted in bps for rates products
- [[Carry Trade]] , where you earn or pay the rate differential in bps
- [[LIBOR]] , historically the reference rate quoted in bps

## Common misconceptions

**Basis point is not a percent.** "Rates moved 50 basis points" means 0.50%, not 50%. Confusing the two is a 100x error.

**Bps and pips are not the same.** A [[Pip]] is the 4th decimal of an FX quote (0.0001); a basis point is 0.01% of a rate. Same number, different meaning.

**Day count matters.** DV01 depends on actual/360, actual/365, or 30/360. Wrong convention changes the PnL.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 4
- CME Group, "Introduction to Interest Rate Futures"
- Bank for International Settlements, "Triennial Central Bank Survey" (2022)
