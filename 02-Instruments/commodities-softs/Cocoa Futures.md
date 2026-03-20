---
aliases: [cocoa, CC, ICE cocoa, LIFFE cocoa]
tags:
  - "#agri/softs/cocoa"
date-added: "2026-03-20"
---

# Cocoa Futures

## Definition

Cocoa futures represent the price of raw cocoa beans, the primary ingredient in chocolate. Two benchmark contracts exist: ICE US (CC, priced in USD/tonne) and ICE Europe/LIFFE (C, priced in GBP/tonne). Cocoa is one of the most supply concentrated commodities, with approximately 70% of global production coming from West Africa (Ivory Coast and Ghana). This concentration creates extreme price volatility when weather, disease, or political events hit the growing regions.

## Why it matters (commodities and FX)

Cocoa is the most volatile soft commodity and experienced a historic supply crisis in 2023 to 2025 that sent prices to all time highs above $10,000/tonne. For a commodities trader, cocoa represents the purest form of supply driven commodity trading: demand is relatively stable (people keep eating chocolate), but supply is geographically concentrated, weather dependent, and affected by structural issues (aging tree stock, swollen shoot virus, smallholder farmer economics). This makes cocoa a natural laboratory for understanding [[Convenience Yield]], [[Backwardation]], and supply shock dynamics.

## Contract specifications

| Field | Value |
|-------|-------|
| Exchange | ICE US |
| Ticker | CC |
| Contract size | 10 metric tonnes |
| Tick size | $1/tonne |
| Tick value | $10.00 |
| Trading hours | 04:45 to 13:30 ET |
| Settlement | Physical delivery |
| Expiry months | Mar, May, Jul, Sep, Dec |
| Currency | USD |

ICE Europe (London):
| Field | Value |
|-------|-------|
| Exchange | ICE Europe |
| Ticker | C |
| Contract size | 10 metric tonnes |
| Currency | GBP |

## Fundamentals

### Supply drivers
- Ivory Coast: approximately 40% of global production. Main crop Oct to Mar, mid crop Apr to Sep
- Ghana: approximately 15 to 20% of production. Cocoa Board (COCOBOD) controls pricing and marketing
- Ecuador, Cameroon, Nigeria: secondary producers
- Swollen shoot virus disease (CSSVD): devastating Ghanaian and Ivorian tree stock
- Aging tree stock: average cocoa tree is 25+ years old in West Africa, past peak productivity
- Rainfall patterns in West Africa: critical during pod development (Jun to Sep)
- Farmer economics: low prices lead to underinvestment, switching to rubber or palm oil

### Demand drivers
- Chocolate confectionery: approximately 35% of cocoa demand
- Cocoa butter and powder: industrial food ingredients
- Europe is the largest consuming region (~35%), followed by North America (~20%)
- Grindings data (quarterly) is the primary demand indicator
- Demand is relatively price inelastic in the short term but manufacturers reformulate at sustained high prices

### Seasonality
Strong seasonal pattern driven by West African main crop harvest (Oct to Mar). Prices tend to weaken during harvest as supply enters the market. The "inter crop" period (Apr to Sep) sees tightening as available supply dwindles before next harvest. Weather during the West African rainy season (May to Oct) is the key uncertainty window.

## Key data and reports

- ICCO (International Cocoa Organization): quarterly grinding statistics, production forecasts
- Ivory Coast arrivals data: weekly port arrival figures from Abidjan and San Pedro
- Ghana COCOBOD purchases: cumulative seasonal purchases
- European, Asian, and North American quarterly grindings data
- ICE certified stocks: deliverable inventory in exchange warehouses
- Rainfall data: West African growing regions
- Commitment of Traders: managed money positioning

## Curve structure

Cocoa frequently trades in [[Backwardation]] during supply scares because physical availability of certified, deliverable cocoa is limited and storage costs for cocoa are meaningful (temperature control, pest management). Deep [[Contango]] occurs when supply is comfortable and warehouses are full. The 2024 to 2025 crisis produced extreme backwardation with front month premiums exceeding $2,000/tonne over deferred contracts.

## Key spreads and relative value

- **ICE US / ICE London (NY/London) arb:** the differential between USD priced and GBP priced cocoa. Reflects origin quality differences (West African vs other), FX (GBP/USD), and regional demand. A key [[Relative Value Trade]] in softs.
- **Cocoa calendar spreads:** front month vs deferred. Signals physical tightness. The most actively traded spread in cocoa.
- **Cocoa/Sugar ratio:** both are tropical agricultural products from overlapping regions. Sugar competes for land with cocoa in some areas.
- **Cocoa/Coffee ratio:** both are tropical softs with concentrated supply. Useful for relative value within the softs complex.
- **Crush margin:** cocoa bean price vs combined value of cocoa butter + cocoa powder. Analogous to the [[Crack Spread]] in oil.

## Important relationships

- Inverse relationship with West African rainfall (drought = higher prices)
- GBP/USD affects the NY/London arb directly
- Correlation with other softs during broad "commodity supercycle" moves
- Weak correlation with broad commodity indices (cocoa is supply driven, not macro driven)
- Ivory Coast and Ghana CFA franc is pegged to EUR, so EUR/USD affects farmer economics

## Trading notes

*Add personal observations here.*

## Related instruments

- [[Coffee Futures]]
- [[Sugar Futures]]
- [[Cotton Futures]]
- [[Palm Oil Futures]]

## Related concepts

- [[Backwardation]]
- [[Convenience Yield]]
- [[Forward Curve]]
- [[Seasonality]]
- [[Relative Value Trade]]
- [[Supply and Demand Fundamentals]]
