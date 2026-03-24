---
aliases: [cocoa arb, NY London cocoa, cocoa arbitrage, CC vs C spread, cocoa quality spread]
tags:
  - "#agri/softs/cocoa"
date-added: "2026-03-24"
---

# Cocoa NY-London Spread

## Core Thesis

The Cocoa NY-London spread trades the price difference between ICE US cocoa (CC, priced in USD/tonne) and ICE Europe/LIFFE cocoa (C, priced in GBP/tonne). Think of it like comparing the price of the same product in 2 different shops that serve slightly different customers and accept different currencies. New York cocoa reflects globally sourced beans deliverable to US warehouses, while London cocoa historically reflects West African origin beans deliverable to European warehouses. The spread captures 3 intertwined forces: quality differentials between deliverable origins, GBP/USD exchange rate movements, and regional supply/demand imbalances between European and US chocolate manufacturers.

## Mechanics

### How the Spread Works

To compare the 2 contracts, you must convert London cocoa from GBP/tonne to USD/tonne. The spread is typically quoted as:

**NY-London Spread = CC (USD/tonne) - [C (GBP/tonne) x GBP/USD exchange rate]**

A positive spread means New York trades at a premium to London. A negative spread means London is more expensive in dollar terms. Historically, New York has traded at a premium of $50 to $300/tonne over London (converted to USD), reflecting the broader range of deliverable origins and higher average quality on the ICE US contract.

### Entry Criteria
- Spread deviates from its seasonal pattern or trailing 12 month mean by more than 1.5 [[Z-Score|standard deviations]]
- Identifiable catalyst: shift in West African supply allocation between European and US buyers, GBP/USD dislocation, changes in deliverable supply at either exchange
- Divergence in certified stocks between ICE US and ICE Europe warehouses

### Exit Criteria
- Spread reverts toward seasonal or fundamental fair value
- FX component reverses (if FX was the primary driver, the trade may no longer make sense)
- Time stop: 4 to 8 weeks without convergence

### Position Sizing
Both contracts are 10 metric tonnes, so the spread trades 1:1 on a tonnage basis. However, because one leg is in GBP and the other in USD, you carry FX exposure. Some traders hedge the GBP/USD component separately to isolate the pure cocoa quality spread. Margin is not reduced as much as same exchange spreads because the legs trade on different ICE divisions.

## Instruments Used
- [[Cocoa Futures]] ICE US (CC), USD/tonne
- [[Cocoa Futures]] ICE Europe (C), GBP/tonne
- [[GBP/USD]] for FX hedging (optional but recommended for isolating the quality spread)

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | GBP/USD moves overwhelming the cocoa quality signal |
| Max Loss Scenario | Structural shift in deliverable supply rules at either exchange, or GBP flash crash while holding unhedged FX exposure |
| Hedged Exposure | Directional cocoa price risk is largely cancelled |
| Unhedged Exposure | FX risk (GBP/USD), basis between deliverable origins, liquidity mismatch between exchanges |
| Margin Requirements | Full margin on both legs (no inter exchange spread credit) |

## Edge Source

The spread is driven by physical market dynamics that move slowly and are trackable: West African export allocation between European and US destinations, shipping schedules from Abidjan and San Pedro, certified stock levels at each exchange, and European vs US grindings demand. Traders who monitor Ivory Coast port arrivals, ICCO data, and exchange warehouse reports can identify supply shifts before they show up in the spread. The FX overlay creates noise that fundamental cocoa traders can exploit when GBP/USD moves the spread away from its quality based fair value.

## When It Works / When It Fails

### Works Well When
- FX is stable and the spread is driven by cocoa fundamentals (quality premiums, regional demand shifts)
- One exchange has a clear surplus or deficit of deliverable cocoa relative to the other
- Seasonal patterns hold: European grindings demand peaks in Q4 (pre Christmas chocolate production), pulling London higher

### Fails When
- GBP/USD volatility dominates, drowning out the cocoa signal (e.g., Brexit referendum in 2016 moved the spread violently on FX, not cocoa)
- Exchange delivery rule changes alter the relative value of certified stocks
- One leg becomes illiquid (London cocoa has lower volume than New York in some contract months)
- Shipping disruptions change the cost of moving cocoa between regions

## Historical Examples

**2016 Brexit Vote:** The GBP collapse after the Brexit referendum caused London cocoa (in USD terms) to plummet relative to New York. The NY-London spread widened sharply, not because of any change in cocoa fundamentals, but purely because GBP/USD dropped from 1.50 to 1.32 overnight. Traders who were long the spread without FX hedging profited enormously. Those who had been short got destroyed.

**2024 to 2025 Supply Crisis:** During the extreme cocoa shortage, both contracts surged above $10,000/tonne equivalent. The spread became volatile as physical tightness affected both exchanges differently. London certified stocks collapsed faster because European buyers were more exposed to West African shortfalls. The NY premium compressed as US buyers also scrambled.

## Concrete Example (Current or Recent)

NY cocoa (CC) trades at $8,500/tonne. London cocoa (C) trades at GBP 5,200/tonne. GBP/USD is 1.28. London in USD terms = 5,200 x 1.28 = $6,656/tonne. The NY-London spread is $8,500 - $6,656 = $1,844/tonne. The 12 month average spread is $1,200 with a standard deviation of $400. The current spread is 1.6 sigma wide.

You believe the NY premium is elevated because US certified stocks are temporarily low but Ivory Coast shipments are en route to US warehouses. You sell the spread: sell 1 CC (NY) at $8,500, buy 1 C (London) at GBP 5,200, and sell GBP 66,560 forward to hedge FX. If the spread narrows to $1,200, you profit approximately $644/tonne x 10 tonnes = $6,440 per spread. If the spread widens to $2,400 (1.5 sigma further), you lose approximately $556/tonne x 10 tonnes = $5,560. Risk/reward is roughly 1.2:1.

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
