---
aliases: [KC-Chicago wheat spread, HRW-SRW spread, Kansas City Chicago wheat, KC premium, wheat class spread]
tags:
  - "#agri/grains/wheat"
date-added: "2026-07-03"
---

# KC-Chicago Wheat Spread

## Core Thesis

The KC-Chicago wheat spread trades the price difference between two US wheat classes that differ in protein and milling use. Kansas City ([[KC Wheat Futures]]) is hard red winter (HRW), the high protein bread wheat grown in the Southern Plains. Chicago ([[Wheat Futures]]) is soft red winter (SRW), the low protein wheat for cakes and pastries grown in the eastern Midwest. The spread is quoted as KC minus Chicago, so a positive number is the KC premium. That premium is the market price of protein and of HRW supply tightness. When the Southern Plains bakes in drought and millers need protein, KC pulls away from Chicago and the premium widens. When HRW is abundant and high protein, the premium narrows or flips to a discount. This is a class and [[Quality Spread]], not a directional wheat bet.

The mechanism is not acreage substitution the way the [[Soybean-Corn Spread]] works, because a farmer cannot turn SRW into HRW. The two crops are grown in different regions with different agronomy, so the spread reprices the relative scarcity of protein rather than triggering a supply switch. That makes it a slower and more regime dependent mean reversion than acreage spreads. It reverts, but only once the drought or glut that drove it resolves through a new harvest.

## Mechanics

### Calculating the Spread

**KC-Chicago Spread = KC wheat price (cents/bushel) minus Chicago wheat price (cents/bushel)**

Example: KC at 638.50 cents/bu, Chicago at 600.25 cents/bu. Spread = plus 38.25 cents/bu, a KC premium. A negative value would be a KC discount, meaning HRW is trading below SRW, which happens in HRW gluts.

Both contracts are 5,000 bushels with a tick of 1/4 cent worth 12.50 USD, so the spread is priced directly in cents per bushel and 1 cent of spread move is 12.50 USD per 1:1 pair.

### Entry Criteria
- Premium is compressed or negative going into a Southern Plains drought risk window (Apr to Jun pre harvest), betting on a widening
- Premium is stretched to an extreme after a drought scare, betting on reversion once rain returns or harvest confirms the crop
- USDA condition ratings for Kansas, Oklahoma, and Texas diverging from the SRW growing regions
- [[WASDE]] by class balance sheet showing HRW tightening or loosening relative to SRW
- Use [[Z-Score]] on the spread against a class specific mean, since the fair premium drifts with the protein cycle

### Exit Criteria
- Premium reverts to its recent regime mean after the driver resolves
- The catalyst plays out: drought breaks (exit a long premium) or a supply shock hits (exit a short premium)
- Harvest confirms HRW yield and protein, removing the uncertainty that justified the extreme
- Time stop: if the weather driver has passed and the spread has not reverted, reassess. Class spreads can stay dislocated for a full [[Crop Year]]

### Position Sizing
Bushel neutral 1:1, both contracts 5,000 bushels: long 1 KE, short 1 ZW for a long premium position. Because both legs are the same size, currency, and tick value, the spread is naturally dollar neutral per bushel and no ratio adjustment is needed, unlike the [[Soybean-Corn Spread]]. CME recognizes the inter market wheat spread, so margin is reduced versus two outright legs.

## Instruments Used
- KC Wheat Futures CME/KCBT (KE), 5,000 bushels, HRW, see [[KC Wheat Futures]]
- Chicago Wheat Futures CBOT (ZW), 5,000 bushels, SRW, see [[Wheat Futures]]
- New crop July or September months for pre harvest drought trades
- Matched expiries to keep the spread a pure class spread rather than a mixed class and calendar spread

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Weather in one region resolving fast and reversing the protein signal (Southern Plains rain collapses the KC premium in days) |
| Max Loss Scenario | A regional shock to the leg you are short: a Kansas drought while short the KC premium, or an HRW glut while long it |
| Hedged Exposure | Flat wheat direction is largely hedged, both legs are wheat |
| Unhedged Exposure | Class and protein basis risk, regional weather divergence, Black Sea supply shifting relative HRW versus SRW export demand |
| Margin Requirements | CME recognized inter market spread, margin reduction versus outright legs |

## Edge Source

The edge is understanding protein economics and regional weather better than a flat wheat trader. HRW protein is a specific, priced attribute, and its scarcity is driven by a concentrated growing region (Kansas, Oklahoma, Texas) that can be modeled from USDA condition ratings, the Kansas Wheat Quality Tour, and drought monitors. Because HRW is regionally concentrated while SRW and the global crop are diversified, the spread isolates a tradable regional signal that outright wheat washes out. See [[Quality Spread]].

Moderate [[Seasonality]]: the KC premium tends to build into the Apr to Jun Southern Plains drought risk window and release into the May to July harvest if the crop is made. Reversion is anchored not by a fast supply switch but by the eventual harvest, so the [[Mean Reversion]] horizon is longer and more regime dependent than acreage spreads.

## When It Works / When It Fails

### Works Well When
- Southern Plains drought tightens HRW protein while SRW regions get normal weather, cleanly widening the premium
- The premium is at a historical extreme and the driving weather event has clearly passed, setting up reversion
- [[WASDE]] by class balances confirm the HRW versus SRW tightness divergence
- Protein premiums in the cash market corroborate the futures spread

### Fails When
- Both classes move together on a global driver (Black Sea disruption, a broad world supply shock) and the class divergence never materializes
- A fast weather reversal in one region round trips the spread before reversion can be captured
- Feed demand or a big low protein crop distorts the SRW leg independently of HRW
- Export demand shifts between classes (a large HRW tender or cancellation) moves one leg on flow, not fundamentals

## Historical Examples

**2011 Southern Plains Drought:** A severe Texas and Oklahoma drought hammered HRW while the eastern SRW belt fared better. The KC premium over Chicago widened sharply as protein went scarce. Traders long the premium into the drought were paid, and the spread reverted only after the following year's crop.

**2014 HRW Freeze and Drought:** Another Southern Plains stress year lifted the KC premium as HRW yields and protein disappointed. The spread stayed elevated through the marketing year, illustrating that class spreads can remain dislocated for a full [[Crop Year]] rather than snapping back quickly.

**2017 SRW Glut:** Large soft red winter supplies and weak protein premiums held Chicago heavy while HRW held firmer, sustaining a KC premium. The episode shows the spread can be driven by the SRW leg loosening as much as by the HRW leg tightening.

## Concrete Example (Current or Recent)

**Concrete:** On 2026-07-02 KC settles at 638.50 cents/bu and Chicago at 600.25 cents/bu, so the spread is plus 38.25 cents/bu, a KC premium, up 7.00 cents on the day (roughly plus 22.4% on the spread), plus 118.6% over 3 months and plus 215.0% over the year. Southern Plains drought and milling protein tightness are blowing out the HRW premium. A trader who believes the drought is now fully priced sells the premium: sell 1 KE at 638.50, buy 1 ZW at 600.25, bushel neutral 1:1. Target: reversion to plus 20 cents as forecast rain reaches Kansas. If the spread narrows to plus 20, the gain is (38.25 minus 20) cents times 12.50 USD = 228.13 USD per 1:1 pair. The fail case: the drought intensifies, protein tightens further, and the premium widens to plus 55 cents. The short premium loses (55 minus 38.25) times 12.50 = 209.38 USD per pair. Stop the trade if the spread breaks plus 52.

**Simplified:** Kansas City wheat is high protein bread wheat, Chicago wheat is low protein pastry wheat. The spread (KC minus Chicago) is the price of protein and of Kansas drought. It widens when the Southern Plains dries out and millers scramble for protein, and it narrows or flips negative when hard red winter is plentiful. You cannot switch one crop into the other, so it reverts only when a new harvest resolves the scarcity, which makes it slower than acreage spreads. Trade it 1:1, both contracts are 5,000 bushels.

## Related Strategies
- [[Inter-Commodity Spread]]
- [[Quality Spread]]
- [[Spread Trade]]
- [[Relative Value Trade]]
- [[Soybean-Corn Spread]]

## Related Concepts
- [[Quality Spread]]
- [[WASDE]]
- [[Seasonality]]
- [[Mean Reversion]]
- [[Stocks to Use Ratio]]
- [[Z-Score]]
- [[Crop Year]]

---
*Status: #seedling | Last reviewed: 2026-07-03*
