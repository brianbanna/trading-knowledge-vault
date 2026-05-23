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

Roll yield is the P&L generated when a futures position is rolled from an expiring contract to the next contract along the [[Forward Curve]]. In [[Backwardation]] (front higher than deferred), rolling a long position generates positive roll yield because you sell the expiring contract high and buy the next one low. In [[Contango]] (front lower), rolling a long generates negative roll yield (roll cost). Roll yield is a critical and often misunderstood component of commodity returns.

## Why it matters (commodities and FX)

Roll yield dominates total commodity returns over time, often exceeding spot price changes. Deep contango destroys returns even if spot rises. USO (oil) and UNG (natural gas) have historically underperformed spot dramatically because they bleed negative roll yield monthly. For an active trader, roll yield drives which contract to hold, when to roll, and whether a [[Calendar Spread]] has structural carry in your favor.

Roll yield is the commodity analogue of [[Carry Trade|carry in FX]]. Backwardation pays you carry. Contango charges you carry.

## Concrete example

**Concrete:** [[Henry Hub Natural Gas]] March at $3.50, April at $3.70. Curve in [[Contango]]. You hold a long March and roll before expiry. Sell March at $3.50, buy April at $3.70. Pay $0.20/MMBtu to maintain exposure. On 10,000 MMBtu, that is $2,000 negative roll yield. If spot stays flat at $3.50, you lose $2,000. Spot must rise more than $0.20 to break even. Reverse the curve (March $3.70, April $3.50) and you earn $2,000 rolling even with spot flat.

**Simplified:** Futures positions cannot be held forever. Before the contract expires you sell it and buy the next one. If the next contract is cheaper than the one you sold, you make money on the roll. If it is more expensive, you lose. For long positions, backwardation is a tailwind, contango is a headwind. Over years, this roll P&L can dwarf the actual spot move.

## Key mechanics and formulas

**Roll yield (single roll):**
`Roll Yield = (Price of expiring contract - Price of new contract) / Price of expiring contract`

**Annualized roll yield (approximate):**
`Annualized Roll Yield = Roll Yield x (365 / Days between rolls)`

**Total return decomposition for commodity futures:**
`Total Return = Spot Return + Roll Yield + Collateral Yield`

Collateral yield = interest on margin posted (T bill rate).

**Roll yield as share of total return:** In the S&P GSCI 1970 to 2020, roll yield contributed over half of total returns in backwardated markets and destroyed over half of spot gains in contangoed markets.

## Prerequisites

- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]
- [[Convenience Yield]]
- [[Futures Contract Mechanics]]

## Related concepts (learn next)

- [[Calendar Spread]] - directly trades the roll yield. Calendar spread P&L = change in roll yield.
- [[Cost of Carry Model]] - theoretical framework. Storage, financing, convenience yield all feed in.
- [[Optimal Roll Timing]] - choosing when to roll based on curve shape and liquidity improves returns.
- [[Commodity Index Construction]] - GSCI, BCOM, DBIQ use different roll schedules and produce different returns from the same commodities.
- [[Carry Trade]] - the FX analogue.
- [[Term Structure Signal]] - curve slope (which determines roll yield) is itself a signal: backwardated markets outperform contangoed ones.

## Common misconceptions

**"Spot price is what matters."** For futures investors, roll yield matters more than spot direction over multi month horizons. Natural gas has had periods where spot rose 30% but long futures lost money because contango exceeded the gain.

**"Roll yield is a transaction cost."** Not a fee. It is a structural feature of the forward curve reflecting physical market conditions (storage, supply tightness, convenience yield). Genuine return source, positive or negative.

**"Hold longer dated contracts to avoid roll yield."** You avoid frequent rolling but still face the initial discount or premium of the deferred contract versus spot. Roll yield spread over a longer period, not eliminated.

## Sources

- Gorton and Rouwenhorst, "Facts and Fantasies about Commodity Futures" (2006)
- Erb and Harvey, "The Strategic and Tactical Value of Commodity Futures" (2006)
- CME Group: Understanding Roll Yield in Commodity Markets
