---
aliases: [market impact, price impact, permanent impact, temporary impact]
tags:
  - "#microstructure"
  - "#execution"
date-added: "2026-03-20"
---

# Market Impact

## Definition

Market impact is the price movement caused by a trade. Buying pushes price up; selling pushes it down. Impact has 2 components: temporary impact (price distortion during execution that reverses after trading stops) and permanent impact (the information content of the trade producing a lasting change). Impact scales with order size relative to available [[Liquidity]]. A 10 contract order in WTI CL has negligible impact. A 10,000 contract order moves the market measurably.

## Why it matters (commodities and FX)

Market impact is the hidden cost not on a commission schedule. For large commodity positions, impact can exceed spreads and commissions combined. A fund buying $100M of [[Copper Futures]] over a day moves copper against itself. This erodes expected profit. Expected alpha 50 bps, expected impact 30 bps, net 20 bps. This determines maximum position sizes, optimal execution horizons, and which markets are tradeable at your desired size.

## Concrete example

**Concrete:** Commodity fund buying 2,000 WTI contracts (2M barrels). ADV 500,000. At 10% participation, execution takes ~0.8 days. Square root impact: estimated permanent impact = σ x sqrt(V_trade / ADV) = 0.30 x sqrt(2,000 / 500,000) x $74 ≈ $1.40/bbl. On 2M barrels: $2.8M total impact, ~1.9% of the $148M notional. The trade must clear 1.9% just to break even on execution. [[VWAP]] over 2 days at 5% participation roughly halves impact to ~$1.4M. Slower execution = lower impact, more timing risk.

**Simplified:** Your own buying pushes the price up against you. Your own selling pushes it down. The bigger your order relative to what is available, the worse the average price you get. Some of this reverses after you finish (temporary). Some sticks (permanent), because your trade leaked information. Slowing down cuts impact but exposes you to the market moving on its own.

## Key mechanics and formulas

**Square root impact (Almgren):**
`Impact = σ x (V / ADV)^0.5 x Price`

σ = daily vol (fraction), V = order size (contracts), ADV = average daily volume. Doubling order size raises impact ~40%, not 100%.

**Temporary vs permanent:**
- Temporary: distortion reversing minutes to hours after execution. Caused by maker inventory imbalance
- Permanent: lasting change reflecting trade information content. If you buy because supply is tighter than the market expects, price permanently adjusts

**Impact vs participation rate:**
`Impact ≈ η x (Participation Rate)^δ`

η is market specific, δ ≈ 0.5 to 0.8. Higher participation = more impact, sub linearly.

## Prerequisites
- [[Liquidity]]
- [[Bid-Ask Spread]]
- [[Volatility]]

## Related concepts (learn next)
- [[Execution Algorithms]] - algos minimize impact by optimizing speed/impact tradeoff
- [[Slippage]] - slippage includes impact plus spread and timing
- [[VWAP]] - benchmark measuring execution quality including impact
- [[Liquidity]] - impact is inversely related. Thin markets = high impact
- [[Liquidity Risk]] - extreme impact in stress is a form of liquidity risk

## Common misconceptions

**"Impact only matters for large funds."** Even 50 contracts in a thin contract month has meaningful impact. Impact is size RELATIVE to liquidity, not absolute.

**"Impact is fully temporary."** Research shows 50 to 70% of impact is permanent in commodity futures. Your trade communicates information that does not fully reverse.

**"You can avoid impact with limit orders."** Limit orders dodge immediate impact but create execution risk (no fill). If you must fill, you eventually cross the spread, producing impact. Limit orders trade execution certainty for price improvement.

## Sources

- Almgren and Chriss, "Optimal Execution of Portfolio Transactions" (2000)
- Bouchaud, Farmer, Lillo, "How Markets Slowly Digest Changes in Supply and Demand" (2008)
- Kissell, "The Science of Algorithmic Trading" (2013)
