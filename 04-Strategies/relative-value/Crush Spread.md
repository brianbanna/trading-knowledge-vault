---
aliases: [crush spread, soybean crush, crush margin, board crush]
tags:
  - "#agri/oilseeds/soybeans"
date-added: "2026-03-20"
---

# Crush Spread

## Definition
The crush spread is the gross processing margin for converting [[Soybeans]] into [[Soybean Meal]] and [[Soybean Oil]], calculated as the combined value of the output products minus the cost of raw soybeans. It is the agricultural equivalent of the [[Crack Spread]] in petroleum refining, measuring whether processing is profitable. One bushel of soybeans (60 lbs) yields ~44 lbs of meal, 11 lbs of oil, and 5 lbs of hulls and waste. The "board crush" uses exchange traded futures prices on [[CBOT]]. The physical "crush margin" accounts for actual processing costs (energy, labor, transportation). Crush spreads are quoted in cents per bushel and serve as a key profitability indicator for ADM, Bunge, and Cargill. When the board crush exceeds processing costs ($0.40 to $0.60/bu), crushers increase throughput and bid for more raw soybeans.

## Why it matters (commodities and FX)
The crush spread determines soybean processing economics and drives global demand for raw soybeans, affecting major exporting countries and their currencies ([[BRL/USD]], [[ARS/USD]]). A widening crush signals strong product demand relative to soybean supply, encouraging imports and processing activity. Crush trades let commodity desks express a view on processing margins without a directional bet on soybean prices. Strong seasonality: margins widen in Q4 and Q1 when South American supplies have not arrived and US meal demand for livestock peaks.

## Concrete example
**Concrete:** October 2022. Soybean meal demand surges on poultry sector expansion. Trader buys the crush: long January meal at $420/short ton, long January oil at $0.64/lb, short January soybeans at $14.00/bu. Board crush ~$1.85/bu. By December, meal rallies to $470/short ton, beans rise to $14.50/bu, crush widens to $2.45/bu. Gain $0.60/bu, ~$3,000 per properly ratioed crush unit.

**Simplified:** Soybeans go into a crusher and come out as meal (for animal feed) and oil (for cooking). The crush spread is what the crusher earns: value of meal + oil minus cost of soybeans. Trade it by buying the outputs and selling the input, or the reverse. Bet on margin widening (strong product demand) or compressing (weak demand or beans surge).

## Key mechanics and formulas
- **Board crush ($/bu) = (Soybean meal price x 0.022) + (Soybean oil price x 11) - Soybean price**
  - Meal price in $/short ton; multiply by 0.022 to convert yield per bushel (44 lbs / 2,000 lbs per short ton)
  - Oil price in $/lb; multiply by 11 (lbs of oil per bushel)
  - Soybean price in $/bu
- **CBOT crush unit:** 10 soybean contracts (50,000 bu) vs 11 soybean oil contracts (660,000 lbs) vs 9 or 10 soybean meal contracts (~100 short tons each)
- **Breakeven:** Board crush must exceed $0.40 to $0.60/bu for crushers to operate profitably after energy and overhead
- **Reverse crush:** Short meal + short oil, long beans (bet on margin compression)

## Prerequisites
- [[Grains]]
- [[Spread Trade]]
- [[Futures Contract]]
- [[WASDE]]

## Related concepts (learn next)
- [[Spread Trade]] is the general framework for relative value positions like the crush.
- [[Stocks to Use Ratio]] for soybeans, meal, and oil individually affects crush spread levels.
- [[WASDE]] provides soybean crush demand estimates that drive future processing margins.
- [[Old Crop New Crop]] interacts with crush when old crop soybean supply tightens.
- [[Basis Risk]] arises when board crush diverges from actual physical processing margins.
- [[Contango Roll Cost]] affects the carry cost of holding crush spread positions across expirations.
- [[Implied Volatility]] on crush spread options reflects uncertainty about future processing margins.
- [[COT Positioning]] in soybeans, meal, and oil reveals whether speculative money is net long or short the crush.

## Common misconceptions
- **"The board crush equals the actual processing margin."** The board crush ignores energy costs (natural gas for meal dryers), transportation, labor, and the value of hulls. Physical crush margins differ by $0.20 to $0.40/bu from the exchange traded board crush.
- **"Crush spreads are low risk."** Exchange margins are lower than outright positions, but crush spreads can move $0.50 to $1.00/bu in a month. The 3 legged nature adds execution complexity and slippage.
- **"High crush spreads always mean buy soybeans."** A high crush can persist when product demand is structurally strong. Processor bidding may already be reflected in soybean basis.

## Sources
- CME Group, "Soybean Crush Reference Guide"
- "Trading and Hedging with Agricultural Futures and Options" by James B. Bittman
- Johnson, R.L., "Commodity Spread Trading: The Hidden Yield"
- USDA Oil Crops Yearbook
