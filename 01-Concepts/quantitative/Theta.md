---
aliases: [theta, time decay, theta decay]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Theta

## Definition
Theta is the rate at which an option's value declines with the passage of time, all else equal. It is the daily cost of holding a long option, in dollars (or pips) per day. For a long [[ATM]] option, theta is negative because [[time value]] erodes as [[expiry]] approaches. Theta is not linear: it accelerates near expiry, with the most rapid decay in the final week. Theta is the direct tradeoff for [[Gamma]]: long gamma means short theta, and vice versa. This gamma/theta tradeoff is the fundamental tension in options trading.

## Why it matters (commodities and FX)
Theta is the "carry" of an options position. FX dealers who sell options collect theta daily but bear [[Gamma]] risk. Systematic theta collection (selling [[Straddle]]s or [[Strangle]]s) generates steady income in calm markets but catastrophic losses in vol spikes. In commodities, theta dynamics around [[expiry]] are critical: [[Brent Crude]] or [[WTI Crude Oil]] options with 1 to 3 days to expiry can have theta at 30% to 50% of remaining premium, making entry/exit timing critical.

## Concrete example

**Concrete:** Trader sells a 1 week EURUSD ATM [[Straddle]] at 8.5% implied vol, collecting 55 pips. Daily theta ~8 pips at inception, rising to 12 pips by the final 2 days. EURUSD moves less than 20 pips per day all week. At expiry the straddle has 15 pips intrinsic. Net 40 pips, mostly theta. Contrast: trader buys a 2 month EURUSD ATM call (82 pips premium) expecting a breakout. Spot moves sideways for 6 weeks. 60 of the 82 pips have evaporated to theta. Spot finally moves 50 pips in the right direction in the last week, but the option is worth 35 pips at expiry. Net loss 47 pips despite being directionally correct.

**Simplified:** Time decay is rent. If you own an option, you pay rent every day. If you sold it, you collect rent. The rent gets bigger as expiry approaches because there is less time for the option to do anything useful. Theta is what makes options different from buying the underlying: even if your thesis is right, you can lose money waiting because the rent eats your position.

## Key mechanics and formulas
- **Theta (call)** = (- spot × N'(d1) × vol) / (2 × sqrt(time)) - foreign rate × spot × e^(- foreign rate × time) × N(d1) + domestic rate × strike × e^(- domestic rate × time) × N(d2)
- **Theta (simplified ATM)** ≈ (- spot × vol) / (2 × sqrt(2 × pi × time)). Theta is proportional to vol and inversely proportional to sqrt(time).
- **Theta acceleration**: proportional to 1 / sqrt(time). A 1 week option decays roughly twice as fast (per day) as a 1 month option.
- **Gamma theta identity**: theta = -0.5 × gamma × spot² × vol². Links the 2 greeks exactly.
- **Daily theta** = annual theta / 365 (calendar days) for FX options
- **Weekend theta**: FX options lose 3 calendar days over the weekend but only 2 trading days of gamma P&L opportunity, structural edge for sellers.

## Prerequisites
- [[Gamma]]
- [[Vanilla Option]]
- [[ATM]]
- [[Implied Volatility]]
- [[Time Value]]

## Related concepts (learn next)
- [[Gamma]]: direct tradeoff. Long gamma requires paying theta; breakeven set by implied vol.
- [[Vega]]: theta and vega interact. Higher implied vol = higher premium = higher absolute theta.
- [[Straddle]]: maximum theta position at any tenor, benchmark for theta collection.
- [[Realized Volatility]]: theta is fair when realized = implied. Sellers profit when realized undershoots.
- [[Strangle]]: lower absolute theta than straddle, but higher theta per unit vega.
- [[ATM]]: theta is most negative at ATM where time value is highest.
- [[Expiry Pinning]]: extreme theta near expiry concentrates decay and hedging dynamics.

## Common misconceptions
1. **"Theta is constant."** Theta accelerates dramatically into expiry. An option losing 2 pips/day with 30 days left loses 8 pips/day with 3 days left.
2. **"Theta is always a cost."** For sellers, theta is income. The question: does theta collected compensate for [[Gamma]] and [[Vega]] risk?
3. **"You can avoid theta by rolling."** Rolling resets the clock but pays the bid/offer and potentially higher implied vol. Not free.
4. **"Weekend theta is free money for sellers."** Theta accrues over weekends, but gap risk from weekend events (elections, geopolitics) can produce Monday opens that more than offset.

## Sources
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
