---
aliases: [theta, time decay, theta decay]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Theta

## Definition
Theta measures the rate at which an option's value declines with the passage of time, all else being equal. It represents the daily cost of holding a long option position, expressed as the dollar (or pip) amount lost per day. For a long [[ATM]] option, theta is always negative because [[time value]] erodes as [[expiry]] approaches. Theta is not linear: it accelerates as expiry nears, with the most rapid decay occurring in the final week. Theta is the direct tradeoff for [[Gamma]] exposure: a position that is long gamma (benefits from spot moves) is short theta (pays time decay), and vice versa. This gamma/theta tradeoff is the fundamental tension in all options trading.

## Why it matters (commodities and FX)
Theta represents the "carry" or "rent" of an options position. In FX, dealers who sell options to clients collect theta daily but bear [[Gamma]] risk. Systematic theta collection strategies (selling [[Straddle]]s or [[Strangle]]s) generate steady income in calm markets but face catastrophic losses during vol spikes. In commodities, theta dynamics around [[expiry]] dates are critical: [[Brent Crude]] or [[WTI Crude Oil]] options with 1 to 3 days to expiry can have theta equal to 30% to 50% of the remaining premium, making timing of entry and exit critical. Understanding theta helps traders decide whether to buy or sell premium and when to roll positions before decay accelerates.

## Concrete example
**Success:** A trader sells a 1 week EUR/USD ATM [[Straddle]] at 8.5% implied vol, collecting 55 pips. Daily theta is approximately 8 pips per day at inception, rising to 12 pips per day by the final 2 days. EUR/USD moves less than 20 pips per day for the entire week. At expiry, the straddle has 15 pips of intrinsic value. Net profit is 55 minus 15 = 40 pips, mostly from theta collection.

**Failure:** A trader buys a 2 month EUR/USD ATM call (82 pips premium) expecting a breakout. Spot moves sideways for 6 weeks. By then, 60 pips of the original 82 pip premium has evaporated from theta alone. Spot finally moves 50 pips in the right direction in the last week, but the option is only worth 35 pips at expiry. Net loss is 47 pips despite being directionally correct.

## Key mechanics and formulas
- **Theta (call)** = (negative spot × N'(d1) × vol) / (2 × sqrt(time)) minus foreign rate × spot × e^(negative foreign rate × time) × N(d1) + domestic rate × strike × e^(negative domestic rate × time) × N(d2)
- **Theta (simplified ATM)** = approximately (negative spot × vol) / (2 × sqrt(2 × pi × time)), showing theta is proportional to vol and inversely proportional to sqrt(time)
- **Theta acceleration**: theta is proportional to 1 / sqrt(time), so a 1 week option decays roughly twice as fast (per day) as a 1 month option
- **Gamma theta identity**: theta = negative 0.5 × gamma × spot² × vol², linking the 2 greeks exactly
- **Daily theta** = annual theta / 365 (calendar days) for FX options
- **Weekend theta**: FX options lose 3 calendar days of theta over the weekend but only 2 trading days of gamma P&L opportunity, creating a structural edge for sellers over weekends

## Prerequisites
- [[Gamma]]
- [[Vanilla Option]]
- [[ATM]]
- [[Implied Volatility]]
- [[Time Value]]

## Related concepts (learn next)
- [[Gamma]]: the exact tradeoff partner; long gamma requires paying theta, and the breakeven is determined by implied vol
- [[Vega]]: theta and vega interact because higher implied vol means higher premium and therefore higher absolute theta
- [[Straddle]]: the maximum theta position at any tenor, making it the benchmark for theta collection strategies
- [[Realized Volatility]]: theta is "fair" when realized vol equals implied vol; sellers profit when realized undershoots
- [[Strangle]]: lower absolute theta than the straddle, but higher theta per unit of vega
- [[ATM]]: theta is most negative at ATM, where time value is highest
- [[Expiry Pinning]]: extreme theta near expiry concentrates decay and hedging dynamics

## Common misconceptions
1. **"Theta is constant."** Theta accelerates dramatically as expiry approaches. An option that loses 2 pips per day with 30 days left may lose 8 pips per day with 3 days left.
2. **"Theta is always a cost."** For option sellers, theta is income. The question is whether the theta collected compensates for the [[Gamma]] and [[Vega]] risk borne.
3. **"You can avoid theta by rolling options."** Rolling to a new expiry resets the clock but requires paying the bid/offer spread and potentially buying at higher implied vol. Rolling is not free.
4. **"Weekend theta is free money for sellers."** While theta accrues over weekends, gap risk from weekend events (elections, geopolitical developments) can produce Monday opens that more than offset the theta collected.

## Sources
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
