---
aliases: [basis point, bp, bps, basis points]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Basis Point

## Definition
A basis point is 1/100th of 1 percent, or 0.01%. It is the standard unit for quoting changes in interest rates, credit spreads, and yield differentials. If a central bank raises rates by 25 basis points, that means the rate went up by 0.25%. The term exists because saying "percent of a percent" gets confusing fast. In FX, basis points measure [[Swap]] rates, [[Forward Contract]] premiums, and [[Cross Pairs]] spread differentials. In commodities, they appear in financing costs and storage rate quotes.

## Why it matters (commodities and FX)
FX traders live in basis points. The difference between a 3 month EUR deposit at 3.50% and 3.75% is 25 bps, and that gap drives [[FX Swap]] pricing directly. When a commodities trader finances inventory, the borrowing rate in bps determines whether a [[Contango]] carry trade is profitable. Central bank decisions are announced in bps (25, 50, 75), and every rate decision reprices the entire FX forward curve. Misreading "25 bps" as "25%" would be a career ending mistake.

## Concrete example
**Win scenario:** You are trading [[FX Swap]]s on EUR/USD. The 3 month EUR/USD swap spread is quoted at 45 bps. You notice the ECB is likely to cut by 25 bps at next week's meeting, which would compress the swap spread. You enter a position that profits from the spread narrowing. The ECB cuts, the spread compresses to 20 bps, and you capture the 25 bps move on a [[Notional]] of 50 million EUR. Your [[PnL]] is roughly 50,000,000 x 0.0025 x (90/360) = 31,250 EUR.

**Fail scenario:** You put on the same trade but the ECB surprises with a hold. The spread widens from 45 bps to 70 bps instead. You lose on the 25 bps move in the wrong direction. Same math, opposite sign: roughly negative 31,250 EUR in [[Unrealized PnL]] before you [[Stop Loss]] out.

## Key mechanics and formulas
- 1 basis point = 0.01% = 0.0001 in decimal
- 100 basis points = 1%
- Dollar value of 1 bp (DV01) = [[Notional]] x 0.0001 x (days / 360)
  - [[Notional]]: face value of the trade
  - days: tenor of the instrument
  - 360: day count convention (actual/360 for most money markets)
- For a 100 million USD position, 1 bp = 10,000 USD per year, or about 27.78 USD per day

## Prerequisites
- [[Pip]]
- [[Notional]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Pip]] , the FX equivalent, where 1 pip = 0.0001 for most pairs
- [[DV01]] , the dollar value of a 1 basis point move in rates
- [[Swap]] , where basis points price the fixed vs floating leg
- [[FX Swap]] , where forward points are closely tied to rate differentials in bps
- [[Bid-Ask Spread]] , often quoted in basis points for rates products
- [[Carry Trade]] , where you earn or pay the rate differential in bps
- [[LIBOR]] , historically the reference rate quoted in bps

## Common misconceptions
- **Basis point is not a percent.** Saying "rates moved 50 basis points" means 0.50%, not 50%. Confusing the two is a 100x error.
- **Bps and pips are not the same.** In FX, a [[Pip]] is the 4th decimal place of a quote (0.0001), while a basis point is 0.01% of a rate. They happen to be the same number (0.0001) but measure completely different things.
- **Not all instruments use the same day count.** DV01 calculations depend on whether you use actual/360, actual/365, or 30/360. Using the wrong convention changes the PnL.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 4
- CME Group, "Introduction to Interest Rate Futures"
- Bank for International Settlements, "Triennial Central Bank Survey" (2022)
