---
aliases: [charm, delta bleed, delta decay, DdeltaDtime, dDelta/dTime]
tags:
  - "#quant"
  - "#microstructure"
date-added: "2026-05-23"
---

# Charm

## Definition

Charm is the rate at which [[Delta]] changes as time passes, holding everything else constant. Even with spot unchanged, delta drifts as the clock ticks. Charm = d(Delta) / d(t) = -d²(Option price) / d(S × t). Also called "delta bleed."

An OTM call with delta 0.30 today may have delta 0.15 tomorrow at unchanged spot, because the option became less likely to finish ITM. The 15 point drift is charm.

Charm is largest for slightly OTM options with moderate tenor, and explodes for near ATM options into expiry. It dominates [[0DTE]] and the final week of any short dated option.

By [[Put Call Parity]], charm of a call equals charm of a put at the same strike and expiry.

## Why it matters (commodities and FX)

Charm moves a delta hedged book overnight without any market activity:

- **Overnight delta drift.** A market maker who closes flat at 4:00 PM Friday returns Monday with non zero delta even if the underlying gapped to zero. Charm bled the delta over 65 hours. For an FX desk running thousands of options, this drift is the largest single source of weekend P&L variance.
- **0DTE dominance.** With [[0DTE]] options at half of SPX option volume, charm is the dominant greek for intraday delta drift. A dealer short 0DTE puts at 10:00 AM with spot at strike sees delta drift by tens of percent over the day from charm alone.
- **Pinning dynamics.** Charm and [[Gamma]] together produce [[Expiry Pinning]]. ITM expiring options have charm pulling delta toward 1; OTM options toward 0. The resulting hedge flow pins spot at strike.
- **Commodity calendar options.** Long dated [[Brent Crude]] options on monthly cycles have predictable charm patterns. Roll strategies anticipate delta drift around contract roll dates.

For weekend and holiday FX option books, charm answers "where did my delta go?" Time passed, charm did its work.

## Concrete example

**Concrete:** Dealer short 1,000 [[USDJPY]] 152.00 calls, 5 days to expiry. Spot 151.50, vol 9%, delta 0.42 per option. Short delta: 42,000 USD. Hedges by buying 42,000 USD spot. Two calendar days pass. Spot opens Monday at 151.50. Charm of -0.04 per day drifted delta from 0.42 to 0.34. Short option delta now 34,000 USD, spot hedge still 42,000 USD long. Net 8,000 USD long that the dealer never put on. A 30 pip Monday drop costs ~$6,000 of ghost losses. Scale to a 50,000 contract FX book and weekend charm drift costs tens of thousands without any actual market move.

**Simplified:** Delta is not frozen between Friday close and Monday open. Time alone drifts it. Even with spot unchanged, the option's delta shrinks (or grows) as days pass. If you hedged Friday and did not adjust, your "neutral" book is no longer neutral Monday morning. Charm is the size of that drift per day. Short dated options drift faster than long dated. Weekends are dangerous because three calendar days pass while you cannot adjust.

## Key mechanics and formulas

**Charm for a call (Black Scholes):**

`Charm_call = -N'(d1) × [(r - q) / (σ × sqrt(T)) - d2 / (2T)]`

Sign flips on the second term for puts. N'() = standard normal PDF, d1 and d2 standard BS quantities.

**Useful intuition:**
- Charm is near zero for deep ITM and deep OTM options
- Charm peaks for slightly OTM options
- Charm magnitude grows as T → 0 for near ATM options
- For ATM call: charm ≈ -1 / (2T) per unit time. T = 1/365 (1 day) makes charm enormous

**Trader units:** "delta change per calendar day." Charm of -0.04 = delta drops 4 points per day.

**Pricing identity:**

`Charm = d(Delta) / d(t) = -d(Theta) / d(S)`

Charm is symmetric: the rate delta drifts in time equals the negative rate theta changes with spot.

**Intraday vs calendar day:** charm scales with time to expiry. For 0DTE options, intraday charm per hour ≈ 1/(24 × T_days). A 0DTE option at 10:00 AM with 6 hours left has charm of 5 to 8 delta points per hour for ATM strikes.

**Aggregation:** Charm is additive across a portfolio. Total book charm = sum of individual option charms × position size. Prime broker greek reports include charm at position and book level.

## Prerequisites
- [[Delta]]
- [[Theta]]
- [[Option]]
- [[Greeks]]
- [[Black Scholes Model]]

## Related concepts (learn next)
- [[Delta]] - charm is the time derivative of delta.
- [[Theta]] - linked by symmetry. Charm = -dTheta/dSpot.
- [[0DTE]] - charm dominates 0DTE delta management.
- [[Expiry Pinning]] - charm plus gamma drive pinning at high open interest strikes.
- [[Gamma]] - together they describe delta evolution under spot and time.
- [[Veta]] - vega analog: dVega/dTime.
- [[Color]] - gamma analog: dGamma/dTime.

## Common misconceptions

**"Delta only changes when spot moves."** Wrong. Delta changes with spot (gamma), vol (vanna), and time (charm). All three drive intraday delta drift.

**"Charm matters only at expiry."** False. Charm is present every day. Small but cumulative for long dated options, dominant for [[0DTE]], material in the final two weeks of monthlies.

**"Weekend charm is small because the market is closed."** Calendar days drive charm, not trading days. Friday close to Monday open is 3 days of charm, not 1.

**"You can ignore charm with a tight gamma hedge."** Gamma protects against spot moves, not time. A perfectly gamma hedged book is still exposed to charm.

## Sources

- Taleb, Nassim Nicholas. *Dynamic Hedging*. Chapter on second order and time greeks.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Wystup, Uwe. *FX Options and Structured Products*. Detailed treatment of charm in FX dealer books.
- Sinclair, Euan. *Positional Option Trading*. Practical chapter on near expiry option dynamics including charm.
- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form charm expressions.
