---
aliases: [digital option, binary option, digital]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Digital Option

## Definition
A digital option (binary option) pays a fixed amount if the [[underlying]] finishes above (digital call) or below (digital put) a [[strike price]] at [[expiry]], and zero otherwise. The payoff is all or nothing: no proportional relationship to the size of the move. A typical FX digital pays USD 1M if EUR/USD is above 1.1000 at 10 AM NY on expiry, whether spot is 1.1001 or 1.1200. Digitals are embedded in structured products and are closely related to [[Barrier Option]]s. Hedging digitals near expiry creates extreme [[Gamma]] and [[Delta]] challenges for dealers.

## Why it matters (commodities and FX)
Digital options are widely used in FX structured products, range accruals, and target redemption notes. The all or nothing payoff is attractive for specific payout scenarios, but the hedging challenge near expiry shapes market dynamics. A dealer short a large digital call at 1.1000 faces delta jumping from near 0 to near 1 (or reverse) as spot oscillates around the strike in the final hours, forcing aggressive trading that often causes spot to whip around the strike. In commodities, digital payoffs are embedded in weather derivatives, trigger swaps, and structured notes on [[Brent Crude]] or [[Gold Futures]].

## Concrete example
**Concrete:** Trader buys a 1 month EUR/USD digital call, strike 1.1000, paying 35% of USD 1M notional ($350,000 premium). Spot 1.0900. Over the month EUR rallies to 1.1050 at expiry. Digital pays USD 1M. Net profit $650,000. The day before expiry, spot reaches 1.1020 and the position looks won. In the final 2 hours, a large USD buying flow pushes spot to 1.0995 at the 10 AM fix. Digital expires 5 pips OTM and pays zero. The full $350,000 premium is gone. Being 5 pips away from a $1M payout illustrates the binary risk.

**Simplified:** A digital is a yes/no bet. If spot is above the strike at expiry, you get a fixed payout. If it is below, you get nothing. There is no partial credit. The dealer who sold it has a hedging nightmare in the last hour: if spot sits right on the strike, their delta swings from 0 to 1 on every tick, so they trade huge size to stay flat. That trading is what makes spot jump around the digital strike near expiry.

## Key mechanics and formulas
- **Digital call payoff:** fixed payout if spot at expiry > strike, else 0
- **Digital put payoff:** fixed payout if spot at expiry < strike, else 0
- **Digital call price:** e^(−r_d × T) × N(d2) × payout, with d2 the standard Black Scholes d2
- **Replication via call spread:** buy a call at strike K, sell a call at K + ε, scaled by payout/ε. As ε → 0, converges to the digital
- **Delta near expiry:** for an ATM digital with minutes to expiry, theoretical delta → ∞. In practice, the replicating call spread has delta = payout/ε
- **Vega:** digital call has negative vega when ITM (higher vol reduces probability of staying above) and positive vega when OTM
- **Overhedge convention:** dealers price digitals by shifting the strike by the replicating call spread width, producing a conservative quote

## Prerequisites
- [[Vanilla Option]]
- [[Delta]]
- [[Gamma]]
- [[Implied Volatility]]
- [[ATM]]

## Related concepts (learn next)
- [[Barrier Option]]: a digital at expiry is mathematically equivalent to a European barrier; both share discontinuous payoff risk.
- [[Expiry Pinning]]: digital hedging near expiry creates flows similar to strike pinning from vanilla gamma.
- [[Gamma]]: digital gamma is extreme near the strike at expiry, the most challenging hedging scenario in options.
- [[Vol Surface]]: digital pricing depends on local [[implied volatility]] at the strike, not just [[ATM]] vol.
- [[Risk Reversal]]: skew affects digital pricing because the probability of finishing above or below the strike depends on the full implied distribution.
- [[Vanna]]: digital vanna can be extremely large near the strike, amplifying vol/spot feedback.
- [[Straddle]]: a straddle near a digital strike can hedge the explosive gamma.

## Common misconceptions

**"Digital options are simple because the payoff is binary."** Payoff is simple, hedging is among the most complex in derivatives. The replicating portfolio requires infinitely tight call spreads in theory.

**"Fair price equals risk neutral probability of finishing ITM."** True only in the idealized risk neutral measure. Actual pricing includes vol smile, replicating call spread bid/offer, and dealer overhedge premium.

**"Digitals are banned everywhere."** Retail binary platforms (often scams) are banned in many jurisdictions. Institutional digitals in FX and commodities remain standard and fully legal in the interbank market.

**"You can perfectly hedge a digital."** No finite call spread perfectly replicates a discontinuous payoff. The residual gap is pin risk, and it is unhedgeable.

## Sources
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
