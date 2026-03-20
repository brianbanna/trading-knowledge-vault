---
aliases: [contango carry, metals carry trade, cash and carry metals]
tags:
  - "#metals/base"
date-added: "2026-03-20"
---

# Contango Carry Metals

## Definition

Contango carry in metals is the cost of financing physical metal in storage, which sets the theoretical maximum for the [[Contango]] spread between Cash and the 3 Month (or other deferred) [[LME Prompt Date|prompt date]]. The carry cost includes LME warehouse rent, insurance, and the financing rate (interest rate times the metal value). When the actual Cash/3M contango exceeds the total carry cost, a risk free arbitrage exists: buy Cash metal (take delivery), pay warehouse rent and financing, and simultaneously sell forward. This "cash and carry" trade caps how wide contango can get, because arbitrageurs step in to capture the spread, buying Cash and selling forward until the contango narrows to the carry cost.

## Why it matters (commodities and FX)

The contango carry relationship is fundamental to understanding metals curve shape. In a well supplied market, the Cash/3M contango should approximate the cost of carry. When contango is less than carry cost, it signals that the market is tighter than it appears (approaching backwardation). When contango exceeds carry cost, it signals a temporary dislocation that arbitrageurs will correct. For warehouse operators and trading houses, the carry trade is a core profit center: firms like Glencore and Trafigura earn steady returns by financing metal in storage during contango markets. For financial traders, monitoring contango relative to carry cost helps identify when the market is mispricing physical conditions.

## Concrete example

LME aluminum Cash is at $2,380/tonne and 3 Month is at $2,420/tonne, a $40 contango. The carry cost for 3 months is: LME rent ($8/tonne/month × 3 = $24) + insurance ($3) + financing (5% annualized × $2,380 × 3/12 = $30) = $57 total. Since the contango ($40) is less than carry cost ($57), the cash and carry trade is not profitable, meaning the market is tighter than pure contango suggests. If contango widened to $70 (exceeding the $57 carry), a trader would buy Cash aluminum, store it in the LME warehouse, and sell 3 Month forward, locking in $13/tonne profit.

## Key mechanics and formulas

**Cash and carry profit:** `Profit = (3M Price - Cash Price) - (Rent + Insurance + Financing)`

**Carry cost components:**
- LME warehouse rent: $5 to $15/tonne/month (varies by metal and location)
- Insurance: ~$1 to $3/tonne for 3 months
- Financing: `Metal Value × Interest Rate × Time Period`

**Maximum contango:** `Max Contango ≈ Rent + Insurance + Financing for the period`

If actual contango > this, the cash and carry arb is profitable and will be exploited.

## Prerequisites

- [[Contango]]
- [[Cash to 3 Month Spread]]
- [[Cost of Carry]]
- [[LME]]

## Related concepts (learn next)

- [[Cash to 3 Month Spread]] because the contango carry relationship defines the theoretical bounds of this spread.
- [[Cost of Carry]] because metals carry costs parallel the general cost of carry framework for all commodities.
- [[Contango]] because the carry trade only works in contango markets.
- [[LME Warehouse Stocks]] because metal held for carry trades adds to visible LME stocks.
- [[Backwardation]] because backwardation signals that convenience yield exceeds carry costs, ending the carry trade.
- [[Physical Premium]] because carry economics affect the decision to hold metal in LME vs deliver it physically.

## Common misconceptions

**"The cash and carry trade is always profitable in contango."** Only when the contango exceeds all in carry costs. Many mild contango markets do not offer enough spread to cover rent, insurance, and financing.

**"Carry costs are fixed."** Interest rates change, LME rents vary by location and metal, and insurance costs fluctuate. Rising interest rates directly increase financing costs and narrow the window for profitable carry.

**"The carry trade has no risk."** Execution risk (sourcing and delivering metal), counterparty risk (on the forward sale), and warehouse queue risk (delays in withdrawal) all create real, though typically small, risks.

## Sources

- LME: Warehouse Rent Schedule
- CRU Group: Metals Financing and Carry Trade Analysis
- CME Group: Understanding Contango and Carry in Commodities
