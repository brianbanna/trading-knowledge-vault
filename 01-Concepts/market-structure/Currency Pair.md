---
aliases: [currency pair, FX pair, forex pair]
tags:
  - "#fx"
date-added: "2026-03-20"
---

# Currency Pair

## Definition
A currency pair quotes 2 currencies, with the value of 1 (the base) expressed in units of the other (the quote). Base first, quote second, separated by a slash. EUR/USD = 1.0850 means 1 euro costs 1.0850 US dollars. The base/quote hierarchy follows a fixed order: EUR is base against all others, then GBP, then AUD, then NZD, then USD. Currency pairs are the fundamental unit of FX trading; every transaction simultaneously buys one currency and sells another.

## Why it matters (commodities and FX)
Commodity prices are predominantly quoted in USD, so any non USD producer or consumer carries inherent currency pair exposure. A European refiner buying USD priced crude must transact EUR/USD. Knowing the convention avoids costly errors: buying EUR/USD is buying euros and selling dollars, not the reverse. For systematic traders, the choice of [[Currency Pair|pairs]] directly affects liquidity, costs, and the ability to isolate macro themes.

## Concrete example

**Concrete:** Trader goes long GBP 5 million GBP/USD at 1.2650, buying GBP 5 million and selling USD 6,325,000. GBP/USD rises to 1.2730: profit = 80 [[Pip|pips]] × 5,000,000 = $40,000. Now consider EUR/GBP at 0.8570. Long EUR/GBP buys euros and sells pounds, isolating the EUR vs GBP relationship without direct USD exposure. EUR/GBP falls to 0.8500: loss of 70 pips on the position.

**Simplified:** A currency pair is just a price for one currency expressed in another. The first currency listed is what you are buying or selling; the second is what you pay or receive. Long EUR/USD means buying euros and paying with dollars. The pip is the smallest standard increment, and pair conventions (which currency goes first) are fixed by market norm.

## Key mechanics and formulas
- **Base / Quote**: EUR/USD = 1.0850 means 1 EUR = 1.0850 USD. Buying the pair = buying base, selling quote.
- **Direct quote** (US perspective): USD is quote (EUR/USD, GBP/USD).
- **Indirect quote** (US perspective): USD is base (USD/JPY, USD/CHF).
- **Cross rate derivation**: EUR/GBP = EUR/USD ÷ GBP/USD. If EUR/USD = 1.0850 and GBP/USD = 1.2650, EUR/GBP = 0.8577.
- **Reciprocal**: USD/JPY = 150.00 means JPY/USD = 1 / 150.00 = 0.006667.

## Prerequisites
- [[Spot Rate]]
- [[Pip]]
- [[Big Figure]]

## Related concepts (learn next)
- [[Major Pairs]]: the most liquid USD pairs, dominant share of global FX volume.
- [[Cross Pairs]]: pairs excluding USD, useful to isolate bilateral relationships.
- [[G10 Currencies]]: the 10 most liquid currencies, source of the most traded pairs.
- [[EM Currencies]]: higher yielding, less liquid, wider [[Bid-Ask Spread|spreads]].
- [[Pip]]: standard unit of price change (0.0001 for most, 0.01 for JPY pairs).
- [[Dollar Index]]: composite USD vs a basket, a synthetic currency pair.

## Common misconceptions

**The first currency is always what you are buying.** Base is what you buy on a long; short means selling base and buying quote. Direction follows the trade, not the quotation.

**All pairs move similarly.** EUR/USD and USD/JPY can move opposite directions same day because base/quote flips the USD side. A strong dollar means EUR/USD falls but USD/JPY rises.

**Cross pairs are exotic.** Crosses like EUR/GBP and AUD/NZD are highly liquid [[G10 Currencies|G10]] pairs. "Exotic" refers to [[EM Currencies|EM]] pairs, not the absence of USD.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- Levich, Richard M., *International Financial Markets*, 2nd ed.
- CME Group, "FX Products: Understanding FX Futures and Options."
