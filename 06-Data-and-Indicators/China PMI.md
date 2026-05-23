---
aliases: [China PMI, Caixin PMI, NBS PMI, Chinese PMI]
tags:
  - "#metals/base"
  - "#macro"
date-added: "2026-03-20"
---

# China PMI

## Definition

The China Purchasing Managers Index is a monthly survey of manufacturing activity in China, the world's largest base metals consumer and second largest economy. Two versions exist: NBS Manufacturing PMI (state run, tilted to large SOEs) and Caixin Manufacturing PMI (S&P Global, tilted to smaller private firms). Above 50 = expansion, below 50 = contraction. PMI leads actual production and GDP by 1 to 3 months.

## Why it matters (commodities and FX)

Base metals are highly sensitive to China PMI because China consumes ~50% of global copper, aluminum, zinc, and nickel. The surprise vs consensus drives the reaction, not the absolute level. Subcomponents (new orders, export orders, inventories, employment) add granularity. Strong PMI supports [[Commodity Currencies]] (AUD, NZD) and weakens safe havens. PMI also feeds [[SHFE]] pricing and the [[SHFE vs LME Arb]] calculation.

## Concrete example

**Concrete:** Consensus for January 2026 NBS Manufacturing PMI is 49.5. Actual prints at 51.2, a 1.7 point beat. Within the hour, LME copper rallies $200/tonne (3M from $9,400 to $9,600), AUD/USD jumps 40 pips, SGX iron ore rises 3%. A trader long 50 lots of LME copper and AUD 5M of AUD/USD into the print captures $250,000 on copper plus $20,000 on FX. Counter scenario: PMI prints 48.0 (1.5 point miss). Copper drops $300/tonne to $9,100, AUD/USD falls 60 pips. Same position loses ~$405,000.

**Simplified:** China makes and consumes most of the world's industrial metals. PMI is a monthly survey asking factory managers if business is getting better. A surprise beat means stronger demand than priced in, so copper, AUD, and iron ore jump. A miss does the reverse. Trade the gap between what printed and what the market expected, not the headline level.

## Key mechanics and formulas

**Release schedule:**
- NBS PMI: last day of month, 9:00 AM Beijing
- Caixin PMI: 1st business day of following month, 9:45 AM Beijing

**Interpretation:**
- Above 50: expansion
- Below 50: contraction
- Distance from 50: pace of change

**Key subcomponents:**
- New orders: forward demand
- New export orders: external demand
- Inventories: restocking vs destocking
- Prices paid: input cost inflation

**Metal sensitivity:** 1 point PMI surprise moves LME copper $100 to $200/tonne and iron ore 2 to 4%.

## Prerequisites

- [[Copper Futures]]
- [[LME]]
- [[SHFE]]

## Related concepts (learn next)

- [[Copper Futures]] because copper is the most PMI sensitive base metal.
- [[SHFE vs LME Arb]] because strong PMI supports Chinese demand and the SHFE premium.
- [[Commodity Currencies]] because AUD and other commodity currencies react to China PMI.
- [[Green Metals]] because Chinese industrial activity drives energy transition metal demand.
- [[Macro Regime]] because PMI helps identify the growth component of the regime.
- [[Risk-On Risk-Off]] because China PMI shifts global risk sentiment.

## Common misconceptions

**"Only the headline PMI matters."** Subcomponents give a more accurate signal. A headline driven by inventory restocking is different from one driven by new orders.

**"NBS and Caixin always agree."** They survey different company sizes. Divergence reveals a split between large SOEs and smaller private firms.

**"Strong PMI means strong metal demand immediately."** PMI leads activity, not consumption. There is a lag between PMI improvement and physical metal demand showing up at the warehouse.

## Sources

- NBS: China Manufacturing PMI Monthly Release
- S&P Global / Caixin: China Manufacturing PMI
- Bloomberg: China Economic Surprise Index
