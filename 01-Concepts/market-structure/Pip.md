---
aliases: [pip, pips, percentage in point]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Pip

## Definition
A pip (percentage in point) is the smallest standard unit of price movement in a [[Currency Pair|currency pair]]. For most pairs, 1 pip = 0.0001 (the 4th decimal). For JPY pairs, quoted to 2 decimals, 1 pip = 0.01. Modern platforms display an additional digit (a "pipette" or fractional pip), so EUR/USD shows 1.08503 where the final "3" is 0.3 of a pip. Pips standardize price changes across pairs, letting traders compare moves and calculate PnL consistently.

## Why it matters (commodities and FX)
Pips are the universal language for FX price changes, spreads, and PnL. When a commodity trader hedges USD/CAD and the broker quotes a 1.5 pip spread, pip value determines real transaction cost. Risk management in FX runs in pips: 50 pip stop, 80 pip average daily range, 0.3 pip per day in [[Forward Points|swap points]] on a carry. Without fluency in pips you cannot size positions, compare opportunities, or talk to counterparties.

## Concrete example

**Concrete:** A trader buys 1M EUR/USD at 1.0850. Each pip on 1M EUR = 100 USD (0.0001 × 1,000,000). EUR/USD rises 45 pips to 1.0895: profit = 45 × 100 = 4,500 USD. Now USD/JPY: sell 1M USD/JPY at 150.00. Each pip is ~6,667 JPY (0.01 × 1,000,000), ~44.44 USD at the rate. USD/JPY falls 60 pips to 149.40: profit = 60 × 6,667 = 400,020 JPY, ~2,676 USD. Adverse case: setting a 20 pip stop on GBP/USD around a BoE decision, when the pair regularly swings 80+ pips around announcements, almost guarantees being stopped out before the directional view plays out.

**Simplified:** A pip is the standard "unit" of FX price moves. For most pairs it is the 4th decimal (0.0001). For JPY pairs it is the 2nd (0.01). Dollar value depends on pair and position size. Trader shorthand: "I made 30 pips" = the price moved 30 of those units in their favor.

## Key mechanics and formulas
- **Standard pip:** 0.0001 for most pairs; 0.01 for JPY pairs.
- **Pipette:** 0.00001 (1/10th of a pip). The 5th decimal on most platforms.
- **Pip value (quote currency):** Pip size × Position size in base currency.
  - EUR/USD, 1M EUR: 0.0001 × 1,000,000 = 100 USD per pip.
- **Pip value (account currency, when different from quote):** (Pip size × Position size) / Current rate of quote vs account ccy.
  - USD/CHF, 1M USD, account in USD: (0.0001 × 1,000,000 CHF) / USD/CHF rate.
- **JPY pip value:** 0.01 × Position size. For 1M USD/JPY: 10,000 JPY per pip.
- **Spread cost in USD:** Spread in pips × Pip value × Number of round trips.

## Prerequisites
- [[Currency Pair]]
- [[Spot Rate]]

## Related concepts (learn next)
- [[Big Figure]]: the integer or large round portion of a rate, representing 100 pips
- [[Bid-Ask Spread]]: quoted in pips, transaction cost of a round trip
- [[Forward Points]]: expressed in pips, premium/discount of forward to spot
- [[Major Pairs]]: tightest pip spreads, as low as 0.1 pips for EUR/USD
- [[Spot Rate]]: base price from which pip movements are measured
- [[Position Sizing]]: pip value is the critical input given a risk budget

## Common misconceptions
1. **A pip is always the same dollar value.** Pip value depends on pair, position size, and current rate. 1 pip on EUR/USD (1M) = 100 USD, but 1 pip on USD/JPY (1M) ranges 44 to 67 USD by spot.
2. **Pipettes do not matter.** At institutional scale, 0.1 pip on 100M is 10,000 USD. Fractional pips are critical for execution quality measurement and best execution compliance.
3. **All moves are measured in pips.** EM FX and crypto use percentage or basis points instead. Pip counts become meaningless when the rate itself is in the thousands (USD/KRW at 1,350).

## Sources
- Lien, Kathy, *Day Trading and Swing Trading the Currency Market*, 3rd ed.
- CME Group, "Understanding FX Futures: Tick Size and Pip Value."
- Investopedia, "What Is a Pip in Forex Trading?"
