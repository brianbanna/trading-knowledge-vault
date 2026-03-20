---
aliases: [vega, vol sensitivity, volatility exposure]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Vega

## Definition
Vega measures the sensitivity of an option's price to a 1 percentage point change in [[implied volatility]]. An option with a vega of 0.05 gains 0.05 in value (e.g., 5 pips in FX) for each 1 vol point increase in implied vol. Vega is not a Greek letter (there is no Greek letter vega), but it is universally included in the [[Greeks]] toolkit. All long option positions are long vega, meaning they benefit from rising implied vol, while all short option positions are short vega. Vega is the primary risk measure for [[Volatility]] as a tradeable asset class, distinct from [[Delta]] (directional risk) and [[Gamma]] (convexity risk). Vega exposure peaks near [[ATM]] and declines for deep in or out of the money options.

## Why it matters (commodities and FX)
Vega is the dominant risk factor for any options book. An FX options desk running EUR 500 million notional in EUR/USD options might carry 50,000 EUR of vega, meaning a 1 vol point move in implied vol swings P&L by EUR 50,000. In commodities, [[Brent Crude]] vega exposure determines how much a desk profits or loses from the routine vol expansions around [[OPEC]] meetings and [[EIA Report]] releases. Managing vega across tenors (the "vega term structure") is a core skill: a book can be vega flat in aggregate but massively long short dated vega and short long dated vega, creating exposure to term structure shifts. Most options blowups involve uncontrolled vega exposure in a vol spike.

## Concrete example
**Success:** A trader is long EUR 200 million notional of EUR/USD 3 month ATM options with a vega of 0.08 per million notional. Total vega is EUR 16,000. Implied vol rises from 7.5% to 9.0% (1.5 vol points) after a surprise tariff announcement. Vega P&L = 16,000 × 1.5 = EUR 24,000 profit, before any delta or gamma effects.

**Failure:** A commodity desk sells 3 month [[Brent Crude]] straddles to collect premium, accumulating a short vega position of USD 80,000 per vol point. Geopolitical tensions in the Middle East push 3 month Brent implied vol from 28% to 38% in 1 week (10 vol point move). Vega loss = 80,000 × 10 = USD 800,000. The premium collected over the prior 2 months was only USD 250,000. Net loss is USD 550,000.

## Key mechanics and formulas
- **Vega** = spot × e^(negative foreign rate × time) × sqrt(time) × N'(d1), where N'(d1) is the standard normal density at d1
- **Vega per 1 vol point** = vega / 100 (since vol is in percentage terms)
- **Vega peaks at ATM**: when d1 is approximately 0, N'(d1) is at its maximum
- **Vega scales with sqrt(time)**: longer dated options have more vega, approximately proportional to the square root of time to expiry
- **Weighted vega**: desks often weight vega by 1 / sqrt(time) to normalize across tenors, making 1 month and 1 year vega comparable
- **Vega P&L** = vega × change in implied vol (in vol points)
- **Put call parity for vega**: calls and puts at the same strike and expiry have identical vega

## Prerequisites
- [[Implied Volatility]]
- [[Vanilla Option]]
- [[ATM]]
- [[Vol Surface]]
- [[Greeks]]

## Related concepts (learn next)
- [[Volga]]: the sensitivity of vega to changes in vol, a second order effect critical for OTM options
- [[Gamma]]: convexity in spot dimension, analogous to volga in vol dimension
- [[Theta]]: long vega positions pay theta; the vega/theta tradeoff is the core options dilemma
- [[Realized Volatility]]: vega captures sensitivity to implied vol; realized vol drives delta hedged P&L through gamma
- [[Vanna]]: cross sensitivity between delta and vol; links vega risk to directional risk
- [[Vol Surface]]: vega exposure is distributed across the surface; managing it requires monitoring all tenors and strikes
- [[Straddle]]: the maximum vega structure at any given tenor, used for pure vol bets

## Common misconceptions
1. **"Vega is the same as volatility risk."** Vega captures sensitivity to implied vol changes, but volatility risk also includes [[Realized Volatility]] exposure (captured by [[Gamma]]) and smile dynamics (captured by [[Vanna]] and [[Volga]]).
2. **"Long vega is always a good hedge."** Long vega protects against vol spikes but bleeds [[Theta]] daily. If vol does not rise, the position is a consistent loser.
3. **"Vega is constant."** Vega itself changes with spot (via [[Vanna]]), with vol (via [[Volga]]), and with time. These second order effects can be larger than the first order vega for deep OTM options.
4. **"Total book vega of zero means no vol risk."** A book can be vega neutral in aggregate but carry massive vega exposure in specific tenors or strikes, leading to large P&L from term structure or smile moves.

## Sources
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Gatheral, Jim. *The Volatility Surface: A Practitioner's Guide*.
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
