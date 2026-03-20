---
aliases: [flow signals, order flow signals, flow intelligence]
tags:
  - "#microstructure"
  - "#fx"
date-added: "2026-03-20"
---

# Flow Signals

## Definition
Flow signals are predictive trading signals derived from observing the direction, size, and urgency of customer order flow before it is fully reflected in market prices. In FX markets, banks that operate [[Single Dealer Platform]]s see billions of dollars of client orders each day and can detect patterns: when multiple corporate clients are buying the same currency, when hedge funds are aggressively selling, or when central banks are intervening. This "informational edge from flow" is the primary advantage large FX dealers have over pure systematic traders. Flow signals can also be extracted from public data: [[ECN]] trade tapes allow classification of trades as buyer or seller initiated, volume imbalances reveal net directional pressure, and [[sweep]] patterns indicate aggressive informed trading. The key distinction is between proprietary flow intelligence (visible only to the bank receiving the orders) and public flow signals (derived from observable market data).

## Why it matters (commodities and FX)
Flow signals are arguably the most valuable edge in FX markets. Banks that see 10 to 15% of global FX flow (like JP Morgan or Citi) can detect macro shifts in positioning hours or days before they are reflected in price. A bank observing that 5 different sovereign wealth funds are all selling USD in the same week has a powerful directional signal. For non-bank participants, public flow signals from [[ECN]] data provide a partial substitute. In commodity markets, analogous flow intelligence comes from physical commodity traders (Vitol, Trafigura, Glencore) who see physical supply and demand flows before financial markets price them. The [[CFTC Commitments of Traders]] report provides a delayed, aggregated version of flow data for futures markets. Building flow signal models from public data is a core skill for systematic FX and commodity traders.

## Concrete example
A top-tier FX bank observes the following on a Monday morning: 3 separate Asian central banks have submitted orders to sell a combined 2 billion USD against local currencies; a large US pension fund is buying 500 million EUR for rebalancing; and 4 macro hedge funds are accumulating short USDJPY positions. The bank's flow analytics team aggregates these signals into a "USD bearish" indicator, which informs the bank's own positioning and the skew it applies to prices on its [[Single Dealer Platform]]. By Tuesday, EURUSD has risen 80 pips and USDJPY has fallen 60 pips, consistent with the flow signal. A public-data-only trader attempts to replicate this signal using [[EBS]] trade tape data: she classifies trades as buyer or seller initiated (using the Lee-Ready algorithm), computes a 1 hour rolling net buy/sell imbalance, and finds a 55% directional hit rate at a 4 hour horizon. This is profitable but substantially weaker than the bank's proprietary signal. In a failure scenario, the public flow signal gives a "buy EURUSD" reading driven by algorithmic market makers' positioning (noise), not informed directional flow, and the trade loses 30 pips over the next day.

## Key mechanics and formulas
- **Trade classification (Lee-Ready)**: if trade price > mid-price, classify as buyer-initiated; if trade price < mid-price, classify as seller-initiated; if trade price = mid-price, use tick rule (compare to previous trade)
- **Order flow imbalance**: OFI = sum of buyer-initiated volume - sum of seller-initiated volume over a window
- **Normalized flow**: NOFI = OFI / total volume; ranges from -1 (all selling) to +1 (all buying)
- **Flow impact regression**: Price change(t, t+h) = alpha + beta x OFI(t-w, t) + error; beta measures the predictive power of flow over horizon h
- **VPIN (Volume-Synchronized Probability of Informed Trading)**: VPIN = |buy volume - sell volume| / total volume, computed on volume bars; high VPIN signals elevated informed trading
- **Aggregated flow persistence**: serial correlation of OFI across 1 hour windows; persistent flow (autocorrelation > 0.3) suggests institutional accumulation

## Prerequisites
- [[Tick Data]]
- [[Top of Book]]
- [[Sweep]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Positioning Signal]]: longer-horizon aggregation of flow data reveals crowded trades and contrarian opportunities.
- [[Sweep]]: sweeps are the most visible and urgent form of directed flow on public venues.
- [[Skew Microstructure]]: order book skew is the passive counterpart to active flow signals; both predict short-term direction.
- [[Internalization]]: banks' ability to see and internalize flow is the source of their informational advantage.
- [[FX Fix]]: fix-related flow is the most predictable and well-studied flow pattern.
- [[Single Dealer Platform]]: the venue through which banks observe proprietary client flow.
- [[CTA]]: trend-following CTAs generate persistent directional flow that banks can detect and trade around.
- [[Depth of Book]]: flow pressure is reflected in depth depletion on one side of the book.

## Common misconceptions
1. **"Public flow signals are as good as proprietary flow"**: Banks with large client bases see the direction, size, identity, and urgency of orders before they reach the market. Public flow signals from ECN trade tapes capture only a fraction of this information and with a delay.
2. **"Flow always predicts future price movement"**: Some flow is purely mechanical (index rebalancing, option delta hedging) and has zero predictive content beyond the immediate impact. Distinguishing informative from non-informative flow is the critical challenge.
3. **"The CFTC Commitments of Traders report is real-time flow data"**: The COT report is published weekly with a 3 day lag and shows only net futures positioning, not flow direction or urgency. It is useful for longer-horizon [[positioning signal]]s but useless for intraday or daily flow trading.

## Sources
- Evans, Martin D.D., Lyons, Richard K., "Order Flow and Exchange Rate Dynamics," Journal of Political Economy (2002)
- Lyons, Richard K., "The Microstructure Approach to Exchange Rates," MIT Press (2001)
- Easley, David, de Prado, Marcos Lopez, O'Hara, Maureen, "Flow Toxicity and Liquidity in a High-Frequency World," Review of Financial Studies (2012)
- King, Osler, Rime, "Foreign Exchange Market Structure, Players, and Evolution," Norges Bank Working Paper (2012)
