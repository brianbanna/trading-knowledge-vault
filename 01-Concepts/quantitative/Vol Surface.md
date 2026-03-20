---
aliases: [vol surface, volatility surface, implied vol surface]
tags:
  - "#quant"
  - "#fx"
date-added: "2026-03-20"
---

# Vol Surface

## Definition
The volatility surface is a 2 dimensional map of [[implied volatility]] across 2 axes: [[Delta]] (or strike) and [[tenor]] (time to expiry). In FX, the surface is constructed from 3 market quotes at each tenor: [[ATM]] vol, [[Risk Reversal]], and [[Butterfly]]. These 3 numbers define the vol smile at a given tenor, and stacking smiles across tenors (overnight, 1 week, 1 month, 3 months, 6 months, 1 year) builds the full surface. The vol surface encodes the market's complete probabilistic view of future price distributions. Changes in the surface's shape, slope, and curvature are tradeable signals that distinguish sophisticated options traders from those who focus only on headline ATM vol.

## Why it matters (commodities and FX)
The vol surface is the central pricing and risk management tool for every options desk. In FX, all exotic products ([[Barrier Option]]s, [[Digital Option]]s, accumulators) are priced by calibrating models to the vanilla vol surface and then computing exotic payoffs under those dynamics. A mispriced vol surface means mispriced exotics, so desks monitor surface changes in real time. In commodities, the vol surface of [[Brent Crude]] options reveals term structure effects (front month vol is often higher), skew (puts are typically richer due to producer hedging), and event risk (spikes around [[OPEC]] or [[EIA Report]] dates). Trading the surface directly via RR and BF positions is a major source of alpha for vol desks.

## Concrete example
**Success:** A trader notices that EUR/USD 1 month [[Butterfly]] has compressed to 0.15 vols, the lowest level in 6 months, while 3 month BF remains at 0.40. She buys the 1 month 25D [[Strangle]] and sells the 3 month 25D strangle, betting on BF normalization. Over the next 2 weeks, a surprise French political crisis widens the 1 month BF to 0.50 while the 3 month barely moves. The trade profits approximately 15 pips on the BF expansion.

**Failure:** A trader observes that the USD/JPY vol surface is steeply inverted: 1 week vol at 14% and 1 month at 9%. He sells 1 week [[Straddle]]s and buys 1 month straddles, expecting the term structure to flatten. Instead, a trade war escalation keeps front end vol elevated for 3 weeks, and the 1 week straddle must be rolled at higher vol each week. Cumulative roll losses total 60 pips before the term structure finally normalizes.

## Key mechanics and formulas
- **Smile construction (FX)**: at each tenor, 5 points define the smile: 10D put, 25D put, ATM, 25D call, 10D call
- **From market quotes to strikes**: sigma(25D call) = ATM + 0.5 × [[Risk Reversal]] + [[Butterfly]]; sigma(25D put) = ATM minus 0.5 × RR + BF
- **Interpolation methods**: cubic spline in delta space, SABR model, or [[Vanna]] [[Volga]] method for inter strike interpolation
- **Term structure**: ATM vol plotted against tenor; typically upward sloping (normal) or inverted (crisis/event driven)
- **Sticky delta**: the assumption that the smile is fixed in delta space as spot moves (common in FX)
- **Sticky strike**: the assumption that vol at a given strike is fixed as spot moves (common in equity)
- **Surface dynamics**: changes in ATM (parallel shift), RR (skew tilt), and BF (curvature change) are the 3 independent risk factors

## Prerequisites
- [[ATM]]
- [[Risk Reversal]]
- [[Butterfly]]
- [[Delta]]
- [[Implied Volatility]]

## Related concepts (learn next)
- [[Vanna]]: sensitivity of the smile to spot moves; drives RR dynamics and delta hedging flow
- [[Volga]]: sensitivity of the smile curvature to vol levels; drives butterfly dynamics
- [[Gamma]]: the surface's strike dimension determines where gamma exposure concentrates
- [[Realized Volatility]]: the vol surface embeds expectations of future RV plus a risk premium
- [[Barrier Option]]: exotic pricing depends critically on the vol surface calibration, especially the smile
- [[Straddle]]: ATM straddle premium maps directly to the ATM point on the surface
- [[Strangle]]: strangle pricing maps to the wing points on the surface (25D and 10D)

## Common misconceptions
1. **"The vol surface is static."** The surface moves continuously throughout the trading day, driven by option supply/demand, spot moves, and new information. Morning and afternoon surfaces can differ by several tenths of a vol.
2. **"ATM vol is sufficient for risk management."** ATM vol captures only the center of the distribution. Ignoring the smile (RR and BF) underestimates the risk of OTM options and exotics by a wide margin.
3. **"You need complex models to trade the surface."** While SABR and local vol models are used for exotic pricing, many successful vol traders simply track ATM, RR, and BF time series and trade mean reversion or breakouts in these 3 quantities.
4. **"The vol surface implies a unique probability distribution."** Multiple models can fit the same surface but produce different dynamics, which is why exotic prices depend on model choice even when the vanilla surface is matched exactly.

## Sources
- Gatheral, Jim. *The Volatility Surface: A Practitioner's Guide*.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Castagna, Antonio. *FX Options and Smile Risk*.
