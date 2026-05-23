---
aliases: [risk reversal, RR, 25 delta risk reversal, 25D RR]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Risk Reversal

## Definition
A risk reversal (RR) is the difference in [[implied volatility]] between an OTM call and an OTM put at the same [[Delta]], most commonly 25 delta. Formula: 25D RR = 25D call vol − 25D put vol. Positive RR means calls are richer than puts, indicating market priced upside skew in the [[underlying]]. As a position, an RR is long an OTM call and short an OTM put (or reverse), creating a long skew payoff. RRs are the primary directional skew measure on the [[Vol Surface]] and 1 of the 3 standard FX vol quotes alongside [[ATM]] and [[Butterfly]].

## Why it matters (commodities and FX)
The 25D RR is the consensus measure of directional skew. Strongly negative EUR/USD RR (puts richer) signals demand for EUR downside protection, often reflecting positioning or hedging. Commodity options on [[Brent Crude]] or [[Gold Futures]] show structurally negative RRs because producers buy puts, creating standing demand for downside. Changes in RR often precede or coincide with spot moves. A widening RR before an [[OPEC]] meeting or central bank decision reveals how the market is positioning for tail outcomes.

## Concrete example

**Concrete:** January 2025. EUR/USD 1 month 25D RR sits at −0.35 vols (puts slightly richer). Trader thinks ECB will surprise hawkish, buys the RR: long 25D call (1.0950) and short 25D put (1.0650) for near zero net premium. ECB signals a pause, EUR rallies from 1.0800 to 1.1000. Call gains 50 pips intrinsic plus vol expansion; put expires worthless. Net 48 pips after the small initial cost. Failure case: trader buys USD/JPY 25D RR (long upside, short downside) in late 2024 for 0.15 vols. BOJ hikes, USD/JPY drops 155 to 148, short put at 152 goes deeply ITM, costs 400 pips. Long call expires worthless. RR has unlimited downside from the short leg.

**Simplified:** Out of the money calls and puts cost different amounts of implied vol. The risk reversal is just that gap. Positive = calls more expensive than puts = market is paying up for upside. Negative = puts more expensive = market is paying up for downside protection. As a trade, you buy 1 wing and sell the other, getting a near zero cost directional bet with unlimited risk from the sold leg.

## Key mechanics and formulas
- **25D RR** = σ(25D call) − σ(25D put)
- **Positive RR**: calls richer, market skewed bullish
- **Negative RR**: puts richer, market skewed bearish or hedging downside
- **RR as trade**: long RR = buy OTM call + sell OTM put (bullish skew bet); short RR = sell OTM call + buy OTM put
- **Strike recovery**: 25D call vol = [[ATM]] vol + 0.5 × RR + [[Butterfly]]; 25D put vol = ATM vol − 0.5 × RR + Butterfly
- **10D RR**: same at the 10 delta level, captures extreme tail skew
- **RR in premium**: net structure premium, often near zero for small RR

## Prerequisites
- [[Delta]]
- [[ATM]]
- [[Implied Volatility]]
- [[Vol Surface]]
- [[Vanilla Option]]

## Related concepts (learn next)
- [[Butterfly]]: the other vol surface parameter, measures wing richness (kurtosis) rather than skew
- [[Vol Surface]]: defined by ATM, RR, and BF across tenors in standard FX quoting
- [[Vanna]]: RRs have significant vanna exposure, linking delta to vol changes
- [[Straddle]]: pure vol trade with no skew view
- [[Strangle]]: symmetric wings trade, contrasts with asymmetric RR
- [[Barrier Option]]: barrier hedging demand distorts RR in structured product heavy pairs
- [[Expiry Pinning]]: large RR positions near expiry create directional hedging flow

## Common misconceptions
1. **"Positive RR means bullish market."** It means upside vol is more expensive, which can reflect hedging demand (importers buying calls) rather than directional consensus.
2. **"Risk reversals are free."** Net premium can be near zero, but short put (or short call) leg has unlimited risk and significant margin.
3. **"RR only matters for options traders."** Spot and forward traders watch RR as a sentiment and flow indicator. Rapid RR shifts signal institutional positioning changes that move spot.
4. **"25D is the only RR that matters."** 10D RR captures tail skew that 25D misses, especially around events.

## Sources
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Malz, Allan. "Estimating the Probability Distribution of the Future Exchange Rate from Option Prices," *Journal of Derivatives*, 1997.
- Bloomberg Terminal. "FXFM: FX Forecasting Model" (risk reversal decomposition).
