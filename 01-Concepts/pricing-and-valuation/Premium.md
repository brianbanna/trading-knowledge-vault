---
aliases: [Option Price, Option Premium]
tags:
  - "#quant"
date-added: "2026-06-18"
---

# Premium

## Definition
The premium is the price the buyer pays the seller to enter an option contract. Plain English: it is the cost of the right the option gives you, paid upfront and kept by the seller no matter what happens next. The premium equals [[Intrinsic Value]] plus [[Time Value]]: the part that would pay off if exercised now, plus the part that reflects the chance the option gains more value before [[Expiration]]. For the buyer, the premium is the maximum possible loss; for the seller, it is the maximum possible gain. It is quoted per unit of the underlying, such as cents per pound, dollars per barrel, or pips in FX, and is multiplied by contract size to get the cash amount.

## Why it matters (commodities and FX)
Every option trade starts with a cash outlay or inflow equal to the premium, so it sets the budget and the risk on day 1. A commodities trader buying downside protection knows the premium is the most they can lose, which makes options attractive versus a futures position that can lose far more. Sellers of premium, such as producers writing covered calls, treat it as income but accept open ended risk. Because premium decays through [[Theta]] and inflates with [[Implied Volatility]], timing entries around volatility and time to expiry is central to whether the cost is worth paying.

## Concrete example
**Concrete:** [[Gold Futures]] front month trades at $2,300/oz. You buy 1 [[Call Option]] with a $2,350 [[Strike Price]] for a premium of $18.00/oz. A COMEX gold option covers 100 ounces, so you pay $1,800 cash. The premium is entirely [[Time Value]] here, since the $2,350 strike is above the $2,300 price and there is zero [[Intrinsic Value]].
- Win case: at expiry gold settles at $2,400. Intrinsic value is $50/oz ($2,400 minus $2,350), worth $5,000. Subtract the $1,800 premium and net profit is $3,200. The option finished ITM net of premium because it cleared the $2,368 breakeven (strike plus premium).
- Fail case: at expiry gold settles at $2,330. The $2,350 strike is above the market, so the call expires worthless. You lose the full $1,800 premium and nothing more. The seller keeps the entire $1,800 as their maximum gain.

**Simplified:** The premium is what you pay to own the option, and it is the most a buyer can lose. It is made of intrinsic value plus time value. If the option expires worthless, the whole premium is gone.

## Key mechanics and formulas
- Premium = [[Intrinsic Value]] + [[Time Value]].
- Intrinsic value (call) = max(0, S - K); intrinsic value (put) = max(0, K - S), where S is the underlying price and K is the [[Strike Price]].
- Time value = Premium - Intrinsic value. It is always positive before expiry and decays to zero at [[Expiration]].
- Cash cost = quoted premium x contract size (for example $18.00/oz x 100 oz = $1,800).
- Breakeven (long call) = K + premium. Breakeven (long put) = K - premium.
- Premium rises with higher [[Implied Volatility]] and more time to expiry; it falls each day through [[Theta]] decay.

## Prerequisites
- [[Option]]
- [[Strike Price]]
- [[Intrinsic Value]]
- [[Time Value]]

## Related concepts (learn next)
- [[Intrinsic Value]] because it is the first of the two components that make up every premium.
- [[Time Value]] because it is the second component and the part that erodes over time.
- [[Theta]] because it measures how fast time value, and therefore premium, decays each day.
- [[Implied Volatility]] because it is the main input that inflates or deflates the premium for a given strike.
- [[Moneyness]] because where the strike sits versus spot dictates how much premium is intrinsic versus time value.
- [[Vega]] because it quantifies how much premium changes when implied volatility shifts.
- [[Payoff Diagram]] because the premium sets the vertical offset and breakeven point on the payoff curve.

## Common misconceptions
- "The premium is what I make if the trade works." Wrong: for a buyer the premium is the cost and the maximum loss, not the profit. Profit comes from intrinsic value beyond the premium paid.
- "A cheap premium means a good trade." Wrong: low premium usually means the strike is far OTM with low probability of paying off, so cheapness reflects low odds, not value.
- "If the option finishes ITM, I made money." Wrong: you only profit once intrinsic value exceeds the premium paid. An option can expire slightly ITM and still leave you with a net loss.
- "Premium is fixed once quoted." Wrong: the premium of a live option moves continuously with the underlying, [[Implied Volatility]], and time decay until expiry.

## Sources
- CME Group, "Options on Futures" and "Understanding Option Pricing" guides.
- John C. Hull, "Options, Futures, and Other Derivatives," option valuation chapters.
- ICE, FX and energy options specifications and pricing notes.
