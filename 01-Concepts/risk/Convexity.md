---
aliases: [convexity, non-linear payoff, crisis alpha, tail hedge, asymmetric payoff]
tags:
  - "#risk"
date-added: "2026-03-20"
---

# Convexity

## Definition

Convexity describes a non-linear relationship between an input and an output. In trading, a convex position gains disproportionately more from large moves than it loses from small ones. Graphically, the P&L curve bends upward (concave to the origin). Options are the classic convex instrument: buying a call option costs a fixed premium but offers unlimited upside. Convexity is the property that makes [[Safe Haven Assets]] valuable in portfolios: they do not just protect, they ACCELERATE their protection as the stress gets worse. The opposite of convexity is concavity (a position that loses more than proportionally from large moves, like a short option position).

## Why it matters (commodities and FX)

Commodity markets are prone to extreme moves ([[Supply Shock|supply shocks]], [[Geopolitical Risk]], weather events) that produce non-normal return distributions with fat tails. A portfolio that is convex to these moves gains disproportionately during crises. A portfolio that is concave (short options, short vol, mean reversion strategies at extremes) loses disproportionately. Understanding your portfolio's convexity profile tells you whether you will survive a tail event or be destroyed by it.

Gold has natural convexity in a portfolio context: its [[Correlation]] with equities becomes more negative as the equity drawdown deepens. A 5% equity drop might see gold up 2%. A 20% equity crash might see gold up 15%. This accelerating protection is convexity, and it is why institutional allocators hold gold beyond what its average return alone would justify.

## Concrete example

**Crude oil put option as hedge:** You hold a long [[Brent Crude]] position worth $1 million. You buy a 3 month 10% out of the money put for $2/bbl (cost: ~$20,000 on 10,000 barrels). Scenarios:

- Brent stays flat: you lose $20,000 (the premium). Linear cost.
- Brent drops 5%: put is still out of the money. Loss = $50,000 on position, put = ~$5,000 value (still mostly lost). Net = ~$45,000 loss.
- Brent drops 20%: put is 10% in the money. Loss = $200,000 on position, put pays ~$100,000. Net = ~$120,000 loss. The put offset 40% of the loss.
- Brent drops 40% (crisis): put is 30% in the money. Loss = $400,000 on position, put pays ~$300,000. Net = ~$120,000 loss. The put offset 75% of the loss.

The protection accelerates as the move gets larger. That is convexity. The cost is the premium paid during normal times (small, predictable losses).

**Mean reversion concavity:** A trader selling the [[Brent-WTI Spread]] at 2 sigma, expecting reversion. Small mean reversion: +$0.50/bbl profit. If the spread moves to 5 sigma instead (structural break): -$5/bbl loss. The strategy loses disproportionately on large moves. This is concavity, and it is the hidden risk in most relative value strategies.

## Key mechanics and formulas

**Option convexity (gamma):**
`P&L from move = Delta x ΔS + 0.5 x Gamma x (ΔS)²`

The gamma term (0.5 x Gamma x ΔS²) grows with the SQUARE of the price move. This is the mathematical source of convexity: large moves produce disproportionately more P&L than small ones.

**Portfolio convexity:**
A portfolio has positive convexity if: `∂²(Portfolio Value) / ∂(Risk Factor)² > 0`

The second derivative of value with respect to the risk factor is positive. The P&L curve bends upward.

**Convexity ratio:**
`Convexity = |P&L at -3σ| / (3 x |P&L at -1σ|)`

If >1: convex (tail protection accelerates). If <1: concave (tail losses accelerate). If =1: linear.

## Prerequisites
- [[Volatility]]
- [[Hedging]]
- [[Correlation]]

## Related concepts (learn next)
- [[Safe Haven Assets]] - safe havens derive their portfolio value from convexity, not average returns.
- [[Hedging]] - options provide convex hedges. Futures provide linear hedges. The choice depends on the risk profile desired.
- [[Volatility]] - option convexity (gamma) is highest when implied vol is low (options are cheap). Buying convexity in low vol environments is the classic "crisis alpha" strategy.
- [[Risk-On Risk-Off]] - convex assets (gold, Treasuries, long vol) outperform in risk off transitions.
- [[Mean Reversion]] - most mean reversion strategies are concave (limited upside, unlimited downside). Adding option overlays can restore convexity.
- [[Structural Break]] - convexity protects you when a structural break makes your model wrong. Without it, model failure = catastrophic loss.

## Common misconceptions

**"Convexity is free."** Convexity always has a cost. Buying options costs premium (theta decay). Holding gold costs the [[Real Interest Rates|real rate]] opportunity cost. Buying crash protection costs carry. The question is whether the cost is worth the protection.

**"Only option traders need to think about convexity."** Every portfolio has a convexity profile. A mean reversion book is concave. A trend following book is convex. A long commodity / long commodity currency portfolio is concave to risk off events. Understanding this without trading options is still critical.

**"Convexity and leverage are the same thing."** Leverage amplifies linearly (2x leverage = 2x gains AND 2x losses). Convexity amplifies asymmetrically (disproportionate gains vs losses). They are fundamentally different risk properties.

## Sources

- Taleb, Nassim Nicholas, "Antifragile" (2012)
- Ilmanen, "Expected Returns" (2011), chapter on tail risks and convexity
- Bhansali, Vineer, "Tail Risk Hedging" (2013)
