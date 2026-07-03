---
aliases: [soybeans, beans, ZS, CBOT soybeans, S]
tags:
  - "#agri/oilseeds/soybeans"
date-added: "2026-07-03"
---

# Soybean Futures

## Definition

Soybean futures are the price of raw soybeans, the oilseed that sits at the front of the [[Crush Spread]]. A soybean is not consumed as a raw bean at scale. It is crushed into two products that carry almost all of its value: high protein [[Soybean Meal Futures|meal]] and [[Soybean Oil Futures|oil]]. One bushel weighs 60 lbs and yields roughly 44 lbs of meal, 11 lbs of oil, and 5 lbs of hulls and waste. The benchmark contract is CBOT ZS, quoted in US cents per bushel. Snapshot: 1,146.75 cents/bushel on 2026-07-02.

## Why it matters (commodities and FX)

Soybeans are the largest oilseed crop and one of the most politically sensitive commodities in global trade. Supply is concentrated in the US, Brazil, and Argentina, while demand is dominated by China, which buys more than 60% of world exports to feed its hog herd. That concentration makes the flat price a proxy for US China trade relations and for the Brazilian harvest. Soybeans are the raw input to the [[Crush Spread]], so their price sets the cost side of the crusher [[Process Margin|process margin]]. Because Brazil is the marginal exporter, [[USD/BRL]] drives farmer selling and export competitiveness in the same way the Real drives coffee and sugar.

## Concrete example

**Concrete:** A crusher watches the board crush, the combined value of [[Soybean Meal Futures|meal]] and [[Soybean Oil Futures|oil]] output minus the bean cost. In August, November soybeans (ZSX6) trade 1,150 cents/bushel, December meal (ZMZ6) 305 USD/short ton, December oil (ZLZ6) 65 cents/lb. Per bushel the meal yields 44/2000 short ton × 305 = 6.71 USD, the oil yields 11 lbs × 0.65 = 7.15 USD, so gross product value is 13.86 USD versus a bean cost of 11.50 USD, a gross crush margin of 2.36 USD/bushel. That margin is wide, so crushers bid aggressively for beans and the flat price grinds higher into harvest. Win case: a trader long beans against short products captures the margin compression as beans catch up, banking most of a 40 cent bean rally. Fail case: a surprise bearish [[WASDE]] lifts the US yield estimate to a record, the [[Stocks to Use Ratio|stocks to use ratio]] jumps, beans gap down 55 cents (ZS moves 50 USD per cent per contract, so 55 cents is 2,750 USD per contract) and the long bean leg loses faster than the short products recover.

**Simplified:** Soybean futures are the price of 5,000 bushels of raw soybeans. You crush a bean into meal and oil, and those two products are what people actually buy. If meal and oil are expensive relative to beans, crushers make money and bid up beans. Most price action comes from the US and Brazilian harvests and from how much China is buying. Each contract is 5,000 bushels, so 1 cent per bushel is 50 USD per contract, and one quarter cent tick is 12.50 USD.

## Contract specifications

| Field | Value |
|-------|-------|
| Exchange | CBOT (CME Group) |
| Ticker | ZS |
| Contract size | 5,000 bushels |
| Tick size | 1/4 cent per bushel (0.25 cent) |
| Tick value | 12.50 USD |
| Trading hours | 19:00 to 07:45 and 08:30 to 13:20 CT |
| Settlement | Physical delivery |
| Expiry months | Jan, Mar, May, Jul, Aug, Sep, Nov |
| Currency | USD (cents per bushel) |

## Fundamentals

### Supply drivers
- United States: ~30 to 35% of global production. Harvest Sep to Nov
- Brazil: the largest exporter, harvest Feb to May, expanding acreage every year
- Argentina: third largest producer and the dominant crush and meal exporter
- [[USD/BRL]]: a weaker Real incentivizes Brazilian farmer selling and cheapens Brazilian beans in USD terms
- Weather in the US Midwest (Jul pod fill) and in the Brazilian Center West (Jan to Feb)
- Acreage competition with corn: see the [[Soybean-Corn Spread]] and the November bean to December corn ratio near 2.5 that farmers use to allocate land

### Demand drivers
- China imports: more than 60% of world seaborne trade, driven by hog crush margins
- Domestic US crush for meal and oil, growing with renewable diesel demand pulling on [[Soybean Oil Futures|oil]]
- Global animal protein consumption sets the floor under meal demand
- Argentine and Brazilian export tax and policy shifts redirect crush and bean flows

### Seasonality
US price tends to build a weather premium into June and July, the pod setting and fill window, then release it into the September to November harvest low. Brazilian harvest pressure hits Feb to May. The [[Old Crop New Crop]] spread (old crop July versus new crop November) captures the transition and inverts when old crop stocks are tight.

## Key data and reports

- USDA [[WASDE]]: monthly world and US supply and demand balances
- USDA Crop Production and the final January report: US yield and production
- USDA Grain Stocks (quarterly): the [[Stocks to Use Ratio|stocks to use]] input
- USDA Prospective Plantings (Mar) and Acreage (Jun): the corn versus bean acreage fight
- USDA Export Sales (weekly): China flash sales and cancellations
- NOPA monthly crush: US crush volume and meal and oil stocks
- CONAB: Brazilian production estimates
- CFTC COT report: managed money positioning in ZS

## Curve structure

The soybean curve carries a hard seasonal shape because of the two hemisphere harvests and the July to November crop year break. Old crop months (through July) and new crop months (November onward) can trade as almost separate markets. Tight old crop stocks push the front into [[Backwardation]], with old crop July over new crop November. Ample stocks give a normal carry [[Contango]]. The August contract straddles the transition and is thinly traded.

## Key spreads and relative value

- **[[Crush Spread]]:** long beans versus short meal and oil, or the reverse (a reverse crush). The single most important spread in the complex and the reason this note, [[Soybean Meal Futures]], and [[Soybean Oil Futures]] cross link.
- **[[Soybean-Corn Spread]]:** the November bean to December corn ratio that governs US spring acreage. Above roughly 2.5 favors beans, below favors corn.
- **[[Old Crop New Crop]] spread:** July over November for the crop year transition.
- **Soybean calendar spreads:** front versus deferred around US and Brazilian harvest windows.
- **US versus Brazil basis:** the export arbitrage that [[USD/BRL]] and freight drive.

## Important relationships

- Inverse correlation with [[USD/BRL]]: a weaker Real pushes more Brazilian selling and cheaper beans in USD
- Product tension: bean price is bid up when the [[Crush Spread]] and [[Process Margin]] are wide and pressured when crush margins collapse
- Corn linkage through shared Midwest acreage and the [[Soybean-Corn Spread]]
- China demand is the dominant swing factor: export sales and cancellations move the flat price more than US weather in many years
- Meal carries most crush value in most years, so meal strength pulls beans more than oil does

## Trading notes

*Add personal observations here.*

## Related instruments

- [[Soybean Meal Futures]]
- [[Soybean Oil Futures]]
- [[Corn Futures]]
- [[USD/BRL]]

## Related concepts

- [[Crush Spread]]
- [[Process Margin]]
- [[Soybean-Corn Spread]]
- [[Old Crop New Crop]]
- [[Stocks to Use Ratio]]
- [[WASDE]]
- [[Seasonality]]
