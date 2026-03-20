---
aliases: [calendar spread, time spread, intra-commodity spread, horizontal spread]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-03-20"
---

# Calendar Spread

## Core Thesis

A calendar spread is a [[Relative Value Trade]] that buys one delivery month and sells a different delivery month of the same commodity. It isolates the shape of the [[Forward Curve]] as the trade variable, removing most directional price risk. The spread reflects changes in [[Convenience Yield]], [[Storage Economics]], supply/demand tightness, and [[Cost of Carry]]. Calendar spreads are the bread and butter of professional commodity trading.

## Mechanics

### Spread Convention
The standard convention is: **Spread = Near month price minus Far month price.** A "long" calendar spread means long the near month, short the far month. A "short" calendar spread is the reverse. When the curve moves into steeper [[Backwardation]], a long calendar spread profits. When the curve flattens or moves into [[Contango]], a short calendar spread profits.

### Entry Criteria
- Spread deviates from seasonal norm or historical mean
- Fundamental catalyst: inventory report, OPEC decision, weather event (natgas), refinery turnaround schedule
- Term structure signal: [[Z-Score]] of spread vs rolling window exceeds 1.5 to 2.0
- Liquidity: ensure both legs have adequate volume and tight [[Bid-Ask Spread]]

### Exit Criteria
- Spread reverts to target level
- Fundamental catalyst resolves
- Approaching front month expiry (roll or close 5 to 10 days before last trading day)
- Time stop or loss limit hit

### Position Sizing
Both legs are the same contract size (1:1 ratio). Exchanges offer reduced margin for calendar spreads (CME, ICE). Spread margin is typically 10 to 30% of outright margin. Size based on spread volatility (ATR of the spread, not the outright).

## Instruments Used
- Any commodity futures with multiple listed months
- Most liquid: [[WTI Crude Oil]] M1/M2 or M1/M6, [[Brent Crude]], [[Henry Hub Natural Gas]], [[Copper Futures]], [[Gold Futures]]
- CME and ICE list calendar spreads as tradeable instruments with their own order books

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Spread moves against you (e.g., unexpected inventory build while long the spread) |
| Max Loss Scenario | Structural shift in curve shape (pipeline reversal, storage capacity change, demand destruction) |
| Hedged Exposure | Directional price risk ~80 to 95% hedged (spread legs move together) |
| Unhedged Exposure | Curve shape risk, [[Convenience Yield]] shifts, roll timing |
| Margin Requirements | Significantly reduced vs outright (10 to 30% of single leg margin) |

## Edge Source

Fundamental: inventory cycles, seasonal patterns, and storage economics are analyzable and somewhat predictable. Calendar spreads in energy have strong seasonal components (winter/summer natgas, turnaround seasons in crude). Statistical: spread mean reversion is stronger than price mean reversion because the spread is bounded by physical arbitrage (cost of carry sets a floor and ceiling in normal conditions).

## When It Works / When It Fails

### Works Well When
- Clear seasonal pattern (natgas winter/summer: buy the Mar/Apr spread before winter heating demand)
- Inventory cycle turning points (draws starting after a build period)
- Regime is stable (no structural shifts in production, storage, or logistics)

### Fails When
- [[Supply Shock]] overwhelms seasonal norms (unexpected outage, geopolitical event)
- [[Structural Break]] in the curve (e.g., permanent shift in storage capacity, new pipeline)
- Forced liquidation by large players distorts spreads temporarily
- [[Liquidity]] dries up in one leg (deferred months can be illiquid)

## Historical Examples

**Natural Gas Winter/Summer:** The Mar to Apr Henry Hub spread (crossing winter to shoulder season) is one of the most traded seasonal spreads. In a normal year, March trades at a significant premium to April (heating demand). Traders go long this spread in autumn when the seasonal is not yet fully priced. If winter is colder than expected, the spread widens further. If winter is mild, the spread can collapse.

**Crude Oil Backwardation Trades (2022):** Following the Russia/Ukraine invasion, Brent went into extreme backwardation ($5+ M1 premium to M2). Traders who were long the calendar spread profited massively. Those who shorted the spread expecting normalization were squeezed.

## Concrete Example (Current or Recent)

[[Henry Hub Natural Gas]] Dec 2026 trades at $4.20. Mar 2027 trades at $3.80. The Dec/Mar spread is +$0.40 (Dec premium, mild backwardation). Historically, this spread averages +$0.10 at this time of year with a standard deviation of $0.25. The current level is 1.2 sigma above the mean. If you believe winter demand is overpriced (warm winter forecast), you short the spread: sell Dec, buy Mar. If the spread narrows to $0.10 (mean), you earn $0.30 x 10,000 MMBtu = $3,000 per spread. If instead a polar vortex hits and Dec/Mar widens to $1.00, you lose $0.60 x 10,000 = $6,000 per spread. Risk/reward analysis and position sizing are essential.

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
