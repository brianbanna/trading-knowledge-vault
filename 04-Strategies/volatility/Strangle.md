---
aliases: [strangle, long strangle, OTM strangle]
tags:
  - "#fx"
  - "#quant"
date-added: "2026-03-20"
---

# Strangle

## Definition
A strangle is an options strategy that combines a long out of the money (OTM) [[call option]] and a long OTM [[put option]] with different [[strike price]]s but the same [[expiry]]. The standard FX strangle uses 25 [[Delta]] strikes: a 25D call above spot and a 25D put below spot. Because both legs are OTM, the strangle costs less [[premium]] than a [[Straddle]] but requires a larger move in the [[underlying]] to become profitable. Like the straddle, it is a non directional [[Volatility]] bet, but it is more leveraged to tail moves. In FX vol quoting, the strangle premium (combined with the [[ATM]] vol) defines the [[Butterfly]] spread.

## Why it matters (commodities and FX)
Strangles are the go to pre event trade in FX and commodity options. Before NFP, ECB decisions, [[OPEC]] meetings, or crop reports, traders buy strangles because they offer exposure to a large move at a fraction of the [[Straddle]] cost. The 25D strangle is also the building block for the [[Butterfly]] quote: BF = 0.5 × (25D call vol + 25D put vol) minus [[ATM]] vol, which is effectively the strangle vol premium over ATM. Systematic strangle sellers in FX (often structured product desks and yield enhancement funds) provide a persistent supply of wing vol, creating opportunities when their selling becomes excessive and wings cheapen below fair value.

## Concrete example
**Success:** GBP/USD 1 week 25D strangle costs 28 pips ahead of a UK election. Strikes are 1.2950 (call) and 1.2650 (put), with spot at 1.2800. A hung parliament result sends GBP/USD to 1.2500 overnight. The put leg has intrinsic value of 150 pips. Net profit is 150 minus 28 = 122 pips. The call expires worthless, but the put leg more than compensates.

**Failure:** A trader buys the 1 month EUR/USD 25D strangle at 18 pips ahead of an ECB meeting. ECB delivers exactly as expected, and spot oscillates between 1.0750 and 1.0850 for the entire month. Both legs expire OTM. The full 18 pip premium is lost. The strangle needed a move beyond 1.0950 or below 1.0650 to profit, but realized range was only 100 pips.

## Key mechanics and formulas
- **Strangle payoff at expiry** = max(spot minus call strike, 0) + max(put strike minus spot, 0) minus total premium
- **Upper breakeven** = call strike + total premium
- **Lower breakeven** = put strike minus total premium
- **25D strangle vol** = [[ATM]] vol + [[Butterfly]], i.e., the average of 25D call and 25D put implied vols
- **Cost relative to straddle**: typically 30% to 50% of the ATM straddle premium, depending on the butterfly level
- **Greeks**: net delta is approximately 0 at inception; [[Gamma]] and [[Vega]] are lower than the straddle but more convex in the tails; [[Theta]] is lower in absolute terms but higher per unit of vega
- **Strangle vega** peaks away from spot, at the 2 strike levels, unlike the straddle which peaks at ATM

## Prerequisites
- [[Vanilla Option]]
- [[Delta]]
- [[ATM]]
- [[Implied Volatility]]
- [[Butterfly]]

## Related concepts (learn next)
- [[Straddle]]: the ATM equivalent; more expensive but profits from smaller moves
- [[Butterfly]]: defined as the strangle vol premium over ATM, making it a direct measure of strangle richness
- [[Risk Reversal]]: an asymmetric structure (long one wing, short the other) vs. the symmetric strangle
- [[Gamma]]: strangle gamma is lower than straddle gamma near ATM but higher in the tails
- [[Volga]]: strangles have significant volga exposure because OTM options are convex in vol
- [[Vega]]: strangle vega is split across 2 strike points, creating a bimodal sensitivity profile
- [[Barrier Option]]: barrier hedging demand drives OTM option pricing and therefore strangle costs

## Common misconceptions
1. **"Strangles are safer than straddles because they cost less."** The lower cost reflects lower probability of profit. Strangles require larger moves to break even and expire worthless more often than straddles.
2. **"Selling strangles is a high probability trade."** While strangles expire worthless frequently, the losses when they do not are disproportionately large. One tail event can erase months of premium collection.
3. **"The strangle is just a wider straddle."** The risk profiles differ significantly. A strangle has a wider breakeven range but is more leveraged to tail events. Its [[Volga]] exposure makes it sensitive to changes in the smile shape, not just the overall vol level.

## Sources
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed.
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
