---
aliases: [markout, mark-out, post-trade price movement, markout analysis]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Markout

## Definition
A markout is the price movement after a trade, measured over a fixed time horizon. Sell EUR/USD at 1.1000, [[Mid Price]] 10s later is 1.0995: 10 second markout is +5 pips (favorable). If mid moved to 1.1005: markout is -5 pips (unfavorable, counterparty was right). Markout analysis is the primary tool for evaluating execution quality, flow toxicity, and market making profitability. Positive markouts mean consistent good prices. Negative markouts mean adverse selection. Horizon matters: a trade can have positive 1s markout but negative 60s markout, indicating short term noise but medium term [[Adverse Selection]].

## Why it matters (commodities and FX)
In FX, every major dealing desk runs markout analysis on every fill, segmented by client, venue, time of day, and instrument. Markouts drive [[Client Tiering|spread tiering]], [[Last Look]] calibration, and venue selection. In commodities, markouts on Brent, WTI, gold, and copper reveal whether broker flow is predominantly informed or uninformed. A market making desk that does not track markouts cannot distinguish a good month (skill) from a lucky month (favorable flow mix).

## Concrete example

**Concrete:** Market making WTI crude on CME. Sell 50 lots at $78.20, mid $78.18. Positive markout: 30s later mid is $78.15. Markout $78.20 - $78.15 = +$0.05/bbl. Sold above where market went. 50 x 1000 x $0.05 = $2,500 markout profit. Buyer was uninformed. Negative markout: 30s later mid is $78.35. Markout = -$0.15/bbl. Loss: 50 x 1000 x $0.15 = $7,500. Buyer was informed, perhaps saw a pipeline disruption headline 200ms before me. [[Toxic Flow]]. Markout curve plotted at 1s, 5s, 30s, 60s, 300s. Negative at 1s flattening by 60s = counterparty had latency edge ([[Sniping]]). Markout keeps worsening to 300s = counterparty had fundamental information.

**Simplified:** Right after a trade, watch where the price goes. If it moves your way, the trade was good for you. If it moves against you, the counterparty was better informed. Do this for every fill and average it. That number tells you if the flow you trade against is profitable or expensive.

## Key mechanics and formulas
- **Markout at horizon T** = Side x (Mid_T - Trade Price), Side = +1 for buy, -1 for sell
- **Markout from mid** = Side x (Mid_T - Mid_0), isolates post trade movement, removes spread earned
- **Average markout** = sum of markouts / number of trades, per client, per venue, per instrument
- **Break even markout horizon:** point where markout curve crosses from positive to negative. Markout +1 pip at 1s but -2 pips at 60s: flatten inventory before that horizon
- **Spread earned** = |Trade Price - Mid_0|, close to [[Half Spread]]
- **Net P&L per trade** = Spread earned + Markout at horizon T

## Prerequisites
- [[Mid Price]]
- [[Bid-Ask Spread]]
- [[Adverse Selection]]
- [[Quote]]

## Related concepts (learn next)
- [[Toxic Flow]] , flow with persistently negative markouts
- [[Client Tiering]] , adjusting spreads based on markout data per client
- [[Last Look]] , using markout signal in first ms to accept or reject a fill
- [[Half Spread]] , spread earned offsetting markout losses
- [[Market Impact]] , broader concept markouts measure at granular level
- [[Slippage]] , pre trade benchmark cost, complementary to markout's post trade measure
- [[VPIN]] , volume based informed trading probability metric
- [[Flow Signals]] , aggregating markout patterns into direction signals

## Common misconceptions
1. **"Positive markout means profitable trade."** Markout measures post trade movement only; total P&L includes spread earned. -0.3 pips markout with 0.5 pips [[Half Spread]] still nets +0.2 pips. Only markouts more negative than half spread are net losers.
2. **"One horizon tells the whole story."** A trade can look great at 1s and terrible at 5 min. Need the full markout curve. Short horizons capture latency arb, long horizons capture fundamental asymmetry.
3. **"Markout analysis needs HF data."** A voice commodities broker quoting gold by phone can compute markouts. Measure mid 5 min and 30 min after each fill. Longer horizon, same analysis.
4. **"Negative markout always means informed counterparty."** Sometimes the market just moved. Significance matters. 500 trades averaging -3 pips with t-stat > 2 is meaningful. One bad trade is noise.

## Sources
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- CME Group, "Transaction Cost Analysis in Futures Markets"
- Bershova, N. and Rakhlin, D. "High Frequency Trading and Long Term Investors: A View from the Buy Side," *Journal of Investment Strategies*
