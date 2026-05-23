---
aliases: [contango carry, metals carry trade, cash and carry metals]
tags:
  - "#metals/base"
date-added: "2026-03-20"
---

# Contango Carry Metals

## Definition

Contango carry in metals is the cost of financing physical metal in storage, setting the theoretical maximum for the [[Contango]] spread between Cash and the 3 Month (or other deferred) [[LME Prompt Date|prompt date]]. Carry cost = LME warehouse rent + insurance + financing (rate × metal value). When actual Cash/3M contango exceeds total carry, a risk free arbitrage exists: buy Cash metal (take delivery), pay rent and financing, simultaneously sell forward. This "cash and carry" trade caps contango width: arbitrageurs step in until contango narrows back to carry cost.

## Why it matters (commodities and FX)

The contango carry relationship is fundamental to metals curve shape. In a well supplied market, Cash/3M contango approximates cost of carry. Contango below carry signals the market is tighter than it looks (approaching backwardation). Contango above carry signals a temporary dislocation arbitrageurs will correct. For warehouse operators and trading houses, the carry trade is a core profit center: Glencore and Trafigura earn steady returns financing metal in storage during contango markets. For financial traders, monitoring contango vs carry cost flags when the market is mispricing physical conditions.

## Concrete example

**Concrete:** LME aluminum Cash $2,380/tonne, 3 Month $2,420: $40 contango. 3 month carry = rent ($8 × 3 = $24) + insurance ($3) + financing (5% × $2,380 × 3/12 = $30) = $57 total. Contango ($40) < carry ($57): cash and carry not profitable, market tighter than pure contango suggests. If contango widens to $70 (exceeds $57 carry), trader buys Cash aluminum, stores in LME warehouse, sells 3 Month forward, locking in $13/tonne profit.

**Simplified:** Storing metal costs money: rent, insurance, financing the inventory. In a contango market, the futures price is higher than spot. If the gap covers your storage costs and then some, you can buy metal today, pay to store it, sell it forward at the higher price, and pocket the difference risk free. Arbitrageurs do this until the gap shrinks back to just covering storage. So contango cannot get much wider than the cost of storing the metal.

## Key mechanics and formulas

**Cash and carry profit:** `Profit = (3M Price − Cash Price) − (Rent + Insurance + Financing)`

**Carry cost components:**
- LME warehouse rent: $5 to $15/tonne/month (varies by metal and location)
- Insurance: ~$1 to $3/tonne for 3 months
- Financing: `Metal Value × Interest Rate × Time`

**Maximum contango:** `Max Contango ≈ Rent + Insurance + Financing for the period`

If actual contango > this, the cash and carry arb is profitable.

## Prerequisites

- [[Contango]]
- [[Cash to 3 Month Spread]]
- [[Cost of Carry]]
- [[LME]]

## Related concepts (learn next)

- [[Cash to 3 Month Spread]] because the contango carry relationship defines its theoretical bounds.
- [[Cost of Carry]] because metals carry parallels the general framework.
- [[Contango]] because the carry trade only works in contango.
- [[LME Warehouse Stocks]] because metal held for carry adds to visible LME stocks.
- [[Backwardation]] because backwardation signals convenience yield exceeds carry, ending the trade.
- [[Physical Premium]] because carry economics affect the choice to hold in LME vs deliver physically.

## Common misconceptions

**"The cash and carry trade is always profitable in contango."** Only when contango exceeds all in carry costs. Mild contango markets do not cover rent, insurance, and financing.

**"Carry costs are fixed."** Rates change, LME rents vary by location and metal, insurance fluctuates. Rising rates directly increase financing and narrow the profitable window.

**"The carry trade has no risk."** Execution risk (sourcing and delivering metal), counterparty risk (on the forward), and warehouse queue risk (delays in withdrawal) all create real if small risks.

## Sources

- LME: Warehouse Rent Schedule
- CRU Group: Metals Financing and Carry Trade Analysis
- CME Group: Understanding Contango and Carry in Commodities
