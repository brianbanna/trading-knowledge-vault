---
aliases: [seasonality, seasonal patterns, seasonal spread]
tags:
  - "#energy"
  - "#agri"
date-added: "2026-03-20"
---

# Seasonality

## Definition

Seasonality refers to recurring, predictable patterns in commodity prices and spreads that repeat at roughly the same time each year, driven by weather, agricultural cycles, consumer behavior, or industrial schedules. Unlike random price fluctuations, seasonal patterns have identifiable physical causes: heating demand rises in winter, gasoline demand peaks in summer, harvest pressure depresses grain prices in autumn. Seasonality is one of the most exploitable patterns in commodity markets because it is driven by physics and biology, not sentiment.

## Why it matters (commodities and FX)

Seasonal patterns are the baseline against which commodity traders measure "normal" vs "abnormal." A [[Calendar Spread]] that looks cheap might simply reflect the seasonal norm. A supply draw that looks bullish might be the standard winter pattern. Without seasonal context, you cannot distinguish a genuine signal from noise. Professional commodity desks maintain seasonal charts for every spread they trade and calibrate entries/exits relative to the seasonal average, not the absolute level. In FX, seasonality is weaker but exists in flows (year end repatriation, fiscal year patterns in JPY, EM current account cycles).

## Concrete example

**Natural gas (Henry Hub):** The classic seasonal commodity. Winter demand for heating creates a predictable price premium for winter months (Nov to Mar) vs shoulder months (Apr, Oct). The Oct/Mar spread (short Oct, long Mar) captures winter heating premium. Over the past 20 years, this spread has been positive approximately 85% of the time. A trader buys the winter/summer spread in early autumn when the seasonal premium begins to build, and exits by February.

**Gasoline (RBOB):** Demand peaks in US driving season (Memorial Day to Labor Day). Refinery turnaround season (Feb to Apr) reduces gasoline supply just as demand begins to ramp. The RBOB [[Crack Spread]] typically peaks in May to June. Traders go long the gasoline crack in March and exit by June.

**Soybeans:** US harvest pressure in September to November creates seasonal lows. South American harvest (Mar to May) creates a second supply wave. The Nov/Jul soybean spread captures old crop vs new crop dynamics.

## Key mechanics and formulas

**Seasonal index:**
`Seasonal Index(month) = Average price in month / Average annual price`

A seasonal index of 1.05 for March means prices in March are typically 5% above the annual average.

**Deseasonalized price:**
`Deseasonalized = Actual Price / Seasonal Index`

Used to strip seasonal effects and identify genuine supply/demand signals.

**Seasonal spread Z-score:**
`Z = (Current spread - Seasonal average for this date) / Seasonal standard deviation for this date`

This is the correct way to assess whether a spread is rich or cheap: compare it to where it usually is at the same point in the year, not to a flat annual average.

**Win rate and expectancy:**
For any seasonal trade: `Expected Value = (Win Rate x Avg Win) - (Loss Rate x Avg Loss)`. Most seasonal trades have win rates of 65 to 80% but require stop losses because the 20 to 35% of losing years can produce outsized losses (polar vortex blowing up a short natgas winter spread).

## Prerequisites
- [[Forward Curve]]
- [[Calendar Spread]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)
- [[Calendar Spread]] - the primary instrument for expressing seasonal views. Seasonal trades are almost always calendar spreads.
- [[Storage Economics]] - storage injection/withdrawal cycles are the physical mechanism behind energy seasonality.
- [[Convenience Yield]] - seasonal tightness drives convenience yield spikes, which drive calendar spread moves.
- [[Weather Risk]] - temperature drives natgas and power seasonality. Deviations from normal weather are the primary catalyst for seasonal trade P&L.
- [[Supply Shock]] - anti seasonal events (a hurricane in August disrupting refining, a drought during growing season) create the biggest trading opportunities.
- [[Mean Reversion]] - seasonal patterns are a form of mean reversion with a known time component.

## Common misconceptions

**"Seasonality is a guaranteed trade."** It is not. Seasonal patterns have high win rates but individual years can deviate sharply. A warm winter destroys the natgas seasonal. A bumper crop eliminates harvest pressure. Size for the loss scenario, not the average.

**"You can use the same seasonal window every year."** The timing shifts. Spring turnaround season might start 2 weeks early or late depending on refinery maintenance schedules. The seasonal is a guide, not a calendar alarm.

**"Seasonal patterns are arbed away."** They persist because they are driven by physical constraints (weather, crop biology, industrial scheduling) that cannot be arbitraged. The magnitude may compress as more participants trade them, but the direction persists.

## Sources

- Moore Research Center (MRCI): seasonal spread data and charts
- CME Group: Seasonal Patterns in Energy Markets
- Stein, Jonathan, "Seasonality in Commodity Markets" (various MRCI publications)
- EIA seasonal energy outlook reports
