---
aliases: [digital option, binary option, digital]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Digital Option

## Definition
A digital option (also called a binary option) pays a fixed amount if the [[underlying]] finishes above (digital call) or below (digital put) a specified [[strike price]] at [[expiry]], and pays nothing otherwise. The payoff is all or nothing: there is no proportional relationship between the size of the move and the payout. In FX, a typical digital might pay USD 1 million if EUR/USD is above 1.1000 at 10 AM New York time on expiry date, regardless of whether it is at 1.1001 or 1.1200. Digitals are embedded in many structured products and are closely related to [[Barrier Option]]s. The hedging of digital options near expiry creates extreme [[Gamma]] and [[Delta]] challenges for dealers.

## Why it matters (commodities and FX)
Digital options are widely used in FX structured products, range accruals, and target redemption notes. Their all or nothing payoff makes them attractive to clients seeking specific payout scenarios, but the hedging challenge they create near expiry makes them significant for market dynamics. A dealer who is short a large digital call at 1.1000 faces a delta that jumps from near 0 to near 1 (or vice versa) as spot oscillates around the strike in the final hours. This forces aggressive buying and selling near the strike level, often causing spot to oscillate violently around the digital strike near expiry. In commodities, digital payoffs are embedded in weather derivatives, trigger swaps, and structured notes on [[Brent Crude]] or [[Gold Futures]].

## Concrete example
**Success:** A trader buys a 1 month EUR/USD digital call with strike 1.1000, paying 35% of the USD 1 million notional payout (USD 350,000). Spot is at 1.0900. Over the next month, EUR rallies to 1.1050 at expiry. The digital pays out USD 1 million. Net profit is USD 650,000. The payout is the same whether EUR finished at 1.1001 or 1.1200.

**Failure:** Same digital call at 1.1000. Spot reaches 1.1020 the day before expiry, and the trader is sitting on an apparent win. In the final 2 hours of trading, a large USD buying flow pushes spot to 1.0995 at the 10 AM fix. The digital expires 5 pips out of the money and pays zero. The full USD 350,000 premium is lost. Being 5 pips away from a USD 1 million payout illustrates the binary nature of the risk.

## Key mechanics and formulas
- **Digital call payoff** = fixed payout if spot at expiry > strike, else 0
- **Digital put payoff** = fixed payout if spot at expiry < strike, else 0
- **Digital call price** = e^(negative domestic rate × time) × N(d2) × payout, where d2 is the standard Black Scholes d2
- **Digital as a call spread**: a digital call can be replicated (approximately) by buying a call at strike K and selling a call at strike K + epsilon, scaled by payout / epsilon. As epsilon approaches 0, this converges to the digital
- **Delta near expiry**: for a digital call near the strike with minutes to expiry, delta approaches infinity in theory (the payoff is a step function). In practice, the replicating call spread has delta = payout / epsilon
- **Vega of a digital**: a digital call has negative vega when in the money (higher vol reduces the probability of staying above the strike) and positive vega when out of the money
- **Overhedge/underhedge convention**: dealers typically price digitals by shifting the strike by the spread of the replicating call spread, creating a conservative price

## Prerequisites
- [[Vanilla Option]]
- [[Delta]]
- [[Gamma]]
- [[Implied Volatility]]
- [[ATM]]

## Related concepts (learn next)
- [[Barrier Option]]: a digital at expiry is mathematically equivalent to a European barrier; both share discontinuous payoff risk
- [[Expiry Pinning]]: digital hedging near expiry creates extreme flows similar to strike pinning from vanilla gamma
- [[Gamma]]: digital gamma is extreme near the strike at expiry, creating the most challenging hedging scenario in options
- [[Vol Surface]]: digital pricing depends on the local [[implied volatility]] at the strike, not just [[ATM]] vol
- [[Risk Reversal]]: skew affects digital pricing because the probability of finishing above or below the strike depends on the full implied distribution
- [[Vanna]]: digital option vanna can be extremely large near the strike, amplifying vol/spot feedback loops
- [[Straddle]]: a straddle near a digital strike can be used to hedge the explosive gamma of the digital

## Common misconceptions
1. **"Digital options are simple because the payoff is binary."** The payoff is simple, but the hedging is among the most complex in derivatives. The replicating portfolio requires infinitely tight call spreads in theory, which is impossible in practice.
2. **"The fair price of a digital is the probability of finishing in the money."** This is only true under the risk neutral measure. The actual price includes the vol smile effect, the bid/offer spread of the replicating call spread, and the overhedge premium charged by dealers.
3. **"Digitals are banned everywhere."** Retail binary options (often scam platforms) have been banned in many jurisdictions, but institutional digital options in FX and commodities remain standard, actively traded, and fully legal in the interbank market.
4. **"You can perfectly hedge a digital."** No finite call spread can perfectly replicate a discontinuous payoff. The residual risk (the gap between the theoretical digital and the practical call spread hedge) is called "pin risk" and is unhedgeable.

## Sources
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
