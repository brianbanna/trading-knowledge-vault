---
aliases: [corn, maize, ZC, CBOT corn, C]
tags:
  - "#agri/grains/corn"
date-added: "2026-07-03"
---

# Corn Futures

## Definition

Corn futures are the price of a bushel of yellow field corn deliverable in the US, quoted on CBOT in cents per bushel. This is the reference contract for the world's largest grain crop by volume. It is not sweet corn or human table corn. It is commodity feed and industrial corn that goes into animal feed, ethanol, and processed food ingredients. The US is the largest producer and exporter, so the CBOT contract (ZC) is the global benchmark, with [[Corn Futures#Curve structure|new crop and old crop]] months tracking the US [[Crop Year]].

## Why it matters (commodities and FX)

Corn is the anchor of the grain complex. It competes for the same Midwest acreage as soybeans, so the [[Soybean-Corn Spread]] is one of the most reliable acreage substitution trades in agriculture. Roughly 40% of the US corn crop goes to ethanol, which ties corn to energy prices and biofuel policy, and a similar share goes to animal feed, which ties it to the protein complex (cattle, hogs, poultry). On the FX side corn links to Brazil, the second largest exporter. Brazilian corn ethanol has grown from 500 million liters in 2017 to 6.3 billion liters, so Brazilian supply and the [[USD/BRL]] rate now shape the export balance that used to be a US near monopoly. Corn is a textbook study in how [[Seasonality]], [[WASDE]] supply and demand balances, and the [[Stocks to Use Ratio]] set price.

## Concrete example

**Concrete:** On 2026-07-02 front month corn settles at 440.75 cents/bushel, up 4.69% on the day. The move is driven by crop weather stress across the western Corn Belt (a ridge of heat during pollination) and smaller harvest expectations building ahead of the August [[WASDE]]. A trader who bought 2 ZC contracts the prior session at 421 cents rides the move. Each cent is 12.50 USD per contract, so the gain is (440.75 minus 421) cents times 12.50 USD times 2 = 493.75 USD per cent structure, more precisely 19.75 cents times 12.50 USD times 2 = 493.75 USD. The fail case: the ridge breaks 3 days later, rain returns to Iowa and Illinois, and the [[Stocks to Use Ratio]] estimate is revised up. Corn falls back to 415 cents. The same long 2 lots from 421 now loses (421 minus 415) cents times 12.50 USD times 2 = 150 USD, and a trader who chased the top at 440 loses (440 minus 415) times 12.50 times 2 = 625 USD. Weather rallies in corn are violent and often round trip.

**Simplified:** Corn futures are the price of 5,000 bushels of feed corn. The US grows and exports the most, so US Midwest weather from June pollination through the fall harvest drives most of the price action. About 40% of the crop becomes ethanol and much of the rest becomes animal feed. Each contract is 5,000 bushels, and 1 tick (1/4 cent) is 12.50 USD per contract. Watch USDA reports, US weather, and Brazil's second crop.

## Contract specifications

| Field | Value |
|-------|-------|
| Exchange | CBOT (CME Group) |
| Ticker | ZC |
| Contract size | 5,000 bushels |
| Tick size | 1/4 cent per bushel |
| Tick value | 12.50 USD |
| Trading hours | 19:00 to 07:45 and 08:30 to 13:20 CT |
| Settlement | Physical delivery |
| Expiry months | Mar, May, Jul, Sep, Dec |
| Currency | USD (cents per bushel) |

## Fundamentals

### Supply drivers
- US: largest producer, roughly a third of global output. Iowa and Illinois are the core states
- Brazil: second largest exporter. The safrinha (second crop) planted after soybeans is the swing supply
- Argentina, Ukraine, China: other major producers. Ukraine is a large exporter into the EU and North Africa
- US planting window (Apr to May) and pollination (Jul) are the two highest risk weather windows
- Acreage competition with soybeans every spring, tracked through the [[Soybean-Corn Spread]] and USDA Prospective Plantings
- Input costs, especially nitrogen fertilizer, since corn is nitrogen intensive

### Demand drivers
- Ethanol: roughly 40% of the US crop. Ties corn to gasoline and biofuel mandates. Brazilian corn ethanol has scaled from 500 million liters (2017) to 6.3 billion liters
- Animal feed: the largest single use globally. Links corn to cattle, hog, and poultry margins
- Exports: US, Brazil, Argentina, and Ukraine compete for feed grain demand from Mexico, Japan, China, and the EU
- Food and industrial: high fructose corn syrup, starch, sweeteners
- Low short run price elasticity in feed and ethanol channels

### Seasonality
US corn is planted Apr to May, pollinates in Jul, and is harvested Sep to Nov. Prices tend to build a weather premium into the Jun and Jul pollination window and release it into harvest if yields hold, the classic harvest low. Brazil's safrinha corn is harvested Jun to Aug, adding a second global supply pulse. See [[Seasonality]] and [[Old Crop New Crop]] for the calendar spread mechanics.

## Key data and reports

- [[WASDE]]: monthly USDA World Agricultural Supply and Demand Estimates, the core balance sheet
- USDA Prospective Plantings (late March) and Acreage (late June): the acreage battle numbers
- USDA Crop Progress (weekly, Apr to Nov): planting pace, condition ratings, harvest pace
- USDA Grain Stocks (quarterly): old crop carryout
- CONAB: Brazilian crop agency estimates for the safrinha
- CFTC COT report: managed money positioning in ZC
- EIA ethanol production and stocks (weekly): the ethanol demand read

## Curve structure

Corn moves between [[Contango]] and [[Backwardation]] around the [[Crop Year]]. The sharpest structural feature is the [[Old Crop New Crop]] spread, old crop (July, September) versus new crop (December). Old crop tightness with a large expected new crop inverts the July to December spread into backwardation. An adequate carryout and a normal crop give mild contango that reflects storage costs. See [[Forward Curve]].

## Key spreads and relative value

- **[[Soybean-Corn Spread]]:** the acreage substitution trade. Corn cheap relative to soybeans pushes acres to soybeans, and vice versa. Mean reverting around a long run ratio near 2.4:1
- **Corn calendar spreads:** old crop versus new crop (July versus December) around harvest expectations, see [[Old Crop New Crop]]
- **Corn versus [[Wheat Futures|wheat]]:** feed substitution. When wheat is cheap relative to corn, feeders switch, capping the corn to wheat ratio
- **Corn versus ethanol and gasoline:** the ethanol crush, corn cost versus ethanol and distillers grain revenue

## Important relationships

- Feed substitution with [[Wheat Futures|wheat]]: cheap feed wheat displaces corn in rations
- Acreage substitution with [[Soybean Futures|soybeans]] via the [[Soybean-Corn Spread]]
- Energy linkage through ethanol: corn correlates with gasoline and crude when the ethanol margin is the swing use
- [[USD/BRL]]: a weaker Brazilian real incentivizes Brazilian farmer selling and exports, pressuring US export share and CBOT corn
- Inverse link between the [[Stocks to Use Ratio]] and price: a low stocks to use ratio raises price sensitivity to any supply shock

## Trading notes

*Add personal observations here.*

## Related instruments

- [[Wheat Futures]]
- [[Soybean Futures]]
- [[USD/BRL]]

## Related concepts

- [[Soybean-Corn Spread]]
- [[WASDE]]
- [[Stocks to Use Ratio]]
- [[Seasonality]]
- [[Crop Year]]
- [[Old Crop New Crop]]
