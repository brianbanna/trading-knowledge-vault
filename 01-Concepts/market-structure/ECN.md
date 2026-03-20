---
aliases: [ECN, electronic communication network, EBS, Reuters Matching]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# ECN

## Definition
An Electronic Communication Network (ECN) is an anonymous, automated trading venue that matches buy and sell orders from multiple participants without a central dealer intermediary. In FX, the 2 dominant interbank ECNs are [[EBS]] (now part of CME Group) and [[Reuters Matching]] (now Refinitiv Matching), which together handle the majority of interbank spot trading in major currency pairs. ECNs operate a central limit order book (CLOB) where participants post bids and offers, and the system matches orders by price-time priority. Unlike [[Single Dealer Platform]]s, ECN participants do not know who they are trading with until after execution. ECNs are the primary venue for [[price discovery]] in spot FX, meaning the "true" market price is largely determined on these platforms. Access was historically limited to banks and large institutions, but ECN-style platforms now serve hedge funds and proprietary trading firms.

## Why it matters (commodities and FX)
ECNs are where interbank FX prices are set, and those prices propagate to every other venue, platform, and end client. The [[bid-ask spread]] on EBS for [[EURUSD]] or [[USDJPY]] represents the tightest institutional pricing available. For commodity traders who hedge FX exposure, ECN prices serve as the reference for evaluating execution quality on any platform. In commodities, analogous electronic venues (like CME Globex for futures) perform the same price discovery function. Understanding ECN dynamics is essential for building [[transaction cost analysis]] models, designing execution algorithms, and interpreting [[tick data]]. The shift from voice-brokered to ECN-based trading (which accelerated from 2000 to 2015) fundamentally changed FX market structure by enabling algorithmic market making and high-frequency trading.

## Concrete example
A proprietary trading firm wants to buy 20 million EURUSD. On EBS, the current order book shows: best bid 1.08520 (10 million), next bid 1.08515 (15 million); best offer 1.08525 (8 million), next offer 1.08530 (12 million). The firm places a limit buy at 1.08525, lifting the best offer. It gets filled for 8 million at 1.08525, then the remaining 12 million either waits for new offers or, if sent as a market order, sweeps to 1.08530. The total execution cost is roughly 0.5 pips worse than mid, compared to 0.8 to 1.2 pips on a typical [[Single Dealer Platform]] with [[last look]]. However, the trade is immediately visible to all ECN participants, signaling demand. A dealer on a [[Single Dealer Platform]] could have internalized the same trade invisibly. The tradeoff: better price on ECN but more [[information leakage]].

## Key mechanics and formulas
- **Price-time priority**: orders at the same price are filled in the order they were submitted
- **Minimum trade size**: EBS minimum is typically 1 million in base currency for major pairs
- **Effective spread**: Effective spread = 2 x |execution price - mid price at time of execution|
- **ECN fee structure**: typically a per-million fee (e.g., $20 to $30 per million traded)
- **Primary pair coverage**: EBS dominates USDJPY, EURUSD, EURCHF; Reuters Matching dominates Commonwealth pairs (GBPUSD, AUDUSD, NZDUSD, USDCAD)
- **Latency**: co-located participants achieve sub-millisecond order entry; non-co-located participants face 1 to 10 milliseconds

## Prerequisites
- [[Bid-Ask Spread]]
- [[Liquidity]]
- [[Order Book]]
- [[Price Discovery]]

## Related concepts (learn next)
- [[Single Dealer Platform]]: the alternative venue model where banks stream proprietary prices to clients.
- [[Top of Book]]: on an ECN, the top of book is the best anonymous bid and offer available.
- [[Depth of Book]]: the full ECN order book reveals available liquidity at every price level.
- [[Last Look]]: ECNs generally do not allow last look; execution is firm, unlike many SDPs.
- [[Tick Data]]: ECN trade and quote data is the primary source for microstructure research.
- [[Sweep]]: aggressive orders that take liquidity across multiple ECN price levels.
- [[Internalization]]: banks may choose to internalize flow rather than routing it to an ECN.
- [[FX Fix]]: ECN volume spikes dramatically during the WMR fix window.

## Common misconceptions
1. **"ECNs always offer the best price"**: While ECN spreads are tight, the total cost includes platform fees, and large orders may face more [[market impact]] on ECNs because execution is visible to all participants. A [[Single Dealer Platform]] may offer better total cost for large, information-insensitive orders.
2. **"All ECNs are the same"**: EBS and Reuters Matching have very different liquidity pools and pair coverage. Using the wrong ECN for a given pair (e.g., trading AUDUSD on EBS instead of Reuters Matching) will result in worse execution.
3. **"ECN trading is fully anonymous post-trade"**: While pre-trade anonymity is standard, prime broker credit relationships mean that the counterparty's prime broker identity is often known after settlement, allowing sophisticated participants to infer flow patterns.

## Sources
- King, Osler, Rime, "Foreign Exchange Market Structure, Players, and Evolution," Norges Bank Working Paper (2012)
- Chaboud, Chiquoine, Hjalmarsson, Vega, "Rise of the Machines: Algorithmic Trading in the Foreign Exchange Market," Journal of Finance (2014)
- BIS Markets Committee, "Electronic Trading in Fixed Income Markets" (2016)
- CME Group, "EBS Market Data and Connectivity Guide"
