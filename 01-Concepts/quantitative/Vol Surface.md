---
aliases: [vol surface, volatility surface, implied vol surface]
tags:
  - "#quant"
  - "#fx"
date-added: "2026-03-20"
---

# Vol Surface

## Definition
The volatility surface is a 2 dimensional map of [[implied volatility]] across [[Delta]] (or strike) and [[tenor]] (time to expiry). In FX, the surface is built from 3 market quotes at each tenor: [[ATM]] vol, [[Risk Reversal]], and [[Butterfly]]. These 3 numbers define the vol smile at a given tenor; stacking smiles across tenors (overnight, 1 week, 1 month, 3 months, 6 months, 1 year) builds the full surface. The surface encodes the market's complete probabilistic view of future price distributions. Changes in shape, slope, and curvature are tradeable signals separating sophisticated vol traders from those who watch only headline ATM vol.

## Why it matters (commodities and FX)
The vol surface is the central pricing and risk tool for every options desk. In FX, all exotic products ([[Barrier Option]]s, [[Digital Option]]s, accumulators) are priced by calibrating models to the vanilla surface, then computing exotic payoffs under those dynamics. A mispriced surface means mispriced exotics, so desks monitor surface changes in real time. In commodities, the [[Brent Crude]] surface reveals term structure (front month often higher), skew (puts richer from producer hedging), and event risk (spikes around [[OPEC]] or [[EIA Report]] dates). Trading the surface via RR and BF positions is a major alpha source for vol desks.

## Concrete example

**Concrete:** Trader notices EURUSD 1 month [[Butterfly]] has compressed to 0.15 vols, lowest in 6 months, while 3 month BF remains at 0.40. She buys the 1 month 25D [[Strangle]] and sells the 3 month 25D strangle, betting on BF normalization. Over 2 weeks a surprise French political crisis widens the 1 month BF to 0.50 while 3 month barely moves. Profit ~15 pips on the BF expansion. Contrast: trader observes USDJPY vol surface steeply inverted: 1 week vol at 14%, 1 month at 9%. Sells 1 week [[Straddle]]s and buys 1 month, expecting term structure to flatten. Trade war escalation keeps front end elevated for 3 weeks; the 1 week straddle rolls at higher vol each week. Cumulative roll losses 60 pips before term structure normalizes.

**Simplified:** The vol surface is a map showing what vol the market is willing to trade at every strike and every tenor. ATM vol is one point. Strangle vol is another point (wings). Calendar structure is a slice through time. The whole surface moves continuously, and the patterns of how it moves are what vol traders bet on. Most retail option pricing thinks in a single number; pros think in a 2D map and trade the shape changes.

## Key mechanics and formulas
- **Smile construction (FX)**: at each tenor, 5 points define the smile: 10D put, 25D put, ATM, 25D call, 10D call
- **From market quotes to strikes**: sigma(25D call) = ATM + 0.5 × [[Risk Reversal]] + [[Butterfly]]; sigma(25D put) = ATM - 0.5 × RR + BF
- **Interpolation methods**: cubic spline in delta space, SABR model, or [[Vanna]] [[Volga]] for inter strike interpolation
- **Term structure**: ATM vol plotted against tenor; typically upward sloping (normal) or inverted (crisis/event driven)
- **Sticky delta**: assumption that the smile is fixed in delta space as spot moves (common in FX)
- **Sticky strike**: assumption that vol at a given strike is fixed as spot moves (common in equity)
- **Surface dynamics**: changes in ATM (parallel shift), RR (skew tilt), and BF (curvature) are the 3 independent risk factors

## Prerequisites
- [[ATM]]
- [[Risk Reversal]]
- [[Butterfly]]
- [[Delta]]
- [[Implied Volatility]]

## Related concepts (learn next)
- [[Vanna]]: sensitivity of the smile to spot moves. Drives RR dynamics and delta hedging flow.
- [[Volga]]: sensitivity of smile curvature to vol levels. Drives butterfly dynamics.
- [[Gamma]]: the surface's strike dimension determines where gamma exposure concentrates.
- [[Realized Volatility]]: the surface embeds expectations of future RV plus a risk premium.
- [[Barrier Option]]: exotic pricing depends on surface calibration, especially the smile.
- [[Straddle]]: ATM straddle premium maps to the ATM point on the surface.
- [[Strangle]]: strangle pricing maps to wing points (25D and 10D).

## Common misconceptions
1. **"The vol surface is static."** The surface moves continuously throughout the trading day, driven by option supply/demand, spot moves, and new information. Morning and afternoon surfaces can differ by several tenths of a vol.
2. **"ATM vol is sufficient for risk management."** ATM captures only the center of the distribution. Ignoring RR and BF understates OTM and exotic risk by a wide margin.
3. **"You need complex models to trade the surface."** SABR and local vol are used for exotic pricing, but many successful vol traders simply track ATM, RR, BF time series and trade mean reversion or breakouts.
4. **"The vol surface implies a unique probability distribution."** Multiple models fit the same surface but produce different dynamics, which is why exotic prices depend on model choice even when the vanilla surface is matched exactly.

## Sources
- Gatheral, Jim. *The Volatility Surface: A Practitioner's Guide*.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Castagna, Antonio. *FX Options and Smile Risk*.
