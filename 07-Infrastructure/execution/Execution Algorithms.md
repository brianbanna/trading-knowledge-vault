---
aliases: [execution algorithms, execution algos, algo execution, algorithmic execution, child orders]
tags:
  - "#execution"
date-added: "2026-03-20"
---

# Execution Algorithms

## Definition

Execution algorithms break large parent orders into smaller child orders and execute them over time, minimizing [[Market Impact]] and [[Slippage]]. They bridge a trading decision ("buy 500 WTI contracts") and the microstructure reality (you cannot buy 500 at once without moving the price). Three families: benchmark algos ([[VWAP]], [[TWAP]]), aggressive algos (Implementation Shortfall, front loaded to reduce timing risk), passive algos (iceberg, peg, sniper, waiting for favorable prices).

## Why it matters (commodities and FX)

Execution quality is a direct P&L line item. On a $50 million commodity portfolio turning over 2x per year, 2 ticks of execution improvement per trade is worth $500,000+ annually. For [[Relative Value Trade|spread trades]], both legs must execute near simultaneously to lock in the intended spread level. A 1 tick miss on each leg of a [[Calendar Spread]] doubles execution cost.

Commodity algos must account for concentrated liquidity windows (pit session hours for many CME contracts), roll period clustering (Goldman roll, index rebalancing), and event driven [[Volatility]] (EIA inventory, OPEC). An algo running through an EIA number behaves nothing like one running in a calm afternoon.

## Concrete example

**Concrete:** Spread execution. You want to enter a [[Brent-WTI Spread]]: buy 100 WTI, sell 100 Brent. Three approaches. (1) Legging: execute one leg, then the other. If you buy WTI at $74.00 and Brent moves from $78.00 to $78.30 before you sell, the entry spread is $4.30 instead of $4.00, a $30,000 miss. (2) Spread algo: works both legs simultaneously, pausing one when the other falls behind, only executes near the target $4.00. Tighter execution but requires cross exchange connectivity (WTI on NYMEX, Brent on ICE). (3) Exchange listed spread: trade as a single instrument with its own book. Capital efficient but limited to intra exchange spreads.

**Simplified:** A big order does not fit on the screen. The algo chops it into many small orders and feeds them in over time. Different algos balance speed (avoiding adverse price drift) against impact (your own footprint moving the price). Pick the algo by urgency, size relative to liquidity, and event risk.

## Key mechanics and formulas

**Algo type selection:**

| Scenario | Recommended Algo |
|----------|-----------------|
| Passive, no urgency, liquid market | [[VWAP]] |
| Passive, unpredictable volume | [[TWAP]] |
| Urgent, alpha decaying | Implementation Shortfall (IS) |
| Hidden size, illiquid market | Iceberg / dark pool sweep |
| Spread trade, 2 legs | Spread algo with leg management |
| Event sensitive (pre EIA) | Hold execution, resume after |

**Implementation Shortfall (IS):**
`IS = Decision Price - Execution Price (adjusted for direction)`

IS algos trade aggressively early (when alpha is strongest and leakage risk lowest) and slow down later. Minimizes total cost of delay + impact.

**Child order mechanics:**
Parent order: Buy 500 CL
- Child 1: Buy 20 CL limit at $74.02 (passive, inside the bid ask)
- If filled in 30 seconds: next child
- If not filled: adjust to $74.04 (more aggressive)
- Repeat with size/price adjustments across the window

**Participation rate:**
`Participation = Algo Volume / Market Volume`

Keep below 10 to 15% to limit footprint. Above 20% means significant [[Market Impact]].

## Prerequisites
- [[VWAP]]
- [[TWAP]]
- [[Liquidity]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Market Impact]] - the cost algos minimize. Algo selection requires an impact model.
- [[Slippage]] - the realized cost of imperfect execution. Algos reduce but do not eliminate it.
- [[Liquidity]] - algo behavior must adapt to liquidity. VWAP in an illiquid hour fails.
- [[Volatility]] - execution cost scales with vol. Algo parameters should adjust by regime.

## Common misconceptions

**"Algos always beat manual execution."** In thin markets or during events, a skilled manual trader reading the book beats a rigid algo. Algos excel in liquid, normal conditions.

**"Just use VWAP for everything."** Different situations need different algos. Urgent alpha decay needs IS. Patient thin market needs an iceberg. Algo selection is a skill.

**"Lower participation rate is always better."** Lower participation cuts impact but increases execution time, exposing to adverse drift. The optimum balances impact vs timing risk.

## Sources

- Kissell, "The Science of Algorithmic Trading and Portfolio Management" (2013)
- Almgren and Chriss, "Optimal Execution of Portfolio Transactions" (2000)
- CME Group: algo execution best practices for commodity futures
