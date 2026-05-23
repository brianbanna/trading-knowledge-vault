---
aliases: [seasonality, seasonal patterns, seasonal spread]
tags:
  - "#energy"
  - "#agri"
date-added: "2026-03-20"
---

# Seasonality

## Definition

Seasonality refers to recurring, predictable patterns in commodity prices and spreads that repeat at roughly the same time each year, driven by weather, agricultural cycles, consumer behavior, or industrial schedules. Unlike random fluctuations, seasonal patterns have identifiable physical causes: heating demand rises in winter, gasoline peaks in summer, harvest depresses grain prices in autumn. Seasonality is one of the most exploitable patterns in commodities because it is driven by physics and biology, not sentiment.

## Why it matters (commodities and FX)

Seasonal patterns are the baseline against which commodity traders measure normal versus abnormal. A [[Calendar Spread]] that looks cheap may reflect the seasonal norm. A supply draw that looks bullish may be the standard winter pattern. Without seasonal context, signal cannot be distinguished from noise. Professional desks maintain seasonal charts for every spread and calibrate entries/exits relative to the seasonal average, not the absolute level. FX seasonality is weaker but exists in flows (year end repatriation, fiscal year patterns in JPY, EM current account cycles).

## Concrete example

**Concrete:** Natural gas Oct/Mar spread. Trader puts on long Mar, short Oct in early September at +$0.85/MMBtu (winter premium). Over 20 years this spread has been positive about 85% of the time, averaging +$1.20 by January as winter demand approaches. By late November, NOAA outlook turns colder than normal, spread runs to +$1.45. Trader exits at +$1.40, gaining $0.55/MMBtu on 50 contracts = $275,000. Reverse case: warm winter 2011/12, spread collapsed from +$1.10 to +$0.20, killing seasonal longs.

**Simplified:** Some commodities have demand patterns that repeat every year. Winter needs heat, summer needs gasoline, autumn means crops getting harvested. These patterns show up in spreads between contract months. You buy the spread before the seasonal pressure hits and exit when the pattern plays out. It works most years because the cause is physical. It fails in years when weather or supply deviates from the norm.

## Key mechanics and formulas

**Seasonal index:**
`Seasonal Index(month) = Average price in month / Average annual price`

A seasonal index of 1.05 for March means March prices average 5% above the annual average.

**Deseasonalized price:**
`Deseasonalized = Actual Price / Seasonal Index`

Strips seasonal effects to identify genuine supply/demand signals.

**Seasonal spread Z-score:**
`Z = (Current spread - Seasonal average for this date) / Seasonal standard deviation for this date`

The correct way to assess whether a spread is rich or cheap: compare to where it usually is at the same point in the year, not to a flat annual average.

**Win rate and expectancy:**
`Expected Value = (Win Rate x Avg Win) - (Loss Rate x Avg Loss)`. Seasonal trades have 65 to 80% win rates but require stops because losing years produce outsized losses (polar vortex blowing up a short natgas winter spread).

## Prerequisites
- [[Forward Curve]]
- [[Calendar Spread]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)
- [[Calendar Spread]] - primary instrument for expressing seasonal views. Seasonal trades are almost always calendar spreads.
- [[Storage Economics]] - storage injection/withdrawal cycles are the physical mechanism behind energy seasonality.
- [[Convenience Yield]] - seasonal tightness drives convenience yield spikes, which drive calendar spread moves.
- [[Weather Risk]] - temperature drives natgas and power seasonality. Deviations from normal weather are the primary catalyst for seasonal P&L.
- [[Supply Shock]] - anti seasonal events (August hurricane disrupting refining, drought during growing season) create the biggest opportunities.
- [[Mean Reversion]] - seasonal patterns are a form of mean reversion with a known time component.

## Common misconceptions

**"Seasonality is a guaranteed trade."** Not guaranteed. High win rates, but individual years deviate sharply. A warm winter kills the natgas seasonal. A bumper crop eliminates harvest pressure. Size for the loss scenario.

**"Use the same seasonal window every year."** Timing shifts. Spring turnaround season can start 2 weeks early or late depending on refinery maintenance schedules. The seasonal is a guide, not a calendar alarm.

**"Seasonal patterns are arbed away."** They persist because they are driven by physical constraints that cannot be arbitraged. Magnitude may compress as more participants trade them, direction persists.

## Sources

- Moore Research Center (MRCI): seasonal spread data and charts
- CME Group: Seasonal Patterns in Energy Markets
- Stein, Jonathan, "Seasonality in Commodity Markets" (various MRCI publications)
- EIA seasonal energy outlook reports
