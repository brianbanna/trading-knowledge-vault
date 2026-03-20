---
aliases: [COT, Commitment of Traders, CFTC report, COT data, COT positioning]
tags:
  - "#quant"
  - "#macro"
date-added: "2026-03-20"
---

# COT Report

## Definition

The Commitment of Traders (COT) report is a weekly publication by the US Commodity Futures Trading Commission (CFTC) that breaks down open interest in US futures markets by trader category. Published every Friday at 3:30 PM ET (reflecting Tuesday's positions), it shows the net long or short positions of three main groups: commercials (hedgers, typically producers and consumers), non commercials/managed money (speculative hedge funds, CTAs), and non reportable (small speculators). The report covers all major commodity, financial, and FX futures traded on US exchanges ([[COMEX]], NYMEX, CBOT, CME). The Traders in Financial Futures (TFF) version provides even more granular categories for financial contracts.

## Why it matters (commodities and FX)

The COT report is the most widely used positioning indicator in commodity and FX markets. Extreme positioning by managed money (large speculators) is a contrarian signal: when managed money is net long at record levels, the trade is crowded and vulnerable to reversal. When managed money is net short at extremes, the market is washed out and vulnerable to a short covering rally. Commercials (hedgers) tend to be contrarian by nature since producers hedge when prices are high and consumers hedge when prices are low. The COT is most useful at extremes rather than for timing intermediate moves.

## Concrete example

The COT report shows managed money net long 300,000 contracts in [[Brent Crude]], the highest in 2 years. A contrarian trader interprets this as a crowded long position vulnerable to liquidation. She buys put options on Brent. If a bearish catalyst triggers (OPEC overproduction, demand shock), managed money liquidates 100,000 contracts in 2 weeks, and Brent drops $8/bbl. The puts profit handsomely. If instead geopolitical escalation triggers more buying and the net long extends to 350,000, the puts expire worthless.

## Key mechanics and formulas

**Release schedule:** Friday 3:30 PM ET, reporting Tuesday's positions.

**Trader categories (disaggregated COT):**
- Producer/Merchant: physical hedgers
- Swap Dealer: banks running OTC books
- Managed Money: hedge funds, CTAs
- Other Reportables: other large traders
- Non Reportable: small speculators

**Contrarian signal thresholds:** Typically assessed as percentile rank over 3 to 5 year history. Above 90th percentile net long = crowded long. Below 10th percentile = crowded short.

**Key markets covered:** Gold, silver, crude oil (WTI and Brent), natural gas, copper, corn, soybeans, wheat, EUR/USD, JPY, GBP, AUD, CAD, S&P 500, Treasury bonds.

## Prerequisites

- [[Futures Contract]]
- [[COMEX]]

## Related concepts (learn next)

- [[Gold Futures]] because COT gold positioning is a key contrarian signal.
- [[Brent Crude]] because energy COT data shows managed money oil positioning.
- [[CTA]] because CTAs are a major component of the managed money category.
- [[Macro Regime]] because positioning extremes often coincide with regime transitions.
- [[ETF Flows]] because comparing COT futures positioning with ETF flows reveals whether demand is speculative or physical.
- [[Positioning Signal]] because the COT report is the foundation for positioning based trading signals.

## Common misconceptions

**"The COT tells you what will happen next."** The COT shows positioning, not direction. Crowded positions can persist for weeks or months before reversing.

**"Commercials are always right."** Commercial hedgers are not directional traders. They hedge their physical exposure. Their positioning is informative but not predictive in isolation.

**"The weekly lag makes COT useless."** The 3 day lag (Tuesday positions reported Friday) is manageable for most trading horizons. Intraday traders cannot use COT, but position/swing traders find it valuable.

## Sources

- CFTC: Commitment of Traders Reports
- CFTC: Disaggregated and Traders in Financial Futures Reports
- CME Group: COT Data and Analysis Tools
