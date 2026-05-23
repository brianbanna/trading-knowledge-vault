---
aliases: [rel val, relative value, RV trade, spread trade]
tags:
  - "#energy/crude"
  - "#energy/natgas"
  - "#fx/g10"
date-added: "2026-03-20"
---

# Relative Value Trade

## Definition

A position that profits from a change in the price relationship between 2 or more related instruments, not from the outright direction of any single one. You bet that the spread, ratio, or differential moves, not that something goes up or down.

Core logic: if 2 assets are fundamentally linked (same commodity at different delivery dates, same commodity at different locations, 2 correlated currencies), temporary mispricings should revert or move toward a predicted relationship. The trader captures convergence or divergence.

## Why It Matters (Commodities / FX)

The most important concept in commodities trading. Most professional commodity traders do not take naked directional bets. They trade spreads. Commodity prices are driven by supply, demand, storage, and transportation economics, which show up as relationships between contracts, not absolute price levels.

In FX, relative value drives [[FX Carry Trade|carry trades]], cross rate arbitrage, and EM vs DM positioning. Central bank policy divergence is a relative value thesis.

Relative value trades are partially hedged. Long Dec Brent, short Mar Brent: a broad oil selloff hurts both legs. P&L depends on the spread, not direction. Risk is more manageable, not eliminated.

## Concrete Example

**Concrete:** Buy Dec 2026 [[Brent Crude]] at $78, sell Mar 2027 Brent at $77, paying $1 for the calendar spread. OPEC+ cuts and Cushing draws push the front. Dec runs to $81, Mar to $78.50. Spread widens to $2.50, earning $1.50/bbl on 100 lots = $150,000. Flat price view irrelevant: oil could have moved either direction. The spread captures shape of the [[Forward Curve]], not level.

**Simplified:** Two related contracts (different months, different locations, different currencies) usually move together. When they drift apart for a temporary reason, you bet they reconverge. You long the cheap one, short the rich one, and you do not care if the whole market rallies or sells off, only whether the gap closes. Smaller P&L per move, but smaller risk too.

## Prerequisites

- [[Futures Contract Mechanics]]
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Basis]]
- [[Correlation]]

## Related Concepts (Learn Next)

- [[Cointegration]] - statistical test for whether 2 prices maintain a long run equilibrium. Formalizes relative value signals.
- [[Roll Yield]] - P&L from rolling futures forward. Critical for calendar spread economics.
- [[Basis Risk]] - risk the spread does not converge. Primary risk in any relative value trade.
- [[Pairs Trading]] - systematic implementation in equities.
- [[Spread Margin]] - exchanges offer reduced margin for recognized spreads.
- [[Convenience Yield]] - drives backwardation and calendar spread behavior.
- [[Cost of Carry Model]] - theoretical framework linking spot, futures, storage, and rates.

## Key Mechanics / Formulas

**Spread P&L:** `P&L = (Spread at exit) - (Spread at entry) x contract multiplier x number of spreads`

**Calendar Spread:** `Spread = Front month price - Back month price` (convention varies by market)

**Location Spread:** `Spread = Location A price - Location B price`

**Spread ratio:** When contract sizes differ, adjust by `(Contract size A / Contract size B) x (beta or hedge ratio)`. WTI vs Brent: both 1,000 barrels, ratio 1:1.

## Common Misconceptions

**"Relative value trades are low risk."** Lower directional risk. Spread risk can be severe. LTCM blew up on relative value when spreads widened beyond historical norms.

**"If 2 things are correlated, the spread always reverts."** [[Correlation]] is not [[Cointegration]]. 2 assets can be highly correlated but diverge permanently due to structural change.

**"You do not need to understand the outright market."** You do. Each leg is affected by market events. Outright context anticipates spread moves.

**"Calendar spreads are only supply and demand."** They also reflect rates ([[Cost of Carry Model|cost of carry]]), storage, and [[Convenience Yield]]. Full carry model required.

## Sources

- CME Group: Introduction to Spread Trading
- Trading and Exchanges (Larry Harris), Chapter on spread trading
- First encountered while researching commodity trading strategies

## Course Module Mapping

- Primary: Module 7.2 (Mean Reversion Strategies), Module 19.1 (Commodity Market Structure)
- Secondary: Module 2.3 (Futures and Forwards), Module 9.1 (Position Sizing), Module 11.2 (Time Series Analysis)
- Advanced: Module 12.1 (Backtesting Framework) for systematic relative value

---
*Status: #solid | Last reviewed: 2026-03-20*
