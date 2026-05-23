---
aliases: [color, colour, gamma decay, DgammaDtime, dGamma/dTime, gamma bleed]
tags:
  - "#quant"
date-added: "2026-05-23"
---

# Color

## Definition

Color is the rate at which [[Gamma]] changes as time passes. Gamma is not constant: as expiry approaches, gamma concentrates around the strike and explodes for ATM options. Color = d(Gamma) / d(t) = d³(Option price) / d²(S) × d(t).

Color is positive (gamma growing) for ATM options near expiry. Color is negative (gamma decaying) for deep ITM and deep OTM options near expiry as they become more binary.

Color is meaningful in the final week or two of an option's life. Negligible for long dated positions. Drives the explosive gamma growth into the final hours of [[0DTE]] positions.

## Why it matters (commodities and FX)

Color makes the final week of any expiring option position dangerous:

- **Gamma growth into expiry.** A dealer short 1 month ATM options at month start has moderate gamma. By the final week, color has multiplied gamma several fold. Hedging burden ramps nonlinearly. Dealers close positions early or accept the gamma management cost.
- **0DTE behavior.** Color causes 0DTE gamma to grow from "large" at open to "enormous" in the final hour. Dealer hedging flows accelerate into the close because the gamma profile steepens continuously, not just because spot approaches the strike.
- **Commodity options near delivery.** [[WTI Crude Oil]] and [[Henry Hub Natural Gas]] options expire days before underlying futures. Color produces a gamma profile peaking just before option expiry, coinciding with thin underlying liquidity. [[Expiry Pinning]] and squeeze dynamics emerge here.
- **Risk reports.** Sophisticated option books include color to forecast gamma evolution over coming days, enabling pre emptive hedging or position reduction.

Non market makers do not actively hedge color, but understanding it explains why short dated options become unmanageable in their final days.

## Concrete example

**Concrete:** Dealer short 100 contracts of an ATM call on [[ES Futures]] with 15 days to expiry. Spot 5400, vol 13%, gamma per contract 0.0012, total short gamma -0.12. A $1 move adds 12 lots to hedge. Manageable. 10 days pass at spot 5400. Color has been positive: gamma per contract grew to 0.0028, total -0.28. Hedging cost more than doubled with nothing else changed. 3 days left: gamma per contract 0.0044, total -0.44. Last day mid morning: gamma per contract 0.011, total -1.1. A $1 ES move now adds 110 lots. Dealer closes the position into the spread or absorbs enormous hedging cost.

**Simplified:** Gamma grows as expiry approaches for options near the strike. Color is the speed of that growth. Early in the life of an option, gamma changes slowly. In the final week it doubles every few days. In the final hours of a 0DTE position it doubles every hour. If you are short options, your hedging cost balloons even when nothing in the market moves. The position becomes a different beast in its final days from what it was when you put it on.

## Key mechanics and formulas

**Color for a vanilla option (Black Scholes):**

`Color = -e^(-qT) × N'(d1) / (2 × S × T × σ × sqrt(T)) × [2qT + 1 + (2(r-q)T - d2 × σ × sqrt(T)) × d1 / (σ × sqrt(T))]`

Practitioners read it from their pricing system. Structure to remember: color scales as 1/(T × sqrt(T)) for ATM options, growing fast as T → 0.

**Useful intuition:**
- Color is positive for ATM options (gamma growing into expiry)
- Color is negative for deep ITM and deep OTM options (gamma decaying as option becomes binary)
- Color magnitude grows as 1/T^(3/2) for ATM, much faster than vega or theta decay
- For [[0DTE]] ATM options, color per hour can exceed initial gamma

**ATM approximation:**

`Gamma_ATM ≈ N'(0) / (S × σ × sqrt(T))`

Differentiating with respect to T:
`Color_ATM ≈ N'(0) / (2 × S × σ × T^(3/2))`

The 1/T^(3/2) scaling is why color matters only near expiry but matters enormously there.

**Gamma trajectory:** integrating color forward predicts gamma evolution. For an ATM option:
`Gamma(T - dt) ≈ Gamma(T) × sqrt(T / (T - dt))`

A 30 day option becoming a 5 day option sees gamma grow by sqrt(30/5) ≈ 2.45 times, all else equal.

## Prerequisites
- [[Gamma]]
- [[Greeks]]
- [[Option]]
- [[Black Scholes Model]]
- [[Theta]]

## Related concepts (learn next)
- [[Gamma]] - color is the time derivative of gamma.
- [[Charm]] - delta analog. Charm and color are both time bleeds.
- [[Veta]] - vega analog. The full family of time bleed greeks.
- [[Speed]] - spot derivative of gamma. Color and speed together describe gamma evolution.
- [[0DTE]] - 0DTE positions see gamma grow severalfold in a session via color.
- [[Expiry Pinning]] - color plus gamma drive pinning at high open interest strikes.
- [[Theta]] - both accelerate near expiry but tell different stories.

## Common misconceptions

**"Gamma is constant for the life of the option."** Wrong. Gamma changes with spot (speed), vol (zomma), and time (color).

**"Color only matters for exotic options."** Wrong. Standard vanilla options have material color in their final two weeks.

**"Positive color is good for short option positions."** False. Positive color means gamma exposure is growing. Short gamma plus positive color means MORE negative gamma. Positive color is good only for long gamma holders.

**"Color is just another name for gamma decay."** Wrong. Color can be positive or negative depending on moneyness. ATM options have positive color near expiry. Deep OTM options have negative color near expiry.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form color and other third order greeks.
- Taleb, Nassim Nicholas. *Dynamic Hedging*. Discussion of higher order greeks and near expiry dynamics.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Sinclair, Euan. *Positional Option Trading*. Practical discussion of near expiry gamma management.
- Wystup, Uwe. *FX Options and Structured Products*. Treatment of gamma evolution in dealer FX books.
