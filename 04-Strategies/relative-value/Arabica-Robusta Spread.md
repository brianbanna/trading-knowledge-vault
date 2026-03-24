---
aliases: [arabica robusta spread, coffee quality spread, KC RC spread, coffee arb, arabica premium]
tags:
  - "#agri/softs/coffee"
date-added: "2026-03-24"
---

# Arabica-Robusta Spread

## Core Thesis

The Arabica-Robusta spread trades the price difference between the 2 main species of coffee: Arabica (ICE US, ticker KC, in USD cents/lb) and Robusta (ICE Europe, ticker RC, in USD/tonne). Think of it as the gap between premium and economy coffee. Arabica is the smooth, complex tasting bean used in specialty coffee and high end blends. Robusta is the stronger, more bitter, higher caffeine bean used in instant coffee and as a cheap filler in commercial blends. The spread reflects quality premiums, substitution economics, and the relative supply health of Brazil (Arabica) vs Vietnam (Robusta).

The key dynamic: when the spread is wide (Arabica expensive relative to Robusta), roasters substitute more Robusta into blends, which compresses the spread. When the spread is narrow, roasters shift back to Arabica for better taste. This substitution mechanism creates a natural mean reversion anchor.

## Mechanics

### Unit Conversion

The contracts are priced in different units. To compare them:
- KC (Arabica): USD cents/lb. Multiply by 22.0462 to get USD/tonne.
- RC (Robusta): USD/tonne. Already in USD/tonne.

**Spread = KC (converted to USD/tonne) - RC (USD/tonne)**

Example: KC at 240 cents/lb = 240 x 22.0462 = $5,291/tonne. RC at $3,800/tonne. Spread = $1,491/tonne.

Alternatively, many traders express the spread as a ratio: KC (cents/lb) / RC (cents/lb), where RC is converted to cents/lb by dividing by 22.0462.

### Entry Criteria
- Spread (or ratio) deviates from 12 month rolling mean by more than 1.5 [[Z-Score|standard deviations]]
- Fundamental catalyst: Brazilian frost scare (widens spread), Vietnamese drought (narrows spread), shift in roaster blend ratios visible in trade flow data
- [[Seasonality]]: Brazilian harvest (Apr to Sep) tends to compress the spread as Arabica supply arrives. Vietnamese harvest (Oct to Mar) compresses Robusta's discount.

### Exit Criteria
- Spread reverts to fundamental fair value or seasonal norm
- Substitution threshold reached (roasters publicly announce blend changes)
- Loss limit or time stop (6 to 8 weeks)

### Position Sizing
Contract sizes differ significantly. KC is 37,500 lbs (approximately 17 tonnes). RC is 10 tonnes. For a dollar neutral spread, you need to adjust the ratio. At KC = 240 c/lb and RC = $3,800/tonne: KC contract value = 37,500 x $2.40 = $90,000. RC contract value = 10 x $3,800 = $38,000. Dollar neutral ratio is approximately 1 KC : 2.4 RC. In practice, traders often use 1:2 or round to manageable ratios and accept some directional lean.

## Instruments Used
- [[Coffee Futures]] ICE US Arabica (KC)
- [[Coffee Futures]] ICE Europe Robusta (RC)
- BRL/USD exposure is embedded in the Arabica leg (Brazilian farmer selling)

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Weather event in one origin but not the other (e.g., Brazil frost widens spread explosively) |
| Max Loss Scenario | Severe frost in Brazil can move Arabica 30%+ in days while Robusta is unaffected, blowing out the spread |
| Hedged Exposure | Partially hedged vs broad coffee moves, but correlation is only 0.6 to 0.8 |
| Unhedged Exposure | Origin specific supply shocks, BRL/VND currency moves, exchange liquidity mismatch |
| Margin Requirements | Full margin on both legs (different exchanges/divisions, no spread credit) |

## Edge Source

Understanding roaster substitution economics is the primary edge. Large roasters (Nestle, JDE Peet's, Lavazza) adjust blend ratios based on the Arabica-Robusta price gap. When Arabica exceeds roughly 2x the price of Robusta (on a per lb basis), substitution accelerates and compresses the spread. Tracking ICO trade flow data, certified stocks at both exchanges, Brazilian crop estimates (CONAB), and Vietnamese export data provides an informational advantage. The BRL is a hidden driver: a weak Real incentivizes Brazilian farmers to sell Arabica aggressively, narrowing the spread even if demand is unchanged.

## When It Works / When It Fails

### Works Well When
- Spread reaches substitution threshold extremes and roasters respond predictably
- Both harvests proceed normally (no weather surprises), allowing seasonal patterns to play out
- Brazilian Real is stable, isolating the coffee quality signal

### Fails When
- Brazilian frost or drought: the single biggest risk. Frost events can happen overnight and move KC by limit up ($0.20/lb = $7,500 per contract) while RC barely moves. If you are short the spread (short KC, long RC), losses are catastrophic and fast.
- Vietnamese supply disruption narrows the spread from the other side (drought, export restrictions)
- Correlation breakdown during general commodity selloffs (both legs fall but at different rates)
- Structural demand shift: if specialty coffee continues taking market share, the Arabica premium may permanently widen

## Historical Examples

**1994 Brazil Frost:** Two severe frosts in June and July 1994 destroyed approximately 30% of Brazilian Arabica production. KC doubled from 80 to 160 cents/lb within weeks. The Arabica-Robusta spread exploded. Traders short the spread faced margin calls that wiped out years of profits.

**2021 to 2022 Brazilian Drought and Frost:** Drought during 2021 followed by frost in July 2021 pushed KC from 130 to 260 cents/lb. Robusta also rose (to $2,400/tonne) but much less. The spread widened to historic extremes, then mean reverted over 12 months as roasters aggressively substituted Robusta and Brazilian production partially recovered.

**2024 to 2025 Vietnamese Drought:** Severe drought in Vietnam's Central Highlands cut Robusta production. RC surged above $5,000/tonne, compressing the Arabica-Robusta spread from the Robusta side. Traders who expected mean reversion by shorting the spread got squeezed as the Robusta shortage persisted.

## Concrete Example (Current or Recent)

KC trades at 380 cents/lb = $8,377/tonne. RC trades at $5,200/tonne. The spread is $3,177/tonne. The ratio is 380 / (5,200 / 22.0462) = 380 / 235.9 = 1.61x. The 5 year average ratio is approximately 1.8x and the 12 month average is 1.5x (compressed due to the Robusta shortage).

You believe the Vietnamese Robusta shortage is easing as the new harvest arrives (Oct to Mar). You go long the spread: buy 1 KC at 380 c/lb, sell 2 RC at $5,200/tonne. If Robusta falls to $4,500/tonne while Arabica holds at 380, the spread widens to $3,877 and you profit $700/tonne on each RC leg = $7,000 on 2 RC contracts plus the spread widening on KC. If instead both fall but Robusta falls less, you lose on the narrowing spread. Stop loss at a ratio of 1.40x.

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
