---
aliases: [rho, ρ, interest rate sensitivity, rate delta, dPrice/dRate]
tags:
  - "#quant"
  - "#rates"
date-added: "2026-05-23"
---

# Rho

## Definition

Rho measures an option's price sensitivity to a change in the risk free interest rate. Plain English: if rates move 1%, how much does the option price change. Mathematically, rho = d(Option price) / d(r). For a vanilla call, rho is positive (calls become more valuable as rates rise, because the forward price embedded in the option goes up). For a vanilla put, rho is negative.

Rho is the smallest and most ignored of the first order greeks for short dated options because rate moves are slow relative to spot or vol moves, and the magnitude of rho is small for any option with less than a few months to expiry. For long dated options (LEAPS, multi year FX or commodity options), rho becomes material.

In FX options there are two rhos because two currencies are involved: domestic rho (sensitivity to domestic rate) and foreign rho (sensitivity to foreign rate, sometimes called phi). These are equal in magnitude and opposite in sign for ATM options at the forward.

## Why it matters (commodities and FX)

For most short dated trading, rho is a rounding error. The reasons it still matters:

- **Long dated FX options.** A 2 year [[EURUSD]] option has meaningful rho. When the [[Fed]] moves 25 bps unexpectedly, the rate differential shifts, the forward shifts, and long dated options reprice through rho before any vol or spot effect. FX dealers running multi year vol books actively hedge rho with [[Interest Rate Swap|interest rate swaps]] or government bonds.
- **Commodity calendar options.** Long dated [[Brent Crude]] or [[Gold Futures]] options (1+ year tenors) carry rho via the [[Cost of Carry]] that gets baked into the forward curve. Gold is especially sensitive because gold's no income carry means rates dominate its forward pricing.
- **Convertible bonds and structured products.** Embedded options with multi year tenors have rho that bond desks hedge alongside duration. If you trade convertibles or callable structures, rho is a real exposure.
- **Quanto and composite options.** Cross currency options have rho dependencies in both the underlying currency and the payoff currency.

For day to day commodity vol trading on front month options, rho can be safely ignored relative to delta, gamma, vega, and theta.

## Concrete example

A dealer is long a 2 year ATM call on [[EURUSD]], notional EUR 100M, strike at the forward (1.0950). Spot EURUSD: 1.0900. ATM vol: 8%. Domestic (USD) rate: 5.0%. Foreign (EUR) rate: 3.5%.

Domestic rho on this option: approximately +18,000 USD per 1 bp move in USD rates, or +1.8M USD per 100 bp move.

Scenario: Fed surprises with a 50 bp cut on a meeting day. USD rates drop from 5.0% to 4.5%. Pure rho P&L: -900,000 USD (lose 50 bps × 18,000 USD per bp).

But there are second order effects. The rate cut also widens EUR USD rate differential (less negative), which pushes the EURUSD forward up. The forward had been at 1.0950; now it is at roughly 1.1010. The ATM call is now ~60 pips ITM via the forward shift. Vega and gamma effects also kick in if vol moves.

Net: a single rate event creates a multi greek P&L event in long dated FX options. Without rho monitoring, the dealer thought their delta hedged book was insulated, when in fact 900,000 USD walked out on a single Fed decision.

If this had been a 3 month option instead of 2 year, the rho P&L would have been roughly 30,000 USD, a rounding error against typical vega and gamma noise. This is why short dated traders ignore rho and long dated traders cannot.

## Key mechanics and formulas

**Black Scholes rho for a call:**

`Rho_call = K × T × e^(-rT) × N(d2)`

**Black Scholes rho for a put:**

`Rho_put = -K × T × e^(-rT) × N(-d2)`

Where K = strike, T = time to expiry in years, r = risk free rate, N() = standard normal CDF, d2 = (ln(S/K) + (r - σ²/2) × T) / (σ × sqrt(T)).

**Scaling with time:** Rho grows roughly linearly with time to expiry. A 2 year option has roughly 8 times the rho of a 3 month option (same strike, same spot, same vol).

**FX options:** Two rhos exist:
- Domestic rho = ∂Price / ∂r_domestic
- Foreign rho (phi) = ∂Price / ∂r_foreign

For a call on EURUSD (USD payoff, EUR notional): domestic rho > 0, foreign rho < 0.

**Practical magnitude:**

For a 1Y ATM call on a $100 underlying at 20% vol, 5% rate:
- Rho ≈ $0.40 per 1% rate change (i.e., 4 cents per bp)

For the same option at 3 months: rho ≈ $0.10. At 1 month: rho ≈ $0.03.

**Bucketing for risk reporting:** Multi year option books report rho bucketed by tenor (1Y, 2Y, 5Y, 10Y) to allow hedging with specific points on the yield curve, not just parallel shifts.

## Prerequisites
- [[Option]]
- [[Black Scholes Model]]
- [[Greeks]]
- [[Forward Curve]]
- [[Cost of Carry]]

## Related concepts (learn next)
- [[Greeks]] - rho fits into the broader greek hierarchy and is the smallest first order greek for typical option books.
- [[Cost of Carry]] - rates enter option pricing primarily through the forward, which is set by [[Cost of Carry]]. Rho is the sensitivity to one component of carry.
- [[Forward Curve]] - the forward curve embeds rates. Long dated option rho is largely a forward curve sensitivity in disguise.
- [[Duration]] - rho is to options what duration is to bonds, with similar tenor scaling.
- [[Interest Rate Parity]] - the link between FX forwards and rate differentials, which determines FX option rho behavior.
- [[Delta]] - rho is often overshadowed by delta but for long dated options the two need joint hedging.
- [[Theta]] - rho and theta both scale with time but in opposite roles: theta is the cost of holding, rho is the sensitivity to financing.

## Common misconceptions

**"Rho is irrelevant."** True for short dated options. False for any book with multi year exposure, FX vol portfolios, or structured products. Convertible bond desks treat rho as a primary risk.

**"There is one rho for an FX option."** There are two: domestic and foreign. A book that is rho neutral domestically may have large foreign rho exposure. Both need separate hedging.

**"Rho hedging is done with rates futures."** Possible but often inefficient. Long dated rho is usually hedged with [[Interest Rate Swap|IRS]] at matching tenors, because the rho exposure has a specific tenor profile that swap curves match better than Eurodollar futures.

**"Higher rates always help calls."** Generally true via positive rho, but if higher rates trigger a spot selloff (rate shock kills equities or risk currencies), the delta loss often dwarfs the rho gain. Greek decomposition matters when interpreting P&L on rate event days.

## Sources

- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed. Chapter on greek letters.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed. Chapters on FX greeks and dual currency rho.
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed. Discussion of rho and long dated option pricing.
- Castagna, Antonio. *FX Options and Smile Risk*. Treatment of domestic and foreign rho in FX option books.
