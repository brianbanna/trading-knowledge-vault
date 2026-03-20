---
aliases: [roll yield, roll return, roll cost]
tags:
  - "#energy/crude"
  - "#energy/natgas"
  - "#metals/base"
date-added: "2026-03-20"
---

# Roll Yield

## Definition

Roll yield is the P&L generated when a futures position is rolled from an expiring contract to the next contract along the [[Forward Curve]]. In [[Backwardation]] (front month priced higher than deferred), rolling a long position generates positive roll yield because you sell the expiring contract at a higher price and buy the next one at a lower price. In [[Contango]] (front month priced lower), rolling a long position generates negative roll yield (the "roll cost"). Roll yield is a critical and often misunderstood component of total returns in commodity investing.

## Why it matters (commodities and FX)

Roll yield can be the dominant component of total commodity returns over time, often exceeding spot price changes. A commodity in deep contango can destroy returns even if the spot price is rising. This is why ETFs like USO (oil) and UNG (natural gas) have historically underperformed spot prices dramatically: they bleed value through negative roll yield every month. For an active trader, understanding roll yield is essential for choosing which contract month to hold, when to roll, and whether a [[Calendar Spread]] trade has structural carry in your favor.

Roll yield is the commodity analogue of [[Carry Trade|carry in FX]]. A commodity in backwardation is "paying you carry." A commodity in contango is "charging you carry."

## Concrete example

[[Henry Hub Natural Gas]] March contract trades at $3.50. April contract trades at $3.70. The market is in [[Contango]]. You hold a long March position and need to roll before expiry.

Roll: sell March at $3.50, buy April at $3.70. You pay $0.20/MMBtu to maintain your long exposure. On a 10,000 MMBtu contract, that is $2,000 of negative roll yield. If natgas spot stays flat at $3.50, you lose $2,000. You need spot to rise by more than $0.20 just to break even.

Conversely, if the curve were in backwardation (March at $3.70, April at $3.50), you would earn $0.20/MMBtu ($2,000) when rolling. You profit even if spot stays flat.

## Key mechanics and formulas

**Roll yield (single roll):**
`Roll Yield = (Price of expiring contract - Price of new contract) / Price of expiring contract`

**Annualized roll yield (approximate):**
`Annualized Roll Yield = Roll Yield x (365 / Days between rolls)`

**Total return decomposition for commodity futures:**
`Total Return = Spot Return + Roll Yield + Collateral Yield`

Where collateral yield is the interest earned on the margin/collateral posted (typically T bill rate).

**Roll yield as percentage of total return:** In the S&P GSCI commodity index over 1970 to 2020, roll yield contributed more than half of total returns in backwardated markets and destroyed more than half of spot gains in contangoed markets.

## Prerequisites

- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Convenience Yield]]
- [[Futures Contract Mechanics]]

## Related concepts (learn next)

- [[Calendar Spread]] - directly trades the roll yield. When you put on a calendar spread, your P&L IS the change in roll yield between the 2 contract months.
- [[Cost of Carry Model]] - the theoretical framework that determines whether roll yield is positive or negative. Storage costs, financing, and convenience yield all feed into it.
- [[Optimal Roll Timing]] - you don't have to roll at a fixed date. Choosing when to roll based on curve shape and liquidity can improve returns.
- [[Commodity Index Construction]] - different commodity indices (GSCI, BCOM, DBIQ) use different roll schedules and methodologies, producing dramatically different returns from the same underlying commodities.
- [[Carry Trade]] - the FX analogue. Understanding carry as a universal concept across asset classes deepens your grasp of both.
- [[Term Structure Signal]] - the slope of the forward curve (which determines roll yield) is itself a trading signal: backwardated markets tend to outperform contangoed markets.

## Common misconceptions

**"Spot price is what matters for commodity returns."** For futures investors, roll yield often matters more than spot direction over multi month horizons. Natural gas has had periods where spot rose 30% but long futures holders lost money because contango roll cost exceeded the spot gain.

**"Roll yield is a transaction cost."** It is not a fee or cost. It is a structural feature of the forward curve that reflects physical market conditions (storage, supply tightness, convenience yield). It can be positive or negative and is a genuine source of return.

**"You can avoid roll yield by holding longer dated contracts."** You avoid frequent rolling but you still face the initial discount or premium embedded in the deferred contract vs spot. The roll yield is just spread over a longer period.

## Sources

- Gorton and Rouwenhorst, "Facts and Fantasies about Commodity Futures" (2006)
- Erb and Harvey, "The Strategic and Tactical Value of Commodity Futures" (2006)
- CME Group: Understanding Roll Yield in Commodity Markets
