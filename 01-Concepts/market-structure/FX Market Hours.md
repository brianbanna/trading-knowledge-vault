---
aliases: [FX market hours, forex sessions, trading sessions]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# FX Market Hours

## Definition
The FX market operates 24 hours a day, 5 days a week, rotating through 4 major sessions: Sydney, Tokyo, London, New York. Each session matches the business hours of its region's major financial centers. Unlike equity markets with a single opening and closing bell, FX trading migrates from one time zone to the next. Liquidity is not uniform: it peaks during the [[London]] and [[New York]] overlap (roughly 13:00 to 17:00 UTC) when both the world's largest and second largest FX centers are active. Sunday evening Sydney open marks the weekly restart; Friday NY close marks the weekly shutdown. Session timing matters because [[spread]], [[volatility]], and [[slippage]] vary dramatically by hour.

## Why it matters (commodities and FX)
Session timing directly affects execution quality. A [[EURUSD]] trade in Tokyo session faces wider [[bid-ask spread]]s and thinner [[depth of book]] than the same trade during London/NY overlap. Commodity currencies like [[AUDUSD]] and [[NZDUSD]] see tightest spreads during Sydney/Tokyo overlap when local participants are most active. [[Energy]] and [[metals]] futures on London and NY exchanges create cross asset flows concentrating during those sessions, making London/NY overlap the highest volume window for both FX and commodities. Systematic traders must account for session transitions when scheduling [[TWAP]] and [[VWAP]] algos.

## Concrete example

**Concrete:** PM needs to sell USD 500 million USD/JPY. Tokyo session (00:00 to 09:00 UTC) gives the deepest JPY liquidity, top of book depth of 20 to 50 million on [[EBS]], spread 0.3 pips. Same order at 21:00 UTC (Sydney only) faces 1.5 to 3 pip spreads and top of book under 5 million, sweeping multiple levels for 5 to 10 pips of [[market impact]]. Failure mirror: trader assumes EURUSD is liquid in Tokyo, places a large order at 02:00 UTC and suffers 3 pips of slippage because European participants are absent and the book is thin.

**Simplified:** FX never closes during the week, but liquidity is not the same all the time. The deepest, tightest market is when London and New York are both open in the early afternoon UTC. Asian session is thinner for European pairs but deeper for JPY and Asian currencies. Trading outside the right session for your pair means wider spreads and worse fills, sometimes much worse.

## Key mechanics and formulas
- **Session times (approximate UTC):**
  - Sydney: 22:00 to 07:00
  - Tokyo: 00:00 to 09:00
  - London: 08:00 to 17:00
  - New York: 13:00 to 22:00
- **Overlap windows:**
  - Tokyo/London: 08:00 to 09:00 UTC
  - London/NY: 13:00 to 17:00 UTC (highest global liquidity)
- **Intraday volatility** follows a U shape within each session, with spikes at session opens
- **Liquidity score** (heuristic): Liquidity = (number of active centers) × (average quote depth at top of book)

## Prerequisites
- [[Bid-Ask Spread]]
- [[Liquidity]]
- [[Time Zone]]
- [[Market Microstructure]]

## Related concepts (learn next)
- [[FX Fix]]: 4PM London benchmark creates predictable flow during London/NY overlap.
- [[ECN]]: primary electronic venues where interbank liquidity concentrates during peak hours.
- [[Top of Book]]: best bid/offer size varies by session.
- [[Depth of Book]]: deepest during London/NY overlap.
- [[Volatility Smile]]: option implied vols embed session specific expectations.
- [[TWAP]]: time weighted execution algos must be session aware.
- [[Slippage]]: rises sharply outside major sessions.

## Common misconceptions

**"24 hour means always liquid."** Outside London and NY sessions, liquidity for G10 pairs like EURUSD can be 80% thinner. Trading "off hours" is a common slippage source.

**"Tokyo is only for JPY pairs."** Tokyo provides reasonable liquidity for AUDUSD, NZDUSD, and Asian [[emerging market]] currencies.

**"The Sunday open is a normal session."** The Sydney open Sunday is extremely thin, gaps common. Holding positions over the weekend exposes traders to gap risk that cannot be hedged.

## Sources
- Bank for International Settlements, "Triennial Central Bank Survey" (2022)
- Chaboud, Chiquoine, Hjalmarsson, Vega, "Rise of the Machines: Algorithmic Trading in the Foreign Exchange Market," Journal of Finance (2014)
- King, Osler, Rime, "Foreign Exchange Market Structure, Players, and Evolution," Norges Bank Working Paper (2012)
