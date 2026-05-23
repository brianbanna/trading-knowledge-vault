---
aliases: [Henry Hub, HH, NG, NYMEX natural gas]
tags:
  - "#energy/natgas/henry-hub"
date-added: "2026-03-20"
---

# Henry Hub Natural Gas

## Definition

Henry Hub is the US natural gas benchmark, named after the Henry Hub interconnect in Erath, Louisiana where 13 interstate and intrastate pipelines converge. The futures contract (NG) trades on NYMEX (CME Group) and is the world's most liquid natural gas contract. Henry Hub reflects US domestic supply and demand, which since the shale revolution has decoupled from global gas prices ([[TTF Natural Gas|TTF]], [[JKM LNG|JKM]]).

## Why it matters (commodities and FX)

Henry Hub is the world's cheapest major gas benchmark thanks to abundant US shale output. The spread to international benchmarks (TTF, JKM) anchors the global LNG trade: when TTF or JKM clear liquefaction, shipping, and regas costs above Henry Hub, US LNG exports flow to Europe or Asia. The TTF/HH spread is one of the most important [[Relative Value Trade|relative value trades]] in energy.

Natural gas is also the most seasonal major commodity, generating predictable [[Calendar Spread]] opportunities around injection/withdrawal cycles.

## Concrete example

**Concrete:** Monday morning early January. NOAA 6 to 10 day forecast shifts 8 degrees colder for the Midwest and Northeast, projecting a polar vortex intrusion. NG front month (NGG6) opens $3.10/MMBtu. Trader buys 8 NG contracts at $3.12 reading the shift as a structural HDD upgrade not yet priced. Within 2 sessions spot hits $3.58 as power utilities scramble to lock in winter supply and the Feb/Mar [[Calendar Spread]] widens 18 cents. Trader exits at $3.52. P&L: ($3.52 minus $3.12) × 10,000 MMBtu × 8 = $32,000. The Thursday EIA storage report later confirms a withdrawal 35 Bcf above consensus.

**Simplified:** Henry Hub is the price of 1 million BTU of natural gas delivered at a pipeline hub in Louisiana. Cold weather makes the price go up because people need to heat homes and power plants burn more gas. Hot weather also lifts it because of air conditioning. Traders watch the weather forecast and the Thursday EIA storage report. Each contract is 10,000 MMBtu, so a $0.10 move equals $1,000 per contract.

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
- US dry gas production: ~103 Bcf/d (2025). Appalachia (Marcellus/Utica), Permian (associated gas), Haynesville are key basins
- Associated gas from Permian oil drilling: gas produced as byproduct, insensitive to gas prices
- Rig count: Baker Hughes weekly gas rig count
- DUC (drilled but uncompleted) well inventory: supply response buffer
- Pipeline capacity and takeaway constraints from producing basins

### Demand drivers
- Power generation: ~38% of US gas demand. Weather sensitive (summer cooling, winter heating)
- Industrial: ~28%. Chemicals, fertilizer, manufacturing
- Residential/commercial heating: ~22%. Highly winter weather sensitive
- LNG export demand: ~12 to 14 Bcf/d of feedgas capacity. Growing structural demand
- Mexico pipeline exports: ~6 Bcf/d

### Seasonality
The strongest seasonal pattern of any major commodity. Injection season (Apr to Oct): utilities and traders inject gas into underground storage, building winter inventories. Withdrawal season (Nov to Mar): heating demand draws down storage. Prices trough in shoulder months (Apr, Oct) and peak during cold winter spells (Dec to Feb). Summer heat waves also spike prices via power generation for air conditioning.

## Key data and reports

- EIA Weekly Natural Gas Storage Report (Thursday 10:30am ET): the single most important release. Reports net storage change vs expectations.
- EIA Natural Gas Monthly: production, consumption, imports/exports
- Baker Hughes weekly rig count (Friday 1pm ET)
- NOAA weather forecasts: heating degree days (HDD) and cooling degree days (CDD)
- LNG feedgas flows: daily vessel tracking (Kpler, Vortexa) and pipeline monitors
- CFTC COT report: managed money positioning in NG

## Curve structure

Henry Hub has the most pronounced seasonal curve shape of any major commodity. Winter contracts (Dec, Jan, Feb) trade at a premium to summer contracts (Apr, May, Jun) in most years, generating natural seasonal [[Contango]] from spring to winter. Within injection season, mild contango is common. The March/April spread (end of winter/start of injection) is one of the most volatile calendar spreads in commodities.

Structural [[Backwardation]] at the front occurs during extreme cold snaps when immediate supply is critical.

## Key spreads and relative value

- **Henry Hub / TTF spread:** the transatlantic LNG arb. ~$2 to 4/MMBtu of liquefaction + shipping cost. When TTF minus HH exceeds this, US LNG exports are profitable. The most important cross basin energy spread.
- **Henry Hub / JKM spread:** the Pacific LNG arb. Same logic for Asia bound cargoes.
- **Winter/Summer spread:** the core seasonal trade. Buy Nov/Dec/Jan, sell Apr/May/Jun (or reverse depending on storage trajectory).
- **March/April spread (the widowmaker):** highly volatile end of winter spread. Named for its history of blowing up traders.
- **Spark spread:** gas vs power price. Gas fired power plant profitability.
- **Nymex/Waha basis:** Henry Hub vs Permian Basin local price. Pipeline capacity out of the Permian.

## Important relationships

- Strong inverse correlation with temperature (colder = higher in winter, hotter = higher in summer)
- Positive correlation with storage deficits (actual vs 5 year average)
- Weak correlation with crude oil (decoupled since shale, reconnects during extreme moves)
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
