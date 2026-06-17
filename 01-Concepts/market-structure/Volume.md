---
aliases: [Trading Volume, Traded Contracts, Turnover Count]
tags:
  - "#microstructure"
date-added: "2026-06-18"
---

# Volume

## Definition
Volume is the number of contracts traded during a defined period, usually a single trading session. Each time a buyer and a seller transact, that quantity is added to the day's tally. It is a flow measure: it accumulates through the session and resets to 0 when the next session opens. This is the key contrast with [[Open Interest]], which is a stock measure that carries forward and counts live contracts rather than activity. Volume tells you how busy a market was, not how much exposure is still outstanding.

## Why it matters (commodities and FX)
Volume is the primary confirmation tool for any price move. A breakout or trend backed by heavy volume reflects broad participation and conviction, while the same move on thin volume signals that few traders agree and the move is prone to reversal. In commodities, volume also marks [[Liquidity]]: the active [[Front Month]] carries the bulk of daily volume, which is where you get the tightest fills. Traders watch volume spikes around economic releases, inventory reports, and option expiries because they flag where real flow concentrated.

## Concrete example
**Concrete:** Take [[Copper Futures]] (CME, 25,000 lb per contract). Copper has coiled between $4.10 and $4.20 per lb for two weeks. On Tuesday it breaks above $4.20 to settle at $4.24. Win read: that session prints 95,000 contracts of volume against a 20 day average of 55,000. The breakout is confirmed. Heavy participation means many buyers committed at the new level, so the move is more likely to extend. Fail read: instead, copper pokes above $4.20 to $4.24 but volume is only 28,000, roughly half the average. The breakout is suspect. With so few buyers behind it, there is no real demand at the new price, and copper slides back into the range within a day or two, trapping the breakout buyers.

**Simplified:** Volume counts how many contracts changed hands today. A price move on big volume means lots of traders agree, so it tends to hold. The same move on small volume means almost nobody participated, so it often reverses.

## Key mechanics and formulas
- Each transaction adds its contract quantity to the session total. One trade of 50 contracts adds 50.
- Volume resets to 0 at the start of each session; [[Open Interest]] does not.
- Volume vs OI combinations:
  - Price up + volume up + OI up = strong, well supported uptrend (new committed longs).
  - Price up + volume down = move losing participation, suspect.
  - Price up + volume up + OI down = active short covering, can spike then fade.
  - Range break + volume above average = confirmed; range break on thin volume = likely false.

## Prerequisites
- [[Futures Contract]]
- [[Open Interest]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Open Interest]] because pairing this flow measure with the stock of live contracts is the core of reading whether new money is behind a move.
- [[Liquidity]] because volume is the most direct observable proxy for how much size a market can absorb without slippage.
- [[Futures Contract]] because volume is reported per contract and per month, and you need to know how contracts trade to read it.
- [[Turnover]] because turnover scales volume by price or value, giving a notional sense of how much capital actually changed hands.
- [[Front Month]] because volume migrates between months as contracts roll, and tracking it tells you which month is genuinely active.

## Common misconceptions
- "High volume means the price will go up." Wrong. Volume is direction agnostic. Heavy selling produces high volume too. Volume confirms the strength of whatever move is happening, not its sign.
- "Volume and open interest measure the same activity." Wrong. The same 100 contracts traded back and forth all day inflate volume while leaving open interest flat. Volume counts trades, OI counts surviving positions.
- "Low volume sessions are safe to ignore." Wrong. Thin volume itself is information: it warns that moves are fragile, spreads are wider, and false breakouts are more likely, which matters for sizing and execution.

## Sources
- CME Group, daily volume and open interest reports.
- John Murphy, Technical Analysis of the Financial Markets, volume confirmation principles.
