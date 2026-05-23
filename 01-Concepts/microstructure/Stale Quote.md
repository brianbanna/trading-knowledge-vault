---
aliases: [stale quote, stale price, outdated quote]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Stale Quote

## Definition
A stale quote is a price that has not been updated and no longer reflects the current market. It happens when the market moves but a maker's resting order or streamed price lags behind. The quote was valid when posted but is now mispriced vs the true [[Mid Price]]. Stale quotes are guaranteed losing trades for the quoter because any counterparty trading against them gets a better price than the market currently offers. In electronic markets, quotes become stale in milliseconds. In voice markets, in seconds or minutes. The latency between a market event and a quote update is the window of vulnerability.

## Why it matters (commodities and FX)
In FX, stale quotes are the primary source of [[Sniping]] losses. When ECB announces, EUR/USD can move 50 pips in 100ms. Any dealer with 150ms quote update has a 50ms window where the quote is stale. In commodities, stale quotes arise when correlated instruments move first: if WTI jumps on an EIA report, a dealer still showing old Brent is stale by the WTI/Brent relationship. Managing staleness via faster systems, wider spreads during events, and [[Last Look]] is essential for survival.

## Concrete example

**Concrete:** Market making Brent crude futures, quoting $82.50 / $82.54. EIA weekly petroleum report at 10:30 AM ET shows larger than expected drawdown. Failure: WTI jumps $0.40 within 200ms. Fair Brent given WTI move and historical correlation should be ~$82.90. Quoting engine takes 350ms to process WTI and update Brent. For 150ms, $82.54 offer is stale by $0.36. Fast algo lifts at $82.54. Now short at $82.54 with market at $82.90. Loss $0.36/bbl. 20 lots x 1000 bbl: $7,200 from a single stale quote. Defense: configure system to pull quotes 50ms before any scheduled release (EIA, API, OPEC). Quotes dark for 500ms. [[Sniping|Sniper]] has nothing to hit. After seeing new WTI level, requote Brent at $82.86 / $82.94 (wider for post news uncertainty). Resume safely.

**Simplified:** A stale quote is a price you forgot to update after the market moved. Anyone smart enough to spot it gets free money trading against you. Solutions: update faster, pull quotes before known events, or wait wider after the move. Voice traders face the same thing slower; the principle is identical.

## Key mechanics and formulas
- **Staleness window** = Time(event) - Time(update). Positive means stale during that interval
- **Maximum stale quote loss** = Price move during window x Size shown. Worst case per stale fill
- **Stale quote probability** rises with: slower systems, more correlated instruments, scheduled releases, high vol regimes
- **Quote to trade ratio:** high ratio of updates to fills means quoting fast enough. Low ratio means quotes sit too long
- **Pull to post interval:** time between pulling a stale quote and posting a fresh one. Minimizing reduces zero liquidity provision

## Prerequisites
- [[Quote]]
- [[Mid Price]]
- [[Bid-Ask Spread]]
- [[Top of Book]]

## Related concepts (learn next)
- [[Sniping]] , the strategy of deliberately hitting stale quotes
- [[Adverse Selection]] , stale quotes are the most extreme form (counterparty knows with certainty)
- [[Last Look]] , allows the quoter to reject fills on quotes that went stale between request and fill
- [[Latency]] , the root cause in electronic markets
- [[Two Way Price]] , a stale two way price has both sides mispriced
- [[Toxic Flow]] , stale quote exploitation creates the most toxic flow profiles
- [[Market Impact]] , the price move that makes a quote stale

## Common misconceptions
1. **"Stale quotes only matter in HFT."** Voice commodity brokers face them too. Gold quoted at $2,340 by phone with client taking 5s to respond can be stale. Timescale differs, principle is identical.
2. **"Last Look fully solves staleness."** [[Last Look]] helps but is imperfect. Some clients route to venues without it. Regulators scrutinize it. In futures (CME, ICE), there is no last look. Resting limit orders are firm.
3. **"Faster tech eliminates stale quotes."** Faster tech shrinks the window but never closes it. Some events (flash crashes, fat fingers, geopolitical shocks) move the market faster than any system reacts. Risk management must assume some stale fills.
4. **"Only my quotes go stale."** As a price taker, quotes on the screen can also be stale. An offer that looked available 50ms ago may already be filled by the time your order reaches the exchange. A form of [[Slippage]].

## Sources
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- Budish, Cramton, Shim. "The High Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response," *Quarterly Journal of Economics*, 2015
- CME Group, "Market Data and Latency"
