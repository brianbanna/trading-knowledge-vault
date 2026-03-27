---
aliases: [stale quote, stale price, outdated quote]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Stale Quote

## Definition
A stale quote is a price that has not been updated and no longer reflects the current market. It happens when the market moves but a market maker's resting order or streamed price lags behind. The quote was valid when it was posted but is now mispriced relative to the true [[Mid Price]]. Stale quotes are guaranteed losing trades for the quoter because any counterparty who trades against them is getting a better price than the market currently offers. In electronic markets, quotes become stale in milliseconds. In voice markets, a quote might go stale in seconds or minutes. The latency between a market event and a quote update is the window of vulnerability.

## Why it matters (commodities and FX)
In FX, stale quotes are the primary source of [[Sniping]] losses. When the ECB announces a rate decision, EUR/USD can move 50 pips in 100 milliseconds. Any dealer whose quote update takes 150 milliseconds has a 50 millisecond window where their quote is stale and vulnerable. In commodities, stale quotes arise when correlated instruments move first: if WTI crude jumps on an EIA inventory report, a dealer still showing the old Brent quote is stale by the WTI/Brent spread relationship. Managing quote staleness through faster systems, wider spreads during events, and [[Last Look]] is essential for survival as a market maker.

## Concrete example
I am making a market in Brent crude futures, quoting $82.50 / $82.54. The EIA weekly petroleum status report drops at 10:30 AM ET showing a larger than expected drawdown.

**Fail scenario (my quote goes stale):** WTI jumps $0.40 within 200 milliseconds of the release. The fair Brent price, given the WTI move and the historical correlation, should be approximately $82.90. But my quoting engine takes 350 milliseconds to process the WTI move and update the Brent quote. For 150 milliseconds, my $82.54 offer is stale by $0.36. A fast algorithm lifts my offer at $82.54. I am now short at $82.54 when the market is $82.90. Loss: $0.36 per barrel. On 20 lots of 1000 barrels, that is $7,200 from a single stale quote.

**Win scenario (proper staleness management):** I configure my system to pull quotes 50 milliseconds before any scheduled data release (EIA, API, OPEC). My quotes go dark for 500 milliseconds. The [[Sniping|sniper]] has nothing to hit. After I see the new WTI level, I requote Brent at $82.86 / $82.94 (wider spread to compensate for post news uncertainty). I resume quoting safely.

## Key mechanics and formulas
- **Staleness window** = Time(market event) minus Time(quote update). Any positive value means the quote is stale during that interval
- **Maximum stale quote loss** = Price move during staleness window x Size shown. This is the worst case loss per stale fill
- **Stale quote probability** increases with: slower systems, more correlated instruments, scheduled data releases, high volatility regimes
- **Quote to trade ratio:** A high ratio of quote updates to fills means the quoter is updating fast enough to avoid staleness. A low ratio means quotes are sitting too long
- **Pull to post interval:** The time between pulling a stale quote and posting a fresh one. Minimizing this reduces the period of zero liquidity provision

## Prerequisites
- [[Quote]]
- [[Mid Price]]
- [[Bid-Ask Spread]]
- [[Top of Book]]

## Related concepts (learn next)
- [[Sniping]] , the strategy of deliberately hitting stale quotes for risk free profit
- [[Adverse Selection]] , stale quotes are the most extreme form of adverse selection (the counterparty knows with certainty)
- [[Last Look]] , allows the quoter to reject fills on quotes that went stale between the request and the fill
- [[Latency]] , the root cause of staleness in electronic markets
- [[Two Way Price]] , a stale two way price has both sides mispriced
- [[Toxic Flow]] , stale quote exploitation creates the most toxic flow profiles
- [[Market Impact]] , the price move that makes a quote stale

## Common misconceptions
1. **"Stale quotes only matter in HFT."** Voice commodity brokers also deal with stale quotes. If a broker quotes gold at $2,340 over the phone and the client takes 5 seconds to respond, the quote may be stale by that time. The timescale differs, but the principle is identical.
2. **"Last Look fully solves the staleness problem."** [[Last Look]] helps but is imperfect. Some clients route flow specifically to venues without last look. Regulators are scrutinizing last look practices. And in futures markets (CME, ICE), there is no last look at all. Resting limit orders are firm.
3. **"Faster technology eliminates stale quotes."** Faster technology reduces the staleness window but never eliminates it. There will always be events (flash crashes, fat finger trades, geopolitical shocks) that move the market faster than any system can react. Risk management must assume some stale fills will occur.
4. **"Only my own quotes go stale."** If I am a price taker, the quotes I see on the screen can also be stale. An offer that looked available 50 milliseconds ago may already be filled by the time my order reaches the exchange. This is a form of [[Slippage]].

## Sources
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- Budish, Cramton, Shim. "The High Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response," *Quarterly Journal of Economics*, 2015
- CME Group, "Market Data and Latency"
