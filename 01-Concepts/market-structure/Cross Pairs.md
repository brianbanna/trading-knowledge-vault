---
aliases: [cross pairs, FX crosses, cross rates]
tags:
  - "#fx/g10"
date-added: "2026-03-20"
---

# Cross Pairs

## Definition
Cross pairs (or crosses) are [[Currency Pair|currency pairs]] that do not include the US dollar on either side. Examples include EUR/GBP, EUR/JPY, AUD/NZD, GBP/JPY, and EUR/CHF. Historically, converting between 2 non USD currencies required 2 separate transactions through the dollar, so crosses were literally "crossed" through USD. Today, many crosses trade directly with dedicated liquidity, though the interbank market still often constructs cross rates from 2 USD legs. Cross pairs allow traders to isolate the bilateral relationship between 2 economies without the noise of USD fluctuations, making them valuable for expressing targeted macro views.

## Why it matters (commodities and FX)
Cross pairs let commodity traders hedge or express views on relative commodity exporters. AUD/CAD isolates iron ore versus crude oil economies. NOK/SEK separates Norway's oil driven economy from Sweden's manufacturing base. For systematic FX strategies, crosses expand the investable universe from 7 [[Major Pairs|major pairs]] to 45 total [[G10 Currencies|G10]] pairs, significantly improving diversification. Cross pair signals can capture themes invisible in major pairs: if both EUR/USD and GBP/USD are falling, the real story might be EUR/GBP divergence due to ECB vs Bank of England policy differences.

## Concrete example
In early 2024, the Bank of Japan signals a potential exit from negative rates while the Reserve Bank of Australia holds at 4.35%. A trader shorts AUD/JPY at 98.00, betting on JPY strength relative to AUD. AUD/JPY falls to 94.00, generating a 400 [[Pip|pip]] gain. On a 10 million AUD position, that is roughly 4 million JPY per pip, so 400 × ~6,700 USD per pip = approximately 268,000 USD profit. Failure scenario: if global risk appetite surges, AUD/JPY can rally sharply because AUD is a risk on currency and JPY is risk off. In late 2023, AUD/JPY rallied from 94 to 98 in a single week on improved China sentiment, punishing the same short trade.

## Key mechanics and formulas
- **Cross rate from USD pairs**: EUR/GBP = EUR/USD ÷ GBP/USD. If EUR/USD = 1.0850 and GBP/USD = 1.2650, then EUR/GBP = 0.8577.
- **Cross rate with 2 indirect quotes**: EUR/JPY = EUR/USD × USD/JPY. If EUR/USD = 1.0850 and USD/JPY = 150.00, then EUR/JPY = 162.75.
- **Spread in crosses**: Typically wider than majors because the cross spread = spread of leg 1 + spread of leg 2 when routed through USD.
- **Number of G10 crosses**: 45 total G10 pairs minus 7 major pairs = 38 cross pairs (though NOK and SEK pairs with USD are sometimes classified as minor rather than major).
- **Triangular arbitrage**: If the cross rate deviates from the rate implied by the 2 USD legs, arbitrageurs will trade all 3 pairs to close the gap.

## Prerequisites
- [[Currency Pair]]
- [[Major Pairs]]
- [[Spot Rate]]
- [[G10 Currencies]]

## Related concepts (learn next)
- [[Interest Rate Differential]]: the driver of [[Forward Points|forward points]] on crosses, reflecting the rate gap between the 2 non USD economies.
- [[Carry Trade]]: many popular carry trades are expressed as crosses (AUD/JPY, NZD/JPY, NOK/SEK).
- [[Covered Interest Parity]]: applies equally to crosses; the forward cross rate must reflect the interest rate gap.
- [[FX Swap]]: cross currency swaps allow direct funding in the 2 currencies without USD intermediation.
- [[Monetary Policy Divergence]]: the primary fundamental driver of cross pair trends.
- [[Petrocurrency]]: NOK/SEK and AUD/CAD are commodity relative value crosses linking energy and mining themes.
- [[Dollar Index]]: by definition excluded from crosses, making crosses useful for non USD macro views.

## Common misconceptions
1. **Crosses are illiquid**: EUR/GBP, EUR/JPY, and GBP/JPY are among the most liquid pairs in the world, rivaling some USD majors in daily volume.
2. **Crosses remove all USD influence**: While crosses exclude direct USD exposure, both currencies in the cross can be influenced by USD moves. If the dollar surges, both legs of EUR/GBP may fall against USD, but the cross itself may barely move or may move unpredictably depending on relative beta.
3. **Cross rates are independent prices**: Most crosses are still derived from 2 USD legs in the interbank market. The "price" of EUR/GBP is really EUR/USD divided by GBP/USD, and temporary dislocations are quickly arbitraged away.

## Sources
- Lyons, Richard K., *The Microstructure Approach to Exchange Rates*, MIT Press, 2001.
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- Chaboud, A. et al., "Rise of the Machines: Algorithmic Trading in the Foreign Exchange Market," Journal of Finance, 2014.
