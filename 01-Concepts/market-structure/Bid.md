---
aliases: [bid price, buy price, bid side]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Bid

## Definition

The bid is the price at which a buyer will purchase. In a [[Two Way Price]] the bid is the lower number. On a quote of "1.08497 / 1.08503" for [[EUR USD]], 1.08497 is the bid. To sell immediately you sell at the bid. The bid represents demand: the best price someone is currently offering to pay.

## Why it matters (commodities and FX)

Every execution starts with knowing which side you hit. Selling at the bid means accepting the buyer's price, always worse than the [[Mid Price]]. In fast markets (crude after an [[EIA Weekly Petroleum Status Report]] release), the bid drops instantly as buyers pull orders, leaving sellers with far worse prices than expected. Reading bid [[Depth of Book|depth]] tells you how much size can be sold before price deteriorates.

## Concrete example

**Concrete:** Dealer quotes [[Brent Crude]] futures at $82.50 / $82.55. Client hits the bid at $82.50 for 10 lots. Dealer is now [[Long]] 10 lots at $82.50, earning the spread if they can resell near the ask. Scenario 2: EIA shows a surprise build. Bids collapse. Top of book drops from $82.50 to $81.90 in 2 seconds as buyers cancel. A client selling 50 lots sweeps 3 price levels, average fill $81.75, with $0.75 of [[Slippage]] from the pre data bid.

**Simplified:** The bid is what buyers are willing to pay. Sell immediately and you get the bid. If you want a better price, post a limit above the bid and wait for someone to lift it. When bad news hits, buyers vanish and the bid drops fast, so sellers who waited get filled at much worse levels than the screen showed seconds earlier.

## Key mechanics and formulas

Bid = highest price any buyer will pay

[[Bid-Ask Spread]] = [[Ask]] minus Bid

[[Mid Price]] = (Bid + Ask) / 2

**Bid depth** = total volume at the bid and below in the [[Central Limit Order Book|order book]]

FX convention:
- Market maker's bid = price the maker buys base currency
- Client selling at the bid receives the lower price

## Prerequisites

- [[Two Way Price]]
- [[Central Limit Order Book]]

## Related concepts (learn next)

- [[Ask]] for the other side of the two way price
- [[Bid-Ask Spread]] for the gap that represents transaction cost
- [[Mid Price]] for the theoretical reference price
- [[Top of Book]] for the best available bid and ask
- [[Depth of Book]] for volume behind the best bid
- [[Liquidity]] for how bid depth relates to execution ease
- [[Market Order]] for what happens when you hit the bid immediately

## Common misconceptions

**"The bid is the fair price to sell at."** The bid is the best price a buyer offers, not fair value. [[Mid Price]] is closer. Selling at the bid costs half the [[Bid-Ask Spread|spread]].

**"The bid is stable."** In volatile conditions bids vanish in milliseconds as makers widen or pull quotes. Never assume the bid you see will be there when your order arrives.

**"A high bid means strong demand."** A high bid at thin size is less meaningful than a lower bid with deep volume. Check [[Depth of Book|depth]], not just price.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- CME Group, "Understanding the Order Book"
- Cartea, A., Jaimungal, S., and Penalva, J., "Algorithmic and High Frequency Trading," Cambridge University Press
