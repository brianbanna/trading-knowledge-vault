---
aliases: [market impact, price impact, permanent impact, temporary impact]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-20"
---

# Market Impact

## Definition

Market impact is the price movement caused by a trade. When you buy, your demand pushes the price up. When you sell, your supply pushes it down. Market impact has 2 components: temporary impact (the price distortion during execution that reverses after you stop trading) and permanent impact (the information content of your trade that causes a lasting price change). Impact scales with order size relative to available [[Liquidity]]. A 10 contract order in WTI CL has negligible impact. A 10,000 contract order will move the market measurably.

## Why it matters (commodities and FX)

Market impact is the hidden cost of trading that does not appear on a commission schedule. For large commodity positions, market impact can be the single largest transaction cost, exceeding spreads and commissions combined. A fund buying $100 million of [[Copper Futures]] over a day will move the copper price against itself. This impact erodes the expected profit of the trade. If your expected alpha on a trade is 50 bps but your expected market impact is 30 bps, your net expected profit is only 20 bps. Understanding this determines maximum position sizes, optimal execution horizons, and which markets are even tradeable at your desired size.

## Concrete example

A commodity fund wants to buy 2,000 WTI contracts (2 million barrels). Average daily volume is 500,000 contracts. At 10% participation rate, execution takes 4,000 / (500,000 x 0.10) = ~0.8 days. Using a square root impact model:

Estimated permanent impact = σ x sqrt(V_trade / ADV) = 0.30 x sqrt(2,000 / 500,000) x $74 ≈ $74 x 0.30 x 0.063 = $1.40/bbl

On 2,000 contracts x 1,000 bbl = 2 million barrels: total impact cost ≈ $1.40 x 2,000,000 = $2.8 million. For a $148 million position (2M bbl x $74), that is ~1.9% of notional. This means the trade must generate >1.9% return just to break even on execution.

If instead the trader uses a [[VWAP]] algo over 2 days at 5% participation rate, the impact estimate roughly halves: ~$1.4 million. Slower execution = lower impact but more timing risk.

## Key mechanics and formulas

**Square root impact model (Almgren):**
`Impact = σ x (V / ADV)^0.5 x Price`

Where σ = daily volatility (fraction), V = order size (contracts), ADV = average daily volume. The square root relationship means doubling order size increases impact by ~40%, not 100%.

**Temporary vs permanent impact:**
- Temporary: price distortion that reverses within minutes to hours after execution completes. Caused by inventory imbalance in market makers' books.
- Permanent: lasting price change reflecting the information content of the trade. If you are buying because you know supply is tighter than the market expects, the price permanently adjusts.

**Impact as a function of participation rate:**
`Impact ≈ η x (Participation Rate)^δ`

Where η is a market specific constant and δ ≈ 0.5 to 0.8. Higher participation = more impact, but less than linearly.

## Prerequisites
- [[Liquidity]]
- [[Bid-Ask Spread]]
- [[Volatility]]

## Related concepts (learn next)
- [[Execution Algorithms]] - algos are specifically designed to minimize market impact by optimizing the speed/impact tradeoff.
- [[Slippage]] - slippage includes market impact but also includes spread cost and timing effects.
- [[VWAP]] - a benchmark that measures execution quality including impact cost.
- [[Liquidity]] - impact is inversely related to liquidity. Thin markets have high impact.
- [[Liquidity Risk]] - extreme impact during stressed markets is a form of liquidity risk.

## Common misconceptions

**"Market impact only matters for large funds."** Even a 50 contract order in a thin contract month or small commodity can have meaningful impact. Impact is about size RELATIVE to available liquidity, not absolute size.

**"Impact is fully temporary."** Research consistently shows 50 to 70% of impact is permanent in commodity futures. Your trade communicates information to the market, which does not fully reverse.

**"You can avoid impact by using limit orders."** Limit orders avoid immediate impact but create execution risk (not getting filled). If you must fill the order, you eventually cross the spread, producing impact. Limit orders trade off certainty of execution for price improvement.

## Sources

- Almgren and Chriss, "Optimal Execution of Portfolio Transactions" (2000)
- Bouchaud, Farmer, Lillo, "How Markets Slowly Digest Changes in Supply and Demand" (2008)
- Kissell, "The Science of Algorithmic Trading" (2013)
