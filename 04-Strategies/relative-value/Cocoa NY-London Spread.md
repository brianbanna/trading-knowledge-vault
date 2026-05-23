---
aliases: [cocoa arb, NY London cocoa, cocoa arbitrage, CC vs C spread, cocoa quality spread]
tags:
  - "#agri/softs/cocoa"
date-added: "2026-03-24"
---

# Cocoa NY-London Spread

## Core Thesis

The Cocoa NY-London spread trades the price difference between ICE US cocoa (CC, USD/tonne) and ICE Europe/LIFFE cocoa (C, GBP/tonne). New York cocoa reflects globally sourced beans deliverable to US warehouses. London cocoa historically reflects West African origin beans deliverable to European warehouses. The spread captures 3 forces: quality differentials between deliverable origins, GBP/USD movements, and regional supply/demand imbalances between European and US chocolate manufacturers.

## Mechanics

### How the Spread Works

Compare the 2 contracts by converting London cocoa from GBP/tonne to USD/tonne:

**NY-London Spread = CC (USD/tonne) - [C (GBP/tonne) x GBP/USD]**

Positive spread = NY trades at a premium to London. Negative = London more expensive in dollar terms. Historically NY has traded at a $50 to $300/tonne premium over London (converted to USD), reflecting the broader deliverable origins and higher average quality on the ICE US contract.

### Entry Criteria
- Spread deviates from seasonal pattern or trailing 12 month mean by more than 1.5 [[Z-Score|standard deviations]]
- Catalyst: shift in West African supply allocation between European and US buyers, GBP/USD dislocation, changes in deliverable supply at either exchange
- Divergence in certified stocks between ICE US and ICE Europe warehouses

### Exit Criteria
- Spread reverts toward seasonal or fundamental fair value
- FX component reverses (if FX was the primary driver, thesis may no longer hold)
- Time stop: 4 to 8 weeks without convergence

### Position Sizing
Both contracts are 10 metric tonnes, spread trades 1:1 on tonnage. One leg is GBP, other USD: FX exposure embedded. Many traders hedge GBP/USD separately to isolate the cocoa quality spread. Margin not reduced as much as same exchange spreads because legs trade on different ICE divisions.

## Instruments Used
- [[Cocoa Futures]] ICE US (CC), USD/tonne
- [[Cocoa Futures]] ICE Europe (C), GBP/tonne
- [[GBP/USD]] for FX hedging (recommended for isolating the quality spread)

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | GBP/USD moves overwhelming the cocoa quality signal |
| Max Loss Scenario | Structural shift in deliverable supply rules at either exchange, or GBP flash crash with unhedged FX |
| Hedged Exposure | Directional cocoa price risk largely cancelled |
| Unhedged Exposure | FX risk (GBP/USD), basis between deliverable origins, liquidity mismatch |
| Margin Requirements | Full margin on both legs (no inter exchange spread credit) |

## Edge Source

Physical market dynamics drive the spread and move slowly: West African export allocation between European and US destinations, shipping schedules from Abidjan and San Pedro, certified stock levels at each exchange, and European vs US grindings demand. Traders who monitor Ivory Coast port arrivals, ICCO data, and exchange warehouse reports identify supply shifts before the spread reflects them. The FX overlay creates noise that fundamental cocoa traders exploit when GBP/USD pushes the spread away from quality based fair value.

## When It Works / When It Fails

### Works Well When
- FX is stable and the spread is driven by cocoa fundamentals (quality premiums, regional demand)
- One exchange has a clear surplus or deficit of deliverable cocoa relative to the other
- Seasonal patterns hold: European grindings peak in Q4 (pre Christmas chocolate production), pulling London higher

### Fails When
- GBP/USD volatility drowns out the cocoa signal (Brexit referendum in 2016 moved the spread violently on FX, not cocoa)
- Exchange delivery rule changes alter the relative value of certified stocks
- One leg becomes illiquid (London cocoa has lower volume than New York in some contract months)
- Shipping disruptions change the cost of moving cocoa between regions

## Historical Examples

**2016 Brexit Vote:** GBP collapse caused London cocoa (in USD terms) to plummet relative to New York. The NY-London spread widened sharply on pure FX, not cocoa fundamentals, as GBP/USD dropped from 1.50 to 1.32 overnight. Long the spread without FX hedging profited enormously. Shorts got destroyed.

**2024 to 2025 Supply Crisis:** During the extreme cocoa shortage, both contracts surged above $10,000/tonne equivalent. Spread became volatile as physical tightness affected exchanges differently. London certified stocks collapsed faster because European buyers were more exposed to West African shortfalls. The NY premium compressed as US buyers also scrambled.

## Concrete Example (Current or Recent)

**Concrete:** NY cocoa (CC) at $8,500/tonne. London cocoa (C) at GBP 5,200/tonne. GBP/USD at 1.28. London in USD = 5,200 x 1.28 = $6,656/tonne. Spread = $8,500 - $6,656 = $1,844/tonne. 12 month average $1,200, sigma $400. Current spread 1.6 sigma wide. NY premium is elevated because US certified stocks are temporarily low, but Ivory Coast shipments are en route. Sell the spread: sell 1 CC at $8,500, buy 1 C at GBP 5,200, sell GBP 66,560 forward to hedge FX. If spread narrows to $1,200, profit ~$644/tonne x 10 tonnes = $6,440 per spread. If spread widens to $2,400, lose ~$5,560. Risk/reward ~1.2:1.

**Simplified:** Same product (cocoa), 2 different exchanges in different cities and currencies. New York usually trades at a premium because its deliverable bean mix is broader and higher quality. Convert London to dollars, compare, and bet the gap reverts when it stretches. The dollar/pound exchange rate can dominate the trade, so most pros hedge it out.

## Related Strategies
- [[Inter-Commodity Spread]]
- [[Location Arbitrage]]
- [[Relative Value Trade]]
- [[Calendar Spread]]
- [[Brent-WTI Spread]] (analogous cross geography crude spread)

## Related Concepts
- [[Backwardation]]
- [[Convenience Yield]]
- [[Seasonality]]
- [[Z-Score]]
- [[Mean Reversion]]
- [[Correlation]]
- [[Currency Pair]]

---
*Status: #solid | Last reviewed: 2026-03-24*
