---
aliases: [OTM, out of the money, out-of-the-money, deep OTM, deep out of the money]
tags:
  - "#quant"
  - "#fx"
date-added: "2026-06-18"
---

# OTM

## Definition

An option is out of the money (OTM) when exercising it right now would give you nothing: the right is worthless at current prices. A call is OTM when the [[underlying]] trades below the [[Strike Price]] (no point buying at the strike when the market is cheaper). A put is OTM when the underlying trades above the strike (no point selling at the strike when the market is higher). An OTM option has zero [[intrinsic value]]; its entire premium is [[time value]], the market's payment for the chance it moves into the money before expiry. The benchmark for "above" or "below" is conventionally the [[forward rate]], the same reference [[ATM]] uses, not spot. The further OTM, the cheaper the option and the lower its [[Delta]].

## Why it matters (commodities and FX)

OTM options are the cheap, convex, low probability instruments. You pay a small premium for a large payoff if a big move happens, which makes them the natural tool for tail hedges and lottery style directional bets. A commodity desk long physical [[Brent Crude]] buys OTM puts as crash protection; an airline buys OTM calls to cap fuel costs. Because their value is 100% time value, OTM options have the most violent [[Theta]] decay in percentage terms and are pure [[Implied Volatility]] plays: when vol rises, OTM premiums balloon even with spot unchanged. In FX, the demand for OTM downside vs OTM upside is precisely what the [[Risk Reversal]] measures, and the relative richness of far OTM wings is the [[Volatility Smile]]. Selling OTM options (collecting the premium and betting the move does not happen) is the core of most premium harvesting and [[Strangle]] strategies, with the well known asymmetry: small steady gains, occasional large losses.

## Concrete example

**Concrete:** Gold front month at $2,000. Trader buys 1 OTM $2,100 call (OTM by $100) for $12/oz. Intrinsic value = $0; the entire $12 is time value. Delta ≈ 18. Gold spikes to $2,180 on a geopolitical shock: the call is worth $80 intrinsic. P&L = $80 − $12 = +$68/oz, a 5.7x return on premium because the small Delta levered up as the option moved ITM. Fail case: gold drifts to $2,030 at expiry. The $2,100 call is still OTM, worth $0. P&L = −$12/oz, the full premium, even though gold rose $30. OTM buyers can be directionally right and still lose everything if the move is too small or too slow. Mirror trade: sell that same call for $12. If gold stays below $2,100 you keep the full $12; if it rips to $2,180 you lose $68 against $12 collected.

**Simplified:** OTM means the option has no exercise value yet, just a chance of getting there. A call is OTM when price is below the strike; a put when price is above. OTM options are cheap and convex: small premium, big payoff if a large move happens, total loss if it does not. Buying them is a leveraged bet on a move; selling them is collecting premium against a move that probably will not come.

## Key mechanics and formulas

- **Call**: OTM when forward < strike. Intrinsic value = 0.
- **Put**: OTM when forward > strike. Intrinsic value = 0.
- **Option premium** = time value only. There is no intrinsic component to fall back on.
- **Delta**: OTM call delta runs 0 to 50; deep OTM approaches 0. OTM put delta runs 0 to −50. Delta approximates the probability of finishing ITM.
- **Theta**: largest as a fraction of premium for OTM, accelerating into expiry as the chance of crossing the strike collapses.
- **Vega and convexity**: OTM premiums are highly sensitive to [[Implied Volatility]]; a vol spike can multiply an OTM option's value with no spot move.
- **Moneyness ratio** = forward / strike (calls) or strike / forward (puts). Below 1 means OTM.

## Prerequisites
- [[Strike Price]]
- [[intrinsic value]]
- [[time value]]
- [[Vanilla Option]]
- [[Delta]]
- [[forward rate]]

## Related concepts (learn next)
- [[ATM]]: the boundary OTM options must cross to gain intrinsic value.
- [[ITM]]: the mirror case, real exercise value and high delta.
- [[Moneyness]]: the umbrella concept spanning ITM, ATM, and OTM.
- [[time value]]: the entirety of an OTM option's premium.
- [[Theta]]: bites hardest on OTM options as expiry nears.
- [[Volatility Smile]]: the relative richness of far OTM wings vs ATM.
- [[Risk Reversal]]: the price of OTM downside vs OTM upside.
- [[Strangle]]: a strategy built from two OTM legs.

## Common misconceptions

**"OTM options are cheap, so they are good value."** Cheap in dollars, often expensive in probability. Most expire worthless. The low price reflects a low chance of payoff, not a bargain.

**"If the market moves my way, my OTM option profits."** Only if it moves far enough, fast enough, to cross the strike before expiry. Being directionally right by a small amount still loses the full premium.

**"Selling OTM options is low risk because they usually expire worthless."** The high win rate hides the tail. The occasional move that blows through your strike can lose multiples of all the premium collected. Short OTM is short [[Volatility]] with a fat tail.

## Sources
- Hull, John. *Options, Futures, and Other Derivatives*, 10th ed., chapter on properties of options.
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- Taleb, Nassim. *Dynamic Hedging*, on the behavior of out of the money options.
- CME Group. "Options on Futures: Moneyness and Exercise."
