---
aliases: [risk reversal, RR, 25 delta risk reversal, 25D RR]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Risk Reversal

## Definition
A risk reversal (RR) is the difference in [[implied volatility]] between an out of the money call and an out of the money put at the same [[Delta]] level, most commonly 25 delta. In formula terms, 25D RR = 25D call vol minus 25D put vol. A positive RR means calls are more expensive than puts, indicating the market prices a higher probability of upside moves in the [[underlying]]. As a strategy, a risk reversal involves buying an OTM call and selling an OTM put (or vice versa), creating a position that is long skew. Risk reversals are the primary measure of directional asymmetry in the [[Vol Surface]] and are one of the 3 standard FX vol quotes alongside [[ATM]] vol and [[Butterfly]].

## Why it matters (commodities and FX)
The 25D RR is the market's consensus measure of directional skew. In FX, a strongly negative EUR/USD risk reversal (puts richer than calls) signals demand for EUR downside protection, often reflecting positioning or hedging flows. Commodity options on [[Brent Crude]] or [[Gold Futures]] typically show negative risk reversals (puts more expensive) because producers hedge by buying puts, creating structural demand for downside protection. Changes in RR often precede or coincide with spot moves, making them valuable signals. A widening RR before an event like an [[OPEC]] meeting or central bank decision reveals how the market is positioning for tail outcomes.

## Concrete example
**Success:** In January 2025, EUR/USD 1 month 25D RR sits at negative 0.35 vols (puts slightly richer). A trader believes the ECB will surprise hawkish and buys the RR: long 25D call (strike 1.0950) and short 25D put (strike 1.0650) for near zero net premium. EUR rallies from 1.0800 to 1.1000 after the ECB signals a pause. The call gains 50 pips intrinsic plus vol expansion; the put expires worthless. Net profit is approximately 48 pips after adjusting for the small initial cost.

**Failure:** A trader buys the 25D RR on USD/JPY (long upside call, short downside put) in late 2024, paying 0.15 vols for calls over puts. The BOJ surprises with a rate hike, and USD/JPY drops from 155 to 148. The short 25D put (strike 152) moves deeply in the money, costing 400 pips. The long call expires worthless. The RR position has unlimited downside from the short put leg, and the loss dwarfs the modest premium collected.

## Key mechanics and formulas
- **25D RR** = sigma(25D call) minus sigma(25D put)
- **Positive RR**: calls are richer, market skewed bullish on the underlying
- **Negative RR**: puts are richer, market skewed bearish or hedging downside
- **RR as a trade**: long RR = buy OTM call + sell OTM put (bullish skew bet); short RR = sell OTM call + buy OTM put (bearish skew bet)
- **Recovering strikes from RR and BF**: 25D call vol = [[ATM]] vol + 0.5 × RR + [[Butterfly]]; 25D put vol = ATM vol minus 0.5 × RR + Butterfly
- **10D RR**: same concept at the 10 delta level, capturing more extreme tail skew
- **RR in premium terms**: the net premium of the structure, which can be near zero when the RR is small

## Prerequisites
- [[Delta]]
- [[ATM]]
- [[Implied Volatility]]
- [[Vol Surface]]
- [[Vanilla Option]]

## Related concepts (learn next)
- [[Butterfly]]: the other vol surface parameter, measures wing richness (kurtosis) rather than skew
- [[Vol Surface]]: fully defined by ATM, RR, and BF across tenors in standard FX quoting
- [[Vanna]]: risk reversals have significant vanna exposure, linking delta to vol changes
- [[Straddle]]: a pure vol trade with no skew view, complementary to the risk reversal
- [[Strangle]]: a symmetric wings trade; contrasts with the asymmetric risk reversal
- [[Barrier Option]]: barrier hedging demand distorts the RR, especially in structured product heavy pairs
- [[Expiry Pinning]]: large RR positions near expiry create directional hedging flow

## Common misconceptions
1. **"A positive risk reversal means the market is bullish."** It means upside vol is more expensive than downside vol, which could reflect hedging demand (e.g., importers buying calls) rather than a directional consensus.
2. **"Risk reversals are free."** While the net premium can be near zero, the position has unlimited risk from the short put (or short call) leg. Margin requirements are significant.
3. **"RR only matters for options traders."** Spot and forward traders monitor RR as a sentiment and flow indicator. A rapid shift in RR often signals large institutional positioning changes that affect spot.

## Sources
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Malz, Allan. "Estimating the Probability Distribution of the Future Exchange Rate from Option Prices," *Journal of Derivatives*, 1997.
- Bloomberg Terminal. "FXFM: FX Forecasting Model" (risk reversal decomposition).
