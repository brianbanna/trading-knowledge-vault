---
aliases: [color, colour, gamma decay, DgammaDtime, dGamma/dTime, gamma bleed]
tags:
  - "#quant"
date-added: "2026-05-23"
---

# Color

## Definition

Color (also spelled colour) is the third order greek that measures the rate at which [[Gamma]] changes as time passes. Plain English: gamma is not constant. As an option approaches expiry, gamma concentrates around the strike and explodes for ATM options. Color tells you how fast that change happens. Mathematically, color = d(Gamma) / d(t) = d³(Option price) / d²(S) × d(t).

Color is the "gamma bleed" or "gamma growth" depending on moneyness. For an ATM option close to expiry, gamma grows rapidly as expiry approaches, so color is large positive. For deep ITM or OTM options near expiry, gamma decays as the option becomes more binary, so color is negative.

Color is one of the least quoted greeks because it is only meaningful in the final week or two of an option's life. For long dated positions it is negligible. For short dated and [[0DTE]] positions, color drives the explosive growth of gamma into the final hours.

## Why it matters (commodities and FX)

Color is what makes the final week of any expiring option position dangerous:

- **Gamma growth into expiry.** A dealer short 1 month ATM options at the start of the month has moderate gamma. By the final week, color has caused gamma to grow several fold. The hedging burden ramps up nonlinearly. Dealers know this and either close positions early or accept the gamma management cost.
- **0DTE behavior.** In a single trading session, color causes 0DTE gamma to grow from "large" at the open to "enormous" in the final hour. This is why dealer hedging flows accelerate into the close: the gamma profile is steepening continuously, not just because spot is approaching the strike.
- **Commodity options near delivery.** [[WTI Crude Oil]] and [[Henry Hub Natural Gas]] options expire days before underlying futures. Color produces a gamma profile that peaks just before option expiry, often coinciding with thin liquidity in the underlying futures. This is when [[Expiry Pinning]] and squeeze dynamics emerge.
- **Risk reports.** Color is included in greek reports for sophisticated option books precisely because it forecasts how the gamma exposure will evolve over the next days, allowing pre emptive hedging or position reduction.

For most non market making traders, color does not need to be actively hedged, but understanding it explains why short dated options become unmanageable in their final days.

## Concrete example

A dealer is short 100 contracts of an ATM call on [[ES Futures]] with 15 days to expiry. Spot ES: 5400. Implied vol: 13%. Initial gamma per contract: 0.0012 per dollar of spot move. Total short gamma: -0.12.

Reading: a $1 move in ES adds 12 lots of delta to hedge. Manageable.

10 days pass. Spot ES still at 5400 (just for the example). 5 days remain. Color has been positive throughout. Gamma per contract has grown from 0.0012 to 0.0028. Total short gamma: -0.28.

Now a $1 move adds 28 lots of delta to hedge. Hedging cost (bid ask, slippage) more than doubled even though nothing else changed.

3 days remain. Gamma per contract: 0.0044. Total short gamma: -0.44.

Last day, mid morning: Gamma per contract: 0.011. Total short gamma: -1.1. A $1 ES move now adds 110 lots of delta to hedge. Dealer is forced to either close the position (paying through the spread) or accept enormous intraday hedging costs.

The color profile across the 15 days:
- Day 1 to 7: color small positive, gamma growing slowly
- Day 8 to 12: color larger, gamma growing 30% per day
- Day 13 to 15: color extreme, gamma can double per day

If the dealer had recognized the color trajectory at day 5, they could have closed half the position when gamma was still manageable, paying small bid ask spread, rather than fighting exploding gamma in the final hours.

What if spot had moved away from the strike (to 5500 by day 10)? Then color would have been negative for these now OTM options. Gamma would shrink, hedging burden disappears. Color is path dependent: the same option can have positive color when ATM and negative color when far OTM.

## Key mechanics and formulas

**Color for a vanilla option (Black Scholes):**

`Color = -e^(-qT) × N'(d1) / (2 × S × T × σ × sqrt(T)) × [2qT + 1 + (2(r-q)T - d2 × σ × sqrt(T)) × d1 / (σ × sqrt(T))]`

Most practitioners do not compute this from scratch; they read it from their pricing system. The structure to remember: color scales roughly as 1/(T × sqrt(T)) for ATM options, meaning it grows very fast as T → 0.

**Useful intuition:**
- Color is positive for ATM options (gamma growing into expiry)
- Color is negative for deep ITM and deep OTM options (gamma decaying as option becomes binary)
- Color magnitude grows roughly as 1/T^(3/2) for ATM, much faster than vega or theta decay
- For [[0DTE]] ATM options, color per hour can exceed initial gamma

**ATM approximation:**

`Gamma_ATM ≈ N'(0) / (S × σ × sqrt(T))`

Differentiating with respect to T:
`Color_ATM ≈ N'(0) / (2 × S × σ × T^(3/2))`

This 1/T^(3/2) scaling is why color matters only near expiry but matters enormously there.

**Gamma trajectory:** integrating color forward predicts how gamma will evolve. For an ATM option:
`Gamma(T - dt) ≈ Gamma(T) × sqrt(T / (T - dt))`

A 30 day option becoming a 5 day option sees gamma grow by sqrt(30/5) ≈ 2.45 times, all else equal.

## Prerequisites
- [[Gamma]]
- [[Greeks]]
- [[Option]]
- [[Black Scholes Model]]
- [[Theta]]

## Related concepts (learn next)
- [[Gamma]] - color is the time derivative of gamma, so understanding gamma is the prerequisite.
- [[Charm]] - charm is to delta what color is to gamma. Both are time bleeds of spot greeks.
- [[Veta]] - veta is to vega what color is to gamma. The full family of time bleed greeks.
- [[Speed]] - speed is the spot derivative of gamma (dGamma/dSpot). Color and speed together describe how gamma evolves under the two main forcing variables.
- [[0DTE]] - 0DTE positions experience enormous color, with gamma growing severalfold over a single trading session.
- [[Expiry Pinning]] - color combined with gamma drives pinning behavior at high open interest strikes near expiry.
- [[Theta]] - color and theta both accelerate near expiry but tell different stories: theta is the cost of holding, color is the gamma growth driving hedging cost.

## Common misconceptions

**"Gamma is constant for the life of the option."** Wrong. Gamma changes with spot (via speed), with vol (via zomma), and with time (via color). Color is the time channel of gamma evolution.

**"Color only matters for exotic options."** Wrong. Standard vanilla options have material color in their final two weeks. Any short dated option position needs color awareness for hedging cost forecasting.

**"Positive color is good for short option positions."** False. Positive color means your gamma exposure is growing. If you are short options (short gamma), positive color means your short gamma is becoming MORE negative, increasing hedging difficulty. Positive color is good only for long gamma holders who want their convexity to grow.

**"Color is just another name for gamma decay."** Wrong. Color can be positive (gamma growing) or negative (gamma decaying), depending on moneyness. ATM options have positive color near expiry. Deep OTM options have negative color near expiry.

**"You can ignore color if you do not trade near expiry."** True for monthly options held weeks from expiry. Not true once you enter the final week. For [[0DTE]] traders, color is a first order concern from the moment the position is put on.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form color and other third order greeks.
- Taleb, Nassim Nicholas. *Dynamic Hedging*. Discussion of higher order greeks and near expiry dynamics.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Sinclair, Euan. *Positional Option Trading*. Practical discussion of near expiry gamma management.
- Wystup, Uwe. *FX Options and Structured Products*. Treatment of gamma evolution in dealer FX books.
