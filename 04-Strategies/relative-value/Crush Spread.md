---
aliases: [crush spread, soybean crush, crush margin, board crush]
tags:
  - "#agri/oilseeds/soybeans"
date-added: "2026-03-20"
---

# Crush Spread

## Definition
The crush spread is the gross processing margin for converting [[Soybeans]] into [[Soybean Meal]] and [[Soybean Oil]], calculated as the combined value of the output products minus the cost of raw soybeans. It is the agricultural equivalent of the [[Crack Spread]] in petroleum refining, measuring whether it is profitable to process the raw input into finished products. One bushel of soybeans (60 lbs) typically yields approximately 44 lbs of meal, 11 lbs of oil, and 5 lbs of hulls and waste. The "board crush" refers to the spread calculated using exchange traded futures prices on [[CBOT]], while the physical "crush margin" accounts for actual processing costs including energy, labor, and transportation. Crush spreads are quoted in cents per bushel and serve as a key profitability indicator for major processors such as ADM, Bunge, and Cargill. When the board crush exceeds processing costs (typically $0.40 to $0.60/bu), crushers are incentivized to increase throughput and bid for more raw soybeans.

## Why it matters (commodities and FX)
The crush spread determines soybean processing economics and therefore directly influences global demand for raw soybeans, affecting major exporting countries and their currencies ([[BRL/USD]], [[ARS/USD]]). A widening crush signals strong product demand relative to soybean supply, encouraging more imports and higher processing activity. Crush spread trades allow commodity desks to express a view on processing margins without taking a directional bet on the overall level of soybean prices. Crush spread seasonality is pronounced: margins typically widen in Q4 and Q1 when South American soybean supplies have not yet arrived and US meal demand for livestock feeding peaks.

## Concrete example
**Success case:** In October 2022, soybean meal demand surged due to strong global poultry sector expansion. A trader bought the crush spread: long January meal at $420/short ton, long January oil at $0.64/lb, short January soybeans at $14.00/bu. The board crush was approximately $1.85/bu. By December, meal rallied to $470/short ton while beans only rose to $14.50/bu, widening the crush to $2.45/bu, a $0.60/bu gain or approximately $3,000 per properly ratioed crush unit.

**Failure case:** In April 2018, a trader bought the crush at $1.20/bu expecting seasonal margin widening. China imposed retaliatory tariffs on US soybeans, crushing domestic soybean prices and disrupting the normal product/input price relationship. The trader's position lost $0.30/bu as meal demand weakened in sympathy with trade war uncertainty. The lesson: exogenous policy shocks can overwhelm seasonal patterns in processing margin trades.

## Key mechanics and formulas
- **Board crush ($/bu) = (Soybean meal price x 0.022) + (Soybean oil price x 11) - Soybean price**
  - Soybean meal price in $/short ton; multiply by 0.022 to convert yield per bushel (44 lbs / 2,000 lbs per short ton)
  - Soybean oil price in $/lb; multiply by 11 (approximate lbs of oil extracted per bushel)
  - Soybean price in $/bu
- **CBOT crush unit:** 10 soybean contracts (50,000 bu) versus 11 soybean oil contracts (660,000 lbs) versus 9 or 10 soybean meal contracts (approximately 100 short tons each)
- **Breakeven:** Board crush must exceed roughly $0.40 to $0.60/bu for crushers to operate profitably after energy and overhead
- **Reverse crush:** Short meal + short oil, long beans (a bet on margin compression)

## Prerequisites
- [[Grains]]
- [[Spread Trade]]
- [[Futures Contract]]
- [[WASDE]]

## Related concepts (learn next)
- [[Spread Trade]] is the general framework for relative value positions like the crush.
- [[Stocks to Use Ratio]] for soybeans, meal, and oil individually affects crush spread levels and direction.
- [[WASDE]] provides soybean crush demand estimates that drive expectations for future processing margins.
- [[Old Crop New Crop]] interacts with crush when old crop soybean supply tightens, squeezing processor availability.
- [[Basis Risk]] arises when the board crush diverges from actual physical processing margins at a specific plant location.
- [[Contango Roll Cost]] affects the carry cost of holding crush spread positions across contract expirations.
- [[Implied Volatility]] on crush spread options reflects market uncertainty about future processing margins.
- [[COT Positioning]] in soybeans, meal, and oil reveals whether speculative money is net long or short the crush.

## Common misconceptions
- **"The board crush equals the actual processing margin."** The board crush ignores energy costs (natural gas for meal dryers), transportation, labor, and the value of hulls. Physical crush margins can differ by $0.20 to $0.40/bu from the exchange traded board crush.
- **"Crush spreads are low risk."** While exchange margins are lower than outright positions, crush spreads can move $0.50 to $1.00/bu in a month during volatile periods. The 3 legged nature of the trade adds execution complexity and slippage risk.
- **"High crush spreads always mean buy soybeans."** A high crush can persist when product demand is structurally strong; it does not necessarily imply soybeans are undervalued. Processor bidding may already be reflected in soybean basis levels.

## Sources
- CME Group, "Soybean Crush Reference Guide"
- "Trading and Hedging with Agricultural Futures and Options" by James B. Bittman
- Johnson, R.L., "Commodity Spread Trading: The Hidden Yield"
- USDA Oil Crops Yearbook
