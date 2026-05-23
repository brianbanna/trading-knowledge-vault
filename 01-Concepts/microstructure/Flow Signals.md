---
aliases: [flow signals, order flow signals, flow intelligence]
tags:
  - "#microstructure"
  - "#fx"
date-added: "2026-03-20"
---

# Flow Signals

## Definition
Flow signals are predictive trading signals derived from observing the direction, size, and urgency of customer order flow before it is fully reflected in market prices. Banks operating [[Single Dealer Platform]]s see billions of dollars of client orders each day and detect patterns: multiple corporates buying the same currency, hedge funds aggressively selling, or central banks intervening. This informational edge from flow is the primary advantage large FX dealers have over pure systematic traders. Flow signals also come from public data: [[ECN]] trade tapes allow classification as buyer or seller initiated, volume imbalances reveal net pressure, and [[sweep]] patterns indicate aggressive informed trading. Distinguish proprietary flow intelligence (visible only to the receiving bank) from public flow signals (derived from observable market data).

## Why it matters (commodities and FX)
Flow signals are arguably the most valuable edge in FX. Banks seeing 10 to 15% of global FX flow (JP Morgan, Citi) detect macro positioning shifts hours or days before they are priced. A bank observing 5 sovereign wealth funds all selling USD in one week has a powerful directional signal. For non bank participants, public flow signals from [[ECN]] data provide a partial substitute. In commodities, analogous intelligence comes from physical traders (Vitol, Trafigura, Glencore) who see physical supply demand before financial markets price it. The [[CFTC Commitments of Traders]] report gives a delayed, aggregated version for futures. Building flow signal models from public data is core for systematic FX and commodity traders.

## Concrete example

**Concrete:** Top tier FX bank, Monday morning. 3 Asian central banks submit orders to sell 2B USD combined. US pension fund buys 500M EUR for rebalancing. 4 macro funds accumulate short USDJPY. Flow analytics aggregates into a USD bearish indicator, informing the bank's own positioning and the skew applied on its SDP. By Tuesday, EURUSD up 80 pips and USDJPY down 60 pips, consistent with the signal. Public data trader tries to replicate using EBS tape: Lee Ready trade classification, 1 hour rolling net imbalance, finds 55% directional hit rate at 4 hour horizon. Profitable but weaker. Failure case: public signal gives buy EURUSD reading driven by algo maker positioning (noise) not informed flow, loses 30 pips next day.

**Simplified:** Flow signals are reading what big customers are doing in real time and trading on that. If you see 5 large funds all selling the same currency, the currency probably drops next. Banks see this directly because customers trade through them. Outsiders try to reconstruct flow from public trade tapes, which works but is weaker.

## Key mechanics and formulas
- **Trade classification (Lee Ready)**: trade price > mid = buyer initiated; < mid = seller initiated; = mid = use tick rule (compare to previous trade)
- **Order flow imbalance**: OFI = sum buyer initiated volume - sum seller initiated volume over a window
- **Normalized flow**: NOFI = OFI / total volume; -1 (all selling) to +1 (all buying)
- **Flow impact regression**: Price change(t, t+h) = alpha + beta x OFI(t-w, t) + error; beta measures predictive power
- **VPIN**: |buy vol - sell vol| / total vol on volume bars; high VPIN = informed trading
- **Aggregated flow persistence**: serial correlation of OFI across 1 hour windows; autocorr > 0.3 suggests institutional accumulation

## Prerequisites
- [[Tick Data]]
- [[Top of Book]]
- [[Sweep]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Positioning Signal]]: longer horizon aggregation reveals crowded trades and contrarian opportunities
- [[Sweep]]: the most visible and urgent form of directed flow on public venues
- [[Skew Microstructure]]: book skew is the passive counterpart to active flow signals
- [[Internalization]]: banks' ability to see and internalize flow is the source of their edge
- [[FX Fix]]: fix related flow is the most predictable and studied pattern
- [[Single Dealer Platform]]: venue through which banks observe proprietary client flow
- [[CTA]]: trend following CTAs generate persistent directional flow banks can detect
- [[Depth of Book]]: flow pressure shows up as depth depletion on one side

## Common misconceptions
1. **"Public flow signals match proprietary flow"**: banks see direction, size, identity, and urgency before orders hit the market. Public ECN tapes capture a fraction with delay.
2. **"Flow always predicts future price"**: some flow is purely mechanical (index rebalancing, option delta hedging) with zero predictive content beyond immediate impact. Distinguishing informative from non informative flow is the challenge.
3. **"The CFTC COT report is real time flow"**: COT is published weekly with 3 day lag, showing only net futures positioning, not direction or urgency. Useful for longer horizon [[positioning signal]]s, useless for intraday flow trading.

## Sources
- Evans, Martin D.D., Lyons, Richard K., "Order Flow and Exchange Rate Dynamics," Journal of Political Economy (2002)
- Lyons, Richard K., "The Microstructure Approach to Exchange Rates," MIT Press (2001)
- Easley, David, de Prado, Marcos Lopez, O'Hara, Maureen, "Flow Toxicity and Liquidity in a High-Frequency World," Review of Financial Studies (2012)
- King, Osler, Rime, "Foreign Exchange Market Structure, Players, and Evolution," Norges Bank Working Paper (2012)
