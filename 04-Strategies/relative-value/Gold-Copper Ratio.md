---
aliases: [gold copper ratio, gold vs copper, copper gold ratio, Dr Copper vs gold, macro risk ratio]
tags:
  - "#metals/precious/gold"
  - "#metals/base/copper"
  - "#macro"
date-added: "2026-03-24"
---

# Gold-Copper Ratio

## Core Thesis

The Gold-Copper ratio divides the price of gold by the price of copper to produce a single number that captures the market's view on global growth vs fear. Think of it as a tug of war between 2 metals with opposite personalities. Gold is the ultimate safe haven, rising when people are scared, when real interest rates fall, and when central banks ease. Copper is "Dr Copper," the metal with a PhD in economics, rising when construction booms, manufacturing expands, and China is growing. A rising ratio means fear is winning (gold up, copper down). A falling ratio means optimism is winning (copper up, gold flat or lagging). Trading this ratio lets you express a macro view while hedging out the general "metals going up or down" component.

## Mechanics

### Calculating the Ratio

**Gold-Copper Ratio = Gold price ($/oz) / Copper price ($/lb)**

Example: Gold at $2,300/oz, copper at $4.20/lb. Ratio = 2,300 / 4.20 = 548.

For exchange traded futures: COMEX gold (GC, 100 troy oz) vs COMEX copper (HG, 25,000 lbs). The ratio is commonly expressed using spot prices in $/oz and $/lb.

Historical range: roughly 300 to 800 over the past 20 years. Average around 450 to 550. The ratio spiked to 750+ during COVID (March 2020) and dropped to 350 during the China infrastructure boom (2006, 2011).

### Entry Criteria
- Ratio deviates from its 2 year mean by more than 1.5 [[Z-Score|standard deviations]]
- Macro catalyst aligning with the trade: if ratio is extremely high (>700), you need to believe growth is about to recover (China stimulus, rate cuts lifting manufacturing). If extremely low (<350), you need to believe risk off is coming.
- Confirmation from related indicators: ISM Manufacturing, China PMI, [[TIPS Breakeven|breakevens]], credit spreads

### Exit Criteria
- Ratio reverts to mean or overshoots
- Macro thesis invalidated (e.g., you expected recovery but PMI keeps falling)
- Time stop: macro mean reversion can take months. 8 to 12 week minimum holding period is common.

### Position Sizing
Dollar neutral: match notional value of both legs. GC contract = 100 oz x $2,300 = $230,000. HG contract = 25,000 lbs x $4.20 = $105,000. So approximately 1 GC : 2 HG for dollar neutral. Margin is reduced on COMEX for recognized inter commodity spreads.

## Instruments Used
- [[Gold Futures]] COMEX (GC)
- [[Copper Futures]] COMEX (HG) or LME copper
- ETFs as proxy: GLD vs COPX or similar (less precise, no leverage)

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Macro regime persists longer than expected (growth stays weak or strong for years) |
| Max Loss Scenario | [[Structural Break]] in the relationship: gold reprices permanently higher on central bank buying while copper demand structurally declines, or vice versa |
| Hedged Exposure | General metals direction partially cancelled |
| Unhedged Exposure | Macro regime risk, China specific demand shocks, central bank gold policy, supply disruptions in either metal |
| Margin Requirements | COMEX inter commodity spread credit available |

## Edge Source

This is a macro expression trade, not a fundamental commodity trade. Edge comes from macro analysis: reading the global growth cycle, understanding China's credit impulse (copper demand), and central bank policy trajectory (gold). The ratio correlates strongly with the ISM Manufacturing PMI, the US 10 year yield, and China's credit impulse. Traders who can time cyclical turns have an edge. The physical anchoring is weaker than in processing spreads (gold and copper have no substitution or processing link), so mean reversion is slower and driven by macro cycles rather than arbitrage.

## When It Works / When It Fails

### Works Well When
- Clear macro inflection points: recession ending (short gold, long copper = short the ratio), expansion ending (long gold, short copper = long the ratio)
- China stimulus announcements (compresses the ratio rapidly as copper surges)
- Fed easing cycles beginning (can go either way, need to assess which metal benefits more)

### Fails When
- Gold is driven by non macro factors: central bank buying creating a structural bid independent of risk sentiment (2022 to 2025 central bank gold accumulation)
- Copper supply disruptions move copper independently of demand (mine strikes, export bans from Indonesia/Chile)
- The ratio trends for extended periods during sustained macro regimes (2001 to 2006 China boom kept the ratio compressed for 5 years)
- Correlation between gold and copper temporarily increases during broad commodity liquidation events

## Historical Examples

**March 2020 COVID Crash:** The ratio spiked from 500 to 750+ as gold held relatively firm while copper collapsed to $2.10/lb. Traders who shorted the ratio (long copper, short gold) at the extreme and held through the recovery were rewarded as massive Chinese stimulus pulled copper to $4.70/lb by 2021 while gold drifted sideways, compressing the ratio back to 400.

**2011 Copper Peak:** Copper hit $4.60/lb on Chinese infrastructure demand. Gold was at $1,500/oz. Ratio = 326. This was an extreme low. Over the next 4 years, copper halved while gold declined less, pushing the ratio back above 600.

**2022 to 2025 Divergence:** Central bank gold buying (China, India, Turkey, Poland) pushed gold above $2,000 while copper struggled on weak Chinese property. The ratio stayed elevated, frustrating mean reversion traders. A reminder that structural central bank demand can break the historical relationship.

## Concrete Example (Current or Recent)

Gold at $2,300/oz. Copper at $4.10/lb. Ratio = 561. The 2 year average is 530 with a standard deviation of 70. Current ratio is 0.4 sigma above mean, not extreme. You are watching for China's March PMI. If PMI prints above 52 (expansion) and the ratio is still above 560, you would short the ratio: sell 1 GC at $2,300 (notional $230,000), buy 2 HG at $4.10 (notional $205,000). Target: ratio compresses to 480 (a 14% move). If gold stays at $2,300, that means copper needs to reach $4.79/lb. P&L on 2 HG contracts: ($4.79 - $4.10) x 25,000 x 2 = $34,500 gain on copper. Gold leg flat = $0. Total profit approximately $34,500. Risk: ratio expands to 620. Stop loss at 600.

## Related Strategies
- [[Inter-Commodity Spread]]
- [[Relative Value Trade]]
- [[Brent-WTI Spread]]
- [[SHFE vs LME Arb]]

## Related Concepts
- [[Risk-On Risk-Off]]
- [[Safe Haven Assets]]
- [[Correlation]]
- [[Mean Reversion]]
- [[Z-Score]]
- [[Central Bank Buying]]
- [[China PMI]]
- [[Green Metals]]

---
*Status: #solid | Last reviewed: 2026-03-24*
