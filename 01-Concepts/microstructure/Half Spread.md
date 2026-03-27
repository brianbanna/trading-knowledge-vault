---
aliases: [half spread, half-spread, single-side cost]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Half Spread

## Definition
The half spread is half the [[Bid-Ask Spread]]. It represents the cost of a single trade measured from the [[Mid Price]]. If the bid is 1.1000 and the ask is 1.1002, the spread is 2 pips and the half spread is 1 pip. When I buy at the ask, I pay mid plus the half spread. When I sell at the bid, I receive mid minus the half spread. The half spread is the market maker's gross revenue per side before accounting for [[Adverse Selection]] costs. It is also the minimum cost a price taker pays for immediacy on a single transaction.

## Why it matters (commodities and FX)
The half spread is the fundamental unit of transaction cost analysis (TCA) in FX and commodities. When evaluating an execution algorithm or a broker, the question is: "How much did I pay relative to mid?" That answer is the half spread or better. In EUR/USD, the half spread at [[Top of Book]] is typically 0.1 to 0.5 pips in normal conditions. In less liquid commodities like lean hogs or cocoa, the half spread can be several ticks. A market maker's profitability equals the half spread earned minus [[Adverse Selection]] cost minus hedging cost. If a maker quotes a 2 pip spread in GBP/USD (1 pip half spread) but the average [[Markout]] is negative 1.2 pips, the maker is losing 0.2 pips per trade despite earning the half spread.

## Concrete example
Gold futures on COMEX are quoted at $2,340.00 bid / $2,340.40 offer. The spread is $0.40. The half spread is $0.20 per troy ounce.

**Win scenario (market maker):** I sell 10 contracts (100 oz each) at $2,340.40 and the mid does not move. My edge is the half spread: $0.20 per ounce. Profit: 10 x 100 x $0.20 = $200. If I then buy 10 contracts at $2,340.00 on the bid, I complete a [[Round Trip]] and earn the full spread: $0.40 x 10 x 100 = $400.

**Fail scenario (price taker):** I need to buy 50 contracts of gold urgently. I lift the offer at $2,340.40, paying the half spread of $0.20 above mid. But my order is large enough to sweep through [[Depth of Book|additional levels]]: 10 contracts fill at $2,340.40, 15 at $2,340.60, 15 at $2,340.80, and 10 at $2,341.00. My average fill is $2,340.68, which is $0.48 above the original mid. My effective half spread is $0.48, more than double the displayed half spread, because [[Market Impact]] consumed additional levels.

## Key mechanics and formulas
- **Half spread** = (Ask minus Bid) / 2 = Spread / 2
- **Half spread in basis points** = Half spread / Mid x 10000
- **Execution cost from mid** = |Fill Price minus Mid| (should approximate the half spread for small market orders)
- **Market maker gross P&L per side** = Half Spread minus Adverse Selection cost
- **Market maker net P&L per round trip** = Spread minus 2 x Adverse Selection cost
- For a price taker, total single side cost = Half Spread + [[Slippage]] + [[Market Impact]] (the latter 2 are 0 for small orders in liquid markets)

## Prerequisites
- [[Bid-Ask Spread]]
- [[Mid Price]]
- [[Top of Book]]

## Related concepts (learn next)
- [[Round Trip]] , two half spreads, the full cost of buying and selling
- [[Markout]] , compares post trade price movement to the half spread to determine net profitability
- [[Slippage]] , execution cost beyond the displayed half spread, caused by timing or size
- [[Market Impact]] , the additional cost when order size exceeds [[Top of Book]] and sweeps deeper levels
- [[Adverse Selection]] , the risk that offsets the half spread revenue for market makers
- [[Bid-Ask Spread]] , the parent concept from which half spread is derived
- [[Effective Spread]] , 2 x |Fill Price minus Mid|, which captures the realized (not quoted) half spread

## Common misconceptions
1. **"The half spread is my total cost."** The half spread is only the immediate, visible cost. For larger orders, [[Market Impact]], [[Slippage]], and information leakage add to the total cost. A 0.5 pip half spread in EUR/USD can become a 2 pip total cost on a 200 million order.
2. **"A smaller half spread is always better."** A tight half spread with high rejection rates (via [[Last Look]]) can be worse than a wider half spread with guaranteed fills. The effective cost depends on fill probability, not just the displayed price.
3. **"Half spread is constant."** Half spreads widen dramatically during news events, illiquid hours (FX during the Asia to London gap), and market stress. Copper half spreads that are $0.50 during London hours might be $2.00 during Asian hours when LME is closed.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- CME Group, "Understanding Transaction Costs in Futures Markets"
