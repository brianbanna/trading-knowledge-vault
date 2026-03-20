---
aliases: [inter-commodity spread, cross-commodity spread, quality spread, product spread]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-03-20"
---

# Inter-Commodity Spread

## Core Thesis

An inter-commodity spread buys one commodity and sells a different but economically related commodity, profiting from changes in their relative pricing. Unlike [[Calendar Spread|calendar spreads]] (same commodity, different months), inter-commodity spreads trade the relationship between different products. The economic linkage can be a processing relationship ([[Crack Spread]], crush spread), substitution (palladium vs platinum in catalytic converters), shared demand drivers (copper vs aluminum in electrical), or input/output (natural gas vs power). The key requirement: there must be a structural economic reason for the 2 prices to be related.

## Mechanics

### Spread Types

**Processing spreads:** Long the input, short the output (or reverse). [[Crack Spread]] (crude to gasoline/diesel), crush spread (soybeans to meal and oil), spark spread (natural gas to power), dark spread (coal to power).

**Substitution spreads:** Long 1 substitute, short the other. Platinum vs palladium (autocatalyst), copper vs aluminum (wiring), [[Brent Crude]] vs Dubai (refinery feedstock choice).

**Relative demand spreads:** Long 1 cyclical metal, short another. Copper vs zinc (construction vs galvanizing), gold vs copper (safe haven vs growth).

**Cross market spreads:** Same commodity in different geographies. [[Brent-WTI Spread]], TTF vs Henry Hub (transatlantic gas), LME copper vs COMEX copper.

### Entry Criteria
- Spread deviates from fundamental fair value or historical range
- Identifiable catalyst: refinery turnaround affecting crack spreads, substitution threshold crossed, demand divergence between 2 metals
- [[Z-Score]] vs appropriate lookback period (90 day, 1 year, or seasonal)

### Exit Criteria
- Spread reverts to fair value
- Fundamental thesis invalidated
- Loss limit or time stop

### Position Sizing
Contracts often differ in size, so the hedge ratio must be adjusted. A soybean crush spread uses 1 soybean contract (5,000 bushels) vs 1 soy meal (100 short tons) and 1 soy oil (60,000 lbs), weighted by processing yields. For metal spreads, match notional value: if copper is $9,000/tonne (25 tonne lot = $225,000) and aluminum is $2,400/tonne (25 tonne lot = $60,000), a dollar neutral ratio is approximately 1 copper : 3.75 aluminum.

## Instruments Used
- Crude/products: [[WTI Crude Oil]], [[Brent Crude]], RBOB gasoline, ULSD/heating oil
- Soybeans: soybean futures, soy meal, soy oil (CBOT)
- Metals: [[Copper Futures]], aluminum, zinc, nickel (LME or COMEX), [[Gold Futures]], [[Silver Futures]]
- Gas/power: [[Henry Hub Natural Gas]], [[TTF Natural Gas]], PJM power, German power

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Divergence: the economic relationship weakens or breaks |
| Max Loss Scenario | [[Structural Break]] in the relationship (technology change, regulation, permanent substitution) |
| Hedged Exposure | Partially hedged vs broad commodity selloff (less than calendar spreads) |
| Unhedged Exposure | Relative demand shifts, basis risk between different contracts/exchanges |
| Margin Requirements | Some exchanges offer inter-commodity spread credits; others require full margin on both legs |

## Edge Source

Fundamental: deep understanding of processing economics, substitution thresholds, and supply chain dynamics. The crack spread trader who knows refinery yields, turnaround schedules, and product demand patterns has an informational edge. Statistical: many inter-commodity spreads are mean reverting because physical arbitrage (processing, substitution) constrains the range.

## When It Works / When It Fails

### Works Well When
- Processing economics are stable and spreads deviate from cost based fair value
- Substitution thresholds are well defined (e.g., platinum/palladium at specific price ratios)
- Both legs are liquid and trade on the same exchange or with reliable cross exchange execution

### Fails When
- Technological disruption changes the relationship permanently (EVs reducing palladium demand, renewable power breaking the spark spread)
- Regulatory change (carbon pricing alters coal vs gas economics)
- [[Liquidity]] mismatch between legs: one leg moves freely, the other is thin and gappy
- [[Correlation]] breakdown during stress events (both legs move in the same direction but at different speeds)

## Historical Examples

**Gold/Oil Ratio (2020):** The gold/oil ratio spiked to historic extremes (>40 barrels of oil per ounce of gold, vs a ~15 to 20 long term average) during the COVID crash as oil collapsed and gold held firm. Mean reversion traders who went long oil/short gold at extremes profited over the following 12 months.

**Palladium/Platinum (2018 to 2021):** Palladium surged to a $1,500+ premium over platinum due to gasoline vehicle catalytic converter demand and Russian supply fears. Platinum/palladium substitution in autocatalysts eventually capped the divergence, but the [[Structural Break]] lasted years.

## Concrete Example (Current or Recent)

The 3:2:1 [[Crack Spread]] using [[WTI Crude Oil]], RBOB gasoline, and ULSD: WTI at $74/bbl, RBOB at $2.40/gal (= $100.80/bbl), ULSD at $2.60/gal (= $109.20/bbl). Crack spread = ((2 x $100.80) + (1 x $109.20) - (3 x $74)) / 3 = ($201.60 + $109.20 - $222) / 3 = $29.60/bbl. If the 5 year seasonal average for this week is $22/bbl, the crack is $7.60 rich. A short crack trade (sell gasoline + ULSD, buy crude) profits if margins normalize. Risk: a refinery outage could push cracks higher.

## Related Strategies
- [[Relative Value Trade]]
- [[Calendar Spread]]
- [[Crack Spread]]
- [[Brent-WTI Spread]]
- [[Location Arbitrage]]

## Related Concepts
- [[Correlation]]
- [[Mean Reversion]]
- [[Structural Break]]
- [[Z-Score]]
- [[Seasonality]]
- [[Hedging]]

---
*Status: #solid | Last reviewed: 2026-03-20*
