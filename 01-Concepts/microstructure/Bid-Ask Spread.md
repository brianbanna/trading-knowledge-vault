---
aliases: [bid-ask spread, bid-offer spread, spread, tick spread, bid offer]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Bid-Ask Spread

## Definition

The bid ask spread is the difference between the highest bid and the lowest ask. It is the cost of immediacy: crossing the spread to trade now costs the spread. The spread compensates market makers for providing [[Liquidity]], bearing inventory risk, and facing adverse selection. Tight spreads indicate liquidity and competition. Wide spreads indicate illiquidity, uncertainty, or low competition.

## Why it matters (commodities and FX)

The spread is the most immediate transaction cost. Every round trip costs at least 1 full spread. For a high turnover [[Calendar Spread]] trader doing 50 round trips per day, spread cost dwarfs commissions by 10x. For longer horizon traders, spread matters at entry and exit but is less dominant relative to expected P&L.

Commodity spreads vary by orders of magnitude: 1 tick ($0.01/bbl) in [[WTI Crude Oil]] front month, vs $1+/bbl in deferred months or thin commodities. In FX, EUR/USD trades 0.1 to 0.5 pip interbank, while USD/TRY runs 5 to 50 pips. Picking the instrument and contract month around available spread is essential.

## Concrete example

**Concrete:** Buying 100 [[Brent Crude]] contracts. Screen: bid $78.20 x 200, ask $78.21 x 150. Spread $0.01 (1 tick). Buy at $78.21 and later sell at the bid: round trip cost = $0.01/bbl x 1,000 bbl x 100 contracts = $1,000. That is the minimum before commissions and [[Market Impact]]. Now [[Platinum Futures]]: bid $940 x 10, ask $942 x 8. Spread $2.00 per oz. Round trip on 1 contract (50 oz) = $100. On 10 contracts: $1,000. Bid ask cost in platinum is far higher per dollar notional than WTI.

**Simplified:** The bid is what buyers will pay. The ask is what sellers want. The gap between them is the spread. If you want to trade right now, you pay the spread. Tight spread, cheap to trade. Wide spread, expensive. Buy then sell on the same prices and you lose exactly one spread, whether the market moved or not.

## Key mechanics and formulas

**Bid ask spread:**
`Spread = Ask - Bid`

**Relative spread (cross instrument):**
`Relative Spread = (Ask - Bid) / Midpoint x 10,000` (bps)

WTI at 78.20/78.21: 0.01/78.205 x 10,000 = 1.3 bps
Platinum at 940/942: 2/941 x 10,000 = 21.3 bps

**Effective spread (actual paid):**
`Effective Spread = 2 x |Trade Price - Midpoint|`

Mid $78.205, buy at $78.21: effective half spread = $0.005, full = $0.01. Wider than quoted when the order moves price.

**Components:**
1. **Inventory risk:** compensation for holding unwanted positions
2. **Adverse selection:** compensation for informed counterparties
3. **Order processing:** fixed costs of quoting and execution

## Prerequisites
- [[Liquidity]]
- [[Front Month]]

## Related concepts (learn next)
- [[Liquidity]] - spread is the most visible liquidity measure
- [[Market Impact]] - what happens when your order exceeds size at best bid/ask
- [[Slippage]] - gap between intended and actual fill, often driven by spread
- [[VWAP]] - execution benchmarks account for spread costs
- [[Execution Algorithms]] - algos try to capture spread (buy at/near bid) rather than cross it

## Common misconceptions

**"Quoted spread is the actual cost."** For small orders, yes. Larger orders cross multiple levels and effective spread widens. That is [[Market Impact]].

**"Tighter spreads are always better."** Tight spreads in thin markets (small displayed size) are misleading. 1 tick spread with 5 lots displayed sweeps to far wider levels at 50 lots.

**"Spreads are constant through the day."** Spreads widen at open, around data (EIA, NFP), in overnight sessions, and at close. Cheapest execution is peak liquidity hours with no imminent event risk.

## Sources

- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003)
- CME Group: market data and best practices
- O'Hara, Maureen, "Market Microstructure Theory" (1995)
