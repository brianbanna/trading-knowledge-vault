---
aliases: [option, call option, put option, commodity option]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Option

## Definition
An option is a contract giving the buyer the right, not the obligation, to buy (call) or sell (put) an underlying at a strike price on or before an expiry date. The buyer pays a premium upfront. Payoff is asymmetric: maximum loss for the buyer is the premium; upside is theoretically unlimited for calls and substantial for puts (down to zero). The seller (writer) collects premium but assumes unlimited risk on calls and large risk on puts. Commodity options trade both on exchanges (CME, ICE) on futures underlyings, and OTC for customized structures. Price is set by underlying, strike, time, rate, and [[Implied Volatility]], captured by Black Scholes or Black 76 for options on futures.

## Why it matters (commodities and FX)
Options manage asymmetric risk. A producer buys [[put options|puts]] to protect against price drops while keeping upside, unlike a [[Futures Contract|futures]] or [[Swap]] hedge that locks both directions. A consumer buys calls to cap input costs while benefiting from drops. Options enable pure volatility trades: a straddle (call + put at the same strike) profits from large moves either direction. [[Implied Volatility]] reveals the market's forward looking uncertainty, a richer signal than futures alone. Sophisticated traders get exposure to [[Volatility Smile|skew]], term structure, and convexity that linear instruments cannot replicate.

## Concrete example

**Concrete:** A gold miner buys a 3M COMEX put, strike $2,300/oz, spot $2,400. Premium $50/oz ($5,000 per 100 oz contract). Gold drops to $2,100. Intrinsic value $200/oz, minus $50 premium = $150/oz net, or $15,000 per contract. Physical revenue declined but the put offsets. Max loss was capped at the $50 premium. Adverse case: a nat gas trader buys $3.50 Henry Hub calls at $0.15/MMBtu premium expecting cold winter. Winter is mild, gas stays below $3.00, calls expire worthless. Loss: full $0.15/MMBtu ($1,500 per contract). Buy 6 consecutive months and the cumulative $9,000 loss shows options are wasting assets that need the move to occur within the lifetime.

**Simplified:** You pay a small upfront cost (premium) for the right to buy or sell at a fixed price later. If the price moves your way, you exercise and profit. If not, you walk away losing only the premium. Selling the option flips it: you collect the premium but take the asymmetric downside. Insurance, basically.

## Key mechanics and formulas
- **Option value:** Premium = Intrinsic + Time value
  - Intrinsic (call) = max(Underlying minus Strike, 0)
  - Intrinsic (put) = max(Strike minus Underlying, 0)
  - Time value decays toward expiry ([[Theta]])
- **Black 76 (options on futures):** C = e^(-rT) × [F × N(d1) minus K × N(d2)], where F = futures, K = strike, r = rate, T = time, d1 = [ln(F/K) + (sigma^2/2) × T] / (sigma × sqrt(T)), d2 = d1 minus sigma × sqrt(T)
- **Key Greeks:**
  - [[Delta]]: sensitivity to underlying (0 to 1 calls, -1 to 0 puts)
  - [[Gamma]]: rate of change of delta; highest for ATM near expiry
  - [[Theta]]: daily time decay; the cost of owning options
  - [[Vega]]: sensitivity to [[Implied Volatility]]; PnL per 1 point vol change

## Prerequisites
- [[Futures Contract]]
- [[Implied Volatility]]
- [[Margin]]

## Related concepts (learn next)
- [[Implied Volatility]]: the key variable beyond observable inputs
- [[Volatility Smile]]: how IV varies across strikes, revealing tail risk perception
- [[Spread Trade]] using options (call spreads, put spreads, straddles, strangles): defined risk expressions
- [[Weather Premium]] in grain options: seasonal opportunity for vol buyers and sellers
- [[Margin]] for option sellers: substantial and changes with market moves
- [[Basis Risk]]: when options on one underlying hedge a related but different exposure
- [[Forward Contract]]: linear hedging alternative; options add asymmetry
- [[Cash Settlement]]: many commodity options settle into the underlying futures rather than physical

## Common misconceptions
- **"Buying options is always safer than futures."** Premium is capped but real and often substantial. Options expire worthless more than 50% of the time in many environments; buyers must be selective.
- **"Selling options is easy money."** Premium income is steady but tail risk is real. One large adverse move (nat gas tripling in a polar vortex) wipes years of premium in a single event.
- **"Options are too complex for commodity trading."** Used daily by producers, consumers, and speculators. Core concepts (insurance, asymmetric payoff, premium as cost of protection) are intuitive even when the pricing math is not.

## Sources
- John Hull, "Options, Futures, and Other Derivatives"
- Sheldon Natenberg, "Option Volatility and Pricing"
- CME Group, "Introduction to Options on Futures"
- Fischer Black, "The Pricing of Commodity Contracts," Journal of Financial Economics, 1976
