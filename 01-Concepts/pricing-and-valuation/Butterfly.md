---
aliases: [butterfly, butterfly spread, 25 delta butterfly, 25D BF]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Butterfly

## Definition
The butterfly (BF) in FX options is the average of 25 delta call and 25 delta put [[implied volatility]] minus [[ATM]] IV. It measures how much more expensive the wings (OTM options) are relative to the ATM center of the [[Vol Surface]]. A higher BF means fatter tails in the implied distribution: the market prices higher probability of large moves either way. As a trade, long butterfly = long the 25D [[Strangle]] + short the [[ATM]] [[Straddle]], isolating exposure to smile curvature. BF is 1 of 3 standard FX vol quotes, with [[ATM]] vol and [[Risk Reversal]].

## Why it matters (commodities and FX)
The butterfly prices tail risk and kurtosis. In FX, BFs widen ahead of central bank decisions, elections, and referendums as the market assigns higher probability to extreme outcomes. A persistently elevated BF on USDTRY or USDBRL signals ongoing structural tail risk from EM crises. In commodities, BFs on [[Brent Crude]] widen ahead of [[OPEC]] meetings and geopolitical escalations. Monitoring BF changes tells you whether tail insurance is cheap or expensive vs the realized frequency of large moves.

## Concrete example
**Concrete:** EURUSD 1M 25D butterfly at 0.25 vols, historically low ahead of the French presidential election. Trader buys the BF (long 25D strangle, short ATM straddle) for 5 pips debit. Surprise result, EURUSD gaps 300 pips. The 25D strangle explodes; the short straddle loses less. BF jumps to 0.85, position gains 35 pips. Reverse case: trader buys 25D BF on GBPUSD ahead of BOE at 0.55 vols. BOE delivers in line, vol collapses evenly, smile flattens, BF drops to 0.30. Long strangle decays faster than short straddle recovers. Loss: 12 pips from [[Theta]] and vol compression.

**Simplified:** Buying a butterfly is buying the wings and selling the middle of the vol surface. You win if the market either does almost nothing (short straddle pays) or makes a huge move (long strangle pays). You lose in the boring middle, where moderate moves hurt the long strangle without saving the short straddle. It is a bet on the shape of the distribution, not the direction.

## Key mechanics and formulas
- **25D Butterfly** = 0.5 × (σ(25D call) + σ(25D put)) − σ(ATM)
- **Always positive**: OTM options carry tail risk premium, BF sits above zero
- **Recovering wing vols**: σ(25D call) = ATM + 0.5 × [[Risk Reversal]] + BF; σ(25D put) = ATM − 0.5 × RR + BF
- **10D Butterfly** = 0.5 × (σ(10D call) + σ(10D put)) − σ(ATM), captures deeper tail pricing
- **As a trade**: long BF = long 25D strangle + short ATM straddle; short BF = reverse
- **Vega exposure**: long BF is approximately vega neutral (wing vega offsets ATM vega) but has significant [[Volga]] exposure
- **P&L driver**: profits on very large or very small realized moves vs ATM vol, loses in the middle range

## Prerequisites
- [[ATM]]
- [[Delta]]
- [[Risk Reversal]]
- [[Vol Surface]]
- [[Implied Volatility]]

## Related concepts (learn next)
- [[Risk Reversal]]: captures skew (directional asymmetry) while BF captures curvature (kurtosis)
- [[Volga]]: primary greek driving BF P&L; BF is essentially a volga trade
- [[Strangle]]: wing component of the BF structure
- [[Straddle]]: body (ATM) component
- [[Vol Surface]]: fully specified by ATM, RR, and BF at each tenor
- [[Vanna]]: interacts with BF through smile dynamics
- [[Gamma]]: BF structures have complex gamma profiles that shift with spot

## Common misconceptions
**"Butterfly is always a cheap trade."** Net premium is small but the position bleeds from [[Theta]] in moderate realized vol. Payoff needs very large or very small moves.

**"A higher butterfly means the market is scared."** Higher BF means tail options are relatively expensive, but this reflects structural demand (barrier hedging in [[Barrier Option]] markets) as much as fear.

**"Butterfly and risk reversal are independent."** They interact. Large RR with small BF = heavily skewed smile. Small RR with large BF = symmetric fat tails.

## Sources
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Castagna, Antonio. *FX Options and Smile Risk*.
- Reiswich, Dimitri and Wystup, Uwe. "FX Volatility Smile Construction," Wilmott Magazine, 2010.
