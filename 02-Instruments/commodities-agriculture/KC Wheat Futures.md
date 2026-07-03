---
aliases: [KC wheat, KE, hard red winter wheat, HRW, Kansas City wheat]
tags:
  - "#agri/grains/wheat"
date-added: "2026-07-03"
---

# KC Wheat Futures

## Definition

KC wheat futures are the price of a bushel of hard red winter wheat (HRW), the higher protein US milling wheat, quoted in cents per bushel with ticker KE on CME (the former Kansas City Board of Trade, KCBT). HRW is the classic bread wheat. It has more protein and gluten than Chicago soft red winter, so it goes into bread flour rather than the cakes and pastries that use SRW. It is grown in the Southern Plains, mainly Kansas, Oklahoma, and Texas, which makes it acutely sensitive to drought in that region. See [[Wheat Futures]] for the full three class map (Chicago SRW, Kansas City HRW, Minneapolis HRS).

## Why it matters (commodities and FX)

KC wheat is the protein and quality leg of the US wheat complex. Its price relative to Chicago is not a directional wheat bet, it is a bet on protein scarcity and Southern Plains weather, traded directly as the [[KC-Chicago Wheat Spread]]. Because HRW is concentrated in Kansas, Oklahoma, and Texas, a single regional drought can send KC to a large premium over Chicago even when the overall wheat market is oversupplied. That regional concentration is exactly why KC is a cleaner drought and [[Quality Spread]] instrument than the more globally diversified [[Wheat Futures|Chicago benchmark]]. HRW is also the main US bread wheat export class, so it links to milling demand from importers who need protein.

## Concrete example

**Concrete:** On 2026-07-02 KC wheat settles at 638.50 cents/bushel, up 22.14% over the trailing year. Persistent drought across western Kansas and the Oklahoma panhandle has cut HRW yields and protein is scarce, so millers pay up for the bread wheat class. A trader long 2 KE from 610 cents gains (638.50 minus 610) cents times 12.50 USD times 2 = 712.50 USD, since KE carries the same 5,000 bushel size and 12.50 USD per cent as Chicago. The fail case: drought breaks, timely rain hits the Southern Plains during grain fill, the HRW crop comes in larger and higher protein than feared, and KC falls back toward 590 cents while the premium over Chicago collapses. The long 2 lots from 610 now loses (610 minus 590) times 12.50 times 2 = 500 USD, and the protein scarcity story that justified the price is gone in a fortnight. HRW rallies live and die on Kansas rain.

**Simplified:** KC wheat (KE) is the price of 5,000 bushels of hard red winter wheat, the high protein bread wheat grown in Kansas, Oklahoma, and Texas. It trades at a premium or discount to Chicago ([[Wheat Futures]]) depending on protein and HRW supply. Southern Plains drought is the main driver. Same contract size and tick value as Chicago, so 1 cent is 12.50 USD per contract. The cleanest way to trade it is the spread against Chicago, see [[KC-Chicago Wheat Spread]].

## Contract specifications

| Field | Value |
|-------|-------|
| Exchange | CME (former KCBT) |
| Ticker | KE (Kansas City HRW) |
| Contract size | 5,000 bushels |
| Tick size | 1/4 cent per bushel |
| Tick value | 12.50 USD |
| Trading hours | 19:00 to 07:45 and 08:30 to 13:20 CT |
| Settlement | Physical delivery |
| Expiry months | Mar, May, Jul, Sep, Dec |
| Currency | USD (cents per bushel) |

## Fundamentals

### Supply drivers
- Southern Plains concentration: Kansas, Oklahoma, and Texas dominate HRW. Regional drought is the single biggest risk
- Winter wheat calendar: planted in the fall, dormant over winter, harvested May to July. Fall establishment and spring grain fill are the key weather windows
- Protein content is a supply variable in its own right. Heat and drought during grain fill can raise protein but cut yield, or a big soft crop can flood the market with low protein wheat
- Competes with the other US classes ([[Wheat Futures|Chicago SRW]], Minneapolis HRS) and with global HRW substitutes from Russia and Argentina
- Acreage has been eroded over decades as row crops win better land

### Demand drivers
- Bread and hard baked goods milling: protein and gluten strength are what buyers pay for
- Exports: HRW is the main US bread wheat export class, sold into Latin America, the Middle East, North Africa, and Asia
- Blending demand: millers blend high protein HRW to lift the protein of a flour grist, so the protein premium is a demand pull
- Feed use only when HRW is weather damaged or cheap relative to [[Corn Futures|corn]]

### Seasonality
HRW winter wheat is harvested May to July, the same window as Chicago SRW, which is the seasonal supply pulse and often the price low. The pre harvest spring drought scare in the Southern Plains (Apr to Jun) is the recurring seasonal setup that widens the KC premium. See [[Seasonality]].

## Key data and reports

- [[WASDE]]: monthly USDA balance sheet, including the by class HRW numbers
- USDA Winter Wheat Seedings (January): HRW planted area
- USDA Crop Progress (weekly): Kansas, Oklahoma, and Texas condition ratings, the drought read
- Kansas Wheat Quality Tour (May): field scouting of the HRW crop, yield and protein
- USDA Grain Stocks (quarterly): HRW carryout
- CFTC COT report: managed money positioning in KE

## Curve structure

KC wheat, like Chicago, tends toward [[Contango]] when world and US stocks are ample and storage is rewarded, and inverts to [[Backwardation]] on genuine HRW tightness such as a severe Southern Plains drought. The more informative structure for KC is not its own calendar spread but its price relative to Chicago, the [[KC-Chicago Wheat Spread]], which is the market's live read on protein and HRW supply. See [[Forward Curve]].

## Key spreads and relative value

- **[[KC-Chicago Wheat Spread]]:** the core trade. KC (HRW) premium or discount to Chicago (SRW). Widens on Southern Plains drought and high protein demand, flips to a discount in HRW gluts
- **KC versus Minneapolis:** HRW against the highest protein hard red spring, a finer [[Quality Spread]] along the protein ladder
- **KC versus [[Corn Futures|corn]]:** feed substitution when HRW is weather damaged and cheap

## Important relationships

- Class and quality spread with [[Wheat Futures|Chicago SRW]] via the [[KC-Chicago Wheat Spread]], driven by relative protein supply, see [[Quality Spread]]
- Southern Plains drought sensitivity is higher than for the geographically diversified Chicago contract
- Inverse link between the HRW [[Stocks to Use Ratio]] and the KC premium: tight high protein stocks widen the premium
- Global HRW competition from Russia and Argentina caps the export premium

## Trading notes

*Add personal observations here.*

## Related instruments

- [[Wheat Futures]]
- [[Corn Futures]]

## Related concepts

- [[KC-Chicago Wheat Spread]]
- [[Quality Spread]]
- [[WASDE]]
- [[Seasonality]]
- [[Stocks to Use Ratio]]
