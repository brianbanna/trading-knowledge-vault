---
aliases: [rho, ρ, interest rate sensitivity, rate delta, dPrice/dRate]
tags:
  - "#quant"
  - "#rates"
date-added: "2026-05-23"
---

# Rho

## Definition

Rho is an option's price sensitivity to a change in the risk free interest rate. If rates move 1%, how much does the option price change. Rho = d(Option price) / d(r). For a vanilla call, rho is positive (calls gain as rates rise because the embedded forward rises). For a vanilla put, rho is negative.

Rho is the smallest and most ignored first order greek for short dated options. Rate moves are slow relative to spot or vol, and the magnitude is small for any option under a few months. For long dated options (LEAPS, multi year FX or commodity options), rho becomes material.

FX options have two rhos because two currencies are involved: domestic rho (sensitivity to domestic rate) and foreign rho (sensitivity to foreign rate, sometimes called phi). Equal magnitude, opposite sign for ATM options at the forward.

## Why it matters (commodities and FX)

For most short dated trading, rho is a rounding error. Where it still matters:

- **Long dated FX options.** A 2 year [[EURUSD]] option has meaningful rho. When the [[Fed]] moves 25 bps unexpectedly, the rate differential shifts, the forward shifts, and long dated options reprice through rho before any vol or spot effect. FX dealers running multi year vol books hedge rho with [[Interest Rate Swap|interest rate swaps]] or government bonds.
- **Commodity calendar options.** Long dated [[Brent Crude]] or [[Gold Futures]] options (1+ year) carry rho via [[Cost of Carry]] baked into the forward curve. Gold is especially sensitive because its no income carry means rates dominate forward pricing.
- **Convertible bonds and structured products.** Embedded options with multi year tenors carry rho that bond desks hedge alongside duration. Trading convertibles or callable structures = real rho exposure.
- **Quanto and composite options.** Cross currency options have rho dependencies in both the underlying and payoff currencies.

For day to day commodity vol trading on front month options, rho is safely ignored against delta, gamma, vega, and theta.

## Concrete example

**Concrete:** Dealer long a 2 year ATM call on [[EURUSD]], EUR 100M notional, strike at forward 1.0950. Spot 1.0900, ATM vol 8%, USD rate 5.0%, EUR rate 3.5%. Domestic rho: ~+18,000 USD per 1 bp move in USD rates, or +1.8M per 100 bps. Fed surprises with a 50 bp cut. USD rate 5.0% to 4.5%. Pure rho P&L: -900,000 USD. But the cut also widens EURUSD rate differential, pushing the forward to ~1.1010. The ATM call is now ~60 pips ITM via the forward shift. Vega and gamma kick in if vol moves. Net: a single rate event creates a multi greek P&L event in long dated FX options. The same option at 3 months would have rho P&L of ~30,000 USD, a rounding error.

**Simplified:** Rates show up in option prices through the forward. If rates change, the forward changes, and any option that lives long enough for that to matter sees its price move. Short dated options have small forward sensitivity, so rho is invisible. Long dated options have large forward sensitivity, so a Fed move can shift them by 1% or more before any spot or vol effect. FX options have two rates that matter (domestic and foreign), so a single rate decision can move the option via either channel.

## Key mechanics and formulas

**Black Scholes rho for a call:**

`Rho_call = K × T × e^(-rT) × N(d2)`

**Black Scholes rho for a put:**

`Rho_put = -K × T × e^(-rT) × N(-d2)`

K = strike, T = time to expiry in years, r = risk free rate, N() = standard normal CDF, d2 = (ln(S/K) + (r - σ²/2) × T) / (σ × sqrt(T)).

**Scaling with time:** Rho grows roughly linearly with T. A 2 year option has ~8 times the rho of a 3 month option (same strike, spot, vol).

**FX options:** Two rhos:
- Domestic rho = ∂Price / ∂r_domestic
- Foreign rho (phi) = ∂Price / ∂r_foreign

For a call on EURUSD (USD payoff, EUR notional): domestic rho > 0, foreign rho < 0.

**Practical magnitude:**

For a 1Y ATM call on a $100 underlying at 20% vol, 5% rate:
- Rho ≈ $0.40 per 1% rate change (4 cents per bp)

Same option at 3 months: rho ≈ $0.10. At 1 month: rho ≈ $0.03.

**Bucketing for risk reporting:** Multi year option books report rho bucketed by tenor (1Y, 2Y, 5Y, 10Y) to hedge specific points on the yield curve, not just parallel shifts.

## Prerequisites
- [[Option]]
- [[Black Scholes Model]]
- [[Greeks]]
- [[Forward Curve]]
- [[Cost of Carry]]

## Related concepts (learn next)
- [[Greeks]] - rho fits in the broader hierarchy and is the smallest first order greek for typical books.
- [[Cost of Carry]] - rates enter pricing primarily through the forward, which is set by [[Cost of Carry]]. Rho is sensitivity to one carry component.
- [[Forward Curve]] - the forward curve embeds rates. Long dated option rho is largely a forward curve sensitivity in disguise.
- [[Duration]] - rho is to options what duration is to bonds, with similar tenor scaling.
- [[Interest Rate Parity]] - links FX forwards and rate differentials, driving FX option rho.
- [[Delta]] - rho is often overshadowed by delta; for long dated options both need joint hedging.
- [[Theta]] - rho and theta both scale with time but in opposite roles: theta is the cost of holding, rho is the financing sensitivity.

## Common misconceptions

**"Rho is irrelevant."** True for short dated. False for any book with multi year exposure, FX vol portfolios, or structured products. Convertible bond desks treat rho as a primary risk.

**"There is one rho for an FX option."** Two: domestic and foreign. A book rho neutral domestically may carry large foreign rho exposure. Both need separate hedging.

**"Rho hedging is done with rates futures."** Possible but often inefficient. Long dated rho is usually hedged with [[Interest Rate Swap|IRS]] at matching tenors because the tenor profile fits swap curves better than Eurodollar futures.

**"Higher rates always help calls."** True via positive rho, but if higher rates trigger a spot selloff, delta loss often dwarfs rho gain. Greek decomposition matters on rate event days.

## Sources

- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed. Chapter on greek letters.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed. Chapters on FX greeks and dual currency rho.
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed. Discussion of rho and long dated option pricing.
- Castagna, Antonio. *FX Options and Smile Risk*. Treatment of domestic and foreign rho in FX option books.
