---
aliases: [strangle, long strangle, OTM strangle]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Strangle

## Definition
A strangle combines a long out of the money (OTM) [[call option]] and a long OTM [[put option]] at different [[strike price]]s but the same [[expiry]]. The standard FX strangle uses 25 [[Delta]] strikes: a 25D call above spot and a 25D put below spot. Both legs OTM: the strangle costs less [[premium]] than a [[Straddle]] but requires a larger move to profit. Like the straddle, a non directional [[Volatility]] bet, but more leveraged to tail moves. In FX vol quoting, the strangle premium (with [[ATM]] vol) defines the [[Butterfly]] spread.

## Why it matters (commodities and FX)
Strangles are the go to pre event trade in FX and commodity options. Before NFP, ECB decisions, [[OPEC]] meetings, or crop reports, traders buy strangles for exposure to a large move at a fraction of the [[Straddle]] cost. The 25D strangle is also the building block for the [[Butterfly]] quote: BF = 0.5 × (25D call vol + 25D put vol) minus [[ATM]] vol, the strangle vol premium over ATM. Systematic strangle sellers in FX (structured product desks, yield enhancement funds) supply persistent wing vol, creating opportunities when their selling becomes excessive and wings cheapen below fair value.

## Concrete example
**Concrete:** GBP/USD 1 week 25D strangle costs 28 pips ahead of a UK election. Strikes 1.2950 (call) and 1.2650 (put), spot at 1.2800. Hung parliament sends GBP/USD to 1.2500 overnight. Put leg has 150 pips intrinsic. Net profit 150 - 28 = 122 pips. Call expires worthless, put more than compensates.

**Simplified:** Buy a call above spot and a put below spot. Both OTM, so cheaper than a straddle. You profit only if the move is big enough to push one of them deep in the money beyond the premium paid. Lose if the underlying stays in the range between the 2 strikes. Used to bet on a big move when direction is unclear.

## Key mechanics and formulas
- **Strangle payoff at expiry** = max(spot minus call strike, 0) + max(put strike minus spot, 0) minus total premium
- **Upper breakeven** = call strike + total premium
- **Lower breakeven** = put strike minus total premium
- **25D strangle vol** = [[ATM]] vol + [[Butterfly]], the average of 25D call and 25D put implied vols
- **Cost relative to straddle**: 30% to 50% of the ATM straddle premium, depending on butterfly level
- **Greeks**: net delta ~0 at inception; [[Gamma]] and [[Vega]] lower than straddle but more convex in the tails; [[Theta]] lower in absolute terms but higher per unit of vega
- **Strangle vega** peaks away from spot at the 2 strike levels, unlike the straddle which peaks at ATM

## Prerequisites
- [[Vanilla Option]]
- [[Delta]]
- [[ATM]]
- [[Implied Volatility]]
- [[Butterfly]]

## Related concepts (learn next)
- [[Straddle]]: the ATM equivalent; more expensive but profits from smaller moves
- [[Butterfly]]: defined as the strangle vol premium over ATM, a direct measure of strangle richness
- [[Risk Reversal]]: an asymmetric structure (long one wing, short the other) vs the symmetric strangle
- [[Gamma]]: strangle gamma is lower than straddle gamma near ATM but higher in the tails
- [[Volga]]: strangles have significant volga exposure because OTM options are convex in vol
- [[Vega]]: strangle vega is split across 2 strike points, creating a bimodal sensitivity profile
- [[Barrier Option]]: barrier hedging demand drives OTM option pricing and therefore strangle costs

## Common misconceptions
1. **"Strangles are safer than straddles because they cost less."** Lower cost reflects lower probability of profit. Strangles require larger moves to break even and expire worthless more often than straddles.
2. **"Selling strangles is a high probability trade."** Strangles expire worthless often, but losses when they do not are disproportionately large. One tail event erases months of premium collection.
3. **"The strangle is just a wider straddle."** Risk profiles differ. A strangle has a wider breakeven range but is more leveraged to tail events. Its [[Volga]] exposure makes it sensitive to changes in the smile shape, not just the overall vol level.

## Sources
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
