---
aliases: [bid price, buy price, bid side]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Bid

## Definition

The bid is the price at which a buyer is willing to purchase an asset. In a [[Two Way Price]], the bid is always the lower number. When a market maker shows "1.08497 / 1.08503" on [[EUR USD]], 1.08497 is the bid. If you want to sell immediately, you sell at the bid. The bid represents demand: the best price someone in the market is currently offering to pay.

## Why it matters (commodities and FX)

Every trade execution starts with understanding which side of the market you are hitting. Selling at the bid means accepting the buyer's price, which is always less favorable than the [[Mid Price]]. In fast moving commodity markets (e.g., crude after an [[EIA Weekly Petroleum Status Report]] release), the bid can drop instantly as buyers pull their orders, leaving sellers with far worse prices than expected. Monitoring bid [[Depth of Book|depth]] tells a trader how much can be sold before the price deteriorates further.

## Concrete example

A dealer quotes [[Brent Crude]] futures at $82.50 / $82.55 (bid / [[Ask]]).

**Scenario 1 (normal):** A client wants to sell 10 lots. The client hits the bid at $82.50. The dealer is now [[Long]] 10 lots at $82.50 and has earned potential spread revenue if they can sell at or near the ask.

**Scenario 2 (thin bid):** EIA data shows a surprise inventory build. Bids collapse. The [[Top of Book]] bid drops from $82.50 to $81.90 in 2 seconds as buyers cancel orders. A client trying to sell 50 lots sweeps through 3 price levels, getting an average fill of $81.75, experiencing $0.75 of [[Slippage]] from the pre data bid.

## Key mechanics and formulas

Bid = highest price any buyer is willing to pay

[[Bid-Ask Spread]] = [[Ask]] minus Bid

[[Mid Price]] = (Bid + Ask) / 2

**Bid depth** = total volume available at the bid price and below in the [[Central Limit Order Book|order book]]

In FX quoting convention:
- The market maker's bid = the price at which the maker buys the base currency
- The client's perspective: selling at the bid means receiving the lower price

## Prerequisites

- [[Two Way Price]]
- [[Central Limit Order Book]]

## Related concepts (learn next)

- [[Ask]] for the other side of the two way price
- [[Bid-Ask Spread]] for the gap between bid and ask that represents transaction cost
- [[Mid Price]] for the theoretical reference price between bid and ask
- [[Top of Book]] for the best available bid and ask
- [[Depth of Book]] for how much volume sits behind the best bid
- [[Liquidity]] for how bid depth relates to ease of execution
- [[Market Order]] for what happens when you hit the bid immediately

## Common misconceptions

1. **"The bid is the fair price to sell at."** The bid is the best price a buyer offers, not the fair value. The [[Mid Price]] is closer to fair value. Selling at the bid means paying half the [[Bid-Ask Spread|spread]] as a cost.

2. **"The bid is stable."** In volatile conditions, bids can vanish in milliseconds as market makers widen or pull quotes. Never assume the bid you see will still be there when your order arrives.

3. **"A high bid means strong demand."** A high bid at thin size is less meaningful than a lower bid with deep volume. Always check [[Depth of Book|depth]], not just the price.

## Sources

- Harris, Larry, "Trading and Exchanges," Oxford University Press
- CME Group, "Understanding the Order Book"
- Cartea, A., Jaimungal, S., and Penalva, J., "Algorithmic and High Frequency Trading," Cambridge University Press
