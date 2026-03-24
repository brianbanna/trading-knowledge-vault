---
aliases: [platinum palladium spread, PGM spread, platinum vs palladium, PL PA spread, autocatalyst spread]
tags:
  - "#metals/precious/platinum"
  - "#metals/precious/palladium"
date-added: "2026-03-24"
---

# Platinum-Palladium Spread

## Core Thesis

The Platinum-Palladium spread trades the price difference between 2 metals that serve the same industrial function: catalytic converters in vehicles. Think of it as trading the substitution decision that every automaker faces. Platinum works better in diesel catalytic converters. Palladium works better in gasoline catalytic converters. But at certain price ratios, automakers will spend the R&D money to switch from one to the other. This substitution threshold creates a natural ceiling and floor for the spread, making it one of the most structurally anchored inter commodity trades in metals.

Historically, platinum traded at a premium to palladium (platinum was roughly 2 to 4x the price of palladium through the 2000s). This relationship inverted dramatically in 2017 to 2021 as palladium surged on gasoline vehicle demand and Russian supply fears, while platinum suffered from the diesel emissions scandal (Dieselgate) killing diesel car demand in Europe.

## Mechanics

### Calculating the Spread

**Spread = Platinum ($/oz) - Palladium ($/oz)**

Or as a ratio: **Platinum / Palladium**

Historical range: the ratio went from 4.0x (platinum premium) in 2008 to 0.35x (palladium premium) in 2021. The long term average (pre 2015) was around 2.0 to 3.0x.

### Entry Criteria
- Ratio at extreme levels where substitution economics become compelling (below 0.5x or above 3.0x historically)
- Auto industry catalyst: new emissions regulations, EV adoption rate changes, automaker announcements about catalyst reformulation
- South African supply disruption (70% of platinum, 35% of palladium) or Russian supply disruption (40% of palladium)
- Confirmation from auto sales data, diesel vs gasoline market share trends

### Exit Criteria
- Ratio reverts toward substitution equilibrium (roughly 0.8 to 1.2x in the current regime)
- Thesis invalidated: automakers abandon substitution plans, or EV adoption eliminates both metals' demand
- Time stop: substitution takes 18 to 24 months to implement, so this is a patient trade

### Position Sizing
Both NYMEX contracts are 50 troy oz. At platinum $950/oz and palladium $1,000/oz, notional values are close ($47,500 vs $50,000), so 1:1 is approximately dollar neutral. Adjust when prices diverge significantly.

## Instruments Used
- [[Platinum Futures]] NYMEX (PL), 50 troy oz
- Palladium Futures NYMEX (PA), 100 troy oz (note: PA is 100 oz, PL is 50 oz, so 2 PL : 1 PA for ounce neutral)
- ETFs: PPLT (platinum) vs PALL (palladium) for smaller notional

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Substitution takes longer than expected (18 to 24 month engineering cycles) |
| Max Loss Scenario | [[Structural Break]]: EV adoption eliminates catalytic converter demand entirely, decoupling both metals from the substitution anchor |
| Hedged Exposure | General PGM direction partially hedged |
| Unhedged Exposure | Supply concentration risk (South Africa strikes, Russian sanctions), auto industry structural shifts, hydrogen economy optionality for platinum |
| Margin Requirements | CME inter commodity spread credit available for PL/PA |

## Edge Source

Understanding auto industry catalyst formulation economics is the primary edge. The substitution threshold is not a fixed price ratio but depends on R&D costs, regulatory approval timelines, and metal loading rates (grams per vehicle). Industry sources (Johnson Matthey PGM Market Report, WPIC) provide annual supply/demand data. South African mine cost curves and Russian export policy are critical supply side inputs. The hydrogen economy represents asymmetric optionality for platinum (fuel cell catalysts use platinum, not palladium), which is not yet priced into the long run ratio.

## When It Works / When It Fails

### Works Well When
- Ratio reaches substitution extremes and automakers are actively reformulating (confirmed by industry reports)
- Supply disruptions in one metal but not the other (South African platinum strikes, Russian palladium sanctions)
- Clear directional shift in auto powertrain mix (diesel share rising = platinum demand up)

### Fails When
- EV adoption accelerates faster than expected, destroying demand for both metals and breaking the substitution anchor
- Russian supply cuts are priced in but don't materialize, or South African supply normalizes unexpectedly
- The trade is crowded: when every macro fund is long platinum/short palladium, the unwind can be violent
- Substitution takes years to implement, meaning the spread can stay extreme longer than your risk budget allows

## Historical Examples

**2017 to 2021 Palladium Surge:** Palladium went from $700 to $3,000/oz while platinum stagnated at $800 to $1,000. The ratio collapsed from 1.3x to 0.35x. Diesel's market share in Europe fell from 55% to 30% post Dieselgate, crushing platinum demand. Meanwhile, gasoline vehicle production boomed globally, pulling palladium higher. Russian supply was tight. Traders who went long platinum/short palladium too early (at 1.0x ratio in 2018) endured 3 years of pain before the ratio bottomed.

**2022 to 2023 Reversion:** Palladium peaked at $3,400 in March 2022 (Russia invasion panic) then collapsed to $1,000 by late 2023 as substitution kicked in, EV adoption reduced catalyst demand, and Russian supply continued despite sanctions. Platinum held around $900 to $1,000. The ratio recovered from 0.35x to 1.0x. Patient traders who went long platinum/short palladium in 2021 were rewarded.

**2008 Platinum Peak:** Platinum hit $2,300/oz on South African power crisis and mine safety shutdowns. Palladium was $450. Ratio = 5.1x. Both crashed in the financial crisis but the ratio normalized to 2.5x.

## Concrete Example (Current or Recent)

Platinum at $950/oz. Palladium at $950/oz. Ratio = 1.0x. The 3 year average is 0.8x. Current ratio is above recent average, suggesting platinum has strengthened relative to palladium. You believe hydrogen fuel cell development will provide structural platinum demand. You go long the ratio: buy 2 PL at $950 (2 x 50 oz = 100 oz, notional $95,000), sell 1 PA at $950 (100 oz, notional $95,000). This is ounce neutral and dollar neutral.

If platinum rises to $1,100 and palladium stays at $950 (ratio = 1.16x): profit on PL = ($1,100 - $950) x 100 oz = $15,000. PA leg flat = $0. Total profit = $15,000. If palladium rallies to $1,200 while platinum stays at $950 (ratio drops to 0.79x): loss on PA = ($1,200 - $950) x 100 oz = $25,000. Stop loss at ratio 0.85x.

## Related Strategies
- [[Inter-Commodity Spread]]
- [[Relative Value Trade]]
- [[Gold-Copper Ratio]] (analogous macro metals ratio)
- [[SHFE vs LME Arb]]

## Related Concepts
- [[Mean Reversion]]
- [[Structural Break]]
- [[Z-Score]]
- [[Correlation]]
- [[Green Metals]]
- [[Scrap Ratio]]

---
*Status: #solid | Last reviewed: 2026-03-24*
