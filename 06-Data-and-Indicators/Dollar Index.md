---
aliases: [DXY, dollar index, US dollar index, USDX]
tags:
  - "#fx/g10"
  - "#macro"
date-added: "2026-03-20"
---

# Dollar Index

## Definition
The Dollar Index (DXY) is a weighted geometric mean of USD against a basket of 6 [[G10 Currencies|G10 currencies]]: EUR (57.6%), JPY (13.6%), GBP (11.9%), CAD (9.1%), SEK (4.2%), CHF (3.6%). Created in 1973 after Bretton Woods, base 100. DXY is calculated continuously and trades as a futures contract on ICE. EUR's 58% weight means DXY is dominated by EUR/USD. Rising DXY = broad USD strength, falling DXY = USD weakness. It is the single most watched summary of USD performance across developed markets.

## Why it matters (commodities and FX)
Commodities are priced in USD, so DXY has an inverse correlation with commodity prices ranging from −0.3 to −0.7 depending on period. Rising DXY makes commodities more expensive in foreign currency terms, dampening demand. Crude, gold, copper, and ags all show negative DXY correlation. For FX traders, DXY separates broad USD moves from pair specific factors. EUR/USD falling with flat DXY is EUR specific (ECB news), not a dollar story.

## Concrete example
**Concrete:** September 2022, DXY surges to a 20 year high of 114.78 as the Fed hikes aggressively while other central banks lag. WTI drops from $120 to $80, gold from $2,050 to $1,620. Macro trader long 10 DXY futures from 105 in June holds to 114 = 9 points × $1,000/point × 10 contracts = $90,000.

**Simplified:** DXY is one number that summarizes how strong the dollar is against a basket of major currencies. When it rises, the dollar is broadly strong; commodities priced in dollars get more expensive in local currency and demand falls. When it drops, commodities get cheaper globally and prices rise. Most macro traders glance at DXY every morning to decide if the day is a USD up day or a USD down day.

## Key mechanics and formulas
- **DXY formula:** DXY = 50.14348112 × (EUR/USD)^(−0.576) × (USD/JPY)^(0.136) × (GBP/USD)^(−0.119) × (USD/CAD)^(0.091) × (USD/SEK)^(0.042) × (USD/CHF)^(0.036)
- **Weights:** EUR 57.6%, JPY 13.6%, GBP 11.9%, CAD 9.1%, SEK 4.2%, CHF 3.6%
- **Futures:** ICE DXY futures; 1 point = $1,000 per contract
- **EUR/USD pass through:** 1% move in EUR/USD moves DXY ~0.58% inversely
- **No AUD, NZD, NOK:** despite G10 status, excluded because the basket has not been updated since 1973

## Prerequisites
- [[G10 Currencies]]
- [[Currency Pair]]
- [[Major Pairs]]
- [[Spot Rate]]

## Related concepts (learn next)
- [[Major Pairs]]: EUR/USD is the closest single pair proxy for DXY exposure.
- [[Monetary Policy Divergence]]: primary driver of DXY trends.
- [[Interest Rate Differential]]: DXY tracks the weighted rate differential vs basket.
- [[Real Effective Exchange Rate]]: a broader, inflation adjusted alternative.
- [[Petrocurrency]]: CAD, NOK, AUD move inversely to DXY on the commodity channel.
- [[Terms of Trade]]: strong DXY compresses commodity exporters' local currency revenues.
- [[Cross Pairs]]: strip out USD when DXY dominates all majors.

## Common misconceptions

**"DXY represents the global dollar."** The basket excludes CNY, MXN, KRW, INR, BRL, AUD, NZD. The Fed's trade weighted broad dollar index is more representative.

**"DXY and EUR/USD are interchangeable."** Correlation is ~−0.97 but they diverge on JPY, GBP, or CAD specific moves. In late 2022, DXY fell sharply on JPY strength after a BoJ shift while EUR/USD was stable.

**"Rising DXY is always bearish for commodities."** Statistical, not causal. Early 2022, DXY and oil both rose: Fed tightening (bullish USD) plus Ukraine supply disruption (bullish oil). Context matters.

## Sources
- ICE, "US Dollar Index Futures: Contract Specifications."
- Fatum, Rasmus and Scholnick, Barry, "Do Exchange Rates Respond to Day to Day Changes in Monetary Policy Expectations?" Journal of Monetary Economics, 2008.
- Federal Reserve Bank of St. Louis, FRED database.
