---
aliases: [hedging, hedge, risk offset, portfolio hedge]
tags:
  - "#risk"
date-added: "2026-03-20"
---

# Hedging

## Definition

Hedging is taking an offsetting position in a related instrument to reduce the risk of an existing exposure. A perfect hedge eliminates all price risk and all profit potential. In practice, hedges are imperfect: the hedge instrument does not move 1:1 with the exposure, leaving residual [[Basis]] risk. Hedging is distinct from [[Relative Value Trade|relative value trading]]: a hedge protects an existing position, while a relative value trade aims to profit from a spread. The instruments look identical; the intent and risk management differ.

## Why it matters (commodities and FX)

Hedging is the reason commodity futures markets exist. Producers (oil companies, miners, farmers) sell futures to lock prices for future production. Consumers (airlines, refiners, food companies) buy futures to lock input costs. Producer and consumer hedging creates the fundamental supply and demand that speculators trade against.

For a trader running a relative value book, hedging manages residual risks that spreads do not eliminate. A [[Calendar Spread]] hedges directional price risk but leaves curve risk. A [[Brent-WTI Spread]] hedges oil direction but leaves location basis. The skill is knowing what is hedged and what is not, then deciding which residuals to keep (edge) and which to offset.

## Concrete example

**Concrete:** An airline expects 100 million gallons of jet fuel next year at $2.50/gal. Risk: jet fuel rises to $3.50, costs rise $100M. Hedge: buy crude futures (no liquid jet fuel futures). 100 million gallons ≈ 2.38 million barrels. Buy 2,380 WTI contracts. WTI rises 30% from $74 to $96; futures gains offset most of the jet fuel cost rise. Basis risk: jet fuel may not move with WTI 1:1. The crack spread can widen or narrow. The hedge is directionally effective, imperfect on basis.

**Simplified:** You have an exposure that loses money if a price moves a certain way. You take a position in something similar that gains when that move happens. If the two prices move together, the gain offsets the loss. They almost never move together perfectly, so a small residual risk (basis) remains. Hedging trades large price risk for smaller basis risk plus a cost (spreads, roll, margin). You hedge when the residual risk is worth less than the original exposure was costing you to carry.

## Key mechanics and formulas

**Optimal hedge ratio (minimum variance):**
`h* = Cov(ΔS, ΔF) / Var(ΔF) = ρ × (σ_S / σ_F)`

h* = number of futures contracts per unit of exposure, ρ = [[Correlation]] between spot and futures changes, σ_S = spot vol, σ_F = futures vol.

**Hedge effectiveness:**
`R² = ρ²`

R² of 0.85 means the hedge explains 85% of price variation. The remaining 15% is basis.

**Cost of hedging:**
- Direct: [[Bid-Ask Spread]], commissions, margin financing
- Indirect: opportunity cost of forgone favorable moves
- Roll: in [[Contango]] markets, [[Roll Yield]] erodes hedge value

**Hedge P&L:**
`Total P&L = Physical P&L + Hedge P&L`
`= (S_end − S_start) × Quantity − h × (F_end − F_start) × Contract Size`

## Prerequisites
- [[Forward Curve]]
- [[Basis]]
- [[Correlation]]
- [[Relative Value Trade]]

## Related concepts (learn next)
- [[Basis]] — the risk that the hedge instrument does not move perfectly with the exposure. The primary risk in any hedge.
- [[Roll Yield]] — hedging with futures involves rolling; roll cost or benefit affects hedge economics.
- [[Correlation]] — the hedge ratio depends on correlation. When correlation breaks ([[Structural Break]]), the hedge fails.
- [[Convexity]] — option based hedges are convex (limited cost, unlimited protection). Futures hedges are linear.
- [[Liquidity Risk]] — a hedge is only effective if both legs can be maintained.
- [[Cost of Carry]] — theoretical relationship between hedge instrument (futures) and underlying exposure (physical).

## Common misconceptions

**"A hedge means zero risk."** A hedge reduces risk but introduces basis, roll, margin, and counterparty risk. Net risk falls but is not zero.

**"You should always hedge."** Hedging costs spreads, roll, and margin. If the cost exceeds the expected benefit, accepting the risk is rational. Many producers selectively hedge only at favorable prices.

**"Hedging and speculation are opposites."** A hedge on an underlying exposure is risk reducing. Many "hedges" are speculative: an airline hedging 100% of next year's fuel at current prices is implicitly betting prices rise. The degree of hedging is itself a directional decision.

## Sources

- Hull, Options, Futures, and Other Derivatives, Chapter 3 (Hedging Strategies Using Futures)
- CME Group: Hedging with Commodity Futures
- Stulz, Rene, "Rethinking Risk Management" (1996)
