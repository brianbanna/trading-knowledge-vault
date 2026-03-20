---
aliases: [volatility smile, vol smile, volatility skew, vol skew, skew]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-20"
---

# Volatility Smile

## Definition
The volatility smile (or skew) is the pattern of [[Implied Volatility]] across different strike prices for options sharing the same expiry date on a given underlying. In a world where the Black Scholes model held perfectly, IV would be identical at every strike, but in reality IV varies systematically. In equity markets, IV is typically higher for out of the money puts than for at the money options, creating an asymmetric "smirk" (negative skew) that reflects crash protection demand. In commodity markets, IV can be higher for out of the money calls (positive skew) because supply disruptions cause sudden upside price spikes. The smile is visualized by plotting IV on the vertical axis against [[Delta]] or moneyness (strike/spot) on the horizontal axis. The shape reveals which direction the market fears most and how much premium it assigns to tail risk relative to normal sized moves.

## Why it matters (commodities and FX)
The skew tells traders where the market perceives asymmetric risk, providing information that the futures price alone cannot convey. In crude oil markets, positive call skew (call IV exceeding put IV) signals that participants are paying up for protection against supply shock induced price spikes. In FX, [[risk reversal]] (the difference between 25 delta call and 25 delta put IV) is the standard measure of skew and is itself an actively traded instrument. Changes in skew are tradeable signals: widening call skew in crude ahead of geopolitical tension suggests the market is pricing in more upside tail risk. The [[butterfly]] spread measures the overall fatness of both tails relative to the center, capturing pure convexity demand independent of direction.

## Concrete example
**Success case:** Brent crude 1 month options show ATM IV at 25%, 25 delta call IV at 28%, and 25 delta put IV at 23%. The risk reversal is +5% (call skew). A trader interprets this as the market over pricing supply disruption fear and sells the 25 delta calls (expensive) while buying 25 delta puts (cheap), creating a short risk reversal. Over the next 3 weeks, geopolitical fears fade, call IV drops to 25.5% and put IV rises to 24.5%. The risk reversal narrows from +5% to +1%, and the trader profits approximately $1,800 per contract from the skew compression.

**Failure case:** A trader sells the call skew in natural gas options heading into winter, expecting the +8% risk reversal to compress. A polar vortex drives Henry Hub from $3.50 to $7.00 in 2 weeks. The 25 delta calls become deep in the money, the risk reversal blows out to +18%, and the short risk reversal loses $12,000 per contract. The lesson: selling commodity call skew is effectively selling insurance against supply shocks, which can produce catastrophic losses when the tail event materializes.

## Key mechanics and formulas
- **Risk reversal (skew measure):** RR = 25 delta call IV - 25 delta put IV. Positive RR = call skew (upside fear). Negative RR = put skew (downside fear).
- **Butterfly (smile curvature):** BF = (25 delta call IV + 25 delta put IV) / 2 - ATM IV. High BF = fat tails on both sides; the market expects big moves. Low BF = thin tails.
- **Skew patterns by asset class:**
  - Equities: negative skew (put skew), reflecting crash protection demand since 1987
  - Commodities: often positive skew (call skew), reflecting supply disruption risk
  - FX: varies by pair and regime (JPY pairs often exhibit call skew reflecting yen safe haven rallies)
- **Skew dynamics:** Skew steepens during periods of stress and flattens during calm. In commodities, call skew steepens when inventory is low ([[Stocks to Use Ratio]] tight) and flattens when inventory is high.
- **Vanna:** The sensitivity of delta to vol (equivalently, the sensitivity of vega to spot). Skew creates vanna exposure that affects spot prices through dealer hedging flows.

## Prerequisites
- [[Implied Volatility]]
- [[Option]]
- [[Futures Contract]]

## Related concepts (learn next)
- [[Implied Volatility]] is the foundational concept; the smile describes how IV varies across strikes.
- [[Option]] pricing models must be adjusted to account for the smile, as Black Scholes assumes flat vol across strikes.
- [[Weather Premium]] in agricultural options creates seasonal skew patterns where call skew steepens during growing season.
- [[COT Positioning]] extremes can coincide with skew extremes, as speculative crowding drives demand for directional protection.
- [[Basis Risk]] exists between the skew on one underlying and the skew on a correlated underlying used as a hedge.
- [[Spread Trade]] strategies like risk reversals and butterflies are the standard instruments for trading the smile directly.
- [[Margin]] requirements for short skew positions can increase rapidly when the smile steepens.

## Common misconceptions
- **"The smile is symmetric."** In most markets, the smile is asymmetric (a smirk or skew), reflecting directional fear rather than equal concern about both tails. Symmetric smiles are the exception, not the rule.
- **"Skew is constant over time."** Skew changes dynamically. It steepens during crises and flattens during calm periods. These regime shifts in skew are themselves tradeable opportunities.
- **"Positive commodity skew means the market is bullish."** Positive call skew means the market assigns elevated probability to extreme upside moves (supply shocks), not that it expects prices to rise on average. Skew reflects tail risk pricing, not directional expectation.
- **"You can ignore skew for ATM options."** Even ATM option traders must understand skew because delta hedging an ATM option in a skewed vol surface creates P&L from vanna and volga that does not exist in a flat vol world.

## Sources
- Sheldon Natenberg, "Option Volatility and Pricing"
- Emanuel Derman, "The Volatility Smile"
- CME Group, "Commodity Option Skew Analysis"
- Jim Gatheral, "The Volatility Surface: A Practitioner's Guide"
