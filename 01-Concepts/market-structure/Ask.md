---
aliases: [ask price, offer, offer price, sell price, ask side]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Ask

## Definition

The ask (or offer) is the price at which a seller will sell. In a [[Two Way Price]] the ask is the higher number. On a quote of "1.08497 / 1.08503" for [[EUR USD]], 1.08503 is the ask. To buy immediately you buy at the ask. The ask represents supply: the best price someone is currently willing to accept for selling.

## Why it matters (commodities and FX)

Buying at the ask costs more than the [[Mid Price]], and that gap compounds. An FX desk doing $500 million per day in [[EUR USD]] with a 0.3 [[Pip]] half spread pays roughly $15,000 daily in ask side costs alone. In commodities, the ask on illiquid contracts (far dated [[LNG]] forwards) can be wide, making entry expensive. Reading ask depth tells you how much size you can buy before price runs away.

## Concrete example

**Concrete:** Trader buys 20 lots of [[Copper Futures]] on the [[LME]]. Book:

| Level | Bid | Size | Ask | Size |
|-------|-----|------|-----|------|
| 1 | $9,245 | 5 | $9,248 | 8 |
| 2 | $9,243 | 10 | $9,250 | 12 |
| 3 | $9,240 | 15 | $9,253 | 10 |

A [[Limit Order]] at $9,249 fills 8 at $9,248 and 12 at $9,249, average $9,248.60. A [[Market Order]] sweeps: 8 at $9,248, 12 at $9,250, average $9,249.20, paying $0.60 per lot more by sweeping [[Depth of Book|depth]].

**Simplified:** The ask is what sellers want for the asset. Buy immediately and you pay the ask. If you want a better price, post a limit and wait for sellers to come to you. If you grab everything in front of you at once, you eat through the book and pay progressively worse prices for each chunk.

## Key mechanics and formulas

Ask = lowest price any seller will accept

[[Bid-Ask Spread]] = Ask minus [[Bid]]

[[Mid Price]] = ([[Bid]] + Ask) / 2

**Ask depth** = total volume at the ask and above in the [[Central Limit Order Book|order book]]

FX convention:
- Market maker's ask = price the maker sells base currency
- Client buying at the ask pays the higher price

## Prerequisites

- [[Two Way Price]]
- [[Central Limit Order Book]]

## Related concepts (learn next)

- [[Bid]] for the other side of the two way price
- [[Bid-Ask Spread]] for the transaction cost between bid and ask
- [[Mid Price]] for the reference price between bid and ask
- [[Top of Book]] for the best available bid and ask
- [[Depth of Book]] for how much volume sits behind the best ask
- [[Limit Order]] for specifying the maximum price you will pay
- [[Slippage]] for what happens when the ask moves before your order fills

## Common misconceptions

**"The ask is the fair price to buy at."** The ask embeds the seller's markup. [[Mid Price]] is closer to fair value. Buying at the ask costs half the [[Bid-Ask Spread|spread]].

**"Offer and ask are different."** Identical. "Offer" is voice and European usage. "Ask" is electronic and US usage.

**"The ask only rises in a rising market."** In a liquidity vacuum, the ask gaps up even in a falling market when sellers withdraw. The ask reflects supply, not direction.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- CME Group, "Understanding the Order Book"
- Cartea, A., Jaimungal, S., and Penalva, J., "Algorithmic and High Frequency Trading," Cambridge University Press
