---
aliases: [round trip, round-trip cost, full spread cost]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Round Trip

## Definition
A round trip is a buy and a sell of the same instrument. The full cost of a round trip, in the simplest case, is the [[Bid-Ask Spread]]: I buy at the ask and sell at the bid, and the difference is what I paid for the privilege of entering and exiting the position. A round trip is the complete cycle of a trade. For a market maker, a round trip where both sides fill at the quoted spread is the ideal outcome, capturing the full spread as profit. For a price taker, the round trip cost is the minimum friction of trading, and it must be overcome by the expected profit of the position.

## Why it matters (commodities and FX)
Round trip cost is the hurdle rate for any short term trading strategy. If the round trip in EUR/USD is 0.4 pips, any signal that predicts less than 0.4 pips of movement is unprofitable. In commodities, round trip costs vary enormously: WTI crude on CME might cost 1 tick ($10 per contract), while a less liquid commodity like lumber might cost 5 to 10 ticks. [[Turnover]] amplifies round trip costs. A strategy that turns over inventory 50 times per day pays 50 round trips worth of spread. High [[Turnover]] strategies need extremely tight spreads or large per trade alpha to survive.

## Concrete example
I trade copper futures on COMEX. The market is $4.2500 bid / $4.2520 offer. The spread is $0.0020 per pound. Each contract is 25,000 pounds.

**Win scenario:** I buy 10 contracts at $4.2520 (the offer) because my model predicts a $0.0100 rise. Copper moves to $4.2600 / $4.2620. I sell 10 contracts at $4.2600 (the bid). My round trip: bought at $4.2520, sold at $4.2600. Profit per pound: $0.0080. But I paid the spread twice (once on entry, once on exit), so the total spread cost is $0.0020 x 2 = $0.0040. Wait, that is wrong. The correct accounting: I bought at the ask ($4.2520, which is $0.0010 above the original mid of $4.2510). I sold at the new bid ($4.2600, which is $0.0010 below the new mid of $4.2610). Total spread cost = 2 x [[Half Spread]] = 2 x $0.0010 = $0.0020. Net profit = ($4.2600 minus $4.2520) minus 0 = $0.0080 per pound (the spread cost is already embedded). On 10 contracts: 10 x 25,000 x $0.0080 = $2,000.

**Fail scenario:** Same setup. Copper does not move. I bought at $4.2520 and now sell at $4.2500. Round trip loss = $0.0020 per pound = spread cost. On 10 contracts: 10 x 25,000 x $0.0020 = $500 lost purely to the round trip cost. This is the baseline friction of trading.

## Key mechanics and formulas
- **Round trip cost (simple)** = Ask minus Bid = [[Bid-Ask Spread]]
- **Round trip cost (from mid)** = 2 x [[Half Spread]]
- **Round trip cost in dollars** = Spread x Contract Size x Number of Contracts
- **Effective round trip cost** = 2 x |Average Fill Price minus Mid at time of fill|. This captures the realized cost, including [[Slippage]] and [[Market Impact]]
- **Break even move** = Round trip cost. The price must move by at least the spread for a position to be profitable
- **Annual spread cost** = Round trips per day x Round trip cost per trade x 252 trading days. A strategy doing 100 round trips per day in EUR/USD at 0.4 pips per RT = 40 pips/day = approximately 10,080 pips/year in friction

## Prerequisites
- [[Bid-Ask Spread]]
- [[Half Spread]]
- [[Mid Price]]

## Related concepts (learn next)
- [[Turnover]] , how frequently positions are opened and closed, directly multiplying round trip costs
- [[Half Spread]] , the single side cost that makes up half the round trip
- [[Slippage]] , additional costs beyond the displayed spread on each leg of the round trip
- [[Market Impact]] , the cost of moving the market against yourself during entry or exit
- [[Effective Spread]] , the realized cost per side, often exceeding the quoted half spread
- [[Bid-Ask Spread]] , the quoted cost of a round trip at [[Top of Book]]
- [[Commission]] , exchange and broker fees that add to the round trip cost beyond the spread

## Common misconceptions
1. **"Round trip cost is just the spread."** For small orders in liquid markets, yes. For large orders, [[Market Impact]] on entry and exit, [[Slippage]], and commissions can double or triple the effective round trip cost. A 200 lot Brent order does not get filled at top of book on both legs.
2. **"I only pay the spread once."** You pay the [[Half Spread]] on entry and the half spread on exit. That is the full spread. Some traders mistakenly count only the entry cost and forget the exit side, understating their friction by 50%.
3. **"Round trip cost does not matter for long term trades."** True that a single round trip is less significant for a position held 6 months. But even for long term traders, repeatedly adjusting hedges, rolling futures, and rebalancing accumulates round trip costs that compound materially over time.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- CME Group, "Understanding Transaction Costs in Futures Markets"
- Kissell, R. *The Science of Algorithmic Trading and Portfolio Management*, Academic Press
