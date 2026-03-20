---
aliases: [pip, pips, percentage in point]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Pip

## Definition
A pip (percentage in point) is the smallest standard unit of price movement in a [[Currency Pair|currency pair]]. For most pairs, 1 pip equals 0.0001 (the 4th decimal place). For JPY pairs, where the exchange rate is quoted to 2 decimal places, 1 pip equals 0.01. Modern electronic trading platforms often display an additional digit beyond the pip (called a "pipette" or fractional pip), so EUR/USD might show 1.08503, where the final "3" is 0.3 of a pip. Pips provide a standardized way to measure price changes across different currency pairs, enabling traders to compare moves and calculate profit and loss consistently regardless of the pair traded.

## Why it matters (commodities and FX)
Pips are the universal language for quoting FX price changes, spreads, and P&L. When a commodity trader hedges USD/CAD exposure and the broker quotes a 1.5 pip spread, understanding pip value is essential for calculating transaction costs. Risk management in FX is denominated in pips: a stop loss might be 50 pips away, a daily range might average 80 pips, and a carry position might earn 0.3 pips per day in [[Forward Points|swap points]]. Without fluency in pips, you cannot size positions, compare opportunities, or communicate with counterparties.

## Concrete example
A trader buys 1 million EUR/USD at 1.0850. Each pip on a 1 million EUR position is worth 100 USD (0.0001 × 1,000,000). If EUR/USD rises 45 pips to 1.0895, the profit is 45 × 100 = 4,500 USD. Now consider USD/JPY: a trader sells 1 million USD/JPY at 150.00. Each pip is worth approximately 6,667 JPY (0.01 × 1,000,000), or about 44.44 USD at the current rate. If USD/JPY falls 60 pips to 149.40, the profit is 60 × 6,667 = 400,020 JPY, roughly 2,676 USD. Failure: setting a 20 pip stop on GBP/USD during a Bank of England decision, when the pair regularly moves 80+ pips around announcements, almost guarantees being stopped out.

## Key mechanics and formulas
- **Standard pip**: 0.0001 for most pairs; 0.01 for JPY pairs.
- **Pipette**: 0.00001 (1/10th of a pip). The 5th decimal place on most platforms.
- **Pip value (quote currency)**: Pip size × Position size in base currency.
  - EUR/USD, 1 million EUR: 0.0001 × 1,000,000 = 100 USD per pip.
- **Pip value (account currency, when different from quote)**: (Pip size × Position size) / Current exchange rate of quote currency vs account currency.
  - USD/CHF, 1 million USD, account in USD: (0.0001 × 1,000,000 CHF value) / USD/CHF rate.
- **JPY pip value**: 0.01 × Position size. For 1 million USD/JPY: 0.01 × 1,000,000 = 10,000 JPY per pip.
- **Spread cost in USD**: Spread in pips × Pip value × Number of round trips.

## Prerequisites
- [[Currency Pair]]
- [[Spot Rate]]

## Related concepts (learn next)
- [[Big Figure]]: the integer or large round number portion of an exchange rate, representing 100 pips.
- [[Bid-Ask Spread]]: quoted in pips, representing the transaction cost of a round trip trade.
- [[Forward Points]]: expressed in pips, showing the premium or discount of the forward rate to spot.
- [[Major Pairs]]: offer the tightest pip spreads, sometimes as low as 0.1 pips for EUR/USD.
- [[Spot Rate]]: the base price from which pip movements are measured.
- [[Position Sizing]]: pip value is the critical input for determining how many units to trade given a risk budget.

## Common misconceptions
1. **A pip is always the same dollar value**: Pip value depends on the pair, the position size, and the current exchange rate. 1 pip on EUR/USD (1 million) = 100 USD, but 1 pip on USD/JPY (1 million) ≈ 44 to 67 USD depending on the spot rate.
2. **Pipettes do not matter**: At institutional scale, 0.1 pip on a 100 million position is 10,000 USD. Fractional pips are critical for execution quality measurement and best execution compliance.
3. **All moves are measured in pips**: Some markets (notably EM FX and cryptocurrency) use percentage moves or basis points instead, because pip counts become meaningless when the exchange rate itself is in the thousands (e.g., USD/KRW at 1,350).

## Sources
- Lien, Kathy, *Day Trading and Swing Trading the Currency Market*, 3rd ed.
- CME Group, "Understanding FX Futures: Tick Size and Pip Value."
- Investopedia, "What Is a Pip in Forex Trading?"
