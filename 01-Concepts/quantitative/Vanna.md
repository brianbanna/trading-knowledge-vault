---
aliases: [vanna, DdeltaDvol, delta-vol cross greek]
tags:
  - "#quant"
  - "#fx"
date-added: "2026-03-20"
---

# Vanna

## Definition
Vanna is the second order cross [[Greeks|greek]] measuring sensitivity of [[Delta]] to a change in [[implied volatility]], or equivalently sensitivity of [[Vega]] to a change in the [[underlying]]. Vanna = d(delta)/d(vol) = d(vega)/d(spot). For a call, vanna is positive when OTM (vol up = delta up) and negative when ITM. Vanna is the key greek for understanding [[Risk Reversal]] positions and how [[Vol Surface]] dynamics interact with spot. In FX, vanna driven hedging flows from large exotic and structured product books are a significant spot driver.

## Why it matters (commodities and FX)
Vanna is the most underappreciated greek in FX options. Large dealer books carry substantial vanna from [[Barrier Option]]s and structured products. When vol rises, vanna pushes OTM option delta up, forcing dealers to rehedge in spot. This creates a feedback loop: rising vol changes delta, triggers spot hedging, moves spot further, changes vol again. In pairs with heavy exotic flow (EURUSD, USDJPY, AUDUSD), vanna driven rehedging is the dominant intraday flow. Vanna explains why certain spot levels act as magnets and why risk reversals predict spot direction.

## Concrete example

**Concrete:** Dealers are long a large amount of EURUSD 25D calls (short vanna: vol up = delta up = sell EUR). EURUSD vol compresses 8.5% to 7.5%, reducing OTM call delta and forcing dealers to buy EUR to maintain hedges. The trader buys EURUSD, riding the vanna driven buying. Spot rallies 40 pips over 2 days as vol drops further. Contrast: trader assumes vanna flows push USDJPY lower as vol spikes (dealers rehedging short OTM puts by selling USD). BOJ intervenes to support the yen with a massive spot move overwhelming the vanna effect. The vanna model predicted gradual; the intervention produced a 500 pip gap making the vanna signal irrelevant.

**Simplified:** Vanna is how delta changes when vol moves. If you own OTM options, rising vol makes them more likely to finish ITM, so their delta moves toward 0.5 (or -0.5 for puts). Anyone hedging these options has to adjust their spot position when vol moves, not just when spot moves. In FX, dealer books are big and skewed, so vol moves trigger predictable spot flows. Watching vanna flows tells you which way dealers will be forced to trade.

## Key mechanics and formulas
- **Vanna** = d(delta)/d(vol) = d(vega)/d(spot) = (- d1 / vol) × N'(d1) × e^(- foreign rate × time)
- **Sign convention**: OTM call vanna is positive (vol up = delta up); OTM put vanna is negative (vol up = delta more negative)
- **Vanna is zero at ATM** (approximately): ATM delta is relatively insensitive to vol
- **Vanna peaks** at ~25 delta, which is why the 25D [[Risk Reversal]] captures the smile's skew at maximum vanna sensitivity
- **Vanna flow** = aggregate vanna × change in vol; the net spot hedging flow from a vol move
- **Vanna Volga pricing**: the [[Vanna]] [[Volga]] method prices exotics by adjusting Black Scholes with vanna and volga corrections weighted by the smile

## Prerequisites
- [[Delta]]
- [[Vega]]
- [[Implied Volatility]]
- [[Vol Surface]]
- [[Risk Reversal]]

## Related concepts (learn next)
- [[Volga]]: the other second order vol greek. Vanna captures delta/vol interaction; volga captures vega/vol interaction.
- [[Risk Reversal]]: significant net vanna position (long OTM call, short OTM put).
- [[Vol Surface]]: vanna determines how the smile shifts as spot moves (sticky delta vs sticky strike).
- [[Delta]]: vanna describes how delta changes with vol, complementing [[Gamma]] which describes how delta changes with spot.
- [[Barrier Option]]: barriers carry large vanna near the barrier, driving spot flows.
- [[Gamma]]: spot convexity in price; vanna is cross convexity between price and vol.
- [[Expiry Pinning]]: vanna flows near large option positions amplify or dampen pinning.

## Common misconceptions
1. **"Vanna is too esoteric to matter practically."** In FX, vanna driven flows from exotic books are often the largest systematic flow, routinely moving spot 20 to 50 pips in major pairs.
2. **"Vanna is always small."** For OTM options or barriers, vanna can dominate. A [[Barrier Option]] near its trigger has vanna dwarfing its delta and gamma.
3. **"Vanna effects cancel across the market."** Dealer books are structurally skewed (e.g., consistently short downside barriers in USDJPY), so aggregate vanna is not zero and creates directional spot pressure.

## Sources
- Bossens, Frédéric et al. "Vanna-Volga Methods Applied to FX Derivatives," *International Journal of Theoretical and Applied Finance*, 2010.
- Castagna, Antonio. *FX Options and Smile Risk*.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
