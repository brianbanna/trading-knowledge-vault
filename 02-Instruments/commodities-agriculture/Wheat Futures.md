---
aliases: [wheat, Chicago wheat, SRW, soft red winter wheat, ZW, CBOT wheat, W]
tags:
  - "#agri/grains/wheat"
date-added: "2026-07-03"
---

# Wheat Futures

## Definition

Wheat futures are the price of a bushel of wheat, but wheat is not one commodity. There are three US futures wheats, each a different class of grain with its own protein, milling use, growing region, and contract. This note covers the Chicago soft red winter (SRW) benchmark, ticker ZW on CBOT, quoted in cents per bushel. SRW is a lower protein wheat used for cakes, cookies, crackers, and pastries. The three classes and contracts to keep separate are:

- **Chicago soft red winter (SRW):** ZW on CBOT. Lower protein, softer milling. This note. Grown in the eastern Midwest and mid South
- **Kansas City hard red winter (HRW):** KE, see [[KC Wheat Futures]]. Higher protein bread wheat from the Southern Plains
- **Minneapolis hard red spring (HRS):** MW on MGEX. Highest protein, spring planted in the Northern Plains

## Why it matters (commodities and FX)

Wheat is the most geographically dispersed of the major grains, so it is the grain most exposed to global weather and geopolitics rather than a single country's crop. The three US classes trade against each other, which makes wheat a natural relative value complex. The [[KC-Chicago Wheat Spread]] trades HRW protein against SRW, a class and [[Quality Spread]]. Chicago SRW is also a feed grain substitute for [[Corn Futures|corn]], so cheap wheat caps the corn to wheat ratio. Wheat links to FX through the big exporters, Russia, the EU, Canada, Australia, Argentina, and the US, so Black Sea supply and export politics can move price more than US weather does.

## Concrete example

**Concrete:** On 2026-07-02 Chicago SRW settles at 600.25 cents/bushel. The catalyst in the tape is a USDA report confirming the smallest US wheat crop on record, with planted area the lowest since records began in 1919. A trader long 3 ZW from 560 cents on the tightening story gains (600.25 minus 560) cents times 12.50 USD times 3 = 1,509.38 USD, since each cent is 12.50 USD per 5,000 bushel contract. The fail case: the smallest US crop still matters little if the world is oversupplied. A record Russian and EU crop lands into the same window, US export sales disappoint, and Chicago slides back to 560 cents within two weeks despite the bullish US headline. The long 3 lots from 560 is now flat to underwater on carry, and a trader who bought the 600 breakout loses (600 minus 560) times 12.50 times 3 = 1,500 USD. Wheat punishes traders who read the US crop in isolation and ignore the Black Sea balance.

**Simplified:** Chicago wheat (ZW) is the price of 5,000 bushels of soft red winter wheat, the low protein wheat for cakes and crackers. It is one of three US wheats. Kansas City ([[KC Wheat Futures]], KE) is high protein bread wheat, Minneapolis (MGEX) is the highest protein spring wheat. Wheat grows everywhere, so watch Russia, the EU, and the Black Sea as much as US weather. Each tick (1/4 cent) is 12.50 USD per contract.

## Contract specifications

| Field | Value |
|-------|-------|
| Exchange | CBOT (CME Group) |
| Ticker | ZW (Chicago SRW) |
| Contract size | 5,000 bushels |
| Tick size | 1/4 cent per bushel |
| Tick value | 12.50 USD |
| Trading hours | 19:00 to 07:45 and 08:30 to 13:20 CT |
| Settlement | Physical delivery |
| Expiry months | Mar, May, Jul, Sep, Dec |
| Currency | USD (cents per bushel) |

## Fundamentals

### Supply drivers
- Russia: the largest exporter. Black Sea supply and export policy set the world floor price
- EU, Ukraine, Canada, Australia, Argentina, US: the other major exporters. Wheat is a global auction
- US classes by region: SRW in the eastern Midwest and mid South, HRW in the Southern Plains (see [[KC Wheat Futures]]), HRS in the Northern Plains
- Winter wheat is planted in the fall, goes dormant, and is harvested early summer. Spring wheat is planted in spring
- Weather risk is diversified across hemispheres and continents, so no single crop dominates the balance
- US wheat acreage has trended down for decades as corn and soybeans win Midwest acres

### Demand drivers
- Food milling is the dominant use, unlike corn. Protein content determines the milling class and price
- Feed wheat: low protein or weather damaged wheat feeds into rations and competes with [[Corn Futures|corn]]
- Exports: North Africa, the Middle East, and Southeast Asia are the large structural importers. Egypt is the classic swing buyer
- Low short run price elasticity in food use

### Seasonality
US winter wheat (SRW and HRW) is harvested May to July, the seasonal supply pulse and often the seasonal price low. Spring wheat is harvested Aug to Sep. Because wheat is grown across both hemispheres, there is a harvest somewhere much of the year, which dampens the single crop seasonality seen in corn. See [[Seasonality]].

## Key data and reports

- [[WASDE]]: monthly USDA world and US wheat balance sheets, including by class
- USDA Winter Wheat Seedings (January) and Prospective Plantings (late March)
- USDA Crop Progress (weekly): winter wheat condition ratings and harvest pace
- USDA Grain Stocks (quarterly): carryout by class
- Russian and EU export and crop data (SovEcon, IKAR, Strategie Grains)
- Egypt GASC and other state tender results: the export demand read
- CFTC COT report: managed money positioning in ZW

## Curve structure

Chicago wheat frequently sits in [[Contango]] because ample world stocks and full commercial storage reward carry, and Chicago in particular has a history of wide carrying charge structures tied to delivery and storage economics. It inverts to [[Backwardation]] on genuine supply shocks such as a Black Sea disruption. The class spreads (Chicago versus Kansas City versus Minneapolis) shift with the relative tightness of low versus high protein supply. See [[Forward Curve]] and [[Old Crop New Crop]].

## Key spreads and relative value

- **[[KC-Chicago Wheat Spread]]:** HRW (Kansas City) protein premium over SRW (Chicago). A class and [[Quality Spread]] that widens on Southern Plains drought and high protein demand
- **Chicago versus Minneapolis:** SRW against the highest protein hard red spring, another [[Quality Spread]]
- **Wheat versus [[Corn Futures|corn]]:** feed substitution. A low wheat to corn ratio pulls feed wheat into rations
- **Wheat calendar spreads:** old crop versus new crop around harvest, see [[Old Crop New Crop]]

## Important relationships

- Class spreads with [[KC Wheat Futures|Kansas City HRW]] and Minneapolis HRS driven by relative protein supply, see [[Quality Spread]]
- Feed substitution with [[Corn Futures|corn]]: cheap wheat displaces corn in feed rations
- Black Sea sensitivity: Russian crop size and export policy can dominate US fundamentals
- Inverse link between the [[Stocks to Use Ratio]] and price sensitivity, though the relevant balance is global, not just US

## Trading notes

*Add personal observations here.*

## Related instruments

- [[KC Wheat Futures]]
- [[Corn Futures]]

## Related concepts

- [[KC-Chicago Wheat Spread]]
- [[Quality Spread]]
- [[WASDE]]
- [[Stocks to Use Ratio]]
- [[Seasonality]]
