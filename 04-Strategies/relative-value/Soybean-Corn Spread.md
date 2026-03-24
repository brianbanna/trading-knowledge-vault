---
aliases: [soybean corn ratio, bean corn spread, corn soy ratio, acreage battle, planting ratio]
tags:
  - "#agri/oilseeds/soybeans"
  - "#agri/grains/corn"
date-added: "2026-03-24"
---

# Soybean-Corn Spread

## Core Thesis

The Soybean-Corn spread trades the price ratio between the 2 crops that compete for the same farmland in the US Midwest. Think of it as trading the farmer's planting decision. Every spring, millions of American farmers look at the price of soybeans vs corn and decide which to plant on their acres. If soybeans are expensive relative to corn, more acres go to beans. If corn is expensive, more acres go to corn. This planting decision then affects supply 6 months later, which pushes the ratio back toward equilibrium. This biological arbitrage mechanism makes the soybean-corn ratio one of the most reliably mean reverting spreads in all of commodities.

The ratio is traditionally expressed as soybeans / corn. The long run average is approximately 2.4:1. When the ratio exceeds 2.5, farmers plant more soybeans. When it drops below 2.2, they plant more corn. These thresholds shift modestly over time with input costs and yields, but the mechanism is remarkably consistent.

## Mechanics

### Calculating the Ratio

**Soybean-Corn Ratio = Soybean price (cents/bushel) / Corn price (cents/bushel)**

Example: Soybeans at $12.50/bu (1250 cents), corn at $4.80/bu (480 cents). Ratio = 1250 / 480 = 2.60.

Both trade on CBOT. Soybean contract (ZS) = 5,000 bushels. Corn contract (ZC) = 5,000 bushels. Same contract size simplifies the spread.

### Entry Criteria
- Ratio deviates from 2.4 by more than 0.3 (above 2.7 or below 2.1)
- Timing matters enormously: the trade works best when entered before or during the US planting window (March to May), because the acreage response is the mechanism that drives convergence
- USDA Prospective Plantings report (late March) as a catalyst
- [[WASDE]] supply/demand balance for both crops

### Exit Criteria
- Ratio reverts to 2.3 to 2.5 range
- After planting decisions are locked in (June), the ratio is driven by growing season weather, not acreage substitution. The mean reversion anchor weakens.
- Time stop: if not converging by July, reassess

### Position Sizing
Both contracts are 5,000 bushels. For a 1:1 bushel neutral spread: buy 1 ZS, sell 1 ZC. However, this is not dollar neutral. At $12.50/bu soybeans ($62,500 contract) vs $4.80/bu corn ($24,000 contract), a dollar neutral ratio is approximately 1 ZS : 2.6 ZC. In practice, most traders use 1:1 (bushel neutral) because the acreage substitution mechanism operates per bushel, not per dollar.

## Instruments Used
- Soybean Futures CBOT (ZS), 5,000 bushels
- Corn Futures CBOT (ZC), 5,000 bushels
- New crop months (November soybeans, December corn) for planting decision trades
- Old crop months for current supply/demand trades

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Growing season weather overriding the acreage signal (drought in corn belt can move either crop 30%+) |
| Max Loss Scenario | Severe weather event that affects one crop catastrophically (2012 corn drought pushed corn to $8/bu) |
| Hedged Exposure | General grain direction partially hedged |
| Unhedged Exposure | Weather risk, export demand shocks (China soybean buying), ethanol mandate changes (corn), basis risk |
| Margin Requirements | CME recognized spread, margin reduction approximately 50 to 70% |

## Edge Source

The biological arbitrage is the anchor: farmers physically switch acres, creating a supply response 6 months after the price signal. This is the single most predictable arbitrage mechanism in agriculture. Edge comes from understanding the USDA Prospective Plantings survey methodology, tracking real time planting progress via USDA weekly crop progress reports, and modeling input cost economics (seed, fertilizer, herbicide costs differ between corn and soybeans). Corn is more input intensive (requires more nitrogen fertilizer), so when fertilizer prices spike, the breakeven shifts in favor of soybeans.

The trade has strong [[Seasonality]]: the ratio tends to widen (soybeans outperform) from October to February as South American crop uncertainty builds, then narrow from March to June as US planting resolves.

## When It Works / When It Fails

### Works Well When
- Ratio reaches extreme levels before the US planting window (Feb to Apr)
- USDA Prospective Plantings confirms the expected acreage shift
- Normal growing season weather allows planted acres to translate into expected production
- Input cost differentials reinforce the acreage signal

### Fails When
- Growing season weather dominates: a drought can reverse 6 months of acreage based positioning in 2 weeks
- China demand shock: a sudden large Chinese soybean purchase (or cancellation) can move soybeans 5%+ in a week regardless of the ratio
- Ethanol mandate changes: corn is 35 to 40% used for ethanol. A policy change can structurally shift corn demand independent of acres
- South American production surprise: a large Brazilian soybean crop can overwhelm US acreage response

## Historical Examples

**2012 US Drought:** Corn prices surged from $5.50 to $8.30/bu as the worst drought in decades hit the Corn Belt. Soybeans also rose but less dramatically (to $17/bu). The ratio compressed to 2.0x. Traders who were long the ratio (long soybeans, short corn) expecting mean reversion from 2.5x got hurt as corn's drought premium dominated.

**2020 to 2021 China Demand Surge:** Chinese soybean imports surged post COVID as hog herd rebuilding drove demand. Soybeans went from $8.50 to $16. Corn also rallied (ethanol recovery, China corn imports) but the ratio widened to 2.8x. The subsequent US planting response in 2021 (record soybean acres) brought the ratio back toward 2.4x by late 2021.

**Spring 2023:** Ratio at 2.25 in March suggested corn was relatively expensive. USDA Prospective Plantings showed a shift to more corn acres. By harvest, the large corn crop pushed corn prices lower and the ratio widened to 2.6x. Textbook acreage response trade.

## Concrete Example (Current or Recent)

November soybeans (new crop) at $11.80/bu. December corn (new crop) at $4.60/bu. Ratio = 2.57. This is modestly above the 2.4 equilibrium, suggesting soybeans are slightly expensive relative to corn. The USDA Prospective Plantings report is in 1 week.

If you expect the report to show a shift toward more soybean acres (confirming the price signal), the resulting supply increase will eventually compress the ratio. You sell the spread: sell 1 November ZS at $11.80, buy 1 December ZC at $4.60. Target: ratio compresses to 2.35. If soybeans fall to $11.00 and corn holds at $4.60 (ratio = 2.39), P&L = ($11.80 - $11.00) x 5,000 = $4,000 profit on ZS short, corn flat = net $4,000. Risk: a Brazilian crop scare pushes soybeans to $13 while corn stays at $4.60 (ratio = 2.83). Loss = ($13.00 - $11.80) x 5,000 = $6,000. Stop loss at ratio 2.75.

## Related Strategies
- [[Inter-Commodity Spread]]
- [[Crush Spread]] (downstream soybean processing spread)
- [[Relative Value Trade]]
- [[Calendar Spread]]

## Related Concepts
- [[Seasonality]]
- [[Stocks to Use Ratio]]
- [[Old Crop New Crop]]
- [[WASDE]]
- [[Mean Reversion]]
- [[Z-Score]]
- [[Crop Year]]

---
*Status: #solid | Last reviewed: 2026-03-24*
