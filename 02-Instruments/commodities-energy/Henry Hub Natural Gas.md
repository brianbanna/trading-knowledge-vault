---
aliases: [Henry Hub, HH, NG, NYMEX natural gas]
tags:
  - "#energy/natgas/henry-hub"
date-added: "2026-03-20"
---

# Henry Hub Natural Gas

## Definition

Henry Hub is the US benchmark for natural gas pricing, named after the Henry Hub interconnect in Erath, Louisiana where 13 interstate and intrastate pipelines converge. The futures contract (ticker NG) trades on NYMEX (CME Group) and is the most liquid natural gas contract globally. Henry Hub prices reflect US domestic gas supply and demand, which since the shale revolution has diverged significantly from global gas prices ([[TTF Natural Gas|TTF]], [[JKM LNG|JKM]]).

## Why it matters (commodities and FX)

Henry Hub is the world's cheapest major gas benchmark due to abundant US shale production. The spread between Henry Hub and international benchmarks (TTF, JKM) is the foundation of the global LNG trade: when TTF or JKM are high enough relative to Henry Hub to cover liquefaction, shipping, and regasification costs, US LNG exports flow to Europe or Asia. This TTF/HH spread is one of the most important [[Relative Value Trade|relative value trades]] in energy.

Natural gas is also the most seasonal major commodity, creating predictable [[Calendar Spread]] opportunities around injection/withdrawal cycles.

## Contract specifications

| Field | Value |
|-------|-------|
| Exchange | NYMEX (CME Group) |
| Ticker | NG |
| Contract size | 10,000 MMBtu |
| Tick size | $0.001/MMBtu |
| Tick value | $10.00 |
| Trading hours | Sun to Fri, 17:00 to 16:00 CT |
| Settlement | Physical delivery at Henry Hub |
| Expiry months | All 12 months, up to 12 years out |
| Last trading day | 3 business days before first calendar day of delivery month |
| Currency | USD |

## Fundamentals

### Supply drivers
- US dry gas production: approximately 103 Bcf/d (2025). Appalachia (Marcellus/Utica), Permian (associated gas), Haynesville are key basins
- Associated gas from oil production: Permian Basin oil drilling produces gas as a byproduct, creating supply that is insensitive to gas prices
- Rig count: Baker Hughes weekly gas rig count
- DUC (drilled but uncompleted) well inventory: supply response buffer
- Pipeline capacity and takeaway constraints from producing basins

### Demand drivers
- Power generation: approximately 38% of US gas demand. Weather sensitive (summer cooling, winter heating)
- Industrial: approximately 28%. Chemicals, fertilizer, manufacturing
- Residential/commercial heating: approximately 22%. Highly weather sensitive in winter
- LNG export demand: approximately 12 to 14 Bcf/d of feedgas capacity. Growing structural demand
- Mexico pipeline exports: approximately 6 Bcf/d

### Seasonality
The strongest seasonal pattern of any major commodity. Injection season (Apr to Oct): utilities and traders inject gas into underground storage, building inventories for winter. Withdrawal season (Nov to Mar): heating demand draws down storage. Prices typically trough in shoulder months (Apr, Oct) and peak during cold winter spells (Dec to Feb). Summer heat waves can also spike prices due to power generation demand for air conditioning.

## Key data and reports

- EIA Weekly Natural Gas Storage Report (Thursday 10:30am ET): the single most important data release for natural gas. Reports net change in underground storage vs expectations.
- EIA Natural Gas Monthly: production, consumption, imports/exports
- Baker Hughes weekly rig count (Friday 1pm ET)
- NOAA weather forecasts: heating degree days (HDD) and cooling degree days (CDD)
- LNG feedgas flows: daily data from vessel tracking (Kpler, Vortexa) and pipeline monitors
- CFTC COT report: managed money positioning in NG

## Curve structure

Henry Hub has the most pronounced seasonal curve shape of any major commodity. Winter contracts (Dec, Jan, Feb) trade at a premium to summer contracts (Apr, May, Jun) in most years, creating a natural seasonal [[Contango]] from spring to winter. Within the injection season, the curve often shows mild contango. The March/April spread (end of winter/start of injection) is one of the most volatile calendar spreads in all of commodities.

Structural [[Backwardation]] in the front of the curve occurs during extreme cold snaps when immediate gas supply is critical.

## Key spreads and relative value

- **Henry Hub / TTF spread:** the transatlantic LNG arb. Approximately $2 to 4/MMBtu of liquefaction + shipping cost. When TTF minus HH exceeds this, US LNG exports are profitable. The most important cross basin energy spread.
- **Henry Hub / JKM spread:** the Pacific LNG arb. Similar to TTF/HH but for Asia bound cargoes.
- **Winter/Summer spread:** the core seasonal trade. Buy Nov/Dec/Jan, sell Apr/May/Jun (or vice versa depending on storage trajectory).
- **March/April spread (the widowmaker):** extremely volatile end of winter spread. Named for its ability to blow up traders.
- **Spark spread:** gas price vs power price. Reflects gas fired power plant profitability.
- **Nymex/Waha basis:** Henry Hub vs Permian Basin local price. Reflects pipeline capacity out of the Permian.

## Important relationships

- Strong inverse correlation with temperature (colder = higher prices in winter, hotter = higher in summer)
- Positive correlation with storage deficits (actual storage vs 5 year average)
- Weak correlation with crude oil (decoupled since shale revolution, but reconnects during extreme moves)
- Correlation with [[TTF Natural Gas|TTF]] mediated by LNG export economics
- Inverse correlation with production data (higher production = lower prices with lag)

## Trading notes

*Add personal observations here.*

## Related instruments

- [[TTF Natural Gas]]
- [[JKM LNG]]
- [[NBP Natural Gas]]
- [[Brent Crude]]

## Related concepts

- [[Contango]]
- [[Backwardation]]
- [[Seasonality]]
- [[Convenience Yield]]
- [[Roll Yield]]
- [[Forward Curve]]
- [[Relative Value Trade]]
- [[Storage Economics]]
- [[Calendar Spread]]
