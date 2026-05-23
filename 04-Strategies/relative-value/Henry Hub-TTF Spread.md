---
aliases: [transatlantic gas spread, HH TTF spread, US Europe gas arb, LNG arbitrage, natgas arb]
tags:
  - "#energy/natgas/henry-hub"
  - "#energy/natgas/ttf"
  - "#energy/natgas/lng"
date-added: "2026-03-24"
---

# Henry Hub-TTF Spread

## Core Thesis

The Henry Hub-TTF spread trades the price difference between US natural gas ([[Henry Hub Natural Gas]], NYMEX NG, USD/MMBtu) and European natural gas ([[TTF Natural Gas]], ICE Endex, EUR/MWh). The price gap that LNG tankers exist to exploit. When European gas is expensive relative to US gas, more LNG cargoes sail from US export terminals (Sabine Pass, Cameron, Freeport, Calcasieu Pass) to European regasification terminals. When the gap narrows below the cost of liquefaction, shipping, and regasification, cargoes divert to Asia or stay home. Anchored by the full chain LNG netback cost, making it one of the most physically grounded inter commodity spreads in energy.

## Mechanics

### Unit Conversion

Henry Hub in USD/MMBtu. TTF in EUR/MWh. To compare:
- 1 MWh = 3.412 MMBtu (approximately)
- Convert TTF to USD/MMBtu: TTF (EUR/MWh) / 3.412 x EUR/USD

**Spread = TTF (converted to USD/MMBtu) - Henry Hub (USD/MMBtu)**

Example: TTF at EUR 30/MWh, EUR/USD at 1.08. TTF in USD/MMBtu = (30 x 1.08) / 3.412 = $9.50/MMBtu. Henry Hub at $2.50/MMBtu. Spread = $7.00/MMBtu.

### The LNG Netback

Spread must exceed full chain cost to incentivize cargoes:
- US liquefaction fee: ~$2.50 to $3.50/MMBtu (tolling agreements)
- Shipping (US Gulf to NW Europe): ~$0.50 to $1.50/MMBtu depending on tanker rates and distance
- European regasification: ~$0.30 to $0.50/MMBtu
- **Total cost: ~$3.50 to $5.50/MMBtu**

Spread >$5.50: every available cargo heads to Europe. Spread <$3.50: US exports to Europe slow, cargoes divert to Asia ([[JKM]] vs TTF becomes relevant).

### Entry Criteria
- Spread deviates from the LNG netback cost range by more than $2/MMBtu
- Seasonal catalyst: European winter demand (Oct to Mar), US hurricane season disrupting export terminals (Jun to Nov), Asian demand competition
- European storage: >90% entering winter, TTF weakens, spread compresses. <70%, TTF strengthens.
- US LNG export terminal outages (Freeport LNG 2022) or new capacity additions

### Exit Criteria
- Spread reverts toward the LNG netback equilibrium ($3.50 to $5.50)
- Seasonal driver resolves (winter ends, hurricane season passes)
- Time stop: 4 to 8 weeks

### Position Sizing
NG (NYMEX) = 10,000 MMBtu per contract. TTF (ICE Endex) = 1 MW per hour for each hour in delivery month (varies). Conversion is not straightforward. Many traders use financial derivatives or LNG forward contracts already netback adjusted. For futures: match notional. At HH $2.50/MMBtu ($25,000 contract value) and TTF EUR 30/MWh (monthly contract varies), sizing requires careful calculation.

## Instruments Used
- [[Henry Hub Natural Gas]] NYMEX (NG)
- [[TTF Natural Gas]] ICE Endex (TFM)
- JKM (Platts LNG) for the Asia diversion optionality
- EUR/USD for FX hedging
- LNG freight derivatives (optional, for isolating the commodity spread from shipping)

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | LNG supply chain disruption (terminal outage, tanker shortage, canal closure) |
| Max Loss Scenario | Geopolitical event that permanently reprices European gas (Russia pipeline cut in 2022 sent TTF to EUR 340/MWh) |
| Hedged Exposure | General energy direction partially hedged |
| Unhedged Exposure | FX (EUR/USD), shipping rates, terminal outage risk, Asian demand competition, weather in both regions |
| Margin Requirements | Full margin on both legs (different exchanges) |

## Edge Source

Tracking the physical LNG supply chain provides the edge. Key data: US LNG feed gas flows (daily, from pipeline data providers), European storage levels (GIE AGSI+), tanker tracking (vessel AIS data), terminal maintenance schedules, and JKM pricing for Asian competition. The spread has a hard physical floor (below netback cost, cargoes stop) and is capped on the upside by regasification capacity limits and demand destruction.

## When It Works / When It Fails

### Works Well When
- Spread reaches extremes beyond the netback cost range and no structural shift has occurred
- Seasonal patterns align: selling the spread (short TTF, long HH) in March as winter demand fades, buying it in September before winter builds
- Clear terminal status: no outages, known capacity online

### Fails When
- Geopolitical shock: 2022 Russia Ukraine war permanently widened the spread as Europe lost 150 bcm/year of pipeline gas and became structurally dependent on LNG. Mean reversion to the old $3 to $5 range was wrong because fair value shifted.
- LNG terminal outage: Freeport LNG explosion in June 2022 removed 2 bcf/d of US export capacity for 6 months, compressing the spread on the HH side (HH fell because gas was trapped in the US) while TTF stayed elevated.
- Asian demand competition: cold Asian winter pulls LNG cargoes from Europe, widening TTF-HH beyond the netback cost.
- EUR/USD volatility adds noise to the spread, especially during ECB/Fed policy divergence

## Historical Examples

**2022 European Energy Crisis:** Russia cut pipeline gas to Europe. TTF spiked to EUR 340/MWh in August 2022 (~$100/MMBtu equivalent). Henry Hub at $8/MMBtu. Spread exploded to $90+/MMBtu, far above any netback cost. Every available LNG cargo on earth headed to Europe. Spread gradually compressed as Europe filled storage and demand destruction kicked in, but took 12 months to normalize toward $5 to $8.

**2023 to 2024 Normalization:** European storage entered winter 2023 at 95%+. TTF collapsed to EUR 25 to 30/MWh. Henry Hub at $2 to $3. Spread compressed to $5 to $7, right at the LNG netback cost. Textbook mean reversion to physical equilibrium.

**Freeport LNG Outage (June 2022):** Explosion took 2 bcf/d offline. Henry Hub dropped from $9 to $6 as gas backed up in the US. TTF stayed at EUR 130/MWh. Spread widened further. Traders who expected convergence from the HH side got hurt because the supply disruption was on the export side, trapping gas domestically.

## Concrete Example (Current or Recent)

**Concrete:** Henry Hub at $3.80/MMBtu. TTF at EUR 35/MWh. EUR/USD at 1.08. TTF converted = (35 x 1.08) / 3.412 = $11.07/MMBtu. Spread = $7.27/MMBtu. Full chain LNG cost ~$4.50/MMBtu. Spread is $2.77 above netback, cargoes flowing profitably but not extreme. European storage at 45% entering injection season (April). Low for the time of year (5 year average 55%). TTF should hold firm as Europe needs to refill. Go long the spread: buy TTF, sell HH. If TTF rises to EUR 42/MWh while HH stays at $3.80, new spread $9.49. Profit ~$2.22/MMBtu = $22,200 per NG contract equivalent. Risk: warm European spring collapses storage demand, TTF falls to EUR 28, loss ~$22,100. Low storage tilts probability.

**Simplified:** Same product (gas), 2 continents. Europe buys liquefied gas (LNG) from the US. The price gap between US gas and European gas has to cover the cost of liquefying, shipping, and regasifying. When the gap stretches beyond that cost, ships move and the gap closes. Trade the deviations from physical shipping cost.

## Related Strategies
- [[Inter-Commodity Spread]]
- [[Location Arbitrage]]
- [[Brent-WTI Spread]] (analogous transatlantic energy arb)
- [[Relative Value Trade]]
- [[Calendar Spread]]

## Related Concepts
- [[Storage Economics]]
- [[Seasonality]]
- [[Convenience Yield]]
- [[Mean Reversion]]
- [[Structural Break]]
- [[Freight]]
- [[Correlation]]

---
*Status: #solid | Last reviewed: 2026-03-24*
