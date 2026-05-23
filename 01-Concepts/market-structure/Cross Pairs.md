---
aliases: [cross pairs, FX crosses, cross rates]
tags:
  - "#fx/g10"
date-added: "2026-03-20"
---

# Cross Pairs

## Definition
Cross pairs are [[Currency Pair|currency pairs]] without USD on either side. Examples: EUR/GBP, EUR/JPY, AUD/NZD, GBP/JPY, EUR/CHF. Historically, converting between 2 non USD currencies required 2 transactions through the dollar, so crosses were literally "crossed" through USD. Today many crosses trade directly with dedicated liquidity, though interbank often constructs cross rates from 2 USD legs. Cross pairs isolate the bilateral relationship between 2 economies without USD noise, useful for targeted macro views.

## Why it matters (commodities and FX)
Cross pairs let commodity traders hedge or express views on relative commodity exporters. AUD/CAD isolates iron ore vs crude oil economies. NOK/SEK separates Norway's oil driven economy from Sweden's manufacturing. For systematic FX, crosses expand the universe from 7 [[Major Pairs|majors]] to 45 total [[G10 Currencies|G10]] pairs, improving diversification. Cross signals capture themes invisible in majors: if EUR/USD and GBP/USD both fall, the real story might be EUR/GBP divergence driven by ECB vs BoE policy.

## Concrete example

**Concrete:** Early 2024, BoJ signals potential exit from negative rates; RBA holds at 4.35%. A trader shorts AUD/JPY at 98.00 betting on JPY strength. AUD/JPY falls to 94.00, 400 pip gain. On AUD 10 million, roughly 4 million JPY per pip, ~$268,000 profit. Failure mirror: if global risk appetite surges, AUD/JPY rallies because AUD is risk on and JPY is risk off. Late 2023, AUD/JPY rallied from 94 to 98 in a single week on improved China sentiment, punishing the same short.

**Simplified:** A cross is just a currency pair that does not include the US dollar. They let you bet on one economy versus another directly, without the dollar's moves clouding the view. If you want to express that the eurozone is stronger than the UK, you trade EUR/GBP rather than EUR/USD and GBP/USD separately. Liquidity is generally lower than the major pairs but still very deep for the big crosses.

## Key mechanics and formulas
- **Cross rate from USD pairs**: EUR/GBP = EUR/USD ÷ GBP/USD. If EUR/USD = 1.0850 and GBP/USD = 1.2650, EUR/GBP = 0.8577.
- **Cross rate with 2 indirect quotes**: EUR/JPY = EUR/USD × USD/JPY. If EUR/USD = 1.0850 and USD/JPY = 150.00, EUR/JPY = 162.75.
- **Spread in crosses**: Typically wider than majors because cross spread = leg 1 spread + leg 2 spread when routed through USD.
- **Number of G10 crosses**: 45 total G10 pairs minus 7 majors = 38 cross pairs (some NOK/SEK USD pairs classify as minor rather than major).
- **Triangular arbitrage**: If the cross rate deviates from the implied rate, arbitrageurs trade all 3 pairs to close the gap.

## Prerequisites
- [[Currency Pair]]
- [[Major Pairs]]
- [[Spot Rate]]
- [[G10 Currencies]]

## Related concepts (learn next)
- [[Interest Rate Differential]]: driver of [[Forward Points|forward points]] on crosses.
- [[Carry Trade]]: many popular carries are crosses (AUD/JPY, NZD/JPY, NOK/SEK).
- [[Covered Interest Parity]]: applies to crosses; the forward cross must reflect the rate gap.
- [[FX Swap]]: cross currency swaps allow direct funding without USD.
- [[Monetary Policy Divergence]]: primary driver of cross trends.
- [[Petrocurrency]]: NOK/SEK and AUD/CAD are commodity RV crosses linking energy and mining.
- [[Dollar Index]]: by definition excluded from crosses.

## Common misconceptions

**Crosses are illiquid.** EUR/GBP, EUR/JPY, and GBP/JPY rank among the most liquid pairs globally, rivaling some USD majors.

**Crosses remove all USD influence.** Both currencies can be USD driven. If the dollar surges, both legs of EUR/GBP may fall against USD; the cross itself may barely move or move unpredictably depending on relative beta.

**Cross rates are independent prices.** Most crosses derive from 2 USD legs in interbank. EUR/GBP is really EUR/USD divided by GBP/USD; temporary dislocations get arbitraged away.

## Sources
- Lyons, Richard K., *The Microstructure Approach to Exchange Rates*, MIT Press, 2001.
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- Chaboud, A. et al., "Rise of the Machines: Algorithmic Trading in the Foreign Exchange Market," Journal of Finance, 2014.
