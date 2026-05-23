---
aliases: [spot rate, spot FX, spot exchange rate]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Spot Rate

## Definition
The spot rate is the current market price at which one currency exchanges for another for immediate delivery. "Immediate" means T+2 settlement for most pairs; USD/CAD settles T+1. The spot rate is the fundamental reference price in FX and the anchor from which all other FX instruments (forwards, options, swaps) are priced. Determined continuously by supply and demand in the interbank market, with major dealing banks providing liquidity round the clock from Sunday evening to Friday close. The spot rate on a screen is a mid: the average of best [[Bid-Ask Spread|bid]] and offer.

## Why it matters (commodities and FX)
Every FX trade starts with the spot rate. [[Carry Trade|Carry]], [[Forward Points|forwards]], and [[FX Swap|FX swaps]] price off it. Commodity traders converting foreign revenues to domestic face spot rate exposure daily. For systematic macro, spot is the primary input for momentum, mean reversion, and valuation signals. Where spot trades relative to [[Forward Points|forwards]] reveals the market's implied cost of holding a position.

## Concrete example

**Concrete:** A trader buys 10M EUR/USD at spot 1.0850 Monday morning. Settlement Wednesday (T+2): trader delivers 10,850,000 USD and receives 10,000,000 EUR. By Friday spot is 1.0920: position gained 70 [[Pip|pips]], ~70,000 USD on 10M EUR notional. If spot dropped to 1.0780 instead, loss is ~70,000 USD. March 2020: EUR/USD swung from 1.1500 to 1.0636 in 2 weeks, showing how fast spot moves in a liquidity crisis. Even the deepest pair gaps when funding stress hits.

**Simplified:** The "right now" price for swapping one currency for another. T+2 settlement, not literally instant. The number you see on a screen is an average of bank quotes. Every other FX instrument prices off this one.

## Key mechanics and formulas
- **Spot quotation:** Base / Quote. EUR/USD = 1.0850 means 1 EUR = 1.0850 USD.
- **PnL in quote currency:** (Exit rate minus Entry rate) × Position size in base.
  - Example: (1.0920 minus 1.0850) × 10,000,000 EUR = 70,000 USD.
- **Inverse rate:** USD/EUR = 1 / (EUR/USD). EUR/USD = 1.0850 → USD/EUR = 0.9217.
- **Settlement:** T+2 for most [[Currency Pair|pairs]], T+1 for USD/CAD, T+0 possible at a premium.

## Prerequisites
- [[Currency Pair]]
- [[Pip]]
- [[Big Figure]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Forward Points]]: adjustment added to spot for the forward rate, reflecting [[Interest Rate Differential|rate differentials]]
- [[FX Swap]]: combines spot + simultaneous forward; the most traded FX instrument by volume
- [[Cross Pairs]]: non USD pairs derived from 2 USD spot rates
- [[Dollar Index]]: weighted basket measuring USD strength against 6 currencies
- [[Covered Interest Parity]]: arbitrage relation linking spot, forward, rates
- [[NDF]]: cash settled spot equivalent for restricted [[EM Currencies|EM]]

## Common misconceptions
1. **Spot means instant.** Settlement is T+2, not real time. Same day settlement exists ("value today") at a premium but is rare.
2. **The spot rate is a single number.** Every bank quotes its own bid and offer. The screen "spot" is a mid compiled from multiple LPs.
3. **Spot is only for speculation.** Most volume is corporate hedging, central bank operations, and portfolio rebalancing, not directional bets.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey," 2022.
- Chaboud, A. et al., "Rise of the Machines: Algorithmic Trading in the Foreign Exchange Market," Journal of Finance, 2014.
- Hull, John C., *Options, Futures, and Other Derivatives*, 11th ed.
