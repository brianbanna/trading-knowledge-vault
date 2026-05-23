---
aliases: [Brent WTI spread, Brent WTI arb, transatlantic crude spread, BZ-CL spread]
tags:
  - "#energy/crude/brent"
  - "#energy/crude/wti"
date-added: "2026-03-20"
---

# Brent-WTI Spread

## Core Thesis

The Brent-WTI spread captures relative pricing between the world's 2 primary crude benchmarks. It reflects the cost of moving crude between the US Gulf Coast and global seaborne markets, US pipeline logistics to Cushing, Atlantic Basin supply/demand, and the structural difference between a landlocked benchmark (WTI/Cushing) and a seaborne one (Brent). The spread mean reverts around a level set by transportation economics. Regime shifts in infrastructure (pipelines, export terminals) permanently alter the equilibrium.

## Mechanics

### Entry Criteria
- Spread deviates from trailing 6 to 12 month mean (>1.5 [[Z-Score]])
- Identifiable catalyst: Cushing inventory build/draw, US export capacity change, OPEC action affecting seaborne crude
- Seasonal patterns: US refinery turnarounds widen the spread as Cushing builds

### Exit Criteria
- Spread reverts to mean or overshoots
- Catalyst resolves (Cushing draws normalize, pipeline constraints ease)
- Time stop: 4 to 6 weeks without movement, reassess

### Position Sizing
Both contracts are 1,000 barrels, spread trades 1:1. CME margin reduction for recognized spreads ~50 to 70%. Size on spread volatility, not outright crude vol.

## Instruments Used
- [[Brent Crude]] (ICE CO or CME BZ)
- [[WTI Crude Oil]] (NYMEX CL)

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | [[Structural Break]] in the spread relationship (infrastructure, policy) |
| Max Loss Scenario | Permanent regime shift (US export ban reimposed, Cushing bypass pipeline built) |
| Hedged Exposure | Directional crude price risk largely cancelled |
| Unhedged Exposure | Basis risk, logistics risk, quality differential changes |
| Margin Requirements | Reduced spread margin (CME inter commodity credit) |

## Edge Source

Structural: the spread is anchored by physical transportation costs, pipeline tariffs, and storage economics. These change slowly and predictably. Informational edge comes from tracking Cushing inventories (Genscape satellite data), tanker rates, pipeline flow data, and US export volumes in near real time.

## When It Works / When It Fails

### Works Well When
- Cushing inventories move toward extremes (very full = WTI weakens, spread widens; very empty = WTI strengthens, spread narrows)
- Clear seasonal patterns in US refinery runs
- Stable infrastructure regime

### Fails When
- Infrastructure regime shifts: the 2011 to 2014 WTI blowout discount ($20+) occurred because Cushing was oversupplied without enough pipeline capacity to the Gulf Coast. New pipelines (Seaway reversal, Keystone) permanently narrowed the spread.
- US export policy changes
- Geopolitical premium in Brent unrelated to Atlantic Basin logistics

## Historical Examples

**2011 to 2014:** Cushing glut from Bakken and Canadian production overwhelmed pipeline capacity. WTI traded at $15 to $25 discount to Brent. Seaway pipeline reversal (2012) and subsequent expansions normalized the spread to $3 to $6.

**April 2020:** WTI went negative while Brent held above $20. Spread spiked above $50 briefly. Cushing was nearly full, making WTI delivery mechanically impossible. Extreme [[Location Arbitrage]] dislocation.

**2022 to 2023:** Post Russia/Ukraine, Brent spiked on seaborne supply fears while US supply was insulated. Spread widened to $8 to $10. Narrowed as Russian oil rerouted to Asia.

## Concrete Example (Current or Recent)

**Concrete:** Brent at $78. WTI at $74. Spread = $4 (Brent premium). 12 month average $3.50, sigma $1.20. Current spread is 0.4 sigma above mean, not yet a signal. If Cushing inventories surprise +5 mb and the spread widens to $6.50 (2.5 sigma), go long WTI / short Brent, expecting reversion toward $3.50 to $4.00 as Cushing draws or exports rise. P&L target: $2 to $2.50 per barrel. Risk: spread widens if Cushing keeps building. Stop loss at $7.50 ($1 risk per barrel).

**Simplified:** Same product (crude), 2 locations. One inland (WTI at Cushing), one seaborne (Brent). The price gap pays for shipping, pipelines, and quality differences. When the gap stretches too far, traders move barrels until it closes. The trade: bet the gap reverts when it gets stretched.

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
