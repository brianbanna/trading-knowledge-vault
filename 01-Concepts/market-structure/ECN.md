---
aliases: [ECN, electronic communication network, EBS, Reuters Matching]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# ECN

## Definition
An Electronic Communication Network (ECN) is an anonymous, automated trading venue that matches buy and sell orders from multiple participants without a central dealer intermediary. The 2 dominant interbank FX ECNs are [[EBS]] (now CME Group) and [[Reuters Matching]] (now Refinitiv Matching), which together handle most interbank spot in major pairs. ECNs run a central limit order book (CLOB), matching by price time priority. Unlike [[Single Dealer Platform]]s, participants do not know who they trade with until after execution. ECNs drive [[price discovery]] in spot FX: the "true" market price is largely set on these platforms. Access was historically limited to banks and large institutions; ECN style platforms now serve hedge funds and prop firms.

## Why it matters (commodities and FX)
ECNs set interbank FX prices, which propagate to every other venue, platform, and end client. The [[bid-ask spread]] on EBS for [[EURUSD]] or [[USDJPY]] represents the tightest institutional pricing available. Commodity traders hedging FX use ECN prices as the reference for execution quality on any platform. In commodities, analogous venues (CME Globex for futures) play the same role. ECN dynamics matter for building [[transaction cost analysis]], designing execution algos, and interpreting [[tick data]]. The shift from voice to ECN trading (2000 to 2015) fundamentally changed FX market structure by enabling algorithmic market making and HFT.

## Concrete example

**Concrete:** A prop firm buys EUR 20 million EUR/USD. On EBS the book: best bid 1.08520 (10 million), next 1.08515 (15 million); best offer 1.08525 (8 million), next 1.08530 (12 million). The firm posts a limit buy at 1.08525, lifting the best offer. Fills 8 million at 1.08525; remaining 12 million either waits for new offers or, if market, sweeps to 1.08530. Execution cost roughly 0.5 pips worse than mid, vs 0.8 to 1.2 pips on a typical [[Single Dealer Platform]] with [[last look]]. The trade is visible to all ECN participants, signaling demand. A dealer on a [[Single Dealer Platform]] could have internalized invisibly. Tradeoff: better price on ECN, more [[information leakage]].

**Simplified:** An ECN is an electronic order book where banks and large traders post bids and offers anonymously. The platform matches buyers and sellers automatically by price and time. EBS and Reuters Matching are the two big FX ECNs. Their prices set the global benchmark because they aggregate liquidity from the largest banks. Tight spreads, but anyone watching the book can see your order and react to it.

## Key mechanics and formulas
- **Price time priority**: same price orders fill in submission order
- **Minimum trade size**: EBS minimum is typically 1 million base for major pairs
- **Effective spread**: 2 × |execution price − mid at execution|
- **ECN fee structure**: per million traded ($20 to $30/million)
- **Primary pair coverage**: EBS dominates USDJPY, EURUSD, EURCHF; Reuters Matching dominates Commonwealth pairs (GBPUSD, AUDUSD, NZDUSD, USDCAD)
- **Latency**: co located participants achieve sub millisecond order entry; non co located 1 to 10 ms

## Prerequisites
- [[Bid-Ask Spread]]
- [[Liquidity]]
- [[Order Book]]
- [[Price Discovery]]

## Related concepts (learn next)
- [[Single Dealer Platform]]: alternative where banks stream proprietary prices.
- [[Top of Book]]: best anonymous bid and offer on an ECN.
- [[Depth of Book]]: full ECN book reveals liquidity at every level.
- [[Last Look]]: ECNs generally do not allow it; execution is firm.
- [[Tick Data]]: ECN trade and quote data drives microstructure research.
- [[Sweep]]: aggressive orders taking liquidity across multiple ECN levels.
- [[Internalization]]: banks may internalize rather than route to an ECN.
- [[FX Fix]]: ECN volume spikes around the WMR fix window.

## Common misconceptions

**"ECNs always offer the best price."** Spreads are tight but total cost includes platform fees, and large orders face more [[market impact]] because execution is visible. A [[Single Dealer Platform]] may offer better total cost for large, information insensitive orders.

**"All ECNs are the same."** EBS and Reuters Matching have different liquidity pools and pair coverage. Wrong venue (AUDUSD on EBS) means worse execution.

**"ECN trading is fully anonymous post trade."** Pre trade anonymity is standard, but prime broker credit relationships mean the counterparty's PB identity is often known after settlement, letting sophisticated participants infer flow patterns.

## Sources
- King, Osler, Rime, "Foreign Exchange Market Structure, Players, and Evolution," Norges Bank Working Paper (2012)
- Chaboud, Chiquoine, Hjalmarsson, Vega, "Rise of the Machines: Algorithmic Trading in the Foreign Exchange Market," Journal of Finance (2014)
- BIS Markets Committee, "Electronic Trading in Fixed Income Markets" (2016)
- CME Group, "EBS Market Data and Connectivity Guide"
