---
aliases: [spot rate, spot FX, spot exchange rate]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Spot Rate

## Definition
The spot rate is the current market price at which one currency can be exchanged for another for immediate delivery. In practice, "immediate" means settlement in 2 business days (T+2) for most currency pairs, though USD/CAD settles T+1. The spot rate is the most fundamental reference price in foreign exchange markets and serves as the anchor from which all other FX instruments (forwards, options, swaps) are priced. It is determined continuously by supply and demand in the interbank market, with major dealing banks providing liquidity around the clock from Sunday evening to Friday close. The spot rate you see on a screen is typically a mid rate, meaning the average of the best available [[Bid-Ask Spread|bid]] and offer in the market.

## Why it matters (commodities and FX)
Every FX trade begins with the spot rate. If you trade [[Carry Trade|carry]], [[Forward Points|forwards]], or [[FX Swap|FX swaps]], the spot rate is your baseline. Commodity traders converting revenues from foreign sales back to domestic currency face spot rate exposure daily. For systematic macro strategies, the spot rate is the primary input for momentum, mean reversion, and valuation signals. Understanding where spot trades relative to [[Forward Points|forward points]] tells you the market's implied cost of holding a position.

## Concrete example
A trader buys 10 million EUR/USD at a spot rate of 1.0850 on Monday morning. Settlement occurs on Wednesday (T+2): the trader delivers 10,850,000 USD and receives 10,000,000 EUR. If by Friday the spot rate has moved to 1.0920, the position has gained 70 [[Pip|pips]], worth approximately 70,000 USD on 10 million EUR notional. Conversely, if spot drops to 1.0780, the loss is 70 pips or roughly 70,000 USD. In March 2020, EUR/USD spot swung from 1.1500 to 1.0636 in 2 weeks, illustrating how quickly spot can move during a liquidity crisis.

## Key mechanics and formulas
- **Spot quotation**: Base currency / Quote currency. EUR/USD = 1.0850 means 1 EUR costs 1.0850 USD.
- **P&L in quote currency**: (Exit rate − Entry rate) × Position size in base currency.
  - Example: (1.0920 − 1.0850) × 10,000,000 EUR = 70,000 USD.
- **Inverse rate**: USD/EUR = 1 / (EUR/USD). If EUR/USD = 1.0850, then USD/EUR = 0.9217.
- **Settlement**: T+2 for most [[Currency Pair|currency pairs]], T+1 for USD/CAD, T+0 possible for same day value at a premium.

## Prerequisites
- [[Currency Pair]]
- [[Pip]]
- [[Big Figure]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Forward Points]]: the adjustment added to spot to derive the forward rate, reflecting [[Interest Rate Differential|interest rate differentials]].
- [[FX Swap]]: combines a spot transaction with a simultaneous forward, the most traded FX instrument by volume.
- [[Cross Pairs]]: spot rates for non USD pairs derived from 2 USD spot rates.
- [[Dollar Index]]: a weighted basket measuring USD spot strength against 6 currencies.
- [[Covered Interest Parity]]: the arbitrage relationship linking spot, forward, and interest rates.
- [[NDF]]: cash settled spot equivalent for restricted [[EM Currencies|EM currencies]].

## Common misconceptions
1. **Spot means instant**: Settlement is T+2, not real time. Actual same day settlement ("value today") exists but costs extra and is rarely used outside of urgent flows.
2. **The spot rate is a single number**: There is no single spot rate. Every bank quotes its own bid and offer, and the "spot rate" on your screen is a mid compiled from multiple liquidity providers.
3. **Spot is only for speculation**: The majority of spot volume comes from corporate hedging, central bank operations, and portfolio rebalancing, not directional bets.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- Chaboud, A. et al., "Rise of the Machines: Algorithmic Trading in the Foreign Exchange Market," Journal of Finance, 2014.
- Hull, John C., *Options, Futures, and Other Derivatives*, 11th ed.
