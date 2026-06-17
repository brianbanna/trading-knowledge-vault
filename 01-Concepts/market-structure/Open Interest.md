---
aliases: [OI, Open Positions, Outstanding Contracts]
tags:
  - "#microstructure"
date-added: "2026-06-18"
---

# Open Interest

## Definition
Open interest is the total number of [[Futures Contract]] or [[Option]] contracts that are currently open, meaning they have been entered into and not yet closed out, exercised, or delivered. Think of it as the count of live bets still on the table for a given contract. It rises by 1 when a new buyer and a new seller come together to create a fresh contract, and it falls by 1 when an existing buyer and an existing seller both exit. Technically it is a stock measure, a snapshot of accumulated exposure at a point in time, not a flow. This makes it fundamentally different from [[Volume]], which counts trading activity during a session.

## Why it matters (commodities and FX)
Open interest tells you how much real capital is committed to a contract month, which is a direct read on [[Liquidity]] and depth. In commodities, a contract month with high OI is where producers, consumers, and speculators concentrate, so fills are cleaner and spreads tighter. Combined with price direction, OI reveals whether a move is funded by new conviction or just by traders unwinding old positions. It also feeds the [[COT Positioning]] report, the primary lens for gauging whether commercials or speculators are crowded on one side.

## Concrete example
**Concrete:** Take [[WTI Crude Oil]] front month futures. On day 1, OI sits at 300,000 contracts with price at $78. Over the next week WTI rallies to $84. Win read: OI climbs to 340,000 alongside the rally. New money is opening fresh [[Long]] positions, so the uptrend has fresh conviction behind it and is more likely to hold. Fail read: instead, WTI rallies the same $6 to $84 but OI falls to 270,000. Here the move is driven by [[Short]] sellers buying back to close, called short covering. Once the trapped shorts are flushed out, the buying pressure evaporates, and the rally is far more likely to stall or reverse because no new committed buyers stepped in.

**Simplified:** Open interest counts how many contracts are still alive. Price up with OI up means new buyers are arriving, a strong trend. Price up with OI down means old sellers are just escaping, a weak move.

## Key mechanics and formulas
- New buyer + new seller open: OI increases by 1.
- Existing buyer + existing seller close: OI decreases by 1.
- New trader takes over an existing trader's [[Position]] (one opens, one closes): OI unchanged.
- Total long OI always equals total short OI. Every contract has both sides.
- Price and OI joint signal:
  - Price up + OI up = new longs, strong uptrend.
  - Price up + OI down = short covering, weak uptrend.
  - Price down + OI up = new shorts, strong downtrend.
  - Price down + OI down = long liquidation, weak downtrend.

## Prerequisites
- [[Futures Contract]]
- [[Option]]
- [[Long]] and [[Short]]
- [[Position]]

## Related concepts (learn next)
- [[Volume]] because pairing the flow measure with this stock measure is how traders confirm whether a move has real backing.
- [[Liquidity]] because high open interest is one of the clearest proxies for how easily you can enter and exit size.
- [[Futures Contract]] because OI only exists where contracts are created and destroyed, and understanding the lifecycle clarifies why the number moves.
- [[COT Positioning]] because the report decomposes open interest by trader category to show who is crowded.
- [[Front Month]] because OI concentrates in the nearest active month and migrates as contracts roll.
- [[Position]] because every unit of open interest is a live position held by someone on each side.

## Common misconceptions
- "Rising open interest is always bullish." Wrong. OI rising means new positions are opening, but they can be new shorts just as easily as new longs. You must read OI together with price direction to know which side the new money is taking.
- "Open interest and volume are the same thing." Wrong. Volume resets to 0 every session and counts trades, while OI carries over and counts live contracts. A single contract traded back and forth 10 times adds 10 to volume but can leave OI unchanged.
- "Higher OI guarantees a profitable trade." Wrong. OI measures participation and liquidity, not direction or edge. A crowded contract can still move against you.

## Sources
- CME Group, Daily Bulletin and Open Interest definitions.
- CFTC, Commitments of Traders explanatory notes.
