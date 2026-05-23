---
aliases: [round trip, round-trip cost, full spread cost]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Round Trip

## Definition
A round trip is a buy and a sell of the same instrument. The simplest cost is the [[Bid-Ask Spread]]: buy at the ask, sell at the bid, and the difference is what you paid for entering and exiting. For a market maker, a round trip where both sides fill at the quoted spread is ideal, capturing the full spread as profit. For a price taker, the round trip cost is the minimum trading friction, which the expected profit must overcome.

## Why it matters (commodities and FX)
Round trip cost is the hurdle rate for any short term strategy. If EUR/USD round trip is 0.4 pips, any signal predicting less than 0.4 pips is unprofitable. In commodities, round trip costs vary enormously: WTI on CME might cost 1 tick ($10/contract); lumber 5 to 10 ticks. [[Turnover]] amplifies it. A strategy that turns over 50x/day pays 50 round trips of spread. High [[Turnover]] strategies need extremely tight spreads or large per trade alpha to survive.

## Concrete example

**Concrete:** Copper futures on COMEX, $4.2500 bid / $4.2520 ask. Spread $0.0020/lb, contract 25,000 lb. Win: buy 10 contracts at $4.2520 expecting $0.0100 rise. Copper moves to $4.2600 / $4.2620. Sell 10 at $4.2600. Bought at ask ($0.0010 above original mid $4.2510), sold at new bid ($0.0010 below new mid $4.2610). Total spread cost = 2 x [[Half Spread]] = $0.0020. Net profit per pound = $0.0080 (spread already embedded). 10 contracts: $2,000. Failure: copper does not move. Bought $4.2520, now sell at $4.2500. Round trip loss = $0.0020/lb = pure spread cost. 10 contracts: $500 lost as baseline trading friction.

**Simplified:** A round trip is one buy plus one sell. You pay half a spread on each leg. Even if the market does not move, you lose one full spread just from entering and exiting. This is the minimum cost any strategy has to beat to make money.

## Key mechanics and formulas
- **Round trip cost (simple)** = Ask - Bid = [[Bid-Ask Spread]]
- **Round trip cost (from mid)** = 2 x [[Half Spread]]
- **Round trip cost in dollars** = Spread x Contract Size x Number of Contracts
- **Effective round trip cost** = 2 x |Avg Fill Price - Mid at fill|. Captures realized cost including [[Slippage]] and [[Market Impact]]
- **Break even move** = Round trip cost. Price must move at least the spread for profit
- **Annual spread cost** = RT/day x RT cost x 252. A strategy doing 100 RT/day in EUR/USD at 0.4 pips/RT = 40 pips/day = ~10,080 pips/year in friction

## Prerequisites
- [[Bid-Ask Spread]]
- [[Half Spread]]
- [[Mid Price]]

## Related concepts (learn next)
- [[Turnover]] , how often positions cycle, directly multiplying round trip costs
- [[Half Spread]] , the single side cost making up half the round trip
- [[Slippage]] , additional costs beyond displayed spread on each leg
- [[Market Impact]] , the cost of moving the market against yourself
- [[Effective Spread]] , realized cost per side, often exceeding quoted half spread
- [[Bid-Ask Spread]] , quoted cost at [[Top of Book]]
- [[Commission]] , exchange and broker fees adding to RT cost beyond spread

## Common misconceptions
1. **"Round trip cost is just the spread."** For small orders in liquid markets, yes. Large orders add [[Market Impact]] on entry and exit, [[Slippage]], and commissions, often doubling or tripling effective cost. A 200 lot Brent order does not fill at top of book on both legs.
2. **"I only pay the spread once."** You pay [[Half Spread]] on entry and half on exit. Together that is the full spread. Counting only entry understates friction by 50%.
3. **"RT cost does not matter for long term trades."** Single RT is less significant on a 6 month hold. But repeatedly adjusting hedges, rolling futures, and rebalancing accumulates RT costs that compound materially.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- CME Group, "Understanding Transaction Costs in Futures Markets"
- Kissell, R. *The Science of Algorithmic Trading and Portfolio Management*, Academic Press
