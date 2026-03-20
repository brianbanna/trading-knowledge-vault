---
aliases: [straddle, ATM straddle, long straddle]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Straddle

## Definition
A straddle is an options strategy that combines a long [[ATM]] [[call option]] and a long [[ATM]] [[put option]] with the same [[strike price]] and [[expiry]]. The position profits from large moves in either direction and loses if the [[underlying]] stays near the strike. Because both legs are ATM, the straddle has zero net [[Delta]] at inception (delta neutral) and maximum [[Gamma]], [[Vega]], and [[Theta]] exposure. It is the purest expression of a [[Volatility]] view: the trader is betting that [[Realized Volatility]] will exceed the [[implied volatility]] priced into the [[premium]]. In FX, the ATM straddle premium is the standard benchmark quote for option cost at each [[tenor]].

## Why it matters (commodities and FX)
The ATM straddle is the foundational volatility trade in every options market. FX desks quote straddle premiums as the primary measure of option cost: "1 month EUR/USD straddle at 7.8 vol" is shorthand understood globally. Commodity traders buy straddles ahead of [[EIA Report]] releases, [[OPEC]] meetings, or crop reports when they expect a large move but are uncertain of direction. Straddle prices embed the market's forward looking expectation of [[Realized Volatility]], so comparing straddle implied vol to subsequent realized vol is the core framework for systematic vol selling or buying strategies. The straddle also defines the body of the [[Butterfly]] spread.

## Concrete example
**Success:** USD/JPY 1 week ATM straddle is quoted at 10.5% implied vol (premium of 85 pips) ahead of a BOJ meeting. The trader buys the straddle at strike 150.50. The BOJ unexpectedly raises rates by 25 bp, and USD/JPY drops to 147.00 in 2 days. The put leg has 350 pips of intrinsic value. After subtracting the 85 pip premium, the net profit is 265 pips. Realized vol over the week annualizes at 22%, far exceeding the 10.5% implied.

**Failure:** A trader buys the 1 month EUR/USD straddle at 8.2% implied vol for 115 pips. The next month is quiet: spot drifts from 1.0800 to 1.0830. Realized vol comes in at 5.8%. At expiry, the call is worth 30 pips intrinsic, meaning a net loss of 85 pips. The [[Theta]] decay consumed the entire time value, and [[Gamma]] gains from small daily moves (which the trader delta hedged) could not compensate.

## Key mechanics and formulas
- **Straddle payoff at expiry** = |spot at expiry minus strike| minus premium paid
- **Breakeven (upper)** = strike + total premium
- **Breakeven (lower)** = strike minus total premium
- **Straddle premium approximation** = spot × vol × sqrt(time to expiry) × sqrt(2 / pi), approximately 0.8 × spot × vol × sqrt(time)
- **Greeks at inception**: Delta is approximately 0, Gamma is at maximum, Vega is at maximum, Theta is at maximum negative
- **Daily theta** is approximately (straddle premium) / (days to expiry), slightly front loaded
- **Break even realized vol** = implied vol at purchase (in a delta hedged framework)

## Prerequisites
- [[ATM]]
- [[Vanilla Option]]
- [[Implied Volatility]]
- [[Realized Volatility]]
- [[Delta]]

## Related concepts (learn next)
- [[Strangle]]: OTM version of the straddle, cheaper but needs a bigger move to profit
- [[Butterfly]]: long strangle minus short straddle, isolating curvature of the smile
- [[Gamma]]: straddle is the maximum gamma position, profiting from spot acceleration
- [[Theta]]: the daily cost of holding a straddle, the "rent" paid for gamma exposure
- [[Vega]]: straddle P&L is highly sensitive to changes in implied vol even before expiry
- [[Risk Reversal]]: a directional skew trade, contrasting with the non directional straddle
- [[Realized Volatility]]: the benchmark against which straddle profitability is measured

## Common misconceptions
1. **"A straddle profits if the market moves."** The market must move more than the premium paid. A straddle can lose money even with a significant spot move if that move was already priced into the vol.
2. **"Straddles are always delta neutral."** They are delta neutral only at inception. As soon as spot moves, the straddle acquires directional delta from [[Gamma]], requiring rehedging if a pure vol trade is intended.
3. **"Selling straddles is free money in quiet markets."** While short straddles collect premium, a single large move (gap, intervention, flash crash) can produce losses many multiples of the premium collected. The risk reward is asymmetric and favors the buyer in tail scenarios.

## Sources
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
