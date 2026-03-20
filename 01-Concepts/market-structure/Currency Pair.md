---
aliases: [currency pair, FX pair, forex pair]
tags:
  - "#fx"
date-added: "2026-03-20"
---

# Currency Pair

## Definition
A currency pair is the quotation of 2 different currencies, where the value of 1 currency (the base) is expressed in terms of the other (the quote). The base currency is listed first and the quote currency second, separated by a slash. For example, EUR/USD = 1.0850 means 1 euro costs 1.0850 US dollars. The convention for which currency is base and which is quote follows an established hierarchy: EUR is always base against all other currencies, then GBP, then AUD, then NZD, then USD. Currency pairs are the fundamental unit of trading in foreign exchange markets, and every FX transaction involves simultaneously buying 1 currency and selling another.

## Why it matters (commodities and FX)
Commodity prices are predominantly quoted in USD, so any non USD commodity producer or consumer has inherent currency pair exposure. A European refiner buying crude oil priced in USD must transact in EUR/USD. Understanding the quoting convention prevents costly errors: buying EUR/USD is buying euros and selling dollars, not the reverse. For systematic traders, the choice of which [[Currency Pair|pairs]] to trade directly affects liquidity, transaction costs, and the ability to isolate specific macro themes.

## Concrete example
A trader goes long 5 million GBP/USD at 1.2650. This means buying 5 million GBP and simultaneously selling 6,325,000 USD (5,000,000 × 1.2650). If GBP/USD rises to 1.2730, the profit is 80 [[Pip|pips]] × 5,000,000 = 40,000 USD. Now consider the cross pair EUR/GBP at 0.8570. A trader long EUR/GBP is buying euros and selling pounds, isolating the bilateral EUR vs GBP relationship without any direct USD exposure. If EUR/GBP falls to 0.8500, the loss is 70 pips on the position.

## Key mechanics and formulas
- **Base / Quote**: EUR/USD = 1.0850 means 1 EUR = 1.0850 USD. Buying the pair = buying base, selling quote.
- **Direct quote** (from a US perspective): USD is the quote currency (EUR/USD, GBP/USD).
- **Indirect quote** (from a US perspective): USD is the base currency (USD/JPY, USD/CHF).
- **Cross rate derivation**: EUR/GBP = EUR/USD ÷ GBP/USD. If EUR/USD = 1.0850 and GBP/USD = 1.2650, then EUR/GBP = 1.0850 / 1.2650 = 0.8577.
- **Reciprocal**: USD/JPY = 150.00 means JPY/USD = 1 / 150.00 = 0.006667.

## Prerequisites
- [[Spot Rate]]
- [[Pip]]
- [[Big Figure]]

## Related concepts (learn next)
- [[Major Pairs]]: the most liquid USD pairs (EUR/USD, USD/JPY, GBP/USD), accounting for the majority of global FX volume.
- [[Cross Pairs]]: pairs that exclude USD entirely, used to isolate bilateral currency relationships.
- [[G10 Currencies]]: the 10 most liquid currencies from which the most traded pairs are constructed.
- [[EM Currencies]]: higher yielding, less liquid currencies that form pairs with wider [[Bid-Ask Spread|spreads]].
- [[Pip]]: the standard unit of price change in a currency pair (0.0001 for most, 0.01 for JPY pairs).
- [[Dollar Index]]: a composite measure of USD against a basket, effectively a synthetic currency pair.

## Common misconceptions
1. **The first currency is always what you are buying**: The base currency is what you buy when you go long the pair, but going short the pair means you are selling the base and buying the quote. The direction depends on the trade, not the quotation.
2. **All pairs move similarly**: EUR/USD and USD/JPY can move in opposite directions on the same day because the base/quote convention flips the USD side. A strong dollar means EUR/USD falls but USD/JPY rises.
3. **Cross pairs are exotic**: Crosses like EUR/GBP and AUD/NZD are highly liquid [[G10 Currencies|G10]] pairs. "Exotic" refers to pairs involving [[EM Currencies|EM currencies]], not simply the absence of USD.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- Levich, Richard M., *International Financial Markets*, 2nd ed.
- CME Group, "FX Products: Understanding FX Futures and Options."
