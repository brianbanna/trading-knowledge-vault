---
aliases: [liquidity, market liquidity, market depth, order book depth]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Liquidity

## Definition

Liquidity is the ease with which an asset can be bought or sold without significantly moving its price. A liquid market has tight [[Bid-Ask Spread|bid-ask spreads]], deep order books (large quantity available at each price level), high trading volume, and low [[Market Impact]]. An illiquid market has wide spreads, thin order books, low volume, and large price impact per unit traded. Liquidity is not binary but a spectrum, and it varies across instruments, time of day, market conditions, and contract months. Liquidity is the lifeblood of trading: without it, strategies cannot be executed, hedges cannot be maintained, and risk cannot be managed.

## Why it matters (commodities and FX)

Commodity liquidity is highly concentrated. The [[Front Month]] of [[WTI Crude Oil]] is one of the most liquid instruments in the world (500,000+ contracts/day). The 18th month of WTI might trade 5,000 contracts. [[Gold Futures]] are liquid; platinum is thin. EUR/USD trades $500+ billion/day; USD/CLP trades $5 billion. A trader must size positions and choose contract months based on available liquidity, not just the view. A brilliant [[Calendar Spread]] trade in an illiquid back month is untradeable if you cannot get in or out.

Liquidity has a regime component: it is abundant in calm markets and evaporates in stressed markets (inverse relationship with [[Volatility]]). This creates a cruel irony: you most need liquidity to exit positions precisely when it is least available.

## Concrete example

[[WTI Crude Oil]] CL order book during regular trading hours:

| Bid | Size | Ask | Size |
|-----|------|-----|------|
| 74.01 | 150 | 74.02 | 180 |
| 74.00 | 300 | 74.03 | 250 |
| 73.99 | 200 | 74.04 | 200 |

Bid-ask spread: $0.01 (1 tick). Depth at top 3 levels: 650 bid, 630 ask. A market order to buy 50 contracts fills entirely at $74.02. A market order to buy 500 contracts sweeps through multiple levels: 180 at $74.02, 250 at $74.03, 70 at $74.04. Average fill: ~$74.027. [[Market Impact]] = $0.007/bbl on 500 contracts.

Compare to a thin commodity (e.g., palladium, PA):
| Bid | Size | Ask | Size |
|-----|------|-----|------|
| 948 | 5 | 952 | 8 |
| 946 | 10 | 954 | 5 |

Bid-ask spread: $4 (4 ticks of $1). Depth at top 2 levels: 15 bid, 13 ask. Buying 20 contracts sweeps through multiple levels with significant impact.

## Key mechanics and formulas

**Liquidity metrics:**

| Metric | Definition | Good (WTI) | Poor (thin market) |
|--------|-----------|------------|-------------------|
| Bid-ask spread | Ask minus Bid | $0.01 | $1.00+ |
| Depth | Volume at best bid/ask | 100+ lots | 5 to 10 lots |
| ADV | Average daily volume | 500,000 | 1,000 |
| Turnover ratio | ADV / Open Interest | >50% | <10% |

**Kyle's lambda (price impact):**
`ΔP = λ x OrderFlow`

Lambda measures how much the price moves per unit of net order flow. Low lambda = liquid. High lambda = illiquid.

**Amihud illiquidity measure:**
`ILLIQ = |Return| / Dollar Volume`

Average daily absolute return divided by dollar volume. Higher = more illiquid.

## Prerequisites
- [[Forward Curve]]
- [[Front Month]]

## Related concepts (learn next)
- [[Bid-Ask Spread]] - the most visible measure of liquidity. Tight spread = liquid.
- [[Market Impact]] - the cost of trading in terms of price movement. Directly related to liquidity depth.
- [[Slippage]] - the execution cost relative to intended price. Worse in illiquid markets.
- [[Liquidity Risk]] - the risk dimension of illiquidity. What happens when you cannot exit.
- [[Volatility]] - inversely related to liquidity. Vol spikes = liquidity drops.
- [[Execution Algorithms]] - algos are designed to navigate liquidity optimally. Their effectiveness depends on available liquidity.

## Common misconceptions

**"Volume = liquidity."** Volume is a correlate of liquidity but not the same thing. A market can have high volume but poor liquidity if the volume is one sided (all buying, no selling) or concentrated in a few large prints.

**"Screen liquidity is real liquidity."** The order book you see is not the full picture. Much resting liquidity is hidden (iceberg orders, dark pools in equities/FX). Conversely, displayed liquidity can evaporate instantly as passive market makers cancel quotes in fast markets.

**"Liquid markets stay liquid."** Liquidity is conditional. The 2010 Flash Crash, 2014 Treasury flash crash, and 2019 repo crisis all demonstrated that even the most liquid markets can become temporarily illiquid.

## Sources

- Kyle, Albert, "Continuous Auctions and Insider Trading" (1985, Econometrica)
- Amihud, Yakov, "Illiquidity and Stock Returns" (2002, Journal of Financial Markets)
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003)
