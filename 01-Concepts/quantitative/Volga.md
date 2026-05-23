---
aliases: [volga, vomma, DvegaDvol]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Volga

## Definition
Volga (also vomma) is the second order greek measuring sensitivity of [[Vega]] to a change in [[implied volatility]], or the second derivative of option price with respect to implied vol. Volga = d(vega)/d(vol) = d²(price)/d(vol)². Volga captures the convexity of option price in the vol dimension: a high volga position gains more from a vol increase than it loses from an equal vol decrease. OTM options have the highest volga because their vega is most sensitive to vol changes. Volga drives [[Butterfly]] pricing and explains why OTM wings trade at a premium to [[ATM]] in implied vol terms.

## Why it matters (commodities and FX)
Volga is why the [[Vol Surface]] has a smile shape rather than being flat. Market makers who sell OTM options are short volga: if vol rises, the vega of those OTM options increases nonlinearly, amplifying losses beyond what first order [[Vega]] predicted. To compensate, they charge a premium for wings, producing the [[Butterfly]] spread. In FX, the [[Vanna]] [[Volga]] pricing method explicitly decomposes exotic prices into a base plus vanna and volga corrections weighted by the market smile. In commodity markets, volga dynamics around [[Brent Crude]] and [[Henry Hub Natural Gas]] options determine how aggressively wing implied vols spike during crises relative to ATM.

## Concrete example

**Concrete:** EURUSD 3 month 25D [[Butterfly]] at 0.20 vols, historically low. Trader buys the BF (long [[Strangle]], short [[Straddle]]), a long volga position. A banking crisis erupts; implied vol spikes 7% to 12%. The wings see vega jump nonlinearly via volga, causing 25D vol to spike 7.2% to 13.5% while ATM goes 7% to 12%. BF widens to 0.75 vols. Long volga profits 22 pips on the disproportionate wing expansion. Contrast: trader buys USDCHF BF (long volga) at 0.45 vols expecting tail risk to rise. Vol drifts lower 8% to 7% over 6 weeks in a quiet market. Wings lose vega faster than ATM as vol falls (negative volga in reverse), compressing BF to 0.35 vols. Combined with [[Theta]] decay from the long strangle leg, position loses 10 pips.

**Simplified:** Volga is gamma but for vol. If you own OTM options, big vol moves help you more than small vol moves hurt you. That asymmetry has a price: it is the cost of butterflies in the market. Short volga positions die in vol spikes because their vega itself grows as vol rises, accelerating losses. Long volga positions are how you bet on tail vol events without making a directional bet on whether vol goes up or down.

## Key mechanics and formulas
- **Volga** = vega × (d1 × d2) / vol, d1 and d2 standard Black Scholes parameters
- **Volga is zero at ATM** (approximately): d1 × d2 ≈ 0 when d1 is near 0
- **Volga peaks at ~15 to 25 delta**: OTM options where d1 and d2 have the same sign
- **Volga is always positive** for vanilla options: vega is a convex function of vol
- **Butterfly as a volga trade**: long BF = long volga. BF spread is proportional to the volga risk premium.
- **Vanna Volga price adjustment** = 0.5 × volga × (market vol² - BS vol²) / vol, approximating the smile correction
- **Volga P&L** = 0.5 × volga × (change in vol)². Quadratic in vol moves, profitable for large vol changes in either direction.

## Prerequisites
- [[Vega]]
- [[Implied Volatility]]
- [[Butterfly]]
- [[Vol Surface]]
- [[Vanilla Option]]

## Related concepts (learn next)
- [[Butterfly]]: direct market expression of volga. BF premium is the price of volga exposure.
- [[Vanna]]: the other second order vol greek. Vanna is delta/vol cross; volga is vega/vol second derivative.
- [[Vega]]: volga describes how vega itself changes, making it a "gamma of vega."
- [[Strangle]]: long strangles carry significant positive volga, profiting from vol of vol.
- [[Vol Surface]]: volga drives surface curvature (smile) across strikes.
- [[Barrier Option]]: barriers carry large volga near triggers, contributing to smile dynamics.
- [[Risk Reversal]]: interacts with volga through vanna asymmetry across strikes.

## Common misconceptions
1. **"Volga is negligible for ATM options."** Volga is smallest near ATM but not zero in practice. ATM is defined at the forward, not exactly where d1 × d2 = 0. Matters for longer dated options.
2. **"Volga only matters for exotic pricing."** Vanilla [[Butterfly]] trading is directly a volga trade. Any position with significant OTM options has volga exposure affecting daily P&L.
3. **"Vol of vol and volga are the same thing."** Vol of vol is the actual variability of implied vol over time (statistical). Volga is a price sensitivity (greek). Related but distinct.

## Sources
- Castagna, Antonio. *FX Options and Smile Risk*.
- Bossens, Frédéric et al. "Vanna-Volga Methods Applied to FX Derivatives," *International Journal of Theoretical and Applied Finance*, 2010.
- Gatheral, Jim. *The Volatility Surface: A Practitioner's Guide*.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
