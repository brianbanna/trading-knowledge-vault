---
aliases: [convexity, non-linear payoff, crisis alpha, tail hedge, asymmetric payoff]
tags:
  - "#risk"
date-added: "2026-03-20"
---

# Convexity

## Definition

Convexity is a nonlinear relationship between an input and an output. A convex position gains disproportionately more from large moves than it loses from small ones. The P&L curve bends upward. Options are the classic convex instrument: a call costs a fixed premium and pays unlimited upside. Convexity is what makes [[Safe Haven Assets]] valuable in portfolios — they accelerate their protection as stress worsens. The opposite is concavity: a position that loses more than proportionally from large moves, like a short option.

## Why it matters (commodities and FX)

Commodity markets produce extreme moves ([[Supply Shock|supply shocks]], [[Geopolitical Risk]], weather) with fat tailed return distributions. A portfolio convex to these moves gains disproportionately during crises. A concave portfolio (short vol, mean reversion at extremes) loses disproportionately. Knowing your convexity profile tells you whether you survive a tail event or get wiped out.

Gold has natural portfolio convexity: its [[Correlation]] with equities becomes more negative as the equity drawdown deepens. A 5% equity drop sees gold up 2%. A 20% crash sees gold up 15%. That acceleration is convexity, and it is why institutional allocators hold gold beyond what its average return alone justifies.

## Concrete example

**Concrete:** Long [[Brent Crude]] position worth $1M. Buy a 3 month 10% OTM put for $2/bbl on 10,000 barrels, costing $20,000.
- Brent flat: lose $20,000 premium. Linear.
- Brent −5%: put still OTM. Loss $50,000 on position, put ≈ $5,000. Net ≈ −$45,000.
- Brent −20%: put 10% ITM. Loss $200,000, put pays ≈ $100,000. Net ≈ −$120,000. Put offset 40%.
- Brent −40% (crisis): put 30% ITM. Loss $400,000, put pays ≈ $300,000. Net ≈ −$120,000. Put offset 75%.

Protection accelerates with the size of the move. The cost is the premium paid during normal periods.

**Simplified:** A convex hedge does almost nothing on small moves but pays huge on big ones. You pay a small known cost (the premium) every period to own a payoff that explodes during a crash. A concave position is the opposite: it earns a steady small return and then occasionally wipes you out. Most carry, vol selling, and mean reversion strategies are concave. Most option buying, long vol, and trend following strategies are convex. Convexity is the shape of your risk, not its size.

## Key mechanics and formulas

**Option convexity (gamma):**
`P&L from move = Delta × ΔS + 0.5 × Gamma × (ΔS)²`

The gamma term grows with the square of the price move. That is the mathematical source of convexity.

**Portfolio convexity:**
A portfolio is convex if `∂²(Portfolio Value) / ∂(Risk Factor)² > 0`. Second derivative positive, P&L curve bends upward.

**Convexity ratio:**
`Convexity = |P&L at −3σ| / (3 × |P&L at −1σ|)`

Above 1: convex. Below 1: concave. Equal to 1: linear.

## Prerequisites
- [[Volatility]]
- [[Hedging]]
- [[Correlation]]

## Related concepts (learn next)
- [[Safe Haven Assets]] derive their portfolio value from convexity, not average returns.
- [[Hedging]] — options give convex hedges, futures give linear hedges.
- [[Volatility]] — option convexity (gamma) is highest when implied vol is low. Buying convexity cheap is the classic crisis alpha play.
- [[Risk-On Risk-Off]] — convex assets (gold, Treasuries, long vol) outperform in risk off transitions.
- [[Mean Reversion]] — most mean reversion strategies are concave. Option overlays restore convexity.
- [[Structural Break]] — convexity protects when the model breaks. Without it, model failure equals catastrophic loss.

## Common misconceptions

**"Convexity is free."** Convexity always costs. Options decay (theta), gold pays no yield, crash protection has carry. The question is whether the cost beats the protection.

**"Only option traders need to think about convexity."** Every portfolio has a convexity profile. Mean reversion books are concave. Trend following books are convex. Long commodity and long commodity currency books are concave to risk off events.

**"Convexity and leverage are the same."** Leverage amplifies linearly (2x gains and 2x losses). Convexity amplifies asymmetrically. Different risk properties.

## Sources

- Taleb, Nassim Nicholas, "Antifragile" (2012)
- Ilmanen, "Expected Returns" (2011), chapter on tail risks and convexity
- Bhansali, Vineer, "Tail Risk Hedging" (2013)
