---
aliases: [liquidity, market liquidity, market depth, order book depth]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Liquidity

## Definition

Liquidity is the ease of buying or selling an asset without significantly moving its price. A liquid market has tight [[Bid-Ask Spread|spreads]], deep order books, high volume, and low [[Market Impact]]. An illiquid market has wide spreads, thin books, low volume, and high impact per unit traded. Liquidity is a spectrum, varying across instruments, time of day, conditions, and contract months. Without it, strategies cannot be executed, hedges cannot be maintained, risk cannot be managed.

## Why it matters (commodities and FX)

Commodity liquidity is concentrated. [[WTI Crude Oil]] [[Front Month]] is one of the most liquid instruments globally (500,000+ contracts/day). 18th month WTI might trade 5,000. [[Gold Futures]] are liquid; platinum is thin. EUR/USD trades $500B+/day; USD/CLP trades $5B. Size positions and pick contract months around available liquidity, not just the view. A brilliant [[Calendar Spread]] in an illiquid back month is untradeable.

Liquidity has a regime component: abundant in calm markets, evaporates in stressed markets (inverse to [[Volatility]]). Cruel irony: you most need liquidity to exit precisely when it is least available.

## Concrete example

**Concrete:** [[WTI Crude Oil]] CL order book in regular hours: bid $74.01 x 150, $74.00 x 300, $73.99 x 200; ask $74.02 x 180, $74.03 x 250, $74.04 x 200. Spread $0.01. Top 3 levels: 650 bid, 630 ask. Market buy 50 contracts fills entirely at $74.02. Market buy 500 contracts sweeps: 180 at $74.02, 250 at $74.03, 70 at $74.04, avg ~$74.027. [[Market Impact]] = $0.007/bbl on 500 contracts. Compare palladium: bid $948 x 5, $946 x 10; ask $952 x 8, $954 x 5. Spread $4 (4 ticks of $1). Top 2 levels: 15 bid, 13 ask. Buying 20 contracts sweeps with material impact.

**Simplified:** Liquid means you can trade size now without moving the price much. Illiquid means even a moderate order shoves the price against you. Same instrument can be liquid at noon and illiquid at midnight, or liquid in calm markets and gone in a crash. Always check what is actually available before sizing.

## Key mechanics and formulas

**Liquidity metrics:**

| Metric | Definition | Good (WTI) | Poor (thin) |
|--------|-----------|------------|-------------------|
| Bid-ask spread | Ask - Bid | $0.01 | $1.00+ |
| Depth | Volume at best bid/ask | 100+ lots | 5 to 10 lots |
| ADV | Average daily volume | 500,000 | 1,000 |
| Turnover ratio | ADV / Open Interest | >50% | <10% |

**Kyle's lambda (price impact):**
`ΔP = λ x OrderFlow`

Low lambda = liquid. High lambda = illiquid.

**Amihud illiquidity:**
`ILLIQ = |Return| / Dollar Volume`

Higher = more illiquid.

## Prerequisites
- [[Forward Curve]]
- [[Front Month]]

## Related concepts (learn next)
- [[Bid-Ask Spread]] - the most visible measure. Tight = liquid
- [[Market Impact]] - cost of trading in price movement, directly tied to depth
- [[Slippage]] - execution cost vs intended price, worse in illiquid markets
- [[Liquidity Risk]] - the risk dimension; what happens when you cannot exit
- [[Volatility]] - inversely related. Vol spikes = liquidity drops
- [[Execution Algorithms]] - algos navigate liquidity; effectiveness depends on it

## Common misconceptions

**"Volume = liquidity."** Volume correlates with liquidity but is not the same. A market can have high volume but poor liquidity if volume is one sided or concentrated in a few large prints.

**"Screen liquidity is real liquidity."** The visible book is not the full picture. Resting liquidity is hidden (icebergs, dark pools). Displayed liquidity also evaporates instantly as passive makers cancel in fast markets.

**"Liquid markets stay liquid."** Liquidity is conditional. 2010 Flash Crash, 2014 Treasury flash crash, 2019 repo crisis all showed the most liquid markets can become temporarily illiquid.

## Sources

- Kyle, Albert, "Continuous Auctions and Insider Trading" (1985, Econometrica)
- Amihud, Yakov, "Illiquidity and Stock Returns" (2002, Journal of Financial Markets)
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003)
