---
aliases: [charm, delta bleed, delta decay, DdeltaDtime, dDelta/dTime]
tags:
  - "#quant"
  - "#microstructure"
date-added: "2026-05-23"
---

# Charm

## Definition

Charm is the second order greek that measures the rate at which [[Delta]] changes as time passes, holding all other variables constant. Plain English: even if spot does not move, your delta drifts as the clock ticks. Charm tells you how fast. Mathematically, charm = d(Delta) / d(t) = -d²(Option price) / d(S × t). It is sometimes called "delta bleed."

Charm matters because delta is not static. An OTM call with delta 0.30 today may have delta 0.15 tomorrow even if spot is unchanged, because as time passes the option becomes less likely to finish ITM. The delta drifted by 15 points purely from time, not from spot moves. That drift is charm in action.

Charm is largest for options that are slightly OTM with moderate time to expiry, and explodes in magnitude as expiry approaches for near ATM options. It is one of the dominant greeks for [[0DTE]] options and for the final week of any short dated option.

By [[Put Call Parity]], charm of a call equals charm of a put with the same strike and expiry (when measured as delta drift).

## Why it matters (commodities and FX)

Charm is the unseen force that moves a delta hedged book overnight even with no market activity:

- **Overnight delta drift.** A market maker who closes their book delta neutral at 4:00 PM Friday returns Monday with non zero delta even if the underlying gapped zero. Why? Charm bled the delta over 65 hours of elapsed time. For an FX desk running thousands of options, this delta drift can be the largest single source of weekend P&L variance.
- **0DTE dominance.** With [[0DTE]] options now half of SPX option volume, charm is the single most important greek for understanding intraday delta drift. A dealer short 0DTE puts at 10:00 AM with spot at the strike will see their delta drift by tens of percent over the day from charm alone, requiring continuous rehedging.
- **Pinning and expiry dynamics.** Charm interacts with [[Gamma]] near expiry to produce [[Expiry Pinning]]. Options expiring in the money have charm pulling their delta toward 1; OTM expiring options have charm pulling delta toward 0. The hedging that results is what pins spot at strike.
- **Commodity calendar options.** Long dated [[Brent Crude]] options on monthly cycles have predictable charm patterns. Funds running roll strategies need to anticipate the delta drift around contract roll dates.

In commodity FX options on weekends and holidays, charm is the explanation for "where did my delta go?" The answer is always: time passed, and charm did its work.

## Concrete example

A dealer is short 1,000 [[USDJPY]] 152.00 calls expiring in 5 days. Spot USDJPY: 151.50. Implied vol: 9%. Initial delta of each option: 0.42. Total short delta: 42,000 USD worth of USDJPY exposure short. Dealer hedges by buying 42,000 USD of USDJPY spot.

Saturday and Sunday: no market activity. Spot opens Monday at 151.50, unchanged.

But: 2 calendar days passed. Charm on each option was approximately -0.04 per day (delta drifts from 0.42 toward whatever it will be at expiry). After 2 days, delta on each option dropped from 0.42 to roughly 0.34.

Dealer's short option delta is now 34,000 USD short. Spot hedge is still 42,000 USD long. Net position: 8,000 USD long USDJPY that the dealer did not put on. If USDJPY drops 0.5% on Monday open (newshock), the dealer loses 40 USD per pip on 8,000 USD notional = ~$200 per pip × ~30 pips = $6,000 of "ghost" losses from a position they never intended.

Multiply by a typical FX book with 50,000 contracts: weekend charm drift can cost tens of thousands without any actual market move. This is why disciplined dealers run charm reports Friday evening and pre adjust hedges.

What if the option were 0DTE expiring today? Charm in the last hour is enormous. The same 0.42 delta call could drift to 0.05 by 3:50 PM if it stays OTM, or to 0.95 if it goes slightly ITM. The intraday charm scale is 10 to 100 times the calendar day scale, and is the primary reason 0DTE dealer hedging looks erratic to outsiders.

## Key mechanics and formulas

**Charm for a call (Black Scholes):**

`Charm_call = -N'(d1) × [(r - q) / (σ × sqrt(T)) - d2 / (2T)]`

For a put, sign flips on the second term. N'() = standard normal PDF, d1 and d2 standard BS quantities.

**Useful intuition:**
- Charm is approximately zero for deep ITM and deep OTM options
- Charm peaks for slightly OTM options
- Charm magnitude grows as T → 0 for near ATM options
- For ATM call: charm ≈ -1 / (2T) per unit time. With T = 1/365 (1 day), charm is enormous

**Charm in units traders use:** typically expressed as "delta change per calendar day." A charm of -0.04 means delta drops by 4 points per day.

**Pricing identity:**

`Charm = d(Delta) / d(t) = -d(Theta) / d(S)`

This means charm is symmetric: the rate at which delta drifts in time equals the negative rate at which theta changes with spot.

**Intraday vs calendar day:** charm scales with time to expiry. For 0DTE options, intraday charm per hour is roughly 1/(24 × T_days). For a 0DTE option at 10:00 AM with 6 hours to expiry, T = 0.25/365, so charm per hour is roughly 5 to 8 delta points for ATM strikes.

**Aggregation:** Charm is additive across a portfolio. Total book charm = sum of individual option charms × position size. Most prime broker greek reports include charm at the position and book level.

## Prerequisites
- [[Delta]]
- [[Theta]]
- [[Option]]
- [[Greeks]]
- [[Black Scholes Model]]

## Related concepts (learn next)
- [[Delta]] - charm is the time derivative of delta, so understanding delta dynamics is the prerequisite for understanding charm.
- [[Theta]] - charm and theta are linked by symmetry. Charm = -dTheta/dSpot.
- [[0DTE]] - charm is the dominant greek for managing 0DTE positions, where delta drifts by huge amounts hour to hour.
- [[Expiry Pinning]] - charm together with gamma produces pinning behavior at high open interest strikes.
- [[Gamma]] - charm and gamma together describe how delta evolves under spot moves and time, the two key forcing variables.
- [[Veta]] - the analog for vega: dVega/dTime. Charm is for delta, veta is for vega.
- [[Color]] - the analog for gamma: dGamma/dTime. Charm is for delta, color is for gamma.

## Common misconceptions

**"Delta only changes when spot moves."** Wrong. Delta changes with spot (gamma), with vol (vanna), AND with time (charm). All three drive intraday delta drift in a delta hedged portfolio.

**"Charm matters only at expiry."** False. Charm is present every day. For long dated options it is small but cumulative. For [[0DTE]] options it is the dominant greek of the day. Even monthly options have meaningful charm in the final two weeks.

**"Weekend charm is small because the market is closed."** Calendar days elapsed are what matter for charm, not trading days. Friday close to Monday open is 3 days of charm, not 1. Weekends and holidays are when delta hedged books drift the most.

**"Charm is the same for puts and calls."** As a delta drift, yes (charm of call delta = charm of put delta with sign convention). But the directional implication is opposite: a call's delta drifts toward 0 or 1 depending on moneyness; a put's drifts toward 0 or -1.

**"You can ignore charm if you have a tight gamma hedge."** Gamma protects against spot moves, not against time. A perfectly gamma hedged book is still exposed to charm. Both need separate management.

## Sources

- Taleb, Nassim Nicholas. *Dynamic Hedging*. Chapter on second order and time greeks.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Wystup, Uwe. *FX Options and Structured Products*. Detailed treatment of charm in FX dealer books.
- Sinclair, Euan. *Positional Option Trading*. Practical chapter on near expiry option dynamics including charm.
- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form charm expressions.
