---
aliases: [soybean corn ratio, bean corn spread, corn soy ratio, acreage battle, planting ratio]
tags:
  - "#agri/oilseeds/soybeans"
  - "#agri/grains/corn"
date-added: "2026-03-24"
---

# Soybean-Corn Spread

## Core Thesis

The Soybean-Corn spread trades the price ratio between the 2 crops that compete for the same US Midwest farmland. Every spring, American farmers look at the price of soybeans vs corn and decide which to plant. Soybeans expensive relative to corn = more acres to beans. Corn expensive = more acres to corn. The planting decision affects supply 6 months later, pushing the ratio back toward equilibrium. This biological arbitrage makes the soybean-corn ratio one of the most reliably mean reverting spreads in commodities.

Traditionally expressed as soybeans / corn. Long run average ~2.4:1. Ratio >2.5: farmers plant more soybeans. Ratio <2.2: more corn. Thresholds shift modestly over time with input costs and yields, but the mechanism is consistent.

## Mechanics

### Calculating the Ratio

**Soybean-Corn Ratio = Soybean price (cents/bushel) / Corn price (cents/bushel)**

Example: Soybeans at $12.50/bu (1250 cents), corn at $4.80/bu (480 cents). Ratio = 2.60.

Both on CBOT. Soybean contract (ZS) = 5,000 bushels. Corn contract (ZC) = 5,000 bushels.

### Entry Criteria
- Ratio deviates from 2.4 by more than 0.3 (above 2.7 or below 2.1)
- Timing matters: works best entered before or during the US planting window (March to May), because acreage response drives convergence
- USDA Prospective Plantings report (late March) as a catalyst
- [[WASDE]] supply/demand balance for both crops

### Exit Criteria
- Ratio reverts to 2.3 to 2.5 range
- After planting decisions lock in (June), ratio is driven by growing season weather, not acreage substitution. Mean reversion anchor weakens.
- Time stop: if not converging by July, reassess

### Position Sizing
Both contracts 5,000 bushels. 1:1 bushel neutral spread: buy 1 ZS, sell 1 ZC. Not dollar neutral. At $12.50/bu soybeans ($62,500) vs $4.80/bu corn ($24,000), dollar neutral ~1 ZS : 2.6 ZC. Most traders use 1:1 because the acreage substitution mechanism operates per bushel, not per dollar.

## Instruments Used
- Soybean Futures CBOT (ZS), 5,000 bushels
- Corn Futures CBOT (ZC), 5,000 bushels
- New crop months (November soybeans, December corn) for planting decision trades
- Old crop months for current supply/demand trades

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Growing season weather overriding the acreage signal (corn belt drought moves either crop 30%+) |
| Max Loss Scenario | Severe weather event affecting one crop catastrophically (2012 corn drought pushed corn to $8/bu) |
| Hedged Exposure | General grain direction partially hedged |
| Unhedged Exposure | Weather risk, export demand shocks (China soybean buying), ethanol mandate changes (corn), basis risk |
| Margin Requirements | CME recognized spread, margin reduction ~50 to 70% |

## Edge Source

Biological arbitrage anchors the spread: farmers physically switch acres, creating a supply response 6 months after the price signal. The most predictable arbitrage mechanism in agriculture. Edge comes from understanding the USDA Prospective Plantings survey methodology, tracking real time planting progress via USDA weekly crop progress reports, and modeling input cost economics (seed, fertilizer, herbicide). Corn is more input intensive (nitrogen fertilizer): when fertilizer prices spike, breakeven shifts toward soybeans.

Strong [[Seasonality]]: ratio widens (soybeans outperform) from October to February as South American crop uncertainty builds, then narrows from March to June as US planting resolves.

## When It Works / When It Fails

### Works Well When
- Ratio reaches extreme levels before the US planting window (Feb to Apr)
- USDA Prospective Plantings confirms the expected acreage shift
- Normal growing season weather allows planted acres to translate into expected production
- Input cost differentials reinforce the acreage signal

### Fails When
- Growing season weather dominates: drought reverses 6 months of acreage based positioning in 2 weeks
- China demand shock: sudden large Chinese soybean purchase (or cancellation) moves soybeans 5%+ in a week regardless of the ratio
- Ethanol mandate changes: corn is 35 to 40% used for ethanol. Policy change structurally shifts corn demand independent of acres
- South American production surprise: a large Brazilian soybean crop overwhelms US acreage response

## Historical Examples

**2012 US Drought:** Corn surged from $5.50 to $8.30/bu as the worst drought in decades hit the Corn Belt. Soybeans also rose but less (to $17/bu). Ratio compressed to 2.0x. Traders long the ratio (long soybeans, short corn) expecting reversion from 2.5x got hurt as corn's drought premium dominated.

**2020 to 2021 China Demand Surge:** Chinese soybean imports surged post COVID as hog herd rebuilding drove demand. Soybeans went from $8.50 to $16. Corn also rallied (ethanol recovery, China corn imports) but ratio widened to 2.8x. The 2021 US planting response (record soybean acres) brought the ratio back toward 2.4x by late 2021.

**Spring 2023:** Ratio at 2.25 in March suggested corn was relatively expensive. USDA Prospective Plantings showed a shift to more corn acres. By harvest, the large corn crop pushed corn lower and the ratio widened to 2.6x. Textbook acreage response trade.

## Concrete Example (Current or Recent)

**Concrete:** November soybeans (new crop) at $11.80/bu. December corn (new crop) at $4.60/bu. Ratio = 2.57. Modestly above 2.4 equilibrium, soybeans slightly expensive vs corn. USDA Prospective Plantings in 1 week. Expecting a shift to more soybean acres (confirming the price signal). Sell the spread: sell 1 November ZS at $11.80, buy 1 December ZC at $4.60. Target: ratio compresses to 2.35. If soybeans fall to $11.00 and corn holds at $4.60 (ratio = 2.39), P&L = $0.80 x 5,000 = $4,000 profit on ZS short, corn flat = net $4,000. Risk: Brazilian crop scare pushes soybeans to $13 while corn stays at $4.60 (ratio = 2.83). Loss = $1.20 x 5,000 = $6,000. Stop loss at ratio 2.75.

**Simplified:** Two crops compete for the same Midwest acres. If one gets relatively expensive, farmers plant more of it. 6 months later that planting hits the market as supply, and the price comes back down. Trade the ratio when it stretches before planting (Feb to Apr), bet on the supply response. Skip the trade once planting locks in: weather drives prices, not acres.

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
