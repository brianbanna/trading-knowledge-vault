---
aliases: [volga, vomma, DvegaDvol]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Volga

## Definition
Volga (also called vomma) is the second order greek that measures the sensitivity of [[Vega]] to a change in [[implied volatility]], or equivalently, the second derivative of the option price with respect to implied vol. Mathematically, volga = d(vega)/d(vol) = d²(price)/d(vol)². Volga captures the convexity of the option price in the volatility dimension: a high volga position gains more from a vol increase than it loses from an equal vol decrease. OTM options have the highest volga because their vega is most sensitive to vol changes. Volga is the primary driver of [[Butterfly]] pricing and explains why OTM options (the "wings") trade at a premium to [[ATM]] in implied vol terms.

## Why it matters (commodities and FX)
Volga explains why the [[Vol Surface]] has a smile shape rather than being flat. Market makers who sell OTM options are short volga: if vol rises, the vega of those OTM options increases nonlinearly, amplifying their losses beyond what first order [[Vega]] predicted. To compensate for this volga risk, they charge a premium for wing options, producing the [[Butterfly]] spread. In FX, the [[Vanna]] [[Volga]] pricing method explicitly decomposes exotic option prices into a base price plus vanna and volga corrections, weighted by the market smile. In commodity markets, volga dynamics around [[Brent Crude]] and [[Henry Hub Natural Gas]] options determine how aggressively wing implied vols spike during crises relative to ATM vol.

## Concrete example
**Success:** EUR/USD 3 month 25D [[Butterfly]] is at 0.20 vols, historically low. A trader buys the BF (long [[Strangle]], short [[Straddle]]), which is essentially a long volga position. A banking crisis erupts, and implied vol spikes from 7% to 12%. The wings (25D options) see their vega jump nonlinearly because of volga, causing their vol to spike from 7.2% to 13.5% while ATM goes from 7% to 12%. The BF widens to 0.75 vols. The long volga position profits 22 pips from the disproportionate wing vol expansion.

**Failure:** A trader buys the [[Butterfly]] on USD/CHF (long volga) at 0.45 vols, expecting tail risk to increase. Instead, vol drifts lower from 8% to 7% over 6 weeks in a quiet market. The wings lose vega faster than ATM as vol falls (negative volga effect in reverse), compressing the BF to 0.35 vols. Combined with [[Theta]] decay from the long strangle leg, the position loses 10 pips.

## Key mechanics and formulas
- **Volga** = vega × (d1 × d2) / vol, where d1 and d2 are the standard Black Scholes parameters
- **Volga is zero at ATM** (approximately): since d1 × d2 is approximately 0 when d1 is near 0
- **Volga peaks at approximately 15 to 25 delta**: OTM options where both d1 and d2 have the same sign
- **Volga is always positive** for vanilla options: vega is a convex function of vol
- **Butterfly as a volga trade**: long BF = long volga exposure; the BF spread is proportional to the volga risk premium
- **Vanna Volga price adjustment** = 0.5 × volga × (market vol² minus BS vol²) / vol, approximating the smile correction
- **Volga P&L** = 0.5 × volga × (change in vol)²; quadratic in vol moves, making it profitable for large vol changes in either direction

## Prerequisites
- [[Vega]]
- [[Implied Volatility]]
- [[Butterfly]]
- [[Vol Surface]]
- [[Vanilla Option]]

## Related concepts (learn next)
- [[Butterfly]]: the direct market expression of volga; BF premium is the price of volga exposure
- [[Vanna]]: the other second order vol greek; vanna is the delta/vol cross, volga is the vega/vol second derivative
- [[Vega]]: volga describes how vega itself changes, making it a "gamma of vega"
- [[Strangle]]: long strangles carry significant positive volga, profiting from vol of vol
- [[Vol Surface]]: volga drives the curvature (smile) of the surface across strikes
- [[Barrier Option]]: barriers carry large volga near trigger levels, contributing to smile dynamics
- [[Risk Reversal]]: interacts with volga through the asymmetry of vanna across strikes

## Common misconceptions
1. **"Volga is negligible for ATM options."** While volga is smallest near ATM, it is not zero in practice because ATM is defined at the forward, not exactly where d1 × d2 = 0. For longer dated options, the difference matters.
2. **"Volga only matters for exotic pricing."** Vanilla [[Butterfly]] trading is directly a volga trade. Any position with significant OTM options has volga exposure that affects daily P&L.
3. **"Vol of vol and volga are the same thing."** Vol of vol describes the actual variability of implied vol over time (a statistical measure), while volga is a price sensitivity (a greek). They are related but distinct concepts.

## Sources
- Castagna, Antonio. *FX Options and Smile Risk*.
- Bossens, Frédéric et al. "Vanna-Volga Methods Applied to FX Derivatives," *International Journal of Theoretical and Applied Finance*, 2010.
- Gatheral, Jim. *The Volatility Surface: A Practitioner's Guide*.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
