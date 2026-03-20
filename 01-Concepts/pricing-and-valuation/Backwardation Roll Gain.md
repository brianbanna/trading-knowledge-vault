---
aliases: [backwardation roll gain, positive roll yield, roll return]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Backwardation Roll Gain

## Definition
Backwardation roll gain is the profit earned when rolling a long [[Futures Contract]] position forward in a backwardated market, where the front month price is higher than the deferred month price. The trader sells the expiring front month contract (at a higher price) and buys the next month contract (at a lower price), pocketing the difference as a gain. This positive [[roll yield]] is one of the most persistent and well documented sources of return in commodity markets. Research by Gorton and Rouwenhorst demonstrated that roll yield accounts for a substantial portion of long term commodity futures returns, often exceeding the contribution from spot price appreciation alone. Backwardation reflects market conditions where current supply is scarce and the convenience yield (the benefit of holding the physical commodity now) exceeds the cost of carry. It tends to prevail when inventories are low, as measured by metrics like the [[Stocks to Use Ratio]], and when there is urgency for immediate supply.

## Why it matters (commodities and FX)
Systematic carry strategies in commodities are built on capturing backwardation roll gains across a diversified portfolio of markets. The economic logic is that backwardated commodities tend to stay backwardated because the supply tightness that creates backwardation persists until new supply enters the market. CTAs, risk parity funds, and commodity index strategies all incorporate roll yield as a primary factor in portfolio construction. For individual traders, preferring long positions in backwardated markets and avoiding (or shorting) contango markets improves risk adjusted returns over multi year horizons. Backwardation roll gain is the commodity market's analogue to the carry earned in FX from holding high yielding currencies. Crude oil, certain base metals, and agricultural commodities with low [[Stocks to Use Ratio]] are the markets that most frequently exhibit backwardation.

## Concrete example
**Success case:** Brent crude front month (June) is at $84.00/bbl and the second month (July) is at $82.50/bbl, a $1.50 backwardation. A trader rolls their long position from June to July by selling June at $84.00 and buying July at $82.50, capturing a $1.50/bbl gain per contract ($1,500 on 1,000 barrels). Over 12 months, if average monthly backwardation is $0.80, the annualized roll gain is approximately $9.60/bbl, or 11.4% on an $84 base. This return is earned on top of any spot price change.

**Failure case:** A trader goes long corn futures in August when the market is in mild backwardation ($0.05/bu per month) due to tight old crop supply. By October, the new harvest floods the market, the curve flips to contango ($0.08/bu per month), and the trader now incurs roll costs instead of gains. If the trader earned $0.10/bu in roll gain during 2 months of backwardation but paid $0.24/bu in roll costs over 3 months of contango, the net roll return is negative $0.14/bu. The lesson: backwardation is not permanent, and the curve can flip after harvest or a demand shock, converting roll gains into [[Contango Roll Cost|roll costs]].

## Key mechanics and formulas
- **Roll gain per period = Front month price - Deferred month price** (positive when in backwardation)
- **Annualized roll yield ~ Average monthly backwardation x 12**
- **Total return decomposition:** Commodity futures return = Spot return + Roll yield + Collateral yield (interest earned on margin)
- **Historical evidence:** Academic studies (Gorton/Rouwenhorst, AQR) show backwardated commodities have outperformed contango commodities by 5 to 10% per year on average over multi decade samples
- **Carry signal:** Rank commodities by roll yield each month; go long the most backwardated (highest carry) and short the most contango (lowest carry). This cross sectional carry strategy has a Sharpe ratio of 0.4 to 0.7 historically.
- **Relationship to scarcity:** Backwardation = Low inventory = High convenience yield = Positive roll yield. The economic logic connects inventory data to roll returns.

## Prerequisites
- [[Futures Contract]]
- [[Spread Trade]]
- [[Stocks to Use Ratio]]

## Related concepts (learn next)
- [[Contango Roll Cost]] is the opposite effect: loss from rolling in contango, which erodes returns for passive longs.
- [[Spread Trade]] in calendar spreads is the direct expression of backwardation and contango economics.
- [[Stocks to Use Ratio]] determines whether a market is likely in backwardation (low S/U = tight = backwardated) or contango (high S/U = surplus = contango).
- [[Old Crop New Crop]] spread is a specific form of backwardation when old crop trades at a premium to new crop.
- [[Delivery]] economics drive the theoretical limits of backwardation near expiry.
- [[Grains]] frequently shift between backwardation and contango depending on the [[Crop Year]] balance sheet.
- [[COT Positioning]] shows that managed money tends to be net long in backwardated markets, reinforcing the structure.
- [[Basis Risk]] exists when a carry strategy is long a backwardated futures contract but the trader's physical exposure tracks a different price index.

## Common misconceptions
- **"Backwardation roll gain is guaranteed."** Backwardation can flip to contango at any time due to demand destruction, new supply, or inventory builds. The roll gain is only earned during periods when the curve remains backwardated at roll time.
- **"You need to time the roll perfectly."** The gain is captured on every roll in a backwardated market, regardless of the exact roll date. Consistency of being long in backwardated markets matters more than precise roll timing.
- **"Roll yield is a free lunch."** Backwardated markets are typically tight, meaning you are taking the risk that supply disruptions persist and prices remain elevated. If the market loosens unexpectedly, both spot price and backwardation can collapse simultaneously, creating correlated losses on both the directional and carry components.
- **"Backwardation means prices will fall."** Backwardation reflects current scarcity and high convenience yield. Spot prices in backwardated markets can continue to rise if supply remains tight.

## Sources
- Gary Gorton and K. Geert Rouwenhorst, "Facts and Fantasies about Commodity Futures"
- AQR, "Carry" (working paper on cross asset carry strategies)
- CME Group, "Roll Yield and Commodity Returns"
- Erb, C. and Harvey, C., "The Strategic and Tactical Value of Commodity Futures"
