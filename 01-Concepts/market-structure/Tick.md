---
aliases: [tick size, minimum price increment, price tick, minimum tick]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Tick

## Definition

A tick is the smallest price increment an instrument can move. It defines the granularity of the price grid. In [[EUR USD]], tick size is 0.00001 (1/10 of a [[Pip]]). In [[WTI]] futures on CME, tick size is $0.01 per barrel. Tick size is set by the exchange or venue and determines the minimum [[Bid-Ask Spread]], precision of limit orders, and the economics of market making. Smaller ticks allow tighter spreads but create more price levels to monitor.

## Why it matters (commodities and FX)

Tick size directly affects trading costs and strategy viability. If [[EUR USD]] had a 1 pip tick (0.0001) instead of 0.1 pip (0.00001), minimum spread would be 1 pip, roughly tripling transaction costs. For market makers, the tick determines minimum profit per [[Round Trip]]. In commodity futures, tick size × contract size = tick value, the dollar PnL per tick move.

## Concrete example

**Concrete:** FX: [[EUR USD]] tick = 0.00001. Quote 1.08497 / 1.08498 is a 1 tick spread (0.1 pip). Each tick on a standard 100,000 unit position = $1.00. Commodities: [[WTI]] futures (CL) have tick = $0.01/bbl, contract = 1,000 bbl. 1 tick = $0.01 × 1,000 = $10 per contract. Market maker quotes WTI at $82.50 / $82.51 (1 tick wide), buys at $82.50 and sells at $82.51, earns $10 per contract. Adversarial: the same maker quotes 1 tick wide on an instrument that should be 3 wide. Informed traders pick off the tight quotes. Each adverse trade costs multiples of the $10 tick profit.

**Simplified:** The smallest move a price is allowed to make. Smaller ticks = tighter possible spreads but more price levels. Tick value (tick size × contract size) is the dollar PnL of a 1 tick move. Market makers live and die on the size of the tick relative to their adverse selection costs.

## Key mechanics and formulas

**Tick value** = tick size × contract size (or position size)

| Instrument | Tick size | Contract size | Tick value |
|-----------|-----------|---------------|------------|
| [[EUR USD]] (spot) | 0.00001 | 100,000 | $1.00 |
| [[WTI]] (CL) | $0.01 | 1,000 bbl | $10.00 |
| [[Brent Crude]] (ICE) | $0.01 | 1,000 bbl | $10.00 |
| [[Gold]] (GC) | $0.10 | 100 oz | $10.00 |
| [[Copper Futures]] (HG) | $0.0005 | 25,000 lbs | $12.50 |
| E mini S&P 500 (ES) | $0.25 | $50 multiplier | $12.50 |

**Minimum spread in ticks:** most liquid instruments trade 1 tick wide. Less liquid instruments trade multiple ticks wide.

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

1. **"A tick and a pip are the same."** In [[EUR USD]], pip = 0.0001 and tick = 0.00001 (1/10 of a pip). A tick is the exchange's minimum increment; a pip is a market quoting convention.

2. **"Smaller tick sizes are always better."** Smaller ticks enable tighter spreads but fragment liquidity across more levels. Optimal tick size balances tight spreads with sufficient depth.

3. **"Tick size is the same across venues."** Different venues for the same instrument can use different tick sizes. EBS and Refinitiv price [[EUR USD]] at different precisions.

## Sources

- CME Group, "Contract Specifications" (tick sizes for all listed futures)
- ICE, "Contract Specifications"
- Harris, Larry, "Trading and Exchanges," Oxford University Press
