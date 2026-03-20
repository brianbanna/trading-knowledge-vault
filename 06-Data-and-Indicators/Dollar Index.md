---
aliases: [DXY, dollar index, US dollar index, USDX]
tags:
  - "#fx/g10"
  - "#macro"
date-added: "2026-03-20"
---

# Dollar Index

## Definition
The Dollar Index (DXY) is a weighted geometric mean of the US dollar's value against a basket of 6 [[G10 Currencies|G10 currencies]]: EUR (57.6%), JPY (13.6%), GBP (11.9%), CAD (9.1%), SEK (4.2%), and CHF (3.6%). Created in 1973 after the collapse of the Bretton Woods system, DXY was set to a base value of 100. The index is calculated continuously and trades as a futures contract on ICE. Because EUR carries nearly 58% weight, DXY is heavily influenced by EUR/USD moves. A rising DXY signals broad dollar strength; a falling DXY signals dollar weakness. It serves as the single most watched summary measure of USD performance across developed market currencies.

## Why it matters (commodities and FX)
Commodities are globally priced in USD, so DXY has a well documented inverse correlation with commodity prices. When DXY rises, commodities become more expensive in foreign currency terms, dampening demand and pushing prices lower. Crude oil, gold, copper, and agricultural commodities all exhibit negative DXY correlation ranging from −0.3 to −0.7 depending on the period. For FX traders, DXY provides a quick read on whether a [[Major Pairs|major pair]] move is driven by broad USD dynamics or pair specific factors. If EUR/USD is falling but DXY is flat, the move is likely EUR specific (perhaps ECB related) rather than a dollar story.

## Concrete example
In September 2022, DXY surged to a 20 year high of 114.78 as the Federal Reserve aggressively hiked rates while other central banks lagged. This correlated with WTI crude falling from 120 to 80 USD/barrel and gold dropping from 2,050 to 1,620 USD/oz. A macro trader who went long DXY futures at 105 in June and held to 114 captured a 9 point move worth 9,000 USD per contract (1,000 USD per point). Conversely, a trader who went long DXY at 114 expecting continued strength suffered as DXY reversed to 101 by July 2023 when the Fed signaled a pause, losing 13 points or 13,000 USD per contract.

## Key mechanics and formulas
- **DXY formula**: DXY = 50.14348112 × (EUR/USD)^(−0.576) × (USD/JPY)^(0.136) × (GBP/USD)^(−0.119) × (USD/CAD)^(0.091) × (USD/SEK)^(0.042) × (USD/CHF)^(0.036).
- **Weights**: EUR 57.6%, JPY 13.6%, GBP 11.9%, CAD 9.1%, SEK 4.2%, CHF 3.6%.
- **Futures**: ICE DXY futures; 1 point = 1,000 USD per contract.
- **Approximate DXY move from EUR/USD**: Because EUR is ~58% weight, a 1% move in EUR/USD moves DXY roughly 0.58% in the opposite direction.
- **No AUD, NZD, or NOK**: Despite their G10 status, these currencies are excluded from DXY because the basket has not been updated since 1973.

## Prerequisites
- [[G10 Currencies]]
- [[Currency Pair]]
- [[Major Pairs]]
- [[Spot Rate]]

## Related concepts (learn next)
- [[Major Pairs]]: the individual pairs that compose DXY; trading EUR/USD is the closest proxy for DXY directional exposure.
- [[Monetary Policy Divergence]]: the primary driver of DXY trends, as Fed policy versus other central banks sets the direction.
- [[Interest Rate Differential]]: DXY tracks the weighted average rate differential between the US and the 6 basket currencies.
- [[Real Effective Exchange Rate]]: a broader, inflation adjusted alternative to DXY that includes more trading partners.
- [[Petrocurrency]]: CAD, NOK, and AUD move inversely to DXY on the commodity channel, though only CAD is in the basket.
- [[Terms of Trade]]: a strong DXY hurts commodity exporters' terms of trade by compressing their local currency revenues.
- [[Cross Pairs]]: crosses strip out USD effects, useful when DXY is dominating all major pair moves simultaneously.

## Common misconceptions
1. **DXY represents the global dollar**: The basket excludes CNY, MXN, KRW, INR, BRL, AUD, and NZD. The Federal Reserve's trade weighted dollar index (broader) is a more representative measure.
2. **DXY and EUR/USD are interchangeable**: While highly correlated (about −0.97), they diverge when JPY, GBP, or CAD move independently. In late 2022, DXY fell sharply on JPY strength after a Bank of Japan policy shift, even as EUR/USD was relatively stable.
3. **A rising DXY is always bad for commodities**: The correlation is statistical, not causal. In early 2022, both DXY and oil rose simultaneously because the Fed was tightening (bullish USD) while the Ukraine conflict disrupted oil supply (bullish oil). Context matters.

## Sources
- ICE, "US Dollar Index Futures: Contract Specifications."
- Fatum, Rasmus and Scholnick, Barry, "Do Exchange Rates Respond to Day to Day Changes in Monetary Policy Expectations?" Journal of Monetary Economics, 2008.
- Federal Reserve Bank of St. Louis, FRED database (DXY historical data).
