---
aliases: [calendar spread, time spread, intra-commodity spread, horizontal spread]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-03-20"
---

# Calendar Spread

## Core Thesis

A calendar spread is a [[Relative Value Trade]] that buys one delivery month and sells a different delivery month of the same commodity. It isolates the shape of the [[Forward Curve]] as the trade variable and removes most directional price risk. The spread reflects changes in [[Convenience Yield]], [[Storage Economics]], supply/demand tightness, and [[Cost of Carry]]. Calendar spreads are the bread and butter of professional commodity trading.

## Mechanics

### Spread Convention
**Spread = Near month price minus Far month price.** Long calendar spread = long near, short far. Short calendar spread = the reverse. Steeper [[Backwardation]] = long spread profits. Curve flattens or moves into [[Contango]] = short spread profits.

### Entry Criteria
- Spread deviates from seasonal norm or historical mean
- Catalyst: inventory report, OPEC decision, weather (natgas), refinery turnaround schedule
- Term structure: [[Z-Score]] of spread vs rolling window exceeds 1.5 to 2.0
- Liquidity: both legs need volume and tight [[Bid-Ask Spread]]

### Exit Criteria
- Spread reverts to target level
- Catalyst resolves
- Approaching front month expiry (roll or close 5 to 10 days before LTD)
- Time stop or loss limit hit

### Position Sizing
Both legs are same contract size (1:1). Exchanges offer reduced margin for calendar spreads (CME, ICE) at 10 to 30% of outright. Size on spread ATR, not outright.

## Instruments Used
- Any commodity futures with multiple listed months
- Most liquid: [[WTI Crude Oil]] M1/M2 or M1/M6, [[Brent Crude]], [[Henry Hub Natural Gas]], [[Copper Futures]], [[Gold Futures]]
- CME and ICE list calendar spreads as tradeable instruments with their own order books

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Spread moves against you (unexpected inventory build while long the spread) |
| Max Loss Scenario | Structural shift in curve shape (pipeline reversal, storage capacity change, demand destruction) |
| Hedged Exposure | Directional price risk ~80 to 95% hedged |
| Unhedged Exposure | Curve shape risk, [[Convenience Yield]] shifts, roll timing |
| Margin Requirements | Reduced vs outright (10 to 30% of single leg margin) |

## Edge Source

Fundamental: inventory cycles, seasonal patterns, and storage economics are analyzable. Energy calendar spreads have strong seasonal components (winter/summer natgas, turnaround seasons in crude). Statistical: spread mean reversion is stronger than price mean reversion because physical arbitrage (cost of carry) bounds the spread in normal conditions.

## When It Works / When It Fails

### Works Well When
- Clear seasonal pattern (natgas winter/summer: buy Mar/Apr spread before winter heating demand)
- Inventory cycle turning points (draws starting after a build period)
- Stable regime (no structural shifts in production, storage, or logistics)

### Fails When
- [[Supply Shock]] overwhelms seasonal norms (outage, geopolitical event)
- [[Structural Break]] in the curve (storage capacity change, new pipeline)
- Forced liquidation by large players distorts spreads
- [[Liquidity]] dries up in one leg (deferred months can be illiquid)

## Historical Examples

**Natural Gas Winter/Summer:** The Mar to Apr Henry Hub spread (winter to shoulder season) is one of the most traded seasonal spreads. In a normal year March trades at a premium to April (heating demand). Traders go long in autumn before the seasonal is fully priced. Cold winter widens the spread further. Mild winter collapses it.

**Crude Oil Backwardation Trades (2022):** Post Russia/Ukraine, Brent went into extreme backwardation ($5+ M1 premium to M2). Long calendar spread profited heavily. Shorts expecting normalization were squeezed.

## Concrete Example (Current or Recent)

**Concrete:** [[Henry Hub Natural Gas]] Dec 2026 at $4.20. Mar 2027 at $3.80. Dec/Mar spread = +$0.40 (mild backwardation). Historical average at this time of year +$0.10, sigma $0.25. Current 1.2 sigma above mean. Warm winter forecast: short the spread (sell Dec, buy Mar). If spread narrows to $0.10 (mean), profit $0.30 x 10,000 MMBtu = $3,000 per spread. If polar vortex hits and Dec/Mar widens to $1.00, lose $0.60 x 10,000 = $6,000 per spread.

**Simplified:** Same commodity, 2 different months. The gap between them reflects storage costs and how tight supply is right now. You bet the gap will move (widen or narrow) without taking a view on whether prices go up or down. Lower margin than an outright bet because the 2 legs offset most of the directional risk.

## Related Strategies
- [[Relative Value Trade]]
- [[Brent-WTI Spread]]
- [[Inter-Commodity Spread]]
- [[Crack Spread]]
- [[Location Arbitrage]]

## Related Concepts
- [[Forward Curve]]
- [[Backwardation]]
- [[Contango]]
- [[Convenience Yield]]
- [[Roll Yield]]
- [[Cost of Carry]]
- [[Seasonality]]
- [[Z-Score]]
- [[Storage Economics]]

---
*Status: #solid | Last reviewed: 2026-03-20*
