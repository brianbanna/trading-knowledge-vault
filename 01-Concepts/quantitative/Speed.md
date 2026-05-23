---
aliases: [speed, gamma of gamma, DgammaDspot, dGamma/dSpot, third order delta]
tags:
  - "#quant"
date-added: "2026-05-23"
---

# Speed

## Definition

Speed is the rate at which [[Gamma]] changes as spot moves. Gamma is not constant across strikes: as spot moves, the option's gamma changes. Speed = d(Gamma) / d(S) = d³(Option price) / d(S)³. Also called "gamma of gamma."

Speed captures the asymmetry of the gamma curve. Gamma peaks at the strike (for ATM options) and decays both directions. Speed describes how rapidly that peak rises or falls as spot moves through the strike. For a vanilla option, speed is large and changes sign as spot crosses the strike: positive when spot is below the strike, negative when above (for a call), reflecting approach to or away from the gamma peak.

Speed matters mainly for positions near barriers, large books with concentrated strikes, and structures where gamma is itself the traded exposure ([[Butterfly|butterflies]], gamma scalping books).

## Why it matters (commodities and FX)

Speed is a second order hedging cost greek. It explains why gamma hedging is more expensive than first order calculations suggest:

- **Gamma scalping costs.** A long gamma trader scalps delta as spot moves. Each scalp captures convexity P&L. Speed means the scalp size needed itself changes as spot moves through the strike, forecasting slippage and inventory cost beyond what gamma alone predicts.
- **Barrier options.** Knock in and knock out options have explosive speed near the barrier because gamma peaks just inside and collapses outside. Dealer books with barrier exposure track speed alongside gamma.
- **Pinning dynamics in commodities.** When [[WTI Crude Oil]] or [[Henry Hub Natural Gas]] options have huge OI at a single strike, dealer aggregate gamma peaks there. Speed across the strike produces the asymmetric flow pattern creating [[Expiry Pinning]]: hedging flows from one side are much larger than the other.
- **Cross asset feedback in 0DTE.** The 0DTE SPX gamma profile has high speed at key strikes (round numbers, prior day's close). Speed is part of what produces the "gamma flip" where dealer flows reverse sign as spot crosses a strike, creating intraday momentum cascades visible in [[Copper Futures]] and [[USDMXN]] moves.

Speed is rarely hedged explicitly. More commonly used as a diagnostic for "this position becomes unhedgeable as spot moves through this level."

## Concrete example

**Concrete:** Dealer short 200 contracts of a 25 day ATM call on [[Brent Crude]] futures. Spot $82.00, strike $82.00, vol 28%. Initial gamma per contract 0.038 per dollar, total short gamma -7.6 lots per dollar. If Brent rallies to $84, speed was negative throughout. Gamma per contract drops to 0.028, total short gamma -5.6. If Brent dropped to $80, speed was positive. Gamma per contract grew to 0.041, total -8.2. The $2 move from $82 to $80 increased gamma 8%. The $2 move from $82 to $84 decreased gamma 26%. Asymmetric. If spot oscillates around $82, hedging requirement changes nonlinearly with each move. For barrier options the effect is far larger: a knock out call with barrier at $90 has a near vertical gamma profile just below the barrier, with gamma collapsing to zero above. Hedging requirements swing by factors of 5 to 10 within a $0.50 range.

**Simplified:** Gamma is not the same on both sides of the strike. As spot moves, gamma changes shape. Speed measures that change. A trader who hedges as if gamma is constant gets caught when spot drifts: their hedge ratio was right at the start, wrong after the move. The bigger the move, the more wrong. Near barriers the effect is extreme because gamma collapses to zero on one side and stays large on the other. Speed warns you when your hedge is about to become unstable.

## Key mechanics and formulas

**Speed for a vanilla option (Black Scholes):**

`Speed = -Gamma / S × (d1 / (σ × sqrt(T)) + 1)`

Or:
`Speed = - e^(-qT) × N'(d1) × (d1 + σ × sqrt(T)) / (S² × σ² × T)`

Structure to remember: speed scales as 1/S² and grows as 1/T as expiry approaches.

**Useful intuition:**
- Speed is zero at the gamma peak (slightly above strike for calls, slightly below for puts due to vol drift)
- Speed is large positive when spot is below the gamma peak (gamma growing as spot rises)
- Speed is large negative when spot is above the gamma peak (gamma falling)
- Speed magnitude grows as T → 0

**Approximation for ATM near expiry:**

`Speed_ATM ≈ - Gamma_ATM / (S × σ × sqrt(T))`

For near expiry ATM with sqrt(T) very small, speed becomes very large per unit spot move.

**Practical use:**

Speed forecasts hedge ratio adjustments:
`ΔHedge ≈ Gamma × ΔS + 0.5 × Speed × (ΔS)²`

The second term shows the hedge requirement grows nonlinearly with move size. For small moves (< 0.5% of spot), the first term dominates. For large moves the speed term becomes material.

**Barrier dynamics:**

Near a barrier, speed effectively goes to infinity at the barrier level for a knock out, reflecting payoff discontinuity. Numerical implementations cap this for stability; the underlying risk is real.

## Prerequisites
- [[Gamma]]
- [[Delta]]
- [[Greeks]]
- [[Option]]
- [[Black Scholes Model]]

## Related concepts (learn next)
- [[Gamma]] - speed is the spot derivative of gamma.
- [[Color]] - time derivative of gamma. Speed and color together describe gamma evolution.
- [[Zomma]] - vol derivative of gamma. The full third order gamma family.
- [[Barrier Option]] - barriers create extreme speed near the trigger, dominating hedge management.
- [[0DTE]] - 0DTE options have large speed near key strikes, contributing to gamma cascades.
- [[Expiry Pinning]] - pinning at round number strikes is driven by speed changing sign across the strike.
- [[Butterfly]] - butterflies are pure gamma trades; speed makes their P&L path dependent.

## Common misconceptions

**"Gamma is constant near the strike."** Not close. Gamma changes with spot (speed), time (color), vol (zomma). Speed dominates intraday spot movement.

**"Speed only matters for exotics."** Wrong. Vanilla options have material speed near expiry. Dealer hedging books track speed for all near expiry ATM positions.

**"Symmetric gamma profile means symmetric speed."** Speed is the rate of change of gamma. Speed is largest in magnitude where the gamma slope is steepest, not where gamma itself is largest. Speed peaks on either side of the gamma peak, not at it.

**"Speed is too high order to be tradeable."** Speed is not directly tradeable but its effects show in P&L of any gamma trading book. Practitioners include it in greek reports and risk limits.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form speed and other third order greeks.
- Taleb, Nassim Nicholas. *Dynamic Hedging*. Treatment of higher order greeks and gamma scalping.
- Wystup, Uwe. *FX Options and Structured Products*. Discussion of speed in barrier option hedging.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Bossens et al. "Vanna Volga Methods Applied to FX Derivatives." Discussion of gamma profile dynamics.
