---
aliases: [butterfly, butterfly spread, 25 delta butterfly, 25D BF]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Butterfly

## Definition
The butterfly (BF) in FX options is the average of the 25 delta call and 25 delta put [[implied volatility]] minus the [[ATM]] implied volatility. It measures how much more expensive the wings (OTM options) are relative to the ATM center of the [[Vol Surface]]. A higher butterfly indicates fatter tails in the implied distribution, meaning the market prices a greater probability of large moves in either direction. As a trading strategy, a long butterfly involves buying the 25D [[Strangle]] (OTM call + OTM put) and selling the [[ATM]] [[Straddle]], isolating exposure to the curvature of the smile. The butterfly is 1 of 3 standard FX vol quotes, alongside [[ATM]] vol and [[Risk Reversal]].

## Why it matters (commodities and FX)
The butterfly captures the market's pricing of tail risk and kurtosis. In FX, butterflies widen ahead of high impact events like central bank decisions, elections, or referendums because the market assigns higher probability to extreme outcomes. A persistently elevated butterfly on a pair like USD/TRY or USD/BRL signals ongoing structural tail risk from emerging market crises. In commodities, butterflies on [[Brent Crude]] options widen ahead of [[OPEC]] meetings and geopolitical escalations. Monitoring butterfly changes helps traders assess whether tail insurance is cheap or expensive relative to the actual frequency of large moves.

## Concrete example
**Success:** EUR/USD 1 month 25D butterfly is at 0.25 vols, historically low ahead of the French presidential election. A trader buys the butterfly: long the 25D strangle and short the ATM straddle for a net debit of 5 pips. The election produces a surprise result, and EUR/USD gaps 300 pips. The 25D strangle explodes in value while the short straddle loses less (it was closer to the money). The butterfly position profits 35 pips as the smile steepens and the BF jumps to 0.85.

**Failure:** A trader buys the 25D butterfly on GBP/USD ahead of a Bank of England meeting, paying 0.55 vols for the structure. The BOE delivers an in line decision, vol collapses evenly across the surface, and the smile flattens. The 25D BF drops to 0.30. The long strangle decays faster than the short straddle recovers, and the position loses 12 pips from [[Theta]] and vol compression. Wings gave back their event premium without a tail move.

## Key mechanics and formulas
- **25D Butterfly** = 0.5 × (sigma(25D call) + sigma(25D put)) minus sigma(ATM)
- **Always positive**: because OTM options carry tail risk premium, the BF is almost always above zero
- **Recovering wing vols**: sigma(25D call) = ATM + 0.5 × [[Risk Reversal]] + BF; sigma(25D put) = ATM minus 0.5 × RR + BF
- **10D Butterfly** = 0.5 × (sigma(10D call) + sigma(10D put)) minus sigma(ATM), capturing deeper tail pricing
- **Butterfly as a trade**: long BF = long 25D strangle + short ATM straddle; short BF = the reverse
- **Vega exposure**: a long butterfly is approximately vega neutral (long wing vega offset by short ATM vega) but has significant [[Volga]] exposure
- **P&L driver**: the position profits when realized moves are either very large or very small relative to ATM vol, and loses in the intermediate range

## Prerequisites
- [[ATM]]
- [[Delta]]
- [[Risk Reversal]]
- [[Vol Surface]]
- [[Implied Volatility]]

## Related concepts (learn next)
- [[Risk Reversal]]: captures skew (directional asymmetry) while butterfly captures smile curvature (kurtosis)
- [[Volga]]: the primary greek driving butterfly P&L, as BF is essentially a volga trade
- [[Strangle]]: the wing component of the butterfly structure
- [[Straddle]]: the body component (ATM) of the butterfly structure
- [[Vol Surface]]: fully specified by ATM, RR, and BF at each tenor
- [[Vanna]]: interacts with butterfly pricing through smile dynamics
- [[Gamma]]: butterfly structures have complex gamma profiles that shift with spot

## Common misconceptions
1. **"Butterfly is always a cheap trade."** While the net premium may be small, the position can bleed steadily from [[Theta]] if realized volatility is moderate. The payoff profile requires either very large or very small moves.
2. **"A higher butterfly means the market is scared."** A higher BF means tail options are relatively expensive, but this could reflect structural demand (e.g., barrier hedging in [[Barrier Option]] markets) rather than fear.
3. **"Butterfly and risk reversal are independent."** In practice, they interact: a large risk reversal with a small butterfly produces a heavily skewed smile, while a small RR with a large BF produces a symmetric but fat tailed distribution.

## Sources
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Castagna, Antonio. *FX Options and Smile Risk*.
- Reiswich, Dimitri and Wystup, Uwe. "FX Volatility Smile Construction," Wilmott Magazine, 2010.
