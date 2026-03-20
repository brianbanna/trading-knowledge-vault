---
aliases: [bid-ask spread, bid-offer spread, spread, tick spread, bid offer]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Bid-Ask Spread

## Definition

The bid-ask spread is the difference between the highest price a buyer is willing to pay (the bid) and the lowest price a seller is willing to accept (the ask, or offer). It represents the cost of immediacy: crossing the spread to trade NOW costs the bid-ask spread. The spread compensates market makers for providing [[Liquidity]], bearing inventory risk, and facing adverse selection (trading against informed participants). Tight spreads indicate high liquidity and competition among market makers. Wide spreads indicate illiquidity, uncertainty, or low competition.

## Why it matters (commodities and FX)

The bid-ask spread is the most immediate transaction cost in trading. Every round trip (buy then sell) costs at least 1 full spread. For a high frequency [[Calendar Spread]] trader doing 50 round trips per day, the spread cost can exceed commission costs by 10x. For longer horizon traders, the spread matters at entry and exit but is less dominant relative to the expected P&L of the trade.

In commodity markets, spreads vary enormously: 1 tick ($0.01/bbl) in [[WTI Crude Oil]] front month, versus $1+/bbl in deferred months or thin commodities. In FX, EUR/USD trades at 0.1 to 0.5 pip in the interbank market, while EM pairs like USD/TRY can be 5 to 50 pips. Understanding the spread landscape is essential for choosing which instruments and contract months to trade.

## Concrete example

You want to buy 100 [[Brent Crude]] contracts. The screen shows bid $78.20 x 200, ask $78.21 x 150. The spread is $0.01 (1 tick). If you buy at the ask ($78.21) and later sell at the bid (assume same spread), the round trip cost is $0.01/bbl x 1,000 bbl x 100 contracts = $1,000. This is the minimum cost of doing the trade, before commissions and [[Market Impact]].

Now consider a thinner instrument: [[Platinum Futures]] bid $940 x 10, ask $942 x 8. Spread = $2.00 per oz. A round trip on 1 contract (50 oz) costs $2.00 x 50 = $100. On 10 contracts: $1,000. The bid-ask cost in platinum is much higher per dollar notional than in WTI.

## Key mechanics and formulas

**Bid-ask spread:**
`Spread = Ask - Bid`

**Relative spread (for cross instrument comparison):**
`Relative Spread = (Ask - Bid) / Midpoint x 10,000` (in basis points)

WTI at 78.20/78.21: relative spread = 0.01/78.205 x 10,000 = 1.3 bps
Platinum at 940/942: relative spread = 2/941 x 10,000 = 21.3 bps

**Effective spread (what you actually pay):**
`Effective Spread = 2 x |Trade Price - Midpoint|`

If mid is $78.205 and you buy at $78.21, effective half spread = $0.005, effective full spread = $0.01. Can be wider than quoted spread if your order is large enough to move the price.

**Components of the spread:**
1. **Inventory risk:** market maker compensation for holding unwanted positions
2. **Adverse selection:** compensation for trading against informed participants
3. **Order processing:** fixed costs of providing quotes and executing trades

## Prerequisites
- [[Liquidity]]
- [[Front Month]]

## Related concepts (learn next)
- [[Liquidity]] - bid-ask spread is the most visible liquidity measure.
- [[Market Impact]] - what happens when your order is larger than the size at the best bid/ask.
- [[Slippage]] - the difference between intended and actual execution price, often driven by the spread.
- [[VWAP]] - execution benchmarks account for spread costs.
- [[Execution Algorithms]] - algos try to capture the spread (buying at or near the bid) rather than crossing it.

## Common misconceptions

**"The quoted spread is the actual cost of trading."** For small orders, yes. For larger orders, you cross through multiple price levels, and the effective spread is wider than the quoted spread. This is [[Market Impact]].

**"Tighter spreads are always better."** Tight spreads in thin markets (where the displayed size is small) can be misleading. You might see a 1 tick spread but only 5 lots available. Trying to trade 50 lots means sweeping through much wider levels.

**"Spreads are constant throughout the day."** Spreads widen at market open, around data releases (EIA, NFP), during overnight sessions, and at market close. The cheapest execution happens during peak liquidity hours with no imminent event risk.

## Sources

- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003)
- CME Group: market data and best practices
- O'Hara, Maureen, "Market Microstructure Theory" (1995)
