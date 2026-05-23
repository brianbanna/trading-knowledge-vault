---
aliases: [volatility smile, vol smile, volatility skew, vol skew, skew]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-20"
---

# Volatility Smile

## Definition
The volatility smile (or skew) is the pattern of [[Implied Volatility]] across different strikes for options sharing the same expiry on a given underlying. Under Black Scholes, IV would be identical at every strike. In reality IV varies systematically. In equities, IV is higher for OTM puts than for ATM, creating an asymmetric smirk (negative skew) that reflects crash protection demand. In commodities, IV can be higher for OTM calls (positive skew) because supply disruptions cause sudden upside spikes. The smile is visualized by plotting IV on the vertical axis against [[Delta]] or moneyness (strike/spot) on the horizontal. The shape reveals which direction the market fears most and how much premium it assigns to tail risk relative to normal sized moves.

## Why it matters (commodities and FX)
Skew shows where the market perceives asymmetric risk — information the futures price alone cannot convey. In crude, positive call skew (call IV above put IV) signals that participants are paying up for protection against supply shock spikes. In FX, [[risk reversal]] (25 delta call IV minus 25 delta put IV) is the standard skew measure and is itself actively traded. Changes in skew are tradeable signals: widening call skew in crude ahead of geopolitical tension signals more upside tail risk. The [[butterfly]] spread measures fatness of both tails relative to the center, capturing pure convexity demand independent of direction.

## Concrete example
**Concrete:** Brent 1 month options show ATM IV at 25%, 25 delta call IV at 28%, 25 delta put IV at 23%. Risk reversal: +5% (call skew). A trader reads this as the market over pricing supply disruption fear, sells 25 delta calls (expensive), buys 25 delta puts (cheap), creating a short risk reversal. Over 3 weeks geopolitical fears fade, call IV drops to 25.5%, put IV rises to 24.5%. Risk reversal narrows from +5% to +1%. Profit roughly $1,800 per contract from skew compression. Risk: selling commodity call skew is selling insurance against supply shocks. If a polar vortex or geopolitical event hits, the short risk reversal blows out for catastrophic losses.

**Simplified:** Options on the same underlying with the same expiry should have the same implied vol in theory. They do not. The market charges more for some strikes than others based on where it fears the price might go. A higher IV on OTM puts means the market is paying for downside protection. A higher IV on OTM calls means the market is paying for upside protection. Trading the skew means betting on how this asymmetry will evolve, not betting on direction directly.

## Key mechanics and formulas
- **Risk reversal (skew):** RR = 25 delta call IV − 25 delta put IV. Positive = call skew (upside fear). Negative = put skew (downside fear).
- **Butterfly (curvature):** BF = (25 delta call IV + 25 delta put IV) / 2 − ATM IV. High = fat tails on both sides; market expects big moves. Low = thin tails.
- **Skew by asset class:**
  - Equities: negative skew (put skew), since 1987
  - Commodities: often positive skew (call skew), supply disruption risk
  - FX: varies by pair (JPY pairs often show call skew reflecting yen safe haven rallies)
- **Skew dynamics:** steepens in stress, flattens in calm. In commodities, call skew steepens when inventory is low ([[Stocks to Use Ratio]] tight) and flattens when inventory is high.
- **Vanna:** sensitivity of delta to vol (equivalently, sensitivity of vega to spot). Skew creates vanna exposure affecting spot via dealer hedging.

## Prerequisites
- [[Implied Volatility]]
- [[Option]]
- [[Futures Contract]]

## Related concepts (learn next)
- [[Implied Volatility]] is the foundational concept; smile describes how IV varies across strikes.
- [[Option]] pricing models must adjust for the smile; Black Scholes assumes flat vol.
- [[Weather Premium]] in agricultural options creates seasonal skew patterns where call skew steepens during growing season.
- [[COT Positioning]] extremes can coincide with skew extremes as crowding drives demand for directional protection.
- [[Basis Risk]] exists between skew on one underlying and skew on a correlated underlying used as a hedge.
- [[Spread Trade]] strategies (risk reversals, butterflies) are the standard instruments for trading skew directly.
- [[Margin]] for short skew positions can rise rapidly when the smile steepens.

## Common misconceptions
- **"The smile is symmetric."** In most markets the smile is asymmetric (a smirk), reflecting directional fear. Symmetric smiles are the exception.
- **"Skew is constant."** Skew changes dynamically. Steepens during crises, flattens during calm. Regime shifts in skew are themselves tradeable.
- **"Positive commodity skew means bullish."** Positive call skew means elevated probability assigned to upside moves (supply shocks), not directional expectation. Skew reflects tail risk pricing.
- **"Skew is irrelevant for ATM options."** Even ATM traders must understand skew: delta hedging an ATM option in a skewed surface creates vanna and volga P&L that does not exist in a flat vol world.

## Sources
- Sheldon Natenberg, "Option Volatility and Pricing"
- Emanuel Derman, "The Volatility Smile"
- CME Group, "Commodity Option Skew Analysis"
- Jim Gatheral, "The Volatility Surface: A Practitioner's Guide"
