---
aliases: [FX market hours, forex sessions, trading sessions]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# FX Market Hours

## Definition
The foreign exchange market operates 24 hours a day, 5 days a week, rotating through 4 major sessions: Sydney, Tokyo, London, and New York. Each session corresponds to the business hours of its region's major financial centers. Unlike equity markets with a single opening and closing bell, FX trading simply migrates from one time zone to the next. Liquidity is not uniform across the day; it peaks during the [[London]] and [[New York]] overlap (roughly 13:00 to 17:00 UTC) when both the world's largest and second largest FX centers are active simultaneously. The Sydney open on Sunday evening (US time) marks the weekly restart, and the New York close on Friday marks the weekly shutdown. Understanding session timing is essential because [[spread]], [[volatility]], and [[slippage]] all vary dramatically by hour.

## Why it matters (commodities and FX)
Session timing directly affects execution quality. A [[EURUSD]] trade placed during the Tokyo session will face wider [[bid-ask spread]]s and thinner [[depth of book]] than the same trade during the London/NY overlap. Commodity currencies like [[AUDUSD]] and [[NZDUSD]] see their tightest spreads during the Sydney/Tokyo overlap when local participants are most active. [[Energy]] and [[metals]] futures that trade on London and New York exchanges create cross-asset flows that concentrate during those sessions, making the London/NY overlap the highest-volume window for both FX and commodities. Systematic traders must account for session transitions when scheduling [[TWAP]] and [[VWAP]] algos.

## Concrete example
A portfolio manager needs to sell 500 million USDJPY. Executing during the Tokyo session (00:00 to 09:00 UTC) gives access to the deepest JPY liquidity pool, with typical top-of-book depth of 20 to 50 million on [[EBS]]. The [[spread]] is 0.3 pips. The same order placed at 21:00 UTC (Sydney session only) faces spreads of 1.5 to 3 pips and top-of-book depth under 5 million, meaning the execution would [[sweep]] through multiple price levels, creating 5 to 10 pips of [[market impact]]. Conversely, a trader who assumed EURUSD would be liquid during Tokyo session placed a large order at 02:00 UTC and suffered 3 pips of slippage because European participants were absent and the book was thin.

## Key mechanics and formulas
- **Session times (approximate UTC):**
  - Sydney: 22:00 to 07:00
  - Tokyo: 00:00 to 09:00
  - London: 08:00 to 17:00
  - New York: 13:00 to 22:00
- **Overlap windows:**
  - Tokyo/London: 08:00 to 09:00 UTC
  - London/NY: 13:00 to 17:00 UTC (highest global liquidity)
- **Intraday volatility** follows a U-shape within each session, with spikes at session opens
- **Liquidity score** (rough heuristic): Liquidity = (number of active market centers) x (average quote depth at top of book)

## Prerequisites
- [[Bid-Ask Spread]]
- [[Liquidity]]
- [[Time Zone]]
- [[Market Microstructure]]

## Related concepts (learn next)
- [[FX Fix]]: the 4PM London benchmark creates predictable flow patterns during the London/NY overlap.
- [[ECN]] : primary electronic venues where interbank FX liquidity concentrates during peak hours.
- [[Top of Book]]: best bid/offer varies in size across sessions, directly tied to session liquidity.
- [[Depth of Book]]: the full order book is deepest during London/NY overlap.
- [[Volatility Smile]]: option implied vols embed session-specific expectations for price movement.
- [[TWAP]]: time-weighted execution algos must be session-aware to avoid poor fills.
- [[Slippage]]: execution shortfall rises sharply outside major session hours.

## Common misconceptions
1. **"24 hour means always liquid"**: While the market is technically open 24 hours, liquidity outside the London and New York sessions can be 80% thinner for G10 pairs like EURUSD. Trading "off hours" is a common source of unexpected slippage.
2. **"Tokyo is only for JPY pairs"**: Tokyo session actually provides reasonable liquidity for AUDUSD, NZDUSD, and Asian [[emerging market]] currencies, not just JPY crosses.
3. **"The Sunday open is a normal session"**: The Sydney open on Sunday is extremely thin, with gaps common. Holding positions over the weekend exposes traders to gap risk that cannot be hedged.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey" (2022)
- Chaboud, Chiquoine, Hjalmarsson, Vega, "Rise of the Machines: Algorithmic Trading in the Foreign Exchange Market," Journal of Finance (2014)
- King, Osler, Rime, "Foreign Exchange Market Structure, Players, and Evolution," Norges Bank Working Paper (2012)
