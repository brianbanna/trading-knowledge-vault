---
aliases: [COT, Commitment of Traders, CFTC report, COT data, COT positioning]
tags:
  - "#quant"
  - "#macro"
date-added: "2026-03-20"
---

# COT Report

## Definition

The Commitment of Traders (COT) is a weekly CFTC publication that breaks down open interest in US futures markets by trader category. Released Friday 3:30 PM ET reflecting Tuesday positions, it shows net longs and shorts for three main groups: commercials (producers, consumers), non commercials / managed money (hedge funds, CTAs), and non reportables (small specs). It covers all major commodity, financial, and FX futures on [[COMEX]], NYMEX, CBOT, and CME. The Traders in Financial Futures (TFF) version provides finer categories for financial contracts.

## Why it matters (commodities and FX)

The COT is the most widely used positioning indicator in commodity and FX markets. Extreme managed money positioning is a contrarian signal: record net long = crowded and vulnerable to reversal; record net short = washed out and vulnerable to short covering. Commercials are inherently contrarian (producers hedge into strength, consumers into weakness). The COT is most useful at extremes, not for timing intermediate moves.

## Concrete example

**Concrete:** COT prints managed money net long 300,000 contracts in [[Brent Crude]], a 2 year high. Trader reads crowded long, buys 50 contracts of $5 OTM puts expiring in 6 weeks at $1.20 (cost $60,000). 2 weeks later OPEC announces a quota overshoot. MM liquidates 100,000 contracts. Brent drops $8/bbl. Puts trade to $4.50, exit for $225,000 (net +$165,000).

**Simplified:** Speculators tend to pile into the same direction. When they are extremely long, there are few new buyers left and any bad news triggers a rush for the exit. When they are extremely short, the opposite. The COT report tells you, with a 3 day delay, where they are positioned. You buy puts or sell into extreme longs, and buy or sell calls into extreme shorts, but only when a catalyst is in sight.

## Key mechanics and formulas

**Release schedule:** Friday 3:30 PM ET, reporting Tuesday positions.

**Trader categories (disaggregated COT):**
- Producer/Merchant: physical hedgers
- Swap Dealer: banks running OTC books
- Managed Money: hedge funds, CTAs
- Other Reportables: other large traders
- Non Reportable: small speculators

**Contrarian thresholds:** Assessed as percentile rank over 3 to 5 year history. Above 90th = crowded long. Below 10th = crowded short.

**Key markets:** Gold, silver, WTI, Brent, natural gas, copper, corn, soybeans, wheat, EUR/USD, JPY, GBP, AUD, CAD, S&P 500, Treasuries.

## Prerequisites

- [[Futures Contract]]
- [[COMEX]]

## Related concepts (learn next)

- [[Gold Futures]] because COT gold positioning is a primary contrarian signal.
- [[Brent Crude]] because energy COT data shows managed money oil positioning.
- [[CTA]] because CTAs are a major component of managed money.
- [[Macro Regime]] because positioning extremes often coincide with regime transitions.
- [[ETF Flows]] because comparing COT futures positioning with ETF flows reveals speculative vs physical demand.
- [[Positioning Signal]] because COT is the foundation for positioning based strategies.

## Common misconceptions

**"COT tells you what happens next."** It shows positioning, not direction. Crowded positions persist for weeks before reversing.

**"Commercials are always right."** Commercials are not directional traders. They hedge physical exposure. Their positioning is informative but not predictive alone.

**"The weekly lag makes COT useless."** The 3 day lag is manageable for swing and position horizons. Intraday traders cannot use it; position traders do.

## Sources

- CFTC: Commitment of Traders Reports
- CFTC: Disaggregated and Traders in Financial Futures Reports
- CME Group: COT Data and Analysis Tools
