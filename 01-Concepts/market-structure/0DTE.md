---
aliases: [0DTE, zero days to expiration, zero DTE, same day expiry options, daily expirations, 0 DTE options]
tags:
  - "#microstructure"
  - "#equities/indices"
  - "#risk"
date-added: "2026-05-23"
---

# 0DTE

## Definition

0DTE means "zero days to expiration." An option that expires the same trading day it is traded. Most common on SPX, SPY, QQQ, and XSP. Daily expiries now extend to mega cap single stocks (TSLA, NVDA), to VIX (Wednesday cycle), and to commodity ETFs (GLD, USO).

The behavior is dominated by [[Gamma]] (huge near the strike), [[Theta]] (collapsing every minute), and [[Charm]] (delta drift in hours, not days). The CBOE added Tuesday and Thursday SPX expiries in 2022, giving every business day a same day contract. By 2024, 0DTE was roughly 50% of SPX option volume on many days. Largest market structure change in US equity options in 20 years.

## Why it matters (commodities and FX)

0DTE is an SPX story, but it bleeds into commodities and FX through dealer hedging flows:

- **Intraday SPX moves are now dealer driven.** Dealers short 0DTE puts (retail buying downside) sell ES futures into weakness to stay delta hedged, which accelerates the selloff. Same dynamic in reverse for short calls. These flows propagate to [[USDJPY]], [[Copper Futures]], and [[Gold Futures]] via cross asset arbitrage desks.

- **VIX understates intraday vol.** 0DTE options are not in the [[VIX]] calculation (VIX uses 23 to 37 day SPX options). Large 0DTE driven moves happen without VIX moving. If VIX is your only [[Risk-On Risk-Off]] gauge, you miss the move.

- **End of day flow is predictable.** Large 0DTE open interest at round number strikes (5,400 SPX, 600 SPY) pulls spot toward the strike via dealer rebalancing in the last 30 minutes. The flow propagates to USDJPY, treasuries, gold.

- **Volmageddon style risk has migrated.** 0DTE absorbed most systematic short vol flow that used to live in 1 week to 1 month options. A future blowup will look different from February 2018.

Practical rule: SPX moves >0.6% in under 30 minutes with VIX moving <1 point = likely 0DTE gamma. Do not stop out cross asset positions on the first leg. Reassess at the close.

## Concrete example

**Concrete:** Wednesday 2:15 PM ET. SPX drops from 5,400 to 5,360 in 18 minutes, no news. VIX moves only from 13.5 to 14.2. Copper drops from $4.65 to $4.605, just above the trader's stop at $4.60. Trader reads the pattern (big intraday SPX move, VIX asleep, no news) as 0DTE gamma and holds. By 3:30 PM SPX recovers to 5,395 as dealer gamma unwinds. Copper closes at $4.64. Recognizing the 0DTE signature saved a bad stop out.

**Simplified:** A big buyer grabs same day SPX puts in the morning. The dealer who sold them is now short. As spot drifts toward the strike, gamma explodes (because expiry is hours away), so the dealer has to sell more and more futures to stay flat. The selling pushes SPX down further, which makes gamma bigger, which forces more selling. A loop. After expiry the position is gone and the forced selling stops. SPX often snaps back. Cross asset stuff (copper, FX) gets dragged along even though nothing real happened.

## Key mechanics and formulas

**Theta:** ATM theta scales as `-S × σ / (2 × sqrt(2π × T))`. T → 0 means theta → -∞. A $15 option at 10:00 AM is worth $0.10 at 3:55 PM if spot is unchanged.

**Gamma:** ATM gamma scales as `1 / (S × σ × sqrt(2π × T))`. With T = 1 hour ≈ 0.0001 years, gamma is orders of magnitude above a 30 day option. A 0.1% spot move can swing delta by 30 to 50 points.

**Dealer Gamma Exposure (GEX):** `GEX ≈ Σ (γ_i × OI_i × 100 × spot)`. Estimated from open interest weighted strike distribution. Large negative GEX = dealers short gamma = small moves amplify. Large positive GEX = stable, small moves dampened.

**Pin risk:** High open interest at round number strikes pulls spot toward those strikes into the close. Same mechanism as monthly [[Expiry Pinning]], now daily.

**Charm:** Delta drift per unit time. For 0DTE ATM options, charm can move delta by 30+ points over a session, requiring continuous rehedging even when spot does not move.

**Volume distribution:** Concentrated 9:30 to 10:00 AM (overnight rebalance), 1:00 to 2:00 PM (lunch flow), 3:00 to 4:00 PM (closing gamma resolution).

## Prerequisites
- [[Option]]
- [[Theta]]
- [[Gamma]]
- [[Delta]]
- [[Implied Volatility]]
- [[Expiry Pinning]]

## Related concepts (learn next)
- [[Expiry Pinning]] - now a daily event at round number strikes, not monthly.
- [[Gamma]] - the dominant greek for 0DTE.
- [[VIX]] - 0DTE flow does not feed VIX, creating systematic divergence between VIX and intraday realized vol.
- [[VVIX]] - increasingly poor at predicting 0DTE driven moves, since 0DTE is order flow not stochastic vol.
- [[Charm]] - delta drift dominates 0DTE intraday hedging.
- [[Volmageddon]] - the 2018 short vol blowup template. A 0DTE analog has not happened yet at scale.
- [[Volatility]] - 0DTE changed the relationship between IV at different tenors and intraday realized vol.

## Common misconceptions

**"0DTE is retail lottery tickets."** Retail uses them that way. Institutional flow is dominated by hedge replacement, overwriting, and dealer hedging. Daily notional traded exceeds the GDP of medium sized countries.

**"0DTE is a US equity story only."** Daily expiries now exist on single stocks, ETFs, and overseas indices (KOSPI 200, Nikkei weekly). The market structure effects will follow.

**"0DTE will cause the next crash."** Possible, unproven. August 5 2024 yen carry unwind tested the system (VIX spiked to 65 intraday) and it held.

**"0DTE volume is mostly speculation."** A large share is institutional hedge replacement: roll 0DTE puts daily instead of holding 30 day puts. More capital efficient, different gamma dynamics for the dealer ecosystem.

**"You cannot use 0DTE for cross asset signals."** You can. SpotGamma and SqueezeMetrics sell exactly that: SPX 0DTE OI concentration and dealer GEX estimates as inputs for FX and commodity intraday timing.

## Sources

- CBOE: SPX Weeklys and Daily Expiry documentation.
- Brogaard, Han, Won. "Does the Tail Wag the Dog? The Effect of 0DTE Options on Underlying Returns." Working paper, 2024.
- JPMorgan Marko Kolanovic notes on 0DTE flow and dealer positioning, 2022 to 2024.
- SpotGamma and SqueezeMetrics: practitioner research on gamma exposure modeling.
- Sinclair, Euan. *Positional Option Trading*. Wiley, 2020.
- BIS Quarterly Review, March 2024: "The market microstructure impact of 0DTE options."
