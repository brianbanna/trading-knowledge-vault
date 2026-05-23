---
aliases: [ATM, at the money, at-the-money]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# ATM

## Definition
An ATM option has its [[strike price]] equal to the current [[forward rate]] of the [[underlying]] at expiry. In FX, ATM is the strike where call [[Delta]] equals negative put delta (the "delta neutral straddle," DNS). At this strike, the option has maximum [[time value]] and zero intrinsic value. ATM [[implied volatility]] is the headline number on every [[Vol Surface]] and anchors the entire term structure. When traders say "vol is 8.5," they mean ATM IV for a given tenor.

## Why it matters (commodities and FX)
ATM IV is the baseline from which [[Risk Reversal]] and [[Butterfly]] adjustments build the full [[Vol Surface]]. In commodities, ATM options on [[Brent Crude]] or [[Gold Futures]] are the most liquid strikes and the natural vehicle for pure [[Volatility]] views. ATM has the highest [[Gamma]] and [[Theta]] per unit of [[premium]], making it the most efficient instrument for trading [[Realized Volatility]] vs [[implied volatility]]. Central bank meetings, NFP, and OPEC announcements all spike ATM vols into the event and collapse them after.

## Concrete example
**Concrete:** EURUSD spot 1.0850, 1M forward 1.0860. 1M ATM strike set at 1.0860. ATM IV 7.8%. Trader buys the ATM [[Straddle]] for 120 pips. ECB surprises with a 50 bp cut, spot moves to 1.1050. Call leg pays 190 pips intrinsic. Net: +70 pips. Reverse trade: trader sells 1W USDJPY ATM straddle at 9.2% for 55 pips. BOJ adjusts YCC, USDJPY drops 400 pips in 2 days. Put leg alone costs 400 pips. Net: -345 pips. Short ATM carries unbounded risk both ways.

**Simplified:** ATM is the strike where the option is balanced between a call and a put. It has no intrinsic value, only time value, and it reacts most sharply to volatility. Buying ATM is a clean bet on a big move in either direction. Selling ATM is a clean bet on a quiet market. Both have asymmetric risk: the buyer pays a known premium for unlimited upside; the seller collects a known premium for unlimited downside.

## Key mechanics and formulas
- **ATM strike (FX DNS convention)** = forward × e^(0.5 × vol² × time), ≈ forward for short tenors
- **ATM Delta** ≈ 50 (calls at +50D, puts at −50D), exact value depends on premium currency adjustment
- **Maximum time value**: at ATM, time value = total premium (intrinsic = 0)
- **Gamma at ATM** = N'(d1) / (spot × vol × sqrt(time)), peaks when d1 = 0
- **Theta at ATM** = −spot × N'(d1) × vol / (2 × sqrt(time)), most negative across all strikes
- **ATM vol interpolation**: midpoint of the [[Vol Surface]], from which [[Risk Reversal]] and [[Butterfly]] derive 25D and 10D vols

## Prerequisites
- [[Implied Volatility]]
- [[Forward Curve]]
- [[Delta]]
- [[Vanilla Option]]
- [[Strike Price]]

## Related concepts (learn next)
- [[Risk Reversal]]: skew relative to ATM, quoted as 25D call vol minus 25D put vol
- [[Butterfly]]: wing richness relative to ATM vol
- [[Straddle]]: the standard ATM volatility trade
- [[Vol Surface]]: ATM vol forms the backbone across tenors
- [[Gamma]]: peaks at ATM, the highest convexity strike
- [[Theta]]: most negative at ATM, the cost of maximum gamma
- [[Vega]]: also peaks near ATM for a given expiry

## Common misconceptions

**"ATM means strike equals spot."** In FX, ATM references the [[forward rate]], not spot. For high carry pairs like USDMXN, the ATM strike differs from spot due to the rate differential.

**"ATM delta is always exactly 50."** Depends on premium currency convention (domestic vs foreign) and whether delta is spot or forward. ATM DNS delta ranges 48 to 52.

**"ATM vol is stable."** ATM vol moves with sentiment, event risk, and option supply/demand. A 1 vol move in EURUSD 1M ATM shifts straddle premiums by 15 to 20 pips.

## Sources
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Reiswich, Dimitri and Wystup, Uwe. "FX Volatility Smile Construction," Wilmott Magazine, 2010.
- Bloomberg Terminal. "OVML: FX Option Valuation."
