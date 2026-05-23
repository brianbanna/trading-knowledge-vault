---
aliases: [arabica robusta spread, coffee quality spread, KC RC spread, coffee arb, arabica premium]
tags:
  - "#agri/softs/coffee"
date-added: "2026-03-24"
---

# Arabica-Robusta Spread

## Core Thesis

The Arabica-Robusta spread trades the price difference between the 2 coffee species: Arabica (ICE US, ticker KC, USD cents/lb) and Robusta (ICE Europe, ticker RC, USD/tonne). Arabica is the higher quality bean used in specialty and premium blends. Robusta is stronger, more bitter, higher caffeine, used in instant coffee and as filler. The spread reflects quality premiums, substitution economics, and the relative supply health of Brazil (Arabica) vs Vietnam (Robusta).

Mechanism: when the spread is wide, roasters substitute Robusta into blends, compressing the spread. When narrow, roasters shift back to Arabica. Substitution creates a mean reversion anchor.

## Mechanics

### Unit Conversion

Contracts price in different units:
- KC (Arabica): USD cents/lb. Multiply by 22.0462 for USD/tonne.
- RC (Robusta): USD/tonne.

**Spread = KC (converted to USD/tonne) - RC (USD/tonne)**

Example: KC at 240 cents/lb = $5,291/tonne. RC at $3,800/tonne. Spread = $1,491/tonne.

Some traders use a ratio: KC (cents/lb) / RC (cents/lb), where RC is divided by 22.0462.

### Entry Criteria
- Spread deviates from 12 month rolling mean by more than 1.5 [[Z-Score|standard deviations]]
- Fundamental catalyst: Brazilian frost (widens), Vietnamese drought (narrows), roaster blend shifts in trade flow data
- [[Seasonality]]: Brazilian harvest (Apr to Sep) compresses the spread. Vietnamese harvest (Oct to Mar) compresses Robusta's discount.

### Exit Criteria
- Spread reverts to fundamental fair value or seasonal norm
- Substitution threshold reached (roasters announce blend changes)
- Loss limit or time stop (6 to 8 weeks)

### Position Sizing
Contract sizes differ. KC is 37,500 lbs (~17 tonnes). RC is 10 tonnes. At KC = 240 c/lb and RC = $3,800/tonne: KC contract value = $90,000. RC contract value = $38,000. Dollar neutral ratio ~1 KC : 2.4 RC. Most traders use 1:2 and accept some directional lean.

## Instruments Used
- [[Coffee Futures]] ICE US Arabica (KC)
- [[Coffee Futures]] ICE Europe Robusta (RC)
- BRL/USD exposure embedded in the Arabica leg

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Weather event in one origin but not the other (Brazil frost widens spread explosively) |
| Max Loss Scenario | Severe Brazil frost moves Arabica 30%+ in days while Robusta is unaffected |
| Hedged Exposure | Partially hedged vs broad coffee moves, correlation 0.6 to 0.8 |
| Unhedged Exposure | Origin specific shocks, BRL/VND moves, exchange liquidity mismatch |
| Margin Requirements | Full margin on both legs (different exchanges, no spread credit) |

## Edge Source

Roaster substitution economics drive the spread. Large roasters (Nestle, JDE Peet's, Lavazza) adjust blend ratios based on the Arabica-Robusta gap. When Arabica exceeds ~2x Robusta (per lb), substitution accelerates. Tracking ICO trade flow data, certified stocks at both exchanges, Brazilian crop estimates (CONAB), and Vietnamese export data provides informational edge. The BRL is a hidden driver: a weak Real incentivizes Brazilian farmers to sell Arabica aggressively, narrowing the spread even with unchanged demand.

## When It Works / When It Fails

### Works Well When
- Spread reaches substitution threshold extremes and roasters respond
- Both harvests proceed normally, allowing seasonal patterns to play out
- BRL is stable, isolating the coffee quality signal

### Fails When
- Brazilian frost or drought: the biggest risk. Frost events happen overnight and move KC by limit up ($0.20/lb = $7,500 per contract) while RC barely moves. Short the spread = catastrophic losses.
- Vietnamese supply disruption narrows the spread from the Robusta side
- Correlation breakdown during commodity selloffs
- Structural demand shift: specialty coffee market share gains may permanently widen the Arabica premium

## Historical Examples

**1994 Brazil Frost:** 2 severe frosts in June and July 1994 destroyed ~30% of Brazilian Arabica production. KC doubled from 80 to 160 cents/lb in weeks. Spread exploded. Traders short the spread faced margin calls that wiped out years of profits.

**2021 to 2022 Brazilian Drought and Frost:** Drought in 2021 followed by July 2021 frost pushed KC from 130 to 260 cents/lb. Robusta rose to $2,400/tonne but less. Spread widened to historic extremes, then mean reverted over 12 months as roasters substituted Robusta and Brazilian production recovered.

**2024 to 2025 Vietnamese Drought:** Drought in Vietnam's Central Highlands cut Robusta production. RC surged above $5,000/tonne, compressing the spread from the Robusta side. Mean reversion shorts got squeezed.

## Concrete Example (Current or Recent)

**Concrete:** KC at 380 cents/lb = $8,377/tonne. RC at $5,200/tonne. Spread = $3,177/tonne. Ratio = 380 / (5,200 / 22.0462) = 1.61x. 5 year average ratio ~1.8x, 12 month ~1.5x (compressed by Robusta shortage). Vietnamese new harvest (Oct to Mar) easing the shortage. Trader goes long the spread: buy 1 KC at 380 c/lb, sell 2 RC at $5,200/tonne. If Robusta falls to $4,500/tonne while Arabica holds at 380, spread widens to $3,877. Profit $700/tonne on each RC leg = $7,000 on 2 RC contracts plus the spread widening on KC. Stop loss at ratio 1.40x.

**Simplified:** Buy expensive coffee, sell cheap coffee. If the cheap one falls (or the expensive one rises), the gap widens and you profit. The gap stays bounded because roasters switch blends when one side gets too expensive. Frost or drought in one country can blow the gap open before substitution kicks in. That is the risk.

## Related Strategies
- [[Inter-Commodity Spread]]
- [[Relative Value Trade]]
- [[Cocoa NY-London Spread]] (analogous quality/geography spread in softs)
- [[Calendar Spread]]

## Related Concepts
- [[Seasonality]]
- [[Convenience Yield]]
- [[Backwardation]]
- [[Mean Reversion]]
- [[Z-Score]]
- [[Correlation]]
- [[Commodity Currencies]]

---
*Status: #solid | Last reviewed: 2026-03-24*
