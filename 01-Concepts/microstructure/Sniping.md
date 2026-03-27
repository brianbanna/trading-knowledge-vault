---
aliases: [sniping, latency arbitrage, quote sniping, stale quote sniping]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Sniping

## Definition
Sniping is trading against someone's [[Stale Quote]] for a guaranteed or near guaranteed profit. The sniper detects that a market maker's price has not been updated after a price moving event and hits the stale price before the maker can cancel or update it. This is a form of [[Adverse Selection]] where the information advantage is not about fundamental value but about speed: the sniper processes the event faster than the quoter updates. In electronic markets, sniping races play out in microseconds. The sniper's edge is the latency difference between detecting the event and the quoter refreshing the price.

## Why it matters (commodities and FX)
In FX, sniping is a major cost for dealers streaming prices on [[ECN|ECNs]] like EBS and Refinitiv Matching. When US nonfarm payrolls are released, EUR/USD can move 30 to 80 pips in under a second. Any resting limit order that is not cancelled within the first 50 milliseconds is a sniping target. In commodities, cross market sniping is common: a fast trader sees WTI move on CME and immediately hits a Brent quote on ICE that has not yet adjusted. The annual cost of sniping to market makers is estimated in the hundreds of millions across major FX pairs. This is why market makers invest heavily in latency reduction and why [[Last Look]] exists.

## Concrete example
EUR/USD is trading at 1.1000 mid. US CPI comes in hotter than expected at 08:30 ET. The dollar should strengthen, and EUR/USD should drop approximately 40 pips.

**Sniper's win scenario:** My system detects the CPI print via a direct data feed 5 milliseconds after release. I see a market maker on EBS still showing a 1.0999 bid (posted before the release). I sell 5 million EUR at 1.0999. Within 200 milliseconds, the market prints 1.0960. I cover my short at 1.0960. Profit: 39 pips on 5 million = $19,500 on a single trade. The market maker's quote was stale by 40 pips for approximately 50 milliseconds, and I captured nearly all of it.

**Sniper's fail scenario:** I try the same trade, but the market maker has co located servers and cancels the 1.0999 bid 3 milliseconds after the CPI release, before my sell order arrives. My order hits empty air. No fill, no profit. Or worse, I sell at a price that turns out to be fair because the initial CPI reaction reverses. Sniping only works when the price move is real and the quote is genuinely stale.

**Market maker's defense:** I pull all quotes 100 milliseconds before the 08:30 scheduled release. I requote at 1.0958 / 1.0966 (wider spread) at 08:30:00.300, only after confirming the new equilibrium. I sacrifice 300 milliseconds of quoting time but avoid any sniping losses.

## Key mechanics and formulas
- **Sniping profit** = |True Price minus Stale Quote| x Size. This is the guaranteed edge per sniped fill
- **Sniping window** = Time(event) to Time(quote refresh). The longer this window, the more vulnerable the quoter is
- **Sniping probability** = P(sniper arrives before quote refresh). Depends on relative latencies of sniper and quoter
- **Annual sniping cost** = Sum over all stale fills of |Fill Price minus Fair Price at fill time| x Size
- **Latency race:** Sniper latency < Quoter latency implies sniping is possible. Both sides invest in co location, FPGA hardware, and microwave networks to win the race
- **Cross asset sniping:** Fair value of Asset B = f(Asset A). If Asset A moves and quoter has not updated Asset B, the sniper trades Asset B at the old price. Common pairs: WTI/Brent, gold/silver, EUR/USD vs EUR futures

## Prerequisites
- [[Stale Quote]]
- [[Adverse Selection]]
- [[Mid Price]]
- [[Top of Book]]

## Related concepts (learn next)
- [[Stale Quote]] , the vulnerability that sniping exploits
- [[Last Look]] , the market maker's defense mechanism that allows rejecting sniped fills
- [[Latency]] , the root cause of the speed differential that enables sniping
- [[Toxic Flow]] , sniping produces the most toxic markout profiles
- [[Markout]] , sniped trades show immediately negative markouts at all horizons
- [[ECN]] , anonymous venues where sniping is most prevalent due to no [[Last Look]]
- [[Market Impact]] , the event that makes the quote stale and creates the sniping opportunity
- [[Frequent Batch Auctions]] , a proposed market design that eliminates sniping by batching orders

## Common misconceptions
1. **"Sniping is illegal."** Sniping on public information (economic releases, price moves in correlated instruments) is entirely legal. It is simply fast trading. Inside information is a different matter, but sniping as commonly practiced in FX and futures uses only publicly available data processed faster.
2. **"Only HFT firms snipe."** Any trader who recognizes a stale price can snipe. A voice commodities trader who sees WTI jump on a headline and immediately calls an LME broker to buy copper (because the broker has not adjusted yet) is sniping at a human timescale.
3. **"Co location eliminates sniping risk."** Co location reduces latency but does not eliminate the race. A co located market maker still faces co located snipers. The race moves from milliseconds to microseconds, but the dynamic persists. The structural solution is [[Last Look]] (in OTC) or [[Frequent Batch Auctions]] (proposed for exchanges).
4. **"Sniping is risk free."** Near risk free, not perfectly risk free. The initial price reaction can reverse (a "false break"). If I snipe EUR/USD on a CPI print and the number gets revised 30 seconds later, I could lose. The edge is probabilistic, not certain.

## Sources
- Budish, Cramton, Shim. "The High Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response," *Quarterly Journal of Economics*, 2015
- Aquilina, Budish, O'Neill. "Quantifying the High Frequency Trading Arms Race," *Quarterly Journal of Economics*, 2022
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
