---
aliases: [markout, mark-out, post-trade price movement, markout analysis]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Markout

## Definition
A markout is the price movement after a trade, measured over a fixed time horizon. If I sell EUR/USD at 1.1000 and the [[Mid Price]] 10 seconds later is 1.0995, my 10 second markout is +5 pips (favorable, the market moved in my direction). If the mid moved to 1.1005, my markout is negative 5 pips (unfavorable, the counterparty was right). Markout analysis is the primary tool for evaluating execution quality, flow toxicity, and market making profitability. Positive markouts mean I am consistently trading at good prices. Negative markouts mean I am being adversely selected. The horizon matters: a trade can have a positive 1 second markout but a negative 60 second markout, indicating short term noise but medium term [[Adverse Selection]].

## Why it matters (commodities and FX)
In FX, every major dealing desk runs markout analysis on every fill, segmented by client, venue, time of day, and instrument. Markouts are how dealers decide [[Client Tiering|spread tiering]], [[Last Look]] calibration, and which [[ECN|venues]] to provide liquidity on. In commodities, markouts on Brent, WTI, gold, and copper futures reveal whether a broker's flow is predominantly informed or uninformed. A market making desk that does not track markouts cannot distinguish between a good month (skill) and a lucky month (favorable flow mix).

## Concrete example
I am making markets in WTI crude futures on CME. I sell 50 lots at $78.20 when the mid is $78.18.

**Win scenario (positive markout):** 30 seconds later, the mid is $78.15. My 30 second markout is $78.20 minus $78.15 = +$0.05 per barrel. I sold above where the market went. On 50 lots of 1000 barrels, that is 50 x 1000 x $0.05 = $2,500 of markout profit. The buyer was uninformed.

**Fail scenario (negative markout):** 30 seconds later, the mid is $78.35. My 30 second markout is $78.20 minus $78.35 = negative $0.15 per barrel. I sold below where the market went. Loss: 50 x 1000 x $0.15 = $7,500. The buyer was informed, perhaps they saw a pipeline disruption headline 200 milliseconds before I did. This trade was [[Toxic Flow]].

**Markout curve:** I plot markouts at 1 second, 5 seconds, 30 seconds, 60 seconds, and 300 seconds. If the markout is negative at 1 second but flattens by 60 seconds, the counterparty had a short lived latency edge (likely [[Sniping]]). If the markout keeps getting more negative out to 300 seconds, the counterparty had genuine fundamental information.

## Key mechanics and formulas
- **Markout at horizon T** = Side x (Mid_T minus Trade Price), where Side = +1 for a buy, negative 1 for a sell
  - Mid_T = [[Mid Price]] at time T after the trade
  - Trade Price = actual execution price
- **Markout from mid** = Side x (Mid_T minus Mid_0), which isolates post trade price movement, removing the spread earned
- **Average markout** = Sum of markouts / Number of trades, computed per client, per venue, per instrument
- **Break even markout horizon:** The point where the markout curve crosses from positive to negative. If my markout is +1 pip at 1 second but negative 2 pips at 60 seconds, the break even is somewhere between, and I need to flatten inventory before that horizon
- **Spread earned** = |Trade Price minus Mid_0|, typically close to [[Half Spread]]
- **Net P&L per trade** = Spread earned + Markout at horizon T

## Prerequisites
- [[Mid Price]]
- [[Bid-Ask Spread]]
- [[Adverse Selection]]
- [[Quote]]

## Related concepts (learn next)
- [[Toxic Flow]] , flow with persistently negative markouts, the primary output of markout analysis
- [[Client Tiering]] , adjusting spreads based on markout data per client
- [[Last Look]] , using the markout signal in the first milliseconds to accept or reject a fill
- [[Half Spread]] , the spread earned component that offsets markout losses
- [[Market Impact]] , the broader concept of how trades move prices, which markouts measure at a granular level
- [[Slippage]] , the pre trade cost relative to a benchmark, complementary to markout's post trade measurement
- [[VPIN]] , a volume based metric that estimates the probability of informed trading
- [[Flow Signals]] , aggregating markout patterns to build signals about market direction

## Common misconceptions
1. **"Positive markout means the trade was profitable."** Markout measures post trade price movement, but total P&L also includes the spread earned. A markout of negative 0.3 pips combined with a [[Half Spread]] of 0.5 pips still yields a net profit of 0.2 pips. Only markouts more negative than the half spread are net losers.
2. **"One horizon tells the whole story."** A trade can look great at 1 second and terrible at 5 minutes. A market maker needs the full markout curve to understand the flow. Short horizon markouts capture latency arbitrage, long horizon markouts capture fundamental information asymmetry.
3. **"Markout analysis requires high frequency data."** Even a voice commodities broker quoting gold over the phone can compute markouts. Measure the mid 5 minutes and 30 minutes after each fill. The horizon is longer, but the analysis is the same.
4. **"Negative markout always means the counterparty was informed."** Sometimes the market just moved by coincidence. Statistical significance matters. A single negative markout means nothing. 500 trades with an average markout of negative 3 pips and a t statistic above 2 is meaningful.

## Sources
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- CME Group, "Transaction Cost Analysis in Futures Markets"
- Bershova, N. and Rakhlin, D. "High Frequency Trading and Long Term Investors: A View from the Buy Side," *Journal of Investment Strategies*
