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

A position that profits from a change in the price relationship between 2 or more related instruments, rather than from the outright directional move of any single one. You are not betting something goes up or down. You are betting the spread, ratio, or differential between 2 things moves in a specific direction.

The core logic: if 2 assets are fundamentally linked (same commodity at different delivery dates, same commodity at different locations, 2 correlated currencies), temporary mispricings should revert or move toward a predicted relationship. The trader captures that convergence or divergence.

## Why It Matters (Commodities / FX)

This is arguably the most important concept in commodities trading. Most professional commodity traders do not take naked directional bets. They trade spreads. The reason: commodity prices are driven by supply, demand, storage, and transportation economics, and these forces show up as relationships between contracts, not as absolute price levels.

In FX, relative value drives [[FX Carry Trade|carry trades]], cross rate arbitrage, and EM vs DM positioning. Central bank policy divergence is fundamentally a relative value thesis.

Relative value trades are naturally partially hedged. If you are long Dec Brent and short Mar Brent, a broad oil selloff hurts both legs. Your P&L depends primarily on the spread, not the direction. This makes risk more manageable but does not eliminate it.

## Concrete Example

**Commodity Calendar Spread:** Buy Dec 2026 [[Brent Crude]], sell Mar 2027 Brent. You are trading the shape of the [[Forward Curve]]. If near term supply tightens, Dec strengthens vs Mar ([[Backwardation]] deepens). P&L depends on the spread, not whether oil goes to 90 or 60.

**Location Spread:** Buy [[TTF Natural Gas]] (Europe), sell [[Henry Hub Natural Gas]] (US). You are trading the transatlantic gas differential. This reflects LNG shipping costs, European storage levels, and supply disruption risk.

**Inter Product Spread:** Buy crude oil, sell gasoline and heating oil ([[Crack Spread]]). Replicates refinery margins. Not a bet on oil direction but on refining economics.

**FX Relative Value:** Long AUD/USD, short EUR/USD (net long AUD/EUR). Expresses a view that Australian rates relative to European rates make AUD more attractive.

**Cross Commodity:** Long [[Copper Futures]], short [[Aluminum Futures]]. Both base metals, but copper is more sensitive to construction/electrical demand, aluminum more energy intensive to produce. Trading relative demand dynamics.

## Prerequisites

- [[Futures Contract Mechanics]]
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Basis]]
- [[Correlation]]

## Related Concepts (Learn Next)

- [[Cointegration]] - statistical test for whether 2 prices maintain a long run equilibrium. Formalizes relative value signals quantitatively.
- [[Roll Yield]] - P&L from rolling futures forward. Critical for calendar spread economics beyond just spread direction.
- [[Basis Risk]] - risk that the spread does not converge as expected. The primary risk in any relative value trade.
- [[Pairs Trading]] - systematic/quantitative implementation of relative value in equities.
- [[Spread Margin]] - exchanges offer reduced margin for recognized spreads. Affects capital efficiency.
- [[Convenience Yield]] - the benefit of holding physical commodity vs futures. Drives backwardation and calendar spread behavior.
- [[Cost of Carry Model]] - the theoretical framework linking spot, futures, storage, and interest rates.

## Key Mechanics / Formulas

**Spread P&L:** `P&L = (Spread at exit) - (Spread at entry) x contract multiplier x number of spreads`

**Calendar Spread:** `Spread = Front month price - Back month price` (convention varies by market)

**Location Spread:** `Spread = Location A price - Location B price`

**Spread ratio (for different sized contracts):** When contract sizes differ, you need a hedge ratio. Example: if trading WTI vs Brent and contract sizes are both 1000 barrels, the ratio is 1:1. If contract sizes differ, adjust by `(Contract size A / Contract size B) x (beta or hedge ratio)`.

## Common Misconceptions

**"Relative value trades are low risk."** They are lower directional risk. Spread risk can be severe. LTCM blew up on relative value trades when spreads widened far beyond historical norms.

**"If 2 things are correlated, the spread always reverts."** [[Correlation]] is not [[Cointegration]]. 2 assets can be highly correlated but diverge permanently due to structural changes.

**"You do not need to understand the outright market."** You do. A relative value trade still has legs individually affected by market events. Understanding outright context helps anticipate when spreads will move.

**"Calendar spreads are only about supply and demand."** They are also about interest rates ([[Cost of Carry Model|cost of carry]]), storage costs, and [[Convenience Yield]]. The full cost of carry model is required.

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
