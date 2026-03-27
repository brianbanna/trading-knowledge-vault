---
aliases: [ask price, offer, offer price, sell price, ask side]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Ask

## Definition

The ask (also called the offer) is the price at which a seller is willing to sell an asset. In a [[Two Way Price]], the ask is always the higher number. When a market maker shows "1.08497 / 1.08503" on [[EUR USD]], 1.08503 is the ask. If you want to buy immediately, you buy at the ask. The ask represents supply: the best price someone in the market is currently willing to accept for selling.

## Why it matters (commodities and FX)

Buying at the ask means paying more than the [[Mid Price]], and that cost compounds over many trades. An FX desk executing $500 million notional per day in [[EUR USD]] with a 0.3 [[Pip]] half spread pays approximately $15,000 per day just in ask side costs. In commodities, the ask on illiquid contracts (e.g., far dated [[LNG]] forwards) can be wide, making entry expensive. Understanding ask depth helps traders estimate how much they can buy before the price runs away.

## Concrete example

A trader wants to buy 20 lots of [[Copper Futures]] on the [[LME]]. The screen shows:

| Level | Bid | Size | Ask | Size |
|-------|-----|------|-----|------|
| 1 | $9,245 | 5 | $9,248 | 8 |
| 2 | $9,243 | 10 | $9,250 | 12 |
| 3 | $9,240 | 15 | $9,253 | 10 |

**Success case:** The trader sends a [[Limit Order]] at $9,249. A seller adjusts their ask down, and the trader gets filled at $9,248 on 8 lots, then $9,249 on the remaining 12 lots. Average price: $9,248.60.

**Failure case:** The trader sends a [[Market Order]] for all 20 lots. They lift the ask at $9,248 for 8 lots, $9,250 for 12 lots. Average price: $9,249.20, paying $0.60 more per lot than the best ask due to sweeping through [[Depth of Book|depth]].

## Key mechanics and formulas

Ask = lowest price any seller is willing to accept

[[Bid-Ask Spread]] = Ask minus [[Bid]]

[[Mid Price]] = ([[Bid]] + Ask) / 2

**Ask depth** = total volume available at the ask price and above in the [[Central Limit Order Book|order book]]

In FX quoting convention:
- The market maker's ask = the price at which the maker sells the base currency
- The client's perspective: buying at the ask means paying the higher price

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

1. **"The ask is the fair price to buy at."** The ask includes the seller's markup. The [[Mid Price]] is a better approximation of fair value. Buying at the ask means paying half the [[Bid-Ask Spread|spread]].

2. **"Offer and ask are different things."** They are identical. "Offer" is more common in voice markets and European usage. "Ask" is more common in electronic markets and US usage.

3. **"The ask only moves up in a rising market."** In a liquidity vacuum, the ask can gap up even in a falling market if sellers withdraw. The ask reflects available supply, not market direction.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- CME Group, "Understanding the Order Book"
- Cartea, A., Jaimungal, S., and Penalva, J., "Algorithmic and High Frequency Trading," Cambridge University Press
