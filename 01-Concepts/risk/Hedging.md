---
aliases: [hedging, hedge, risk offset, portfolio hedge]
tags:
  - "#risk"
date-added: "2026-03-20"
---

# Hedging

## Definition

Hedging is the practice of taking an offsetting position in a related instrument to reduce the risk of an existing exposure. A perfect hedge eliminates all price risk but also eliminates all profit potential. In practice, hedges are imperfect: they reduce but do not eliminate risk because the hedging instrument does not move exactly 1:1 with the exposure (this residual risk is called [[Basis]] risk). Hedging is distinct from [[Relative Value Trade|relative value trading]]: a hedge is entered to PROTECT an existing position, while a relative value trade is entered to PROFIT from a spread. The instruments may look identical, but the intent and risk management differ.

## Why it matters (commodities and FX)

Hedging is the reason commodity futures markets exist. Producers (oil companies, miners, farmers) sell futures to lock in prices for future production. Consumers (airlines, refiners, food companies) buy futures to lock in input costs. This producer/consumer hedging creates the fundamental supply and demand in futures markets that speculators trade against.

For a trader running a relative value book, hedging is about managing the RESIDUAL risks that spreads do not eliminate. A [[Calendar Spread]] hedges directional price risk but leaves curve risk. A [[Brent-WTI Spread]] hedges oil direction but leaves location basis risk. The skill is understanding what is hedged and what is not, and deciding which residual risks to keep (because you have an edge) and which to offset.

## Concrete example

**Airline jet fuel hedge:** An airline expects to consume 100 million gallons of jet fuel next year. Jet fuel at $2.50/gal. Risk: jet fuel rises to $3.50, increasing costs by $100 million. Hedge: buy crude oil futures (since no liquid jet fuel futures exist). 100 million gallons ≈ 2.38 million barrels. Buy 2,380 WTI contracts. If oil rises 30%, WTI moves from $74 to $96, the futures gain offsets most of the jet fuel cost increase. Basis risk: jet fuel may not move exactly with WTI. The jet fuel crack spread can widen or narrow independently. The hedge is effective directionally but imperfect on the basis.

**FX commodity hedge:** An Australian mining company earns revenue in USD (copper priced in USD) but has costs in AUD. If AUD/USD rises from 0.65 to 0.75, their AUD revenue falls. Hedge: sell AUD/USD forward. This locks the exchange rate but exposes the company to movements in the forward points (carry cost of the hedge).

## Key mechanics and formulas

**Optimal hedge ratio (minimum variance):**
`h* = Cov(ΔS, ΔF) / Var(ΔF) = ρ x (σ_S / σ_F)`

Where h* = number of futures contracts per unit of exposure, ρ = [[Correlation]] between spot and futures changes, σ_S = volatility of spot, σ_F = volatility of futures.

**Hedge effectiveness:**
`R² = ρ²`

An R² of 0.85 means the hedge explains 85% of the price variation. The remaining 15% is basis risk.

**Cost of hedging:**
- Direct cost: [[Bid-Ask Spread]], commissions, margin financing
- Indirect cost: opportunity cost of forgoing favorable price moves
- Roll cost: if the hedge uses futures, rolling costs ([[Roll Yield]]) in [[Contango]] markets erode hedge value

**Hedge P&L:**
`Total P&L = Physical Position P&L + Hedge P&L`
`= (S_end - S_start) x Quantity - h x (F_end - F_start) x Contract Size`

## Prerequisites
- [[Forward Curve]]
- [[Basis]]
- [[Correlation]]
- [[Relative Value Trade]]

## Related concepts (learn next)
- [[Basis]] - the risk that the hedging instrument does not move perfectly with the exposure. Basis risk is the primary risk in any hedge.
- [[Roll Yield]] - hedging with futures involves rolling, and the roll cost or benefit affects hedge economics.
- [[Correlation]] - the hedge ratio depends on correlation. When correlation breaks down ([[Structural Break]]), the hedge fails.
- [[Convexity]] - option based hedges provide convex protection (limited cost, unlimited protection). Futures hedges are linear.
- [[Liquidity Risk]] - a hedge is only effective if both legs can be maintained. Illiquid hedging instruments create their own risks.
- [[Cost of Carry]] - the theoretical relationship between the hedging instrument (futures) and the underlying exposure (physical).

## Common misconceptions

**"A hedge means zero risk."** A hedge reduces risk but introduces basis risk, roll risk, margin risk, and counterparty risk. The net risk is lower but not zero.

**"You should always hedge."** Hedging has costs. If the cost of hedging (spreads, roll, margin) exceeds the expected benefit, it may be rational to accept the risk. Many commodity producers selectively hedge only when prices are favorable.

**"Hedging and speculation are opposites."** A hedge on an underlying exposure is risk reducing. But many "hedges" are actually speculative: an airline choosing to hedge 100% of next year's fuel at current prices is making an implicit bet that prices will rise. The DEGREE of hedging is itself a directional decision.

## Sources

- Hull, Options, Futures, and Other Derivatives, Chapter 3 (Hedging Strategies Using Futures)
- CME Group: Hedging with Commodity Futures
- Stulz, Rene, "Rethinking Risk Management" (1996)
