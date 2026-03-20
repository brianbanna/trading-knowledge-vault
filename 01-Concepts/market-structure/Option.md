---
aliases: [option, call option, put option, commodity option]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Option

## Definition
An option is a financial contract that gives the buyer the right, but not the obligation, to buy (call) or sell (put) an underlying asset at a specified strike price on or before a specified expiry date. The buyer pays a premium upfront for this right. Options provide asymmetric payoffs: the buyer's maximum loss is limited to the premium paid, while potential profit is theoretically unlimited for calls and substantial for puts (down to zero). The seller (writer) of an option receives the premium income but assumes potentially unlimited risk on calls and large risk on puts. In commodity markets, options are traded both on exchanges (CME, ICE) referencing futures as the underlying, and OTC for customized structures. The price of an option is determined by the underlying price, strike price, time to expiry, risk free rate, and [[Implied Volatility]], as captured by the Black Scholes or Black 76 model for commodity options on futures.

## Why it matters (commodities and FX)
Options are essential for managing asymmetric risk in commodity and FX markets. A producer can buy [[put options|put]] options to protect against price drops while retaining full upside, unlike a [[Futures Contract|futures]] or [[Swap]] hedge that locks in both directions. A consumer can buy calls to cap input costs while benefiting if prices fall. Options also enable pure volatility trades: buying a straddle (call + put at the same strike) profits from large moves regardless of direction. The [[Implied Volatility]] embedded in option prices reveals the market's forward looking expectation of uncertainty, providing a richer set of signals than futures prices alone. For sophisticated traders, option markets offer exposure to [[Volatility Smile|skew]], term structure, and convexity that cannot be replicated with linear instruments.

## Concrete example
**Success case:** A gold miner buys a 3 month put option on COMEX gold with a strike of $2,300/oz when spot is at $2,400/oz. The premium is $50/oz ($5,000 per 100 oz contract). Gold drops to $2,100/oz. The put's intrinsic value is $200/oz, minus the $50 premium = $150/oz net profit, or $15,000 per contract. The miner's physical gold revenue declined, but the put payout partially offsets the loss. Maximum loss on the option was limited to the $50/oz premium.

**Failure case:** A natural gas trader buys $3.50 call options on Henry Hub at a premium of $0.15/MMBtu ($1,500 per 10,000 MMBtu contract) expecting a cold winter. Winter temperatures are mild, gas stays below $3.00, and the calls expire worthless. Loss: the full $0.15/MMBtu premium, or $1,500 per contract. If the trader had bought calls for 6 consecutive months at similar premiums, the cumulative $9,000 loss without a payoff demonstrates that buying options is a wasting asset strategy that requires the anticipated move to occur within the option's lifetime.

## Key mechanics and formulas
- **Option value:** Premium = Intrinsic value + Time value
  - Intrinsic value (call) = max(Underlying price - Strike, 0)
  - Intrinsic value (put) = max(Strike - Underlying price, 0)
  - Time value decays as expiry approaches ([[Theta]])
- **Black 76 model (commodity options on futures):** C = e^(-rT) x [F x N(d1) - K x N(d2)], where F = futures price, K = strike, r = risk free rate, T = time, N() = cumulative normal, d1 = [ln(F/K) + (sigma^2/2) x T] / (sigma x sqrt(T)), d2 = d1 - sigma x sqrt(T)
- **Key Greeks:**
  - [[Delta]]: sensitivity to underlying price (0 to 1 for calls, -1 to 0 for puts)
  - [[Gamma]]: rate of change of delta; highest for ATM options near expiry
  - [[Theta]]: daily time decay; the cost of owning options
  - [[Vega]]: sensitivity to [[Implied Volatility]]; $P&L per 1 point vol change

## Prerequisites
- [[Futures Contract]]
- [[Implied Volatility]]
- [[Margin]]

## Related concepts (learn next)
- [[Implied Volatility]] is the key variable that determines option prices beyond the observable inputs.
- [[Volatility Smile]] shows how IV varies across strike prices, revealing the market's perception of tail risk.
- [[Spread Trade]] using options (call spreads, put spreads, straddles, strangles) enables defined risk expressions.
- [[Weather Premium]] in grain options is a seasonal opportunity for both vol buyers and sellers.
- [[Margin]] for option sellers can be substantial and changes with market moves.
- [[Basis Risk]] exists when options on one underlying are used to hedge a related but different exposure.
- [[Forward Contract]] is the linear hedging alternative; options add the dimension of asymmetric payoff.
- [[Cash Settlement]] applies to many commodity options that settle into the underlying futures rather than physical delivery.

## Common misconceptions
- **"Buying options is always safer than futures."** Options limit maximum loss to the premium, but that premium is a real and often substantial cost. In many environments, options expire worthless more than 50% of the time, meaning option buyers must be selective about when and how they deploy capital.
- **"Selling options is easy money."** Option selling earns premium consistently but assumes tail risk. A single large adverse move (e.g., natural gas tripling during a polar vortex) can wipe out years of premium income in a single event.
- **"Options are too complex for commodity trading."** Options are used daily by producers, consumers, and speculative traders. The core concepts (insurance, asymmetric payoff, premium as cost of protection) are intuitive even if the mathematical pricing models are complex.

## Sources
- John Hull, "Options, Futures, and Other Derivatives"
- Sheldon Natenberg, "Option Volatility and Pricing"
- CME Group, "Introduction to Options on Futures"
- Fischer Black, "The Pricing of Commodity Contracts," Journal of Financial Economics, 1976
