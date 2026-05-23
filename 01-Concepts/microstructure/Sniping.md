---
aliases: [sniping, latency arbitrage, quote sniping, stale quote sniping]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Sniping

## Definition
Sniping is trading against someone's [[Stale Quote]] for a guaranteed or near guaranteed profit. The sniper detects that a market maker's price has not updated after a price moving event and hits the stale price before the maker can cancel. It is a form of [[Adverse Selection]] where the edge is speed, not fundamental value: the sniper processes the event faster than the quoter refreshes. In electronic markets, sniping races play out in microseconds. The sniper's edge is the latency difference between detecting the event and refreshing the price.

## Why it matters (commodities and FX)
In FX, sniping is a major cost for dealers streaming on [[ECN|ECNs]] like EBS and Refinitiv Matching. When US nonfarm payrolls release, EUR/USD can move 30 to 80 pips in under a second. Any resting limit order not cancelled within the first 50ms is a sniping target. In commodities, cross market sniping is common: a fast trader sees WTI move on CME and immediately hits a Brent quote on ICE that has not adjusted. Annual sniping cost to market makers is estimated in the hundreds of millions across major FX pairs. This is why makers invest heavily in latency reduction and why [[Last Look]] exists.

## Concrete example

**Concrete:** EUR/USD at 1.1000 mid. US CPI prints hotter than expected at 08:30 ET. EUR/USD should drop ~40 pips. Sniper win: system detects CPI 5ms after release. Sees a market maker on EBS still showing 1.0999 bid (posted before release). Sells 5M EUR at 1.0999. Within 200ms, market prints 1.0960. Covers short at 1.0960. Profit: 39 pips on 5M = $19,500 single trade. Sniper fail: maker has colocated servers and cancels 1.0999 bid 3ms after CPI, before the sell order arrives. Order hits empty air. Maker defense: pull all quotes 100ms before scheduled 08:30 release. Requote at 1.0958 / 1.0966 (wider) at 08:30:00.300, after confirming new equilibrium. Sacrificed 300ms of quoting time, avoided sniping losses.

**Simplified:** A big number drops. The market jumps. A slow market maker still has their old quote on the screen. A faster trader hits that stale quote at the old price and immediately offsets at the new market. Risk free profit equal to the move size. Makers protect themselves by pulling quotes before known releases and updating faster than the snipers.

## Key mechanics and formulas
- **Sniping profit** = |True Price - Stale Quote| x Size. Guaranteed edge per sniped fill
- **Sniping window** = Time(event) to Time(quote refresh). Longer = more vulnerable
- **Sniping probability** = P(sniper arrives before refresh). Depends on relative latencies
- **Annual sniping cost** = sum over stale fills of |Fill Price - Fair Price at fill| x Size
- **Latency race:** Sniper latency < Quoter latency implies sniping possible. Both invest in colocation, FPGA, microwave networks
- **Cross asset sniping:** fair value of Asset B = f(Asset A). If A moves and B not updated, sniper trades B at old price. Common pairs: WTI/Brent, gold/silver, EUR/USD vs EUR futures

## Prerequisites
- [[Stale Quote]]
- [[Adverse Selection]]
- [[Mid Price]]
- [[Top of Book]]

## Related concepts (learn next)
- [[Stale Quote]] , the vulnerability sniping exploits
- [[Last Look]] , maker defense mechanism allowing rejection of sniped fills
- [[Latency]] , root cause of the speed differential enabling sniping
- [[Toxic Flow]] , sniping produces the most toxic markout profiles
- [[Markout]] , sniped trades show immediately negative markouts at all horizons
- [[ECN]] , anonymous venues where sniping is most prevalent (no [[Last Look]])
- [[Market Impact]] , the event making the quote stale
- [[Frequent Batch Auctions]] , proposed market design eliminating sniping by batching orders

## Common misconceptions
1. **"Sniping is illegal."** Sniping on public information (economic releases, correlated instrument moves) is legal. It is fast trading. Inside information is different; sniping as practiced in FX and futures uses only public data processed faster.
2. **"Only HFT firms snipe."** Any trader who spots a stale price can snipe. A voice commodities trader seeing WTI jump on a headline and immediately calling an LME broker to buy copper (before the broker adjusts) is sniping at human timescale.
3. **"Colocation eliminates sniping risk."** Colocation cuts latency but does not eliminate the race. A colocated maker still faces colocated snipers. Race moves from ms to microseconds, dynamic persists. Structural fix is [[Last Look]] (OTC) or [[Frequent Batch Auctions]] (proposed for exchanges).
4. **"Sniping is risk free."** Near risk free, not perfectly. Initial price reaction can reverse (false break). Sniping EUR/USD on a CPI print that gets revised 30s later could lose. The edge is probabilistic, not certain.

## Sources
- Budish, Cramton, Shim. "The High Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response," *Quarterly Journal of Economics*, 2015
- Aquilina, Budish, O'Neill. "Quantifying the High Frequency Trading Arms Race," *Quarterly Journal of Economics*, 2022
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
