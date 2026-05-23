---
aliases: [straddle, ATM straddle, long straddle]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Straddle

## Definition
A straddle combines a long [[ATM]] [[call option]] and a long [[ATM]] [[put option]] at the same [[strike price]] and [[expiry]]. The position profits from large moves in either direction and loses if the [[underlying]] stays near the strike. Both legs ATM: the straddle has zero net [[Delta]] at inception (delta neutral) and maximum [[Gamma]], [[Vega]], and [[Theta]]. The purest expression of a [[Volatility]] view: the trader bets [[Realized Volatility]] will exceed the [[implied volatility]] in the [[premium]]. In FX, the ATM straddle premium is the standard benchmark quote for option cost at each [[tenor]].

## Why it matters (commodities and FX)
The ATM straddle is the foundational volatility trade in every options market. FX desks quote straddle premiums as the primary measure of option cost: "1 month EUR/USD straddle at 7.8 vol" is shorthand understood globally. Commodity traders buy straddles ahead of [[EIA Report]] releases, [[OPEC]] meetings, or crop reports when expecting a large move with uncertain direction. Straddle prices embed the market's forward looking expectation of [[Realized Volatility]]: comparing straddle implied vol to subsequent realized vol is the core framework for systematic vol selling or buying. The straddle also defines the body of the [[Butterfly]] spread.

## Concrete example
**Concrete:** USD/JPY 1 week ATM straddle quoted at 10.5% implied vol (85 pips premium) ahead of a BOJ meeting. Trader buys at strike 150.50. BOJ unexpectedly raises rates 25 bp, USD/JPY drops to 147.00 in 2 days. Put leg has 350 pips intrinsic. Net profit 265 pips. Realized vol over the week annualizes at 22%, far above the 10.5% implied.

**Simplified:** Buy a call and a put at the same strike. You profit if the underlying moves enough in either direction to cover both premiums. You lose if it sits still. A pure volatility bet: you win when the market moves more than was priced in, lose when it moves less.

## Key mechanics and formulas
- **Straddle payoff at expiry** = |spot at expiry minus strike| minus premium paid
- **Breakeven (upper)** = strike + total premium
- **Breakeven (lower)** = strike minus total premium
- **Straddle premium approximation** = spot × vol × sqrt(time to expiry) × sqrt(2 / pi), ~0.8 × spot × vol × sqrt(time)
- **Greeks at inception**: Delta ~0, Gamma at maximum, Vega at maximum, Theta at maximum negative
- **Daily theta** ~ straddle premium / days to expiry, slightly front loaded
- **Break even realized vol** = implied vol at purchase (in a delta hedged framework)

## Prerequisites
- [[ATM]]
- [[Vanilla Option]]
- [[Implied Volatility]]
- [[Realized Volatility]]
- [[Delta]]

## Related concepts (learn next)
- [[Strangle]]: OTM version, cheaper but needs a bigger move to profit
- [[Butterfly]]: long strangle minus short straddle, isolating curvature of the smile
- [[Gamma]]: straddle is the maximum gamma position, profiting from spot acceleration
- [[Theta]]: the daily cost of holding a straddle, the rent paid for gamma exposure
- [[Vega]]: straddle P&L is highly sensitive to changes in implied vol even before expiry
- [[Risk Reversal]]: a directional skew trade, contrasting with the non directional straddle
- [[Realized Volatility]]: the benchmark against which straddle profitability is measured

## Common misconceptions
1. **"A straddle profits if the market moves."** The market must move more than the premium paid. A straddle loses money even with a significant spot move if that move was already priced into the vol.
2. **"Straddles are always delta neutral."** Delta neutral only at inception. Once spot moves, the straddle acquires directional delta from [[Gamma]], requiring rehedging if a pure vol trade is intended.
3. **"Selling straddles is free money in quiet markets."** Short straddles collect premium, but a single large move (gap, intervention, flash crash) produces losses many multiples of the premium collected. Risk reward is asymmetric and favors the buyer in tail scenarios.

## Sources
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
