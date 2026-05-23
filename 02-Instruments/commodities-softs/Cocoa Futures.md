---
aliases: [cocoa, CC, ICE cocoa, LIFFE cocoa]
tags:
  - "#agri/softs/cocoa"
date-added: "2026-03-20"
---

# Cocoa Futures

## Definition

Cocoa futures price raw cocoa beans, the primary chocolate ingredient. Two benchmark contracts: ICE US (CC, USD/tonne) and ICE Europe/LIFFE (C, GBP/tonne). Cocoa is one of the most supply concentrated commodities, with ~70% of global production from West Africa (Ivory Coast and Ghana). This concentration creates extreme volatility when weather, disease, or political events hit growing regions.

## Why it matters (commodities and FX)

Cocoa is the most volatile soft and ran a historic supply crisis in 2023 to 2025 that sent prices to all time highs above $10,000/tonne. For a commodities trader, cocoa is the purest form of supply driven trading: demand is stable (people keep eating chocolate), but supply is geographically concentrated, weather dependent, and structurally constrained (aging tree stock, swollen shoot virus, smallholder economics). A natural laboratory for [[Convenience Yield]], [[Backwardation]], and supply shock dynamics.

## Concrete example

**Concrete:** Monday morning, the weekly [[West African Port Arrivals]] print from Abidjan comes in 22% below the prior 4 week pace, confirming dry Harmattan conditions are damaging the Ivorian main crop. CC front month (CCN6) was $7,850/tonne Friday close. Trader buys 8 CC contracts at $7,890 on the open. Over 4 sessions spot grinds to $8,320 as Q1 European grindings data also surprises weak (industrial buyers cutting forward demand only modestly while supply concerns dominate). Trader sells 6 at $8,280 and 2 at $8,310. P&L: average $8,290 vs $7,890 = $400 × 10 tonnes × 8 = $32,000. Front month [[Backwardation]] to deferred widened $180.

**Simplified:** Cocoa is the price of 1 tonne of raw cocoa beans, the main ingredient in chocolate. About 70% comes from Ivory Coast and Ghana, so West African weather and disease drive most of the price action. Traders watch port arrival data, rainfall in growing regions, and quarterly grindings figures. Each ICE US contract is 10 tonnes, so a $10/tonne move equals $100 per contract. Cocoa is the most volatile of the softs.

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
- Ivory Coast: ~40% of global production. Main crop Oct to Mar, mid crop Apr to Sep
- Ghana: ~15 to 20%. Cocoa Board (COCOBOD) controls pricing and marketing
- Ecuador, Cameroon, Nigeria: secondary producers
- Swollen shoot virus (CSSVD): devastating Ghanaian and Ivorian tree stock
- Aging tree stock: average West African cocoa tree is 25+ years old, past peak productivity
- Rainfall in West Africa: critical during pod development (Jun to Sep)
- Farmer economics: low prices lead to underinvestment, switching to rubber or palm oil

### Demand drivers
- Chocolate confectionery: ~35% of cocoa demand
- Cocoa butter and powder: industrial food ingredients
- Europe is the largest consuming region (~35%), then North America (~20%)
- Grindings data (quarterly) is the primary demand indicator
- Demand is price inelastic short term but manufacturers reformulate at sustained high prices

### Seasonality
Strong seasonal pattern driven by West African main crop harvest (Oct to Mar). Prices weaken during harvest as supply enters the market. Inter crop period (Apr to Sep) sees tightening as available supply dwindles before next harvest. Weather during the West African rainy season (May to Oct) is the key uncertainty window.

## Key data and reports

- [[ICCO]] (International Cocoa Organization): quarterly grinding statistics, production forecasts
- [[West African Port Arrivals]]: weekly port arrival figures from Abidjan and San Pedro
- Ghana COCOBOD purchases: cumulative seasonal purchases (see [[West African Port Arrivals]])
- European, Asian, and North American quarterly grindings data (see [[ICCO]])
- [[ICE Cocoa Stocks]]: deliverable exchange inventory
- Rainfall data: West African growing regions
- [[COT Positioning]]: managed money positioning

## Curve structure

Cocoa frequently trades in [[Backwardation]] during supply scares because deliverable certified cocoa is limited and storage costs are meaningful (temperature control, pest management). Deep [[Contango]] occurs when supply is comfortable and warehouses are full. The 2024 to 2025 crisis produced extreme backwardation with front month premiums exceeding $2,000/tonne over deferred contracts.

## Key spreads and relative value

- **[[Cocoa NY-London Spread|ICE US / ICE London (NY/London) arb]]:** the USD vs GBP cocoa differential. Reflects origin quality (West African vs other), FX (GBP/USD), and regional demand. A key [[Relative Value Trade]] in softs.
- **Cocoa calendar spreads:** front month vs deferred. Signals physical tightness. The most actively traded spread.
- **Cocoa/Sugar ratio:** both are tropical agri products from overlapping regions. Sugar competes for land with cocoa in some areas.
- **Cocoa/Coffee ratio:** both are tropical softs with concentrated supply. Useful for relative value within softs.
- **Crush margin:** cocoa bean price vs combined value of cocoa butter + cocoa powder. Analogous to the [[Crack Spread]] in oil.

## Important relationships

- Inverse relationship with West African rainfall (drought = higher prices)
- GBP/USD directly affects the NY/London arb
- Correlated with other softs during broad "commodity supercycle" moves
- Weak correlation with broad commodity indices (cocoa is supply driven, not macro driven)
- Ivory Coast and Ghana CFA franc pegged to EUR, so EUR/USD affects farmer economics

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
