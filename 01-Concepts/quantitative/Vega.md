---
aliases: [vega, vol sensitivity, volatility exposure]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Vega

## Definition
Vega is the sensitivity of an option's price to a 1 percentage point change in [[implied volatility]]. An option with vega 0.05 gains 0.05 (e.g., 5 pips in FX) per 1 vol point increase. Vega is not a Greek letter, but it is universally included in the [[Greeks]] toolkit. Long options are long vega; short options are short vega. Vega is the primary risk measure for [[Volatility]] as a tradeable asset, distinct from [[Delta]] (directional) and [[Gamma]] (convexity). Vega exposure peaks near [[ATM]] and declines for deep ITM or OTM options.

## Why it matters (commodities and FX)
Vega is the dominant risk factor for any options book. An FX options desk running EUR 500M notional in EURUSD might carry EUR 50,000 of vega: a 1 vol point move swings P&L by EUR 50,000. In commodities, [[Brent Crude]] vega exposure determines profit/loss from routine vol expansions around [[OPEC]] meetings and [[EIA Report]] releases. Managing vega across tenors (the vega term structure) is a core skill: a book can be vega flat in aggregate but massively long short dated and short long dated, exposing it to term structure shifts. Most options blowups involve uncontrolled vega in a vol spike.

## Concrete example

**Concrete:** Trader long EUR 200M EURUSD 3 month ATM options with vega 0.08 per million notional. Total vega EUR 16,000. Implied vol rises 7.5% to 9.0% (1.5 vol points) after a surprise tariff announcement. Vega P&L = 16,000 × 1.5 = EUR 24,000 before delta or gamma effects. Contrast: commodity desk sells 3 month [[Brent Crude]] straddles to collect premium, accumulating short vega of USD 80,000 per vol point. Middle East tensions push 3 month Brent implied vol 28% to 38% in a week. Vega loss = 80,000 × 10 = USD 800,000. Premium collected over the prior 2 months was USD 250,000. Net loss USD 550,000.

**Simplified:** Vega is your bet on volatility levels. If you own options and vol rises, you make money even before spot moves. If you sold options and vol rises, you lose. The whole vol market is essentially a market in vega exposure: dealers want to be flat, end users want directional vol exposure, and prices adjust to match supply and demand for vega.

## Key mechanics and formulas
- **Vega** = spot × e^(- foreign rate × time) × sqrt(time) × N'(d1), N'(d1) = standard normal density at d1
- **Vega per 1 vol point** = vega / 100 (since vol is in percentage terms)
- **Vega peaks at ATM**: when d1 ≈ 0, N'(d1) is maximized
- **Vega scales with sqrt(time)**: longer dated options have more vega, ~proportional to sqrt(time to expiry)
- **Weighted vega**: desks weight vega by 1 / sqrt(time) to normalize across tenors, making 1 month and 1 year comparable
- **Vega P&L** = vega × change in implied vol (in vol points)
- **Put call parity for vega**: calls and puts at the same strike and expiry have identical vega

## Prerequisites
- [[Implied Volatility]]
- [[Vanilla Option]]
- [[ATM]]
- [[Vol Surface]]
- [[Greeks]]

## Related concepts (learn next)
- [[Volga]]: sensitivity of vega to vol changes, second order, critical for OTM options.
- [[Gamma]]: convexity in spot; analogous to volga in vol.
- [[Theta]]: long vega positions pay theta. The vega/theta tradeoff is the core options dilemma.
- [[Realized Volatility]]: vega captures sensitivity to implied; realized drives delta hedged P&L through gamma.
- [[Vanna]]: cross sensitivity between delta and vol. Links vega risk to directional risk.
- [[Vol Surface]]: vega exposure is distributed across the surface. Management requires monitoring all tenors and strikes.
- [[Straddle]]: maximum vega structure at any tenor, used for pure vol bets.

## Common misconceptions
1. **"Vega is the same as volatility risk."** Vega captures implied vol changes; vol risk also includes [[Realized Volatility]] exposure (captured by [[Gamma]]) and smile dynamics (captured by [[Vanna]] and [[Volga]]).
2. **"Long vega is always a good hedge."** Long vega protects against vol spikes but bleeds [[Theta]] daily. If vol does not rise, the position loses consistently.
3. **"Vega is constant."** Vega changes with spot (via [[Vanna]]), vol (via [[Volga]]), and time. These second order effects can be larger than first order vega for deep OTM options.
4. **"Total book vega of zero means no vol risk."** A book can be vega neutral in aggregate but carry massive vega in specific tenors or strikes, with large P&L from term structure or smile moves.

## Sources
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Gatheral, Jim. *The Volatility Surface: A Practitioner's Guide*.
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
