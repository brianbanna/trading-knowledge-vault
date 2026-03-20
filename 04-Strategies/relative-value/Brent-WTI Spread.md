---
aliases: [Brent WTI spread, Brent WTI arb, transatlantic crude spread, BZ-CL spread]
tags:
  - "#energy/crude/brent"
  - "#energy/crude/wti"
date-added: "2026-03-20"
---

# Brent-WTI Spread

## Core Thesis

The Brent-WTI spread captures the relative pricing between the world's 2 primary crude oil benchmarks. It reflects the cost of moving crude between the US Gulf Coast and global seaborne markets, US pipeline logistics to Cushing, relative supply/demand in the Atlantic Basin, and structural differences between a landlocked (WTI/Cushing) and seaborne (Brent) benchmark. The spread is mean reverting around a level set by transportation economics but regime shifts in infrastructure (pipeline buildouts, export terminal capacity) can permanently alter the equilibrium.

## Mechanics

### Entry Criteria
- Spread deviates significantly from its trailing 6 to 12 month mean (>1.5 [[Z-Score]])
- Identifiable fundamental catalyst: Cushing inventory build/draw, US export capacity change, OPEC action affecting seaborne crude
- Seasonal patterns: US refinery turnaround season can widen the spread as Cushing builds

### Exit Criteria
- Spread reverts to mean or overshoots to the other side
- Fundamental catalyst resolves (Cushing draws normalize, pipeline constraints ease)
- Time stop: if spread has not moved within 4 to 6 weeks, reassess thesis

### Position Sizing
Both contracts are 1,000 barrels, so the spread trades 1:1. Margin is reduced for recognized spreads on CME (approximately 50 to 70% reduction vs outright margin). Size based on spread volatility, not outright crude volatility.

## Instruments Used
- [[Brent Crude]] (ICE CO or CME BZ)
- [[WTI Crude Oil]] (NYMEX CL)

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | [[Structural Break]] in the spread relationship (infrastructure change, policy shift) |
| Max Loss Scenario | Permanent regime shift (e.g., US export ban reimposed, Cushing bypass pipeline built) |
| Hedged Exposure | Directional crude oil price risk largely cancelled |
| Unhedged Exposure | Basis risk, logistics risk, quality differential changes |
| Margin Requirements | Reduced spread margin (CME inter commodity credit) |

## Edge Source

Structural: the spread is anchored by physical transportation costs, pipeline tariffs, and storage economics. These change slowly and predictably. Informational edge comes from tracking Cushing inventories (Genscape satellite data), tanker rates, pipeline flow data, and US export volumes in near real time.

## When It Works / When It Fails

### Works Well When
- Cushing inventories move toward extremes (very full = WTI weakens, spread widens; very empty = WTI strengthens, spread narrows)
- Clear seasonal patterns in US refinery runs
- Stable infrastructure regime (no major pipeline additions or removals)

### Fails When
- Infrastructure regime shifts: the 2011 to 2014 WTI blowout discount (WTI at $20+ discount to Brent) occurred because Cushing was oversupplied and insufficient pipeline capacity existed to move crude to the Gulf Coast. New pipelines (Seaway reversal, Keystone) permanently narrowed the spread.
- US export policy changes
- Sudden geopolitical premium in Brent that has nothing to do with Atlantic Basin logistics

## Historical Examples

**2011 to 2014:** Cushing glut from rising Bakken and Canadian production overwhelmed pipeline capacity. WTI traded at $15 to $25 discount to Brent. The Seaway pipeline reversal (2012) and subsequent capacity expansions gradually normalized the spread to $3 to $6.

**April 2020:** WTI went negative while Brent held above $20. The spread spiked to over $50 briefly. Cushing was nearly full, making WTI delivery mechanically impossible. This was an extreme [[Location Arbitrage]] dislocation.

**2022 to 2023:** Post Russia/Ukraine invasion, Brent spiked on seaborne supply fears while US supply was insulated. Spread widened to $8 to $10. Narrowed as markets adjusted to Russian oil rerouting to Asia.

## Concrete Example (Current or Recent)

Brent trades at $78. WTI trades at $74. The spread is $4 (Brent premium). The 12 month average is $3.50 with a standard deviation of $1.20. The current spread is 0.4 standard deviations above the mean, not yet a signal. If Cushing inventories report a surprise 5 million barrel build and the spread widens to $6.50 (2.5 sigma), you go long WTI / short Brent, expecting the spread to narrow back toward $3.50 to $4.00 as Cushing draws or exports increase. P&L target: $2 to $2.50 per barrel. Risk: spread widens further if Cushing continues building. Stop loss at $7.50 ($1 risk per barrel).

## Related Strategies
- [[Relative Value Trade]]
- [[Calendar Spread]]
- [[Location Arbitrage]]
- [[Crack Spread]]

## Related Concepts
- [[Contango]]
- [[Backwardation]]
- [[Storage Economics]]
- [[Convenience Yield]]
- [[Z-Score]]
- [[Mean Reversion]]
- [[Structural Break]]

---
*Status: #solid | Last reviewed: 2026-03-20*
