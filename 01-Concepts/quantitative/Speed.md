---
aliases: [speed, gamma of gamma, DgammaDspot, dGamma/dSpot, third order delta]
tags:
  - "#quant"
date-added: "2026-05-23"
---

# Speed

## Definition

Speed is the third order greek that measures the rate at which [[Gamma]] changes as the underlying spot price changes. Plain English: gamma is not constant across strikes. As spot moves, the option's gamma changes. Speed tells you how fast. Mathematically, speed = d(Gamma) / d(S) = d³(Option price) / d(S)³. It is sometimes called "gamma of gamma" or "the third spot derivative."

Speed captures the asymmetry of the gamma curve. Gamma peaks at the strike (for ATM options) and decays in both directions. Speed describes how rapidly that peak rises or falls as spot moves through the strike. For a typical vanilla option, speed is large and changes sign as spot crosses the strike: positive when spot is below the strike and negative when above (for a call), reflecting the fact that you are approaching or moving away from the gamma peak.

Speed matters mainly for positions near barriers, large books with concentrated strikes, and any structure where gamma is itself the traded exposure ([[Butterfly|butterflies]], gamma scalping books).

## Why it matters (commodities and FX)

Speed is a "second order hedging cost" greek. It explains why gamma hedging is more expensive than first order calculations suggest:

- **Gamma scalping costs.** A trader running a long gamma book scalps delta as spot moves. Each scalp captures some convexity P&L. But speed means the scalp size needed itself changes as spot moves through the strike. Speed forecasts hedging slippage and inventory cost beyond what gamma alone predicts.
- **Barrier options.** Knock in and knock out options have explosive speed near the barrier because gamma peaks just inside the barrier and collapses outside. Dealer books with barrier exposure track speed alongside gamma to anticipate the hedging discontinuity at the barrier level.
- **Pinning dynamics in commodities.** When [[WTI Crude Oil]] or [[Henry Hub Natural Gas]] options have huge open interest at a single strike, dealer aggregate gamma peaks at that strike. Speed across the strike level produces the asymmetric flow pattern that creates [[Expiry Pinning]]: hedging flows from one side are much larger than from the other side.
- **Cross asset feedback in 0DTE.** The 0DTE SPX gamma profile has high speed at key strikes (round numbers, prior day's close). Speed is part of what produces the "gamma flip" behavior where dealer flows reverse sign as spot crosses a strike, creating intraday momentum cascades visible in [[Copper Futures]] and [[USDMXN]] cross asset moves.

Speed is rarely hedged explicitly. It is more commonly used as a diagnostic for "this position is becoming unhedgeable as spot moves through this level."

## Concrete example

A dealer is short 200 contracts of a 25 day ATM call on [[Brent Crude]] futures. Spot Brent: $82.00. Strike: $82.00. Implied vol: 28%. Initial gamma per contract: 0.038 per dollar. Total short gamma: -7.6 lots per dollar move.

Reading: a $1 Brent move requires hedging 8 lots to stay delta neutral. Workable.

Now imagine spot Brent rallies to $84 (above the strike). Speed has been negative throughout the move (gamma decaying as spot moves above strike). Gamma per contract dropped from 0.038 to 0.028. Total short gamma: -5.6.

Conversely, if spot dropped to $80, speed was positive in that direction (spot moving toward higher gamma region as the option becomes more sensitive). Gamma per contract grew to 0.041. Total short gamma: -8.2.

Asymmetric. The $2 move from $82 to $80 increased gamma by 8%. The $2 move from $82 to $84 decreased gamma by 26%.

Hedging cost implication: if spot is oscillating around $82, the gamma hedging requirement changes nonlinearly with each move. The dealer cannot just hedge as if gamma is constant. They must adjust hedge ratios continuously based on current spot location relative to strike. Failing to do so leaves them under or over hedged in a way that produces P&L noise from a "delta neutral" book.

For barrier options the effect is far larger. A knock out call with barrier at $90 has speed that produces a near vertical gamma profile just below the barrier, with gamma collapsing to zero above. A trader hedging near the barrier faces hedging requirements that swing by factors of 5 to 10 within a $0.50 range of the barrier.

## Key mechanics and formulas

**Speed for a vanilla option (Black Scholes):**

`Speed = -Gamma / S × (d1 / (σ × sqrt(T)) + 1)`

Or equivalently:
`Speed = - e^(-qT) × N'(d1) × (d1 + σ × sqrt(T)) / (S² × σ² × T)`

The structure to remember: speed scales as 1/S² and grows as 1/T as expiry approaches.

**Useful intuition:**
- Speed is zero at the gamma peak (slightly above strike for calls, slightly below for puts due to vol drift)
- Speed is large positive when spot is below the gamma peak (gamma growing as spot rises)
- Speed is large negative when spot is above the gamma peak (gamma falling as spot rises further)
- Speed magnitude grows as T → 0, similar to gamma itself

**Approximation for ATM near expiry:**

`Speed_ATM ≈ - Gamma_ATM / (S × σ × sqrt(T))`

For a near expiry ATM option with sqrt(T) very small, speed can become very large per unit spot move.

**Practical use:**

Speed is most useful for predicting hedge ratio adjustments:
`ΔHedge ≈ Gamma × ΔS + 0.5 × Speed × (ΔS)²`

The second term shows how the hedge requirement grows nonlinearly with the size of the spot move. For small moves (< 0.5% of spot), the first term dominates. For large moves the speed term becomes material.

**Barrier dynamics:**

Near a barrier, speed effectively goes to infinity at the barrier level for a knock out option, reflecting the discontinuity of the payoff. Numerical implementations cap this for stability, but the underlying risk is real: small spot moves near the barrier produce huge gamma changes.

## Prerequisites
- [[Gamma]]
- [[Delta]]
- [[Greeks]]
- [[Option]]
- [[Black Scholes Model]]

## Related concepts (learn next)
- [[Gamma]] - speed is the spot derivative of gamma, so understanding gamma is the prerequisite.
- [[Color]] - color is the time derivative of gamma. Speed and color together describe gamma's evolution under spot and time.
- [[Zomma]] - zomma is the vol derivative of gamma (dGamma/dVol). The full third order gamma family.
- [[Barrier Option]] - barriers create extreme speed near the trigger level, dominating hedge management.
- [[0DTE]] - 0DTE options have large speed near key strikes, contributing to gamma cascade behavior.
- [[Expiry Pinning]] - pinning at round number strikes is driven by speed changing sign across the strike.
- [[Butterfly]] - butterflies are pure gamma trades; speed is what makes their P&L path dependent on how spot moves through the strikes.

## Common misconceptions

**"Gamma is constant near the strike."** Not even close. Gamma changes with spot (via speed), with time (via color), and with vol (via zomma). Speed is the channel that matters most for intraday spot movement.

**"Speed only matters for exotics."** Wrong. Vanilla options have material speed near expiry. Dealer hedging books actively track speed for all near expiry ATM positions.

**"Symmetric gamma profile means symmetric speed."** Speed is the rate of change of gamma. Even when the gamma profile is approximately symmetric around the strike (as for ATM options), speed is largest in magnitude where the gamma slope is steepest, not where gamma itself is largest. Speed peaks on either side of the gamma peak, not at it.

**"Speed is too high order to be tradeable."** Speed is not directly tradeable as a standalone exposure, but its effects are visible in P&L of any gamma trading book. Practitioners include it in greek reports and risk limits.

**"Hedging gamma neutralizes speed."** False. Even a gamma hedged book has residual speed exposure because the hedge instruments themselves have different speed profiles than the underlying position. Most desks accept speed as residual risk rather than attempting to hedge it.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form speed and other third order greeks.
- Taleb, Nassim Nicholas. *Dynamic Hedging*. Treatment of higher order greeks and gamma scalping.
- Wystup, Uwe. *FX Options and Structured Products*. Discussion of speed in barrier option hedging.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Bossens et al. "Vanna Volga Methods Applied to FX Derivatives." Discussion of gamma profile dynamics.
