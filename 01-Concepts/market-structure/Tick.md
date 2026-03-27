---
aliases: [tick size, minimum price increment, price tick, minimum tick]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Tick

## Definition

A tick is the smallest possible price increment that an instrument can move. It defines the granularity of the price grid. In [[EUR USD]], the tick size is 0.00001 (one tenth of a [[Pip]]). In [[WTI]] crude futures on CME, the tick size is $0.01 per barrel. Tick size is set by the exchange or venue and determines the minimum [[Bid-Ask Spread]], the precision of limit orders, and the economics of market making. Smaller ticks allow tighter spreads but create more price levels to monitor.

## Why it matters (commodities and FX)

Tick size directly affects trading costs and strategy viability. If [[EUR USD]] had a tick size of 1 pip (0.0001) instead of 0.1 pip (0.00001), the minimum spread would be 1 pip, roughly tripling transaction costs. For market makers, the tick determines the minimum profit per [[Round Trip]]. In commodity futures, tick size multiplied by contract size gives the tick value, which is the dollar PnL per tick move.

## Concrete example

**FX:** [[EUR USD]] has a tick size of 0.00001. A quote of 1.08497 / 1.08498 is a 1 tick spread (0.1 pip). Each tick on a standard 100,000 unit position = $1.00.

**Commodities:** [[WTI]] crude futures (CL) have a tick size of $0.01 per barrel, and 1 contract = 1,000 barrels. So 1 tick = $0.01 * 1,000 = $10.00 per contract.

**Success case:** A market maker quotes WTI at $82.50 / $82.51 (1 tick spread). They buy at $82.50 and sell at $82.51, earning 1 tick = $10 per contract.

**Failure case:** The market maker quotes 1 tick wide, but the instrument's true spread should be 3 ticks. They get adversely selected because informed traders pick off their tight quotes. Each adverse trade costs multiples of the $10 tick profit.

## Key mechanics and formulas

**Tick value** = tick size * contract size (or position size)

| Instrument | Tick size | Contract size | Tick value |
|-----------|-----------|---------------|------------|
| [[EUR USD]] (spot) | 0.00001 | 100,000 | $1.00 |
| [[WTI]] (CL) | $0.01 | 1,000 bbl | $10.00 |
| [[Brent Crude]] (ICE) | $0.01 | 1,000 bbl | $10.00 |
| [[Gold]] (GC) | $0.10 | 100 oz | $10.00 |
| [[Copper Futures]] (HG) | $0.0005 | 25,000 lbs | $12.50 |
| E mini S&P 500 (ES) | $0.25 | $50 multiplier | $12.50 |

**Minimum spread in ticks:**
Most liquid instruments trade at 1 tick wide. Less liquid instruments trade multiple ticks wide.

## Prerequisites

- [[Bid]]
- [[Ask]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)

- [[Pip]] for the standard FX price unit (10 ticks in most pairs)
- [[Bid-Ask Spread]] for how tick size constrains the minimum spread
- [[Depth of Book]] for how orders stack at each tick level
- [[Tick Data]] for time series recorded at tick level granularity
- [[Top of Book]] for the best bid and ask at the finest tick resolution
- [[Slippage]] for price movement measured in ticks during execution

## Common misconceptions

1. **"A tick and a pip are the same thing."** In [[EUR USD]], a pip is 0.0001 and a tick is 0.00001 (one tenth of a pip). A tick is the exchange's minimum increment; a pip is a market convention for quoting.

2. **"Smaller tick sizes are always better."** Smaller ticks allow tighter spreads but fragment liquidity across more price levels. The optimal tick size balances tight spreads against sufficient depth at each level.

3. **"Tick size is the same across all venues."** Different venues for the same instrument can have different tick sizes. EBS and Refinitiv may price [[EUR USD]] at different precisions.

## Sources

- CME Group, "Contract Specifications" (tick sizes for all listed futures)
- ICE, "Contract Specifications"
- Harris, Larry, "Trading and Exchanges," Oxford University Press
