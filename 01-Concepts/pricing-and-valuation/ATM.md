---
aliases: [ATM, at the money, at-the-money]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# ATM

## Definition
At the money (ATM) describes an option whose [[strike price]] equals the current [[forward rate]] of the [[underlying]] at the option's [[expiry]]. In FX, ATM is specifically defined as the strike where the [[Delta]] of the call equals the negative [[Delta]] of the put (often called "delta neutral straddle" or DNS). This is the point where the option has maximum [[time value]] and zero intrinsic value. ATM [[implied volatility]] is the single most watched number on any [[Vol Surface]] because it anchors the entire volatility term structure. When traders say "vol is 8.5," they almost always mean the ATM implied vol for a specific tenor.

## Why it matters (commodities and FX)
The ATM implied vol is the headline quote in every FX options market and serves as the baseline from which [[Risk Reversal]] and [[Butterfly]] adjustments build the full [[Vol Surface]]. In commodities, ATM options on [[Brent Crude]] or [[Gold Futures]] are the most liquid strikes, making them the natural vehicle for expressing pure [[Volatility]] views. ATM options have the highest [[Gamma]] and [[Theta]] per unit of [[premium]], so they are the most efficient instruments for trading [[Realized Volatility]] versus [[implied volatility]]. Central bank meetings, NFP releases, and OPEC announcements all cause ATM vols to spike in anticipation and collapse afterward.

## Concrete example
**Success:** EUR/USD spot is 1.0850 and the 1 month forward is 1.0860. The 1 month ATM strike is set at 1.0860. ATM implied vol is quoted at 7.8%. A trader buys the ATM [[Straddle]] (call + put) for a combined premium of 120 pips. Over the next month, the ECB surprises with a 50 bp cut, and spot moves to 1.1050. The call leg pays 190 pips intrinsic; net profit is 190 minus 120 = 70 pips.

**Failure:** A trader sells the 1 week ATM straddle on USD/JPY at 9.2% implied vol, collecting 55 pips. The BOJ unexpectedly adjusts yield curve control, and USD/JPY drops 400 pips in 2 days. The put leg alone costs 400 pips to cover, producing a net loss of 345 pips. ATM short positions carry unlimited risk in both directions.

## Key mechanics and formulas
- **ATM strike (FX DNS convention)** = forward × e^(0.5 × vol² × time), which simplifies to approximately the forward rate for short tenors
- **ATM Delta** = approximately 50 (calls at +50D, puts at negative 50D), though exact values depend on premium currency adjustment
- **Maximum time value**: at the ATM strike, time value = total premium (intrinsic value = 0)
- **Gamma at ATM** = N'(d1) / (spot × vol × sqrt(time)), which peaks when d1 = 0 (i.e., at ATM)
- **Theta at ATM** = (negative spot × N'(d1) × vol) / (2 × sqrt(time)), the most negative value across all strikes
- **ATM vol interpolation**: the midpoint of the [[Vol Surface]], from which [[Risk Reversal]] and [[Butterfly]] adjustments derive 25D and 10D vols

## Prerequisites
- [[Implied Volatility]]
- [[Forward Curve]]
- [[Delta]]
- [[Vanilla Option]]
- [[Strike Price]]

## Related concepts (learn next)
- [[Risk Reversal]]: measures skew relative to ATM, quoted as 25D call vol minus 25D put vol
- [[Butterfly]]: measures wing richness relative to ATM vol
- [[Straddle]]: the standard ATM volatility trade, long call plus long put
- [[Vol Surface]]: ATM vol forms the backbone across tenors
- [[Gamma]]: peaks at ATM, making it the highest convexity strike
- [[Theta]]: most negative at ATM, the cost of maximum gamma exposure
- [[Vega]]: also peaks near ATM for a given expiry

## Common misconceptions
1. **"ATM means strike equals spot."** In FX, ATM is defined relative to the [[forward rate]], not spot. For high carry pairs like USD/MXN, the ATM strike can differ significantly from spot due to the interest rate differential.
2. **"ATM delta is always exactly 50."** The precise ATM delta depends on the premium currency convention (domestic vs. foreign) and whether the delta is spot delta or forward delta. In practice, ATM DNS delta can range from 48 to 52.
3. **"ATM vol is stable."** ATM vol moves constantly with market sentiment, event risk, and supply/demand for options. A 1 vol point move in EUR/USD 1 month ATM can shift straddle premiums by 15 to 20 pips.

## Sources
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Clark, Iain. *Foreign Exchange Option Pricing: A Practitioner's Guide*.
- Reiswich, Dimitri and Wystup, Uwe. "FX Volatility Smile Construction," Wilmott Magazine, 2010.
- Bloomberg Terminal. "OVML: FX Option Valuation."
